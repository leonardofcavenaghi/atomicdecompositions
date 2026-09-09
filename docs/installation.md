# Installation Instructions

The `gwflags` software is written to be flexible and fast. It evaluates Gromov-Witten invariants for flag varieties and complete intersections exactly, avoiding slow symbolic computer algebra system (CAS) loops. 

It can run on **plain Python** or from within **SageMath**.

---

## 1. Prerequisites

Before installing the software, you need either Python or SageMath on your computer.

### Option A: Plain Python (Recommended for most users)

You need Python 3.9 or newer.

=== "Windows"
    1. Download the official installer from [Python.org](https://www.python.org/downloads/windows/).
    2. **Crucial Step:** During installation, check the box that says **"Add Python to PATH"** before clicking "Install Now".
    3. Open Command Prompt (`cmd`) and verify the installation:
       ```cmd
       python --version
       ```

=== "macOS"
    1. macOS comes with a version of Python, but it is recommended to use [Homebrew](https://brew.sh/).
    2. Open your Terminal and install Homebrew if you haven't already:
       ```bash
       /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
       ```
    3. Install Python:
       ```bash
       brew install python
       ```
    4. Verify:
       ```bash
       python3 --version
       ```

=== "Linux (Ubuntu/Debian)"
    1. Open your terminal.
    2. Update your package list and install Python 3 and `pip`:
       ```bash
       sudo apt update
       sudo apt install python3 python3-pip python3-venv
       ```
    3. Verify:
       ```bash
       python3 --version
       ```

### Option B: SageMath (Recommended for algebraic/symbolic speed)

If you have SageMath installed, the package auto-detects it and uses its symbolic ring for faster final matrix assembly. You can download SageMath from [sagemath.org](https://www.sagemath.org/).

---

## 2. Installing the Software

Once your Python environment is ready, you can download the code and install its dependencies.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/plby/gromov_witten.git
   cd gromov_witten
   ```

2. **Install the single Python dependency (`sympy`):**
   ```bash
   pip install sympy
   ```
   *(If you are using SageMath, you do not need to install `sympy` as it is included).*

---

## 3. Quick Start & Verification

To verify that the installation is successful and independently known values from Schubert calculus match exactly, run the test suite:

```bash
python3 tests/test_gwflags.py
```

### Using the Command Line Interface (CLI)

The package provides a built-in CLI for rapid computations. For example, to check the quantum multiplication matrix for \( \mathbb{P}^2 \) (Type \(A_2\)):

```bash
python3 -m gwflags.cli A2 --keep 1 sqm
```

### Using the Graphical User Interface (GUI)

There is also a local web application built into the software:

```bash
python3 -m gwflags.gui
```
This will start a local server. Open your web browser to the provided `localhost` URL to access interactive presets for all benchmark and reference examples.
