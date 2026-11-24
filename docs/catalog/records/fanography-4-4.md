---
title: "Fanography 4-4"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 4-4."
keywords: ["Fanography 4-4", "Fano variety 4-4", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "smooth toric ambient", "regularized exponent multiset"]
---

# Fanography 4-4 — toric complete intersection in smooth 4-fold

**Geometric presentation.** Smooth complete intersection of codimension 1 in a smooth projective toric 4-fold of Picard rank 3 (fan presentation retained).

**Fanography family:** [4-4](https://fanography.info/4-4/) — Blowup of [3-19](https://fanography.info/3-19/) in the proper transform of a conic through the points. [Fano variety 4-4 reference card](../fanography.md#fano-variety-4-4) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 1. **Dimension:** 3. **Index:** 1. **h(1,1):** 4.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 12\) | 1 | 1 |
| \(z + 10\) | 1 | 1 |
| \(z^{2} + 26 z + 193\) | 2 | 1 |
| \(z^{4} - 38 z^{3} + 60 z^{2} + 1880 z + 54320\) | 4 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-3933489233992860432000\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 12=0\) | \(\{\!\{0\}\!\}\) |
| \(\lambda + 10=0\) | \(\{\!\{0\}\!\}\) |
| \(\lambda^{2} + 26 \lambda + 193=0\) | \(\{\!\{0\}\!\}\) |
| \(\lambda^{4} - 38 \lambda^{3} + 60 \lambda^{2} + 1880 \lambda + 54320=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-4-4). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=4$, codimension $1$, recorded index $1$, $(-K_X)^3=32$, $e(X)=10$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&4&&0&\\0&&0&&0&&0\\&0&&4&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 8; full even rank: 10; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=32,&\int_X c_1 c_2&=24,\\\int_X c_3&=10,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, -1, -1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0]]
cones = [[0, 1, 2, 4], [0, 1, 4, 5], [0, 4, 5, 6], [1, 2, 3, 6], [0, 1, 3, 5], [0, 2, 4, 6], [1, 3, 5, 6], [0, 1, 2, 3], [0, 2, 3, 6], [1, 4, 5, 6], [1, 2, 4, 6], [0, 3, 5, 6]]
K = [[0, 0, 0, 0, 2, 2, 2]]
novikov_divisors = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5}
```

**Ordered ambient basis:**

```python
['1', 'x3', 'x2', 'x0', 'x0^2', 'x2*x3', 'x0*x3', 'x0^2*x3']
```

Curve enumeration: positive; 14 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x3', 'x2', 'x0', 'x0^2', 'x2*x3', 'x0*x3', 'x0^2*x3']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 2 | $4 y_{2} y_{3}$ |
| 0 | 3 | $4 y_{2} y_{3} + 4 y_{3}^{2}$ |
| 0 | 4 | $6 y_{1} y_{2} y_{3} + 12 y_{2} y_{3}^{2}$ |
| 0 | 5 | $6 y_{1} y_{2} y_{3}$ |
| 0 | 6 | $6 y_{1} y_{2} y_{3}$ |
| 0 | 7 | $16 y_{1} y_{2} y_{3}^{2}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{1}$ |
| 1 | 4 | $4 y_{2} y_{3}$ |
| 1 | 5 | $4 y_{2} y_{3}$ |
| 1 | 6 | $4 y_{2} y_{3} + 4 y_{3}^{2}$ |
| 1 | 7 | $12 y_{2} y_{3}^{2}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $y_{1}$ |
| 2 | 2 | $- y_{2}$ |
| 2 | 3 | $2 y_{3}$ |
| 2 | 4 | $4 y_{3}^{2}$ |
| 2 | 5 | $- 2 y_{1} y_{2}$ |
| 3 | 0 | $1$ |
| 3 | 2 | $y_{2}$ |
| 3 | 4 | $4 y_{2} y_{3}$ |
| 3 | 5 | $2 y_{1} y_{2}$ |
| 3 | 7 | $6 y_{1} y_{2} y_{3}$ |
| 4 | 2 | $1$ |
| 4 | 3 | $2$ |
| 4 | 6 | $y_{1}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $2$ |
| 5 | 4 | $2 y_{3}$ |
| 5 | 5 | $- y_{2}$ |
| 5 | 6 | $2 y_{3}$ |
| 5 | 7 | $4 y_{3}^{2}$ |
| 6 | 1 | $1$ |
| 6 | 3 | $1$ |
| 6 | 5 | $y_{2}$ |
| 6 | 6 | $- y_{1}$ |
| 6 | 7 | $4 y_{2} y_{3}$ |
| 7 | 4 | $3$ |
| 7 | 5 | $1$ |
| 7 | 6 | $2$ |
