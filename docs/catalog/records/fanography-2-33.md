---
title: "Fanography 2-33"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 2-33."
keywords: ["Fanography 2-33", "Fano variety 2-33", "dimension 3", "threefold", "Fano threefold", "Fanography", "Smooth projective toric threefold", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "split projective bundle", "regularized exponent multiset"]
---

# Fanography 2-33 — \(\mathbb P_{\mathbb P^{1}}(\mathcal O^{\oplus 2}\oplus \mathcal O(1))\)

**Geometric presentation.** Smooth projective bundle \(\mathbb P_{\mathbb P^{1}}(\mathcal O^{\oplus 2}\oplus \mathcal O(1))\) in the quotient convention.

**Fanography family:** [2-33](https://fanography.info/2-33/) — Blowup of [1-17](https://fanography.info/1-17/) in a line. [Fano variety 2-33 reference card](../fanography.md#fano-variety-2-33) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Smooth projective toric threefold. **Dimension:** 3. **Index:** 1. **h(1,1):** 2.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{6} + 4 z^{5} + 4 z^{4} - 162 z^{3} - 2268 z^{2} - 6912 z + 417\) | 6 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=964221464\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{6} + 4 \lambda^{5} + 4 \lambda^{4} - 162 \lambda^{3} - 2268 \lambda^{2} - 6912 \lambda + 417=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-2-33). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** smooth toric Fano ambient (no defining bundle twist).
$\dim X=3$, $\dim Y=3$, codimension $0$, recorded index $1$, $(-K_X)^3=54$, $e(X)=6$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&2&&0&\\0&&0&&0&&0\\&0&&2&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 6; full even rank: 6; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=54,&\int_X c_1 c_2&=24,\\\int_X c_3&=6,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, -1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 0]]
cones = [[0, 3, 4], [1, 2, 4], [0, 1, 3], [0, 1, 2], [0, 2, 4], [1, 3, 4]]
K = []
novikov_divisors = [[0, 0, 1, 0, 0], [1, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:**

```python
['1', 'x2', 'x0', 'x0^2', 'x0*x2', 'x0^2*x2']
```

Curve enumeration: positive; 7 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x2', 'x0', 'x0^2', 'x0*x2', 'x0^2*x2']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 3 | $3 y_{2}$ |
| 0 | 5 | $4 y_{1} y_{2}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{1}$ |
| 1 | 5 | $3 y_{2}$ |
| 2 | 0 | $3$ |
| 2 | 1 | $y_{1}$ |
| 3 | 2 | $3$ |
| 3 | 4 | $y_{1}$ |
| 4 | 1 | $3$ |
| 4 | 2 | $1$ |
| 4 | 4 | $- y_{1}$ |
| 5 | 3 | $4$ |
| 5 | 4 | $3$ |
