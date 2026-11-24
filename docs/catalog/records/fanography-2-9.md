---
title: "Fanography 2-9"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 2-9."
keywords: ["Fanography 2-9", "Fano variety 2-9", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 2", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "product of projective spaces", "regularized exponent multiset"]
---

# Fanography 2-9 — complete intersection in \(\mathbb P^{2}\times \mathbb P^{3}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{2}\times \mathbb P^{3}\). Defining multidegrees in this factor order: `[[1, 1], [1, 2]]`.

**Fanography family:** [2-9](https://fanography.info/2-9/) — Complete intersection of degree $(1,1)$ and $(2,1)$ in $\mathbb{P}^3\times\mathbb{P}^2$. [Fano variety 2-9 reference card](../fanography.md#fano-variety-2-9) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 2. **Dimension:** 3. **Index:** 1. **h(1,1):** 2.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 7\) | 1 | 2 |
| \(z^{4} - 8 z^{3} - 1212 z^{2} - 18112 z - 72316\) | 4 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-39304000\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 7=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
| \(\lambda^{4} - 8 \lambda^{3} - 1212 \lambda^{2} - 18112 \lambda - 72316=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-2-9). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=5$, codimension $2$, recorded index $1$, $(-K_X)^3=16$, $e(X)=-4$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&2&&0&\\0&&5&&5&&0\\&0&&2&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 6; full even rank: 6; full odd rank: 10 ($h^{1,2}=5$).

$$
\begin{aligned}\int_X c_1^3&=16,&\int_X c_1 c_2&=24,\\\int_X c_3&=-4,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, -1, 0, 0], [0, 0, 0, -1, -1], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]]
cones = [[0, 2, 3, 4, 6], [1, 3, 4, 5, 6], [0, 2, 3, 5, 6], [0, 1, 3, 4, 6], [1, 2, 4, 5, 6], [0, 1, 2, 4, 5], [2, 3, 4, 5, 6], [0, 1, 3, 4, 5], [0, 1, 3, 5, 6], [0, 1, 2, 4, 6], [0, 1, 2, 5, 6], [0, 2, 3, 4, 5]]
K = [[0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 0, 2]]
novikov_divisors = [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:**

```python
['1', 'x1', 'x0', 'x1^2', 'x0^2', 'x0^3']
```

Curve enumeration: positive; 13 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x1', 'x0', 'x1^2', 'x0^2', 'x0^3']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $20 y_{1} y_{2}$ |
| 0 | 2 | $4 y_{1}^{2} + 20 y_{1} y_{2}$ |
| 0 | 3 | $48 y_{1}^{2} y_{2} + 24 y_{1} y_{2}^{2}$ |
| 0 | 4 | $114 y_{1}^{2} y_{2} + 21 y_{1} y_{2}^{2}$ |
| 0 | 5 | $64 y_{1}^{3} y_{2} + 120 y_{1}^{2} y_{2}^{2} + 4 y_{1} y_{2}^{3}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{2}$ |
| 1 | 2 | $5 y_{1}$ |
| 1 | 3 | $12 y_{1} y_{2}$ |
| 1 | 4 | $6 y_{1}^{2} + 12 y_{1} y_{2}$ |
| 1 | 5 | $30 y_{1}^{2} y_{2} + 3 y_{1} y_{2}^{2}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $3 y_{2}$ |
| 2 | 3 | $16 y_{1} y_{2}$ |
| 2 | 4 | $26 y_{1} y_{2}$ |
| 2 | 5 | $24 y_{1}^{2} y_{2} + 12 y_{1} y_{2}^{2}$ |
| 3 | 1 | $\frac{13}{6}$ |
| 3 | 2 | $\frac{7}{6}$ |
| 3 | 3 | $- y_{2}$ |
| 3 | 4 | $\frac{15 y_{1}}{2}$ |
| 3 | 5 | $2 y_{1}^{2} + \frac{20 y_{1} y_{2}}{3}$ |
| 4 | 1 | $\frac{2}{3}$ |
| 4 | 2 | $\frac{5}{3}$ |
| 4 | 3 | $2 y_{2}$ |
| 4 | 5 | $\frac{20 y_{1} y_{2}}{3}$ |
| 5 | 3 | $2$ |
| 5 | 4 | $4$ |
