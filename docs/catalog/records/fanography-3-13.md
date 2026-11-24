---
title: "Fanography 3-13"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 3-13."
keywords: ["Fanography 3-13", "Fano variety 3-13", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 3", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "product of projective spaces", "regularized exponent multiset"]
---

# Fanography 3-13 — complete intersection in \(\mathbb P^{2}\times \mathbb P^{2}\times \mathbb P^{2}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{2}\times \mathbb P^{2}\times \mathbb P^{2}\). Defining multidegrees in this factor order: `[[0, 1, 1], [1, 0, 1], [1, 1, 0]]`.

**Fanography family:** [3-13](https://fanography.info/3-13/) — Blowup of [2-32](https://fanography.info/2-32/) in a curve $C$ of bidegree $(2,2)$ such that the composition $C\hookrightarrow W\hookrightarrow\mathbb{P}^2\times\mathbb{P}^2\overset{p_i}{\to}\mathbb{P}^2$ is an embedding for $i=1,2$. [Fano variety 3-13 reference card](../fanography.md#fano-variety-3-13) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 3. **Dimension:** 3. **Index:** 1. **h(1,1):** 3.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 10\) | 1 | 1 |
| \(z^{7} + 10 z^{6} - 372 z^{5} - 12240 z^{4} - 169872 z^{3} - 1400160 z^{2} - 6802624 z - 17221120\) | 7 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-18895710683557527552\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 10=0\) | \(\{\!\{0\}\!\}\) |
| \(\lambda^{7} + 10 \lambda^{6} - 372 \lambda^{5} - 12240 \lambda^{4} - 169872 \lambda^{3} - 1400160 \lambda^{2} - 6802624 \lambda - 17221120=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-3-13). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=6$, codimension $3$, recorded index $1$, $(-K_X)^3=30$, $e(X)=8$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&3&&0&\\0&&0&&0&&0\\&0&&3&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 8; full even rank: 8; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=30,&\int_X c_1 c_2&=24,\\\int_X c_3&=8,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, 0, 0, 0, 0], [0, 0, -1, -1, 0, 0], [0, 0, 0, 0, -1, -1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]]
cones = [[0, 1, 2, 4, 5, 8], [0, 1, 2, 4, 6, 8], [0, 1, 3, 4, 6, 8], [1, 2, 4, 5, 7, 8], [0, 2, 4, 5, 6, 7], [1, 2, 4, 6, 7, 8], [0, 2, 3, 5, 6, 8], [0, 1, 3, 4, 5, 7], [0, 1, 3, 4, 6, 7], [0, 1, 2, 3, 6, 8], [0, 1, 2, 4, 6, 7], [0, 3, 4, 5, 6, 8], [1, 3, 4, 5, 7, 8], [0, 1, 2, 3, 5, 8], [0, 1, 2, 3, 5, 7], [0, 3, 4, 5, 6, 7], [2, 4, 5, 6, 7, 8], [1, 2, 3, 5, 7, 8], [0, 2, 4, 5, 6, 8], [1, 2, 3, 6, 7, 8], [3, 4, 5, 6, 7, 8], [1, 3, 4, 6, 7, 8], [0, 1, 3, 4, 5, 8], [0, 2, 3, 5, 6, 7], [2, 3, 5, 6, 7, 8], [0, 1, 2, 3, 6, 7], [0, 1, 2, 4, 5, 7]]
K = [[0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 1]]
novikov_divisors = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5}
```

**Ordered ambient basis:**

```python
['1', 'x2', 'x1', 'x0', 'x2^2', 'x1^2', 'x0^2', 'x1*x2^2']
```

Curve enumeration: positive; 23 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x2', 'x1', 'x0', 'x2^2', 'x1^2', 'x0^2', 'x1*x2^2']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $2 y_{1} y_{3} + 2 y_{2} y_{3}$ |
| 0 | 2 | $2 y_{1} y_{2} + 2 y_{2} y_{3}$ |
| 0 | 3 | $2 y_{1} y_{2} + 2 y_{1} y_{3}$ |
| 0 | 4 | $6 y_{1} y_{2} y_{3}$ |
| 0 | 5 | $6 y_{1} y_{2} y_{3}$ |
| 0 | 6 | $6 y_{1} y_{2} y_{3}$ |
| 0 | 7 | $4 y_{1}^{2} y_{2} y_{3} + 4 y_{1} y_{2}^{2} y_{3} + 4 y_{1} y_{2} y_{3}^{2}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{3}$ |
| 1 | 2 | $y_{2}$ |
| 1 | 3 | $y_{1}$ |
| 1 | 5 | $2 y_{1} y_{2}$ |
| 1 | 6 | $2 y_{1} y_{2}$ |
| 1 | 7 | $3 y_{1} y_{2} y_{3}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $y_{3}$ |
| 2 | 2 | $- y_{2}$ |
| 2 | 3 | $y_{1}$ |
| 2 | 4 | $2 y_{1} y_{3}$ |
| 2 | 6 | $2 y_{1} y_{3}$ |
| 2 | 7 | $3 y_{1} y_{2} y_{3}$ |
| 3 | 0 | $1$ |
| 3 | 1 | $y_{3}$ |
| 3 | 2 | $y_{2}$ |
| 3 | 3 | $- y_{1}$ |
| 3 | 4 | $2 y_{2} y_{3}$ |
| 3 | 5 | $2 y_{2} y_{3}$ |
| 3 | 7 | $3 y_{1} y_{2} y_{3}$ |
| 4 | 1 | $3$ |
| 4 | 2 | $1$ |
| 4 | 3 | $1$ |
| 4 | 4 | $- y_{3}$ |
| 4 | 5 | $y_{2}$ |
| 4 | 6 | $y_{1}$ |
| 4 | 7 | $2 y_{1} y_{2}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $3$ |
| 5 | 3 | $1$ |
| 5 | 4 | $y_{3}$ |
| 5 | 5 | $- y_{2}$ |
| 5 | 6 | $y_{1}$ |
| 5 | 7 | $2 y_{1} y_{3}$ |
| 6 | 1 | $1$ |
| 6 | 2 | $1$ |
| 6 | 3 | $3$ |
| 6 | 4 | $y_{3}$ |
| 6 | 5 | $y_{2}$ |
| 6 | 6 | $- y_{1}$ |
| 6 | 7 | $2 y_{2} y_{3}$ |
| 7 | 4 | $2$ |
| 7 | 5 | $2$ |
| 7 | 6 | $2$ |
