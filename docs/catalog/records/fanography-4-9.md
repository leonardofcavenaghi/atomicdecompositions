---
title: "Fanography 4-9"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 4-9."
keywords: ["Fanography 4-9", "Fano variety 4-9", "dimension 3", "threefold", "Fano threefold", "Fanography", "Smooth projective toric threefold", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "smooth toric ambient", "regularized exponent multiset"]
---

# Fanography 4-9 — smooth projective toric threefold

**Geometric presentation.** Smooth projective toric threefold given directly by its complete smooth fan of Picard rank 4.

**Fanography family:** [4-9](https://fanography.info/4-9/) — Blowup of [3-25](https://fanography.info/3-25/) in an exceptional curve of the blowup. [Fano variety 4-9 reference card](../fanography.md#fano-variety-4-9) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Smooth projective toric threefold. **Dimension:** 3. **Index:** 1. **h(1,1):** 4.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5, y4=7`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{10} + 34 z^{9} - 477 z^{8} - 38358 z^{7} - 564547 z^{6} + 1766202 z^{5} + 137771146 z^{4} + 1514246734 z^{3} + 4988155340 z^{2} - 26102362020 z - 175678959575\) | 10 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=165817641047241935898510222530191288276480\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{10} + 34 \lambda^{9} - 477 \lambda^{8} - 38358 \lambda^{7} - 564547 \lambda^{6} + 1766202 \lambda^{5} + 137771146 \lambda^{4} + 1514246734 \lambda^{3} + 4988155340 \lambda^{2} - 26102362020 \lambda - 175678959575=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-4-9). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** smooth toric Fano ambient (no defining bundle twist).
$\dim X=3$, $\dim Y=3$, codimension $0$, recorded index $1$, $(-K_X)^3=40$, $e(X)=10$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&4&&0&\\0&&0&&0&&0\\&0&&4&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 10; full even rank: 10; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=40,&\int_X c_1 c_2&=24,\\\int_X c_3&=10,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, -1], [-1, -1, 0], [0, 0, -1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 0]]
cones = [[2, 4, 6], [0, 2, 5], [3, 4, 6], [0, 2, 4], [1, 3, 4], [3, 5, 6], [0, 1, 4], [2, 5, 6], [0, 1, 5], [1, 3, 5]]
K = []
novikov_divisors = [[0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5, 'y4': 7}
```

**Ordered ambient basis:**

```python
['1', 'x4', 'x2', 'x1', 'x0', 'x2*x4', 'x1*x4', 'x0*x2', 'x0*x1', 'x0*x1*x4']
```

Curve enumeration: positive; 70 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x4', 'x2', 'x1', 'x0', 'x2*x4', 'x1*x4', 'x0*x2', 'x0*x1', 'x0*x1*x4']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 2 | $2 y_{2} y_{4}$ |
| 0 | 3 | $2 y_{3} y_{4}$ |
| 0 | 6 | $3 y_{1} y_{3} y_{4}$ |
| 0 | 7 | $3 y_{2} y_{3} y_{4}$ |
| 0 | 8 | $3 y_{2} y_{3} y_{4}$ |
| 0 | 9 | $4 y_{1} y_{2} y_{3} y_{4}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{1}$ |
| 1 | 5 | $2 y_{2} y_{4}$ |
| 1 | 6 | $2 y_{3} y_{4}$ |
| 1 | 9 | $3 y_{2} y_{3} y_{4}$ |
| 2 | 0 | $2$ |
| 2 | 2 | $- y_{3}$ |
| 2 | 4 | $y_{3}$ |
| 2 | 5 | $- 2 y_{1} y_{3}$ |
| 2 | 7 | $- 2 y_{1} y_{3} + 2 y_{3} y_{4}$ |
| 2 | 8 | $2 y_{3} y_{4}$ |
| 2 | 9 | $3 y_{1} y_{3} y_{4}$ |
| 3 | 0 | $2$ |
| 3 | 1 | $y_{1}$ |
| 3 | 3 | $- y_{2}$ |
| 3 | 4 | $y_{2}$ |
| 3 | 7 | $2 y_{2} y_{4}$ |
| 3 | 8 | $2 y_{2} y_{4}$ |
| 4 | 0 | $3$ |
| 4 | 1 | $y_{1}$ |
| 4 | 2 | $y_{4}$ |
| 4 | 3 | $y_{4}$ |
| 4 | 4 | $- y_{4}$ |
| 4 | 7 | $2 y_{2} y_{4} + 2 y_{3} y_{4}$ |
| 4 | 8 | $2 y_{2} y_{4} + 2 y_{3} y_{4}$ |
| 4 | 9 | $3 y_{1} y_{3} y_{4}$ |
| 5 | 1 | $2$ |
| 5 | 2 | $1$ |
| 5 | 5 | $- y_{1} - y_{3}$ |
| 5 | 7 | $- y_{3}$ |
| 5 | 9 | $2 y_{3} y_{4}$ |
| 6 | 1 | $2$ |
| 6 | 3 | $3$ |
| 6 | 6 | $- y_{2}$ |
| 6 | 8 | $y_{2}$ |
| 6 | 9 | $2 y_{2} y_{4}$ |
| 7 | 1 | $-3$ |
| 7 | 2 | $1$ |
| 7 | 4 | $-2$ |
| 7 | 5 | $y_{1} - y_{4}$ |
| 7 | 6 | $- y_{4}$ |
| 7 | 7 | $- y_{4}$ |
| 7 | 9 | $- 2 y_{2} y_{4} - 2 y_{3} y_{4}$ |
| 8 | 1 | $3$ |
| 8 | 3 | $1$ |
| 8 | 4 | $3$ |
| 8 | 5 | $y_{4}$ |
| 8 | 6 | $y_{4}$ |
| 8 | 7 | $y_{4}$ |
| 8 | 9 | $2 y_{2} y_{4} + 2 y_{3} y_{4}$ |
| 9 | 5 | $1$ |
| 9 | 6 | $1$ |
| 9 | 7 | $2$ |
| 9 | 8 | $3$ |
