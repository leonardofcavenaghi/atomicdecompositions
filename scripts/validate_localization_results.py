#!/usr/bin/env python3
"""Check exact saved results, executable geometry and their published cards.

This validates completed outputs; it does not repeat the localization sums.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from gwflags import FlagVariety
from gwflags.cli import parse_k
from gwflags.cintersection import ci_rank
from gwflags.quantum import chern_class_ci, chern_class_vector
from scripts.catalog_results import DATA, generated_pages
from scripts.generate_catalog_index import render_index
from scripts.validate_catalog import cards, FIELD_RE, MATRIX_RE

FIELDS = {'id', 'title', 'catalog_page', 'catalog_anchor', 'catalog_aliases',
          'input', 'dimension', 'fano_index', 'curve_classes', 'basis_indices',
          'basis_degrees', 'basis_words', 'matrix_symbolic', 'matrix_at_one',
          'grading', 'charpoly'}


def parse_display(text):
    text = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1)/(\2)', text)
    return sp.sympify(text.replace('\\cdot', '*').strip())


def validate():
    data = json.loads(DATA.read_text(encoding='utf-8'))
    assert data['schema_version'] == 1
    records = data['examples']
    assert len({r['id'] for r in records}) == len(records)
    varieties = {}
    catalog_cards = {}
    for path in (ROOT / 'docs/catalog').glob('*.md'):
        for card in cards(path):
            title = 'Fanography ' + card.title if path.name == 'fanography.md' else card.title
            catalog_cards[(path.name, title)] = card
    for record in records:
        name = record['title']
        assert set(record) == FIELDS, (name, 'unexpected data fields')
        spec = record['input']
        assert set(spec) == {'algebra', 'keep', 'bundle'}
        key = (spec['algebra'], tuple(spec['keep']))
        if key not in varieties:
            varieties[key] = FlagVariety(spec['algebra'], spec['keep'])
        X = varieties[key]
        K = parse_k(spec['bundle'], X) if isinstance(spec['bundle'], str) else spec['bundle']
        assert X.dimension - (ci_rank(K) if K else 0) == record['dimension'], (name, 'dimension')
        index, betas = X.fano_index_and_betas(K)
        assert index == record['fano_index'], (name, 'Fano index')
        assert [list(b) for b in betas] == record['curve_classes'], (name, 'automatic curve list')
        words = X.class_words()
        assert [list(words[i]) for i in record['basis_indices']] == record['basis_words'], (name, 'basis order')
        assert [len(w) for w in record['basis_words']] == record['basis_degrees'], (name, 'basis degrees')
        n = len(record['basis_indices'])
        M = sp.Matrix([[sp.sympify(v) for v in row] for row in record['matrix_symbolic']])
        A = sp.Matrix([[sp.Rational(v) for v in row] for row in record['matrix_at_one']])
        G = sp.Matrix([[sp.Rational(v) for v in row] for row in record['grading']])
        assert M.shape == A.shape == G.shape == (n, n), (name, 'matrix shape')
        assert G == sp.diag(*[sp.Rational(d) - sp.Rational(record['dimension'], 2) for d in record['basis_degrees']]), (name, 'grading')
        assert M.subs({s: 1 for s in M.free_symbols}) == A, (name, 'specialization')
        lam = sp.Symbol('lambda')
        expected_charpoly = sp.sympify(record['charpoly'].replace('lambda', '_lambda'), locals={'_lambda': lam})
        assert sp.expand(A.charpoly(lam).as_expr() - expected_charpoly) == 0, (name, 'characteristic polynomial')
        variables = [sp.Symbol(f'y{i}') for i in spec['keep']]
        assert M.free_symbols <= set(variables), (name, 'Novikov labels')
        chern = chern_class_ci(X, K) if K else chern_class_vector(X)
        for i in range(n):
            for j in range(n):
                if M[i, j] == 0:
                    continue
                for powers, coefficient in sp.Poly(M[i, j], *variables).terms():
                    beta = [0] * X.rs.rank
                    for node, power in zip(spec['keep'], powers):
                        beta[node - 1] = power
                    assert beta in record['curve_classes'], (name, 'unsupported monomial')
                    weight = sum(a * b for a, b in zip(chern, beta))
                    assert weight + record['basis_degrees'][i] - record['basis_degrees'][j] == 1, (name, 'degree axiom')
                    assert coefficient.is_Rational, (name, 'nonrational coefficient')
        targets = record['catalog_aliases'] or [{'page': record['catalog_page'], 'title': name}]
        for target in targets:
            card = catalog_cards.get((target['page'], target['title']))
            if card is None:
                assert target['page'] == 'flag_varieties.md', (name, 'missing catalog card')
                continue
            for field, expected in [('dimension', record['dimension']), ('index', index), ('rank', n)]:
                assert int(FIELD_RE[field].search(card.text).group(1)) == expected, (name, 'card ' + field)
            match = MATRIX_RE.search(card.text)
            assert match, (name, 'missing displayed matrix')
            rows = [[parse_display(cell) for cell in row.split('&')] for row in match.group(1).split('\\\\') if row.strip()]
            display = sp.Matrix(rows)
            assert display.subs({s: 1 for s in display.free_symbols}) == A, (name, 'displayed matrix')
    for path, expected in generated_pages(records).items():
        assert path.read_text(encoding='utf-8') == expected, f'Stale generated page: {path.name}'
    assert (ROOT / 'docs/catalog/index.md').read_text(encoding='utf-8') == render_index(), 'Stale master index'
    print(f'Validated {len(records)} exact results: geometry, automatic curves, ordered bases, grading, specialization, characteristic polynomials and published matrices.')


if __name__ == '__main__':
    validate()
