"""Separate unmarked generation and exact marking evaluation, with resumable storage."""
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sqlite3
import time

from .checkpoint_values import dumps_values, loads_values

from .trees import (DecoratedTree, ahu_canon, all_possible_marks,
                    _tree_adjacency, find_expanded_associations)


def representatives(tree, beta, wd):
    """Stream unmarked representatives using the flag edge-label convention."""
    edges, n = tree
    labels = [(qi, wd.rs.coroots[qi]) for qi in wd.reduced_root_indices]
    assocs = find_expanded_associations(len(edges), labels, list(beta),
                                      [list(g) for g in wd.removed_simple_roots])
    adj = _tree_adjacency(edges, n)
    eidx = {e:i for i,e in enumerate(edges)}
    sequence, visited, order = [], {1}, [1]
    for v in order:
        for w,e in adj[v]:
            if w not in visited:
                visited.add(w); sequence.append((w,v,eidx[e])); order.append(w)
    step = wd.step_table()
    for start in range(len(wd.reduced_group)):
        for assoc in assocs:
            vertices = [0]*(n+1); vertices[1] = start
            for w,v,i in sequence:
                vertices[w] = step[(vertices[v],assoc[i][0])]
            degrees = {e:assoc[i][1] for i,e in enumerate(edges)}
            key,_ = ahu_canon(n,adj,degrees,vertices.__getitem__)
            yield json.dumps(key), (assoc,vertices)


def mark_variants(tree, representative, calc, count, twist=None):
    """Reuse an unmarked base and twist; retain each marked orbit's automorphisms."""
    edges,n = tree
    assoc,vfix = representative
    assoc = [tuple(a) for a in assoc]
    adj = _tree_adjacency(edges,n)
    degrees = {e:assoc[i][1] for i,e in enumerate(edges)}
    images = {v:calc.wd.reduced_group[vfix[v]] for v in range(1,n+1)}
    def make(marks):
        return DecoratedTree(n,edges,dict(zip(edges,assoc)),images,
                             {v:marks[v-1] for v in range(1,n+1)},
                             {v:vfix[v] for v in range(1,n+1)})
    unmarked = make([()]*n)
    sums = []
    for v,(w,parent,children,_) in enumerate(unmarked.table(),1):
        terms = []
        if parent:
            ri,d = parent
            terms.append(Fraction(d)/calc.poly_w(unmarked.parent_w(v),calc.rs.positive_roots_ort[ri]))
        for ri,d in children:
            terms.append(-Fraction(d)/calc.poly_w(w,calc.rs.positive_roots_ort[ri]))
        sums.append(sum(terms))
    shared = all(not calc.bk.is_zero(x) for x in sums)
    base = calc.dec_base_nocache(unmarked)*unmarked.automorphism_group_size() if shared else None
    twisting = twist(unmarked) if twist else 1
    seen = set()
    for marks in all_possible_marks(count,n):
        key,aut = ahu_canon(n,adj,degrees,lambda v:(vfix[v],marks[v-1]))
        if key in seen:
            continue
        seen.add(key)
        dt = make(marks); dt._canon_cache = (key,aut)
        if shared:
            value = base/Fraction(aut)
            for v in range(n):
                value *= sums[v]**len(marks[v])
        else:
            value = calc.dec_base_nocache(dt)
        yield dt, value*twisting


def staged_sum(calc, beta, insertion_sets, K, directory, progress=None, cancel=None):
    from .trees import all_trees
    from .cintersection import omega_complete_intersection
    log = progress or (lambda _: None)
    checked = [0.0]
    def check():
        if cancel and cancel():
            raise InterruptedError('Calculation stopped; committed checkpoints are retained')
        if time.monotonic()-checked[0] >= 5:
            from .execution import worker_limit
            worker_limit(1)  # Refuse further allocation under high memory pressure.
            checked[0] = time.monotonic()
    # Freeze all equivariant values before constructing the persistent identity.
    point = [str(calc.bk.x(i)) for i in range(1,calc.rs.rank+1)]
    identity = dict(version=1, algebra=calc.rs.name, keep=calc.wd.roots_that_stay,
                    beta=list(beta), bundle=repr(K.key() if hasattr(K,'key') else K),
                    point=point, insertions=repr(insertion_sets))
    digest = hashlib.sha256(json.dumps(identity,sort_keys=True).encode()).hexdigest()
    path = ':memory:'
    if directory:
        directory = Path(directory); directory.mkdir(parents=True,exist_ok=True)
        path = str(directory/(digest+'.sqlite'))
    db = sqlite3.connect(path)
    db.execute('PRAGMA cache_size=-2048')
    db.execute('CREATE TABLE IF NOT EXISTS reps (tree INTEGER, key TEXT, data TEXT, PRIMARY KEY(tree,key))')
    db.execute('CREATE TABLE IF NOT EXISTS generated (tree INTEGER PRIMARY KEY)')
    db.execute('CREATE TABLE IF NOT EXISTS sums (tree INTEGER PRIMARY KEY, last_id INTEGER, vals TEXT)')
    width = len(insertion_sets)
    total = [Fraction(0)]*width
    twist = (lambda dt:omega_complete_intersection(calc,K,dt)) if K else None
    try:
        for ti,tree in enumerate(all_trees(sum(beta)+1)):
            check()
            if not db.execute('SELECT 1 FROM generated WHERE tree=?',(ti,)).fetchone():
                log(f'Tree {ti+1}: generating unmarked decorations')
                for k,(key,data) in enumerate(representatives(tree,beta,calc.wd)):
                    check()
                    db.execute('INSERT OR IGNORE INTO reps VALUES(?,?,?)',(ti,key,json.dumps(data)))
                    if k%128 == 0:
                        db.commit()
                db.execute('INSERT INTO generated VALUES(?)',(ti,)); db.commit()
            row = db.execute('SELECT last_id,vals FROM sums WHERE tree=?',(ti,)).fetchone()
            last,acc = (row[0],loads_values(row[1])) if row else (0,[Fraction(0)]*width)
            log(f'Tree {ti+1}: evaluating markings'+(' (resuming)' if row else ''))
            pending = 0
            for rid,data in db.execute('SELECT rowid,data FROM reps WHERE tree=? AND rowid>? ORDER BY rowid',(ti,last)):
                check()
                for dt,base in mark_variants(tree,json.loads(data),calc,len(insertion_sets[0]),twist):
                    carriers = calc.mark_carriers(dt)
                    for j,insertions in enumerate(insertion_sets):
                        value = base
                        for cls,w in zip(insertions,carriers):
                            value *= calc.billey(cls,w)
                        acc[j] += value
                db.execute('INSERT OR REPLACE INTO sums VALUES(?,?,?)',(ti,rid,dumps_values(acc)))
                pending += 1
                if pending%128 == 0:
                    db.commit(); log(f'Tree {ti+1}: {pending} further unmarked decorations evaluated')
            db.commit()
            total = [a+b for a,b in zip(total,acc)]
        return total
    finally:
        db.close()

