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

## Development versions

Flag **1.0.6.dev0** and flag, toric and combined **1.1.0.dev1** are available as [versioned source downloads](installation.md). The stable release remains **v1.0.5**.

The flag updates introduce parameter-name choices, correct empty CLI insertions and improve unmarked tree generation. Version 1.1.0.dev1 adds checkpointed execution and supported Hodge and connection analysis. The combined application offers separate flag and toric workspaces. See [Version differences](software/changes.md) and the [capability comparison](software/launch-2026-11.md).

## Repository organization

Contributor and maintenance guides describe the source tree, distribution snapshots, mathematical collections, generators and validation procedures. A machine-readable repository catalogue checks that tracked files, software distributions and exact datasets are registered. Historical utilities are indexed separately from maintained tools.

## Catalogue notation and spectral data — 2026-11-14

- The spinor-tenfold section by five hyperplanes and a quadric includes a fresh exact matrix, connection exponents and very-general atomic Hodge invariants.
- Newly inserted equations use a locally hosted, pinned SVG renderer; the published equations remain pre-rendered.
- A self-contained notation key defines the first-Chern operator, grading, quantum parameters, cyclic determinant, exponent multisets and atomic Hodge invariants.
- All examples use the same first-Chern sign convention and state their spectral parameter point explicitly.
- The spectral dataset includes exact connection analysis of the original flag matrices and the toric factors. Exponent tables preserve repeated entries and give values separately at each eigenvalue.
- Catalogue summaries include the computed Hodge numbers and link directly to operators and Hodge data. Mathematical hypotheses accompany atomic interpretations.

## Website — 2026-11-13

- A geometric catalogue organized by dimension and construction, with exact downloadable matrices, bases and gradings.
- Separate flag and toric mathematical descriptions, installation choices, and Python, terminal and interface examples.
- Geometric example names with CKP/HLM references explained.
- Per-factor regularized-exponent multisets and exact analysis points.
- Full Hodge data and cyclicity tests, with atomic Hodge invariants where the required hypotheses are established.
- Homogeneous fourfold examples from LG(3,6) and the adjoint G₂ variety, including very-general irrationality criteria.
- Equations rendered as SVG with accessible MathML, independent of visitor JavaScript or a mathematical-font CDN.
- Alphabetical contributor credits, including Milena Brockhof.

[Input/output conventions](software/input-output.md) · [Validation and reproducibility](software/launch-plan.md)

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
  incidence fourfold matrix.
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
