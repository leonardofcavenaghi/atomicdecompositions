# Combined flag and toric GW software

Start with [Launch documentation](LAUNCH.md) for the complete change overview, software choices, input/output conventions and publication and validation.

Version **1.1.0.dev1** combines the flag and toric computation engines in one
local application, with separate workspaces. This is a development snapshot.
The current combined software is on the default `main` branch of
[GiovaneGalindo/Torics](https://github.com/GiovaneGalindo/Torics).

## Install and run

Requires Python 3.9 or later. From this folder, install the package and its
SymPy and mpmath dependencies:

```sh
python -m pip install .
python -m gwapp
```

On Windows, you can also double-click **Start GW Software.cmd** after installation.
Open http://127.0.0.1:8650/ and choose **Flag varieties** or **Toric varieties**.
The installed `gw-combined` command starts the same application.

To download the current source without Git, use
[Download ZIP](https://github.com/GiovaneGalindo/Torics/archive/refs/heads/main.zip)
and extract it before installing. This branch snapshot is not a tagged stable release.

```sh
python -m gwapp --port 8651 --workspace ./workspace --no-browser
```

Omit `--no-browser` to open the browser automatically. Keep checkpoint files
together and use a separate workspace for each running application server.
The default workspace is alongside the source package; use `--workspace` to
choose a writable location, particularly with a system-wide installation.

## Development updates

Flag tree shapes now use rooted level sequences and AHU deduplication, followed
by lexicographic relabeling that preserves existing flag representatives and
checkpoint numbering. Six-edge generation considers 48 rooted candidates for
11 distinct shapes. Compatibility was checked through six edges.

Large intermediate checkpoint fractions use tagged hexadecimal numerator and
denominator strings, avoiding Python's decimal integer conversion limit while
preserving exact arithmetic. Existing decimal checkpoints remain readable.
Resume newly written checkpoints with this updated development build; older
builds cannot read the tagged values. These changes are available from `main`
and its Download ZIP link above, within the unreleased 1.1.0.dev1 snapshot.

## Features and scope

Both engines compute exact genus-zero Gromov-Witten invariants and small
quantum multiplication, including supported complete intersections.
Flag mode adds staged checkpoints, Hodge diamonds for supported ample
line-bundle complete intersections, spectrum analysis, regularized exponent
multisets, and cancellation. It supports one or two exact evaluations per
curve class and up to 12 workers. Toric mode retains its fan, product,
projective-bundle, blow-up, Hodge, quantum, and connection tools.

Flag spectrum analysis computes the unit cyclic determinant only after exact
substitution of the selected Novikov values, avoiding a potentially expensive
generic symbolic determinant. The quantum matrix remains symbolic. Eigenvalues,
cyclicity, and regularized exponents use the same selected values; omitted
variables default to one. The Python analysis API defaults to this behavior;
`symbolic_cyclicity=True` explicitly requests a generic determinant.

Hodge calculations assume a smooth regular section and enforce their
supported positivity hypotheses. Quantum calculations retain their returned
basis and grading. Unsupported connection factors remain unresolved;
the application does not infer a rationality verdict.

The Python APIs remain available through `gwflags` and `gwtoric`; the
standalone interfaces start with `python -m gwflags.gui` and
`python -m gwtoric.gui`. Use `python -m gwflags.cli --help` and
`python -m gwtoric.cli --help` for command-line options.

This repository snapshot contains runtime source, installation metadata,
the Windows launcher, and license. Computation data and checkpoints are
created locally when the application runs.

The flag engine is derived from
[GWFlags](https://github.com/leonardofcavenaghi/atomicdecompositions).
See [LICENSE](LICENSE) for the retained MIT license and attribution.


## Flag notation compatibility

Flag mode defaults to paper notation: ambient-node names in type A and consecutive kept-root names otherwise. Select Legacy ambient-node labels in the interface, use `--novikov-convention ambient` in the flag CLI, or construct `FlagVariety(..., novikov_convention="ambient")` in Python to reproduce previous names. Read `X.novikov_metadata` for the map. Toric coordinates and names are unchanged.

An empty flag CLI `--classes ""` now means zero insertions. The cubic-surface line count uses no insertions and returns 27. See [CHANGELOG.md](CHANGELOG.md).

## Website launch — 2026-11-12

The [website](https://leonardofcavenaghi.github.io/atomicdecompositions/) organizes a universal catalogue by dimension and construction, with distinct flag and toric mathematical conventions and usage guides. The [installation page](https://leonardofcavenaghi.github.io/atomicdecompositions/installation/) provides individual flag/toric and combined versioned downloads. Published toric records preserve exact inputs, symbolic matrices and unresolved connection-factor notes. Stable v1.0.5 remains preserved.
