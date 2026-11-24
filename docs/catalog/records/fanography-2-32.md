---
title: "Fanography 2-32 (toric divisor in P² × P²)"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 2-32 (toric divisor in P² × P²)."
keywords: ["Fanography 2-32", "Fano variety 2-32", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "product of projective spaces", "regularized exponent multiset"]
---

# Fanography 2-32 — complete intersection in \(\mathbb P^{2}\times \mathbb P^{2}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{2}\times \mathbb P^{2}\). Defining multidegrees in this factor order: `[[1, 1]]`.

**Fanography family:** [2-32](https://fanography.info/2-32/) — Divisor on $\mathbb{P}^2\times\mathbb{P}^2$ of bidegree $(1,1)$. [Fano variety 2-32 reference card](../fanography.md#fano-variety-2-32) · [Geometric identification](../sources.md#geometric-identification).
See also the direct homogeneous presentation [Fanography 2-32](../fanography.md#fano-variety-2-32) (realized as \(\mathrm{Fl}(1,2;\mathbb C^3)\) in `gwflags`).
**Construction:** Complete intersection of codimension 1. **Dimension:** 3. **Index:** 2. **h(1,1):** 2.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{6} - 60 z^{4} - 1392 z^{2} - 8000\) | 6 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-119439360\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{6} - 60 \lambda^{4} - 1392 \lambda^{2} - 8000=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-2-32). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=4$, codimension $1$, recorded index $2$, $(-K_X)^3=48$, $e(X)=6$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&2&&0&\\0&&0&&0&&0\\&0&&2&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 6; full even rank: 6; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=48,&\int_X c_1 c_2&=24,\\\int_X c_3&=6,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, 0, 0], [0, 0, -1, -1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
cones = [[0, 2, 3, 4], [0, 1, 2, 5], [2, 3, 4, 5], [1, 3, 4, 5], [0, 1, 3, 5], [0, 1, 3, 4], [1, 2, 4, 5], [0, 2, 3, 5], [0, 1, 2, 4]]
K = [[0, 0, 0, 1, 0, 1]]
novikov_divisors = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:**

```python
['1', 'x1', 'x0', 'x1^2', 'x0^2', 'x0*x1^2']
```

Curve enumeration: positive; 4 classes including zero.

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
| 0 | 1 | $2 y_{2}$ |
| 0 | 2 | $2 y_{1}$ |
| 0 | 5 | $4 y_{1} y_{2}$ |
| 1 | 0 | $2$ |
| 1 | 4 | $2 y_{1}$ |
| 2 | 0 | $2$ |
| 2 | 3 | $2 y_{2}$ |
| 3 | 1 | $4$ |
| 3 | 2 | $2$ |
| 3 | 5 | $2 y_{1}$ |
| 4 | 1 | $2$ |
| 4 | 2 | $4$ |
| 4 | 5 | $2 y_{2}$ |
| 5 | 3 | $2$ |
| 5 | 4 | $2$ |
