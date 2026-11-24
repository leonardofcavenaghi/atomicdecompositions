---
title: "Fanography 2-25"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 2-25."
keywords: ["Fanography 2-25", "Fano variety 2-25", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "product of projective spaces", "regularized exponent multiset"]
---

# Fanography 2-25 — complete intersection in \(\mathbb P^{1}\times \mathbb P^{3}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{1}\times \mathbb P^{3}\). Defining multidegrees in this factor order: `[[1, 2]]`.

**Fanography family:** [2-25](https://fanography.info/2-25/) — Blowup of [1-17](https://fanography.info/1-17/) in an elliptic curve which is an intersection of 2 quadrics. [Fano variety 2-25 reference card](../fanography.md#fano-variety-2-25) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 1. **Dimension:** 3. **Index:** 1. **h(1,1):** 2.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 2\) | 1 | 2 |
| \(z^{4} - 96 z^{2} - 1536 z - 768\) | 4 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 2=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
| \(\lambda^{4} - 96 \lambda^{2} - 1536 \lambda - 768=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-2-25). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=4$, codimension $1$, recorded index $1$, $(-K_X)^3=32$, $e(X)=4$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&2&&0&\\0&&1&&1&&0\\&0&&2&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 6; full even rank: 6; full odd rank: 2 ($h^{1,2}=1$).

$$
\begin{aligned}\int_X c_1^3&=32,&\int_X c_1 c_2&=24,\\\int_X c_3&=4,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, 0, 0, 0], [0, -1, -1, -1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
cones = [[0, 2, 3, 4], [0, 1, 2, 3], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [0, 1, 3, 4], [2, 3, 4, 5], [0, 1, 2, 4]]
K = [[0, 0, 0, 0, 2, 1]]
novikov_divisors = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:**

```python
['1', 'x1', 'x0', 'x1^2', 'x0*x1', 'x1^3']
```

Curve enumeration: positive; 7 classes including zero.

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
| 0 | 1 | $4 y_{2}$ |
| 0 | 3 | $12 y_{1} y_{2}$ |
| 0 | 4 | $12 y_{1} y_{2}$ |
| 0 | 5 | $4 y_{1}^{2} y_{2}$ |
| 1 | 0 | $2$ |
| 1 | 2 | $2 y_{1}$ |
| 1 | 3 | $4 y_{2}$ |
| 1 | 5 | $6 y_{1} y_{2}$ |
| 2 | 0 | $1$ |
| 2 | 2 | $- y_{1}$ |
| 2 | 3 | $6 y_{2}$ |
| 2 | 4 | $4 y_{2}$ |
| 2 | 5 | $3 y_{1} y_{2}$ |
| 3 | 1 | $2$ |
| 3 | 4 | $2 y_{1}$ |
| 4 | 1 | $1$ |
| 4 | 2 | $2$ |
| 4 | 4 | $- y_{1}$ |
| 4 | 5 | $2 y_{2}$ |
| 5 | 3 | $4$ |
| 5 | 4 | $4$ |
