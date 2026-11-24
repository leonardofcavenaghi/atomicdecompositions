---
title: "Fanography 2-23"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 2-23."
keywords: ["Fanography 2-23", "Fano variety 2-23", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 2", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "split projective bundle", "regularized exponent multiset"]
---

# Fanography 2-23 — section of \(\mathbb P_{\mathbb P^{4}}(\mathcal O\oplus \mathcal O(1))\)

**Geometric presentation.** Ambient variety: \(\mathbb P_{\mathbb P^{4}}(\mathcal O\oplus \mathcal O(1))\), in the quotient convention. With \(H\) the pullback of the base hyperplane class and \(\xi=c_1(\mathcal O(1))\), the defining divisors are \(\xi + H\), \(2H\).

**Fanography family:** [2-23](https://fanography.info/2-23/) — Blowup of [1-16](https://fanography.info/1-16/) in an intersection of $A\in|\mathcal{O}_Q(1)|$ and $B\in|\mathcal{O}_Q(2)|$ such that $A$ is smooth; blowup of [1-16](https://fanography.info/1-16/) in an intersection of $A\in|\mathcal{O}_Q(1)|$ and $B\in|\mathcal{O}_Q(2)|$ such that $A$ is singular. [Fano variety 2-23 reference card](../fanography.md#fano-variety-2-23) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 2. **Dimension:** 3. **Index:** 1. **h(1,1):** 2.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 3\) | 1 | 2 |
| \(z\) | 1 | 1 |
| \(z - 22\) | 1 | 1 |
| \(z^{2} + 30 z + 228\) | 2 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 3=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
| \(\lambda=0\) | \(\{\!\{0\}\!\}\) |
| \(\lambda - 22=0\) | \(\{\!\{0\}\!\}\) |
| \(\lambda^{2} + 30 \lambda + 228=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-2-23). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=5$, codimension $2$, recorded index $1$, $(-K_X)^3=30$, $e(X)=4$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&2&&0&\\0&&1&&1&&0\\&0&&2&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 6; full even rank: 6; full odd rank: 2 ($h^{1,2}=1$).

$$
\begin{aligned}\int_X c_1^3&=30,&\int_X c_1 c_2&=24,\\\int_X c_3&=4,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, -1, -1, -1], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
cones = [[0, 2, 3, 4, 5], [1, 2, 3, 5, 6], [0, 1, 3, 4, 5], [1, 2, 4, 5, 6], [0, 1, 2, 3, 5], [1, 3, 4, 5, 6], [0, 1, 2, 3, 4], [0, 1, 2, 4, 5], [1, 2, 3, 4, 6], [2, 3, 4, 5, 6]]
K = [[0, 0, 0, 0, 0, 2, 1], [0, 0, 0, 0, 0, 2, 0]]
novikov_divisors = [[0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:**

```python
['1', 'x1', 'x0', 'x1^2', 'x0*x1', 'x1^3']
```

Curve enumeration: positive; 10 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x1', 'x0', 'x1^2', 'x0*x1', 'x1^3']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $8 y_{1} y_{2}$ |
| 0 | 2 | $8 y_{1} y_{2}$ |
| 0 | 3 | $6 y_{1} y_{2}^{2}$ |
| 0 | 4 | $12 y_{1} y_{2}^{2}$ |
| 0 | 5 | $16 y_{1}^{2} y_{2}^{2}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- 2 y_{1}$ |
| 1 | 2 | $2 y_{2}$ |
| 1 | 3 | $4 y_{1}^{2} + 8 y_{1} y_{2}$ |
| 1 | 4 | $8 y_{1} y_{2}$ |
| 1 | 5 | $6 y_{1} y_{2}^{2}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $2 y_{1}$ |
| 2 | 2 | $- y_{2}$ |
| 2 | 3 | $- 4 y_{1}^{2} + 4 y_{1} y_{2}$ |
| 2 | 4 | $8 y_{1} y_{2}$ |
| 3 | 1 | $1$ |
| 3 | 3 | $- 2 y_{1}$ |
| 3 | 4 | $2 y_{2}$ |
| 4 | 1 | $1$ |
| 4 | 2 | $2$ |
| 4 | 3 | $2 y_{1}$ |
| 4 | 4 | $- y_{2}$ |
| 4 | 5 | $4 y_{1} y_{2}$ |
| 5 | 3 | $3$ |
| 5 | 4 | $4$ |
