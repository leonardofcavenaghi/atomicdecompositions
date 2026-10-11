---
description: Stable gwflags downloads and software release notes.
---

# Releases

[Download stable v1.0.5](https://github.com/leonardofcavenaghi/atomicdecompositions/archive/refs/tags/v1.0.5.zip){ .md-button .md-button--primary }
[Installation](installation.md){ .md-button }

The stable ZIP matches version `1.0.5`. The
[current main source](https://github.com/leonardofcavenaghi/atomicdecompositions/archive/refs/heads/main.zip)
also includes subsequent documentation improvements; record its commit when
using it for reproducible work.

## Website updates after v1.0.5

The documentation now groups catalog, software and mathematical material into
separate sections, with a single release history and a concise matrix-download
guide. Catalog metadata uses the label Ambient Index, and incomplete reference
entries link to Fanography instead of showing empty descriptions. These documentation changes are on main; the stable software remains
the v1.0.5 snapshot.

## v1.0.5 — 2026-10-12

- Automatic quantum-matrix enumeration requires positive Chern pairings on
  the supported curve generators. Mixed zero/positive ambient pairings now
  require an explicit curve list instead of an unjustified finite cap.
- Clarified the quantum-product pairing, bundle quotients, degree-zero API
  behavior, orthogonal line-bundle degrees and ambient index conventions.
- Added validation of displayed spectra and projective Hodge diamonds, and
  checks that stable download links match the package version.

## v1.0.4 — 2026-10-11

- Added 15 completed flag-variety and section examples, including the full
  GM-20 matrix.
- Published symbolic matrices, bases, gradings and curve lists for 131
  completed computations.
- Synchronized the master catalog with the displayed entries and added exact
  data-to-catalog validation.

## v1.0.3 — 2026-10-02

- Fixed formula rendering and example links during page navigation.
- Corrected the description of the smooth `(1,1,1,1)` hypersurface in `(P¹)⁴`.

## v1.0.2 — 2026-10-01

- Corrected and independently recomputed the Fanography 4-1 matrix.
- Improved matrix-specialization documentation and search metadata.

## v1.0.1 — 2026-09-17

- Added the MIT license, package metadata and reproducible test/documentation
  dependencies.
- Added validation across Python 3.9–3.13 and checks before website deployment.

## v1.0.0 — 2026-09-16

- Established the Python, CLI and browser interfaces, including quotient
  bundles and reproducible input/output handling.
- Added catalog, LaTeX and browser validation.
