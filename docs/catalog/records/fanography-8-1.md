---
title: "Fanography 8-1"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 8-1."
keywords: ["Fanography 8-1", "Fano variety 8-1", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "product of projective spaces", "regularized exponent multiset"]
---

# Fanography 8-1 — complete intersection in \(\mathbb P^{1}\times \mathbb P^{3}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{1}\times \mathbb P^{3}\). Defining multidegrees in this factor order: `[[0, 3]]`.

**Fanography family:** [8-1](https://fanography.info/8-1/) — $\mathbb{P}^1\times\mathrm{Bl}_6\mathbb{P}^2$. [Fano variety 8-1 reference card](../fanography.md#fano-variety-8-1) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 1. **Dimension:** 3. **Index:** 1. **h(1,1):** 8.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{2} + 24 z + 132\) | 2 | 2 |
| \(z^{2} - 84 z + 1752\) | 2 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=3158562816\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{2} + 24 \lambda + 132=0\) | \(\{\!\{\frac{1}{3},\frac{2}{3}\}\!\}\) |
| \(\lambda^{2} - 84 \lambda + 1752=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-8-1). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=4$, codimension $1$, recorded index $1$, $(-K_X)^3=18$, $e(X)=18$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&8&&0&\\0&&0&&0&&0\\&0&&8&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 6; full even rank: 18; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=18,&\int_X c_1 c_2&=24,\\\int_X c_3&=18,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, -1, 0], [0, 0, 0, -1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
cones = [[0, 2, 3, 4], [2, 3, 4, 5], [0, 2, 4, 5], [0, 1, 4, 5], [0, 1, 3, 5], [0, 1, 3, 4], [1, 3, 4, 5], [0, 2, 3, 5]]
K = [[0, 0, 0, 0, 0, 3]]
novikov_divisors = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:**

```python
['1', 'x1', 'x0', 'x0^2', 'x0*x1', 'x0^2*x1']
```

Curve enumeration: positive; 7 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x1', 'x0', 'x0^2', 'x0*x1', 'x0^2*x1']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $2 y_{2}$ |
| 0 | 2 | $108 y_{1}^{2}$ |
| 0 | 3 | $756 y_{1}^{3}$ |
| 1 | 0 | $2$ |
| 1 | 4 | $108 y_{1}^{2}$ |
| 1 | 5 | $756 y_{1}^{3}$ |
| 2 | 0 | $1$ |
| 2 | 2 | $9 y_{1}$ |
| 2 | 3 | $108 y_{1}^{2}$ |
| 2 | 4 | $2 y_{2}$ |
| 3 | 2 | $1$ |
| 3 | 5 | $2 y_{2}$ |
| 4 | 1 | $1$ |
| 4 | 2 | $2$ |
| 4 | 4 | $9 y_{1}$ |
| 4 | 5 | $108 y_{1}^{2}$ |
| 5 | 3 | $2$ |
| 5 | 4 | $1$ |
