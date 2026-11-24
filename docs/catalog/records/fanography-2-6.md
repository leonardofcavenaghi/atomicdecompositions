---
title: "Fanography 2-6"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 2-6."
keywords: ["Fanography 2-6", "Fano variety 2-6", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "product of projective spaces", "regularized exponent multiset"]
---

# Fanography 2-6 — complete intersection in \(\mathbb P^{2}\times \mathbb P^{2}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{2}\times \mathbb P^{2}\). Defining multidegrees in this factor order: `[[2, 2]]`.

**Fanography family:** [2-6](https://fanography.info/2-6/) — $(2,2)$-divisor on $\mathbb{P}^2\times\mathbb{P}^2$; double cover of [2-32](https://fanography.info/2-32/) with branch locus an anticanonical divisor. [Fano variety 2-6 reference card](../fanography.md#fano-variety-2-6) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 1. **Dimension:** 3. **Index:** 1. **h(1,1):** 2.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 10\) | 1 | 3 |
| \(z^{3} - 30 z^{2} - 2292 z - 26920\) | 3 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 10=0\) | \(\{\!\{0,0,0\}\!\}\) |
| \(\lambda^{3} - 30 \lambda^{2} - 2292 \lambda - 26920=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-2-6). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=4$, codimension $1$, recorded index $1$, $(-K_X)^3=12$, $e(X)=-12$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&2&&0&\\0&&9&&9&&0\\&0&&2&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 6; full even rank: 6; full odd rank: 18 ($h^{1,2}=9$).

$$
\begin{aligned}\int_X c_1^3&=12,&\int_X c_1 c_2&=24,\\\int_X c_3&=-12,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, 0, 0], [0, 0, -1, -1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
cones = [[0, 2, 3, 4], [0, 1, 2, 5], [2, 3, 4, 5], [1, 3, 4, 5], [0, 1, 3, 5], [0, 1, 3, 4], [1, 2, 4, 5], [0, 2, 3, 5], [0, 1, 2, 4]]
K = [[0, 0, 0, 2, 0, 2]]
novikov_divisors = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:**

```python
['1', 'x1', 'x0', 'x1^2', 'x0^2', 'x0*x1^2']
```

Curve enumeration: positive; 13 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x1', 'x0', 'x1^2', 'x0^2', 'x0*x1^2']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $40 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 0 | 2 | $4 y_{1}^{2} + 40 y_{1} y_{2}$ |
| 0 | 3 | $96 y_{1}^{2} y_{2} + 168 y_{1} y_{2}^{2}$ |
| 0 | 4 | $168 y_{1}^{2} y_{2} + 96 y_{1} y_{2}^{2}$ |
| 0 | 5 | $256 y_{1}^{3} y_{2} + 1376 y_{1}^{2} y_{2}^{2} + 256 y_{1} y_{2}^{3}$ |
| 1 | 0 | $1$ |
| 1 | 2 | $6 y_{1}$ |
| 1 | 3 | $40 y_{1} y_{2}$ |
| 1 | 4 | $4 y_{1}^{2} + 32 y_{1} y_{2}$ |
| 1 | 5 | $168 y_{1}^{2} y_{2} + 96 y_{1} y_{2}^{2}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $6 y_{2}$ |
| 2 | 3 | $32 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 2 | 4 | $40 y_{1} y_{2}$ |
| 2 | 5 | $96 y_{1}^{2} y_{2} + 168 y_{1} y_{2}^{2}$ |
| 3 | 1 | $2$ |
| 3 | 2 | $1$ |
| 3 | 4 | $6 y_{1}$ |
| 3 | 5 | $4 y_{1}^{2} + 40 y_{1} y_{2}$ |
| 4 | 1 | $1$ |
| 4 | 2 | $2$ |
| 4 | 3 | $6 y_{2}$ |
| 4 | 5 | $40 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 5 | 3 | $1$ |
| 5 | 4 | $1$ |
