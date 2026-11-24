---
title: "Fanography 5-2"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 5-2."
keywords: ["Fanography 5-2", "Fano variety 5-2", "dimension 3", "threefold", "Fano threefold", "Fanography", "Smooth projective toric threefold", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "smooth toric ambient", "regularized exponent multiset"]
---

# Fanography 5-2 — smooth projective toric threefold

**Geometric presentation.** Smooth projective toric threefold given directly by its complete smooth fan of Picard rank 5.

**Fanography family:** [5-2](https://fanography.info/5-2/) — Blowup of [3-25](https://fanography.info/3-25/) in the disjoint union of two exceptional lines on the same irreducible component. [Fano variety 5-2 reference card](../fanography.md#fano-variety-5-2) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Smooth projective toric threefold. **Dimension:** 3. **Index:** 1. **h(1,1):** 5.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5, y4=7, y5=11`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{12} + 364 z^{11} + 41118 z^{10} - 1384196 z^{9} - 797972815 z^{8} - 78352910992 z^{7} - 1862448777768 z^{6} + 290528571988160 z^{5} + 33921468139947696 z^{4} + 1796179021770290432 z^{3} + 54769766287342513792 z^{2} + 935588553375882250240 z + 7039149454721760400640\) | 12 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-1786366422226903891094393566636555704129505168684884164481841287880706767630739611582464\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{12} + 364 \lambda^{11} + 41118 \lambda^{10} - 1384196 \lambda^{9} - 797972815 \lambda^{8} - 78352910992 \lambda^{7} - 1862448777768 \lambda^{6} + 290528571988160 \lambda^{5} + 33921468139947696 \lambda^{4} + 1796179021770290432 \lambda^{3} + 54769766287342513792 \lambda^{2} + 935588553375882250240 \lambda + 7039149454721760400640=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-5-2). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** smooth toric Fano ambient (no defining bundle twist).
$\dim X=3$, $\dim Y=3$, codimension $0$, recorded index $1$, $(-K_X)^3=36$, $e(X)=12$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&5&&0&\\0&&0&&0&&0\\&0&&5&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 12; full even rank: 12; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=36,&\int_X c_1 c_2&=24,\\\int_X c_3&=12,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, -1, -1], [-1, -1, 0], [-1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 0]]
cones = [[0, 6, 7], [4, 6, 7], [2, 4, 5], [3, 4, 6], [0, 2, 5], [1, 3, 4], [0, 3, 6], [0, 1, 2], [0, 1, 3], [0, 5, 7], [4, 5, 7], [1, 2, 4]]
K = []
novikov_divisors = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 1, 0, 0]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5, 'y4': 7, 'y5': 11}
```

**Ordered ambient basis:**

```python
['1', 'x5', 'x3', 'x2', 'x1', 'x0', 'x1*x2', 'x0*x5', 'x0*x3', 'x0*x2', 'x0*x1', 'x0*x1*x2']
```

Curve enumeration: positive; 238 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x5', 'x3', 'x2', 'x1', 'x0', 'x1*x2', 'x0*x5', 'x0*x3', 'x0*x2', 'x0*x1', 'x0*x1*x2']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $2 y_{3} y_{4} y_{5}$ |
| 0 | 2 | $2 y_{3} y_{4} y_{5}$ |
| 0 | 3 | $2 y_{2} y_{4} y_{5}$ |
| 0 | 4 | $2 y_{2} y_{3} y_{5}$ |
| 0 | 6 | $3 y_{2} y_{3} y_{4} y_{5}^{2} + 3 y_{2} y_{3} y_{4} y_{5}$ |
| 0 | 10 | $3 y_{1} y_{2} y_{3} y_{5}$ |
| 0 | 11 | $4 y_{1} y_{2} y_{3} y_{4} y_{5}^{2}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{2} - y_{4} y_{5}$ |
| 1 | 2 | $y_{3}$ |
| 1 | 3 | $y_{2}$ |
| 1 | 6 | $2 y_{2} y_{3} y_{5}$ |
| 1 | 11 | $3 y_{1} y_{2} y_{3} y_{5}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $y_{4} y_{5}$ |
| 2 | 2 | $- y_{2} y_{5} - y_{3}$ |
| 2 | 4 | $y_{2} y_{5}$ |
| 2 | 6 | $2 y_{2} y_{4} y_{5}$ |
| 2 | 8 | $- 2 y_{1} y_{2} y_{5}$ |
| 2 | 10 | $2 y_{1} y_{2} y_{5}$ |
| 3 | 0 | $2$ |
| 3 | 1 | $y_{3} y_{5}$ |
| 3 | 2 | $y_{3}$ |
| 3 | 3 | $- y_{3} y_{5}$ |
| 3 | 4 | $y_{3} y_{5}$ |
| 3 | 6 | $2 y_{2} y_{3} y_{5} + 2 y_{3} y_{4} y_{5}$ |
| 3 | 7 | $2 y_{1} y_{3} y_{5}$ |
| 3 | 9 | $- 2 y_{1} y_{3} y_{5}$ |
| 3 | 10 | $2 y_{1} y_{3} y_{5}$ |
| 3 | 11 | $3 y_{1} y_{2} y_{3} y_{5}$ |
| 4 | 0 | $2$ |
| 4 | 1 | $y_{4} y_{5}$ |
| 4 | 2 | $y_{4}$ |
| 4 | 3 | $y_{4}$ |
| 4 | 4 | $- y_{1} - y_{4}$ |
| 4 | 5 | $y_{1}$ |
| 4 | 6 | $2 y_{1} y_{4} + 2 y_{2} y_{4} y_{5} + 2 y_{3} y_{4} y_{5}$ |
| 4 | 8 | $- 2 y_{1} y_{4}$ |
| 4 | 9 | $- 2 y_{1} y_{4}$ |
| 4 | 10 | $2 y_{1} y_{4}$ |
| 5 | 0 | $3$ |
| 5 | 1 | $y_{4} y_{5}$ |
| 5 | 7 | $2 y_{3} y_{4} y_{5}$ |
| 5 | 8 | $2 y_{3} y_{4} y_{5}$ |
| 5 | 9 | $2 y_{2} y_{4} y_{5}$ |
| 5 | 10 | $2 y_{2} y_{3} y_{5}$ |
| 5 | 11 | $3 y_{2} y_{3} y_{4} y_{5}^{2} + 3 y_{2} y_{3} y_{4} y_{5}$ |
| 6 | 1 | $1$ |
| 6 | 2 | $1$ |
| 6 | 3 | $1$ |
| 6 | 4 | $1$ |
| 6 | 6 | $- y_{1}$ |
| 6 | 8 | $y_{1}$ |
| 6 | 9 | $y_{1}$ |
| 6 | 10 | $- y_{1}$ |
| 7 | 1 | $3$ |
| 7 | 5 | $1$ |
| 7 | 7 | $- y_{2} - y_{4} y_{5}$ |
| 7 | 8 | $y_{3}$ |
| 7 | 9 | $y_{2}$ |
| 7 | 11 | $2 y_{2} y_{3} y_{5}$ |
| 8 | 2 | $2$ |
| 8 | 5 | $1$ |
| 8 | 7 | $y_{4} y_{5}$ |
| 8 | 8 | $- y_{2} y_{5} - y_{3}$ |
| 8 | 10 | $y_{2} y_{5}$ |
| 8 | 11 | $2 y_{2} y_{4} y_{5}$ |
| 9 | 1 | $1$ |
| 9 | 3 | $2$ |
| 9 | 5 | $2$ |
| 9 | 7 | $y_{3} y_{5}$ |
| 9 | 8 | $y_{3}$ |
| 9 | 9 | $- y_{3} y_{5}$ |
| 9 | 10 | $y_{3} y_{5}$ |
| 9 | 11 | $2 y_{2} y_{3} y_{5} + 2 y_{3} y_{4} y_{5}$ |
| 10 | 4 | $1$ |
| 10 | 5 | $2$ |
| 10 | 6 | $- y_{4}$ |
| 10 | 7 | $y_{4} y_{5}$ |
| 10 | 8 | $y_{4}$ |
| 10 | 9 | $y_{4}$ |
| 10 | 10 | $- y_{4}$ |
| 10 | 11 | $2 y_{2} y_{4} y_{5} + 2 y_{3} y_{4} y_{5}$ |
| 11 | 6 | $1$ |
| 11 | 7 | $1$ |
| 11 | 8 | $1$ |
| 11 | 9 | $1$ |
| 11 | 10 | $1$ |
