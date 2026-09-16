#!/usr/bin/env python3
"""Validate generated catalog pages for structural and numerical consistency.

The checker is intentionally text based: catalog pages are Markdown artifacts and
this catches accidental edits before a documentation build or deployment.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs" / "catalog"
sys.path.insert(0, str(ROOT))
from catalog_inputs import compact_bundle, fanography_specs
CARD_RE = re.compile(r'^\?\?\? example "([^"]+)"', re.MULTILINE)
ANCHOR_RE = re.compile(r'<span\s+id="([^"]+)"\s*>', re.IGNORECASE)
FIELD_RE = {
    "dimension": re.compile(r'^\s*- \*\*Dimension:\*\*\s*[\$`]?(-?\d+)[\$`]?\s*$', re.MULTILINE),
    "index": re.compile(r'^\s*- \*\*Fano Index:\*\*\s*[\$`]?(-?\d+)[\$`]?\s*$', re.MULTILINE),
    "rank": re.compile(r'^\s*- \*\*Basis Rank:\*\*\s*[\$`]?(\d+)[\$`]?\s*$', re.MULTILINE),
}
MATRIX_RE = re.compile(r"\\begin\{bmatrix\}(.*?)\\end\{bmatrix\}", re.DOTALL)
LINK_RE = re.compile(r'\]\(([^)#]+)?#([^ )]+)\)')
FANOGRAPHY_INPUTS = {
    identifier: (
        str(spec["algebra"]),
        ",".join(str(node) for node in spec["keep"]),
        compact_bundle(spec),
    )
    for identifier, spec in fanography_specs().items()
}

FIELD_TEXT_RE = {
    'ambient': re.compile(r'^\s*- \*\*Ambient Space:\*\*\s*`\$?([^`$\n]+)\$?`', re.MULTILINE),
    'keep': re.compile(r'^\s*- \*\*Keep Nodes:\*\*\s*`([^`]*)`', re.MULTILINE),
    'bundle': re.compile(r'^\s*- \*\*Bundle K:\*\*\s*`([^`]*)`', re.MULTILINE),
}

@dataclass
class Card:
    path: Path
    title: str
    text: str
    anchor: str | None


def cards(path: Path) -> list[Card]:
    text = path.read_text(encoding="utf-8")
    starts = list(CARD_RE.finditer(text))
    result = []
    for i, match in enumerate(starts):
        start = match.start()
        end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
        before = text[max(0, start - 300):start]
        anchor_match = list(ANCHOR_RE.finditer(before))
        result.append(Card(path, match.group(1), text[start:end], anchor_match[-1].group(1) if anchor_match else None))
    return result


def matrix_shape(card: Card) -> tuple[int, int] | None:
    match = MATRIX_RE.search(card.text)
    if not match:
        return None
    rows = [r.strip() for r in re.split(r'\\\\', match.group(1)) if r.strip()]
    counts = [len([c for c in row.split('&') if c.strip()]) for row in rows]
    if not counts:
        return (0, 0)
    if len(set(counts)) != 1:
        return (len(rows), -1)
    return (len(rows), counts[0])


def normalize_anchor(title: str) -> str:
    return re.sub(r'[^a-z0-9]+', '', title.lower())


def validate() -> list[str]:
    errors: list[str] = []
    files = sorted(CATALOG.glob('*.md'))
    all_cards: list[Card] = []
    anchors: dict[str, list[str]] = {}
    for path in files:
        text = path.read_text(encoding='utf-8')
        for match in ANCHOR_RE.finditer(text):
            anchors.setdefault(match.group(1), []).append(str(path.relative_to(ROOT)))
        all_cards.extend(cards(path))
    for anchor, locations in sorted(anchors.items()):
        if len(locations) > 1:
            errors.append(f'duplicate anchor "{anchor}" in {", ".join(locations)}')

    seen_titles: dict[tuple[str, str], int] = {}
    for card in all_cards:
        prefix = f'{card.path.relative_to(ROOT)}: {card.title}'
        key = (card.path.name, card.title)
        seen_titles[key] = seen_titles.get(key, 0) + 1
        if seen_titles[key] > 1:
            errors.append(f'{prefix}: duplicate card title')
        values = {}
        for key, pattern in FIELD_RE.items():
            found = pattern.search(card.text)
            if found:
                values[key] = int(found.group(1))
        if card.path.name == 'fanography.md':
            # Existing Fanography records may predate realization labels; when a
            # label is present, ensure it contains an actual classification.
            type_match = re.search(r'Realization type:\*?\s*([^\n]+)', card.text)
            if type_match and not type_match.group(1).strip(' `*_:.'):
                errors.append(f'{prefix}: empty realization type')
            if 'Catalog only' in card.text and 'Ambient Space:' in card.text:
                errors.append(f'{prefix}: catalog-only entry must not advertise an ambient space')
            if card.title in FANOGRAPHY_INPUTS:
                expected = FANOGRAPHY_INPUTS[card.title]
                actual = []
                for field in ('ambient', 'keep', 'bundle'):
                    match = FIELD_TEXT_RE[field].search(card.text)
                    actual.append(match.group(1).strip() if match else None)
                # Direct flags may omit Bundle K or spell it as a parenthetical
                # “none” note. Every nonempty bundle spelling must match the
                # central source exactly.
                bundle_ok = (
                    actual[2] == expected[2]
                    if expected[2]
                    else actual[2] is None or "none" in actual[2].lower()
                )
                if actual[0] != expected[0] or actual[1] != expected[1] or not bundle_ok:
                    errors.append(f'{prefix}: executable input {tuple(actual)!r} disagrees with expected {expected!r}')
            if card.title == '2-32' and ('y1' in card.text or 'y2' in card.text):
                if 'Quantum Matrix (symbolic' not in card.text:
                    errors.append(f'{prefix}: matrix containing y1/y2 must be labelled symbolic')
            if card.title == '4-1':
                matrix = MATRIX_RE.search(card.text)
                if matrix:
                    rows = [r.strip() for r in re.split(r'\\\\', matrix.group(1)) if r.strip()]
                    if len(rows) > 1:
                        entries = [c.strip() for c in rows[1].split('&')]
                        if len(entries) > 8 and entries[8] != '2':
                            errors.append(f'{prefix}: audited row 2, column 9 must equal 2')
            if card.title == '1-10':
                matrix = MATRIX_RE.search(card.text)
                expected_rows = fanography_specs()['1-10'].get('matrix_at_one')
                if matrix is None:
                    errors.append(f'{prefix}: validated homogeneous-bundle matrix is missing')
                else:
                    rows = [[c.strip() for c in row.strip().split('&')] for row in re.split(r'\\\\', matrix.group(1)) if row.strip()]
                    if rows != expected_rows:
                        errors.append(f'{prefix}: published matrix disagrees with the independently recomputed 1-10 matrix')
        # Category pages use explicit anchors; Fanography uses stable variety
        # headings without anchors and is checked separately by its source links.
        if card.path.name != 'fanography.md':
            if card.anchor is None:
                errors.append(f'{prefix}: missing anchor')
            elif card.anchor != normalize_anchor(card.title):
                errors.append(f'{prefix}: anchor \"{card.anchor}\" does not match normalized title \"{normalize_anchor(card.title)}\"')
        # Only populated catalog cards need all numerical metadata. Catalog-only
        # Fanography records deliberately have no geometry fields.
        if 'Ambient Space:' in card.text:
            for key in ('dimension', 'index', 'rank'):
                if key not in values:
                    errors.append(f'{prefix}: missing {key} metadata')
            if values.get('dimension', 0) < 0:
                errors.append(f'{prefix}: dimension must be nonnegative')
            if values.get('index', 0) <= 0:
                errors.append(f'{prefix}: Fano Index must be positive')
            if values.get('rank', 0) <= 0:
                errors.append(f'{prefix}: Basis Rank must be positive')
        shape = matrix_shape(card)
        if shape is not None:
            rows, cols = shape
            if rows != cols:
                errors.append(f'{prefix}: quantum matrix is not square ({rows}x{cols})')
            if 'rank' in values and rows != values['rank']:
                errors.append(f'{prefix}: Basis Rank {values["rank"]} disagrees with matrix size {rows}')

    # Validate every intra-catalog anchor link points to an existing anchor.
    for path in files:
        for match in LINK_RE.finditer(path.read_text(encoding='utf-8')):
            target_file, anchor = match.group(1), match.group(2)
            if target_file and not target_file.endswith('.md'):
                continue
            if anchor not in anchors:
                errors.append(f'{path.relative_to(ROOT)}: link target #{anchor} has no matching anchor')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--quiet', action='store_true', help='print only failures')
    args = parser.parse_args()
    errors = validate()
    if errors:
        print(f'Catalog validation failed: {len(errors)} issue(s)', file=sys.stderr)
        for error in errors:
            print(f'  - {error}', file=sys.stderr)
        return 1
    if not args.quiet:
        print(f'Catalog validation passed: {len(list(CATALOG.glob("*.md")))} pages checked')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
