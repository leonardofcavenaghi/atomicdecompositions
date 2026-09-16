# Catalog review — 15 September 2026

This review covers the maintained catalog pages and the Fanography reference page.

## Confirmed corrections

- Removed the duplicate `P2 Fano index 3` card and duplicate summary row.
- Reconciled every displayed **Basis Rank** in the Projective and Grassmannian pages with the dimension of its square quantum matrix (46 and 28 card-level corrections respectively), and synchronized the category tables and master index.
- Relabelled Fanography 2-32 as a symbolic matrix because it contains `y1` and `y2` variables.
- Added explicit realization metadata to Fanography cards and kept unsupported weighted, double-cover, and blow-up examples catalog-only.
- Replaced the old `docs/catalog.md` page with a historical pointer, pointing readers to the maintained split catalog.
- Corrected Fanography 1-5 through 1-9 input metadata, corrected 4-1 row 2 column 9,
  and published the independently recomputed 1-10 homogeneous-bundle matrix.

## Organization contract

The public catalog is organized as:

1. Projective Spaces
2. Grassmannians
3. Flag Varieties
4. Fanography references

The master index links the canonical pages. Category pages group entries by dimension and include deterministic summary tables. Fanography has sequential identifiers and distinguishes runnable realizations from catalog-only references.

## Regeneration warning

`restructure_catalog.py` and `generate_datatable.py` are data-generation utilities, not part of the documentation build. They must not be run over the reviewed pages without preserving realization labels, catalog-only status, corrected matrices, and duplicate filtering. Future catalog generation should use a checked-in source dataset and a duplicate-ID validation step.

## Verification

- No duplicate `p2fanoindex3` anchor remains.
- All Projective and Grassmannian cards containing matrices have matching Basis Rank values.
- The checked-in catalog validator covers corrected Fanography inputs and audited matrix cells.
- MkDocs strict build passes.
