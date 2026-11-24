---
title: "Fanography 4-6"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 4-6."
keywords: ["Fanography 4-6", "Fano variety 4-6", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 2", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "split projective bundle over product", "regularized exponent multiset"]
---

# Fanography 4-6 — section of \(\mathbb P_{\mathbb P^{1}\times \mathbb P^{1}\times \mathbb P^{1}}(\mathcal O(0,0,1)\oplus \mathcal O(0,1,0)\oplus \mathcal O(1,0,0))\)

**Geometric presentation.** Ambient variety: \(\mathbb P_{\mathbb P^{1}\times \mathbb P^{1}\times \mathbb P^{1}}(\mathcal O(0,0,1)\oplus \mathcal O(0,1,0)\oplus \mathcal O(1,0,0))\), in the quotient convention. Defining divisor coordinates in the base-and-\(\xi\) lattice basis: `[[0, 0, 0, 1], [0, 0, 0, 1]]`.

**Fanography family:** [4-6](https://fanography.info/4-6/) — Blowup of [1-17](https://fanography.info/1-17/) in the disjoint union of 3 lines. [Fano variety 4-6 reference card](../fanography.md#fano-variety-4-6) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 2. **Dimension:** 3. **Index:** 1. **h(1,1):** 4.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5, y4=7`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{10} + 34 z^{9} - 769 z^{8} - 49986 z^{7} - 619927 z^{6} + 4070582 z^{5} + 132248358 z^{4} + 517247738 z^{3} - 4885419784 z^{2} - 30601667152 z + 3996723241\) | 10 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=10640183582254315768850891156752415232\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{10} + 34 \lambda^{9} - 769 \lambda^{8} - 49986 \lambda^{7} - 619927 \lambda^{6} + 4070582 \lambda^{5} + 132248358 \lambda^{4} + 517247738 \lambda^{3} - 4885419784 \lambda^{2} - 30601667152 \lambda + 3996723241=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-4-6). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=5$, codimension $2$, recorded index $1$, $(-K_X)^3=34$, $e(X)=10$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&4&&0&\\0&&0&&0&&0\\&0&&4&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 10; full even rank: 10; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=34,&\int_X c_1 c_2&=24,\\\int_X c_3&=10,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0]]
cones = [[0, 1, 4, 6, 8], [0, 3, 5, 7, 8], [1, 2, 3, 5, 7], [0, 3, 5, 6, 8], [2, 3, 5, 7, 8], [1, 2, 4, 6, 8], [1, 2, 4, 7, 8], [0, 1, 3, 5, 6], [1, 2, 3, 5, 6], [1, 2, 4, 5, 7], [0, 1, 4, 7, 8], [0, 1, 3, 6, 8], [2, 3, 5, 6, 8], [2, 4, 5, 7, 8], [0, 4, 5, 7, 8], [0, 1, 3, 7, 8], [1, 2, 3, 6, 8], [1, 2, 4, 5, 6], [0, 1, 4, 5, 7], [0, 1, 4, 5, 6], [2, 4, 5, 6, 8], [0, 4, 5, 6, 8], [1, 2, 3, 7, 8], [0, 1, 3, 5, 7]]
K = [[0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1]]
novikov_divisors = [[0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5, 'y4': 7}
```

**Ordered ambient basis:**

```python
['1', 'x6', 'x3', 'x1', 'x0', 'x1^2', 'x3*x6', 'x1*x6', 'x0*x6', 'x1^2*x6']
```

Curve enumeration: positive; 20 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x6', 'x3', 'x1', 'x0', 'x1^2', 'x3*x6', 'x1*x6', 'x0*x6', 'x1^2*x6']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $2 y_{3} y_{4}$ |
| 0 | 2 | $2 y_{1} y_{4}$ |
| 0 | 3 | $2 y_{1} y_{4} + 2 y_{3} y_{4}$ |
| 0 | 4 | $2 y_{2} y_{4}$ |
| 0 | 5 | $- 3 y_{1} y_{2} y_{4} + 3 y_{1} y_{3} y_{4} - 3 y_{2} y_{3} y_{4}$ |
| 0 | 6 | $3 y_{1} y_{3} y_{4}$ |
| 0 | 7 | $3 y_{1} y_{3} y_{4}$ |
| 0 | 8 | $3 y_{2} y_{3} y_{4}$ |
| 0 | 9 | $- 4 y_{1} y_{2} y_{3} y_{4}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{3}$ |
| 1 | 3 | $y_{4}$ |
| 1 | 5 | $2 y_{1} y_{4} - 2 y_{2} y_{4}$ |
| 1 | 6 | $2 y_{1} y_{4}$ |
| 1 | 7 | $2 y_{1} y_{4}$ |
| 1 | 8 | $2 y_{2} y_{4}$ |
| 1 | 9 | $- 3 y_{1} y_{2} y_{4}$ |
| 2 | 0 | $1$ |
| 2 | 2 | $- y_{1}$ |
| 2 | 3 | $y_{4}$ |
| 2 | 5 | $- 2 y_{2} y_{4} + 2 y_{3} y_{4}$ |
| 2 | 6 | $2 y_{3} y_{4}$ |
| 2 | 7 | $2 y_{3} y_{4}$ |
| 2 | 9 | $- 3 y_{2} y_{3} y_{4}$ |
| 3 | 0 | $1$ |
| 3 | 1 | $y_{3}$ |
| 3 | 2 | $y_{1}$ |
| 3 | 3 | $- y_{2} - y_{4}$ |
| 3 | 4 | $y_{2}$ |
| 4 | 0 | $2$ |
| 4 | 1 | $y_{3}$ |
| 4 | 2 | $y_{1}$ |
| 4 | 5 | $- 2 y_{1} y_{4} - 2 y_{3} y_{4}$ |
| 4 | 8 | $2 y_{3} y_{4}$ |
| 4 | 9 | $- 3 y_{1} y_{3} y_{4}$ |
| 5 | 2 | $-2$ |
| 5 | 3 | $-1$ |
| 5 | 4 | $-2$ |
| 5 | 6 | $- y_{3}$ |
| 5 | 8 | $- y_{3}$ |
| 5 | 9 | $2 y_{3} y_{4}$ |
| 6 | 1 | $1$ |
| 6 | 2 | $3$ |
| 6 | 4 | $1$ |
| 6 | 6 | $- y_{1}$ |
| 6 | 7 | $y_{4}$ |
| 6 | 9 | $- 2 y_{2} y_{4} - 2 y_{3} y_{4}$ |
| 7 | 1 | $1$ |
| 7 | 2 | $1$ |
| 7 | 3 | $4$ |
| 7 | 4 | $1$ |
| 7 | 5 | $- 2 y_{2}$ |
| 7 | 6 | $y_{1} + y_{3}$ |
| 7 | 7 | $- y_{2} - y_{4}$ |
| 7 | 8 | $y_{2} + y_{3}$ |
| 8 | 1 | $2$ |
| 8 | 2 | $-2$ |
| 8 | 6 | $y_{1} - y_{3}$ |
| 8 | 8 | $- y_{3}$ |
| 8 | 9 | $- 2 y_{1} y_{4} + 2 y_{3} y_{4}$ |
| 9 | 5 | $2$ |
| 9 | 6 | $-2$ |
| 9 | 7 | $-1$ |
| 9 | 8 | $-2$ |
