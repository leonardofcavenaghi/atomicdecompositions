"""Validation of the quantum-connection asymptotics module against
Kontsevich's "dimension theory" slides and Kuznetsov-component
dimensions of Fano hypersurfaces:

    dim Ku(X_d in P^n) = (n+1)(d-2)/d       (S^d = [(n+1)(d-2)] shift)

    python3 tests/test_quantum_connection.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import sympy
from fractions import Fraction

from gwflags import projective_space, FlagVariety
from gwflags.quantum_connection import spectral_exponents


def kg_of(X, K=None):
    M, Gr, idx = X.small_quantum_multiplication(K)
    subs = {}
    rows = []
    for row in M:
        r = []
        for v in row:
            e = sympy.sympify(v)
            subs.update({s: 1 for s in e.free_symbols})
            r.append(e)
        rows.append(r)
    Km = [[sympy.nsimplify(e.subs(subs)) for e in r] for r in rows]
    n = len(Km)
    Gm = [[sympy.Rational(Fraction(str(Gr[i][i]))) if i == j else 0
           for j in range(n)] for i in range(n)]
    return Km, Gm


def dims_by_sector(X, K=None):
    Km, Gm = kg_of(X, K)
    res = spectral_exponents(Km, Gm)
    return {z: (info['multiplicity'],
                sympy.nsimplify(info['dimension'], rational=True)
                if info['dimension'] is not None else None,
                info['exponents'])
            for z, info in res.items()}


def test_projective_spaces_all_zero():
    for n in (1, 2, 3):
        d = dims_by_sector(projective_space(n))
        for z, (m, dim, exps) in d.items():
            assert m == 1 and dim == 0, (n, z, dim)


def test_cubic_threefold_slide8():
    d = dims_by_sector(projective_space(4), [[3]])
    zero = d[sympy.Integer(0)]
    assert zero[0] == 2
    assert sorted(zero[2]) == [sympy.Rational(-5, 6),
                               sympy.Rational(-1, 6)]
    assert zero[1] == sympy.Rational(5, 3)          # dim Ku = 5/3
    for z, (m, dim, exps) in d.items():
        if z != 0:
            assert dim == 0, (z, dim)


def test_quadric_threefold():
    # Ku(quadric) = Clifford points: dimension 0 everywhere
    d = dims_by_sector(projective_space(4), [[2]])
    for z, (m, dim, exps) in d.items():
        assert dim == 0, (z, dim)


def test_cubic_fourfold_k3():
    # Ku(cubic 4-fold) is a K3 category: dimension 2 at the z=0 sector
    d = dims_by_sector(projective_space(5), [[3]])
    zero = d[sympy.Integer(0)]
    assert zero[0] == 2
    assert zero[1] == 2, zero
    for z, (m, dim, exps) in d.items():
        if z != 0:
            assert dim == 0, (z, dim)


def test_quartic_threefold_prediction():
    # index 1: spectrum {232, -24 x3}; the degenerate sector carries the
    # Kuznetsov component, predicted dimension (n+1)(d-2)/d = 5/2
    d = dims_by_sector(projective_space(4), [[4]])
    degenerate = [v for z, v in d.items() if v[0] > 1]
    assert len(degenerate) == 1
    m, dim, exps = degenerate[0]
    assert m == 3
    assert dim == sympy.Rational(5, 2), (dim, exps)
    simple = [v for z, v in d.items() if v[0] == 1]
    assert all(v[1] == 0 for v in simple)


def test_v8_new_data():
    # (2,2,2) in P^6: spectrum {56, -8 x3}; report the degenerate-sector
    # dimension as new data (sanity: real, in (0, dim X])
    X = FlagVariety('A6', [1])
    d = dims_by_sector(X, [[2], [2], [2]])
    degenerate = [v for z, v in d.items() if v[0] > 1]
    assert len(degenerate) == 1
    m, dim, exps = degenerate[0]
    print(f'   V8 degenerate sector: mult {m}, exponents {exps}, '
          f'dimension {dim}')
    assert m == 3
    dv = float(dim)
    assert 0 < dv <= 3


if __name__ == '__main__':
    import time
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            t0 = time.time()
            fn()
            print(f'{name}: ok ({time.time() - t0:.1f}s)')
    print('all quantum-connection tests passed')
