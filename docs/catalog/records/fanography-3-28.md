---
title: "Fanography 3-28"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 3-28."
keywords: ["Fanography 3-28", "Fano variety 3-28", "dimension 3", "threefold", "Fano threefold", "Fanography", "Smooth projective toric threefold", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "split projective bundle over product", "regularized exponent multiset"]
---

# Fanography 3-28 — \(\mathbb P_{\mathbb P^{1}\times \mathbb P^{1}}(\mathcal O\oplus \mathcal O(0,1))\)

**Geometric presentation.** Smooth projective bundle \(\mathbb P_{\mathbb P^{1}\times \mathbb P^{1}}(\mathcal O\oplus \mathcal O(0,1))\) in the quotient convention.

**Fanography family:** [3-28](https://fanography.info/3-28/) — $\mathbb{P}^1\times\mathrm{Bl}_p\mathbb{P}^2$. [Fano variety 3-28 reference card](../fanography.md#fano-variety-3-28) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Smooth projective toric threefold. **Dimension:** 3. **Index:** 1. **h(1,1):** 3.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{8} + 6 z^{7} - 103 z^{6} - 1464 z^{5} - 2462 z^{4} + 26022 z^{3} + 257760 z^{2} + 606168 z - 983007\) | 8 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=54525723630325859376\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{8} + 6 \lambda^{7} - 103 \lambda^{6} - 1464 \lambda^{5} - 2462 \lambda^{4} + 26022 \lambda^{3} + 257760 \lambda^{2} + 606168 \lambda - 983007=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-3-28). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** smooth toric Fano ambient (no defining bundle twist).
$\dim X=3$, $\dim Y=3$, codimension $0$, recorded index $1$, $(-K_X)^3=48$, $e(X)=8$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&3&&0&\\0&&0&&0&&0\\&0&&3&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 8; full even rank: 8; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=48,&\int_X c_1 c_2&=24,\\\int_X c_3&=8,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, 0, 0], [0, -1, -1], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0]]
cones = [[1, 3, 5], [3, 4, 5], [0, 1, 3], [0, 1, 2], [1, 2, 5], [2, 4, 5], [0, 2, 4], [0, 3, 4]]
K = []
novikov_divisors = [[1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5}
```

**Ordered ambient basis:**

```python
['1', 'x2', 'x1', 'x0', 'x1*x2', 'x0*x2', 'x0*x1', 'x0*x1*x2']
```

Curve enumeration: positive; 14 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x2', 'x1', 'x0', 'x1*x2', 'x0*x2', 'x0*x1', 'x0*x1*x2']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 2 | $2 y_{3}$ |
| 0 | 3 | $2 y_{1}$ |
| 0 | 4 | $3 y_{2} y_{3}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{2}$ |
| 1 | 4 | $2 y_{3}$ |
| 1 | 5 | $2 y_{1}$ |
| 2 | 0 | $2$ |
| 2 | 1 | $y_{2}$ |
| 2 | 6 | $2 y_{1}$ |
| 3 | 0 | $2$ |
| 3 | 6 | $2 y_{3}$ |
| 3 | 7 | $3 y_{2} y_{3}$ |
| 4 | 1 | $2$ |
| 4 | 2 | $3$ |
| 4 | 7 | $2 y_{1}$ |
| 5 | 1 | $2$ |
| 5 | 3 | $1$ |
| 5 | 5 | $- y_{2}$ |
| 5 | 7 | $2 y_{3}$ |
| 6 | 2 | $2$ |
| 6 | 3 | $2$ |
| 6 | 5 | $y_{2}$ |
| 7 | 4 | $2$ |
| 7 | 5 | $2$ |
| 7 | 6 | $3$ |
