"""Engine-vs-engine certification: the Holmes-Muratore Theorem 3.4 GKM
engine (gwflags.gkm) against the classical V3.nb-derived engine
(gwflags.localization), evaluated at the SAME random point of the
equivariant torus — the raw localization sums must agree exactly as
rational numbers, term reorganization notwithstanding.

    python3 tests/test_gkm_engine.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from gwflags import FlagVariety
from gwflags.gkm import GKMEngine, gkm_graph_of_flag, gkm_gw
from gwflags.localization import GWCalculator
from gwflags.symbolic import NumericBackend, SympyBackend


def both_engines(X, classes, beta, seed=101):
    bk = NumericBackend(seed=seed)
    calc = GWCalculator(X.rs, None, bk, wd=X.wd)
    ours = calc.gw_invariant(classes, tuple(beta))
    theirs = gkm_gw(X, classes, beta, backend=bk)
    return ours, theirs


def bylen(X):
    d = {}
    for m in X.classes:
        d.setdefault(X.wd.length(m), []).append(m)
    return d


def test_flag_independence_of_h():
    # Theorem 3.6: h(e, d) must not depend on the chosen flag of e.
    for algebra, keep in [('A2', [1]), ('A3', [2]), ('B2', [1, 2])]:
        X = FlagVariety(algebra, keep)
        bk = NumericBackend(seed=7)
        g = gkm_graph_of_flag(X.rs, X.wd, bk)
        eng = GKMEngine(g, bk)
        # index flags by edge
        by_edge = {}
        for v in range(g.n):
            for fi, fl in enumerate(g.flags[v]):
                by_edge.setdefault(fl['edge'], []).append((v, fi))
        for eid, sides in by_edge.items():
            assert len(sides) == 2
            (v1, f1), (v2, f2) = sides
            for d in (1, 2, 3):
                assert eng.h(v1, f1, d) == eng.h(v2, f2, d), \
                    (algebra, keep, eid, d)


def test_no_parallel_edges_in_battery():
    # documents the assumption under which the classical engine's
    # degree-only dedup is equivalent to the intrinsic GKM formulation
    for algebra, keep in [('A2', [1]), ('A2', [1, 2]), ('A3', [2]),
                          ('A3', [1, 3]), ('A4', [1]), ('A4', [1, 2]),
                          ('B2', [1, 2]), ('G2', [1]), ('G2', [2]),
                          ('A2xA2', [1, 3])]:
        X = FlagVariety(algebra, keep)
        g = gkm_graph_of_flag(X.rs, X.wd, NumericBackend(seed=3))
        assert not g.parallel_edges, (algebra, keep, g.parallel_edges)


def test_p1_symbolic_identity():
    # strongest form on the smallest case: identical rational functions
    import sympy
    X = FlagVariety('A1', [1])
    bk = SympyBackend()
    calc = GWCalculator(X.rs, None, bk, wd=X.wd)
    ours = calc.gw_invariant([X.pt, X.pt], (1,))
    theirs = gkm_gw(X, [X.pt, X.pt], (1,), backend=bk)
    assert sympy.simplify(sympy.sympify(ours) - sympy.sympify(theirs)) == 0


def test_battery_exact_equality():
    cases = []
    X = FlagVariety('A2', [1])                       # P^2
    h = X.schubert((1,))
    cases += [(X, [X.pt, X.pt], (1, 0)),
              (X, [X.pt, X.pt, h], (1, 0)),
              (X, [X.pt] * 5, (2, 0))]
    F = FlagVariety('A2', [1, 2])                    # Fl(3)
    cases += [(F, [F.pt, F.pt], (1, 1)),
              (F, [F.pt, F.schubert((1, 2))], (1, 0)),
              (F, [F.pt, F.pt], (2, 1))]
    G = FlagVariety('A3', [2])                       # Gr(2,4)
    bl = bylen(G)
    cases += [(G, [bl[1][0], bl[3][0], bl[4][0]], (0, 1, 0)),
              (G, [bl[4][0], bl[4][0], bl[2][0]], (0, 2, 0))]
    B = FlagVariety('B2', [1, 2])                    # SO(5)/B
    blb = bylen(B)
    cases += [(B, [B.pt, B.pt], (1, 1)),
              (B, [blb[3][0], blb[3][0]], (1, 1))]
    P = FlagVariety('A2xA2', [1, 3])                 # P^2 x P^2
    blp = bylen(P)
    cases += [(P, [P.pt, blp[3][0]], (1, 0, 1, 0))]

    for i, (X, classes, beta) in enumerate(cases):
        ours, theirs = both_engines(X, classes, beta, seed=200 + i)
        assert ours == theirs, \
            (X.rs.name, [X.wd.length(c) for c in classes], beta,
             ours, theirs)
        print(f'  {X.rs.name} keep {X.wd.roots_that_stay} '
              f'lens {[X.wd.length(c) for c in classes]} beta {beta}: '
              f'both = {ours}')


if __name__ == '__main__':
    import time
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            t0 = time.time()
            fn()
            print(f'{name}: ok ({time.time() - t0:.1f}s)')
    print('all GKM-engine tests passed')
