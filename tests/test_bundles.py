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


if __name__ == '__main__':
    import time
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            t0 = time.time()
            fn()
            print(f'{name}: ok ({time.time() - t0:.1f}s)')
    print('all bundle tests passed')
