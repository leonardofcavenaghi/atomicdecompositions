---
title: "Complete intersection of multidegrees (2,3) in P² × P⁴ — PROD5-A02"
description: Exact fan inputs, ordered ambient basis, symbolic quantum multiplication and saved computation notes for PROD5-A02.
---

# Complete intersection in \(\mathbb P^{2}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{2}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[2, 3]]`.

Source identifier: **PROD5-A02**; see [CKP and HLM terminology](../sources.md). The presentation is verified by the [fan and divisor certificate](../../data/geometric-presentations.json).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index in source:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)

Saved record: **complete with notes**. Matrix coefficients are exact; connection-factor notes below are retained. This page transcribes a completed computation, without rerunning localization.

## PROD5-A02 --- construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{2}\times\mathbb P^{4}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 3]]
residual_product_degrees = [1, 2]
```

The residual product degrees give the anticanonical class. 
Related workbook IDs: [11, 69].

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=400$, $e(X)=-818$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&15&&400&&400&&15&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=15$, $h^{3,2}=400$; even rank 12; odd rank 830.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 13, -397)$.

```python
chern_numbers = {'c1_5': 400, 'c1_3_c2': 608, 'c1_c2_2': 912, 'c1_2_c3': -110, 'c2_c3': -150, 'c1_c4': 578, 'c5': -818}
```

### Exact software inputs

Executable input: `examples/fivefolds_positive/inputs/PROD5-A02.py`. Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

```python
rays = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [-1, -1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, -1, -1, -1, -1]]
cones = [[0, 1, 3, 4, 5, 6], [0, 1, 3, 4, 5, 7], [0, 1, 3, 4, 6, 7], [0, 1, 3, 5, 6, 7],
 [0, 1, 4, 5, 6, 7], [0, 2, 3, 4, 5, 6], [0, 2, 3, 4, 5, 7], [0, 2, 3, 4, 6, 7],
 [0, 2, 3, 5, 6, 7], [0, 2, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7],
 [1, 2, 3, 4, 6, 7], [1, 2, 3, 5, 6, 7], [1, 2, 4, 5, 6, 7]]
K = [[2, 0, 0, 3, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

### Ordered basis and curve conventions

```python
ambient_basis = ['1', 'x3', 'x0', 'x3^2', 'x0^2', 'x0*x3', 'x3^3', 'x0*x3^2', 'x0^2*x3', 'x3^4',
 'x0*x3^3', 'x0*x3^4']
ambient_rank = 12
novikov_divisors = [[0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
h2_basis = [[1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1]]
```

### Computation record

**Status:**  complete with notes. Snapshot: 2026-11-09 18:05 UTC.
Checkpoint directory: `examples/fivefolds_positive/batch_results/PROD5-A02/`.

### Computed quantum multiplication

Write $M=c_1(X)\star$ and use the ordered basis $e_0,\ldots,e_{11}$ below. Columns are images: $M e_j=\sum_i M_{ij}e_i$.

```python
basis = ['1', 'x3', 'x0', 'x3^2', 'x0^2', 'x0*x3', 'x3^3', 'x0*x3^2', 'x0^2*x3', 'x3^4', 'x0*x3^3', 'x0*x3^4']
```



$$
\mathrm{Gr}=\operatorname{diag}\!\left(- \frac{5}{2},- \frac{3}{2},- \frac{3}{2},- \frac{1}{2},- \frac{1}{2},- \frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{3}{2},\frac{3}{2},\frac{5}{2}\right).
$$


**Exact matrix:**  every nonzero entry is listed below; all omitted entries are zero. Indices are zero based. No Novikov specialization has been made in this table.

| Row $i$ | Column $j$ | $M_{ij}$ |
|---|---|---|
| Row $i$ | Column $j$ | $M_{ij}$ |
| 0 | 1 | $12 y_{1}$ |
| 0 | 2 | $4 y_{2}^{2}$ |
| 0 | 3 | $324 y_{1} y_{2}$ |
| 0 | 4 | $162 y_{1} y_{2}$ |
| 0 | 5 | $324 y_{1} y_{2}$ |
| 0 | 6 | $72 y_{1}^{2} + 1408 y_{1} y_{2}^{2}$ |
| 0 | 7 | $3168 y_{1} y_{2}^{2}$ |
| 0 | 8 | $2448 y_{1} y_{2}^{2}$ |
| 0 | 9 | $4320 y_{1}^{2} y_{2} + 1280 y_{1} y_{2}^{3}$ |
| 0 | 10 | $10260 y_{1}^{2} y_{2} + 6720 y_{1} y_{2}^{3}$ |
| 0 | 11 | $48384 y_{1}^{2} y_{2}^{2} + 3072 y_{1} y_{2}^{4}$ |
| 1 | 0 | $2$ |
| 1 | 2 | $9 y_{2}$ |
| 1 | 3 | $30 y_{1}$ |
| 1 | 4 | $6 y_{2}^{2}$ |
| 1 | 5 | $4 y_{2}^{2}$ |
| 1 | 6 | $864 y_{1} y_{2}$ |
| 1 | 7 | $1134 y_{1} y_{2}$ |
| 1 | 8 | $567 y_{1} y_{2}$ |
| 1 | 9 | $1664 y_{1} y_{2}^{2}$ |
| 1 | 10 | $6720 y_{1} y_{2}^{2}$ |
| 1 | 11 | $3780 y_{1}^{2} y_{2} + 4800 y_{1} y_{2}^{3}$ |
| 2 | 0 | $1$ |
| 2 | 3 | $44 y_{1}$ |
| 2 | 5 | $12 y_{1}$ |
| 2 | 6 | $432 y_{1} y_{2}$ |
| 2 | 7 | $756 y_{1} y_{2}$ |
| 2 | 8 | $486 y_{1} y_{2}$ |
| 2 | 9 | $48 y_{1}^{2} + 512 y_{1} y_{2}^{2}$ |
| 2 | 10 | $72 y_{1}^{2} + 2432 y_{1} y_{2}^{2}$ |
| 2 | 11 | $4320 y_{1}^{2} y_{2} + 1280 y_{1} y_{2}^{3}$ |
| 3 | 1 | $2$ |
| 3 | 4 | $9 y_{2}$ |
| 3 | 5 | $9 y_{2}$ |
| 3 | 6 | $12 y_{1}$ |
| 3 | 7 | $4 y_{2}^{2}$ |
| 3 | 8 | $6 y_{2}^{2}$ |
| 3 | 9 | $324 y_{1} y_{2}$ |
| 3 | 10 | $864 y_{1} y_{2}$ |
| 3 | 11 | $1632 y_{1} y_{2}^{2}$ |
| 4 | 2 | $1$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 6 | $48 y_{1}$ |
| 4 | 7 | $44 y_{1}$ |
| 4 | 8 | $12 y_{1}$ |
| 4 | 9 | $96 y_{1} y_{2}$ |
| 4 | 10 | $384 y_{1} y_{2}$ |
| 4 | 11 | $48 y_{1}^{2} + 256 y_{1} y_{2}^{2}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $2$ |
| 5 | 4 | $3 y_{2}$ |
| 5 | 6 | $56 y_{1}$ |
| 5 | 7 | $30 y_{1}$ |
| 5 | 9 | $288 y_{1} y_{2}$ |
| 5 | 10 | $936 y_{1} y_{2}$ |
| 5 | 11 | $1024 y_{1} y_{2}^{2}$ |
| 6 | 3 | $2$ |
| 6 | 7 | $9 y_{2}$ |
| 6 | 8 | $9 y_{2}$ |
| 6 | 10 | $4 y_{2}^{2}$ |
| 6 | 11 | $108 y_{1} y_{2}$ |
| 7 | 3 | $1$ |
| 7 | 5 | $2$ |
| 7 | 8 | $3 y_{2}$ |
| 7 | 9 | $8 y_{1}$ |
| 7 | 10 | $12 y_{1}$ |
| 7 | 11 | $144 y_{1} y_{2}$ |
| 8 | 4 | $2$ |
| 8 | 5 | $1$ |
| 8 | 8 | $- 2 y_{2}$ |
| 8 | 9 | $24 y_{1}$ |
| 8 | 10 | $56 y_{1}$ |
| 8 | 11 | $120 y_{1} y_{2}$ |
| 9 | 6 | $2$ |
| 9 | 7 | $- \frac{9}{4}$ |
| 9 | 8 | $- \frac{9}{2}$ |
| 9 | 10 | $9 y_{2}$ |
| 9 | 11 | $- 18 y_{1} + 4 y_{2}^{2}$ |
| 10 | 6 | $1$ |
| 10 | 7 | $\frac{7}{2}$ |
| 10 | 8 | $3$ |
| 10 | 11 | $12 y_{1}$ |
| 11 | 9 | $1$ |
| 11 | 10 | $\frac{7}{2}$ |

Enumeration mode: positive; 14 curve classes including zero. Matrix computation time: 9.44 minutes.
Saved checks: matrix rank, basis, Poincare pairing, unit column, c1 homogeneity.

## PROD5-A02 --- spectrum and connection

**Specialization:**  $y_1=2,\ y_2=3$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$



$$
\det(xI-K^F)=p_{1}(x)^{6}\,p_{2}(x).
$$




$$
\begin{aligned}p_{1}(x)&=x - 6.\end{aligned}
$$




$$
\begin{aligned}p_{2}(x)&=x^{6} + 24 x^{5} - 468 x^{4} + 243324 x^{3} - 8079912 x^{2} + 91955952 x\\&-323829900.\end{aligned}
$$


Cyclic determinant: $\Delta=0$. The specialized operator is not cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 82.259346 | 0 | 7 | -6 | 0 |
| 2 | -12.838225 | -54.408342 | 8 | -6 | 0 |
| 3 | -12.838225 | 54.408342 | 9 | -6 | 0 |
| 4 | -13.008188 | -4.7565607 | 10 | -6 | 0 |
| 5 | -13.008188 | 4.7565607 | 11 | -6 | 0 |
| 6 | -6.5665194 | 0 | 12 | -6 | 0 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | unresolved | unresolved | not computed |
| $p_{2}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
**Unresolved factor $p_{1}$:**  the eigenvalue 6 has a 2-dimensional kernel, so its generalized eigenspace is not a single Jordan block and the factor is not cyclic (check cyclic_determinant first).

**Search aliases:** PROD5-A02; dimension 5; fivefold; Complete intersection in a product of projective spaces; Fano; quantum cohomology; Gromov-Witten; Hodge diamond; quantum multiplication; connection exponents; Complete intersection of multidegrees (2,3) in P² × P⁴; product of projective spaces.
