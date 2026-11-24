---
title: "Fanography 3-20"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 3-20."
keywords: ["Fanography 3-20", "Fano variety 3-20", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "smooth toric ambient", "regularized exponent multiset"]
---

# Fanography 3-20 — toric complete intersection in smooth 4-fold

**Geometric presentation.** Smooth complete intersection of codimension 1 in a smooth projective toric 4-fold of Picard rank 3 (fan presentation retained).

**Fanography family:** [3-20](https://fanography.info/3-20/) — Blowup of [1-16](https://fanography.info/1-16/) in the disjoint union of two lines. [Fano variety 3-20 reference card](../fanography.md#fano-variety-3-20) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 1. **Dimension:** 3. **Index:** 1. **h(1,1):** 3.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{8} + 20 z^{7} - 188 z^{6} - 9780 z^{5} - 146664 z^{4} - 1437960 z^{3} - 8901700 z^{2} - 38593640 z - 85607500\) | 8 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1079081496086971632192\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{8} + 20 \lambda^{7} - 188 \lambda^{6} - 9780 \lambda^{5} - 146664 \lambda^{4} - 1437960 \lambda^{3} - 8901700 \lambda^{2} - 38593640 \lambda - 85607500=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-3-20). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=4$, codimension $1$, recorded index $1$, $(-K_X)^3=38$, $e(X)=8$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&3&&0&\\0&&0&&0&&0\\&0&&3&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 8; full even rank: 8; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=38,&\int_X c_1 c_2&=24,\\\int_X c_3&=8,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, -1, -1], [-1, -1, 0, 0], [0, 0, -1, -1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
cones = [[3, 4, 5, 6], [1, 3, 4, 6], [0, 1, 4, 6], [0, 2, 3, 5], [2, 4, 5, 6], [1, 3, 4, 5], [0, 1, 3, 6], [0, 2, 4, 5], [0, 1, 3, 5], [0, 2, 4, 6], [0, 2, 3, 6], [0, 1, 4, 5], [2, 3, 5, 6]]
K = [[0, 0, 0, 0, 1, 0, 1]]
novikov_divisors = [[0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5}
```

**Ordered ambient basis:**

```python
['1', 'x2', 'x1', 'x0', 'x2^2', 'x1^2', 'x0^2', 'x0^2*x2']
```

Curve enumeration: positive; 11 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x2', 'x1', 'x0', 'x2^2', 'x1^2', 'x0^2', 'x0^2*x2']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $2 y_{2} y_{3}$ |
| 0 | 2 | $2 y_{1} y_{3}$ |
| 0 | 4 | $- 3 y_{1} y_{2} y_{3}$ |
| 0 | 5 | $- 3 y_{1} y_{2} y_{3}$ |
| 0 | 7 | $4 y_{1} y_{2} y_{3}^{2}$ |
| 1 | 0 | $2$ |
| 1 | 1 | $- y_{1}$ |
| 1 | 3 | $y_{1}$ |
| 1 | 4 | $- 2 y_{1} y_{3}$ |
| 1 | 6 | $- 2 y_{1} y_{3}$ |
| 1 | 7 | $3 y_{1} y_{2} y_{3}$ |
| 2 | 0 | $2$ |
| 2 | 2 | $- y_{2}$ |
| 2 | 3 | $y_{2}$ |
| 2 | 5 | $- 2 y_{2} y_{3}$ |
| 2 | 6 | $- 2 y_{2} y_{3}$ |
| 2 | 7 | $3 y_{1} y_{2} y_{3}$ |
| 3 | 0 | $3$ |
| 3 | 1 | $y_{3}$ |
| 3 | 2 | $y_{3}$ |
| 3 | 3 | $- y_{3}$ |
| 3 | 4 | $- 2 y_{1} y_{3}$ |
| 3 | 5 | $- 2 y_{2} y_{3}$ |
| 3 | 6 | $- 2 y_{1} y_{3} - 2 y_{2} y_{3}$ |
| 3 | 7 | $3 y_{1} y_{2} y_{3}$ |
| 4 | 1 | $\frac{1}{2}$ |
| 4 | 2 | $- \frac{3}{2}$ |
| 4 | 3 | $-2$ |
| 4 | 4 | $- \frac{y_{1}}{2}$ |
| 4 | 5 | $\frac{y_{2}}{2}$ |
| 4 | 6 | $\frac{y_{1}}{2} - \frac{y_{2}}{2} + y_{3}$ |
| 4 | 7 | $- 2 y_{2} y_{3}$ |
| 5 | 1 | $- \frac{3}{2}$ |
| 5 | 2 | $\frac{1}{2}$ |
| 5 | 3 | $-2$ |
| 5 | 4 | $\frac{y_{1}}{2}$ |
| 5 | 5 | $- \frac{y_{2}}{2}$ |
| 5 | 6 | $- \frac{y_{1}}{2} + \frac{y_{2}}{2} + y_{3}$ |
| 5 | 7 | $- 2 y_{1} y_{3}$ |
| 6 | 1 | $- \frac{3}{2}$ |
| 6 | 2 | $- \frac{3}{2}$ |
| 6 | 3 | $1$ |
| 6 | 4 | $\frac{y_{1}}{2}$ |
| 6 | 5 | $\frac{y_{2}}{2}$ |
| 6 | 6 | $- \frac{y_{1}}{2} - \frac{y_{2}}{2} - y_{3}$ |
| 7 | 4 | $-2$ |
| 7 | 5 | $-2$ |
| 7 | 6 | $-2$ |
