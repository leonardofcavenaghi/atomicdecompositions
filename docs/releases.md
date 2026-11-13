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

## Current development version: 1.0.6.dev0

The development update changes default non-type-A flag Novikov labels to consecutive kept-root names while preserving type A labels. Python, CLI and interface choices retain legacy names when requested. Empty CLI insertion text now denotes an unmarked invariant. Exact coefficients, curve lists, bases and grading are preserved. This development build is distributed with the 2026-11-12 website launch; it is not a stable tag; v1.0.5 remains the preserved stable snapshot.

Existing catalog matrices retain their original ambient-node labels. Use the ambient compatibility convention to compare fresh calculations with those archives. No stored coefficients, bases or gradings were rewritten.

The development build also adopts the verified rooted-shape/AHU tree generator from upstream commit 7f167e1, preserving the previous representatives and ordering through the independently checked range.

## Website launch — 2026-11-12

- Universal catalogue organized by dimension and construction, with separate flag and toric mathematical descriptions.
- Individual flag 1.0.6.dev0, flag 1.1.0.dev1 and toric 1.1.0.dev1 downloads, plus combined 1.1.0.dev1 and preserved flag 1.0.5.
- Revised isolated-environment installation commands, version-specific launchers and unmarked cubic-surface installation checks.
- Published 96 completed fourfold and 72 completed fivefold toric matrix records, preserving unresolved connection-factor notes and excluding unfinished matrices.
- Added Milena Brockhof to the contributors.

The new software downloads keep development version labels. See [version differences](software/changes.md), [input/output formats](software/input-output.md) and [validation scope](software/launch-plan.md).

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


## Upcoming launch documentation

Read the [complete change overview](software/launch-2026-11.md), [input/output conventions](software/input-output.md), and [launch preparation](software/launch-plan.md) for the prepared software collection. The new documentation is ready for review; publication and the later visual redesign remain separate steps.
