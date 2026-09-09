"""Forensic comparison of the GM-20 quantum matrix (Fl(1,2,5) cap
O(0,1)+O(0,2)+O(1,0)) against the earlier reference computation.

Establishes, computationally, the two findings of discrepancy.md:
  (1) restricted to curve classes of total degree <= 4, the two matrices
      are conjugate by an explicit grading-compatible integer basis
      change P (identity except [[1,2],[0,-2]] on the two degree-3
      slots) — i.e. the reference is CORRECT at degrees <= 4;
  (2) the full matrix additionally carries degree-5 terms (certified
      nonzero by the divisor axiom) that the reference lacks.

    python3 tests/gm20_forensics.py       (several minutes: two full
                                           GM-20 matrix builds plus the
                                           degree-5 invariant sweep)
"""

import os
import sys

import sympy

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from reference_cases import CASES
from gwflags import FlagVariety


def main():
    label, algebra, keep, K, refm = next(c for c in CASES if 'GM-20' in c[0])
    R = sympy.Matrix([[sympy.sympify(v) for v in row] for row in refm])

    X = FlagVariety(algebra, keep)
    fano, betas = X.fano_index_and_betas(K)
    M, Gr, idx = X.small_quantum_multiplication(K, betas, workers=8)
    O = sympy.Matrix([[sympy.sympify(v) for v in row] for row in M])

    b4 = [b for b in betas if sum(b) <= 4]
    X2 = FlagVariety(algebra, keep)
    M4, _, _ = X2.small_quantum_multiplication(K, b4, workers=8)
    O4 = sympy.Matrix([[sympy.sympify(v) for v in row] for row in M4])

    # (1) basis-change solve, blockwise on equal-grading groups
    n = O.rows
    groups = {}
    for a in range(n):
        groups.setdefault(str(Gr[a][a]), []).append(a)
    P = sympy.zeros(n, n)
    unknowns = []
    for mem in groups.values():
        for i in mem:
            for j in mem:
                v = sympy.Symbol(f'p_{i}_{j}')
                P[i, j] = v
                unknowns.append(v)
    eqs = sympy.expand(P * O4 - R * P)
    sol = sympy.solve([eqs[i, j] for i in range(n) for j in range(n)],
                      unknowns, dict=True)
    assert sol, 'no basis change exists — reference differs at degree <= 4'
    Pc = P.subs(sol[0]).subs({v: 1 for v in P.subs(sol[0]).free_symbols})
    assert Pc.det() != 0
    assert sympy.expand(Pc * O4 * Pc.inv() - R) == sympy.zeros(n, n)
    print('(1) P * M_ours^{<=4} * P^-1 == M_reference  EXACTLY, with P =')
    sympy.pprint(Pc)
    print(f'    det P = {Pc.det()}  (identity outside the degree-3 block)')

    # spectra agree once truncated
    s = {v: 1 for v in (O4.free_symbols | R.free_symbols)}
    specA = sorted((complex(x) for x, m in O4.subs(s).eigenvals().items()
                    for _ in range(m)), key=lambda z: (z.real, z.imag))
    specB = sorted((complex(x) for x, m in R.subs(s).eigenvals().items()
                    for _ in range(m)), key=lambda z: (z.real, z.imag))
    assert all(abs(a - b) < 1e-8 for a, b in zip(specA, specB))
    print('    spectra at y=1 of truncated-ours and reference: identical')

    # (2) the degree-5 difference
    D = sympy.expand(O - O4)
    cells = [(i, j, D[i, j]) for i in range(n) for j in range(n)
             if D[i, j] != 0]
    print('(2) degree-5 terms present in the full matrix, absent from the '
          'reference:')
    for i, j, v in cells:
        print(f'    cell ({i},{j}): {v}')
    y1, y2 = sympy.symbols('y1 y2')
    for i, j, v in cells:
        p = sympy.Poly(v, y1, y2)
        assert all(sum(m) == 5 for m in p.monoms())
    # the underlying certified invariants
    for beta, expect in [((2, 3, 0, 0), 224), ((1, 4, 0, 0), 128)]:
        by = {}
        for m in X.classes:
            by.setdefault(X.wd.length(m), []).append(m)
        vals = set()
        for a in by.get(4, []):
            for b in by.get(4, []):
                vals.add(X.gw([a, b], beta, K))
        assert expect in vals, (beta, vals)
        print(f'    beta={beta[:2]}: certified two-point invariant '
              f'{expect} (nonzero)')
    print('\nconclusion: reference correct at degrees <= 4 up to the basis '
          'change P; genuinely missing the (nonzero) degree-5 classes.')


if __name__ == '__main__':
    main()
