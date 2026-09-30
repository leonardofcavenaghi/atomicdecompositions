"""Regression checks for the Peskine sixfold support.

These tests cover the geometry-aware bundle representation and the A9/P
partial-flag backend.  They deliberately do not launch the full positive
degree localization sum: that path is an exploratory backend for this large
example, while the construction and the classical twisted metric are the
stable API surface tested here.
"""

import os
import sys
from fractions import Fraction

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from gwflags import (FlagVariety, PeskineBundle, peskine_bundle, taut_sub,
                     taut_quot, dual, tensor, wedge, quot)
from gwflags.bundles import HomogeneousBundle


@pytest.fixture(scope='module')
def peskine_data():
    X = FlagVariety('A9', [1, 4])
    return X, peskine_bundle(X)


def _simple_root_index(X, node):
    root = tuple(1 if j == node - 1 else 0 for j in range(X.rs.rank))
    return X.rs.positive_roots.index(root)


def test_a9_partial_backend_is_small_but_complete(peskine_data):
    X, _ = peskine_data
    assert len(X.classes) == 840
    assert X.dimension == 27
    assert len(X.wd.group) == 3628800
    assert X.wd.length(X.pt) == 27
    assert all(X.class_of_word(word) == cls
               for word, cls in zip(X.class_words(), X.classes))


def test_peskine_bundle_uses_actual_edge_restrictions(peskine_data):
    X, K = peskine_data
    assert K.rank == 21
    assert K.c1_coordinates() == [13, 5]
    assert K.is_curvewise_convex()
    assert K.effective_beta_generators == (
        (1, 0, 0, 3, 0, 0, 0, 0, 0),)

    alpha1 = K.edge_splitting(_simple_root_index(X, 1))
    alpha4 = K.edge_splitting(_simple_root_index(X, 4))
    assert sorted(degree for _, degree in alpha1) == [0] * 8 + [1] * 13
    assert sorted(degree for _, degree in alpha4) == [0] * 16 + [1] * 5


def test_original_fiber_weight_expression_exposes_the_old_failure(peskine_data):
    X, K = peskine_data
    line = taut_sub(X, 1)
    raw = tensor(
        quot(wedge(2, dual(taut_quot(X, 1))),
             wedge(2, dual(taut_quot(X, 4)))),
        dual(line))
    assert isinstance(raw, HomogeneousBundle)
    assert raw.rank == K.rank
    assert min(raw.splitting_degrees(_simple_root_index(X, 4))) < 0
    with pytest.raises(ValueError, match='splitting degree is negative'):
        X._check_K(raw)


def test_peskine_beta_semigroup_and_alias(peskine_data):
    X, K = peskine_data
    assert PeskineBundle(X).key() == K.key()
    fano, betas = X.fano_index_and_betas(K)
    assert fano == 3
    assert betas == [
        (0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1, 0, 0, 3, 0, 0, 0, 0, 0),
        (2, 0, 0, 6, 0, 0, 0, 0, 0),
    ]


def test_peskine_gui_and_cli_aliases(peskine_data):
    X, K = peskine_data
    from gwflags.cli import parse_k as cli_parse_k
    from gwflags.gui import parse_k as gui_parse_k
    for parser in (cli_parse_k, gui_parse_k):
        assert parser('Peskine()', X).key() == K.key()
        assert parser('peskine()', X).key() == K.key()


def test_peskine_degree_zero_ambient_operator(peskine_data):
    """Exercise the direct A9 backend and the classical twisted metric."""
    X, K = peskine_data
    zero = (0,) * X.rs.rank
    matrix, grading, indices = X.small_quantum_multiplication(
        K, betas=[zero])
    assert indices == list(range(10))
    assert [grading[i][i] for i in range(10)] == [
        -3, -2, -1, 0, 1, 2, 3, -1, 0, 1]
    assert matrix == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, Fraction(-14, 5), 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, -5, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0, Fraction(153, 4)],
        [0, 0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, Fraction(13, 5), 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 4, 0],
    ]
