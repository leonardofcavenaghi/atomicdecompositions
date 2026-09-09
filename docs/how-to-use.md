# How to Use `gwflags`

This guide bridges the theoretical framework of the Atomic Decomposition of Complete Intersections in Flag Varieties with practical computation using the `gwflags` package. Below, we showcase how to compute the projected flag-ambient part of small quantum multiplication by the first Chern class for several prominent geometric spaces. 

By analyzing the eigenvalues and Jordan defects of these matrices, you can extract coarse Hodge atoms and establish irrationality proofs or K3-center constraints.

---

## 1. Cubic Fourfolds
**Theory:** $X = \mathcal{Z}(\mathbb{P}^5, \mathcal{O}_{\mathbb{P}^5}(3))$. 
The small quantum multiplication by $c_1(TX)$ yields an eigenvalue 0 with algebraic multiplicity 2 and geometric multiplicity 1 (Jordan defect 1). This proves the irrationality of Hodge-general cubic fourfolds and recovers uniform K3-center constraints.

**Python API:**
```python
from gwflags import FlagVariety, O

# P^5 represented by A5 algebra, keeping node 1
X = FlagVariety('A5', [1])
bundle = O(X, 3)

# Compute the small quantum multiplication matrix
matrix = X.small_quantum_multiplication(bundle)
```

---

## 2. Küchle Fourfolds of type (c5)
**Theory:** $F = \text{Gr}(3,7)$, $X = \mathcal{Z}(F, \Lambda^2 \mathcal{U}^\vee \oplus \Lambda^3 \mathcal{Q} \oplus \mathcal{O}_F(1))$. 
This is a crucial counter-example where the ambient-completeness condition (AC) fails. The localization computes a $6 \times 6$ matrix that only sees the projected flag-ambient operator, demonstrating why one must distinguish cohomology inherited from the flag variety from the larger monodromy-fixed part.

**Python API:**
```python
from gwflags import FlagVariety, O, osum, wedge, dual, taut_sub, taut_quot

# Gr(3,7) represented by A6 algebra, keeping node 3
X = FlagVariety('A6', [3])

# Construct the complex vector bundle
bundle = osum(wedge(2, dual(taut_sub(X, 3))), wedge(3, taut_quot(X, 3)), O(X, 1))

matrix = X.small_quantum_multiplication(bundle)
```

---

## 3. Ordinary Gushel–Mukai Fourfolds
**Theory:** $F = \text{Gr}(2,5)$, $X = \mathcal{Z}(F, \mathcal{O}_F(1) \oplus \mathcal{O}_F(2))$. 
The operator has 0 as a semisimple eigenvalue of multiplicity 2 (Jordan defect 0), plus four simple nonzero eigenvalues. This satisfies both multiplicity and Jordan-defect bounds, recovering irrationality for Hodge-general members.

**Python API:**
```python
from gwflags import FlagVariety, O, osum

# Gr(2,5) represented by A4 algebra, keeping node 2
X = FlagVariety('A4', [2])
bundle = osum(O(X, 1), O(X, 2))

matrix = X.small_quantum_multiplication(bundle)
```

---

## 4. Quartic Fourfolds
**Theory:** $X = \mathcal{Z}(\mathbb{P}^5, \mathcal{O}_{\mathbb{P}^5}(4))$. 
A Fano fourfold of index 2. The zero eigenvalue has algebraic multiplicity 3 and geometric multiplicity 1 (a single Jordan block of size 3).

**CLI Usage:**
For quick computations from the command line, `gwflags` provides a convenient CLI.
```bash
python3 -m gwflags.cli A5 --keep 1 -K 4 sqm
```

---

## 5. Intersections of a Quadric and a Cubic in $\mathbb{P}^6$
**Theory:** $X = \mathcal{Z}(\mathbb{P}^6, \mathcal{O}_{\mathbb{P}^6}(2) \oplus \mathcal{O}_{\mathbb{P}^6}(3))$. 
Fano fourfold of index 2. Similar to the quartic, the zero eigenvalue has algebraic multiplicity 3 and geometric multiplicity 1.

**CLI Usage:**
```bash
python3 -m gwflags.cli A6 --keep 1 -K "2;3" sqm
```

---

## 6. Intersection of Three Quadrics in $\mathbb{P}^7$
**Theory:** $X = \mathcal{Z}(\mathbb{P}^7, \mathcal{O}_{\mathbb{P}^7}(2)^{\oplus 3})$. 
Fano fourfold of index 2. The zero eigenvalue has algebraic multiplicity 3 and geometric multiplicity 1.

**CLI Usage:**
```bash
python3 -m gwflags.cli A7 --keep 1 -K "2;2;2" sqm
```
