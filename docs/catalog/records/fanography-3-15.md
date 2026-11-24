---
title: "Fanography 3-15"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 3-15."
keywords: ["Fanography 3-15", "Fano variety 3-15", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "split projective bundle over product", "regularized exponent multiset"]
---

# Fanography 3-15 — section of \(\mathbb P_{\mathbb P^{1}\times \mathbb P^{2}}(\mathcal O(0,1)\oplus \mathcal O(1,0))\)

**Geometric presentation.** Ambient variety: \(\mathbb P_{\mathbb P^{1}\times \mathbb P^{2}}(\mathcal O(0,1)\oplus \mathcal O(1,0))\), in the quotient convention. Defining divisor coordinates in the base-and-\(\xi\) lattice basis: `[[0, 1, 1]]`.

**Fanography family:** [3-15](https://fanography.info/3-15/) — Blowup of [1-16](https://fanography.info/1-16/) in the disjoint union of a line and a conic. [Fano variety 3-15 reference card](../fanography.md#fano-variety-3-15) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 1. **Dimension:** 3. **Index:** 1. **h(1,1):** 3.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 7\) | 1 | 1 |
| \(z^{7} + 13 z^{6} - 609 z^{5} - 16047 z^{4} - 137340 z^{3} + 53250 z^{2} + 9545405 z + 39712175\) | 7 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-316944704202326234244\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 7=0\) | \(\{\!\{0\}\!\}\) |
| \(\lambda^{7} + 13 \lambda^{6} - 609 \lambda^{5} - 16047 \lambda^{4} - 137340 \lambda^{3} + 53250 \lambda^{2} + 9545405 \lambda + 39712175=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-3-15). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=4$, codimension $1$, recorded index $1$, $(-K_X)^3=32$, $e(X)=8$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&3&&0&\\0&&0&&0&&0\\&0&&3&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 8; full even rank: 8; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=32,&\int_X c_1 c_2&=24,\\\int_X c_3&=8,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, -1, -1], [-1, -1, -1, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [1, 1, 1, 0]]
cones = [[1, 2, 3, 5], [0, 1, 3, 5], [0, 1, 4, 5], [1, 2, 3, 4], [0, 3, 4, 6], [0, 4, 5, 6], [1, 2, 4, 5], [0, 3, 5, 6], [0, 1, 3, 4], [2, 3, 4, 6], [2, 4, 5, 6], [2, 3, 5, 6]]
K = [[0, 0, 0, 0, 0, 2, 1]]
novikov_divisors = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5}
```

**Ordered ambient basis:**

```python
['1', 'x3', 'x1', 'x0', 'x3^2', 'x1*x3', 'x0*x3', 'x1^2*x3']
```

Curve enumeration: positive; 14 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x3', 'x1', 'x0', 'x3^2', 'x1*x3', 'x0*x3', 'x1^2*x3']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $4 y_{2} y_{3}$ |
| 0 | 2 | $4 y_{2} y_{3}$ |
| 0 | 3 | $2 y_{1} y_{3}$ |
| 0 | 4 | $3 y_{1} y_{2} y_{3} + 3 y_{2} y_{3}^{2}$ |
| 0 | 5 | $6 y_{2} y_{3}^{2}$ |
| 0 | 6 | $6 y_{1} y_{2} y_{3}$ |
| 0 | 7 | $- 16 y_{1} y_{2} y_{3}^{2}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{2}$ |
| 1 | 2 | $2 y_{3}$ |
| 1 | 6 | $2 y_{1} y_{3}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $y_{2}$ |
| 2 | 2 | $- y_{1} - y_{3}$ |
| 2 | 3 | $y_{1}$ |
| 2 | 4 | $2 y_{2} y_{3}$ |
| 2 | 5 | $4 y_{2} y_{3}$ |
| 2 | 7 | $- 6 y_{1} y_{2} y_{3}$ |
| 3 | 0 | $2$ |
| 3 | 1 | $y_{2}$ |
| 3 | 4 | $4 y_{2} y_{3}$ |
| 3 | 5 | $4 y_{2} y_{3}$ |
| 3 | 6 | $4 y_{2} y_{3}$ |
| 3 | 7 | $- 6 y_{1} y_{2} y_{3} - 6 y_{2} y_{3}^{2}$ |
| 4 | 1 | $1$ |
| 4 | 2 | $-2$ |
| 4 | 3 | $-2$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 5 | $2 y_{3}$ |
| 4 | 6 | $- 2 y_{2}$ |
| 4 | 7 | $- 4 y_{1} y_{3} + 8 y_{2} y_{3}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $3$ |
| 5 | 3 | $1$ |
| 5 | 4 | $y_{2}$ |
| 5 | 5 | $- y_{1} - y_{3}$ |
| 5 | 6 | $y_{1} + y_{2}$ |
| 5 | 7 | $- 4 y_{2} y_{3}$ |
| 6 | 1 | $2$ |
| 6 | 2 | $2$ |
| 6 | 3 | $3$ |
| 6 | 4 | $y_{2}$ |
| 6 | 6 | $y_{2}$ |
| 6 | 7 | $- 8 y_{2} y_{3}$ |
| 7 | 4 | $-1$ |
| 7 | 5 | $-1$ |
| 7 | 6 | $- \frac{3}{2}$ |
