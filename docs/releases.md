# Release notes

## v1.0.0 — 2026-09-16

- Stabilized the Python, CLI, and browser interfaces, including quotient
  bundles and reproducible input/output handling.
- Added continuous validation for the software suite, catalog source, catalog
  LaTeX, strict site builds, and browser navigation/GUI controls.
- Kept release metadata and local working documents separate from the public
  computational documentation.

## 2026-09-16 — Quotients and catalog navigation

- Added same-variety quotient bundles through `quot(E,F)` / `Quot(E,F)` with
  multiplicity-aware fiber-weight validation.
- Published copyable quotient examples and synchronized Python, CLI, GUI, and
  API documentation.
- Catalog example links now open the selected card and re-typeset its formulas
  after instant navigation.

## 2026-09-16 — Interface alignment

- Published kept-root beta input with canonical ambient output and
  explicit validation of removed roots.
- Added compact bundle aliases and strict reduced/minimal Schubert-word checks
  to both browser and CLI interfaces.
- Synchronized the API, methodology, and website audit documentation.

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
