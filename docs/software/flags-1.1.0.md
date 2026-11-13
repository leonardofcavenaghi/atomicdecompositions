---
description: Use version 1.1.0.dev1 flag engine through Python, the command line, the standalone flag interface and the enhanced combined workspace.
---

# How to use version 1.1.0.dev1 flag software

This guide describes the prepared development version `1.1.0.dev1`. It is distributed as a development source bundle. The individual flag distribution contains the flag engine and its shared execution dependencies. Install that source bundle, or select the combined distribution for the enhanced `/flag/` workspace. Copying only `gwflags/` omits required shared modules.

## Launch the interface

After following [Installation](../installation.md), run:

```bash
python -m gwflags.gui --no-browser
```

Open <http://127.0.0.1:8642>. This standalone interface has **Describe this space**, **Compute quantum matrix** and **Compute one GW invariant**.

For the additional Hodge, saved-progress, cancellation and exponent controls, install the **combined 1.1.0.dev1** distribution first, then run:

```bash
python -m gwapp --workspace ./gw-work --no-browser
```

Open <http://127.0.0.1:8650/flag/>. The [combined guide](combined.md) describes the shared launcher.

## Fastest path: load an example

1. Choose the cubic-surface preset.
2. Confirm algebra `A3`, kept root `1`, bundle `3` and curve class `1`.
3. Leave **Insertions** empty: this is an unmarked calculation, with no point insertion.
4. Click **Compute one GW invariant**. The answer is 27.
5. Use **Copy input JSON** or **Download result JSON** in the flag workspace to retain the inputs and result.

## The core inputs

The flag fields use the same conventions as the [original flag guide](flags-1.0.6.md): algebra names such as `A4` or `A2xA2`; 1-based kept nodes; semicolon-separated bundle summands; and beta in kept-root order or zero-padded ambient-root coordinates.

Examples of **Bundle K** are `3`, `1,1;2,2`, `Q(2)`, `dual(S(2))` and `osum(Q(2),O(1))`. The node must be kept, and S/Q constructions require a supported type A factor. Python list notation such as `[[3]]` belongs to the Python API, not the form.

**Novikov notation** defaults to Paper notation. Type A retains ambient labels; the other families use consecutive kept-root labels. Thus C3/keep 3, G2/keep 2 and D5/keep 4 use `y1`. Describe the space to see the explicit map. The compatibility choice **Legacy ambient-node labels** restores the previous names without changing beta.

## Additional computations in the combined flag workspace

| Control | Concrete behavior |
|---|---|
| Exact evaluations per curve class | Two independent exact evaluations by default; one is available but omits the agreement check |
| Parallel workers | 1 is serial; 0 requests automatic allocation on this configured path, capped at 12 |
| Hodge diamond | Ambient flags or supported ample line-bundle intersections; assumes a smooth regular section |
| Compute quantum matrix | Saves exact progress and keeps the matrix symbolic |
| Update spectrum & exponents | Requires a completed matrix for the same inputs; reuses it at the selected Novikov point |
| Stop calculation | Terminates the running flag job; committed checkpoints remain available for a repeated request |

In the combined workspace, omitted Novikov values default to one for analysis. The symbolic matrix remains available. Exact flag exponent analysis requires rational specialized entries; unsupported sectors are reported as unresolved. Neither numerical eigenvalues nor computed exponent classes alone give a rationality verdict.

The standalone `gwflags.gui` has different specialization behavior: **Evaluate y** substitutes into the returned matrix and suppresses its separate numerical `y=1` display. Its worker value 0 is serial. Do not assume it has the combined workspace's extra buttons.

## Python and CLI

Unmarked cubic-surface lines:

```python
from gwflags import FlagVariety

X = FlagVariety("A3", [1])
assert X.gw([], beta=(1,), K=[[3]]) == 27
```

Checkpointed exact flag invariants use the execution wrapper:

```python
from gwflags.execution import configure, gw

X = configure(FlagVariety("A3", [1]),
              checkpoint_directory="flag-checkpoints", evaluations=2)
assert gw(X, [], beta=(1,), K=[[3]]) == 27
```

Calling `X.gw(...)` directly retains the original non-staged path. The wrapper above selects staging; configured quantum-matrix blocks also use staging.

A supported non-Fano Hodge example is the plane cubic:

```python
from gwflags.hodge import hodge_report

h = hodge_report("A2", [1], [[3]])
assert h["dimension"] == 1
assert h["hodge_matrix"][0][1] == 1
```

The returned quantum basis and grading must accompany any analysis:

```python
from gwflags.gui_analysis import matrix_analysis
from gwflags.connection_spectra import connection_report

P2 = FlagVariety("A2", [1])
M, grading, indices = P2.small_quantum_multiplication()
analysis = matrix_analysis(M, unit_index=indices.index(0))
connection = connection_report(M, grading)
assert analysis["cyclic_at_specialization"] is True
assert connection["rank"] == len(indices)
```

The standalone CLI shares the original flag commands. Put bundle and notation options before the subcommand:

```bash
python -m gwflags.cli A3 --keep 1 -K 3 gw --beta 1 --classes ""
python -m gwflags.cli C2 --keep 2 --novikov-convention ambient info
```

The standalone CLI does not expose the combined application's Hodge and saved-analysis buttons. Use the Python modules or the enhanced workspace for those operations.

## Reading results and mathematical scope

`small_quantum_multiplication` returns `(matrix, grading, basis_indices)`. The indices refer to the returned flag's Schubert ordering. For complete intersections this is an ambient sector; Hodge dimensions do not supply missing primitive quantum multiplication.

The original convexity and positive curve-bound conditions remain in force. Changing an input format or a Novikov name does not establish smoothness, an effective cone or ambient completeness.

## Troubleshooting

- Keep the workspace directory between runs if you want to resume calculations.
- Compute a quantum matrix before requesting cached spectrum/exponent analysis.
- Repeat the same geometry, bundle, evaluation count and naming convention when reusing a completed matrix.
- Read the reported Hodge support error rather than inferring that every accepted GW bundle supports Hodge reconstruction.
- Use a separate environment from the preserved original flag distribution: both install the package name `gwflags`.

See [Notation and compatibility](notation.md) and [Changes](changes.md).


## Checkpoint format compatibility

The prepared build includes the verified 7f167e1 update: faster unmarked shape generation preserves the tested legacy ordering, and large partial-sum fractions are saved as exact tagged hexadecimal integers. Once new tagged values have been written, resume with this updated build; older readers do not understand them.

For the common conventions and concrete result examples, see [Input/output](input-output.md). The [upcoming release overview](launch-2026-11.md) explains the differences between the offerings.
