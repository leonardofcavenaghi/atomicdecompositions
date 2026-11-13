"""Use a verified integral ample divisor to bound localization edges exactly."""
from contextlib import contextmanager, closing
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import zlib


def adjunction_divisor(variety, K=None):
    """Return c1(TY)-sum(K) only when it is integral and ambient ample.

    Positivity on X alone is insufficient: localization edges lie in Y.
    """
    rows = variety.check_K(K)
    divisor = tuple(1-sum(row[i] for row in rows) for i in range(variety.k))
    if any(Fraction(a).denominator != 1 for a in divisor):
        return None
    divisor = tuple(int(a) for a in divisor)
    degrees = [variety.fan.wall_degree(divisor, w['cls']) for w in variety.fan.walls]
    return divisor if degrees and min(degrees) > 0 else None


def localization_divisor(variety, K=None, beta=None):
    """Select the automatic search divisor, preserving explicit overrides.

    Setting localization_degree_divisor=None explicitly opts out of automatic
    adjunction bounds. This is also useful for exact old/new comparisons.
    """
    if hasattr(variety, 'localization_degree_divisor'):
        return variety.localization_degree_divisor
    divisor = adjunction_divisor(variety, K)
    if divisor is not None and beta is not None:
        # Keep a stronger existing bound, and keep its checkpoints on ties.
        previous = variety.fan.ample_divisor()
        def ceiling(a):
            minimum = min(variety.fan.wall_degree(a, w['cls']) for w in variety.fan.walls)
            return variety.fan.wall_degree(a, beta)//minimum
        if ceiling(previous) <= ceiling(divisor):
            return None
    return divisor


def edge_bound_report(variety, K, betas):
    """The same per-class bound as the solver, with its positivity certificate.

    For the divisor quantum product c1(X).beta <= dim(X)+1, hence the
    adjunction bound is at most dim(X)+1. General GW calls are NOT clipped
    at that number: their insertion dimension may allow larger classes.
    """
    previous = variety.fan.ample_divisor()
    divisor = localization_divisor(variety, K)
    if divisor is None:
        divisor = previous
    minimum = min(variety.fan.wall_degree(divisor, w['cls']) for w in variety.fan.walls)
    if minimum <= 0 or any(Fraction(a).denominator != 1 for a in divisor):
        raise ValueError('Edge-bound divisor must be integral and ambient ample')
    old_minimum = min(variety.fan.wall_degree(previous, w['cls']) for w in variety.fan.walls)
    bounds = []
    for beta in betas:
        if not any(beta):
            continue
        selected = localization_divisor(variety, K, beta)
        if selected is None:
            selected = previous
        selected_minimum = min(variety.fan.wall_degree(selected, w['cls']) for w in variety.fan.walls)
        bounds.append(dict(beta=list(beta), max_edges=variety.fan.wall_degree(selected, beta)//selected_minimum,
                           ample=list(selected), minimum_edge_degree=selected_minimum))
    adjunction = adjunction_divisor(variety, K)
    return dict(ample=list(divisor), minimum_edge_degree=minimum, bounds=bounds,
                max_edges=max((b['max_edges'] for b in bounds), default=0),
                ambient_adjunction_ample=adjunction is not None,
                bound_divisor='adjunction' if divisor == adjunction else 'other_ample',
                selection='Per-class minimum of the existing ample bound and the ambient ample adjunction bound; existing bound wins ties',
                dimension=variety.n-len(variety.check_K(K)),
                previous_max_edges=max((variety.fan.wall_degree(previous, beta)//old_minimum
                                        for beta in betas if any(beta)), default=0))


@contextmanager
def degree_bound(engine, divisor):
    if divisor is None:
        yield
        return
    if len(divisor) != engine.fan.k or any(Fraction(a).denominator != 1 for a in divisor):
        raise ValueError('An integral ambient divisor is required for the edge bound')
    divisor = tuple(int(a) for a in divisor)
    degrees = {eid: engine.fan.wall_degree(divisor, cls)
               for eid, cls in engine.edge_cls.items()}
    if not degrees or min(degrees.values()) <= 0:
        raise ValueError('Edge-bound divisor must be positive on every ambient invariant curve')
    previous = engine.ample, engine.edge_deg, engine.min_deg
    engine.ample, engine.edge_deg, engine.min_deg = divisor, degrees, min(degrees.values())
    try:
        yield
    finally:
        engine.ample, engine.edge_deg, engine.min_deg = previous


def reuse_degree_checkpoints(engine, sets, beta, twist, config, executor=None):
    """Import unchanged tree contributions from a looser ample-degree search.

Only the search divisor and edge ceiling may differ. In particular, the solver
sources, actual evaluation point, insertions and twist must match exactly.
The full contribution routine is unchanged by the choice of search divisor.
"""
    from .tree_parallel import manifest, digest, tree_jobs, Checkpoints, atomic_json, now
    maximum = engine.fan.wall_degree(engine.ample, beta) // engine.min_deg
    spec = manifest(engine, sets, beta, twist, maximum)
    if executor is not None and executor.__module__ == 'gwtoric.decoration_parallel':
        from . import decoration_parallel, marking_evaluation
        spec.update(decoration_executor_sha256=hashlib.sha256(Path(decoration_parallel.__file__).read_bytes()).hexdigest(),
                    marking_evaluator_sha256=hashlib.sha256(Path(marking_evaluation.__file__).read_bytes()).hexdigest())
    elif executor is not None and executor.__module__ != 'gwtoric.tree_parallel':
        return  # Unknown executors need their own provenance and resume contract.
    spec = json.loads(json.dumps(spec, default=str))
    identity = digest(spec)
    directory = Path(config['checkpoint_directory'])
    directory.mkdir(parents=True, exist_ok=True)
    new_path = directory / f'{identity}.sqlite'
    if new_path.exists():
        return
    shapes = {index: digest((edges, k)) for index, edges, k in tree_jobs(maximum)}
    essential = {k: v for k, v in spec.items() if k not in ('ample', 'max_edges')}
    imported = {}
    groups = {}
    sources = []
    for path in directory.glob('*.sqlite'):
        info_path = path.with_suffix('.json')
        if not info_path.exists():
            continue
        old = json.loads(info_path.read_text(encoding='utf-8'))
        if digest(old) != path.stem:
            raise ValueError('Checkpoint manifest digest mismatch')
        if {k:v for k,v in old.items() if k not in ('ample','max_edges')} != essential:
            continue
        if old['max_edges'] < maximum:
            continue
        old_degrees = [engine.fan.wall_degree(old['ample'], cls) for cls in engine.edge_cls.values()]
        if min(old_degrees) <= 0 or old['max_edges'] != engine.fan.wall_degree(old['ample'], beta)//min(old_degrees):
            raise ValueError('Invalid original ample-degree bound')
        database = sqlite3.connect(path.resolve().as_uri()+'?mode=ro', uri=True)
        count = 0
        try:
            if database.execute('SELECT identity FROM metadata').fetchall() != [(path.stem,)]:
                raise ValueError('Checkpoint database provenance mismatch')
            for index, shape, blob in database.execute('SELECT id, shape, vals FROM trees ORDER BY id'):
                encoded = json.loads(zlib.decompress(blob))
                values = tuple(Fraction(v) for v in encoded) if encoded else (Fraction(0),)*len(sets)
                if len(values) != len(sets):
                    raise ValueError('Checkpoint contribution width mismatch')
                if index not in shapes:
                    if any(values):
                        raise ValueError('Nonzero contribution beyond the proven bound')
                    continue
                if shape != shapes[index]:
                    raise ValueError('Checkpoint tree shape mismatch')
                if index in imported and imported[index] != values:
                    raise ValueError('Conflicting exact tree contributions')
                imported[index] = values
                count += 1
        finally:
            database.close()
        # Canonical unmarked keys and their exact contributions are independent
        # of the positive search divisor. Copy a whole partial database, never
        # add partial totals from different enumerations (keys may overlap).
        for part in (directory/'groups'/path.stem).glob('tree-*.sqlite'):
            index = int(part.stem.split('-')[1])
            with closing(sqlite3.connect(part.resolve().as_uri()+'?mode=ro', uri=True)) as db:
                width, saved, encoded = db.execute('SELECT width,count,vals FROM progress WHERE id=1').fetchone()
                values = [Fraction(v) for v in json.loads(encoded)]
                if width != len(sets) or len(values) != len(sets):
                    raise ValueError('Checkpoint decoration width mismatch')
                if db.execute('SELECT COUNT(*) FROM decorations').fetchone()[0] != saved:
                    raise ValueError('Checkpoint decoration count mismatch')
                if index not in shapes:
                    if saved or any(values):
                        raise ValueError('Saved decorations beyond the proven bound')
                    continue
                if index not in groups or saved > groups[index][0]:
                    groups[index] = saved, part
        sources.append(dict(checkpoint=path.stem, imported_trees=count))
    if not sources:
        return
    atomic_json(directory/f'{identity}.json', spec)
    # Publish the main DB last: interrupted migration can safely retry from
    # unchanged sources, including in-flight batches saved as ready tasks.
    pending = new_path.with_suffix('.migrating.sqlite')
    target = Checkpoints(pending, identity, len(sets))
    try:
        target.db.execute('DELETE FROM trees')
        target.db.commit()
        for index, values in sorted(imported.items()):
            target.put(index, shapes[index], values)
    finally:
        target.close()
    for index, (_, source) in groups.items():
        if index in imported:
            continue
        destination = directory/'groups'/identity/source.name
        destination.parent.mkdir(parents=True, exist_ok=True)
        part_pending = destination.with_suffix('.migrating.sqlite')
        with closing(sqlite3.connect(source.resolve().as_uri()+'?mode=ro', uri=True)) as src, closing(sqlite3.connect(part_pending)) as dst:
            src.backup(dst)
            if dst.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='tasks'").fetchone():
                dst.execute('UPDATE tasks SET owner=NULL')
            dst.commit()
        os.replace(part_pending, destination)
    atomic_json(directory/f'{identity}.migration.json', dict(updated=now(), sources=sources,
        imported_trees=len(imported), maximum_edges=maximum,
        partial_groups=[dict(tree=index, saved=count) for index,(count,_) in groups.items() if index not in imported],
        reason='Same fixed-locus contributions; verified positive divisor gives a smaller exhaustive search'))
    os.replace(pending, new_path)
