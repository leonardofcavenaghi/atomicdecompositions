---
title: "Fanography 2-36"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 2-36."
keywords: ["Fanography 2-36", "Fano variety 2-36", "dimension 3", "threefold", "Fano threefold", "Fanography", "Smooth projective toric threefold", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "split projective bundle", "regularized exponent multiset"]
---

# Fanography 2-36 — \(\mathbb P_{\mathbb P^{2}}(\mathcal O\oplus \mathcal O(2))\)

**Geometric presentation.** Smooth projective bundle \(\mathbb P_{\mathbb P^{2}}(\mathcal O\oplus \mathcal O(2))\) in the quotient convention.

**Fanography family:** [2-36](https://fanography.info/2-36/) — $\mathbb{P}(\mathcal{O}_{\mathbb{P}^2}\oplus\mathcal{O}_{\mathbb{P}^2}(2))$. [Fano variety 2-36 reference card](../fanography.md#fano-variety-2-36) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Smooth projective toric threefold. **Dimension:** 3. **Index:** 1. **h(1,1):** 2.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{6} - 8 z^{5} - 36 z^{4} + 300 z^{3} + 432 z^{2} - 18000 z + 110772\) | 6 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-74727456\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{6} - 8 \lambda^{5} - 36 \lambda^{4} + 300 \lambda^{3} + 432 \lambda^{2} - 18000 \lambda + 110772=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-2-36). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** smooth toric Fano ambient (no defining bundle twist).
$\dim X=3$, $\dim Y=3$, codimension $0$, recorded index $1$, $(-K_X)^3=62$, $e(X)=6$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&2&&0&\\0&&0&&0&&0\\&0&&2&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 6; full even rank: 6; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=62,&\int_X c_1 c_2&=24,\\\int_X c_3&=6,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, 2], [0, 0, -1], [0, 0, 1], [0, 1, 0], [1, 0, 0]]
cones = [[0, 1, 4], [0, 2, 3], [1, 3, 4], [2, 3, 4], [0, 1, 3], [0, 2, 4]]
K = []
novikov_divisors = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:**

```python
['1', 'x1', 'x0', 'x0^2', 'x0*x1', 'x0^2*x1']
```

Curve enumeration: positive; 9 classes including zero.

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
| 0 | 3 | $3 y_{1} y_{2}$ |
| 1 | 0 | $2$ |
| 1 | 2 | $- y_{1}$ |
| 1 | 3 | $- 2 y_{1}^{2}$ |
| 1 | 5 | $3 y_{1} y_{2}$ |
| 2 | 0 | $1$ |
| 2 | 2 | $2 y_{1}$ |
| 2 | 3 | $4 y_{1}^{2}$ |
| 2 | 4 | $2 y_{2}$ |
| 2 | 5 | $- 6 y_{1} y_{2}$ |
| 3 | 2 | $1$ |
| 3 | 3 | $2 y_{1}$ |
| 3 | 5 | $2 y_{2}$ |
| 4 | 1 | $5$ |
| 4 | 2 | $2$ |
| 4 | 3 | $- y_{1}$ |
| 5 | 3 | $2$ |
| 5 | 4 | $5$ |
