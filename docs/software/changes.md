---
description: Behavior changes in the versioned standalone and combined development distributions.
---

# Version differences

Flag 1.0.6.dev0 and flag, toric and combined 1.1.0.dev1 are development versions. Stable flag v1.0.5 retains its original input conventions.

## Flag versions 1.0.6.dev0 and 1.1.0.dev1

- Default parameter names retain ambient nodes in type A and use consecutive kept-root labels for other families. C3/keep 3, G2/keep 2 and D5/keep 4 therefore use `y1`.
- Python, CLI and interface offer the `paper`, `ambient` and `compact` conventions. Results record the selected node-to-parameter map. Relabeling preserves coefficients, curve coordinates, ordered bases and grading.
- Empty CLI insertion text means zero insertions. The cubic-surface line count is 27 with an empty insertion list.
- The standalone interface displays bundle rank and explains serial workers and quotient-bundle validation.
- Unmarked trees use rooted-shape generation and AHU canonicalization. Independent comparisons preserve the previous representatives and ordering through six edges.

## Flag version 1.1.0.dev1 and the combined application

Version 1.1.0.dev1 adds checkpointed flag execution and supported Hodge, cyclicity and exponent analysis. The combined flag workspace exposes saved progress, cancellation and analysis controls. Completed-matrix caches include the naming convention and map.

Large intermediate fractions are stored with exact tagged hexadecimal integers, avoiding decimal-conversion limits. Old decimal checkpoints remain readable. Checkpoints containing tagged values require the updated reader.

## Toric version 1.1.0.dev1

The toric engine uses explicit fans or supported constructors, divisor-polynomial classes and integral ray relations. Its divisor and Novikov bases are reported separately when they differ. Automatic curve searches retain their completeness assumptions and cutoffs.

The combined application provides separate flag and toric workspaces with the same geometric input models as the individual engines. See [Version comparison](launch-2026-11.md) for capabilities, [Input/output conventions](input-output.md) for exact formats and [Validation and reproducibility](launch-plan.md) for the checks.
