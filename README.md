# GEOATOMS — quantum cohomology computations

GEOATOMS provides exact genus-zero Gromov–Witten computations for flag varieties, toric varieties and supported complete intersections. The website combines mathematical methods, software guides and a catalogue organized by geometric dimension and construction.

[Website and catalogue](https://leonardofcavenaghi.github.io/atomicdecompositions/) · [Installation](https://leonardofcavenaghi.github.io/atomicdecompositions/installation/) · [Version comparison](docs/software/launch-2026-11.md) · [Release notes](docs/releases.md)

## Software distributions

| Distribution | Scope | Source | Guide |
|---|---|---|---|
| Flag `1.0.6.dev0` | Flag varieties and homogeneous complete intersections | Repository root | [Flag guide](docs/software/flags-1.0.6.md) |
| Flag `1.1.0.dev1` | Flag computations, checkpointed execution and supported Hodge and connection analysis | [Flag source](software/flag-1.1.0.dev1/) | [Flag guide](docs/software/flags-1.1.0.md) |
| Toric `1.1.0.dev1` | Toric varieties and complete intersections, with supported Hodge and connection analysis | [Toric source](software/toric-1.1.0.dev1/) | [Toric guide](docs/software/toric-1.1.0.md) |
| Combined `1.1.0.dev1` | Both engines, with separate flag and toric interface workspaces | [Combined source](software/combined-1.1.0.dev1/) | [Combined guide](docs/software/combined.md) |

These are development versions. The stable flag release remains [v1.0.5](https://github.com/leonardofcavenaghi/atomicdecompositions/archive/refs/tags/v1.0.5.zip); its [preserved source](software/flag-1.0.5/) and [guide](docs/software/flags-legacy.md) retain that version’s conventions.

Installing the repository root installs **flag `1.0.6.dev0`**. Choose a versioned source directory or [source archive](docs/installation.md) to install a different distribution. Use a separate virtual environment for each distribution.

## Install from a checkout

Use Python 3.9 or later. From the repository directory, create an environment:

```bash
python -m venv .venv
```

Activate it with `source .venv/bin/activate` on Linux/macOS, `.venv\Scripts\activate.bat` in Windows Command Prompt, or `.venv\Scripts\Activate.ps1` in PowerShell. Package installation resolves SymPy and mpmath.

Choose **one** installation command:

| Distribution | Installation command |
|---|---|
| Flag `1.0.6.dev0` | `python -m pip install .` |
| Flag `1.1.0.dev1` | `python -m pip install ./software/flag-1.1.0.dev1` |
| Toric `1.1.0.dev1` | `python -m pip install ./software/toric-1.1.0.dev1` |
| Combined `1.1.0.dev1` | `python -m pip install ./software/combined-1.1.0.dev1` |

The [installation guide](docs/installation.md) also covers standalone ZIP downloads and platform-specific commands.

## Launch the interface

Run the command matching the installed distribution:

```bash
# Either individual flag version:
python -m gwflags.gui --no-browser --port 8642

# Individual toric version:
python -m gwtoric.gui --no-browser --port 8643

# Combined version:
python -m gwapp --no-browser --port 8650 --workspace ./geoatoms-workspace
```

Open `http://127.0.0.1:8642`, `http://127.0.0.1:8643`, or `http://127.0.0.1:8650`, respectively. The combined interface has separate **Flag varieties** and **Toric varieties** workspaces. The version-specific guides provide complete interface, Python and terminal examples.

## Python examples

For either flag distribution, or the combined distribution:

```python
from gwflags import FlagVariety

P3 = FlagVariety("A3", [1])
assert P3.gw([], beta=(1,), K=[[3]]) == 27
```

For the toric distribution, or the combined distribution:

```python
from gwtoric import projective_space

P3 = projective_space(3)
assert P3.gw([], beta=(1, 1, 1, 1), K=[[3]]) == 27
```

Both examples count the 27 lines on a smooth cubic surface, with **zero insertions**. The curve coordinates differ: kept-root coordinates for the flag input and full ray coordinates for the toric input. Bundle rows and Novikov names follow the [input/output conventions](docs/software/input-output.md).

## Mathematics and catalogue

- [Localization on flag varieties](docs/methodology.md): root systems, Schubert classes, curve coordinates and twisted localization.
- [Localization on toric varieties](docs/toric/mathematics.md): fans, divisor classes, invariant curves and twisted localization.
- [Geometric catalogue](docs/catalog/index.md): constructions, inputs, ordered bases, quantum multiplication and computed exponent multisets.
- [Atomic invariants](docs/catalog/atomic-invariants.md): cyclic determinants, full Hodge data and atomic Hodge polynomials where the required hypotheses hold.
- [Exact datasets](docs/catalog/datasets.md): downloadable inputs, matrices, bases, gradings and analysis points.

A returned ambient quantum operator need not describe full cohomology. The mathematical guides and individual examples state the hypotheses for interpreting it and for identifying full atomic decompositions.

## Repository organization

[Repository map](docs/development/repository-map.md) · [Contributing](CONTRIBUTING.md) · [Maintenance guide](docs/development/maintenance.md) · [File and collection catalogue](docs/data/repository-catalog.json)

Maintained software, exact results, analysis data and documentation have separate roles. Historical helpers are indexed under [archive/](archive/README.md); they are separate from the supported generators and validators in `scripts/`.

## Development and validation

For the repository-root flag package:

```bash
python -m pip install -e ".[test]"
python -m pytest tests/ -q
```

Automated checks also install the downloadable distributions on Linux and Windows, validate catalogue mathematics and data, and exercise website navigation, search, equation rendering and interface controls. See [Validation and reproducibility](docs/software/launch-plan.md).
