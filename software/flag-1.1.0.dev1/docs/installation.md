---
description: Install individual flag or toric distributions or the combined application, using isolated environments and version-specific launch commands.
---

# How to install

Choose a distribution below. Each ZIP is an installable source bundle: extract it, open the folder containing `pyproject.toml`, and follow the same installation steps. Use a **separate virtual environment for each distribution**, since they share the Python import name `gwflags`.

## Installing this source bundle

You have already downloaded and extracted this runtime source bundle. Continue with the environment and installation steps below, starting at step 1. The versioned archive choices and their checksums are provided on the website; those ZIP files are not nested inside this ZIP. This handbook covers the complete software collection, so choose launch commands supported by the bundle you installed.

## 1. Create an environment

Install **Python 3.9 or newer** with `pip` and `venv` available. Python 3.12 or 3.13 is a practical starting point. On Windows, enable **Add Python to PATH** in the Python installer. Open a terminal in the extracted folder containing `pyproject.toml`.

=== "Windows PowerShell"

    ```powershell
    py -m venv .venv
    .\.venv\Scripts\python.exe -m pip install --upgrade pip
    .\.venv\Scripts\python.exe -m pip install .
    ```

    Activation is optional. Use `.\.venv\Scripts\python.exe` in place of `python` in the launch commands below. This also avoids PowerShell activation-policy errors.

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    .venv/bin/python -m pip install --upgrade pip
    .venv/bin/python -m pip install .
    source .venv/bin/activate
    ```

    If your Linux distribution provides `venv` or `pip` separately, install those Python components through its package manager before creating the environment.

The package installer resolves SymPy and mpmath automatically; do not install similarly named unrelated packages. Version 1.1.0.dev1 requires SymPy >=1.14, while flag 1.0.6.dev0 declares SymPy >=1.10. Both require mpmath >=1.2. For source development use `python -m pip install -e .` instead of `python -m pip install .`.

## 2. Launch the selected program

Run the command for the distribution you installed:

=== "Flag 1.0.6.dev0 / 1.1.0.dev1"

    ```bash
    python -m gwflags.gui --no-browser
    ```

    Open <http://127.0.0.1:8642>. Follow the [1.0.6.dev0 guide](software/flags-1.0.6.md) or [1.1.0.dev1 guide](software/flags-1.1.0.md). The standalone flag interface and the enhanced combined flag workspace have different controls.

=== "Toric 1.1.0.dev1"

    ```bash
    python -m gwtoric.gui --no-browser
    ```

    Open <http://127.0.0.1:8643>. Follow the [toric guide](software/toric-1.1.0.md).

=== "Combined 1.1.0.dev1"

    ```bash
    python -m gwapp --workspace ./gw-work --no-browser
    ```

    Open <http://127.0.0.1:8650>. Choose **Flag varieties** or **Toric varieties**. The writable workspace holds jobs and checkpoints. Follow the [combined guide](software/combined.md).

Use `--port` to choose a free port. Keep the terminal open while computing; stop the server with Ctrl-C. On Windows, use the full environment Python path from step 1. The local interfaces do not require a web-hosting service.

## 3. Check the installation

From outside the extracted source directory, run the relevant command with the environment Python:

```bash
python -c "from gwflags import FlagVariety; assert FlagVariety('A3',[1]).gw([], beta=(1,), K=[[3]]) == 27; print('Flag check passed')"
```

For toric or combined 1.1.0.dev1:

```bash
python -c "from gwtoric import projective_space; assert projective_space(3).gw([], beta=(1,1,1,1), K=[[3]]) == 27; print('Toric check passed')"
```

These are unmarked cubic-surface counts: the insertion list is empty. They also check that the installed imports work. Command-line users can run `python -m gwflags.cli --help`, or `python -m gwtoric.cli --help` for the toric distribution.

## SageMath and archived calculations

The flag backend can use SageMath where available; plain Python is the baseline for these instructions. Toric and combined analysis modules directly use SymPy. No separate SageMath installation is needed for the plain Python route.

Preserved v1.0.5 uses the original input conventions and retains its historical empty-CLI behavior. Use the [archived guide](software/flags-legacy.md) for that version; use current versions for the CLI correction. Existing saved flag catalogue matrices keep ambient-node Novikov labels: select `novikov_convention='ambient'` for comparisons.
