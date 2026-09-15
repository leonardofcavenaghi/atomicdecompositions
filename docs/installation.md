# Installation

Choose the path that matches your background. You do not need SageMath to use the browser interface or the core Python API.

## New to Python (recommended path)

1. Install Python 3.9 or newer (Python 3.10+ is recommended) from [python.org](https://www.python.org/downloads/). On Windows, select **Add Python to PATH**.
2. Install Git from [git-scm.com](https://git-scm.com/downloads), or download the repository as a ZIP.
3. Open a terminal and obtain the source:

```bash
git clone https://github.com/leonardofcavenaghi/atomicdecompositions.git
cd atomicdecompositions
```

4. Create and activate an isolated environment:

=== "Windows"

    ```powershell
    py -m venv .venv
    .venv\Scripts\Activate.ps1
    ```

=== "macOS/Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

5. Install the project and its declared dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

6. Launch the local website:

```bash
python -m gwflags.gui --no-browser
```

Open <http://127.0.0.1:8642>. Stop the server with `Ctrl-C`.

## Comfortable with Python

From a checkout, activate your existing environment and run `python -m pip install -e .`. Then use the GUI, CLI, or import `FlagVariety` in a script. Run a quick smoke test:

```bash
python -c "from gwflags import FlagVariety; print(FlagVariety('A2',[1]).dimension)"
```

To run the tests, install the optional test dependency first:

```bash
python -m pip install pytest
```

Then run the full tests with:

```bash
python -m pytest tests/ -q
```

## SageMath users

SageMath is optional. If it is installed, `gwflags` can use it for symbolic work; the plain Python installation above remains the supported baseline. On Windows, use WSL for SageMath and follow the Linux commands there.

## Command-line and browser entry points

```bash
python -m gwflags.cli A2 --keep 1 sqm
python -m gwflags.gui --port 9000 --no-browser
```

For complete examples and input syntax, see [How to Use](how-to-use.md). In the GUI, compact bundles use `3` or `1,1;2,2`; Python code may use `K=[[3]]`.
