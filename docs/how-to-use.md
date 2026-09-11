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
- **Card 1 (Space Definition)** -> **Algebra:** `A3`
- **Card 1** -> **Keep Simple Roots:** `1`
- **Card 1** -> **Twisting Bundle K:** `[[3]]`
- **Card 3 (GW Invariants)** -> **Curve Class &beta;:** `1, 0, 0`
- **Card 3** -> **Insertions:** *(Leave empty)*
- **Card 3** -> **Click:** Compute Invariant (Output: `27`)

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
- **Card 1 (Space Definition)** -> **Algebra:** `A4`
- **Card 1** -> **Keep Simple Roots:** `1`
- **Card 1** -> **Twisting Bundle K:** `[[5]]`
- **Card 3 (GW Invariants)** -> **Curve Class &beta;:** `1, 0, 0, 0`
- **Card 3** -> **Insertions:** *(Leave empty)*
- **Card 3** -> **Click:** Compute Invariant (Output: `2875`)

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
- **Card 1 (Space Definition)** -> **Algebra:** `A3`
- **Card 1** -> **Keep Simple Roots:** `2`
- **Card 1** -> **Twisting Bundle K:** *(Leave empty)*
- **Card 3 (GW Invariants)** -> **Curve Class &beta;:** `0, 1, 0`
- **Card 3** -> **Insertions:** `((0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 0, 0), (0, 1, 0, 0)) | ((0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1)) | ((1, 0, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 1, 0, 0))`
- **Card 3** -> **Click:** Compute Invariant (Output: `1`)

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
- **Card 1 (Space Definition)** -> **Algebra:** `A2`
- **Card 1** -> **Keep Simple Roots:** `1`
- **Card 1** -> **Twisting Bundle K:** *(Leave empty)*
- **Card 2 (Execution Options)** -> **Click:** Compute c₁(TX)⋆ Matrix

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
- **Card 1 (Space Definition)** -> **Algebra:** `A3`
- **Card 1** -> **Keep Simple Roots:** `2`
- **Card 1** -> **Twisting Bundle K:** *(Leave empty)*
- **Card 2 (Execution Options)** -> **Click:** Compute c₁(TX)⋆ Matrix

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
Once you click **Compute c₁(TX)⋆ Matrix** for any space, the interface will automatically compute the characteristic polynomial and display the exact symbolic eigenvalues (e.g. roots of unity for $\mathbb{P}^2$) at the bottom of the result panel!

**In Python:**
```python
from gwflags import FlagVariety

X = FlagVariety('A2', [1])
M, Gr, basis = X.small_quantum_multiplication()
eigs = X.eigenvalues(M)
print(eigs)
```

### Evaluating Quantum Matrices and Characteristic Polynomials
The GUI now supports **custom evaluation of Novikov variables**. If you want to compute the matrix at specific values (instead of keeping it purely symbolic), you can type `y1=2, y2=-1` into the new **"Evaluate y"** box. The system will automatically substitute these values into the matrix and dynamically compute the corresponding **Characteristic Polynomial** for you to inspect!

## Example 5: Non-Trivial Bundles (Quotient and Tautological Subbundles)
The `gwflags` GUI and CLI parser now natively supports the evaluation of complex Homogeneous Bundles beyond simple sums of line bundles.
For example, you can take a complete intersection cut out by a section of the **Tautological Quotient Bundle** $\mathcal{Q}$.

A famous mathematical identity states that the zero-locus of a regular section of $\mathcal{Q}$ on $Gr(2,5)$ is isomorphic to $\mathbb{P}^3$.
We can verify this isomorphism natively by passing the bundle explicitly:

**In the Graphical Interface:**
- **Card 1 (Space Definition)** -> **Algebra:** `A4`
- **Card 1** -> **Keep Simple Roots:** `2`
- **Card 1** -> **Twisting Bundle K:** `taut_quot(X, 2)`
- **Card 2 (Execution Options)** -> **Click:** Compute c₁(TX)⋆ Matrix
*(Output: You will instantly get a $4 \times 4$ quantum matrix identical to $\mathbb{P}^3$, with characteristic polynomial $\lambda^4 - 256 = 0$!)*

**In Python:**
```python
from gwflags import FlagVariety
from gwflags.bundles import taut_quot

X = FlagVariety('A4', [2])
# Pass the quotient bundle as K
Q = taut_quot(X, 2)
M, Gr, basis = X.small_quantum_multiplication(K=Q)

for row in M:
    print([str(sym) for sym in row])
```
You can also freely use `taut_sub`, `dual`, `sym`, `wedge`, `osum`, and `tensor` in the Twist Bundle input field.
