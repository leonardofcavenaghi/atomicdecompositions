# Change log and review record

## 2026-09-16 — Quotient bundles and catalog rendering

- Added `quot(E, F)` and `Quot(E, F)` to the Python, CLI, and browser bundle
  interfaces. The operation requires `F` to be a same-variety subbundle of `E`;
  fiber-weight containment is checked with multiplicity at every fixed point,
  including equivalent type-A characters modulo the trace direction.
- Added quotient examples and validation failures to the How-to-Use guide, API
  reference, GUI help, and regression tests.
- Fixed catalog hash navigation and MathJax rendering after instant page loads:
  selecting an individual example now opens its card and renders its matrices
  without a manual refresh or duplicate formula containers.

## 2026-09-16 — Input alignment

- Documented `beta` input in kept-root order: zero-padded ambient vectors remain
  valid, removed-root entries
  are rejected, and results report canonical ambient coordinates.
- Added restricted bundle aliases `O(...)`, `S(node)`, and `Q(node)` to
  the browser and CLI, while retaining explicit Python constructors.
- Made browser/CLI Schubert insertion parsing require reduced minimal words and
  added canonical Novikov labels `y<ambient node>`.
- Guarded automatic small-quantum degree enumeration against negative kept
  Chern pairings; formal non-nef calculations now require explicit beta lists.

## 2026-09-15 — interface, catalog, and documentation review

- Added guided preset metadata: recommended action, cleared dependent inputs, and expected output.
- Clarified every GUI field with labels, examples, validation feedback, responsive layout, and accessibility status updates.
- Added a compact input-format panel and basis-word **Add** controls to reduce manual Weyl-word entry.
- Added exact input summaries to results and corrected the GUI language for matrix, space-info, and invariant actions.
- Audited Fanography mappings against rank lists; marked weighted/double-cover and blow-up entries as catalog-only when unsupported by the current input model.
- Added explicit realization types (direct flag variety, line-bundle complete intersection, homogeneous-bundle zero locus, or catalog-only).
- Rewrote the How-to-Use guide with beginner and experienced installation paths, copyable examples, parser boundaries, troubleshooting, and the correct CLI option order.

## Validation required for each release

1. Run the full Python test suite.
2. Build the MkDocs site with `--strict`.
3. Smoke-test `/api/presets`, Space Info, quantum matrix, GW invariant, compact bundles, and quotient bundles.
4. Review this file and the catalog for unresolved “pending” matrices or catalog-only entries.

## 2026-09-15 — catalog audit

- Audited all canonical catalog pages and corrected duplicate projective entries, 74 matrix-rank metadata mismatches, and a symbolic Fanography matrix label.
- Added a catalog organization review and marked the legacy aggregate page as historical.

- Recomputed supported pending Fanography matrices for 1-5, 1-14, 2-24, 2-34, and 4-1; updated the corrected 4-1 basis rank.
- Replaced legacy duplicate catalog pages with pointers to the validated canonical catalog.

## 2026-09-16 — Fanography 1-10 matrix

- Published the Fanography 1-10 (`V(3,22)`) quantum multiplication matrix for the
  three-copy homogeneous bundle on `Gr(3,7)`.
- Verified the matrix with an exact `gwflags` run and by matching all 21
  regularized quantum-period coefficients in the smooth-Fano reference data.

## 2026-09-16 — catalog source and regression hardening

- Centralized executable Fanography inputs in `catalog_inputs.json`; the
  injector, verifier, matrix helper, and catalog validator now consume the same
  records.
- Added a fast regression fixture for Fanography 1-10 that checks its symbolic
  matrix, rendered catalog card, and all 21 independent period coefficients.
- Corrected the 1-15 card to the runnable `A4`, keep `2`, `K=1;1;1`
  realization described by its Grassmannian linear section.

## 2026-09-15 — independent mathematics and software audit

- Corrected Fanography 1-5 through 1-9 so each displayed ambient space, kept
  node, and Bundle K matches its stated geometry; recorded the supported
  homogeneous-bundle input for 1-10 and marked its matrix pending independent
  recomputation.
- Corrected Fanography 4-1 row 2, column 9 and labelled the variable-dependent
  2-32 matrix symbolic.
- Added catalog input validation, parser and bundle-constructor regression tests,
  and the independent [mathematics and software audit](audits/math-software-review.md).
- Final audit run: catalog validation passed, strict MkDocs build passed, and
  57 Python tests passed.
