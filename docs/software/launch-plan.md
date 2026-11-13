---
description: Versioned source archives, installation checks, mathematical regression tests and catalogue verification scope.
---

# Validation and reproducibility

The distributed flag 1.0.6.dev0 and flag, toric and combined 1.1.0.dev1 packages are development versions. Stable v1.0.5 remains available with its original behavior.

## Source archives

Each archive contains package metadata, the required shared runtime modules, installation instructions and a SHA-256 file manifest. The [download manifest](../downloads/manifest.json) identifies the archive bytes. Individual 1.1.0.dev1 distributions include the shared flag/toric execution infrastructure; the combined distribution also provides `gwapp` and its interface assets.

Record the distribution version and archive checksum with a calculation. For a source checkout, record its commit. Install each distribution in a separate environment following [Installation](../installation.md).

## Software checks

Regression tests cover flag and toric localization, supported bundle operations, Hodge and spectrum calculations, unmarked tree generation, exact checkpoint fractions and combined-worker routing. The documented examples are checked against their corresponding versions, including the cubic-surface invariant 27 with an empty insertion list in Python, CLI and interface requests.

The downloadable archives are installed and their launchers exercised in isolated Linux and Windows environments. Website checks cover catalogue consistency, documentation builds, search, mathematical display and interface copy/download controls. SageMath is outside this automated platform coverage.

The updated tree generator preserves the previous representatives, vertex labels and ordering through six edges in independent comparisons. Large checkpoint fractions retain exact signs, numerators and denominators; old decimal checkpoints remain readable, while tagged large-fraction values require the updated reader.

## Mathematical data

Catalogue validation checks fan and divisor dimensions, cone indices, exact matrix expressions, basis ordering, grading and characteristic polynomials. These consistency checks complement the stated localization provenance; they do not independently rerun every localization sum.

Each result retains its curve-list assumptions and exact analysis point. A complete quantum matrix can have unresolved connection factors. Full atomic decompositions require the cyclicity and cohomological hypotheses described in [Atomic invariants](../catalog/atomic-invariants.md); a matrix and its exponents alone do not imply a rationality conclusion.

[Version comparison](launch-2026-11.md) · [Input/output conventions](input-output.md) · [Installation](../installation.md)
