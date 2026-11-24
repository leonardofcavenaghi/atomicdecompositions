---
title: "Fanography 3-6"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 3-6."
keywords: ["Fanography 3-6", "Fano variety 3-6", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "split projective bundle over product", "regularized exponent multiset"]
---

# Fanography 3-6 — section of \(\mathbb P_{\mathbb P^{1}\times \mathbb P^{1}}(\mathcal O^{\oplus 2}\oplus \mathcal O(0,1))\)

**Geometric presentation.** Ambient variety: \(\mathbb P_{\mathbb P^{1}\times \mathbb P^{1}}(\mathcal O^{\oplus 2}\oplus \mathcal O(0,1))\), in the quotient convention. Defining divisor coordinates in the base-and-\(\xi\) lattice basis: `[[1, 0, 2]]`.

**Fanography family:** [3-6](https://fanography.info/3-6/) — Blowup of [1-17](https://fanography.info/1-17/) in the disjoint union of a line and an elliptic curve of degree 4. [Fano variety 3-6 reference card](../fanography.md#fano-variety-3-6) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 1. **Dimension:** 3. **Index:** 1. **h(1,1):** 3.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 11\) | 1 | 2 |
| \(z^{6} - 8 z^{5} - 1376 z^{4} - 14562 z^{3} + 224496 z^{2} + 4298640 z + 17704065\) | 6 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 11=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
| \(\lambda^{6} - 8 \lambda^{5} - 1376 \lambda^{4} - 14562 \lambda^{3} + 224496 \lambda^{2} + 4298640 \lambda + 17704065=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-3-6). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=4$, codimension $1$, recorded index $1$, $(-K_X)^3=22$, $e(X)=6$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&3&&0&\\0&&1&&1&&0\\&0&&3&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 8; full even rank: 8; full odd rank: 2 ($h^{1,2}=1$).

$$
\begin{aligned}\int_X c_1^3&=22,&\int_X c_1 c_2&=24,\\\int_X c_3&=6,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, -1, 0], [0, 0, 0, -1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]]
cones = [[1, 3, 5, 6], [0, 1, 5, 6], [0, 2, 3, 4], [1, 3, 4, 6], [0, 1, 3, 5], [0, 2, 4, 6], [0, 1, 3, 4], [0, 2, 5, 6], [0, 2, 3, 5], [0, 1, 4, 6], [2, 3, 4, 6], [2, 3, 5, 6]]
K = [[0, 0, 1, 0, 0, 2, 2]]
novikov_divisors = [[0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5}
```

**Ordered ambient basis:**

```python
['1', 'x4', 'x1', 'x0', 'x0^2', 'x1*x4', 'x0*x4', 'x0^2*x4']
```

Curve enumeration: positive; 18 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x4', 'x1', 'x0', 'x0^2', 'x1*x4', 'x0*x4', 'x0^2*x4']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $4 y_{1} y_{2}$ |
| 0 | 2 | $8 y_{2} y_{3}$ |
| 0 | 3 | $4 y_{1} y_{2} + 4 y_{2}^{2} + 8 y_{2} y_{3}$ |
| 0 | 4 | $12 y_{1} y_{2}^{2} + 12 y_{1} y_{2} y_{3} + 12 y_{2}^{2} y_{3} + 3 y_{2} y_{3}^{2}$ |
| 0 | 5 | $12 y_{1} y_{2} y_{3}$ |
| 0 | 6 | $12 y_{1} y_{2}^{2} + 12 y_{1} y_{2} y_{3}$ |
| 0 | 7 | $32 y_{1} y_{2}^{2} y_{3} + 4 y_{1} y_{2} y_{3}^{2}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{1}$ |
| 1 | 3 | $2 y_{2}$ |
| 1 | 4 | $4 y_{2}^{2} + 8 y_{2} y_{3}$ |
| 1 | 5 | $8 y_{2} y_{3}$ |
| 1 | 6 | $4 y_{2}^{2} + 8 y_{2} y_{3}$ |
| 1 | 7 | $12 y_{2}^{2} y_{3} + 3 y_{2} y_{3}^{2}$ |
| 2 | 0 | $1$ |
| 2 | 2 | $- y_{3}$ |
| 2 | 3 | $3 y_{2}$ |
| 2 | 4 | $6 y_{1} y_{2} + 2 y_{2}^{2} + 2 y_{2} y_{3}$ |
| 2 | 5 | $4 y_{1} y_{2}$ |
| 2 | 6 | $6 y_{1} y_{2}$ |
| 2 | 7 | $6 y_{1} y_{2}^{2} + 3 y_{1} y_{2} y_{3}$ |
| 3 | 0 | $1$ |
| 3 | 1 | $y_{1}$ |
| 3 | 2 | $2 y_{3}$ |
| 3 | 4 | $4 y_{1} y_{2} + 4 y_{2} y_{3}$ |
| 3 | 6 | $4 y_{1} y_{2}$ |
| 3 | 7 | $6 y_{1} y_{2} y_{3}$ |
| 4 | 2 | $2$ |
| 4 | 3 | $3$ |
| 4 | 5 | $2 y_{1}$ |
| 4 | 6 | $y_{1}$ |
| 4 | 7 | $4 y_{1} y_{2}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $2$ |
| 5 | 3 | $1$ |
| 5 | 4 | $4 y_{2}$ |
| 5 | 5 | $- y_{3}$ |
| 5 | 6 | $3 y_{2}$ |
| 5 | 7 | $2 y_{1} y_{2} + 2 y_{2}^{2} + 2 y_{2} y_{3}$ |
| 6 | 1 | $1$ |
| 6 | 2 | $-2$ |
| 6 | 3 | $-1$ |
| 6 | 5 | $- 2 y_{1} + 2 y_{3}$ |
| 6 | 6 | $- y_{1}$ |
| 6 | 7 | $- 4 y_{1} y_{2} + 4 y_{2} y_{3}$ |
| 7 | 4 | $4$ |
| 7 | 5 | $2$ |
| 7 | 6 | $3$ |
