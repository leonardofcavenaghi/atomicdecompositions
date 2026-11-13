---
title: "Complete intersection of multidegrees (2,3), (1,1) in P³ × P⁴ — PROD5-D03"
description: Exact fan inputs, ordered ambient basis, symbolic quantum multiplication and saved computation notes for PROD5-D03.
---

# Complete intersection in \(\mathbb P^{3}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{3}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[2, 3], [1, 1]]`.

Source identifier: **PROD5-D03**; see [CKP and HLM terminology](../sources.md). The presentation is verified by the [fan and divisor certificate](../../data/geometric-presentations.json).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index in source:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)

Saved record: **complete with notes**. Matrix coefficients are exact; connection-factor notes below are retained. This page transcribes a completed computation, without rerunning localization.

## PROD5-D03 --- construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{3}\times\mathbb P^{4}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 3], [1, 1]]
residual_product_degrees = [1, 1]
```

The residual product degrees give the anticanonical class. 
Related workbook IDs: [50, 94].

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=90$, $e(X)=-2138$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&56&&1019&&1019&&56&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=56$, $h^{3,2}=1019$; even rank 12; odd rank 2150.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 54, -1016)$.

```python
chern_numbers = {'c1_5': 90, 'c1_3_c2': 294, 'c1_c2_2': 962, 'c1_2_c3': -238, 'c2_c3': -750, 'c1_c4': 914, 'c5': -2138}
```

### Exact software inputs

Executable input: `examples/fivefolds_positive/inputs/PROD5-D03.py`. Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

```python
rays = [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0],
 [-1, -1, -1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, -1, -1, -1, -1]]
cones = [[0, 1, 2, 4, 5, 6, 7], [0, 1, 2, 4, 5, 6, 8], [0, 1, 2, 4, 5, 7, 8],
 [0, 1, 2, 4, 6, 7, 8], [0, 1, 2, 5, 6, 7, 8], [0, 1, 3, 4, 5, 6, 7],
 [0, 1, 3, 4, 5, 6, 8], [0, 1, 3, 4, 5, 7, 8], [0, 1, 3, 4, 6, 7, 8],
 [0, 1, 3, 5, 6, 7, 8], [0, 2, 3, 4, 5, 6, 7], [0, 2, 3, 4, 5, 6, 8],
 [0, 2, 3, 4, 5, 7, 8], [0, 2, 3, 4, 6, 7, 8], [0, 2, 3, 5, 6, 7, 8],
 [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 8], [1, 2, 3, 4, 5, 7, 8],
 [1, 2, 3, 4, 6, 7, 8], [1, 2, 3, 5, 6, 7, 8]]
K = [[2, 0, 0, 0, 3, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

### Ordered basis and curve conventions

```python
ambient_basis = ['1', 'x4', 'x0', 'x4^2', 'x0^2', 'x0*x4', 'x4^3', 'x0^3', 'x0*x4^2', 'x4^4', 'x0*x4^3',
 'x0*x4^4']
ambient_rank = 12
novikov_divisors = [[0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0]]
h2_basis = [[1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1]]
```

### Computation record

**Status:**  complete with notes. Snapshot: 2026-11-09 18:05 UTC.
Checkpoint directory: `examples/fivefolds_positive/batch_results/PROD5-D03/`.

### Computed quantum multiplication

Write $M=c_1(X)\star$ and use the ordered basis $e_0,\ldots,e_{11}$ below. Columns are images: $M e_j=\sum_i M_{ij}e_i$.

```python
basis = ['1', 'x4', 'x0', 'x4^2', 'x0^2', 'x0*x4', 'x4^3', 'x0^3', 'x0*x4^2', 'x4^4', 'x0*x4^3', 'x0*x4^4']
```



$$
\mathrm{Gr}=\operatorname{diag}\!\left(- \frac{5}{2},- \frac{3}{2},- \frac{3}{2},- \frac{1}{2},- \frac{1}{2},- \frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{3}{2},\frac{3}{2},\frac{5}{2}\right).
$$


**Exact matrix:**  every nonzero entry is listed below; all omitted entries are zero. Indices are zero based. No Novikov specialization has been made in this table.

| Row $i$ | Column $j$ | $M_{ij}$ |
|---|---|---|
| Row $i$ | Column $j$ | $M_{ij}$ |
| 0 | 1 | $108 y_{1}^{2} + 456 y_{1} y_{2}$ |
| 0 | 2 | $456 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 0 | 3 | $756 y_{1}^{3} + 47916 y_{1}^{2} y_{2} + 4080 y_{1} y_{2}^{2}$ |
| 0 | 4 | $16524 y_{1}^{2} y_{2} + 9468 y_{1} y_{2}^{2}$ |
| 0 | 5 | $36612 y_{1}^{2} y_{2} + 8496 y_{1} y_{2}^{2}$ |
| 0 | 6 | $1295712 y_{1}^{3} y_{2} + 1272384 y_{1}^{2} y_{2}^{2} + 9216 y_{1} y_{2}^{3}$ |
| 0 | 7 | $139968 y_{1}^{3} y_{2} + 744336 y_{1}^{2} y_{2}^{2} + 24768 y_{1} y_{2}^{3}$ |
| 0 | 8 | $1515888 y_{1}^{3} y_{2} + 2343840 y_{1}^{2} y_{2}^{2} + 34688 y_{1} y_{2}^{3}$ |
| 0 | 9 | $5443200 y_{1}^{4} y_{2} + 34515360 y_{1}^{3} y_{2}^{2} + 4065120 y_{1}^{2} y_{2}^{3} + 5120 y_{1} y_{2}^{4}$ |
| 0 | 10 | $16057440 y_{1}^{4} y_{2} + 121378680 y_{1}^{3} y_{2}^{2} + 18844800 y_{1}^{2} y_{2}^{3} + 40960 y_{1} y_{2}^{4}$ |
| 0 | 11 | $20155392 y_{1}^{5} y_{2} + 605050560 y_{1}^{4} y_{2}^{2} + 527117760 y_{1}^{3} y_{2}^{3} + 19979136 y_{1}^{2} y_{2}^{4} + 12288 y_{1} y_{2}^{5}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $9 y_{1}$ |
| 1 | 2 | $11 y_{2}$ |
| 1 | 3 | $108 y_{1}^{2} + 1736 y_{1} y_{2}$ |
| 1 | 4 | $1242 y_{1} y_{2} + 10 y_{2}^{2}$ |
| 1 | 5 | $1896 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 1 | 6 | $96174 y_{1}^{2} y_{2} + 10704 y_{1} y_{2}^{2}$ |
| 1 | 7 | $15309 y_{1}^{2} y_{2} + 15984 y_{1} y_{2}^{2}$ |
| 1 | 8 | $123930 y_{1}^{2} y_{2} + 29664 y_{1} y_{2}^{2}$ |
| 1 | 9 | $565056 y_{1}^{3} y_{2} + 1060704 y_{1}^{2} y_{2}^{2} + 10240 y_{1} y_{2}^{3}$ |
| 1 | 10 | $1698408 y_{1}^{3} y_{2} + 4102272 y_{1}^{2} y_{2}^{2} + 66688 y_{1} y_{2}^{3}$ |
| 1 | 11 | $2449440 y_{1}^{4} y_{2} + 35090280 y_{1}^{3} y_{2}^{2} + 8682000 y_{1}^{2} y_{2}^{3} + 28160 y_{1} y_{2}^{4}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $28 y_{1}$ |
| 2 | 3 | $456 y_{1}^{2} + 880 y_{1} y_{2}$ |
| 2 | 4 | $1176 y_{1} y_{2}$ |
| 2 | 5 | $108 y_{1}^{2} + 1336 y_{1} y_{2}$ |
| 2 | 6 | $1260 y_{1}^{3} + 101436 y_{1}^{2} y_{2} + 3072 y_{1} y_{2}^{2}$ |
| 2 | 7 | $25272 y_{1}^{2} y_{2} + 6552 y_{1} y_{2}^{2}$ |
| 2 | 8 | $756 y_{1}^{3} + 145836 y_{1}^{2} y_{2} + 10224 y_{1} y_{2}^{2}$ |
| 2 | 9 | $918144 y_{1}^{3} y_{2} + 636480 y_{1}^{2} y_{2}^{2} + 2048 y_{1} y_{2}^{3}$ |
| 2 | 10 | $2860416 y_{1}^{3} y_{2} + 2651904 y_{1}^{2} y_{2}^{2} + 15360 y_{1} y_{2}^{3}$ |
| 2 | 11 | $5443200 y_{1}^{4} y_{2} + 34515360 y_{1}^{3} y_{2}^{2} + 4065120 y_{1}^{2} y_{2}^{3} + 5120 y_{1} y_{2}^{4}$ |
| 3 | 1 | $1$ |
| 3 | 4 | $18 y_{2}$ |
| 3 | 5 | $11 y_{2}$ |
| 3 | 6 | $1552 y_{1} y_{2}$ |
| 3 | 7 | $486 y_{1} y_{2} + 6 y_{2}^{2}$ |
| 3 | 8 | $2418 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 3 | 9 | $16848 y_{1}^{2} y_{2} + 4368 y_{1} y_{2}^{2}$ |
| 3 | 10 | $52326 y_{1}^{2} y_{2} + 21576 y_{1} y_{2}^{2}$ |
| 3 | 11 | $93312 y_{1}^{3} y_{2} + 496224 y_{1}^{2} y_{2}^{2} + 16512 y_{1} y_{2}^{3}$ |
| 4 | 2 | $1$ |
| 4 | 3 | $46 y_{1}$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 5 | $28 y_{1}$ |
| 4 | 6 | $532 y_{1}^{2} + 416 y_{1} y_{2}$ |
| 4 | 7 | $564 y_{1} y_{2}$ |
| 4 | 8 | $456 y_{1}^{2} + 1112 y_{1} y_{2}$ |
| 4 | 9 | $504 y_{1}^{3} + 26232 y_{1}^{2} y_{2} + 384 y_{1} y_{2}^{2}$ |
| 4 | 10 | $1260 y_{1}^{3} + 92256 y_{1}^{2} y_{2} + 2592 y_{1} y_{2}^{2}$ |
| 4 | 11 | $382464 y_{1}^{3} y_{2} + 280704 y_{1}^{2} y_{2}^{2} + 1024 y_{1} y_{2}^{3}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $1$ |
| 5 | 3 | $43 y_{1}$ |
| 5 | 4 | $5 y_{2}$ |
| 5 | 5 | $9 y_{1}$ |
| 5 | 6 | $180 y_{1}^{2} + 1280 y_{1} y_{2}$ |
| 5 | 7 | $918 y_{1} y_{2}$ |
| 5 | 8 | $108 y_{1}^{2} + 2596 y_{1} y_{2}$ |
| 5 | 9 | $35856 y_{1}^{2} y_{2} + 2112 y_{1} y_{2}^{2}$ |
| 5 | 10 | $119124 y_{1}^{2} y_{2} + 11904 y_{1} y_{2}^{2}$ |
| 5 | 11 | $339552 y_{1}^{3} y_{2} + 570624 y_{1}^{2} y_{2}^{2} + 6656 y_{1} y_{2}^{3}$ |
| 6 | 3 | $1$ |
| 6 | 4 | $- \frac{9}{19}$ |
| 6 | 5 | $- \frac{9}{19}$ |
| 6 | 6 | $- \frac{474 y_{1}}{19}$ |
| 6 | 7 | $9 y_{2}$ |
| 6 | 8 | $- \frac{387 y_{1}}{19} + 11 y_{2}$ |
| 6 | 9 | $- \frac{648 y_{1}^{2}}{19} + \frac{3744 y_{1} y_{2}}{19}$ |
| 6 | 10 | $- \frac{1620 y_{1}^{2}}{19} + \frac{10404 y_{1} y_{2}}{19} + 4 y_{2}^{2}$ |
| 6 | 11 | $- \frac{54432 y_{1}^{2} y_{2}}{19} + \frac{43704 y_{1} y_{2}^{2}}{19}$ |
| 7 | 4 | $\frac{122}{57}$ |
| 7 | 5 | $\frac{65}{57}$ |
| 7 | 6 | $\frac{4424 y_{1}}{57}$ |
| 7 | 7 | $- 2 y_{2}$ |
| 7 | 8 | $\frac{5417 y_{1}}{57}$ |
| 7 | 9 | $\frac{5056 y_{1}^{2}}{19} + \frac{5376 y_{1} y_{2}}{19}$ |
| 7 | 10 | $\frac{14008 y_{1}^{2}}{19} + \frac{78304 y_{1} y_{2}}{57}$ |
| 7 | 11 | $504 y_{1}^{3} + \frac{406920 y_{1}^{2} y_{2}}{19} + \frac{20288 y_{1} y_{2}^{2}}{19}$ |
| 8 | 3 | $1$ |
| 8 | 4 | $\frac{15}{19}$ |
| 8 | 5 | $\frac{34}{19}$ |
| 8 | 6 | $\frac{790 y_{1}}{19}$ |
| 8 | 7 | $3 y_{2}$ |
| 8 | 8 | $\frac{645 y_{1}}{19}$ |
| 8 | 9 | $\frac{1080 y_{1}^{2}}{19} + \frac{8656 y_{1} y_{2}}{19}$ |
| 8 | 10 | $\frac{2700 y_{1}^{2}}{19} + \frac{35632 y_{1} y_{2}}{19}$ |
| 8 | 11 | $\frac{300024 y_{1}^{2} y_{2}}{19} + \frac{47088 y_{1} y_{2}^{2}}{19}$ |
| 9 | 6 | $1$ |
| 9 | 7 | $- \frac{15}{4}$ |
| 9 | 8 | $- \frac{19}{4}$ |
| 9 | 9 | $- 70 y_{1}$ |
| 9 | 10 | $- \frac{395 y_{1}}{2} + 11 y_{2}$ |
| 9 | 11 | $- 270 y_{1}^{2} - 684 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 10 | 6 | $1$ |
| 10 | 7 | $\frac{3}{2}$ |
| 10 | 8 | $\frac{7}{2}$ |
| 10 | 9 | $28 y_{1}$ |
| 10 | 10 | $79 y_{1}$ |
| 10 | 11 | $108 y_{1}^{2} + 456 y_{1} y_{2}$ |
| 11 | 9 | $1$ |
| 11 | 10 | $\frac{7}{2}$ |

Enumeration mode: positive; 26 curve classes including zero. Matrix computation time: 133.51 minutes.
Saved checks: matrix rank, basis, Poincare pairing, unit column, c1 homogeneity.

## PROD5-D03 --- spectrum and connection

**Specialization:**  $y_1=2,\ y_2=3$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$



$$
\det(xI-K^F)=p_{1}(x)^{7}\,p_{2}(x).
$$




$$
\begin{aligned}p_{1}(x)&=x - 18.\end{aligned}
$$




$$
\begin{aligned}p_{2}(x)&=x^{5} + 186 x^{4} - 157212 x^{3} + 23873544 x^{2} - 710255196 x\\&+5945038200.\end{aligned}
$$


Cyclic determinant: $\Delta=0$. The specialized operator is not cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 552.79102 | 0 | 7 | -18 | 0 |
| 2 | -165.43492 | -77.267395 | 8 | -18 | 0 |
| 3 | -165.43492 | 77.267395 | 9 | -18 | 0 |
| 4 | -18 | 0 | 10 | -18 | 0 |
| 5 | -18 | 0 | 11 | -17.960593 | -0.013974018 |
| 6 | -18 | 0 | 12 | -17.960593 | 0.013974018 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | unresolved | unresolved | not computed |
| $p_{2}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
**Unresolved factor $p_{1}$:**  the eigenvalue 18 has a 2-dimensional kernel, so its generalized eigenspace is not a single Jordan block and the factor is not cyclic (check cyclic_determinant first).

**Search aliases:** PROD5-D03; dimension 5; fivefold; Complete intersection in a product of projective spaces; Fano; quantum cohomology; Gromov-Witten; Hodge diamond; quantum multiplication; connection exponents; Complete intersection of multidegrees (2,3), (1,1) in P³ × P⁴; product of projective spaces.
