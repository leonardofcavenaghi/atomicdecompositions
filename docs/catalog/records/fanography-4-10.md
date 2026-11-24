---
title: "Fanography 4-10"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 4-10."
keywords: ["Fanography 4-10", "Fano variety 4-10", "dimension 3", "threefold", "Fano threefold", "Fanography", "Smooth projective toric threefold", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "smooth toric ambient", "regularized exponent multiset"]
---

# Fanography 4-10 — smooth projective toric threefold

**Geometric presentation.** Smooth projective toric threefold given directly by its complete smooth fan of Picard rank 4.

**Fanography family:** [4-10](https://fanography.info/4-10/) — $\mathbb{P}^1\times\mathrm{Bl}_2\mathbb{P}^2$. [Fano variety 4-10 reference card](../fanography.md#fano-variety-4-10) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Smooth projective toric threefold. **Dimension:** 3. **Index:** 1. **h(1,1):** 4.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5, y4=7`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{10} + 24 z^{9} - 504 z^{8} - 17736 z^{7} - 53772 z^{6} + 2392392 z^{5} + 24735328 z^{4} + 43909008 z^{3} - 347018784 z^{2} - 1116525312 z + 318569616\) | 10 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-73574033641854087239811314192351232\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{10} + 24 \lambda^{9} - 504 \lambda^{8} - 17736 \lambda^{7} - 53772 \lambda^{6} + 2392392 \lambda^{5} + 24735328 \lambda^{4} + 43909008 \lambda^{3} - 347018784 \lambda^{2} - 1116525312 \lambda + 318569616=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-4-10). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** smooth toric Fano ambient (no defining bundle twist).
$\dim X=3$, $\dim Y=3$, codimension $0$, recorded index $1$, $(-K_X)^3=42$, $e(X)=10$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&4&&0&\\0&&0&&0&&0\\&0&&4&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 10; full even rank: 10; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=42,&\int_X c_1 c_2&=24,\\\int_X c_3&=10,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, 0], [-1, 0, 0], [0, -1, 0], [0, 0, -1], [0, 0, 1], [0, 1, 0], [1, 0, 0]]
cones = [[0, 2, 4], [0, 1, 3], [1, 3, 5], [2, 3, 6], [0, 2, 3], [4, 5, 6], [3, 5, 6], [1, 4, 5], [2, 4, 6], [0, 1, 4]]
K = []
novikov_divisors = [[0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5, 'y4': 7}
```

**Ordered ambient basis:**

```python
['1', 'x3', 'x2', 'x1', 'x0', 'x2*x3', 'x1*x3', 'x0*x3', 'x0*x1', 'x0*x1*x3']
```

Curve enumeration: positive; 46 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x3', 'x2', 'x1', 'x0', 'x2*x3', 'x1*x3', 'x0*x3', 'x0*x1', 'x0*x1*x3']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $2 y_{3}$ |
| 0 | 2 | $2 y_{2} y_{4}$ |
| 0 | 3 | $2 y_{1} y_{4}$ |
| 0 | 8 | $3 y_{1} y_{2} y_{4}$ |
| 1 | 0 | $2$ |
| 1 | 5 | $2 y_{2} y_{4}$ |
| 1 | 6 | $2 y_{1} y_{4}$ |
| 1 | 9 | $3 y_{1} y_{2} y_{4}$ |
| 2 | 0 | $2$ |
| 2 | 2 | $- y_{1}$ |
| 2 | 4 | $y_{1}$ |
| 2 | 5 | $2 y_{3}$ |
| 2 | 8 | $2 y_{1} y_{4}$ |
| 3 | 0 | $2$ |
| 3 | 3 | $- y_{2}$ |
| 3 | 4 | $y_{2}$ |
| 3 | 6 | $2 y_{3}$ |
| 3 | 8 | $2 y_{2} y_{4}$ |
| 4 | 0 | $3$ |
| 4 | 2 | $y_{4}$ |
| 4 | 3 | $y_{4}$ |
| 4 | 4 | $- y_{4}$ |
| 4 | 7 | $2 y_{3}$ |
| 4 | 8 | $2 y_{1} y_{4} + 2 y_{2} y_{4}$ |
| 5 | 1 | $2$ |
| 5 | 2 | $2$ |
| 5 | 5 | $- y_{1}$ |
| 5 | 7 | $y_{1}$ |
| 5 | 9 | $2 y_{1} y_{4}$ |
| 6 | 1 | $2$ |
| 6 | 3 | $2$ |
| 6 | 6 | $- y_{2}$ |
| 6 | 7 | $y_{2}$ |
| 6 | 9 | $2 y_{2} y_{4}$ |
| 7 | 1 | $3$ |
| 7 | 4 | $2$ |
| 7 | 5 | $y_{4}$ |
| 7 | 6 | $y_{4}$ |
| 7 | 7 | $- y_{4}$ |
| 7 | 9 | $2 y_{1} y_{4} + 2 y_{2} y_{4}$ |
| 8 | 2 | $1$ |
| 8 | 3 | $1$ |
| 8 | 4 | $1$ |
| 8 | 9 | $2 y_{3}$ |
| 9 | 5 | $1$ |
| 9 | 6 | $1$ |
| 9 | 7 | $1$ |
| 9 | 8 | $2$ |
