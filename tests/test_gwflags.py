"""Verification suite for the V3.nb translation.

Every expected value is an independently known number from classical or
quantum Schubert calculus.  Run:  python3 -m pytest tests/  (or just
python3 tests/test_gwflags.py).
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from gwflags import FlagVariety, projective_space, grassmannian, full_flag
from gwflags.rootsystem import RootSystemData
from gwflags.quantum import metric_matrix, reduce_matrix, betas_and_fano_index


def test_root_counts():
    for alg, npos in [('A1', 1), ('A2', 3), ('A3', 6), ('B2', 4),
                      ('G2', 6), ('B3', 9), ('C3', 9), ('D4', 12),
                      ('F4', 24)]:
        assert len(RootSystemData(alg).positive_roots) == npos


def test_weyl_and_schubert_basis():
    X = projective_space(2)
    assert sorted(X.wd.length(m) for m in X.classes) == [0, 1, 2]
    G = grassmannian(2, 4)
    assert sorted(G.wd.length(m) for m in G.classes) == [0, 1, 2, 2, 3, 4]
    assert G.dimension == 4


def test_p1():
    X = projective_space(1)
    assert X.gw([X.pt, X.wd.group[0]], (0,)) == 1
    assert X.gw([X.pt, X.pt], (1,)) == 1


def test_p2():
    X = projective_space(2)
    assert X.gw([X.pt, X.pt], (1, 0)) == 1          # line through 2 points
    h = X.schubert((1,))
    assert X.gw([X.pt, X.pt, h], (1, 0)) == 1       # divisor axiom
    assert X.gw([h, h], (0, 0)) == 1                # <h,h> pairing


def test_p2_conics():
    X = projective_space(2)
    assert X.gw([X.pt] * 5, (2, 0)) == 1            # conic through 5 points


def test_p3():
    X = projective_space(3)
    assert X.gw([X.pt, X.pt], (1, 0, 0)) == 1


def test_full_flag_a2():
    X = full_flag('A2')
    assert X.gw([X.pt, X.pt], (1, 1)) == 1


def test_gr24():
    G = grassmannian(2, 4)
    bylen = {}
    for m in G.classes:
        bylen.setdefault(G.wd.length(m), []).append(m)
    s1, s21, pt = bylen[1][0], bylen[3][0], bylen[4][0]
    # sigma_1 * sigma_21 = sigma_22 + q   (Bertram)
    assert G.gw([s1, s21, pt], (0, 1, 0)) == 1


def test_sqm_p1():
    X = projective_space(1)
    fano, betas = betas_and_fano_index(X, [])
    assert fano == 2
    M, Gr, idx = X.small_quantum_multiplication(betas=betas)
    y1 = X.bk.y(1)
    assert M == [[0, 2 * y1], [2, 0]]
    ev = set(map(str, X.eigenvalues(M)))
    assert ev == {'2*sqrt(y1)', '-2*sqrt(y1)'}


def test_sqm_p2():
    X = projective_space(2)
    fano, betas = betas_and_fano_index(X, [])
    assert fano == 3
    M, Gr, idx = X.small_quantum_multiplication(betas=betas)
    y1 = X.bk.y(1)
    assert M == [[0, 0, 3 * y1], [3, 0, 0], [0, 3, 0]]


def test_product_p1xp1():
    X = FlagVariety('A1xA1', [1, 2])            # P^1 x P^1
    assert X.dimension == 2
    assert len(X.classes) == 4
    # divisor axiom: <pt, sigma_{s_e}>_{(1,0)} = <sigma_{s_e}, beta> * <pt>
    h1, h2 = X.schubert((1,)), X.schubert((2,))
    assert X.gw([X.pt, h1], (1, 0)) == 1
    assert X.gw([X.pt, h2], (1, 0)) == 0
    M, Gr, idx = X.small_quantum_multiplication()
    ev = sorted(str(e) for e in X.eigenvalues(M, at_one=True))
    assert ev == ['-4', '0', '0', '4']


def test_ahu_matches_bruteforce():
    import random
    from itertools import permutations as perms
    from gwflags.trees import DecoratedTree, all_trees_n

    def brute(dt):
        def key(q):
            vs = tuple(sorted((q[v - 1], dt.vid[v], dt.vmarks[v])
                              for v in range(1, dt.n + 1)))
            es = tuple(sorted((tuple(sorted((q[u - 1], q[v - 1]))),
                               dt.elabel[(u, v)][1]) for u, v in dt.edges))
            return (vs, es)
        ks = [key(q) for q in perms(range(1, dt.n + 1))]
        return min(ks), ks.count(key(tuple(range(1, dt.n + 1))))

    rng = random.Random(11)
    canon_map = {}
    for _ in range(600):
        n = rng.randint(1, 6)
        edges, _ = all_trees_n(n)[rng.randrange(len(all_trees_n(n)))]
        p = list(range(1, n + 1))
        rng.shuffle(p)
        redges = tuple(tuple(sorted((p[u - 1], p[v - 1]))) for u, v in edges)
        elabel = {e: (rng.randint(0, 2), rng.randint(1, 3)) for e in redges}
        vid = {v: rng.randint(0, 2) for v in range(1, n + 1)}
        marks = {v: tuple(sorted(rng.sample(range(1, 4), rng.randint(0, 2))))
                 for v in range(1, n + 1)}
        dt = DecoratedTree(n, redges, elabel, dict(vid), marks, vid)
        bkey, baut = brute(dt)
        akey, aaut = dt._canon()
        assert aaut == baut
        assert canon_map.setdefault(akey, bkey) == bkey
        assert canon_map.setdefault(bkey, akey) == akey


def test_dfs_assoc_matches_fallback():
    import random
    from gwflags.trees import find_expanded_associations

    def fallback(num_edges, labels, beta, gens):
        from itertools import permutations as perms
        from gwflags.trees import nonneg_compositions, congruent_mod_gens
        k = num_edges
        cmax = max(1, sum(abs(b) for b in beta)
                   + (sum(abs(x) for g in gens for x in g) if gens else 0))
        expanded = [(ri, c, tuple(c * x for x in co))
                    for (ri, co) in labels for c in range(1, cmax + 1)]
        valid = []
        for count in nonneg_compositions(k, len(expanded)):
            total = [0] * len(beta)
            for cnt, (_, _, vec) in zip(count, expanded):
                for i, x in enumerate(vec):
                    total[i] += cnt * x
            if congruent_mod_gens(total, beta, gens):
                ms = []
                for cnt, (ri, c, _) in zip(count, expanded):
                    ms.extend([(ri, c)] * cnt)
                valid.extend(set(perms(ms)))
        return valid

    rng = random.Random(5)
    for _ in range(40):
        rank = rng.randint(1, 3)
        nlab = rng.randint(1, 3)
        labels = [(i, tuple(rng.randint(0, 2) for _ in range(rank)))
                  for i in range(nlab)]
        labels = [(i, co) for i, co in labels if any(co)]
        if not labels:
            continue
        beta = [rng.randint(0, 2) for _ in range(rank)]
        gens = []
        if rank > 1 and rng.random() < 0.5:
            gens = [[1 if j == rank - 1 else 0 for j in range(rank)]]
        k = rng.randint(1, 3)
        a = sorted(find_expanded_associations(k, labels, beta, gens))
        b = sorted(fallback(k, labels, beta, gens))
        assert a == b, (k, labels, beta, gens)


def test_ci_curve_in_p1xp1():
    # (1,2)-curve in P1xP1 is a P1; its ambient quantum multiplication by
    # c1 must have eigenvalues +-2 sqrt(y) (at y=1: +-2).  Regression for
    # the beta-enumeration gap (c1_CI = (1,0) has a zero entry) and for the
    # K-column / kept-node pairing convention.
    X = FlagVariety('A1xA1', [1, 2])
    K = [[1, 2]]
    fano, betas = X.fano_index_and_betas(K)
    assert fano == 1
    assert (2, 1) in [tuple(b) for b in betas]
    M, Gr, idx = X.small_quantum_multiplication(K, betas)
    ev = sorted(str(e) for e in X.eigenvalues(M, at_one=True))
    assert ev == ['-2', '2'], ev


def test_cy_complete_intersection():
    # quartic K3 in P^3: c1 = 0, c1* is the zero operator (no crash)
    X = projective_space(3)
    fano, betas = X.fano_index_and_betas([[4]])
    assert fano == 0
    M, Gr, idx = X.small_quantum_multiplication([[4]], betas)
    assert all(v == 0 for row in M for v in row)


def test_input_validation():
    # A malformed bundle spec must be rejected, not silently reinterpreted:
    # [[2,2,2]] on Picard-rank-1 P^4 used to compute the quadric O(2).
    X = projective_space(4)
    for bad in ([[2, 2, 2]], [[2], [-1]]):
        try:
            X.small_quantum_multiplication(bad)
            assert False, f'{bad} not rejected'
        except ValueError:
            pass
    try:
        X.gw([X.pt, X.pt], (1, 0))          # beta too short
        assert False, 'short beta not rejected'
    except ValueError:
        pass
    try:
        FlagVariety('A4', [0, 9])
        assert False, 'bad keep not rejected'
    except ValueError:
        pass


def test_soundness_of_gate_and_point_evaluation():
    # The two fast-path pillars, checked against the symbolic path:
    # (1) a dimension-gated (D=0) localization sum IS a constant equal to
    #     the numeric evaluation;
    # (2) a gated-out (D>0) sum is a genuinely nonzero homogeneous
    #     polynomial whose notebook-style t->0 limit is 0 = our gate.
    import sympy
    X = projective_space(2)
    raw = X.gw_raw([X.pt, X.pt], (1, 0))
    s = sympy.cancel(sympy.together(sympy.sympify(raw)))
    assert s.free_symbols == set() and s == 1
    assert X.gw([X.pt, X.pt], (1, 0)) == 1

    raw = X.gw_raw([X.pt] * 4, (1, 0))          # D = 2 > 0
    poly = sympy.cancel(sympy.together(sympy.sympify(raw)))
    assert poly != 0                             # sum itself is NOT zero
    t = sympy.Symbol('t')
    sub = {v: p * t for v, p in
           zip(sorted(poly.free_symbols, key=str), [10007, 10501])}
    assert sympy.limit(poly.subs(sub), t, 0) == 0
    assert X.gw([X.pt] * 4, (1, 0)) == 0


def test_fl123_matches_reference():
    # Externally supplied reference for Fl(1,2,3) (matrix, grading, Fano
    # index; its Cardano-form eigenvalues were verified numerically to
    # agree with this matrix's spectrum at random (y1, y2) and at y=1).
    X = FlagVariety('A2', [1, 2])
    fano, betas = X.fano_index_and_betas()
    assert fano == 2
    M, Gr, idx = X.small_quantum_multiplication(betas=betas)
    y1, y2 = X.bk.y(1), X.bk.y(2)
    assert M == [
        [0, 2 * y1, 2 * y2, 0, 0, 4 * y1 * y2],
        [2, 0, 0, 2 * y2, 0, 0],
        [2, 0, 0, 0, 2 * y1, 0],
        [0, 2, 4, 0, 0, 2 * y1],
        [0, 4, 2, 0, 0, 2 * y2],
        [0, 0, 0, 2, 2, 0]]
    from fractions import Fraction as Fr
    assert [Gr[a][a] for a in range(6)] == \
        [Fr(-3, 2), Fr(-1, 2), Fr(-1, 2), Fr(1, 2), Fr(1, 2), Fr(3, 2)]


def test_quadric_threefold_matches_notebook_cache():
    # The single complete computation cached in V3.nb's Output cells
    # (its last saved Mathematica run): the quadric threefold Q^3 in P^4.
    # Notebook printed: Fano Index = 3; SQM = {{0,0,6y,0},{3,0,0,6y},
    # {0,3,0,0},{0,0,3,0}}; Gr = diag(-3/2,-1/2,1/2,3/2);
    # eigenvalues {0} u 3*2^(2/3) y^(1/3) mu_3.
    X = projective_space(4)
    K = [[2]]
    fano, betas = X.fano_index_and_betas(K)
    assert fano == 3
    M, Gr, idx = X.small_quantum_multiplication(K, betas)
    y1 = X.bk.y(1)
    assert M == [[0, 0, 6 * y1, 0], [3, 0, 0, 6 * y1],
                 [0, 3, 0, 0], [0, 0, 3, 0]]
    from fractions import Fraction as Fr
    assert [Gr[a][a] for a in range(4)] == \
        [Fr(-3, 2), Fr(-1, 2), Fr(1, 2), Fr(3, 2)]


def test_quadric_surface():
    X = projective_space(3)
    K = [[2]]
    fano, betas = betas_and_fano_index(X, K)
    assert fano == 2
    pre = metric_matrix(X, K, list(range(len(X.classes))))
    cols, sub = reduce_matrix(X, pre)
    assert cols == [0, 1, 2]
    assert sub == [[0, 0, 2], [0, 2, 0], [2, 0, 0]]
    M, Gr, idx = X.small_quantum_multiplication(K, betas)
    ev = set(map(str, X.eigenvalues(M)))
    assert ev == {'-4*sqrt(y1)', '4*sqrt(y1)', '0'}


if __name__ == '__main__':
    import time
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            t0 = time.time()
            fn()
            print(f'{name}: ok ({time.time() - t0:.1f}s)')
    print('all tests passed')
