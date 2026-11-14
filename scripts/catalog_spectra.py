"""Render spectra and computed exponent multisets in the catalogue convention.

The exact source matrices and frozen software exports retain their original
schemas. This presentation layer uses A, the first-Chern operator, throughout.
"""
from __future__ import annotations

import json
import argparse
import re
from functools import lru_cache
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


@lru_cache(maxsize=1)
def records():
    return {r['id']: r for r in json.loads(
        (ROOT / 'docs/data/spectral-data.json').read_text())['records']}


def polynomial_tex(formula, variable='z'):
    z = sp.Symbol('z')
    return sp.latex(sp.sympify(formula, locals={'z': z}).subs(z, sp.Symbol(variable)))


def multiset_tex(values):
    return r'\{\!\{' + ','.join(sp.latex(sp.Rational(v)) for v in values) + r'\}\!\}'


def section(ident, *, record_page=False):
    """One common field order, independent of the source software version."""
    r = records()[ident]
    notation = '../notation.md' if record_page else 'notation.md'
    atomic = json.loads((ROOT / 'docs/data/catalog-records.json').read_text())['records']
    link = next(c['atomic_invariants_link'] for c in atomic if c['id'] == ident)
    if record_page:
        link = '../' + link
    point = ', '.join(k + '=' + str(v) for k, v in sorted(r['point'].items()))
    determinant = sp.latex(sp.Rational(r['unit_cyclic_determinant']))
    lines = [
        '**Parameter point:** `' + point + '`.', '',
        r'Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned '
        r'ambient space, and \(G\) is its centered codimension grading. '
        'Columns are images of the ordered basis. '
        '[Notation and scope](' + notation + ').', '',
        r'\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. '
        r'Each multiplicity and exponent multiset applies separately at every root '
        r'\(\lambda\) of the indicated factor.', '',
        r'| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |',
        '|---|---:|---:|',
    ]
    for f in r['factors']:
        lines.append('| \\(' + polynomial_tex(f['polynomial_A']) + r'\) | '
                     + str(f['conjugate_eigenvalues']) + ' | '
                     + str(f['multiplicity_per_root']) + ' |')
    lines += ['', r'**Unit cyclic determinant:** \(\Delta_A(\mathbf a)='
              + determinant + r'\), in this basis.', '']
    available = [f for f in r['factors'] if f['classes'] is not None]
    if available:
        lines += [r'**Regularized exponent multisets** '
                  r'\(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):', '',
                  r'| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |',
                  '|---|---|']
        for f in available:
            lines.append('| \\(' + polynomial_tex(f['polynomial_A'], 'lambda')
                         + r'=0\) | \('
                         + multiset_tex(f['classes']) + r'\) |')
        lines += ['', 'Repeated entries retain their multiplicity.']
    data_link = ('../../data/' if record_page else '../data/') + r['source']
    lines += ['', '[Exact matrix, ordered basis and grading](' + data_link + ') · '
              '[Hodge data and atomic invariants](' + link + '). '
              'The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.']
    return '\n'.join(lines) + '\n'


def card_section(ident):
    return ('    ??? note "Spectrum and connection exponents"\n\n'
            + '\n'.join('        ' + line if line else ''
                        for line in section(ident).splitlines()) + '\n\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    source = json.loads((ROOT / 'docs/data/localization-results.json').read_text())['examples']
    catalog = json.loads((ROOT / 'docs/data/catalog-records.json').read_text())['records']
    targets = {}
    for r in source:
        for a in r['catalog_aliases'] or [{'page': r['catalog_page'], 'title': r['title']}]:
            targets.setdefault(a['page'], {})[a['title'].removesuffix(' (GM-20)')] = r['id']
    for r in catalog:
        if r['link'].startswith('records/'):
            targets[r['link']] = r['id']
    for name, value in targets.items():
        path = ROOT / 'docs/catalog' / name
        original = text = path.read_text()
        tail = 'The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.'
        if isinstance(value, str):
            pattern = r'(## Spectrum and connection exponents\n\n).*?' + re.escape(tail) + r'\n'
            text, count = re.subn(pattern, lambda m: m[1] + section(value, record_page=True), text, flags=re.S)
            assert count == 1, (name, 'missing spectral section')
        else:
            starts = list(re.finditer(r'^\?\?\? example "([^"]+)"', text, re.M))
            if name == 'flag_varieties.md':
                ident = next(iter(value.values()))
                pattern = r'\?\?\? note "Spectrum and connection exponents"\n\n.*?' + re.escape(tail) + r'\n'
                content = '??? note "Spectrum and connection exponents"\n\n' + '\n'.join(
                    '    ' + line if line else '' for line in section(ident).splitlines()) + '\n'
                text, count = re.subn(pattern, lambda _: content, text, flags=re.S)
                assert count == 1, name
            else:
                for i, m in reversed(list(enumerate(starts))):
                    title = ('Fanography ' if name == 'fanography.md' else '') + m[1]
                    if title not in value:
                        continue
                    end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
                    card = text[m.start():end]
                    pattern = r'    \?\?\? note "Spectrum and connection exponents"\n\n.*?' + re.escape(tail) + r'\n\n'
                    card, count = re.subn(pattern, lambda _: card_section(value[title]), card, flags=re.S)
                    assert count == 1, (name, title)
                    text = text[:m.start()] + card + text[end:]
        if args.check:
            assert original == text, ('Stale spectral presentation', name)
        else:
            path.write_text(text)
    print('Catalogue spectral sections synchronized:', len(records()), 'examples')


if __name__ == '__main__':
    main()
