"""Exact parallel tree sums, with durable checkpoints for each whole tree.

Workers handle separate tree shapes. Within a tree, unmarked decorations are
processed independently and checkpointed in batches, with local marking deduplication.
"""
from concurrent.futures import ProcessPoolExecutor, FIRST_COMPLETED, wait
import copy
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import multiprocessing
import os
from pathlib import Path
import sqlite3
import time
import zlib

_CONTEXT = None
_WORKER_SIZE = None
_WORKER_SIZE_STARTED = None
VERSION = 1


def atomic_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(f'.{os.getpid()}.tmp')
    temp.write_text(json.dumps(data, default=str) + '\n', encoding='utf-8')
    os.replace(temp, path)


def now():
    return datetime.now(timezone.utc).isoformat()


def tree_counts(nmax):
    rooted = [0, 1] + [0] * max(0, nmax - 1)
    for n in range(2, nmax + 1):
        rooted[n] = sum(sum(d * rooted[d] for d in range(1, k + 1) if k % d == 0)
                        * rooted[n-k] for k in range(1, n)) // (n-1)
    return [0] + [rooted[n] - (sum(rooted[i] * rooted[n-i] for i in range(1, n))
                  - (rooted[n//2] if n % 2 == 0 else 0)) // 2 for n in range(1, nmax+1)]


def tree_jobs(max_edges):
    from .engine import free_trees
    index = 0
    for vertices in range(1, max_edges + 2):
        for edges, k in free_trees(vertices):
            index += 1
            yield index, edges, k
        free_trees.cache_clear()  # Only the coordinator enumerates shapes.


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, default=str).encode()).hexdigest()


def manifest(eng, sets, beta, twist, max_edges):
    root = Path(__file__).resolve().parents[1]
    source_files = ('gwtoric/tree_parallel.py', 'gwtoric/engine.py', 'gwtoric/ci.py',
                    'gwtoric/decoration_groups.py', 'gwtoric/fan.py', 'gwflags/gkm.py', 'gwflags/trees.py', 'gwflags/symbolic.py')
    return dict(version=VERSION, sources={f: hashlib.sha256((root/f).read_bytes()).hexdigest()
                                         for f in source_files},
                rays=eng.fan.rays, cones=eng.fan.max_cones, beta=beta,
                ample=eng.ample, max_edges=max_edges, insertions=sets,
                point=sorted(eng.bk._point.items()),
                twist_rows=twist.rows if twist else [],
                twist_weights=twist.w if twist else [],
                attempt=getattr(eng, 'evaluation_attempt', 1),
                evaluation=getattr(eng, 'evaluation_pass', 1))


class Checkpoints:
    def __init__(self, path, identity, width):
        self.width = width
        self.db = sqlite3.connect(path)
        self.db.execute('PRAGMA journal_mode=WAL')
        self.db.execute('PRAGMA synchronous=FULL')
        self.db.execute('CREATE TABLE IF NOT EXISTS metadata (identity TEXT NOT NULL)')
        self.db.execute('CREATE TABLE IF NOT EXISTS trees (id INTEGER PRIMARY KEY, shape TEXT NOT NULL, vals BLOB NOT NULL)')
        stored = self.db.execute('SELECT identity FROM metadata').fetchall()
        if stored and stored != [(identity,)]:
            self.db.close()
            raise ValueError('Tree checkpoint provenance mismatch')
        if not stored:
            self.db.execute('INSERT INTO metadata VALUES (?)', (identity,))
            self.db.commit()

    def load(self):
        completed, total = {}, [Fraction(0)] * self.width
        for index, shape, blob in self.db.execute('SELECT id, shape, vals FROM trees ORDER BY id'):
            values = json.loads(zlib.decompress(blob))
            if values:
                if len(values) != self.width:
                    raise ValueError('Invalid tree checkpoint width')
                total = [a + Fraction(b) for a, b in zip(total, values)]
            completed[index] = shape
        return completed, total

    def put(self, index, shape, values):
        if len(values) != self.width:
            raise ValueError('Invalid tree contribution width')
        data = [str(Fraction(v)) for v in values] if any(values) else []
        blob = zlib.compress(json.dumps(data).encode())
        # A duplicate result is an error, never silently added twice.
        with self.db:
            self.db.execute('INSERT INTO trees VALUES (?, ?, ?)', (index, shape, blob))

    def close(self):
        self.db.close()


def initialize_worker(eng, sets, beta, total_deg, twist, directory, metadata):
    global _CONTEXT
    _CONTEXT = eng, sets, beta, total_deg, twist, directory, metadata


def evaluate_tree(job):
    global _WORKER_SIZE, _WORKER_SIZE_STARTED
    eng, sets, beta, total_deg, twist, directory, metadata = _CONTEXT
    index, edges, k = job
    eng.decoration_checkpoint = str(Path(directory) / 'groups' / metadata['checkpoint'] / f'tree-{index}.sqlite')
    if k != _WORKER_SIZE:
        _WORKER_SIZE, _WORKER_SIZE_STARTED = k, now()
    path = Path(directory) / f'worker-{os.getpid()}.json'
    state = dict(metadata, pid=os.getpid(), parent_pid=os.getppid(), tree_index=index, tree_edges=k-1,
                 tree_started=now(), tree_size_started=_WORKER_SIZE_STARTED, stage='computing_tree')
    atomic_json(path, state)
    started = time.monotonic()
    values = [Fraction(0)] * len(sets)
    try:
        eng._tree_sum_multi(edges, k, sets, len(sets[0]), beta, total_deg, values, twist)
    except BaseException as exc:
        atomic_json(path, dict(state, stage='tree_failed', error=repr(exc), updated=now()))
        raise
    atomic_json(path, dict(state, stage='tree_complete', updated=now(),
                           tree_seconds=time.monotonic()-started))
    return values


def worker_allocation(config):
    maximum = int(config['workers'])
    limit = int(config.get('initial_workers', maximum))
    path = config.get('capacity_file')
    generation = 0
    if path and Path(path).exists():
        allocation = json.loads(Path(path).read_text())
        limit = int(allocation['workers'])
        generation = allocation.get('generation', 0)
    if not 0 <= limit <= maximum:
        raise ValueError('Invalid tree-worker allocation')
    return limit, generation


def worker_limit(config):
    return worker_allocation(config)[0]


def parallel_sum(eng, insertion_sets, beta, twist, config):
    """Same result as engine.gw_multi; no approximate or partial class cache."""
    from .engine import Cancelled
    if eng.bk.name != 'numeric':
        raise ValueError('Tree checkpointing requires the exact numeric backend')
    sizes = {len(t) for t in insertion_sets}
    if len(sizes) != 1 or not insertion_sets or not any(beta):
        raise ValueError('Expected nonzero class and equally sized insertion tuples')
    total_deg = eng.fan.wall_degree(eng.ample, beta)
    if total_deg <= 0:
        return [Fraction(0)] * len(insertion_sets)
    max_edges = total_deg // eng.min_deg
    trees_total = sum(tree_counts(max_edges+1))
    spec = manifest(eng, insertion_sets, beta, twist, max_edges)
    identity = digest(spec)
    base = Path(config['checkpoint_directory'])
    base.mkdir(parents=True, exist_ok=True)
    atomic_json(base / f'{identity}.json', spec)
    store = Checkpoints(base / f'{identity}.sqlite', identity, len(insertion_sets))
    completed, total = store.load()
    metadata = dict(beta=list(beta), max_edges=max_edges, trees_total=trees_total,
                    attempt=spec['attempt'], evaluation=spec['evaluation'], checkpoint=identity)
    status_path = base / 'status.json'
    atomic_json(status_path, dict(metadata, stage='running', trees_completed=len(completed), updated=now()))
    # Send the already chosen numerical weights to every process. Never reroll
    # weights per tree; callbacks and the parent reporter are not serializable.
    worker_eng = copy.copy(eng)
    worker_eng.cancel = None
    worker_eng.progress = None
    # Cached twists refer back to the original engine and its local callback.
    # The selected twist is copied and rebound below; no other twist is needed.
    worker_eng._twists = {}
    worker_twist = copy.copy(twist) if twist else None
    if worker_twist:
        worker_twist.eng = worker_eng
    pool = None
    pending = {}
    validated = set()
    jobs = iter(tree_jobs(max_edges))
    exhausted = False
    try:
        while not exhausted or pending:
            if eng.cancel is not None and eng.cancel():
                raise Cancelled()
            limit, generation = worker_allocation(config)
            while not exhausted and (len(pending) < limit or len(completed) == trees_total):
                try:
                    job = next(jobs)
                except StopIteration:
                    exhausted = True
                    break
                index, edges, vertices = job
                shape = digest((edges, vertices))
                if index in completed:
                    if completed[index] != shape:
                        raise ValueError('Tree enumeration differs from checkpoint')
                    validated.add(index)
                    continue
                if pool is None:
                    pool = ProcessPoolExecutor(max_workers=int(config['workers']),
                        mp_context=multiprocessing.get_context('spawn'),
                        initializer=initialize_worker,
                        initargs=(worker_eng, insertion_sets, tuple(beta), total_deg,
                                  worker_twist, str(base), metadata))
                pending[pool.submit(evaluate_tree, job)] = index, shape
            atomic_json(status_path, dict(metadata, stage='running', driver_pid=os.getpid(),
                trees_completed=len(completed), pending_trees=len(pending),
                unsubmitted_trees=trees_total-len(completed)-len(pending),
                allocation_generation=generation, allocated_workers=limit, updated=now()))
            if not pending:
                time.sleep(.2)
            if pending:
                finished, _ = wait(pending, timeout=1, return_when=FIRST_COMPLETED)
                for future in finished:
                    index, shape = pending.pop(future)
                    values = future.result()
                    store.put(index, shape, values)
                    total = [a+b for a, b in zip(total, values)]
                    completed[index] = shape
                    validated.add(index)
        if len(completed) != trees_total or validated != set(completed):
            raise ValueError('Incomplete tree coverage')
        atomic_json(status_path, dict(metadata, stage='complete', driver_pid=os.getpid(),
            trees_completed=len(completed), pending_trees=0, unsubmitted_trees=0,
            allocation_generation=generation, allocated_workers=limit, updated=now()))
        return total
    except BaseException:
        if pool is not None:
            for process in list(pool._processes.values()):
                if process.is_alive():
                    process.terminate()
        raise
    finally:
        if pool is not None:
            pool.shutdown(wait=True, cancel_futures=True)
        store.close()
