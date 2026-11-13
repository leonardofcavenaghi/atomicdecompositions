"""A bounded, durable producer/consumer queue inside each localization tree.

The producer emits exact canonical UNMARKED keys. Consumers claim disjoint
batches, evaluate every marking orbit locally, and atomically publish the keys
with their exact contribution. A cancelled batch is requeued. The producer
counts towards the process limit; no growing list of decorations lives in RAM.
"""
from contextlib import closing
import copy
from fractions import Fraction
import hashlib
import json
import multiprocessing
import os
from pathlib import Path
import sqlite3
import time
import traceback

from . import tree_parallel as tp
from .decoration_groups import DecorationGroups
from . import marking_evaluation
from .marking_evaluation import evaluate_key

BATCH=32
BACKLOG=1024
PRODUCER_BATCH=128
# Only this exact predecessor has been checked for arithmetic equivalence.
PREVIOUS_EXECUTOR_SHA256='6808a9e68e711388aa4c45714c772c477c21c270cd063e10b162141b20095d37'
PREVIOUS_FACTORIZED_EXECUTOR_SHA256='1a425f003ca8db190d326fe2a3ecf632fd111ba1c8d588132f5a7565cb43ea39'


def atomic_json(path,data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_suffix(f'.{os.getpid()}.tmp')
    temp.write_text(json.dumps(data,default=str)+'\n')
    for attempt in range(40):
        try:os.replace(temp,path);return
        except PermissionError:
            if attempt==39:raise
            time.sleep(.05)


def connect(path):
    db=sqlite3.connect(path,timeout=30)
    db.execute('PRAGMA cache_size=-2048')
    db.execute('PRAGMA synchronous=FULL')
    return db


def prepare(path,width):
    with DecorationGroups(path,width):pass
    with closing(connect(path)) as db:
        db.execute('CREATE TABLE IF NOT EXISTS tasks (key TEXT PRIMARY KEY, owner INTEGER) WITHOUT ROWID')
        db.execute('CREATE TABLE IF NOT EXISTS producer (id INTEGER PRIMARY KEY CHECK(id=1), done INTEGER)')
        db.execute('INSERT OR IGNORE INTO producer VALUES(1,0)')
        db.execute('UPDATE tasks SET owner=NULL')
        db.commit()


def publish(directory,metadata,index,k,role,stage,started,**extra):
    atomic_json(Path(directory)/f'worker-{os.getpid()}.json',dict(metadata,
        pid=os.getpid(),parent_pid=os.getppid(),tree_index=index,tree_edges=k-1,
        role=role,tree_started=started,tree_size_started=started,stage=stage,
        updated=tp.now(),**extra))


def produce(context,job,path,config):
    eng,sets,beta,degree,twist,directory,metadata=context
    index,edges,k=job;started=tp.now()
    publish(directory,metadata,index,k,'producer','computing_tree',started)
    with closing(connect(path)) as db:
        class Collector:
            def __init__(self):self.pending=set()
            def contains(self,key):
                if key in self.pending:return True
                if db.execute('SELECT 1 FROM decorations WHERE key=?',(key,)).fetchone():return True
                if db.execute('SELECT 1 FROM tasks WHERE key=?',(key,)).fetchone():return True
                self.pending.add(key)
                if len(self.pending)>=PRODUCER_BATCH:self.flush()
                return True  # Enumeration only: consumers evaluate the markings.
            def flush(self):
                if not self.pending:return
                while True:
                    limit,_=tp.worker_allocation(config)
                    backlog=db.execute('SELECT COUNT(*) FROM tasks').fetchone()[0]
                    if limit and backlog+len(self.pending)<=BACKLOG:break
                    time.sleep(.1)
                # Recheck completed keys under the write transaction: a consumer
                # may have finished a matching queued key since contains().
                db.execute('BEGIN IMMEDIATE')
                db.executemany('INSERT OR IGNORE INTO tasks SELECT ?,NULL WHERE NOT EXISTS (SELECT 1 FROM decorations WHERE key=?)',
                               [(key,key) for key in self.pending])
                db.commit();self.pending.clear()
        collector=Collector()
        eng._tree_sum_grouped(edges,k,sets,len(sets[0]),beta,degree,collector,twist)
        collector.flush()
        db.execute('UPDATE producer SET done=1 WHERE id=1');db.commit()
    publish(directory,metadata,index,k,'producer','producer_complete',started)


def claim(db,owner):
    # Empty consumers must not repeatedly take SQLite's single writer lock.
    # The locked SELECT below still decides ownership if this read races.
    if not db.execute('SELECT 1 FROM tasks WHERE owner IS NULL LIMIT 1').fetchone():return []
    db.execute('BEGIN IMMEDIATE')
    keys=[r[0] for r in db.execute('SELECT key FROM tasks WHERE owner IS NULL LIMIT ?',(BATCH,))]
    db.executemany('UPDATE tasks SET owner=? WHERE key=?',[(owner,key) for key in keys])
    db.commit();return keys


def commit_batch(db,owner,keys,values):
    db.execute('BEGIN IMMEDIATE')
    for key in keys:
        if db.execute('SELECT owner FROM tasks WHERE key=?',(key,)).fetchone()!=(owner,):
            raise ValueError('Batch ownership mismatch')
    count,encoded=db.execute('SELECT count,vals FROM progress WHERE id=1').fetchone()
    old=[Fraction(v) for v in json.loads(encoded)]
    if len(old)!=len(values):raise ValueError('Batch width mismatch')
    db.executemany('INSERT INTO decorations VALUES(?)',[(key,) for key in keys])
    db.execute('UPDATE progress SET count=?,vals=? WHERE id=1',
               (count+len(keys),json.dumps([str(a+b) for a,b in zip(old,values)])))
    db.executemany('DELETE FROM tasks WHERE key=?',[(key,) for key in keys]);db.commit()


def consume(context,job,path,config):
    eng,sets,beta,degree,twist,directory,metadata=context
    index,edges,k=job;owner=os.getpid();started=tp.now()
    with closing(connect(path)) as db:
        while True:
            limit,_=tp.worker_allocation(config)
            if not limit:return
            keys=claim(db,owner)
            if not keys:
                if db.execute('SELECT done FROM producer WHERE id=1').fetchone()[0]:return
                publish(directory,metadata,index,k,'consumer','waiting_for_batch',started)
                time.sleep(.1);continue
            started=tp.now()
            publish(directory,metadata,index,k,'consumer','computing_tree',started,batch_decorations=len(keys))
            values=[Fraction(0)]*len(sets)
            for key in keys:
                values=[a+b for a,b in zip(values,evaluate_key(eng,sets,twist,key))]
            commit_batch(db,owner,keys,values)


def child(role,context,job,path,config):
    if hasattr(__import__('sys'),'set_int_max_str_digits'):__import__('sys').set_int_max_str_digits(0)
    try:
        (produce if role=='producer' else consume)(context,job,path,config)
    except BaseException:
        atomic_json(Path(context[5])/f'error-{os.getpid()}.json',dict(error=traceback.format_exc()))
        raise


def import_previous(base,old_spec,new_spec,identity,width):
    """Reuse verified equivalent inputs; publish the main DB last.

    A partial copy never looks like a completed import. On interruption,
    copying can restart from the unchanged source databases. Prefer the
    immediate predecessor (including its partial groups and ready tasks)
    over the older serial-tree checkpoint.
    """
    target=base/f'{identity}.sqlite'
    if target.exists():return
    candidates=[dict(new_spec,decoration_executor_sha256=PREVIOUS_FACTORIZED_EXECUTOR_SHA256),
                dict(old_spec,decoration_executor_sha256=PREVIOUS_EXECUTOR_SHA256),old_spec]
    for candidate in candidates:
        old_id=tp.digest(candidate);source=base/f'{old_id}.sqlite'
        if source.exists():break
    else:return
    if json.loads((base/f'{old_id}.json').read_text())!=json.loads(json.dumps(candidate,default=str)):raise ValueError('Old manifest mismatch')
    temporary=base/f'{identity}.importing.sqlite'
    with closing(sqlite3.connect(source.resolve().as_uri()+'?mode=ro',uri=True)) as src,closing(connect(temporary)) as dst:
        if src.execute('SELECT identity FROM metadata').fetchall()!=[(old_id,)]:raise ValueError('Old checkpoint identity mismatch')
        src.backup(dst);dst.execute('UPDATE metadata SET identity=?',(identity,));dst.commit()
    groups=[]
    for part in (base/'groups'/old_id).glob('tree-*.sqlite'):
        dest=base/'groups'/identity/part.name;dest.parent.mkdir(parents=True,exist_ok=True)
        pending=dest.with_suffix('.importing.sqlite')
        with closing(sqlite3.connect(part.resolve().as_uri()+'?mode=ro',uri=True)) as src,closing(connect(pending)) as dst:
            src.backup(dst)
            actual_width,count=dst.execute('SELECT width,count FROM progress WHERE id=1').fetchone()
            if actual_width!=width:raise ValueError('Old checkpoint width mismatch')
            groups.append(dict(file=part.name,saved=count))
        os.replace(pending,dest)
    tp.atomic_json(base/f'{identity}.import.json',dict(source=old_id,target=identity,groups=groups,
        reason='Same canonical keys, exact contributions and marked automorphism factors; tested shared-marking factorization'))
    os.replace(temporary,target)


def parallel_sum(eng,sets,beta,twist,config):
    if eng.bk.name!='numeric':raise ValueError('Exact numeric backend required')
    if not sets or len({len(s) for s in sets})!=1 or not any(beta):raise ValueError('Invalid insertion sets or curve class')
    degree=eng.fan.wall_degree(eng.ample,beta)
    if degree<=0:return [Fraction(0)]*len(sets)
    maximum=degree//eng.min_deg;old_spec=tp.manifest(eng,sets,beta,twist,maximum)
    spec=dict(old_spec,decoration_executor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        marking_evaluator_sha256=hashlib.sha256(Path(marking_evaluation.__file__).read_bytes()).hexdigest())
    identity=tp.digest(spec);base=Path(config['checkpoint_directory']);base.mkdir(parents=True,exist_ok=True)
    import_previous(base,old_spec,spec,identity,len(sets))
    tp.atomic_json(base/f'{identity}.json',spec)
    store=tp.Checkpoints(base/f'{identity}.sqlite',identity,len(sets));completed,total=store.load()
    jobs=list(tp.tree_jobs(maximum));metadata=dict(beta=list(beta),max_edges=maximum,trees_total=len(jobs),
            attempt=spec['attempt'],evaluation=spec['evaluation'],checkpoint=identity,work_unit='decoration_batches')
    worker=copy.copy(eng);worker.cancel=None;worker.progress=None;worker._twists={}
    worker_twist=copy.copy(twist) if twist else None
    if worker_twist:worker_twist.eng=worker
    context=(worker,sets,tuple(beta),degree,worker_twist,str(base),metadata)
    children={}
    def report(limit,generation,stage='running'):
        tp.atomic_json(base/'status.json',dict(metadata,stage=stage,driver_pid=os.getpid(),
            trees_completed=len(completed),pending_trees=int(bool(children)),
            pending_workers=len(children),worker_demand=int(config['workers']) if stage!='complete' else 0,
            unsubmitted_trees=max(0,len(jobs)-len(completed)-int(bool(children))),
            allocation_generation=generation,allocated_workers=limit,updated=tp.now()))
    try:
        for job in jobs:
            index,edges,k=job;shape=tp.digest((edges,k))
            if index in completed:
                if completed[index]!=shape:raise ValueError('Tree shape mismatch')
                continue
            path=base/'groups'/identity/f'tree-{index}.sqlite';prepare(path,len(sets))
            with closing(connect(path)) as db:
                while True:
                    if eng.cancel is not None and eng.cancel():
                        from .engine import Cancelled
                        raise Cancelled()
                    limit,generation=tp.worker_allocation(config)
                    for pid,(proc,role) in list(children.items()):
                        cancel=base/f'cancel-{pid}.json'
                        cancelled=cancel.exists()
                        if cancelled and proc.is_alive():proc.terminate();proc.join()
                        if proc.is_alive():continue
                        proc.join();code=proc.exitcode;proc.close();del children[pid]
                        db.execute('UPDATE tasks SET owner=NULL WHERE owner=?',(pid,));db.commit()
                        cancel.unlink(missing_ok=True)
                        if code and not cancelled:
                            error=base/f'error-{pid}.json'
                            raise RuntimeError(error.read_text() if error.exists() else f'Batch worker exited {code}')
                    done=db.execute('SELECT done FROM producer WHERE id=1').fetchone()[0]
                    backlog=db.execute('SELECT COUNT(*) FROM tasks').fetchone()[0]
                    if done and not backlog and not children:break
                    roles=[r for _,r in children.values()]
                    if limit>len(children) and not done and 'producer' not in roles:
                        p=multiprocessing.get_context('spawn').Process(target=child,args=('producer',context,job,str(path),config))
                        p.start();children[p.pid]=(p,'producer')
                    available=db.execute('SELECT COUNT(*) FROM tasks WHERE owner IS NULL').fetchone()[0]
                    for _ in range(min(max(0,limit-len(children)),(available+BATCH-1)//BATCH)):
                        p=multiprocessing.get_context('spawn').Process(target=child,args=('consumer',context,job,str(path),config))
                        p.start();children[p.pid]=(p,'consumer')
                    report(limit,generation);time.sleep(.1)
                values=[Fraction(v) for v in json.loads(db.execute('SELECT vals FROM progress WHERE id=1').fetchone()[0])]
            store.put(index,shape,values);completed[index]=shape
            total=[a+b for a,b in zip(total,values)]
        report(*tp.worker_allocation(config),stage='complete');return total
    finally:
        for proc,role in children.values():
            if proc.is_alive():proc.terminate()
            proc.join();proc.close()
        store.close()
