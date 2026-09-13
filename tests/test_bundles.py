"""Regressions for homogeneous-bundle twists (gwflags.bundles).

The sharp checks are classical isomorphisms where the twisted ambient
theory must reproduce untwisted answers computed by the same engine:

    Z(Gr(2,4), Q)        =  P^2      (section v: planes containing v)
    Z(Gr(2,5), Q)        =  P^3
    Z(Gr(2,5), Sym^2 S*) =  OG(2,5) = B2/P_2   (isotropic planes)

plus conservativity (legacy split rows == O-bundle objects) and the
convexity gate (tautological S must be rejected, S* accepted).

    python3 tests/test_bundles.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import sympy

from gwflags import FlagVariety, projective_space, grassmannian
from gwflags.bundles import (O, taut_sub, taut_quot, dual, osum, tensor,
                             sym, wedge)
from gwflags.quantum import spectrum_at_one


def sqm(X, K=None):
    M, Gr, idx = X.small_quantum_multiplication(K)
    return M


def canon(M, ysub=None):
    out = []
    for row in M:
        r = []
        for v in row:
            e = sympy.sympify(v)
            if ysub:
                e = e.subs(ysub)
            r.append(sympy.expand(e))
        out.append(r)
    return out


def spectra_match(M1, M2, tol=1e-8):
    s1, s2 = spectrum_at_one(M1), spectrum_at_one(M2)
    return len(s1) == len(s2) and all(abs(a - b) < tol
                                      for a, b in zip(s1, s2))


def test_legacy_rows_equal_bundle_objects():
    # quadric threefold: [[2]] vs O(2)
    X1 = projective_space(4)
    M1 = sqm(X1, [[2]])
    X2 = projective_space(4)
    M2 = sqm(X2, O(X2, 2))
    assert canon(M1) == canon(M2)
    # P3xP3 / O(1,1)+O(1,1): rows vs bundle sum
    Y1 = FlagVariety('A3xA3', [1, 4])
    N1 = sqm(Y1, [[1, 1], [1, 1]])
    Y2 = FlagVariety('A3xA3', [1, 4])
    N2 = sqm(Y2, osum(O(Y2, 1, 1), O(Y2, 1, 1)))
    assert canon(N1) == canon(N2)


def test_convexity_gate():
    X = grassmannian(2, 4)
    S = taut_sub(X, 2)
    assert not S.is_curvewise_convex()
    try:
        X.small_quantum_multiplication(S)
        assert False, 'tautological S not rejected'
    except ValueError as e:
        assert 'S*' in str(e)
    assert dual(S).is_curvewise_convex()
    assert taut_quot(X, 2).is_curvewise_convex()


def test_z_gr24_quot_is_p2():
    X = grassmannian(2, 4)
    Q = taut_quot(X, 2)
    assert Q.rank == 2
    fano, betas = X.fano_index_and_betas(Q)
    assert fano == 3                     # = index of P^2
    M = sqm(X, Q)
    P2 = sqm(projective_space(2))
    y1, y2 = sympy.symbols('y1 y2')
    assert canon(M, {y2: y1}) == canon(P2), (M, P2)


def test_z_gr25_quot_is_p3():
    X = grassmannian(2, 5)
    Q = taut_quot(X, 2)
    assert Q.rank == 3
    fano, betas = X.fano_index_and_betas(Q)
    assert fano == 4                     # = index of P^3
    M = sqm(X, Q)
    P3 = sqm(projective_space(3))
    y1, y2 = sympy.symbols('y1 y2')
    assert canon(M, {y2: y1}) == canon(P3), (M, P3)


def test_z_gr25_sym2sdual_is_og25():
    X = grassmannian(2, 5)
    E = sym(2, dual(taut_sub(X, 2)))
    assert E.rank == 3
    M = sqm(X, E)
    B = FlagVariety('B2', [2])           # OG(2,5)
    MB = sqm(B)
    assert spectra_match(M, MB), (spectrum_at_one(M), spectrum_at_one(MB))


def test_constructor_algebra():
    X = grassmannian(2, 5)
    Sd = dual(taut_sub(X, 2))
    # det S* = O(1): wedge^2 S* equals O(1) as a character (mod the
    # torus-trivial trace direction)
    W = wedge(2, Sd)
    assert W.rank == 1
    assert W.reduced_weights() == O(X, 1).reduced_weights()
    # tensor rank multiplicativity, sym rank formula
    assert tensor(Sd, taut_quot(X, 2)).rank == 2 * 3
    assert sym(3, Sd).rank == 4
    # c1 coordinates: det Q = O(1) too
    assert taut_quot(X, 2).c1_coordinates() == [1]
    assert Sd.c1_coordinates() == [1]


def test_taut_sub_and_quot_gr36():
    """taut_sub and taut_quot on Gr(3,6): rank, convexity, and c1."""
    X = grassmannian(3, 6)
    S = taut_sub(X, 3)
    Q = taut_quot(X, 3)
    # rank checks: S = k=3 planes, Q = n-k=3 complement
    assert S.rank == 3
    assert Q.rank == 3
    # S is NOT globally generated (negative splitting degrees on some curves)
    assert not S.is_curvewise_convex()
    # S* and Q are convex
    assert dual(S).is_curvewise_convex()
    assert Q.is_curvewise_convex()
    # det S* = det Q = O(1): both c1 coords equal [1] on the Picard-rank-1 space
    assert dual(S).c1_coordinates() == [1]
    assert Q.c1_coordinates() == [1]
    # taut_sub should be rejected by small_quantum_multiplication
    try:
        X.small_quantum_multiplication(S)
        assert False, 'S on Gr(3,6) not rejected'
    except ValueError as e:
        assert 'S*' in str(e)


def test_gr36_quot_basic():
    """Z(Gr(3,6), Q): verify basic properties of the quotient bundle section."""
    X = grassmannian(3, 6)
    Q = taut_quot(X, 3)
    assert Q.rank == 3
    fano, betas = X.fano_index_and_betas(Q)
    assert fano == 5
    # The SQM should produce a square matrix
    M = sqm(X, Q)
    assert len(M) > 0 and all(len(row) == len(M) for row in M)


def test_eval_at_y_p1():
    """Evaluate-at-y: P^1 SQM with y1=4 gives concrete integer matrix."""
    X = projective_space(1)
    M, Gr, idx = X.small_quantum_multiplication()
    y1 = X.bk.y(1)
    # M = [[0, 2y1], [2, 0]]; at y1=4 -> [[0, 8], [2, 0]]
    M_at4 = canon(M, {y1: 4})
    assert M_at4 == [[0, 8], [2, 0]]
    # eigenvalues at y1=4 should be ±4
    ev4 = sorted(str(e) for e in X.eigenvalues(M_at4))
    assert set(ev4) == {'-4', '4'}, ev4


def test_eval_at_y_p2():
    """Evaluate-at-y: P^2 SQM with y1=1 recovers the classical (q=1) matrix."""
    X = projective_space(2)
    M, Gr, idx = X.small_quantum_multiplication()
    y1 = X.bk.y(1)
    # M = [[0, 0, 3y1], [3, 0, 0], [0, 3, 0]]; at y1=1 -> classical q=1 form
    M_at1 = canon(M, {y1: 1})
    assert M_at1 == [[0, 0, 3], [3, 0, 0], [0, 3, 0]]
    # characteristic polynomial of c1* at q=1 is lambda^3 - 27 = 0
    import sympy as sp
    mat = sp.Matrix(M_at1)
    lam = sp.Symbol('lambda')
    charpoly = mat.charpoly(lam)
    assert sp.expand(charpoly.as_expr()) == sp.expand(lam**3 - 27)


def test_billey_schubert_rename_regression():
    """Direct regression: billey() parameter was renamed shubert->schubert.
    The rename was purely cosmetic; verify the formula still gives correct
    restrictions on Gr(2,4) (values fixed by the Bertram presentation)."""
    from gwflags.localization import GWCalculator
    from gwflags.symbolic import NumericBackend
    G = grassmannian(2, 4)
    calc = GWCalculator(G.rs, None, NumericBackend(seed=42), wd=G.wd)
    bylen = {}
    for m in G.classes:
        bylen.setdefault(G.wd.length(m), []).append(m)
    # sigma_1 restricted to the point class (longest element) must be nonzero
    s1 = bylen[1][0]
    pt = bylen[4][0]
    val = calc.billey(s1, pt)
    assert val != 0, 'billey(sigma_1, pt) should be nonzero'
    # sigma_0 (identity class) restricted to any vertex must be 1
    s0 = G.wd.group[0]
    for v in G.classes:
        assert calc.billey(s0, v) == 1, f'billey(id, {v}) != 1'
    # Cross-check: GW invariant agrees between both engines
    from gwflags.gkm import gkm_gw
    bk = NumericBackend(seed=43)
    calc2 = GWCalculator(G.rs, None, bk, wd=G.wd)
    s21 = bylen[3][0]
    beta = (0, 1, 0)
    ours = calc2.gw_invariant([s1, s21, pt], beta)
    theirs = gkm_gw(G, [s1, s21, pt], list(beta), backend=bk)
    assert ours == theirs == 1, (ours, theirs)


if __name__ == '__main__':
    import time
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            t0 = time.time()
            fn()
            print(f'{name}: ok ({time.time() - t0:.1f}s)')
    print('all bundle tests passed')
