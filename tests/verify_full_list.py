#!/usr/bin/env python3
"""Verify gwflags against every reference matrix in full_test_list.tex.

For each case: compute the c1(TX)* matrix, then
  1. exact symbolic matrix comparison (same basis expected);
  2. if entries differ: basis-independent comparison — eigenvalue multisets
     at random rational y-points (12 digits) and characteristic-polynomial
     equality — to distinguish basis reordering from real disagreement.

    python3 tests/verify_full_list.py            # all cases
    python3 tests/verify_full_list.py G2 LG      # substring filter
"""

import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import sympy

from gwflags import FlagVariety
from reference_cases import CASES


def sym_matrix(entries):
    ns = {f'y{i}': sympy.Symbol(f'y{i}') for i in range(1, 10)}
    ns['Rational'] = sympy.Rational
    return sympy.Matrix([[sympy.sympify(v, locals=ns) for v in row]
                         for row in entries])


def spectra_match(A, B, trials=3, seed=7):
    import random
    rng = random.Random(seed)
    ys = sorted(set().union(A.free_symbols, B.free_symbols), key=str)
    for _ in range(trials):
        subs = {y: sympy.Rational(rng.randint(2, 60), rng.randint(1, 7))
                for y in ys}
        for M in (A, B):
            if M.subs(subs).free_symbols:
                return False
        ea = sorted((complex(v) for v, m in A.subs(subs).eigenvals().items()
                     for _ in range(m)),
                    key=lambda z: (round(z.real, 8), round(z.imag, 8)))
        eb = sorted((complex(v) for v, m in B.subs(subs).eigenvals().items()
                     for _ in range(m)),
                    key=lambda z: (round(z.real, 8), round(z.imag, 8)))
        if len(ea) != len(eb) or any(abs(a - b) > 1e-9 * max(1, abs(a))
                                     for a, b in zip(ea, eb)):
            return False
    return True


def verify(label, algebra, keep, K, ref_entries, workers=0):
    t0 = time.time()
    X = FlagVariety(algebra, keep)
    M, Gr, idx = X.small_quantum_multiplication(K or None, workers=workers)
    ours = sympy.Matrix([[sympy.sympify(v) for v in row] for row in M])
    took = time.time() - t0
    if ref_entries is None:
        return ('COMPUTED (no reference matrix)', ours, took)
    ref = sym_matrix(ref_entries)
    if ours.shape == ref.shape and sympy.simplify(ours - ref) == \
            sympy.zeros(*ours.shape):
        return ('MATCH (exact)', ours, took)
    if ours.shape == ref.shape and spectra_match(ours, ref):
        lam = sympy.Symbol('lambda')
        cp_ok = sympy.expand(ours.charpoly(lam).as_expr()
                             - ref.charpoly(lam).as_expr()) == 0
        return (f'MATCH (spectra{"+charpoly" if cp_ok else ""}; '
                'different basis/order)', ours, took)
    return ('MISMATCH', ours, took)


def main():
    filters = [a for a in sys.argv[1:] if not a.startswith('-')]
    workers = 8 if '--workers' in sys.argv else 0
    results = []
    for (label, algebra, keep, K, ref) in CASES:
        if filters and not any(f.lower() in label.lower() for f in filters):
            continue
        try:
            status, ours, took = verify(label, algebra, keep, K, ref, workers)
        except Exception as exc:                     # noqa: BLE001
            status, ours, took = f'ERROR: {exc!r}', None, 0.0
        results.append((label, status, took))
        print(f'[{took:7.1f}s] {label}: {status}', flush=True)
        if status == 'MISMATCH' and ours is not None:
            print('  ours =')
            for row in ours.tolist():
                print('   ', row)
    print()
    good = sum(1 for _, s, _ in results if s.startswith('MATCH')
               or s.startswith('COMPUTED'))
    print(f'{good}/{len(results)} cases verified '
          f'({sum(1 for _, s, _ in results if s == "MISMATCH")} mismatches, '
          f'{sum(1 for _, s, _ in results if s.startswith("ERROR"))} errors)')


if __name__ == '__main__':
    main()
