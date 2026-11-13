---
title: HLM-29 — 4-fold complete intersection
description: Exact fan inputs, ordered ambient basis, symbolic quantum multiplication and saved computation notes for HLM-29.
---

# HLM-29

**Construction:** Verra fourfold. **Dimension:** 4. **Index in source:** 2. **h(1,1):** 2.


[Catalogue](../index.md) · [4-folds](../fourfolds.md)

Saved record: **complete with notes**. Matrix coefficients are exact; connection-factor notes below are retained. This page transcribes a completed computation, without rerunning localization.

## HLM-29 --- geometry and Hodge diamond

**Selection:**  nef_additional.
Verra fourfold
**Hodge source:**  HLM-29, HLM Proposition 7.2, [1907.08000v3](https://arxiv.org/abs/1907.08000v3).
$\dim X=4$, $\dim Y=5$, codimension $1$, index $2$, $(-K_X)^4=192$, $e(X)=30$.
\[\begin{array}{ccccccccc}&&&&1&&&&\\&&&0&&0&&&\\&&0&&2&&0&&\\&0&&0&&0&&0&\\0&&1&&22&&1&&0\\&0&&0&&0&&0&\\&&0&&2&&0&&\\&&&0&&0&&&\\&&&&1&&&&\end{array}\]
Ambient rank: 9; full even rank: 30; full odd rank: 0. The complement of the ambient image in middle cohomology has dimension 21.
\[\begin{aligned}\int_Xc_1^4&=192,&\int_Xc_1^2c_2&=144\\\int_Xc_2^2&=114,&\int_Xc_1c_3&=24\\\int_Xc_4&=30,&\chi(\mathcal O_X)&=1.\end{aligned}\]
Minimum wall degrees of the defining bundles: [0]; minimum adjunction wall degree: 0.

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
weights = [[1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1]]
bundles = [[2, 2]]
rays = [[-1, -1, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, -1, -1, -1], [0, 0, 1, 0, 0],
 [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
cones = [[0, 1, 2, 4, 5], [0, 1, 2, 4, 6], [0, 1, 2, 5, 6], [0, 1, 3, 4, 5], [0, 1, 3, 4, 6],
 [0, 1, 3, 5, 6], [0, 2, 3, 4, 5], [0, 2, 3, 4, 6], [0, 2, 3, 5, 6], [1, 2, 3, 4, 5],
 [1, 2, 3, 4, 6], [1, 2, 3, 5, 6]]
K = [[2, 0, 0, 0, 2, 0, 0]]
novikov_divisors = [[0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:** 

```python
['1', 'x3', 'x0', 'x3^2', 'x0^2', 'x0*x3', 'x0*x3^2', 'x0^2*x3', 'x0*x3^3']
```

## HLM-29 --- computation record

**Status:**  complete_with_notes.
**Checkpoint directory:** 

```python
examples/additional_fourfolds/batch_results/HLM-29
```

Enumeration: mori; 6 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x3', 'x0', 'x3^2', 'x0^2', 'x0*x3', 'x0*x3^2', 'x0^2*x3', 'x0*x3^3']
```

\[\mathrm{Gr}=\operatorname{diag}(-2,-1,-1,0,0,0,1,1,2)\]

| $i$ | $j$ | $M_{ij}$ |
|---|---|---|
| 0 | 1 | $4 y_{1} y_{2} + 4 y_{2}$ |
| 0 | 2 | $4 y_{2}$ |
| 0 | 6 | $96 y_{1} y_{2}^{2}$ |
| 0 | 7 | $32 y_{1} y_{2}^{2}$ |
| 1 | 0 | $2$ |
| 1 | 3 | $4 y_{1} y_{2} + 16 y_{2}$ |
| 1 | 4 | $8 y_{2}$ |
| 1 | 5 | $12 y_{2}$ |
| 1 | 8 | $96 y_{1} y_{2}^{2}$ |
| 2 | 3 | $12 y_{1} y_{2} - 12 y_{2}$ |
| 2 | 4 | $- 4 y_{2}$ |
| 2 | 5 | $4 y_{1} y_{2} - 8 y_{2}$ |
| 3 | 1 | $2$ |
| 3 | 6 | $20 y_{2}$ |
| 3 | 7 | $8 y_{2}$ |
| 4 | 6 | $12 y_{1} y_{2} + 12 y_{2}$ |
| 4 | 7 | $4 y_{1} y_{2} + 4 y_{2}$ |
| 5 | 2 | $2$ |
| 5 | 6 | $4 y_{1} y_{2} - 32 y_{2}$ |
| 5 | 7 | $- 12 y_{2}$ |
| 6 | 3 | $6$ |
| 6 | 5 | $2$ |
| 6 | 8 | $12 y_{2}$ |
| 7 | 3 | $-6$ |
| 7 | 4 | $2$ |
| 7 | 8 | $12 y_{1} y_{2} - 24 y_{2}$ |
| 8 | 6 | $2$ |
| 8 | 7 | $\frac{2}{3}$ |

Matrix time: 0.14 minutes. Saved checks: matrix rank, basis, Poincare pairing, unit column, c1 homogeneity.

### Specialized spectrum

At $y_1=2,\ y_2=3$, let $K^F=-M$.

\[\Delta=0\]

Cyclic at this point: False.
Numerical eigenvalues of $M$ (multiplicities retained):

| $j$ | Real part | Imaginary part |
|---|---|---|
| 1 | 23.53751012 | 0 |
| 2 | -23.53751012 | 0 |
| 3 | 2.490736917 | -8.198229182 |
| 4 | 2.490736917 | 8.198229182 |
| 5 | -2.490736917 | -8.198229182 |
| 6 | -2.490736917 | 8.198229182 |
| 7 | 0 | 0 |
| 8 | 0 | 0 |
| 9 | 0 | 0 |

### Exact characteristic factors and connection exponents

Factor 1: multiplicity 3; 1 distinct root(s) of $\det(xI-K^F)$.

\[\begin{aligned}p_{1}(x)&=x\end{aligned}\]

Complete exponent computation: False.
**Unresolved:** 

```python
the eigenvalue 0 has a 3-dimensional kernel, so its generalized eigenspace is not a single Jordan block and the factor is not cyclic (check cyclic_determinant first)
```

Factor 2: multiplicity 1; 6 distinct root(s) of $\det(xI-K^F)$.

\[\begin{aligned}p_{2}(x)&=x^{6} - 432 x^{4} - 62208 x^{2} - 2985984\end{aligned}\]

\[\text{Powers}=\{0\}\]

\[\text{Classes modulo }\mathbb Z=\{0\}\]

Complete exponent computation: True.
Exponent lists are multisets per eigenvalue in each factor. They describe the computed ambient sector only.

**Search aliases:** HLM-29; dimension 4; fourfold; Verra fourfold; Fano; quantum cohomology; Gromov-Witten; Hodge diamond; quantum multiplication; connection exponents; Hausen Laface Mauz; HLM.
