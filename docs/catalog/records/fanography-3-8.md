---
title: "Fanography 3-8"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 3-8."
keywords: ["Fanography 3-8", "Fano variety 3-8", "dimension 3", "threefold", "Fano threefold", "Fanography", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "split projective bundle over product", "regularized exponent multiset"]
---

# Fanography 3-8 — section of \(\mathbb P_{\mathbb P^{1}\times \mathbb P^{2}}(\mathcal O\oplus \mathcal O(1,0))\)

**Geometric presentation.** Ambient variety: \(\mathbb P_{\mathbb P^{1}\times \mathbb P^{2}}(\mathcal O\oplus \mathcal O(1,0))\), in the quotient convention. Defining divisor coordinates in the base-and-\(\xi\) lattice basis: `[[0, 2, 1]]`.

**Fanography family:** [3-8](https://fanography.info/3-8/) — Divisor from the linear system $|(\alpha\circ\pi_1)^*(\mathcal{O}_{\mathbb{P}^2}(1)\otimes\pi_2^*(\mathcal{O}_{\mathbb{P}^2}(2))|$ where $\pi_i\colon\mathrm{Bl}_1\mathbb{P}^2\times\mathbb{P}^2\to\mathrm{Bl}_1\mathbb{P}^2,\mathbb{P}^2$ are the projections, and $\alpha\colon\mathrm{Bl}_1\mathbb{P}^2\to\mathbb{P}^2$ is the blowup. [Fano variety 3-8 reference card](../fanography.md#fano-variety-3-8) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 1. **Dimension:** 3. **Index:** 1. **h(1,1):** 3.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 15\) | 1 | 1 |
| \(z^{7} - 5 z^{6} - 1512 z^{5} - 22230 z^{4} + 292038 z^{3} + 10589460 z^{2} + 103089161 z + 352928735\) | 7 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-2831961718284652160064\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 15=0\) | \(\{\!\{0\}\!\}\) |
| \(\lambda^{7} - 5 \lambda^{6} - 1512 \lambda^{5} - 22230 \lambda^{4} + 292038 \lambda^{3} + 10589460 \lambda^{2} + 103089161 \lambda + 352928735=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-3-8). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef (globally generated) defining divisors and positive anticanonical degree on every torus-invariant wall.
$\dim X=3$, $\dim Y=4$, codimension $1$, recorded index $1$, $(-K_X)^3=24$, $e(X)=8$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&3&&0&\\0&&0&&0&&0\\&0&&3&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 8; full even rank: 8; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=24,&\int_X c_1 c_2&=24,\\\int_X c_3&=8,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, 0, 0], [0, 0, -1, -1], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]]
cones = [[0, 1, 2, 5], [1, 2, 5, 6], [1, 3, 5, 6], [0, 2, 3, 4], [1, 2, 4, 6], [0, 1, 3, 5], [2, 3, 4, 6], [0, 1, 2, 4], [0, 1, 3, 4], [2, 3, 5, 6], [0, 2, 3, 5], [1, 3, 4, 6]]
K = [[0, 0, 0, 2, 0, 1, 1]]
novikov_divisors = [[0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5}
```

**Ordered ambient basis:**

```python
['1', 'x4', 'x1', 'x0', 'x1^2', 'x1*x4', 'x0*x4', 'x1^2*x4']
```

Curve enumeration: positive; 18 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x4', 'x1', 'x0', 'x1^2', 'x1*x4', 'x0*x4', 'x1^2*x4']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $2 y_{1} y_{2}$ |
| 0 | 2 | $8 y_{2} y_{3} + 4 y_{3}^{2}$ |
| 0 | 3 | $2 y_{1} y_{2} + 8 y_{2} y_{3}$ |
| 0 | 4 | $3 y_{1} y_{2} y_{3} + 3 y_{2}^{2} y_{3} + 12 y_{2} y_{3}^{2}$ |
| 0 | 5 | $12 y_{1} y_{2} y_{3}$ |
| 0 | 6 | $12 y_{1} y_{2} y_{3}$ |
| 0 | 7 | $8 y_{1} y_{2}^{2} y_{3} + 16 y_{1} y_{2} y_{3}^{2}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{1}$ |
| 1 | 3 | $y_{2}$ |
| 1 | 4 | $2 y_{2} y_{3}$ |
| 1 | 5 | $8 y_{2} y_{3} + 4 y_{3}^{2}$ |
| 1 | 6 | $8 y_{2} y_{3}$ |
| 1 | 7 | $3 y_{2}^{2} y_{3} + 12 y_{2} y_{3}^{2}$ |
| 2 | 0 | $1$ |
| 2 | 3 | $2 y_{2}$ |
| 2 | 4 | $4 y_{2} y_{3}$ |
| 2 | 5 | $2 y_{1} y_{2}$ |
| 2 | 6 | $4 y_{1} y_{2}$ |
| 2 | 7 | $6 y_{1} y_{2} y_{3}$ |
| 3 | 0 | $1$ |
| 3 | 1 | $y_{1}$ |
| 3 | 2 | $3 y_{3}$ |
| 3 | 3 | $- y_{2}$ |
| 3 | 4 | $2 y_{2} y_{3} + 2 y_{3}^{2}$ |
| 3 | 7 | $3 y_{1} y_{2} y_{3}$ |
| 4 | 2 | $3$ |
| 4 | 3 | $2$ |
| 4 | 5 | $2 y_{1}$ |
| 4 | 7 | $2 y_{1} y_{2}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $1$ |
| 5 | 5 | $- y_{1}$ |
| 5 | 6 | $2 y_{2}$ |
| 5 | 7 | $4 y_{2} y_{3}$ |
| 6 | 1 | $1$ |
| 6 | 2 | $\frac{1}{2}$ |
| 6 | 3 | $\frac{5}{2}$ |
| 6 | 4 | $\frac{3 y_{3}}{2}$ |
| 6 | 5 | $\frac{y_{1}}{2} + 3 y_{3}$ |
| 6 | 6 | $- y_{2}$ |
| 6 | 7 | $2 y_{2} y_{3} + 2 y_{3}^{2}$ |
| 7 | 4 | $2$ |
| 7 | 5 | $3$ |
| 7 | 6 | $2$ |
