---
title: "Fanography 3-9"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 3-9."
keywords: ["Fanography 3-9", "Fano variety 3-9", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "split projective bundle", "regularized exponent multiset"]
---

# Fanography 3-9 — section of \(\mathbb P_{\mathbb P^{2}}(\mathcal O^{\oplus 2}\oplus \mathcal O(2))\)

**Geometric presentation.** Ambient variety: \(\mathbb P_{\mathbb P^{2}}(\mathcal O^{\oplus 2}\oplus \mathcal O(2))\), in the quotient convention. With \(H\) the pullback of the base hyperplane class and \(\xi=c_1(\mathcal O(1))\), the defining divisors are \(2\xi\).

**Fanography family:** [3-9](https://fanography.info/3-9/) — Blowup of the cone over the Veronese of $\mathbb{P}^2$ in $\mathbb{P}^5$ with center the disjoint union of the vertex and a quartic curve on $\mathbb{P}^2$. [Fano variety 3-9 reference card](../fanography.md#fano-variety-3-9) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 1. **Dimension:** 3. **Index:** 1. **h(1,1):** 3.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 6\) | 1 | 2 |
| \(z - 2\) | 1 | 1 |
| \(z^{3} - 18 z^{2} + 108 z - 7992\) | 3 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-1185528960\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 6=0\) | \(\{\!\{\frac{1}{4},\frac{3}{4}\}\!\}\) |
| \(\lambda - 2=0\) | \(\{\!\{0\}\!\}\) |
| \(\lambda^{3} - 18 \lambda^{2} + 108 \lambda - 7992=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-3-9). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=4$, codimension $1$, recorded index $1$, $(-K_X)^3=26$, $e(X)=2$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&3&&0&\\0&&3&&3&&0\\&0&&3&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 6; full even rank: 8; full odd rank: 6 ($h^{1,2}=3$).

$$
\begin{aligned}\int_X c_1^3&=26,&\int_X c_1 c_2&=24,\\\int_X c_3&=2,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, 2, 0], [0, 0, -1, -1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
cones = [[0, 2, 3, 4], [0, 1, 2, 5], [2, 3, 4, 5], [1, 3, 4, 5], [0, 1, 3, 5], [0, 1, 3, 4], [1, 2, 4, 5], [0, 2, 3, 5], [0, 1, 2, 4]]
K = [[0, 0, 0, 2, 0, 4]]
novikov_divisors = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:**

```python
['1', 'x1', 'x0', 'x1^2', 'x0^2', 'x0*x1^2']
```

Curve enumeration: positive; 9 classes including zero.

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
| 0 | 1 | $4 y_{2}^{2}$ |
| 0 | 3 | $72 y_{1} y_{2}^{2}$ |
| 0 | 4 | $24 y_{1} y_{2}^{2}$ |
| 0 | 5 | $128 y_{1} y_{2}^{3}$ |
| 1 | 0 | $1$ |
| 1 | 2 | $- y_{1}$ |
| 1 | 3 | $16 y_{1} y_{2}$ |
| 1 | 4 | $- 2 y_{1}^{2} + 8 y_{1} y_{2}$ |
| 1 | 5 | $48 y_{1} y_{2}^{2}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $4 y_{2}$ |
| 2 | 2 | $2 y_{1}$ |
| 2 | 3 | $- 32 y_{1} y_{2} + 8 y_{2}^{2}$ |
| 2 | 4 | $4 y_{1}^{2} - 8 y_{1} y_{2}$ |
| 2 | 5 | $- 24 y_{1} y_{2}^{2}$ |
| 3 | 1 | $\frac{3}{2}$ |
| 3 | 2 | $\frac{1}{2}$ |
| 3 | 4 | $- \frac{y_{1}}{2}$ |
| 4 | 2 | $1$ |
| 4 | 3 | $8 y_{2}$ |
| 4 | 4 | $2 y_{1}$ |
| 4 | 5 | $8 y_{2}^{2}$ |
| 5 | 3 | $3$ |
| 5 | 4 | $\frac{1}{2}$ |
