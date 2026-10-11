"""Build the master table from canonical cards instead of the legacy cache."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.catalog_results import load_results
from scripts.validate_catalog import cards, FIELD_RE, FIELD_TEXT_RE

HEADER = '| Geometry | Ambient Space | Dimension | Ambient Index | Basis Rank |'


def render_index():
    path = ROOT / 'docs/catalog/index.md'
    prefix = path.read_text(encoding='utf-8').split(HEADER)[0]
    rows = []
    for category in ['projective', 'grassmannians', 'flag_varieties', 'additional', 'fanography']:
        for card in cards(ROOT / 'docs/catalog' / (category + '.md')):
            ambient = FIELD_TEXT_RE['ambient'].search(card.text)
            fields = {name: regex.search(card.text) for name, regex in FIELD_RE.items()}
            if not ambient or not all(fields.values()):
                continue
            values = {name: int(match.group(1)) for name, match in fields.items()}
            title = 'Fanography ' + card.title if category == 'fanography' else card.title
            anchor = 'fano-variety-' + card.title if category == 'fanography' else card.anchor
            rows.append((title, category + '.md#' + anchor, ambient.group(1), values['dimension'], values['index'], values['rank']))
    # The legacy full-flag entry uses a heading rather than a collapsible card.
    for record in load_results():
        for alias in record['catalog_aliases']:
            if alias['page'] == 'flag_varieties.md':
                rows.append((alias['title'], alias['page'] + '#' + alias['anchor'], record['input']['algebra'], record['dimension'], record['fano_index'], len(record['basis_indices'])))
    rows.sort(key=lambda row: (-row[3], row[0]))
    body = '\n'.join(f'| [{title}]({link}) | {ambient} | {dim} | {index} | {rank} |' for title, link, ambient, dim, index, rank in rows)
    return prefix + HEADER + '\n|---|---|---|---|---|\n' + body + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    path = ROOT / 'docs/catalog/index.md'
    content = render_index()
    if args.check:
        if path.read_text(encoding='utf-8') != content:
            raise SystemExit('Master catalog table disagrees with canonical entries.')
    else:
        path.write_text(content, encoding='utf-8')
    print('Master catalog table is synchronized with canonical entries.')


if __name__ == '__main__':
    main()
