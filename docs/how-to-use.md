# How to Use `gwflags`

This guide bridges the theoretical framework of Quantum Cohomology with practical computation using the `gwflags` Python library. You can run these computations directly in a Python script or Jupyter Notebook.

## Example 1: Classic Enumerative Geometry
The `gwflags` library allows you to natively compute Gromov-Witten invariants for complete intersections using Atiyah-Bott localization. Let's compute two famous results in algebraic geometry: the 27 lines on a cubic surface, and the 2875 lines on a quintic threefold.

### The 27 Lines on a Cubic Surface
A cubic surface is a complete intersection in $\mathbb{P}^3$ defined by the vanishing of a degree-3 polynomial (the bundle $\mathcal{O}(3)$). 

```python
from gwflags import FlagVariety

# Define the ambient space P^3 (Cartan type A3, keeping node 1)
X = FlagVariety('A3', [1])

# Compute the 0-point Gromov-Witten invariant for degree 1 curves
# K=[[3]] specifies the twisting bundle O(3)
lines = X.gw([], beta=(1, 0, 0), K=[[3]])

print(f"Number of lines on a cubic surface: {lines}")
# Output: 27
```

### The 2875 Lines on a Quintic Threefold
A quintic threefold is a Calabi-Yau manifold in $\mathbb{P}^4$ defined by $\mathcal{O}(5)$.

```python
from gwflags import FlagVariety

# Define the ambient space P^4
X = FlagVariety('A4', [1])

# Compute the 0-point Gromov-Witten invariant for degree 1 curves
lines = X.gw([], beta=(1, 0, 0, 0), K=[[5]])

print(f"Number of lines on a quintic threefold: {lines}")
# Output: 2875
```

## Example 2: Intersection Theory on Grassmannians
You can compute Gromov-Witten invariants on more complex flag varieties. Here, we compute a 3-point invariant on $Gr(2,4)$ using specific Schubert classes.

```python
from gwflags import FlagVariety

# Define the ambient space Gr(2,4) (Cartan type A3, keeping node 2)
X = FlagVariety('A3', [2])

# Retrieve the Schubert classes (elements of the Weyl group)
classes = X.classes

# classes[5] is the point class (codimension 4)
# classes[2] and classes[3] are classes of codimension 2
# Expected dimension for 3 points on degree 1 curve is 4 + 4(1) + 3 - 3 = 8
# The sum of codimensions (4 + 2 + 2 = 8) satisfies the dimension axiom.

val = X.gw([classes[5], classes[2], classes[3]], beta=(0, 1, 0))

print(f"3-point GW invariant on Gr(2,4): {val}")
# Output: 1
```

## Example 3: Small Quantum Multiplication Matrix
If you want to compute the entire spectrum of the quantum connection at once, you can extract the full $c_1(TX) \star (-)$ small quantum multiplication matrix. Note that these calculations use `sympy` to handle the symbolic Novikov parameters $y_i$.

### Quantum Matrix for $\mathbb{P}^2$
```python
from gwflags import FlagVariety

X = FlagVariety('A2', [1])
M, Gr, basis = X.small_quantum_multiplication()

for row in M:
    print([str(sym) for sym in row])
    
# Output:
# ['0', '0', '3*y1']
# ['3', '0', '0']
# ['0', '3', '0']
```

### Quantum Matrix for $Gr(2,4)$
```python
from gwflags import FlagVariety

X = FlagVariety('A3', [2])
M, Gr, basis = X.small_quantum_multiplication()

for row in M:
    print([str(sym) for sym in row])
    
# Output:
# ['0', '0', '0', '0', '4*y2', '0']
# ['4', '0', '0', '0', '0', '4*y2']
# ['0', '4', '0', '0', '0', '0']
# ['0', '4', '0', '0', '0', '0']
# ['0', '0', '4', '4', '0', '0']
# ['0', '0', '0', '0', '4', '0']
```

## Example 4: Eigenvalues of the Quantum Connection
Once you have the quantum matrix, you can instantly ask `gwflags` to compute its eigenvalues (the spectrum of the quantum connection) to verify if the geometry is semisimple (i.e. has a full set of distinct eigenvalues).

```python
from gwflags import FlagVariety

X = FlagVariety('A2', [1])
M, Gr, basis = X.small_quantum_multiplication()

# Compute the eigenvalues
eigs = X.eigenvalues(M)
print(eigs)

# Output:
# [3*y1**(1/3), 3*y1**(1/3)*(-1 - sqrt(3)*I)/2, 3*y1**(1/3)*(-1 + sqrt(3)*I)/2]
```

## Using the Graphical User Interface (GUI)
If you prefer a visual interface rather than writing Python code, you can start the local server:
```bash
python3 -m gwflags.gui
```
This will start a local server at `http://127.0.0.1:8000`. You can input the Cartan Type, Keep Nodes, and Vector Bundles directly into the web interface and click **Compute SQM** or **Compute GW Invariant**.
