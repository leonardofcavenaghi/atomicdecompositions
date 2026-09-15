# Change log and review record

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
