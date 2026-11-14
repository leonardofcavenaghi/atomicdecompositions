---
description: Procedures for updating exact catalogue data, validating software distributions and publishing mathematical documentation.
---

# Maintenance guide

Use the [repository map](repository-map.md) to distinguish maintained sources, versioned distributions, mathematical datasets and historical helpers. Run the commands below from the repository root in the appropriate environment.

## Adding or correcting an example

1. Specify the geometry, software distribution and exact input conventions. For flags, retain the algebra, kept-root order and bundle input. For toric constructions, retain the ray order, zero-based maximal cones, full divisor rows and Novikov-divisor map.
2. Compute the operator with the existing localization routines and exact arithmetic. Retain its symbolic coefficients, returned basis order, grading, unit and supported curve list. An explicit curve list requires a justified completeness statement for the requested computation.
3. Add the result to its appropriate collection in `docs/data/` and document it in `docs/catalog/`. Follow that collection's schema; the flag and toric schemas use different coordinates and basis descriptions. Preserve the stated analysis point and the relation between the quantum operator and connection characteristic factors.
4. Update `catalog-records.json` with the geometric title, dimension, construction, links and scientific keywords. Keep stable machine keys out of displayed titles. Use the same keys to cross-reference analysis datasets, without treating them as mathematical nomenclature.
5. Update the universal index and affected dimension page. Register the example's Hodge data and cyclicity analysis; publish atomic invariants only when the full cohomological hypotheses are justified. Regularized exponents are multisets attached to an individual eigenvalue at a specified point; unresolved factors have no assigned multiset.
6. Run the relevant validators and review the rendered example. Extend reference checks for a new mathematical case using independent invariants or identities.

A complete ambient matrix can coexist with unresolved connection analysis or incomplete primitive-cohomology information. State these distinctions in mathematical terms. Keep unfinished computations and private research notes outside public pages and interface presets.

## Registering repository contents

The [repository catalogue](../data/repository-catalog.json) classifies tracked paths and records the software and dataset collections. After adding or moving files, stage only the intended paths with `git add`, then regenerate the catalogue:

```bash
python scripts/repository_catalog.py
python scripts/repository_catalog.py --check
```

The generator uses the Git-tracked inventory in a checkout and supports a filesystem inventory when Git metadata is unavailable. Review and stage the generated JSON with the change. Register a new distribution or mathematical collection in `scripts/repository_catalog.py` before regenerating its entry. Its classifications complement the geometric example index; they do not replace it.

## Data sources and generated pages

| Source | Maintained use |
|---|---|
| `docs/data/localization-results.json` | Exact flag results; source for `catalog/additional.md` and `catalog/computed.md` |
| `docs/data/toric-fourfolds.json`, `toric-fivefolds.json` | Exact toric results, interpreted by their example pages and validators |
| `docs/data/flag-fourfolds.json` | Additional homogeneous examples and their exact analysis |
| `docs/data/catalog-records.json` | Canonical catalogue titles, links, dimensions and scientific search terms |
| `docs/data/connection-exponents.json`, `atomic-invariants.json`, `geometric-presentations.json` | Connection, Hodge-theoretic and geometric analyses cross-referenced to their source results |
| `docs/data/spectral-data.json` | Unified first-Chern factors, exact points, unit determinants and exponent multisets used in all example displays |

The supported page generators are:

```bash
python scripts/catalog_results.py
python scripts/generate_catalog_index.py
python scripts/catalog_spectra.py
```

The first writes `docs/catalog/additional.md` and `docs/catalog/computed.md`. The second replaces the universal table in `docs/catalog/index.md` while preserving its introduction. The third updates the spectral sections in existing example pages and cards from `spectral-data.json`, preserving their geometric descriptions and inputs. Their `--check` options detect differences without writing files.

Dimension tables use the same column and ordering conventions as the universal table. The current `generate_catalog_index.py` command writes the universal index only; update the affected dimension table consistently and check it in the browser. The generators do not create new mathematical results. Supply and review the exact inputs, matrices, Hodge data and connection results before rendering them. In spectral data, factors are monic factors of the positive first-Chern operator \(A\); convert negative-operator exports by \((-1)^{\deg p}p(-z)\), and check the determinant in the returned basis. Match factors by their polynomial and parameter point, rather than by a factor number shared across files.

During a MkDocs build, `scripts/search_keywords.py` adds the scientific keywords from the normalized catalogue index to the search index. No visible keyword paragraph is required on an example page.

## Validation

The maintained Python checks have distinct scopes:

| Script in `scripts/` | Checks |
|---|---|
| `repository_catalog.py --check` | Tracked-file classifications and registered distributions and datasets |
| `validate_catalog.py` | Catalogue structure, mathematical input fields and links |
| `validate_localization_results.py` | Exact flag result contracts, matrices, supported curves, generated pages and universal index |
| `validate_toric_results.py` | Fan and divisor contracts, matrix expressions, grading and characteristic polynomials |
| `validate_flag_fourfolds.py` | Homogeneous fourfold results, connection analysis and Hodge identities |
| `validate_geometric_presentations.py` | Geometric identifications from fan combinatorics, lattice bases and divisor relations |
| `validate_exponent_multisets.py` | Exact first-Chern characteristic polynomials, unit Krylov determinants, per-factor multisets, displayed sections and repeated exact connection analysis, including algebraic conjugates for nonlinear sectors |
| `validate_atomic_invariants.py` | Exact cyclic determinants, factorization, Hodge data and certified atomic polynomial sums |
| `validate_catalog_tex.py` | Catalogue equations compiled with LaTeX |
| `validate_catalog_math.py` | Displayed spectra and Hodge diamonds |
| `validate_delivery.py` | Public links and terminology, dataset cross-references, archive checksums and source-mirror agreement |
| `validate_release_metadata.py` | Package versions, stable tags and release/download documentation |
| `validate_search_metadata.py` | Built canonical URLs, sitemap, search keywords and withdrawn-page exclusions |
| `validate_distributions.py` | Independent archive installation and actual interface launchers |

The connection validator can be partitioned with `--shard INDEX/COUNT` (zero-based indices). CI runs all three `0/3`, `1/3` and `2/3` partitions; their disjoint union covers every example. Nonlinear repeated factors are checked at both exact algebraic eigenvalues with two covector orders, using the versioned scalar-filtration functions. This post-analysis does not change the software’s high-level reporting capabilities.

Consistency checks of existing matrices complement fresh localization calculations; they do not repeat every localization sum. Changes to computation behavior also require the Python regression suite:

```bash
python -m pytest tests/ -q
```

The test requirements include the LaTeX parser used by mathematical checks. `validate_catalog_tex.py` additionally requires a TeX installation with `pdflatex` and the packages used by the catalogue.

## Documentation build and browser checks

The private `geoatoms-documentation-checks` package in `scripts/` declares the browser-test dependencies and commands; its lockfile pins their resolved versions. It is build tooling, separate from the Python software distributions.

Install the documented toolchain and browser-test dependencies:

```bash
python -m pip install -r requirements-docs.txt
npm ci --prefix scripts
```

Then build, validate and render the site:

```bash
mkdocs build --strict
python scripts/validate_search_metadata.py
python scripts/validate_release_metadata.py
node scripts/render_static_math.js
node scripts/test_catalog_navigation.js
node scripts/test_gui_controls.js
```

Equation rendering is a separate step after MkDocs. It produces standalone SVG and accessible MathML, rejects unwrapped or invalid mathematical source, and versions local styles and scripts by content. Rebuilding with MkDocs after this step would replace those rendered pages. The rendering build obtains the pinned MathJax runtime from a CDN; published equations do not require that browser download.

The browser tests exercise local HTTP servers. They check catalogue navigation, scientific search, inline mathematical baselines, mobile layout, first opening with JavaScript disabled or math CDNs blocked, and interface copy/download controls. Run them in an environment with a browser and local server access.

## Distribution maintenance

Choose the affected distribution before editing runtime code. Keep the preserved stable source unchanged. If a versioned source distribution changes, update its package metadata, applicable guides, source snapshot manifest, downloadable archive and archive checksum together. Keep each archive's mirrored source directory byte-for-byte consistent with its contents.

`validate_delivery.py` checks archive and source correspondence. `validate_distributions.py` installs each archive into an isolated environment and exercises its imports, command-line entry points and interface servers. CI runs the latter on Linux and Windows. A successful import from the repository checkout does not establish that a downloadable archive is complete.

Record version behavior in `CHANGELOG.md` and `docs/releases.md`, and update installation instructions when launchers, dependencies or input conventions change. The [version comparison](../software/launch-2026-11.md) and [input/output guide](../software/input-output.md) describe user-facing differences.

## Continuous integration and publication

`test.yml` validates catalogue mathematics and the website on every applicable run. `classify_ci_changes.py` compares changed paths with a successful ancestor: known documentation changes can use the documentation checks, while runtime, distribution, dependency and unclassified changes require the full software suite. Pull requests and an unavailable baseline also use the full suite. Software runs include Python-version regressions, separate exact algebra tests and independent source-distribution installation.

After successful validation of `main`, `deploy.yml` checks out that exact commit, builds the documentation, renders the equations and verifies that the source has not been superseded. It publishes the already-rendered `site/` tree to `gh-pages`. GitHub Pages then deploys that branch. Generated HTML belongs on the deployment branch, not among the source documentation.
