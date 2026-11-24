---
title: "Fanography 4-12"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 4-12."
keywords: ["Fanography 4-12", "Fano variety 4-12", "dimension 3", "threefold", "Fano threefold", "Fanography", "Smooth projective toric threefold", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "smooth toric ambient", "regularized exponent multiset"]
---

# Fanography 4-12 — smooth projective toric threefold

**Geometric presentation.** Smooth projective toric threefold given directly by its complete smooth fan of Picard rank 4.

**Fanography family:** [4-12](https://fanography.info/4-12/) — Blowup of [2-33](https://fanography.info/2-33/) in the disjoint union of two exceptional lines of the blowup. [Fano variety 4-12 reference card](../fanography.md#fano-variety-4-12) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Smooth projective toric threefold. **Dimension:** 3. **Index:** 1. **h(1,1):** 4.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5, y4=7`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{10} + 34 z^{9} - 537 z^{8} - 34466 z^{7} - 374135 z^{6} + 3668358 z^{5} + 134240062 z^{4} + 1516208890 z^{3} + 9881149656 z^{2} + 39769549792 z + 107639990857\) | 10 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=12916102359272388972376456175057450085888\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{10} + 34 \lambda^{9} - 537 \lambda^{8} - 34466 \lambda^{7} - 374135 \lambda^{6} + 3668358 \lambda^{5} + 134240062 \lambda^{4} + 1516208890 \lambda^{3} + 9881149656 \lambda^{2} + 39769549792 \lambda + 107639990857=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-4-12). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** smooth toric Fano ambient (no defining bundle twist).
$\dim X=3$, $\dim Y=3$, codimension $0$, recorded index $1$, $(-K_X)^3=46$, $e(X)=10$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&4&&0&\\0&&0&&0&&0\\&0&&4&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 10; full even rank: 10; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=46,&\int_X c_1 c_2&=24,\\\int_X c_3&=10,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, -1], [0, 0, -1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 0], [1, 1, 1]]
cones = [[0, 1, 3], [1, 4, 5], [0, 2, 3], [1, 3, 5], [3, 5, 6], [2, 3, 6], [0, 2, 4], [0, 1, 4], [2, 4, 6], [4, 5, 6]]
K = []
novikov_divisors = [[0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5, 'y4': 7}
```

**Ordered ambient basis:**

```python
['1', 'x3', 'x2', 'x1', 'x0', 'x2*x3', 'x1*x3', 'x0*x2', 'x0*x1', 'x0*x1*x3']
```

Curve enumeration: positive; 70 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x3', 'x2', 'x1', 'x0', 'x2*x3', 'x1*x3', 'x0*x2', 'x0*x1', 'x0*x1*x3']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 2 | $2 y_{3} y_{4}$ |
| 0 | 3 | $2 y_{3} y_{4}$ |
| 0 | 4 | $2 y_{2} y_{4}$ |
| 0 | 7 | $3 y_{2} y_{3} y_{4}$ |
| 0 | 8 | $3 y_{2} y_{3} y_{4}$ |
| 0 | 9 | $4 y_{1} y_{2} y_{3} y_{4}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{1}$ |
| 1 | 3 | $- y_{4}$ |
| 1 | 5 | $2 y_{3} y_{4}$ |
| 1 | 6 | $2 y_{1} y_{4} + 2 y_{3} y_{4}$ |
| 1 | 8 | $- 2 y_{2} y_{4}$ |
| 1 | 9 | $3 y_{2} y_{3} y_{4}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $y_{1}$ |
| 2 | 2 | $- y_{3}$ |
| 2 | 3 | $y_{4}$ |
| 2 | 5 | $- 2 y_{1} y_{3}$ |
| 2 | 6 | $- 2 y_{1} y_{4}$ |
| 2 | 7 | $2 y_{2} y_{4}$ |
| 2 | 8 | $2 y_{2} y_{4}$ |
| 3 | 0 | $1$ |
| 3 | 1 | $- y_{1}$ |
| 3 | 2 | $y_{3}$ |
| 3 | 3 | $- y_{2} - y_{4}$ |
| 3 | 4 | $y_{2}$ |
| 3 | 5 | $2 y_{1} y_{3}$ |
| 3 | 6 | $- 2 y_{1} y_{2} + 2 y_{1} y_{4}$ |
| 3 | 8 | $- 2 y_{1} y_{2}$ |
| 4 | 0 | $2$ |
| 4 | 2 | $y_{3}$ |
| 4 | 5 | $2 y_{1} y_{3}$ |
| 4 | 7 | $2 y_{3} y_{4}$ |
| 4 | 8 | $2 y_{3} y_{4}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $2$ |
| 5 | 5 | $- y_{3}$ |
| 5 | 6 | $y_{4}$ |
| 5 | 9 | $2 y_{2} y_{4}$ |
| 6 | 1 | $1$ |
| 6 | 3 | $1$ |
| 6 | 5 | $y_{3}$ |
| 6 | 6 | $- y_{1} - y_{2} - y_{4}$ |
| 6 | 8 | $- y_{2}$ |
| 7 | 1 | $2$ |
| 7 | 2 | $2$ |
| 7 | 4 | $4$ |
| 7 | 5 | $y_{3}$ |
| 7 | 9 | $2 y_{3} y_{4}$ |
| 8 | 1 | $-2$ |
| 8 | 3 | $1$ |
| 8 | 4 | $-2$ |
| 8 | 5 | $- y_{3}$ |
| 8 | 6 | $y_{1}$ |
| 8 | 9 | $- 2 y_{3} y_{4}$ |
| 9 | 5 | $2$ |
| 9 | 6 | $1$ |
| 9 | 7 | $4$ |
| 9 | 8 | $2$ |
