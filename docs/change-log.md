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
