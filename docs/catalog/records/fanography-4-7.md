---
title: "Fanography 4-7"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 4-7."
keywords: ["Fanography 4-7", "Fano variety 4-7", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "smooth toric ambient", "regularized exponent multiset"]
---

# Fanography 4-7 — toric complete intersection in smooth 4-fold

**Geometric presentation.** Smooth complete intersection of codimension 1 in a smooth projective toric 4-fold of Picard rank 4 (fan presentation retained).

**Fanography family:** [4-7](https://fanography.info/4-7/) — Blowup of [2-32](https://fanography.info/2-32/) in the disjoint union of a curve of degree $(0,1)$ and a curve of degree $(1,0)$. [Fano variety 4-7 reference card](../fanography.md#fano-variety-4-7) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 1. **Dimension:** 3. **Index:** 1. **h(1,1):** 4.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5, y4=7`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{10} + 34 z^{9} - 661 z^{8} - 43482 z^{7} - 546655 z^{6} + 3063482 z^{5} + 125596986 z^{4} + 804859346 z^{3} - 3757434088 z^{2} - 65732679940 z - 224178705023\) | 10 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-49243506798844197336518773702920000000\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{10} + 34 \lambda^{9} - 661 \lambda^{8} - 43482 \lambda^{7} - 546655 \lambda^{6} + 3063482 \lambda^{5} + 125596986 \lambda^{4} + 804859346 \lambda^{3} - 3757434088 \lambda^{2} - 65732679940 \lambda - 224178705023=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-4-7). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=4$, codimension $1$, recorded index $1$, $(-K_X)^3=36$, $e(X)=10$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&4&&0&\\0&&0&&0&&0\\&0&&4&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 10; full even rank: 10; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=36,&\int_X c_1 c_2&=24,\\\int_X c_3&=10,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, 0, 0], [0, 0, -1, -1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]]
cones = [[0, 1, 3, 5], [1, 2, 6, 7], [3, 4, 6, 7], [1, 3, 5, 7], [0, 1, 3, 6], [2, 4, 6, 7], [1, 2, 5, 7], [0, 1, 2, 5], [0, 3, 4, 6], [0, 1, 2, 6], [1, 3, 6, 7], [0, 3, 4, 5], [3, 4, 5, 7], [0, 2, 4, 6], [2, 4, 5, 7], [0, 2, 4, 5]]
K = [[0, 0, 0, 1, 1, 0, 1, 1]]
novikov_divisors = [[0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5, 'y4': 7}
```

**Ordered ambient basis:**

```python
['1', 'x5', 'x2', 'x1', 'x0', 'x2*x5', 'x1*x5', 'x1*x2', 'x0*x5', 'x1*x2*x5']
```

Curve enumeration: positive; 21 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x5', 'x2', 'x1', 'x0', 'x2*x5', 'x1*x5', 'x1*x2', 'x0*x5', 'x1*x2*x5']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $2 y_{2} y_{3}$ |
| 0 | 2 | $2 y_{1} y_{4}$ |
| 0 | 3 | $2 y_{1} y_{4} + 2 y_{3} y_{4}$ |
| 0 | 4 | $2 y_{2} y_{3} + 2 y_{3} y_{4}$ |
| 0 | 6 | $3 y_{2} y_{3} y_{4}$ |
| 0 | 7 | $3 y_{1} y_{3} y_{4}$ |
| 0 | 8 | $3 y_{2} y_{3} y_{4}$ |
| 0 | 9 | $4 y_{1} y_{2} y_{3} y_{4}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{2}$ |
| 1 | 4 | $y_{3}$ |
| 1 | 5 | $2 y_{1} y_{4}$ |
| 1 | 6 | $2 y_{1} y_{4} + 2 y_{3} y_{4}$ |
| 1 | 8 | $2 y_{3} y_{4}$ |
| 1 | 9 | $3 y_{1} y_{3} y_{4}$ |
| 2 | 0 | $1$ |
| 2 | 2 | $- y_{1}$ |
| 2 | 3 | $y_{4}$ |
| 2 | 5 | $2 y_{2} y_{3}$ |
| 2 | 7 | $2 y_{3} y_{4}$ |
| 2 | 9 | $3 y_{2} y_{3} y_{4}$ |
| 3 | 0 | $1$ |
| 3 | 2 | $y_{1}$ |
| 3 | 3 | $- y_{4}$ |
| 3 | 4 | $y_{3}$ |
| 3 | 6 | $2 y_{2} y_{3}$ |
| 3 | 8 | $2 y_{2} y_{3}$ |
| 4 | 0 | $1$ |
| 4 | 1 | $y_{2}$ |
| 4 | 3 | $y_{4}$ |
| 4 | 4 | $- y_{3}$ |
| 4 | 7 | $2 y_{1} y_{4}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $2$ |
| 5 | 4 | $1$ |
| 5 | 5 | $- y_{1}$ |
| 5 | 6 | $y_{4}$ |
| 5 | 7 | $y_{4}$ |
| 5 | 9 | $2 y_{3} y_{4}$ |
| 6 | 1 | $1$ |
| 6 | 2 | $-1$ |
| 6 | 3 | $1$ |
| 6 | 4 | $-1$ |
| 6 | 5 | $y_{1} - y_{2}$ |
| 6 | 6 | $- y_{2} - y_{4}$ |
| 6 | 7 | $- y_{4}$ |
| 6 | 8 | $y_{3}$ |
| 7 | 2 | $2$ |
| 7 | 3 | $3$ |
| 7 | 4 | $2$ |
| 7 | 5 | $y_{2}$ |
| 7 | 6 | $y_{2}$ |
| 7 | 9 | $2 y_{2} y_{3}$ |
| 8 | 1 | $1$ |
| 8 | 2 | $1$ |
| 8 | 3 | $1$ |
| 8 | 4 | $4$ |
| 8 | 5 | $y_{2}$ |
| 8 | 6 | $y_{2} + y_{4}$ |
| 8 | 7 | $y_{4}$ |
| 8 | 8 | $- y_{3}$ |
| 8 | 9 | $2 y_{1} y_{4}$ |
| 9 | 5 | $2$ |
| 9 | 6 | $3$ |
| 9 | 7 | $2$ |
| 9 | 8 | $2$ |
