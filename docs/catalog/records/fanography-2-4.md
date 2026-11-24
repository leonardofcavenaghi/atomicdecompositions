---
title: "Fanography 2-4"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 2-4."
keywords: ["Fanography 2-4", "Fano variety 2-4", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "product of projective spaces", "regularized exponent multiset"]
---

# Fanography 2-4 — complete intersection in \(\mathbb P^{1}\times \mathbb P^{3}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{1}\times \mathbb P^{3}\). Defining multidegrees in this factor order: `[[1, 3]]`.

**Fanography family:** [2-4](https://fanography.info/2-4/) — Blowup of [1-17](https://fanography.info/1-17/) in the intersection of two cubics. [Fano variety 2-4 reference card](../fanography.md#fano-variety-2-4) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 1. **Dimension:** 3. **Index:** 1. **h(1,1):** 2.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 20\) | 1 | 2 |
| \(z^{4} - 90 z^{3} - 2511 z^{2} + 39744 z + 919200\) | 4 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=405795200\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 20=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
| \(\lambda^{4} - 90 \lambda^{3} - 2511 \lambda^{2} + 39744 \lambda + 919200=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-2-4). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=4$, codimension $1$, recorded index $1$, $(-K_X)^3=10$, $e(X)=-14$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&2&&0&\\0&&10&&10&&0\\&0&&2&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 6; full even rank: 6; full odd rank: 20 ($h^{1,2}=10$).

$$
\begin{aligned}\int_X c_1^3&=10,&\int_X c_1 c_2&=24,\\\int_X c_3&=-14,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, 0, 0, 0], [0, -1, -1, -1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
cones = [[0, 2, 3, 4], [0, 1, 2, 3], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [0, 1, 3, 4], [2, 3, 4, 5], [0, 1, 2, 4]]
K = [[0, 0, 0, 0, 3, 1]]
novikov_divisors = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:**

```python
['1', 'x1', 'x0', 'x1^2', 'x0*x1', 'x1^3']
```

Curve enumeration: positive; 13 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x1', 'x0', 'x1^2', 'x0*x1', 'x1^3']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $36 y_{1} y_{2} + 108 y_{2}^{2}$ |
| 0 | 2 | $36 y_{1} y_{2}$ |
| 0 | 3 | $27 y_{1}^{2} y_{2} + 864 y_{1} y_{2}^{2} + 756 y_{2}^{3}$ |
| 0 | 4 | $54 y_{1}^{2} y_{2} + 972 y_{1} y_{2}^{2}$ |
| 0 | 5 | $4 y_{1}^{3} y_{2} + 504 y_{1}^{2} y_{2}^{2} + 3024 y_{1} y_{2}^{3}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $9 y_{2}$ |
| 1 | 2 | $3 y_{1}$ |
| 1 | 3 | $60 y_{1} y_{2} + 108 y_{2}^{2}$ |
| 1 | 4 | $90 y_{1} y_{2}$ |
| 1 | 5 | $18 y_{1}^{2} y_{2} + 324 y_{1} y_{2}^{2}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $11 y_{2}$ |
| 2 | 2 | $- y_{1}$ |
| 2 | 3 | $16 y_{1} y_{2} + 156 y_{2}^{2}$ |
| 2 | 4 | $30 y_{1} y_{2} + 108 y_{2}^{2}$ |
| 2 | 5 | $3 y_{1}^{2} y_{2} + 180 y_{1} y_{2}^{2} + 252 y_{2}^{3}$ |
| 3 | 1 | $1$ |
| 3 | 4 | $3 y_{1}$ |
| 3 | 5 | $12 y_{1} y_{2}$ |
| 4 | 1 | $1$ |
| 4 | 2 | $1$ |
| 4 | 3 | $14 y_{2}$ |
| 4 | 4 | $- y_{1} + 9 y_{2}$ |
| 4 | 5 | $8 y_{1} y_{2} + 36 y_{2}^{2}$ |
| 5 | 3 | $4$ |
| 5 | 4 | $3$ |
