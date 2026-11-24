---
title: "Fanography 3-26"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 3-26."
keywords: ["Fanography 3-26", "Fano variety 3-26", "dimension 3", "threefold", "Fano threefold", "Fanography", "Smooth projective toric threefold", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "smooth toric ambient", "regularized exponent multiset"]
---

# Fanography 3-26 — smooth projective toric threefold

**Geometric presentation.** Smooth projective toric threefold given directly by its complete smooth fan of Picard rank 3.

**Fanography family:** [3-26](https://fanography.info/3-26/) — Blowup of [1-17](https://fanography.info/1-17/) in the disjoint union of a point and a line. [Fano variety 3-26 reference card](../fanography.md#fano-variety-3-26) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Smooth projective toric threefold. **Dimension:** 3. **Index:** 1. **h(1,1):** 3.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{8} + 16 z^{7} - 108 z^{6} - 3372 z^{5} - 19548 z^{4} - 117000 z^{3} - 1886220 z^{2} - 13336920 z - 26238060\) | 8 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1067951073103814800512\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{8} + 16 \lambda^{7} - 108 \lambda^{6} - 3372 \lambda^{5} - 19548 \lambda^{4} - 117000 \lambda^{3} - 1886220 \lambda^{2} - 13336920 \lambda - 26238060=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-3-26). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** smooth toric Fano ambient (no defining bundle twist).
$\dim X=3$, $\dim Y=3$, codimension $0$, recorded index $1$, $(-K_X)^3=46$, $e(X)=8$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&3&&0&\\0&&0&&0&&0\\&0&&3&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 8; full even rank: 8; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=46,&\int_X c_1 c_2&=24,\\\int_X c_3&=8,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, -1], [-1, -1, 0], [0, 0, -1], [0, 0, 1], [0, 1, 0], [1, 0, 0]]
cones = [[1, 3, 5], [1, 3, 4], [2, 4, 5], [0, 1, 4], [0, 1, 5], [3, 4, 5], [0, 2, 5], [0, 2, 4]]
K = []
novikov_divisors = [[0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5}
```

**Ordered ambient basis:**

```python
['1', 'x2', 'x1', 'x0', 'x1^2', 'x0*x2', 'x0*x1', 'x0^2*x2']
```

Curve enumeration: positive; 22 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x2', 'x1', 'x0', 'x1^2', 'x0*x2', 'x0*x1', 'x0^2*x2']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $2 y_{2} y_{3}$ |
| 0 | 4 | $3 y_{1} y_{3}$ |
| 0 | 7 | $4 y_{1} y_{2} y_{3}$ |
| 1 | 0 | $2$ |
| 1 | 5 | $- 2 y_{1}$ |
| 1 | 7 | $3 y_{1} y_{3}$ |
| 2 | 0 | $3$ |
| 2 | 2 | $- y_{2}$ |
| 2 | 3 | $y_{2}$ |
| 2 | 4 | $- 2 y_{2} y_{3}$ |
| 2 | 5 | $2 y_{2} y_{3}$ |
| 2 | 6 | $2 y_{2} y_{3}$ |
| 3 | 0 | $4$ |
| 3 | 1 | $y_{3}$ |
| 3 | 2 | $y_{3}$ |
| 3 | 3 | $- y_{3}$ |
| 3 | 4 | $- 2 y_{2} y_{3}$ |
| 3 | 5 | $2 y_{2} y_{3}$ |
| 3 | 6 | $2 y_{2} y_{3}$ |
| 3 | 7 | $3 y_{1} y_{3}$ |
| 4 | 2 | $3$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 6 | $y_{2}$ |
| 4 | 7 | $2 y_{2} y_{3}$ |
| 5 | 1 | $2$ |
| 5 | 3 | $-2$ |
| 5 | 4 | $- y_{3}$ |
| 5 | 5 | $- y_{3}$ |
| 5 | 7 | $- 2 y_{2} y_{3}$ |
| 6 | 2 | $4$ |
| 6 | 3 | $3$ |
| 6 | 4 | $- 2 y_{2} + y_{3}$ |
| 6 | 5 | $y_{3}$ |
| 6 | 6 | $y_{2}$ |
| 6 | 7 | $4 y_{2} y_{3}$ |
| 7 | 4 | $-2$ |
| 7 | 5 | $2$ |
| 7 | 6 | $3$ |
