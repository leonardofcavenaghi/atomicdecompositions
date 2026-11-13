---
description: Publication versions, validation scope and reproducibility checks for the 2026-11-13 flag and toric website launch.
---

# Publication and validation

The 2026-11-13 launch organizes the universal catalogue by dimension with separate flag and toric methods and publishes versioned source distributions. Flag 1.0.6.dev0 and flag/toric/combined 1.1.0.dev1 remain development builds. Stable v1.0.5 is preserved with its original behavior.

## Distributed sources

Each ZIP contains package metadata, shared runtime dependencies, a launch handbook and a SHA-256 file manifest. The website [download manifest](../downloads/manifest.json) identifies the ZIP bytes. Runtime bundles omit private research notes and local verification dependency copies. The two 1.1.0.dev1 individual bundles include shared flag/toric execution infrastructure and omit `gwapp`; the combined bundle includes all three packages and its JavaScript assets.

## Verification scope

The mathematical regression review passed both standalone flag suites (74 tests each, one socket-dependent HTTP test excluded locally), 133 toric regressions, 19 toric Hodge/spectrum tests, 27 independent tree/checkpoint checks and 19 merged-worker/routing checks. Guide examples were executed against their corresponding sources. In particular, the cubic-surface count is 27 with no insertions in Python, CLI and the interface request path.

The source review adopts upstream execution commit `7f167e17a35069ac1ff1cefecce2ac8a0be8231c`, plus the documented notation and empty-CLI corrections. The new tree generator preserves the old unmarked representatives and ordering in the independently checked range. Tagged exact checkpoint fractions handle large numerators and denominators; ordinary decimal checkpoints remain readable.

GitHub Actions gates website deployment on the package, catalogue, strict documentation and browser checks. Distribution checks install the exact extracted archives in isolated environments and exercise their launchers. The published archives passed isolated Linux and Windows installation and launcher checks. Browser checks cover the website, mathematical rendering, catalogue search and interface copy/download controls. SageMath is outside this automated platform coverage.

## Catalogue publication

The toric data are imported from completed saved records, with source hashes. The import checks dimensions, full divisor-row lengths, zero-based cone indices, matrix indices and duplicate entries. Further exact checks validate symbolic expressions and grading. These checks do not rerun every localization sum or independently certify every geometry and Hodge calculation.

96 fourfold and 72 fivefold matrices are included. Records with unfinished matrix computations are excluded; completed matrices with unresolved connection factors retain their notes. Fivefold records do not receive rationality verdicts. Their one-evaluation or cached two-evaluation provenance is stated on the collection page.

[Main changes](launch-2026-11.md) · [Input/output conventions](input-output.md) · [Installation](../installation.md)
