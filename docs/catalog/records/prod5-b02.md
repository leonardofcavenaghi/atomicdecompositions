---
title: PROD5-B02 — 5-fold complete intersection
description: Exact fan inputs, ordered ambient basis, symbolic quantum multiplication and saved computation notes for PROD5-B02.
---

# PROD5-B02

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index in source:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)

Saved record: **complete**. Matrix coefficients are exact; connection-factor notes below are retained. This page transcribes a completed computation, without rerunning localization.

## PROD5-B02 --- construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{3}\times\mathbb P^{3}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 3]]
residual_product_degrees = [2, 1]
```

The residual product degrees give the anticanonical class. 
Related workbook IDs: [29, 31].

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=320$, $e(X)=-668$.
\[\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&10&&330&&330&&10&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}\]
$h^{4,1}=10$, $h^{3,2}=330$; even rank 12; odd rank 680.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 8, -327)$.

```python
chern_numbers = {'c1_5': 320, 'c1_3_c2': 568, 'c1_c2_2': 896, 'c1_2_c3': -132, 'c2_c3': -92, 'c1_c4': 548, 'c5': -668}
```

### Exact software inputs

Executable input: `examples/fivefolds_positive/inputs/PROD5-B02.py`. Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

```python
rays = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [-1, -1, -1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, -1, -1, -1]]
cones = [[0, 1, 2, 4, 5, 6], [0, 1, 2, 4, 5, 7], [0, 1, 2, 4, 6, 7], [0, 1, 2, 5, 6, 7],
 [0, 1, 3, 4, 5, 6], [0, 1, 3, 4, 5, 7], [0, 1, 3, 4, 6, 7], [0, 1, 3, 5, 6, 7],
 [0, 2, 3, 4, 5, 6], [0, 2, 3, 4, 5, 7], [0, 2, 3, 4, 6, 7], [0, 2, 3, 5, 6, 7],
 [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7], [1, 2, 3, 4, 6, 7], [1, 2, 3, 5, 6, 7]]
K = [[2, 0, 0, 0, 3, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

### Ordered basis and curve conventions

```python
ambient_basis = ['1', 'x4', 'x0', 'x4^2', 'x0^2', 'x0*x4', 'x4^3', 'x0^3', 'x0*x4^2', 'x0*x4^3',
 'x0^3*x4', 'x0^2*x4^3']
ambient_rank = 12
novikov_divisors = [[0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
h2_basis = [[1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1]]
```

### Computation record

**Status:**  complete. Snapshot: 2026-11-09 18:05 UTC.
Checkpoint directory: `examples/fivefolds_positive/batch_results/PROD5-B02/`.

### Computed quantum multiplication

Write $M=c_1(X)\star$ and use the ordered basis $e_0,\ldots,e_{11}$ below. Columns are images: $M e_j=\sum_i M_{ij}e_i$.

```python
basis = ['1', 'x4', 'x0', 'x4^2', 'x0^2', 'x0*x4', 'x4^3', 'x0^3', 'x0*x4^2', 'x0*x4^3', 'x0^3*x4', 'x0^2*x4^3']
```

\[\mathrm{Gr}=\operatorname{diag}\!\left(- \frac{5}{2},- \frac{3}{2},- \frac{3}{2},- \frac{1}{2},- \frac{1}{2},- \frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{3}{2},\frac{3}{2},\frac{5}{2}\right).\]
**Exact matrix:**  every nonzero entry is listed below; all omitted entries are zero. Indices are zero based. No Novikov specialization has been made in this table.

| Row $i$ | Column $j$ | $M_{ij}$ |
|---|---|---|
| Row $i$ | Column $j$ | $M_{ij}$ |
| 0 | 1 | $108 y_{1}^{2}$ |
| 0 | 2 | $4 y_{2}$ |
| 0 | 3 | $756 y_{1}^{3} + 192 y_{1} y_{2}$ |
| 0 | 4 | $324 y_{1} y_{2}$ |
| 0 | 5 | $324 y_{1} y_{2}$ |
| 0 | 6 | $5280 y_{1}^{2} y_{2}$ |
| 0 | 7 | $5184 y_{1}^{2} y_{2}$ |
| 0 | 8 | $15120 y_{1}^{2} y_{2}$ |
| 0 | 9 | $129600 y_{1}^{3} y_{2} + 320 y_{1} y_{2}^{2}$ |
| 0 | 10 | $136080 y_{1}^{3} y_{2} + 1440 y_{1} y_{2}^{2}$ |
| 0 | 11 | $746496 y_{1}^{4} y_{2} + 44928 y_{1}^{2} y_{2}^{2}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $9 y_{1}$ |
| 1 | 3 | $108 y_{1}^{2}$ |
| 1 | 4 | $18 y_{2}$ |
| 1 | 5 | $4 y_{2}$ |
| 1 | 6 | $240 y_{1} y_{2}$ |
| 1 | 7 | $567 y_{1} y_{2}$ |
| 1 | 8 | $864 y_{1} y_{2}$ |
| 1 | 9 | $12528 y_{1}^{2} y_{2}$ |
| 1 | 10 | $15876 y_{1}^{2} y_{2}$ |
| 1 | 11 | $90720 y_{1}^{3} y_{2} + 960 y_{1} y_{2}^{2}$ |
| 2 | 0 | $2$ |
| 2 | 1 | $22 y_{1}$ |
| 2 | 3 | $312 y_{1}^{2}$ |
| 2 | 4 | $4 y_{2}$ |
| 2 | 5 | $108 y_{1}^{2}$ |
| 2 | 6 | $504 y_{1}^{3} + 96 y_{1} y_{2}$ |
| 2 | 7 | $486 y_{1} y_{2}$ |
| 2 | 8 | $756 y_{1}^{3} + 432 y_{1} y_{2}$ |
| 2 | 9 | $11808 y_{1}^{2} y_{2}$ |
| 2 | 10 | $18792 y_{1}^{2} y_{2}$ |
| 2 | 11 | $129600 y_{1}^{3} y_{2} + 320 y_{1} y_{2}^{2}$ |
| 3 | 1 | $1$ |
| 3 | 7 | $18 y_{2}$ |
| 3 | 8 | $4 y_{2}$ |
| 3 | 9 | $324 y_{1} y_{2}$ |
| 3 | 10 | $567 y_{1} y_{2}$ |
| 3 | 11 | $3456 y_{1}^{2} y_{2}$ |
| 4 | 2 | $2$ |
| 4 | 3 | $24 y_{1}$ |
| 4 | 5 | $22 y_{1}$ |
| 4 | 6 | $160 y_{1}^{2}$ |
| 4 | 8 | $312 y_{1}^{2}$ |
| 4 | 9 | $504 y_{1}^{3} + 96 y_{1} y_{2}$ |
| 4 | 10 | $360 y_{1} y_{2}$ |
| 4 | 11 | $5280 y_{1}^{2} y_{2}$ |
| 5 | 1 | $2$ |
| 5 | 2 | $1$ |
| 5 | 3 | $28 y_{1}$ |
| 5 | 5 | $9 y_{1}$ |
| 5 | 6 | $72 y_{1}^{2}$ |
| 5 | 7 | $6 y_{2}$ |
| 5 | 8 | $108 y_{1}^{2}$ |
| 5 | 9 | $288 y_{1} y_{2}$ |
| 5 | 10 | $756 y_{1} y_{2}$ |
| 5 | 11 | $7200 y_{1}^{2} y_{2}$ |
| 6 | 3 | $1$ |
| 6 | 4 | $- \frac{9}{4}$ |
| 6 | 5 | $- \frac{9}{2}$ |
| 6 | 6 | $- 33 y_{1}$ |
| 6 | 8 | $- 63 y_{1}$ |
| 6 | 9 | $- 162 y_{1}^{2} + 4 y_{2}$ |
| 6 | 10 | $18 y_{2}$ |
| 6 | 11 | $- 162 y_{1} y_{2}$ |
| 7 | 4 | $\frac{8}{3}$ |
| 7 | 5 | $\frac{4}{3}$ |
| 7 | 6 | $16 y_{1}$ |
| 7 | 8 | $\frac{128 y_{1}}{3}$ |
| 7 | 9 | $208 y_{1}^{2}$ |
| 7 | 10 | $108 y_{1}^{2}$ |
| 7 | 11 | $504 y_{1}^{3} + 128 y_{1} y_{2}$ |
| 8 | 3 | $2$ |
| 8 | 4 | $\frac{3}{2}$ |
| 8 | 5 | $4$ |
| 8 | 6 | $22 y_{1}$ |
| 8 | 8 | $42 y_{1}$ |
| 8 | 9 | $108 y_{1}^{2}$ |
| 8 | 10 | $6 y_{2}$ |
| 8 | 11 | $324 y_{1} y_{2}$ |
| 9 | 6 | $2$ |
| 9 | 8 | $4$ |
| 9 | 11 | $4 y_{2}$ |
| 10 | 7 | $1$ |
| 10 | 8 | $\frac{4}{3}$ |
| 10 | 9 | $\frac{44 y_{1}}{3}$ |
| 10 | 10 | $9 y_{1}$ |
| 10 | 11 | $72 y_{1}^{2}$ |
| 11 | 9 | $2$ |
| 11 | 10 | $\frac{3}{2}$ |

Enumeration mode: positive; 14 curve classes including zero. Matrix computation time: 10.68 minutes.
Saved checks: matrix rank, basis, Poincare pairing, unit column, c1 homogeneity.

## PROD5-B02 --- spectrum and connection

**Specialization:**  $y_1=2,\ y_2=3$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$

\[\det(xI-K^F)=p_{1}(x)^{4}\,p_{2}(x).\]
\[\begin{aligned}p_{1}(x)&=x - 12.\end{aligned}\]
\[\begin{aligned}p_{2}(x)&=x^{8} + 120 x^{7} + 3192 x^{6} + 165024 x^{5} - 24639984 x^{4}\\&+731278080 x^{3} - 9592128000 x^{2} + 59939426304 x\\&-146046578688.\end{aligned}\]
Cyclic determinant: $\Delta=-39026244510746984439730217597591863638834020352$. The specialized operator is cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 122.11748 | 0 | 7 | -12 | 0 |
| 2 | 28.393931 | -67.859904 | 8 | -12 | 0 |
| 3 | 28.393931 | 67.859904 | 9 | -12 | 0 |
| 4 | -13.512952 | 0 | 10 | -12 | 0 |
| 5 | -12.250337 | -0.856354 | 11 | -11.257521 | 0 |
| 6 | -12.250337 | 0.856354 | 12 | -9.6341909 | 0 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | $- \frac{3}{2},\ - \frac{3}{2},\ - \frac{3}{2},\ - \frac{3}{2}$ | $\frac{1}{2},\ \frac{1}{2},\ \frac{1}{2},\ \frac{1}{2}$ | complete / recursion |
| $p_{2}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
Recursion obstruction for $p_{1}$: $- \frac{\left(2 s + 3\right)^{4}}{1333248}$.

**Search aliases:** PROD5-B02; dimension 5; fivefold; Complete intersection in a product of projective spaces; Fano; quantum cohomology; Gromov-Witten; Hodge diamond; quantum multiplication; connection exponents.
