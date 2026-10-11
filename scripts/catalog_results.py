#!/usr/bin/env python3
"""Render public catalog pages from exact localization results."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'docs/data/localization-results.json'


def load_results():
    return json.loads(DATA.read_text(encoding='utf-8'))['examples']


def bundle_input(record):
    bundle = record['input']['bundle']
    if isinstance(bundle, str):
        return bundle
    return ';'.join(','.join(map(str, row)) for row in bundle)


def matrix_tex(rows):
    return (r'\begin{bmatrix}' + r'\\'.join(
        ' & '.join(sympy.latex(sympy.sympify(x)) for x in row)
        for row in rows) + r'\end{bmatrix}')


def additional_page(records):
    selected = [r for r in records if r['catalog_page'] == 'additional.md']
    lines = [
        '---',
        'description: Exact quantum multiplication matrices and reproducible inputs for additional flag varieties and their complete intersections.',
        '---', '', '# Flag varieties and sections', '',
        'These entries include orthogonal, symplectic, exceptional and partial flag varieties, '
        'and complete intersections in them. Each displayed matrix comes from exact '
        '`gwflags` virtual localization using the full automatically supported curve list.', '',
        'For a worked full-flag example, see [Fl(1,2,3)](flag_varieties.md#afl123).', '',
        'Matrices represent multiplication by $c_1(TY)$ on the returned ambient sector, '
        'with every Novikov variable set to $1$. Columns are inputs and rows are outputs. '
        'The ordered basis below uses reduced Schubert words; `()` is the unit. '
        'Basis indices in the download are zero-based.', '',
        '[Download all symbolic matrices, bases, gradings and curve classes](../data/localization-results.json) '
        'or browse [Download matrices and inputs](computed.md). '
        'See [How to Use](../how-to-use.md) for input conventions.', '',
        '| Geometry | Dimension | Ambient index | Basis rank |',
        '|---|---|---|---|',
    ]
    for r in selected:
        lines.append(f"| [{r['title']}](#{r['catalog_anchor']}) | {r['dimension']} | {r['fano_index']} | {len(r['basis_indices'])} |")
    for r in selected:
        lines += ['', '---', '', f'<span id="{r["catalog_anchor"]}"></span>', '',
                  f'??? example "{r["title"]}"',
                  f'    - **Ambient Space:** `{r["input"]["algebra"]}`',
                  f'    - **Keep Nodes:** `{",".join(map(str, r["input"]["keep"]))}`',
                  f'    - **Bundle K:** `{bundle_input(r)}`' if bundle_input(r) else '    - **Bundle K:** empty (the flag variety itself)',
                  f'    - **Dimension:** ${r["dimension"]}$',
                  f'    - **Ambient Index:** ${r["fano_index"]}$',
                  f'    - **Basis Rank:** ${len(r["basis_indices"])}$',
                  f'    - **Exact data identifier:** `{r["id"]}`', '',
                  '    ??? note "Quantum Matrix ($y=1$)"', '        $$',
                  '        ' + matrix_tex(r['matrix_at_one']), '        $$', '',
                  '    ??? note "Ordered basis and degrees"', '',
                  '        | Position | Schubert word | Complex codimension |',
                  '        |---|---|---|']
        for i, (word, degree) in enumerate(zip(r['basis_words'], r['basis_degrees'])):
            word_text = '(' + ' '.join(map(str, word)) + ')'
            lines.append(f'        | {i + 1} | `{word_text}` | {degree} |')
        if r['id'] == 'e1322438fd01':
            lines += ['', '    The full matrix includes nonzero contributions from curve classes of anticanonical degree 5.']
    return '\n'.join(lines).rstrip() + '\n'


def computed_page(records):
    lines = [
        '---',
        'description: Download exact symbolic quantum multiplication matrices, ordered bases, gradings and supported curve classes for 131 completed localization computations.',
        '---', '', '# Download matrices and inputs', '',
        'This download lets you reuse the matrices displayed in the catalog in Python, '
        'SageMath or other software, or repeat the computations from their original inputs. '
        'It includes the basis order and grading needed to interpret each matrix.', '',
        'You can read the examples directly in the [catalog](index.md); the download is optional. '
        '**Exact** means that fractions and symbolic expressions are preserved instead of '
        'rounded decimal approximations.', '',
        'The `fano_index` field uses the software’s ambient Chern-lattice convention; '
        'it need not be the intrinsic Fano index of a low-dimensional section. '
        'For example, a conic is `P1` with geometric index 2 even when the ambient gcd is 1. '
        'See [catalog conventions](index.md).', '',
        f'This collection contains **{len(records)} completed exact localization computations**, '
        f'including **{sum(r["dimension"] == 3 for r in records)} threefold realizations**. '
        'Different realizations are listed separately even when the resulting varieties are isomorphic.', '',
        '[Download the complete JSON dataset](../data/localization-results.json)', '',
        'Each record contains the executable algebra/kept-root/bundle input, the full '
        'automatically supported curve list in ambient coordinates, the symbolic '
        '$c_1(TY)$ multiplication matrix, its specialization at all $y_i=1$, the '
        'ordered Schubert basis, and the grading. Rational numbers are stored as exact strings. '
        'The matrix acts on the returned ambient sector, with columns as inputs and rows as outputs.', '',
        'These are the same results displayed in the [catalog](index.md). '
        'See [Methods and conventions](../methodology.md) for their mathematical scope.', '',
        '## Use a saved result', '', '```python', 'import json',
        'from pathlib import Path', '',
        'data = json.loads(Path("localization-results.json").read_text())',
        'example = next(r for r in data["examples"] if r["id"] == "e1322438fd01")',
        'print(example["input"])', 'print(example["matrix_symbolic"])',
        'print(example["basis_words"])', '```', '',
        'To recompute a record, construct `FlagVariety` with its algebra and kept '
        'roots, parse its bundle using the documented input syntax, and call '
        '`small_quantum_multiplication(K)` without restricting the automatic curve list.', '',
    ]
    return '\n'.join(lines).rstrip() + '\n'


def generated_pages(records):
    return {
        ROOT / 'docs/catalog/additional.md': additional_page(records),
        ROOT / 'docs/catalog/computed.md': computed_page(records),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for path, content in generated_pages(load_results()).items():
        if args.check:
            if path.read_text(encoding='utf-8') != content:
                raise SystemExit(f'Stale generated catalog page: {path.relative_to(ROOT)}')
        else:
            path.write_text(content, encoding='utf-8')
    print('Exact computation pages are synchronized.')


if __name__ == '__main__':
    main()
