"""Regression tests for parameter names and genuinely unmarked CLI calls."""
import contextlib
import io
import unittest

import sympy as sp

from gwflags import FlagVariety
from gwflags.cli import main, parse_classes


class NotationTests(unittest.TestCase):
    def test_non_a_quantum_operator_preserves_quadric_relation(self):
        X = FlagVariety('C2', [2])
        M, grading, basis = X.small_quantum_multiplication()
        z = sp.Symbol('z')
        y = sp.Symbol('y1')
        self.assertEqual(sp.expand(sp.Matrix(M).charpoly(z).as_expr()), z**4 - 108*y*z)
        self.assertEqual(X.novikov_names, ('y1',))
        legacy = FlagVariety('C2', [2], novikov_convention='ambient')
        old, old_grading, old_basis = legacy.small_quantum_multiplication()
        self.assertEqual(sp.Matrix(old).subs(sp.Symbol('y2'), y), sp.Matrix(M))
        self.assertEqual((grading, basis), (old_grading, old_basis))

    def test_a_type_preserves_published_ambient_names(self):
        X = FlagVariety('A3', [2])
        self.assertEqual(X.novikov_names, ('y2',))
        self.assertEqual(X.novikov_metadata['variables'], [{'node': 2, 'name': 'y2'}])

    def test_empty_text_is_not_a_unit_insertion(self):
        X = FlagVariety('A3', [1])
        self.assertEqual(parse_classes('', X), [])
        self.assertEqual(len(parse_classes('id', X)), 1)
        self.assertEqual(X.gw([], (1,), [[3]]), 27)

    def test_cli_unmarked_cubic_surface(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(io.StringIO()):
            main(['A3', '--keep', '1', '-K', '3', 'gw', '--beta', '1', '--classes', ''])
        self.assertIn('GW invariant = 27', output.getvalue())

    def test_bad_convention_rejected(self):
        with self.assertRaises(ValueError):
            FlagVariety('A2', [1], novikov_convention='typo')


if __name__ == '__main__':
    unittest.main()

