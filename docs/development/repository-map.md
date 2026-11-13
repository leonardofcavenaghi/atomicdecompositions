---
description: Organization of maintained software, versioned distributions, exact datasets, catalogue pages and development tools.
---

# Repository map

## Software and distribution sources

| Location | Purpose |
|---|---|
| [`gwflags/`](https://github.com/leonardofcavenaghi/atomicdecompositions/tree/main/gwflags) | Repository-root flag package; its version and dependencies are declared in `pyproject.toml` |
| [`software/flag-1.1.0.dev1/`](https://github.com/leonardofcavenaghi/atomicdecompositions/tree/main/software/flag-1.1.0.dev1) | Individual flag distribution, including its required shared execution modules |
| [`software/toric-1.1.0.dev1/`](https://github.com/leonardofcavenaghi/atomicdecompositions/tree/main/software/toric-1.1.0.dev1) | Individual toric distribution, including its required shared execution modules |
| [`software/combined-1.1.0.dev1/`](https://github.com/leonardofcavenaghi/atomicdecompositions/tree/main/software/combined-1.1.0.dev1) | Combined application, both engines and separate interface workspaces |
| [`software/flag-1.0.5/`](https://github.com/leonardofcavenaghi/atomicdecompositions/tree/main/software/flag-1.0.5) | Preserved stable flag source |
| [Download manifest](../downloads/manifest.json) | Archive filenames, versions and SHA-256 checksums |

Installing the repository root installs its flag package. It does not select a versioned distribution automatically. Versioned directories are complete distribution sources; their shared modules are intentionally included so each distribution can be installed independently. The [software comparison](../software/launch-2026-11.md) explains their capabilities.

The root flag package separates root systems and Weyl groups (`rootsystem.py`, `weyl.py`), Billey restrictions and decorated-tree localization (`localization.py`), independent GKM localization (`gkm.py`), bundle operations (`bundles.py`, `cintersection.py`), decorated trees (`trees.py`), exact and symbolic evaluation backends (`symbolic.py`), quantum multiplication (`quantum.py`), parameter naming (`novikov.py`) and user interfaces (`cli.py`, `gui.py`).

## Mathematical data

The [dataset guide](../catalog/datasets.md) describes the public schemas and conventions. The [repository catalogue](../data/repository-catalog.json) classifies tracked files, distributions and datasets. Each computation retains its exact inputs, ordered basis, grading, curve coordinates and specialization.

| Files in `docs/data/` | Role |
|---|---|
| `localization-results.json` | Exact flag localization inputs and results |
| `toric-fourfolds.json`, `toric-fivefolds.json` | Exact toric fan, divisor and matrix inputs and results |
| `flag-fourfolds.json` | Additional homogeneous fourfold computations and their analysis |
| `connection-exponents.json` | Regularized exponent multisets at the stated analysis points |
| `atomic-invariants.json` | Hodge data, cyclicity tests and atomic invariants with their hypotheses |
| `geometric-presentations.json` | Identification of geometric constructions from fan and divisor data |
| `catalog-records.json` | Normalized names, dimensions, links and scientific keywords used by the catalogue |

The result collections supply mathematical data. The analysis collections record further calculations and their scope. The normalized catalogue index controls presentation and cross-references; changing a display name does not change the underlying matrix or basis.

[`catalog_inputs.py`](https://github.com/leonardofcavenaghi/atomicdecompositions/blob/main/catalog_inputs.py) and [`catalog_inputs.json`](https://github.com/leonardofcavenaghi/atomicdecompositions/blob/main/catalog_inputs.json) define Fanography flag inputs used by maintained validators and regression tests.

## Documentation and catalogue

| Location | Contents |
|---|---|
| `docs/software/`, `docs/installation.md`, `cli.md` | Version-specific installation, Python, terminal and interface guides |
| `docs/methodology.md`, `docs/toric/mathematics.md` | Mathematical conventions and localization formulas |
| `docs/catalog/index.md` and dimension pages | Universal catalogue, organized by geometry |
| `docs/catalog/records/` | Individual examples with exact inputs and results |
| `docs/catalog/atomic-invariants.md` and `invariants-*.md` | Cyclicity, cohomological scope and atomic Hodge invariants |
| `docs/catalog/additional.md`, `docs/catalog/computed.md` | Pages generated from the original exact matrix collection |
| `docs/downloads/` | Versioned source archives and mathematical computation notes |
| `docs/javascripts/`, `docs/stylesheets/`, `docs/assets/` | Website behavior, layout and images |
| `docs/development/` | Repository organization and maintenance procedures |

Compatibility pages under `docs/archive/`, `docs/audits/` and the legacy software guides retain earlier documentation addresses. Individual records are reached through the catalogue and search; they do not each require a separate navigation entry.

## Maintained tools and tests

[`scripts/`](https://github.com/leonardofcavenaghi/atomicdecompositions/tree/main/scripts) contains the supported catalogue generators, data and documentation validators, equation renderer and browser regressions. The [maintenance guide](maintenance.md) lists their purposes and execution order. [`tests/`](https://github.com/leonardofcavenaghi/atomicdecompositions/tree/main/tests) contains the Python regression suite and its reference data.

[`mkdocs.yml`](https://github.com/leonardofcavenaghi/atomicdecompositions/blob/main/mkdocs.yml) registers website navigation and Markdown extensions. The workflows in [`.github/workflows/`](https://github.com/leonardofcavenaghi/atomicdecompositions/tree/main/.github/workflows) select checks and deploy validated documentation.

Historical helpers are separated into `archive/legacy-tools/python/` and `archive/legacy-tools/browser/`. Earlier catalogue material is under `archive/catalogue/`. The [archive index](https://github.com/leonardofcavenaghi/atomicdecompositions/tree/main/archive) explains their original purpose and limitations. They are not the regeneration path for the current website. Local environments, logs, build output and exploratory screenshots are excluded from the tracked source.
