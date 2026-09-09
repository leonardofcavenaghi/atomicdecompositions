"""Regression: gwflags vs the reference matrices of full_test_list.tex.

Runs every transcribed case except the GM-20 fourfold, whose comparison is
adjudicated separately (see discrepancy.md and tests/gm20_forensics.py:
the reference is correct at curve degrees <= 4 up to an explicit basis
change on the two degree-3 classes, but misses the degree-5 curve
classes, which are certified nonzero by the divisor axiom).

    python3 tests/test_reference_list.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from reference_cases import CASES
from verify_full_list import verify

DISPUTED = ('GM-20',)


def test_reference_matrices():
    failures = []
    for (label, algebra, keep, K, ref) in CASES:
        if any(d in label for d in DISPUTED) or ref is None:
            continue
        status, _, took = verify(label, algebra, keep, K, ref)
        print(f'[{took:6.1f}s] {label}: {status}', flush=True)
        if not status.startswith('MATCH'):
            failures.append((label, status))
    assert not failures, failures


if __name__ == '__main__':
    test_reference_matrices()
    print('all reference cases match')
