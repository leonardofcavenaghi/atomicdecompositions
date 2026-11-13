---
title: "Complete intersection of multidegrees (2,1), (1,3) in P³ × P⁴ — PROD5-D04"
description: Exact fan inputs, ordered ambient basis, symbolic quantum multiplication and saved computation notes for PROD5-D04.
---

# Complete intersection in \(\mathbb P^{3}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{3}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[2, 1], [1, 3]]`.

Source identifier: **PROD5-D04**; see [CKP and HLM terminology](../sources.md). The presentation is verified by the [fan and divisor certificate](../../data/geometric-presentations.json).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index in source:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)

Saved record: **complete with notes**. Matrix coefficients are exact; connection-factor notes below are retained. This page transcribes a completed computation, without rerunning localization.

<!-- saved-exponent-summary:start -->
## Regularized exponent multisets

Analysis point: `y1=2, y2=3`. These lists describe the computed ambient connection. Every row applies **separately to each eigenvalue** satisfying the displayed condition; repeated entries retain their multiplicity.

The characteristic factors below use \(K^F=-A\), so an eigenvalue \(\lambda\) of \(A=c_1\star\) satisfies \(p_i(-\lambda)=0\). The classes are powers modulo \(\mathbb Z\); their order does not pair them term by term with the powers.

| Spectral condition | Multiplicity per eigenvalue | \(F_{b,\lambda}\) | Saved computation |
|---|---:|---|---|
| \(p_{1}(-\lambda)=0\) | 6 | Unresolved | Unresolved |
| \(p_{2}(-\lambda)=0\) | 1 | \(\{\!\{0\}\!\}\) | Complete |

Unresolved factors have no computed multiset here. These ambient data alone do not identify full atoms or establish a rationality result. See the [connection conventions](../../toric/mathematics.md).
<!-- saved-exponent-summary:end -->

## PROD5-D04 --- construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{3}\times\mathbb P^{4}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 1], [1, 3]]
residual_product_degrees = [1, 1]
```

The residual product degrees give the anticanonical class. 
Related workbook IDs: [52, 98].

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=110$, $e(X)=-864$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&19&&419&&419&&19&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=19$, $h^{3,2}=419$; even rank 12; odd rank 876.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 17, -416)$.

```python
chern_numbers = {'c1_5': 110, 'c1_3_c2': 298, 'c1_c2_2': 798, 'c1_2_c3': -128, 'c2_c3': -296, 'c1_c4': 528, 'c5': -864}
```

### Exact software inputs

Executable input: `examples/fivefolds_positive/inputs/PROD5-D04.py`. Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

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
K = [[2, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 3, 0, 0, 0, 0]]
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
Checkpoint directory: `examples/fivefolds_positive/batch_results/PROD5-D04/`.

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
| 0 | 1 | $108 y_{1}^{2} + 264 y_{1} y_{2}$ |
| 0 | 2 | $264 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 0 | 3 | $756 y_{1}^{3} + 22104 y_{1}^{2} y_{2} + 1716 y_{1} y_{2}^{2}$ |
| 0 | 4 | $7236 y_{1}^{2} y_{2} + 3852 y_{1} y_{2}^{2}$ |
| 0 | 5 | $17388 y_{1}^{2} y_{2} + 3708 y_{1} y_{2}^{2}$ |
| 0 | 6 | $538992 y_{1}^{3} y_{2} + 343776 y_{1}^{2} y_{2}^{2} + 2944 y_{1} y_{2}^{3}$ |
| 0 | 7 | $46656 y_{1}^{3} y_{2} + 165312 y_{1}^{2} y_{2}^{2} + 6864 y_{1} y_{2}^{3}$ |
| 0 | 8 | $645120 y_{1}^{3} y_{2} + 708672 y_{1}^{2} y_{2}^{2} + 12128 y_{1} y_{2}^{3}$ |
| 0 | 9 | $1740960 y_{1}^{4} y_{2} + 6437280 y_{1}^{3} y_{2}^{2} + 699040 y_{1}^{2} y_{2}^{3} + 1280 y_{1} y_{2}^{4}$ |
| 0 | 10 | $6909840 y_{1}^{4} y_{2} + 29531760 y_{1}^{3} y_{2}^{2} + 3974840 y_{1}^{2} y_{2}^{3} + 11840 y_{1} y_{2}^{4}$ |
| 0 | 11 | $6718464 y_{1}^{5} y_{2} + 112539456 y_{1}^{4} y_{2}^{2} + 74682432 y_{1}^{3} y_{2}^{3} + 3095424 y_{1}^{2} y_{2}^{4} + 3072 y_{1} y_{2}^{5}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $9 y_{1}$ |
| 1 | 2 | $9 y_{2}$ |
| 1 | 3 | $108 y_{1}^{2} + 858 y_{1} y_{2}$ |
| 1 | 4 | $582 y_{1} y_{2} + 14 y_{2}^{2}$ |
| 1 | 5 | $1008 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 1 | 6 | $39501 y_{1}^{2} y_{2} + 3696 y_{1} y_{2}^{2}$ |
| 1 | 7 | $5103 y_{1}^{2} y_{2} + 4401 y_{1} y_{2}^{2}$ |
| 1 | 8 | $54387 y_{1}^{2} y_{2} + 11226 y_{1} y_{2}^{2}$ |
| 1 | 9 | $179784 y_{1}^{3} y_{2} + 224040 y_{1}^{2} y_{2}^{2} + 2688 y_{1} y_{2}^{3}$ |
| 1 | 10 | $724500 y_{1}^{3} y_{2} + 1107996 y_{1}^{2} y_{2}^{2} + 20288 y_{1} y_{2}^{3}$ |
| 1 | 11 | $816480 y_{1}^{4} y_{2} + 7001280 y_{1}^{3} y_{2}^{2} + 1528200 y_{1}^{2} y_{2}^{3} + 7360 y_{1} y_{2}^{4}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $23 y_{1}$ |
| 2 | 3 | $444 y_{1}^{2} + 412 y_{1} y_{2}$ |
| 2 | 4 | $526 y_{1} y_{2}$ |
| 2 | 5 | $108 y_{1}^{2} + 676 y_{1} y_{2}$ |
| 2 | 6 | $1764 y_{1}^{3} + 36615 y_{1}^{2} y_{2} + 1008 y_{1} y_{2}^{2}$ |
| 2 | 7 | $7965 y_{1}^{2} y_{2} + 1854 y_{1} y_{2}^{2}$ |
| 2 | 8 | $756 y_{1}^{3} + 58965 y_{1}^{2} y_{2} + 3732 y_{1} y_{2}^{2}$ |
| 2 | 9 | $267000 y_{1}^{3} y_{2} + 128240 y_{1}^{2} y_{2}^{2} + 512 y_{1} y_{2}^{3}$ |
| 2 | 10 | $1114284 y_{1}^{3} y_{2} + 672880 y_{1}^{2} y_{2}^{2} + 4480 y_{1} y_{2}^{3}$ |
| 2 | 11 | $1740960 y_{1}^{4} y_{2} + 6437280 y_{1}^{3} y_{2}^{2} + 699040 y_{1}^{2} y_{2}^{3} + 1280 y_{1} y_{2}^{4}$ |
| 3 | 1 | $1$ |
| 3 | 4 | $10 y_{2}$ |
| 3 | 5 | $9 y_{2}$ |
| 3 | 6 | $636 y_{1} y_{2}$ |
| 3 | 7 | $162 y_{1} y_{2} + 6 y_{2}^{2}$ |
| 3 | 8 | $1130 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 3 | 9 | $5310 y_{1}^{2} y_{2} + 1236 y_{1} y_{2}^{2}$ |
| 3 | 10 | $21987 y_{1}^{2} y_{2} + 7260 y_{1} y_{2}^{2}$ |
| 3 | 11 | $31104 y_{1}^{3} y_{2} + 110208 y_{1}^{2} y_{2}^{2} + 4576 y_{1} y_{2}^{3}$ |
| 4 | 2 | $1$ |
| 4 | 3 | $28 y_{1}$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 5 | $23 y_{1}$ |
| 4 | 6 | $520 y_{1}^{2} + 144 y_{1} y_{2}$ |
| 4 | 7 | $168 y_{1} y_{2}$ |
| 4 | 8 | $444 y_{1}^{2} + 444 y_{1} y_{2}$ |
| 4 | 9 | $504 y_{1}^{3} + 6930 y_{1}^{2} y_{2} + 96 y_{1} y_{2}^{2}$ |
| 4 | 10 | $1764 y_{1}^{3} + 32373 y_{1}^{2} y_{2} + 768 y_{1} y_{2}^{2}$ |
| 4 | 11 | $118368 y_{1}^{3} y_{2} + 56256 y_{1}^{2} y_{2}^{2} + 256 y_{1} y_{2}^{3}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $1$ |
| 5 | 3 | $44 y_{1}$ |
| 5 | 4 | $7 y_{2}$ |
| 5 | 5 | $9 y_{1}$ |
| 5 | 6 | $252 y_{1}^{2} + 616 y_{1} y_{2}$ |
| 5 | 7 | $366 y_{1} y_{2}$ |
| 5 | 8 | $108 y_{1}^{2} + 1454 y_{1} y_{2}$ |
| 5 | 9 | $12360 y_{1}^{2} y_{2} + 672 y_{1} y_{2}^{2}$ |
| 5 | 10 | $54348 y_{1}^{2} y_{2} + 4536 y_{1} y_{2}^{2}$ |
| 5 | 11 | $124704 y_{1}^{3} y_{2} + 146880 y_{1}^{2} y_{2}^{2} + 2048 y_{1} y_{2}^{3}$ |
| 6 | 3 | $1$ |
| 6 | 4 | $- \frac{9}{43}$ |
| 6 | 5 | $- \frac{9}{43}$ |
| 6 | 6 | $- \frac{537 y_{1}}{43}$ |
| 6 | 7 | $3 y_{2}$ |
| 6 | 8 | $- \frac{396 y_{1}}{43} + 9 y_{2}$ |
| 6 | 9 | $- \frac{648 y_{1}^{2}}{43} + \frac{3308 y_{1} y_{2}}{43}$ |
| 6 | 10 | $- \frac{2268 y_{1}^{2}}{43} + \frac{13678 y_{1} y_{2}}{43} + 4 y_{2}^{2}$ |
| 6 | 11 | $- \frac{3024 y_{1}^{2} y_{2}}{43} + \frac{31680 y_{1} y_{2}^{2}}{43}$ |
| 7 | 4 | $\frac{388}{129}$ |
| 7 | 5 | $\frac{259}{129}$ |
| 7 | 6 | $\frac{9706 y_{1}}{129}$ |
| 7 | 7 | $- 2 y_{2}$ |
| 7 | 8 | $\frac{15008 y_{1}}{129}$ |
| 7 | 9 | $\frac{11720 y_{1}^{2}}{43} + \frac{6904 y_{1} y_{2}}{43}$ |
| 7 | 10 | $\frac{44116 y_{1}^{2}}{43} + \frac{40904 y_{1} y_{2}}{43}$ |
| 7 | 11 | $504 y_{1}^{3} + \frac{490656 y_{1}^{2} y_{2}}{43} + \frac{24856 y_{1} y_{2}^{2}}{43}$ |
| 8 | 3 | $1$ |
| 8 | 4 | $\frac{21}{43}$ |
| 8 | 5 | $\frac{64}{43}$ |
| 8 | 6 | $\frac{1253 y_{1}}{43}$ |
| 8 | 7 | $3 y_{2}$ |
| 8 | 8 | $\frac{924 y_{1}}{43}$ |
| 8 | 9 | $\frac{1512 y_{1}^{2}}{43} + \frac{7360 y_{1} y_{2}}{43}$ |
| 8 | 10 | $\frac{5292 y_{1}^{2}}{43} + \frac{37544 y_{1} y_{2}}{43}$ |
| 8 | 11 | $\frac{214488 y_{1}^{2} y_{2}}{43} + \frac{36504 y_{1} y_{2}^{2}}{43}$ |
| 9 | 6 | $1$ |
| 9 | 7 | $- \frac{21}{4}$ |
| 9 | 8 | $- \frac{43}{4}$ |
| 9 | 9 | $- \frac{161 y_{1}}{2}$ |
| 9 | 10 | $- \frac{1253 y_{1}}{4} + 9 y_{2}$ |
| 9 | 11 | $- 378 y_{1}^{2} - 660 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 10 | 6 | $1$ |
| 10 | 7 | $\frac{3}{2}$ |
| 10 | 8 | $\frac{9}{2}$ |
| 10 | 9 | $23 y_{1}$ |
| 10 | 10 | $\frac{179 y_{1}}{2}$ |
| 10 | 11 | $108 y_{1}^{2} + 264 y_{1} y_{2}$ |
| 11 | 9 | $1$ |
| 11 | 10 | $\frac{9}{2}$ |

Enumeration mode: positive; 26 curve classes including zero. Matrix computation time: 130.17 minutes.
Saved checks: matrix rank, basis, Poincare pairing, unit column, c1 homogeneity.

## PROD5-D04 --- spectrum and connection

**Specialization:**  $y_1=2,\ y_2=3$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$



$$
\det(xI-K^F)=p_{1}(x)^{6}\,p_{2}(x).
$$




$$
\begin{aligned}p_{1}(x)&=x - 18.\end{aligned}
$$




$$
\begin{aligned}p_{2}(x)&=x^{6} + 168 x^{5} - 76284 x^{4} + 8921700 x^{3} - 332007336 x^{2}\\&+4963631184 x - 26146096812.\end{aligned}
$$


Cyclic determinant: $\Delta=0$. The specialized operator is not cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 411.21778 | 0 | 7 | -18 | 0 |
| 2 | -96.120193 | -61.875008 | 8 | -18 | 0 |
| 3 | -96.120193 | 61.875008 | 9 | -18 | 0 |
| 4 | -18 | 0 | 10 | -17.918994 | -0.54579862 |
| 5 | -18 | 0 | 11 | -17.918994 | 0.54579862 |
| 6 | -18 | 0 | 12 | -15.139407 | 0 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | unresolved | unresolved | not computed |
| $p_{2}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
**Unresolved factor $p_{1}$:**  the eigenvalue 18 has a 2-dimensional kernel, so its generalized eigenspace is not a single Jordan block and the factor is not cyclic (check cyclic_determinant first).

**Search aliases:** PROD5-D04; dimension 5; fivefold; Complete intersection in a product of projective spaces; Fano; quantum cohomology; Gromov-Witten; Hodge diamond; quantum multiplication; connection exponents; Complete intersection of multidegrees (2,1), (1,3) in P³ × P⁴; product of projective spaces; regularized exponent multiset; repeated exponents.
