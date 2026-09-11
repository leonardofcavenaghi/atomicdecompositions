# How to Use `gwflags`

This guide bridges the theoretical framework of Quantum Cohomology with practical computation using the `gwflags` software. You can run these computations either via the **Graphical User Interface (GUI)** or directly via **Python Scripts**.

## Launching the Interface
To start the interface, open your terminal (inside the folder) and run:
```bash
python3 -m gwflags.gui
```
This will start a local server at `http://127.0.0.1:8000`. You can input parameters directly into the web interface.

---

## Example 1: Classic Enumerative Geometry
The `gwflags` library natively computes Gromov-Witten invariants for complete intersections using Atiyah-Bott localization. Let's compute two famous results in algebraic geometry: the 27 lines on a cubic surface, and the 2875 lines on a quintic threefold.

### The 27 Lines on a Cubic Surface
A cubic surface is a complete intersection in $\mathbb{P}^3$ defined by the vanishing of a degree-3 polynomial (the bundle $\mathcal{O}(3)$). 

**In the Graphical Interface:**
- **Mode:** Single GW Invariant
- **Algebra:** `A3`
- **Keep Nodes:** `1`
- **Twisting Bundle K:** `[[3]]`
- **Curve Class (Beta):** `1, 0, 0`
- **Insertions:** *(Leave empty)*
- **Click:** Compute GW Invariant (Output: `27`)

**In Python:**
```python
from gwflags import FlagVariety

X = FlagVariety('A3', [1])
lines = X.gw([], beta=(1, 0, 0), K=[[3]])
print(f"Number of lines on a cubic surface: {lines}")
```

### The 2875 Lines on a Quintic Threefold
A quintic threefold is a Calabi-Yau manifold in $\mathbb{P}^4$ defined by $\mathcal{O}(5)$.

**In the Graphical Interface:**
- **Mode:** Single GW Invariant
- **Algebra:** `A4`
- **Keep Nodes:** `1`
- **Twisting Bundle K:** `[[5]]`
- **Curve Class (Beta):** `1, 0, 0, 0`
- **Insertions:** *(Leave empty)*
- **Click:** Compute GW Invariant (Output: `2875`)

**In Python:**
```python
from gwflags import FlagVariety

X = FlagVariety('A4', [1])
lines = X.gw([], beta=(1, 0, 0, 0), K=[[5]])
print(f"Number of lines on a quintic threefold: {lines}")
```

---

## Example 2: Intersection Theory on Grassmannians
You can compute Gromov-Witten invariants on more complex flag varieties. Here, we compute a 3-point invariant on $Gr(2,4)$ using specific Schubert classes. 
*Note: The GUI requires entering the explicit Weyl group elements for insertions, separated by a pipe `|`.*

**In the Graphical Interface:**
- **Mode:** Single GW Invariant
- **Algebra:** `A3`
- **Keep Nodes:** `2`
- **Twisting Bundle K:** *(Leave empty)*
- **Curve Class (Beta):** `0, 1, 0`
- **Insertions:** `((0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 0, 0), (0, 1, 0, 0)) | ((0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1)) | ((1, 0, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 1, 0, 0))`
- **Click:** Compute GW Invariant (Output: `1`)

**In Python:**
```python
from gwflags import FlagVariety

X = FlagVariety('A3', [2])
classes = X.classes
val = X.gw([classes[5], classes[2], classes[3]], beta=(0, 1, 0))
print(f"3-point GW invariant on Gr(2,4): {val}")
```

---

## Example 3: Small Quantum Multiplication Matrix
If you want to compute the entire spectrum of the quantum connection at once, you can extract the full $c_1(TX) \star (-)$ small quantum multiplication matrix.

### Quantum Matrix for $\mathbb{P}^2$
**In the Graphical Interface:**
- **Mode:** Quantum Multiplication
- **Algebra:** `A2`
- **Keep Nodes:** `1`
- **Twisting Bundle K:** *(Leave empty)*
- **Click:** Compute SQM

**In Python:**
```python
from gwflags import FlagVariety

X = FlagVariety('A2', [1])
M, Gr, basis = X.small_quantum_multiplication()
for row in M:
    print([str(sym) for sym in row])
```

### Quantum Matrix for $Gr(2,4)$
**In the Graphical Interface:**
- **Mode:** Quantum Multiplication
- **Algebra:** `A3`
- **Keep Nodes:** `2`
- **Twisting Bundle K:** *(Leave empty)*
- **Click:** Compute SQM

**In Python:**
```python
from gwflags import FlagVariety

X = FlagVariety('A3', [2])
M, Gr, basis = X.small_quantum_multiplication()
for row in M:
    print([str(sym) for sym in row])
```

---

## Example 4: Eigenvalues of the Quantum Connection
To verify if a geometry is semisimple, you extract the eigenvalues of the matrix generated in Example 3.

**In the Graphical Interface:**
Once you click **Compute SQM** for any space, the interface will automatically compute the characteristic polynomial and display the exact symbolic eigenvalues (e.g. roots of unity for $\mathbb{P}^2$) at the bottom of the result panel!

**In Python:**
```python
from gwflags import FlagVariety

X = FlagVariety('A2', [1])
M, Gr, basis = X.small_quantum_multiplication()
eigs = X.eigenvalues(M)
print(eigs)
```
