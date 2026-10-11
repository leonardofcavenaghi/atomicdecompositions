# Release notes

## v1.0.5 — 2026-10-12

- Made the new catalog and its 131 exact results visible on the homepage, and synchronized every stable download link.
- Corrected the quantum-product formula, tautological bundle example, degree-zero API convention, orthogonal line-bundle convention, and ambient index/basis explanations.
- Automatic quantum-matrix enumeration now rejects mixed zero/positive Chern directions: the dimension axiom gives no finite bound there. Explicit, geometrically justified or deliberately truncated curve lists remain supported. All 131 published examples retain their full automatic lists.
- Fixed the installation code fence and a copied Grassmannian benchmark; strengthened release validation to check homepage and installation links.
- Added CI checks for all 106 displayed eigenvalue lists and all 47 projective Hodge diamonds, using characteristic-polynomial residuals and exact Riemann–Roch respectively.

## v1.0.4 — 2026-10-11

- Added 15 completed flag-variety and section entries, including the full GM-20 matrix.
- Published exact symbolic matrices, ordered bases, gradings and supported curve lists for 131 completed localization computations.
- Rebuilt the master catalog table from canonical entries, correcting stale Fano indices and adding the new examples.
- Added exact data-to-catalog validation and browser coverage for the new entries.

## v1.0.3 — 2026-10-02

- Formulas render after page navigation without requiring a refresh, including rapid page changes.
- Catalog links open the selected example while preserving formula rendering.
- Corrected the description of the smooth `(1,1,1,1)` hypersurface in `(P¹)⁴`.

## v1.0.2 — 2026-10-01

- Corrected the Fanography 4-1 matrix and verified it by exact localization.
- Clarified matrix specialization and validation documentation.
- Added canonical page URLs, descriptive search metadata, and sitemap validation.
- Prevented superseded CI runs from overwriting current website documentation.

## Downloads

- [Stable source ZIP: v1.0.5](https://github.com/leonardofcavenaghi/atomicdecompositions/archive/refs/tags/v1.0.5.zip)
- [Current main source ZIP](https://github.com/leonardofcavenaghi/atomicdecompositions/archive/refs/heads/main.zip)

The stable ZIP matches version `1.0.5`. Record the commit when using main.

## v1.0.1 — 2026-09-17

- Removed local virtual environments, browser dependencies, and generated site output from the source tree; these remain reproducible through CI.
- Pinned the documentation toolchain and added explicit test/documentation installation paths.
- Expanded CI across Python 3.9–3.13 and made GitHub Pages deployment wait for the complete validation workflow.
- Added package metadata, repository URLs, and the MIT license.

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

Every release must pass the Python test suite, catalog and exact-data validators,
strict MkDocs build, release-link checks, and representative GUI/API smoke
tests. Incomplete computations remain outside the published catalog and GUI presets.
