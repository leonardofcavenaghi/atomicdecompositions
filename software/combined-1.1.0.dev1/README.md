# Combined flag and toric GW software (`1.1.0.dev1`)

Start with [LAUNCH.md](LAUNCH.md) for the software overview, input/output conventions, and validation scope.

Version **1.1.0.dev1** combines the flag (`gwflags`) and toric (`gwtoric`) computation engines in one local browser application (`gwapp`) with separate workspaces. This is a development source distribution published through [GEOATOMS](https://leonardofcavenaghi.github.io/atomicdecompositions/) and [leonardofcavenaghi/atomicdecompositions](https://github.com/leonardofcavenaghi/atomicdecompositions).

## Install and run

Requires Python 3.9 or later. From this folder, install the package and its SymPy and mpmath dependencies:

```sh
python -m pip install .
python -m gwapp
```

On Windows, you can also double-click **Start GW Software.cmd** after installation. Open `http://127.0.0.1:8650/` and choose **Flag varieties** or **Toric varieties**. The installed `gw-combined` command starts the same application.

```sh
python -m gwapp --port 8651 --workspace ./workspace --no-browser
```

Omit `--no-browser` to open the browser automatically. Keep checkpoint files together and use a separate workspace for each running application server. Use `--workspace` to choose a writable location, particularly with a system-wide installation.

## Development highlights

Flag tree shapes use rooted level sequences and AHU deduplication, followed by lexicographic relabeling that preserves existing flag representatives and checkpoint numbering. Large intermediate checkpoint fractions use tagged hexadecimal numerator and denominator strings, avoiding Python's decimal integer conversion limit while preserving exact arithmetic; existing decimal checkpoints remain readable.

## Features and scope

Both engines compute exact genus-zero Gromov-Witten invariants and small quantum multiplication, including supported complete intersections. Flag mode adds staged checkpoints, Hodge diamonds for supported ample line-bundle complete intersections, spectrum analysis, regularized exponent multisets, and cancellation. It supports one or two exact evaluations per curve class and up to 12 workers. Toric mode provides fan, product, projective-bundle, blow-up, Hodge, quantum, and connection tools.

Flag spectrum analysis computes the unit cyclic determinant only after exact substitution of the selected Novikov values, avoiding an expensive generic symbolic determinant. The quantum matrix remains symbolic. Eigenvalues, cyclicity, and regularized exponents use the same selected values; omitted variables default to one. The Python analysis API defaults to this behavior; `symbolic_cyclicity=True` explicitly requests a generic determinant.

Hodge calculations assume a smooth regular section and enforce their supported positivity hypotheses. Quantum calculations retain their returned basis and grading. Unsupported connection factors remain unresolved; the application does not infer a rationality verdict.

The Python APIs remain available through `gwflags` and `gwtoric`; the standalone interfaces start with `python -m gwflags.gui` and `python -m gwtoric.gui`. Use `python -m gwflags.cli --help` and `python -m gwtoric.cli --help` for command-line options.

See [LICENSE](LICENSE) for the MIT license and attribution.

## Flag notation compatibility

Flag mode defaults to paper notation: ambient-node names in type A and consecutive kept-root names otherwise. Select legacy ambient-node labels in the interface, use `--novikov-convention ambient` in the flag CLI, or construct `FlagVariety(..., novikov_convention="ambient")` in Python to reproduce previous names. Read `X.novikov_metadata` for the map. Toric coordinates and names are unchanged.

An empty flag CLI `--classes ""` means zero insertions. The unmarked cubic-surface line count is 27. See [CHANGELOG.md](CHANGELOG.md).

## Website and downloads

The [GEOATOMS website](https://leonardofcavenaghi.github.io/atomicdecompositions/) provides a universal catalogue organized by dimension and construction, flag and toric localization guides, and versioned individual and combined downloads. Stable release v1.0.5 remains preserved.
