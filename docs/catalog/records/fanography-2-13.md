---
title: "Fanography 2-13"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 2-13."
keywords: ["Fanography 2-13", "Fano variety 2-13", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 3", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "product of projective spaces", "regularized exponent multiset"]
---

# Fanography 2-13 — complete intersection in \(\mathbb P^{2}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{2}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[1, 1], [1, 1], [0, 2]]`.

**Fanography family:** [2-13](https://fanography.info/2-13/) — Blowup of [1-16](https://fanography.info/1-16/) in a curve of degree 6 and genus 2. [Fano variety 2-13 reference card](../fanography.md#fano-variety-2-13) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 3. **Dimension:** 3. **Index:** 1. **h(1,1):** 2.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 8\) | 1 | 2 |
| \(z + 6\) | 1 | 1 |
| \(z^{3} - 18 z^{2} - 540 z - 5400\) | 3 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-93350880\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 8=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
| \(\lambda + 6=0\) | \(\{\!\{0\}\!\}\) |
| \(\lambda^{3} - 18 \lambda^{2} - 540 \lambda - 5400=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-2-13). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=6$, codimension $3$, recorded index $1$, $(-K_X)^3=20$, $e(X)=2$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&2&&0&\\0&&2&&2&&0\\&0&&2&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 6; full even rank: 6; full odd rank: 4 ($h^{1,2}=2$).

$$
\begin{aligned}\int_X c_1^3&=20,&\int_X c_1 c_2&=24,\\\int_X c_3&=2,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, 0, 0, 0, 0], [0, 0, -1, -1, -1, -1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]]
cones = [[1, 2, 4, 5, 6, 7], [0, 1, 3, 4, 5, 7], [1, 2, 3, 4, 6, 7], [1, 3, 4, 5, 6, 7], [0, 1, 3, 4, 5, 6], [0, 2, 3, 4, 5, 6], [0, 1, 2, 4, 5, 6], [0, 2, 3, 4, 5, 7], [1, 2, 3, 5, 6, 7], [0, 1, 2, 3, 5, 7], [0, 1, 2, 3, 4, 6], [0, 1, 2, 4, 5, 7], [0, 1, 2, 3, 5, 6], [2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 7]]
K = [[0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 2, 0, 0]]
novikov_divisors = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:**

```python
['1', 'x1', 'x0', 'x1^2', 'x0^2', 'x1^3']
```

Curve enumeration: positive; 13 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x1', 'x0', 'x1^2', 'x0^2', 'x1^3']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $12 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 0 | 2 | $12 y_{1} y_{2}$ |
| 0 | 3 | $6 y_{1}^{2} y_{2} + 72 y_{1} y_{2}^{2}$ |
| 0 | 4 | $6 y_{1}^{2} y_{2} + 24 y_{1} y_{2}^{2}$ |
| 0 | 5 | $64 y_{1}^{2} y_{2}^{2} + 64 y_{1} y_{2}^{3}$ |
| 1 | 0 | $1$ |
| 1 | 2 | $2 y_{1}$ |
| 1 | 3 | $16 y_{1} y_{2}$ |
| 1 | 4 | $8 y_{1} y_{2}$ |
| 1 | 5 | $6 y_{1}^{2} y_{2} + 24 y_{1} y_{2}^{2}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $4 y_{2}$ |
| 2 | 2 | $- y_{1}$ |
| 2 | 3 | $4 y_{1} y_{2} + 8 y_{2}^{2}$ |
| 2 | 4 | $4 y_{1} y_{2}$ |
| 2 | 5 | $24 y_{1} y_{2}^{2}$ |
| 3 | 1 | $\frac{3}{2}$ |
| 3 | 2 | $\frac{1}{2}$ |
| 3 | 4 | $y_{1}$ |
| 3 | 5 | $6 y_{1} y_{2}$ |
| 4 | 1 | $\frac{3}{2}$ |
| 4 | 2 | $\frac{5}{2}$ |
| 4 | 3 | $8 y_{2}$ |
| 4 | 4 | $- y_{1}$ |
| 4 | 5 | $6 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 5 | 3 | $3$ |
| 5 | 4 | $1$ |
