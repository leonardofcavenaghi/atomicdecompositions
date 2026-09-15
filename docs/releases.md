# Release notes

## 2026-09-15 — Catalog and interface maintenance

- Added guided GUI presets, clearer input syntax, bundle-combination walkthroughs, and validation feedback.
- Corrected catalog duplicate entries and synchronized matrix-rank metadata.
- Classified Fanography records by realization type and marked unsupported constructions as catalog-only.
- Added catalog and website audit reports.
- Added deterministic, duplicate-safe catalog generation that preserves the reviewed Fanography page by default.
- Added automated validation and browser/API regression coverage.
- Recomputed and verified supported Fanography matrices for 1-5, 1-14, 2-24, 2-34, and 4-1.

## Validation policy

Every release must pass the Python test suite, catalog validator, strict MkDocs build, and representative GUI/API smoke tests. Pending catalog computations must be explicitly labelled rather than presented as verified matrices.
