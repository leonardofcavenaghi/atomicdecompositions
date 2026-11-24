---
title: "Fanography 3-3"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 3-3."
keywords: ["Fanography 3-3", "Fano variety 3-3", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "product of projective spaces", "regularized exponent multiset"]
---

# Fanography 3-3 — complete intersection in \(\mathbb P^{1}\times \mathbb P^{1}\times \mathbb P^{2}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{1}\times \mathbb P^{1}\times \mathbb P^{2}\). Defining multidegrees in this factor order: `[[1, 1, 2]]`.

**Fanography family:** [3-3](https://fanography.info/3-3/) — Divisor on $\mathbb{P}^1\times\mathbb{P}^1\times\mathbb{P}^2$ of degree $(1,1,2)$. [Fano variety 3-3 reference card](../fanography.md#fano-variety-3-3) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 1. **Dimension:** 3. **Index:** 1. **h(1,1):** 3.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 15\) | 1 | 2 |
| \(z^{6} - 20 z^{5} - 1972 z^{4} - 21550 z^{3} + 162028 z^{2} + 2216640 z - 2683599\) | 6 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-26066935185320448\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 15=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
| \(\lambda^{6} - 20 \lambda^{5} - 1972 \lambda^{4} - 21550 \lambda^{3} + 162028 \lambda^{2} + 2216640 \lambda - 2683599=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-3-3). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=4$, codimension $1$, recorded index $1$, $(-K_X)^3=18$, $e(X)=2$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&3&&0&\\0&&3&&3&&0\\&0&&3&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 8; full even rank: 8; full odd rank: 6 ($h^{1,2}=3$).

$$
\begin{aligned}\int_X c_1^3&=18,&\int_X c_1 c_2&=24,\\\int_X c_3&=2,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, -1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
cones = [[1, 2, 3, 6], [2, 3, 5, 6], [2, 4, 5, 6], [0, 1, 3, 4], [0, 2, 3, 5], [1, 2, 4, 6], [0, 3, 4, 5], [0, 1, 2, 3], [0, 1, 2, 4], [3, 4, 5, 6], [1, 3, 4, 6], [0, 2, 4, 5]]
K = [[0, 0, 0, 0, 2, 1, 1]]
novikov_divisors = [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5}
```

**Ordered ambient basis:**

```python
['1', 'x2', 'x1', 'x0', 'x2^2', 'x1*x2', 'x0*x2', 'x1*x2^2']
```

Curve enumeration: positive; 23 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x2', 'x1', 'x0', 'x2^2', 'x1*x2', 'x0*x2', 'x1*x2^2']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $8 y_{1} y_{3} + 8 y_{2} y_{3} + 4 y_{3}^{2}$ |
| 0 | 2 | $2 y_{1} y_{2} + 8 y_{2} y_{3}$ |
| 0 | 3 | $2 y_{1} y_{2} + 8 y_{1} y_{3}$ |
| 0 | 4 | $3 y_{1}^{2} y_{3} + 18 y_{1} y_{2} y_{3} + 12 y_{1} y_{3}^{2} + 3 y_{2}^{2} y_{3} + 12 y_{2} y_{3}^{2}$ |
| 0 | 5 | $36 y_{1} y_{2} y_{3} + 6 y_{2}^{2} y_{3} + 24 y_{2} y_{3}^{2}$ |
| 0 | 6 | $6 y_{1}^{2} y_{3} + 36 y_{1} y_{2} y_{3} + 24 y_{1} y_{3}^{2}$ |
| 0 | 7 | $16 y_{1}^{2} y_{2} y_{3} + 16 y_{1} y_{2}^{2} y_{3} + 80 y_{1} y_{2} y_{3}^{2}$ |
| 1 | 0 | $1$ |
| 1 | 2 | $2 y_{2}$ |
| 1 | 3 | $2 y_{1}$ |
| 1 | 4 | $4 y_{1} y_{3} + 4 y_{2} y_{3}$ |
| 1 | 5 | $2 y_{1} y_{2} + 8 y_{2} y_{3}$ |
| 1 | 6 | $2 y_{1} y_{2} + 8 y_{1} y_{3}$ |
| 1 | 7 | $18 y_{1} y_{2} y_{3}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $3 y_{3}$ |
| 2 | 2 | $- y_{2}$ |
| 2 | 3 | $y_{1}$ |
| 2 | 4 | $6 y_{1} y_{3} + 2 y_{2} y_{3} + 2 y_{3}^{2}$ |
| 2 | 5 | $8 y_{1} y_{3} + 4 y_{2} y_{3} + 4 y_{3}^{2}$ |
| 2 | 6 | $12 y_{1} y_{3}$ |
| 2 | 7 | $3 y_{1}^{2} y_{3} + 9 y_{1} y_{2} y_{3} + 12 y_{1} y_{3}^{2}$ |
| 3 | 0 | $1$ |
| 3 | 1 | $3 y_{3}$ |
| 3 | 2 | $y_{2}$ |
| 3 | 3 | $- y_{1}$ |
| 3 | 4 | $2 y_{1} y_{3} + 6 y_{2} y_{3} + 2 y_{3}^{2}$ |
| 3 | 5 | $12 y_{2} y_{3}$ |
| 3 | 6 | $4 y_{1} y_{3} + 8 y_{2} y_{3} + 4 y_{3}^{2}$ |
| 3 | 7 | $9 y_{1} y_{2} y_{3} + 3 y_{2}^{2} y_{3} + 12 y_{2} y_{3}^{2}$ |
| 4 | 1 | $1$ |
| 4 | 2 | $-2$ |
| 4 | 3 | $-2$ |
| 4 | 4 | $- 6 y_{3}$ |
| 4 | 5 | $2 y_{2} - 6 y_{3}$ |
| 4 | 6 | $2 y_{1} - 6 y_{3}$ |
| 4 | 7 | $2 y_{1} y_{2} - 4 y_{1} y_{3} - 4 y_{2} y_{3} - 4 y_{3}^{2}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $2$ |
| 5 | 3 | $1$ |
| 5 | 4 | $3 y_{3}$ |
| 5 | 5 | $- y_{2} + 3 y_{3}$ |
| 5 | 6 | $y_{1} + 3 y_{3}$ |
| 5 | 7 | $6 y_{1} y_{3} + 2 y_{2} y_{3} + 2 y_{3}^{2}$ |
| 6 | 1 | $1$ |
| 6 | 2 | $1$ |
| 6 | 3 | $2$ |
| 6 | 4 | $3 y_{3}$ |
| 6 | 5 | $y_{2} + 3 y_{3}$ |
| 6 | 6 | $- y_{1} + 3 y_{3}$ |
| 6 | 7 | $2 y_{1} y_{3} + 6 y_{2} y_{3} + 2 y_{3}^{2}$ |
| 7 | 4 | $2$ |
| 7 | 5 | $3$ |
| 7 | 6 | $3$ |
