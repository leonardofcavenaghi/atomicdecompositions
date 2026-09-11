# Installation Instructions

The `gwflags` software evaluates Gromov-Witten invariants for flag varieties and complete intersections natively using the geometry of flag varieties. It can run on **plain Python** or from within **SageMath**.

---

## 1. Prerequisites

Before installing the software, you must ensure the underlying tools are available on your system.

### Option A: Plain Python (Recommended for most users)

You need Python 3.9 or newer.

=== "Windows"

    **Step 1: Install Python**
    1. Download the Python installer from the official [Python website](https://www.python.org/downloads/windows/).
    2. Run the installer. Before clicking "Install Now", you **must** check the box labeled **"Add Python to PATH"**.
    3. Open the Command Prompt (`cmd`) and verify the installation by typing:
       ```cmd
       python --version
       ```

    **Step 2: Install Git**
    1. Download the Git for Windows installer from the official git-scm website ([https://gitforwindows.org/](https://gitforwindows.org/)).
    2. Run the installer and proceed with the default options.
    3. Restart your Command Prompt to ensure the system recognizes the new path variables, then verify by typing:
       ```cmd
       git --version
       ```
    *(Note: If you wish to avoid installing Git, you must manually download the repository as a ZIP file from GitHub, extract it, and use the Command Prompt to navigate into the extracted directory.)*

=== "macOS"

    1. macOS comes with a version of Python, but it is recommended to use [Homebrew](https://brew.sh/).
    2. Open your Terminal and install Homebrew if you haven't already:
       ```bash
       /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
       ```
    3. Install Python and Git:
       ```bash
       brew install python git
       ```
    4. Verify:
       ```bash
       python --version
       git --version
       ```

=== "Linux (Ubuntu/Debian)"

    1. Open your terminal.
    2. Update your package list and install Python 3, Git, and `venv`:
       ```bash
       sudo apt update
       sudo apt install git python python3-pip python3-venv
       ```
    3. Verify:
       ```bash
       python --version
       git --version
       ```

### Option B: SageMath (Recommended for algebraic/symbolic speed)

If you have SageMath installed, the package auto-detects it and uses its symbolic ring for faster final matrix assembly. 

**Important Note for Windows Users:** Running SageMath on Windows natively is historically problematic. It currently requires the Windows Subsystem for Linux (WSL). A standard Windows user cannot simply download an executable and expect it to interface seamlessly with a Windows-based command prompt virtual environment. If you are on Windows, we strongly recommend Option A (Plain Python).

---

## 2. Installing the Software

We will use a **virtual environment** (`venv`) to isolate the project dependencies.

=== "Windows"

    **Step 3: Clone the Repository**
    In the Command Prompt, navigate to the directory where you want to store the software, then execute:
    ```cmd
    git clone https://github.com/leonardofcavenaghi/atomicdecompositions.git
    cd atomicdecompositions
    ```

    **Step 4: Create and Activate the Virtual Environment**
    Execute the following commands:
    ```cmd
    python -m venv venv
    venv\Scripts\activate
    ```
    You will know this step is successful when `(venv)` appears at the beginning of your command prompt line.

    **Step 5: Install Dependencies**
    With the virtual environment active, install the required packages using `pip`:
    ```cmd
    pip install sympy mpmath
    ```

=== "macOS and Linux"

    **Step 3: Clone the Repository**
    ```bash
    git clone https://github.com/leonardofcavenaghi/atomicdecompositions.git
    cd atomicdecompositions
    ```

    **Step 4: Create and Activate the Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

    **Step 5: Install Dependencies**
    ```bash
    pip install sympy mpmath
    ```

---

## 3. Quick Start & Verification

To verify that the installation is successful and that independently known values from Schubert calculus match exactly, you must run the test suite. 

**Note on Python commands:** Note: Since you are operating inside an activated virtual environment, the `python` command is standard across all operating systems.

=== "Windows"
    Run the test suite:
    ```cmd
    python tests/test_gwflags.py
    ```

    To use the Command Line Interface (CLI):
    ```cmd
    python -m gwflags.cli A2 --keep 1 sqm
    ```

    To start the Graphical User Interface (GUI):
    ```cmd
    python -m gwflags.gui
    ```

=== "macOS and Linux"
    Run the test suite:
    ```bash
    python tests/test_gwflags.py
    ```

    To use the Command Line Interface (CLI):
    ```bash
    python -m gwflags.cli A2 --keep 1 sqm
    ```

    To start the Graphical User Interface (GUI):
    ```bash
    python -m gwflags.gui
    ```
