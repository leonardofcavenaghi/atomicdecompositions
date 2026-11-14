"""Check displayed first-Chern spectra, cyclic determinants and exponent multisets.

All characteristic polynomials and Krylov determinants are checked against
exact source matrices, independently of Markdown wording. Flag connection
results are also recomputed with the versioned exact connection algorithm.
This does not repeat the localization sums that produced those matrices.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import importlib.util
import argparse
import json
import re
import sys

import sympy as s
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
                                       implicit_multiplication_application)
R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R))
from scripts.catalog_spectra import section
z, x, t = s.symbols('z x t')


def read(name):
    return json.loads((R / 'docs/data' / name).read_text())


def expression(tex):
    tex = tex.replace(r'\!', '').replace(r'\\&', '').replace(r'\,', '').replace(r'\left', '').replace(r'\right', '')
    tex = re.sub(r'y_\{(\d+)\}', r'y\1', tex)
    tex = re.sub(r'\^\{(-?\d+)\}', r'**(\1)', tex).replace('^', '**')
    tex = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'((\1)/(\2))', tex)
    return parse_expr(tex, local_dict={'x': x, **{f'y{i}': s.Symbol(f'y{i}') for i in range(1, 20)}},
                      transformations=standard_transformations + (implicit_multiplication_application,))


def positive(poly, variable):
    return s.Poly(poly.subs(variable, -z), z).monic().as_expr()


def multiset(values):
    return Counter(Fraction(v) for v in values)


def expand_counts(values):
    return [v for v, n in values.items() for _ in range(n)]


def algebraic_scalar_sector(engine, M, G, point, factor, multiplicity):
    """Check a nonlinear sector at every exact conjugate in two covector orders.

    This calls the versioned scalar-filtration and shifted-indicial routines
    directly; the runtime's high-level report currently skips these sectors.
    Integer changes of exponent representatives are allowed between covectors.
    """
    values = {s.Symbol(k): s.Rational(v) for k, v in point.items()}
    K, grade = -M.subs(values), G.subs(values)
    roots = s.solve(factor, t)
    assert len(roots) == s.degree(factor, t) == 2
    result = None
    for order in [list(range(K.rows)), list(range(1, K.rows)) + [0]]:
        filtration = engine.scalar_filtration(K.extract(order, order), grade.extract(order, order))
        assert filtration['all_relations_verified']
        for eigenvalue in roots:
            classes, representatives = Counter(), Counter()
            total = 0
            for block in filtration['blocks']:
                polynomial, _ = engine.shifted_indicial(block['coefficients'], eigenvalue)
                exponents = engine.exponents(polynomial)
                classes.update(exponents['classes_mod_Z'])
                representatives.update(exponents['representatives'])
                total += s.degree(polynomial, engine.s)
            assert total == multiplicity == sum(classes.values())
            if result is None:
                result = dict(classes_mod_Z=dict(classes), representatives=dict(representatives))
            assert classes == Counter(result['classes_mod_Z'])
    return result


def validate(shard=None):
    spectral = read('spectral-data.json')['records']
    catalog = {r['id']: r for r in read('catalog-records.json')['records']}
    flags = {r['id']: r for name, key in [('localization-results.json', 'examples'),
                                         ('flag-fourfolds.json', 'records')]
             for r in read(name)[key]}
    toric = {r['id']: r for name in ['toric-fourfolds.json', 'toric-fivefolds.json']
             for r in read(name)['records']}
    old_connection = {r['id']: r for r in read('connection-exponents.json')['records']}
    assert len(spectral) == len(catalog) == len({r['id'] for r in spectral})
    assert {r['id'] for r in spectral} == set(flags) | set(toric) == set(catalog)
    if shard is not None:
        index, count = map(int, shard.split('/'))
        assert count > 0 and 0 <= index < count, 'Shard must be INDEX/COUNT, with zero-based INDEX'
        spectral = [r for i, r in enumerate(spectral) if i % count == index]
    spec = importlib.util.spec_from_file_location('catalog_connection_checks',
        R / 'software/flag-1.1.0.dev1/gwflags/connection_spectra.py')
    engine = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(engine)
    factors_checked = computed = recomputed = toric_recomputed = 0
    for r in spectral:
        ident = r['id']
        if ident in flags:
            source = flags[ident]
            M = s.Matrix(source['matrix_symbolic'])
            G = s.Matrix(source['grading'])
            unit_index = source['basis_indices'].index(0)
            report = engine.connection_report(M, G, specialization={s.Symbol(k): s.Rational(v) for k, v in r['point'].items()})
            assert report['status'] == 'computed', ident
            expected = {}
            for f in report['sectors']:
                poly = positive(s.sympify(f['eigenvalue_factor_K']), t)
                expected[poly] = (f['multiplicity_per_root'], f['factor_degree'],
                                 expand_counts(f['representatives']), expand_counts(f['classes_mod_Z']))
            recomputed += 1
        else:
            source = toric[ident]
            M = s.zeros(len(source['basis']))
            for i, j, tex in source['matrix_sparse_latex']:
                M[i, j] = expression(tex)
            unit_index = source['basis'].index('1')
            expected = {}
            connection = old_connection[ident]
            assert {k: str(v) for k, v in connection['point'].items()} == r['point'], ident
            for f in connection['factors']:
                poly = positive(expression(f['polynomial_latex']), x)
                complete = f['status'] == 'complete'
                expected[poly] = (f['multiplicity'], f['distinct_eigenvalues'],
                                 f['powers'] if complete else None, f['classes'] if complete else None)
            # New post-analysis results are independently recomputed from M,G.
            additions = {s.sympify(f['polynomial_A'], locals={'z': z})
                         for f in r['factors'] if f['classes'] is not None
                         and expected[s.sympify(f['polynomial_A'], locals={'z': z})][3] is None}
            if additions:
                grade = source['grading_latex']
                grade = grade[grade.find('(') + 1:grade.rfind(')')]
                G = s.diag(*[expression(v.strip()) for v in grade.split(',')])
                report = engine.connection_report(M, G, specialization={s.Symbol(k): s.Rational(v) for k, v in r['point'].items()})
                toric_recomputed += 1
                for f in report['sectors']:
                    factor = s.sympify(f['eigenvalue_factor_K'])
                    poly = positive(factor, t)
                    if poly not in additions:
                        continue
                    if f['status'] != 'computed':
                        f.update(algebraic_scalar_sector(engine, M, G, r['point'], factor, f['multiplicity_per_root']))
                    expected[poly] = (f['multiplicity_per_root'], f['factor_degree'],
                                      expand_counts(f['representatives']), expand_counts(f['classes_mod_Z']))
        A = M.subs({s.Symbol(k): s.Rational(v) for k, v in r['point'].items()})
        assert not A.free_symbols, (ident, 'unspecialized parameters')
        assert A.rows == A.cols == r['rank'], ident
        actual = {}
        for f in r['factors']:
            poly = s.sympify(f['polynomial_A'], locals={'z': z})
            p = s.Poly(poly, z)
            assert p.LC() == 1 and s.gcd(p, p.diff()).degree() == 0, ident
            assert p.degree() == f['conjugate_eigenvalues'], ident
            assert isinstance(f['multiplicity_per_root'], int) and f['multiplicity_per_root'] > 0, ident
            powers, classes = f['powers'], f['classes']
            assert (powers is None) == (classes is None), ident
            if classes is not None:
                assert len(powers) == len(classes) == f['multiplicity_per_root'], ident
                assert all(0 <= Fraction(v) < 1 for v in classes), ident
                assert Counter(Fraction(v) % 1 for v in powers) == multiset(classes), ident
                computed += 1
            actual[poly] = (f['multiplicity_per_root'], f['conjugate_eigenvalues'], powers, classes)
            factors_checked += 1
        assert actual.keys() == expected.keys(), (ident, 'factor signs/coverage')
        for poly, (m, d, powers, classes) in actual.items():
            em, ed, epowers, eclasses = expected[poly]
            assert (m, d) == (em, ed), ident
            assert (powers is None) == (epowers is None), ident
            if powers is not None:
                assert multiset(powers) == multiset(epowers) and multiset(classes) == multiset(eclasses), ident
        product = s.prod(poly**v[0] for poly, v in actual.items())
        assert s.expand(A.charpoly(z).as_expr() - product) == 0, (ident, 'characteristic polynomial')
        unit = s.eye(A.rows)[:, unit_index]
        columns = [unit]
        for _ in range(1, A.rows):
            columns.append(A * columns[-1])
        assert s.Matrix.hstack(*columns).det() == s.Rational(r['unit_cyclic_determinant']), (ident, 'Delta_A')
        link = catalog[ident]['link']
        page = (R / 'docs/catalog' / link.split('#')[0]).read_text()
        rendered = section(ident, record_page=link.startswith('records/'))
        # Cards indent the same generated mathematical content.
        normalized = '\n'.join(line.lstrip() for line in page.splitlines())
        assert rendered.strip() in normalized, (ident, 'stale displayed spectral data')
    print(json.dumps(dict(records=len(spectral), factors=factors_checked,
                          computed_multisets=computed, recomputed_flag_connections=recomputed,
                          recomputed_toric_connections=toric_recomputed,
                          checks=['positive-A factors', 'exact characteristic polynomials',
                                  'unit Krylov determinants', 'multiset multiplicities',
                                  'classes modulo Z', 'source conventions', 'rendered data'])))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--shard', help='Validate a zero-based INDEX/COUNT partition of the complete dataset')
    validate(parser.parse_args().shard)
