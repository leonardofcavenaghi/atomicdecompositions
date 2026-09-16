"""Regression for the published Fanography 1-10 homogeneous-bundle matrix.

The full localization computation is intentionally not part of the default test
suite: the degree-4 block is a long-running calculation.  The checked-in
snapshot is instead checked against the independent regularized quantum period
for V(3,22), and the Markdown card is checked against that snapshot.  The full
software command remains documented in the audit report for a periodic review.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from catalog_inputs import compact_bundle, fanography_specs

DATA = json.loads((ROOT / "tests" / "data" / "fanography_1_10.json").read_text(encoding="utf-8"))


def _snapshot_matrix():
    return sp.Matrix([[sp.sympify(entry) for entry in row] for row in DATA["matrix"]])


def _regularized_period(matrix: sp.Matrix, order: int) -> list[sp.Expr]:
    """Return d! times the fourth formal-solution coefficient through ``order``."""
    q = sp.Symbol("q")
    y3 = sp.Symbol("y3")
    M = matrix.subs({y3: q})
    max_degree = max(sp.degree(entry, q) or 0 for entry in M)
    coefficients = [M.applyfunc(lambda entry, degree=degree: sp.expand(entry).coeff(q, degree))
                    for degree in range(max_degree + 1)]
    identity = sp.eye(M.rows)
    state = [sp.Matrix([0, 0, 0, 1])]
    for degree in range(1, order + 1):
        rhs = sp.zeros(M.rows, 1)
        for shift in range(1, min(max_degree, degree) + 1):
            rhs += coefficients[shift] * state[degree - shift]
        state.append((degree * identity - coefficients[0]).inv() * rhs)
    return [sp.Integer(1)] + [sp.factorial(degree) * state[degree][3]
                              for degree in range(1, order + 1)]


def test_fanography_1_10_input_is_centralized():
    spec = fanography_specs()["1-10"]
    assert spec["algebra"] == "A6"
    assert spec["keep"] == [3]
    assert compact_bundle(spec).startswith("osum(wedge(2, dual(taut_sub(X, 3)))")
    assert spec["matrix_at_one"] == DATA["matrix_at_one"]


def test_fanography_1_10_matrix_matches_published_card():
    text = (ROOT / "docs" / "catalog" / "fanography.md").read_text(encoding="utf-8")
    card = re.search(r'### Fano Variety 1-10\n\?\?\? example "1-10"(.*?)(?=\n### Fano Variety |\Z)', text, re.S)
    assert card is not None
    block = re.search(r"\\begin\{bmatrix\}(.*?)\\end\{bmatrix\}", card.group(1), re.S)
    assert block is not None
    rows = [[entry.strip() for entry in row.strip().split("&")] for row in re.split(r"\\\\", block.group(1)) if row.strip()]
    assert rows == DATA["matrix_at_one"]


def test_fanography_1_10_period_regression():
    computed = _regularized_period(_snapshot_matrix(), len(DATA["period"]) - 1)
    expected = [sp.Integer(value) for value in DATA["period"]]
    assert computed == expected
