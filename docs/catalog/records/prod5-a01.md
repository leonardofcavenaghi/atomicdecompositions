---
title: "Complete intersection of multidegrees (2,2) in P² × P⁴ — PROD5-A01"
description: Exact fan inputs, ordered ambient basis, symbolic quantum multiplication and saved computation notes for PROD5-A01.
---

# Complete intersection in \(\mathbb P^{2}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{2}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[2, 2]]`.

Source identifier: **PROD5-A01**; see [CKP and HLM terminology](../sources.md). The presentation is verified by the [fan and divisor certificate](../../data/geometric-presentations.json).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index in source:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)

Saved record: **complete**. Matrix coefficients are exact; connection-factor notes below are retained. This page transcribes a completed computation, without rerunning localization.

## PROD5-A01 --- construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{2}\times\mathbb P^{4}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 2]]
residual_product_degrees = [1, 3]
```

The residual product degrees give the anticanonical class. 
Related workbook IDs: [9, 68].

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=1350$, $e(X)=-58$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&0&&35&&35&&0&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=0$, $h^{3,2}=35$; even rank 12; odd rank 70.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, -2, -32)$.

```python
chern_numbers = {'c1_5': 1350, 'c1_3_c2': 1098, 'c1_c2_2': 822, 'c1_2_c3': 250, 'c2_c3': 200, 'c1_c4': 178, 'c5': -58}
```

### Exact software inputs

Executable input: `examples/fivefolds_positive/inputs/PROD5-A01.py`. Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

```python
rays = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [-1, -1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, -1, -1, -1, -1]]
cones = [[0, 1, 3, 4, 5, 6], [0, 1, 3, 4, 5, 7], [0, 1, 3, 4, 6, 7], [0, 1, 3, 5, 6, 7],
 [0, 1, 4, 5, 6, 7], [0, 2, 3, 4, 5, 6], [0, 2, 3, 4, 5, 7], [0, 2, 3, 4, 6, 7],
 [0, 2, 3, 5, 6, 7], [0, 2, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7],
 [1, 2, 3, 4, 6, 7], [1, 2, 3, 5, 6, 7], [1, 2, 4, 5, 6, 7]]
K = [[2, 0, 0, 2, 0, 0, 0, 0]]
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

**Status:**  complete. Snapshot: 2026-11-09 18:05 UTC.
Checkpoint directory: `examples/fivefolds_positive/batch_results/PROD5-A01/`.

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
| 0 | 2 | $4 y_{2}^{2}$ |
| 0 | 3 | $6 y_{1}$ |
| 0 | 6 | $80 y_{1} y_{2}$ |
| 0 | 7 | $80 y_{1} y_{2}$ |
| 0 | 8 | $32 y_{1} y_{2}$ |
| 0 | 9 | $160 y_{1} y_{2}^{2}$ |
| 0 | 10 | $440 y_{1} y_{2}^{2}$ |
| 0 | 11 | $384 y_{1} y_{2}^{3}$ |
| 1 | 0 | $3$ |
| 1 | 2 | $6 y_{2}$ |
| 1 | 4 | $4 y_{2}^{2}$ |
| 1 | 5 | $4 y_{2}^{2}$ |
| 1 | 6 | $6 y_{1}$ |
| 1 | 9 | $80 y_{1} y_{2}$ |
| 1 | 10 | $144 y_{1} y_{2}$ |
| 1 | 11 | $280 y_{1} y_{2}^{2}$ |
| 2 | 0 | $1$ |
| 2 | 6 | $18 y_{1}$ |
| 2 | 7 | $6 y_{1}$ |
| 2 | 9 | $64 y_{1} y_{2}$ |
| 2 | 10 | $144 y_{1} y_{2}$ |
| 2 | 11 | $160 y_{1} y_{2}^{2}$ |
| 3 | 1 | $3$ |
| 3 | 4 | $4 y_{2}$ |
| 3 | 5 | $6 y_{2}$ |
| 3 | 7 | $4 y_{2}^{2}$ |
| 3 | 8 | $4 y_{2}^{2}$ |
| 3 | 11 | $32 y_{1} y_{2}$ |
| 4 | 2 | $1$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 9 | $12 y_{1}$ |
| 4 | 10 | $18 y_{1}$ |
| 4 | 11 | $32 y_{1} y_{2}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $3$ |
| 5 | 4 | $2 y_{2}$ |
| 5 | 9 | $6 y_{1}$ |
| 5 | 10 | $6 y_{1}$ |
| 5 | 11 | $48 y_{1} y_{2}$ |
| 6 | 3 | $3$ |
| 6 | 7 | $6 y_{2}$ |
| 6 | 8 | $4 y_{2}$ |
| 6 | 10 | $4 y_{2}^{2}$ |
| 7 | 3 | $1$ |
| 7 | 5 | $3$ |
| 7 | 8 | $2 y_{2}$ |
| 8 | 4 | $3$ |
| 8 | 5 | $1$ |
| 8 | 8 | $- 2 y_{2}$ |
| 8 | 11 | $6 y_{1}$ |
| 9 | 6 | $3$ |
| 9 | 7 | $-1$ |
| 9 | 8 | $-3$ |
| 9 | 10 | $6 y_{2}$ |
| 9 | 11 | $4 y_{2}^{2}$ |
| 10 | 6 | $1$ |
| 10 | 7 | $4$ |
| 10 | 8 | $3$ |
| 11 | 9 | $1$ |
| 11 | 10 | $4$ |

Enumeration mode: positive; 10 curve classes including zero. Matrix computation time: 3.95 minutes.
Saved checks: matrix rank, basis, Poincare pairing, unit column, c1 homogeneity.

## PROD5-A01 --- spectrum and connection

**Specialization:**  $y_1=2,\ y_2=3$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$



$$
\det(xI-K^F)=p_{1}(x)^{3}\,p_{2}(x).
$$




$$
\begin{aligned}p_{1}(x)&=x - 6.\end{aligned}
$$




$$
\begin{aligned}p_{2}(x)&=x^{9} + 6 x^{8} - 144 x^{7} - 216 x^{6} - 176256 x^{5} + 6850080 x^{4}\\&- 99116352 x^{3} + 704153088 x^{2} - 2492052480 x + 3546878976.\end{aligned}
$$


Cyclic determinant: $\Delta=-9627879200246720310068419083055793112346911571968$. The specialized operator is cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 30.187489 | 0 | 7 | -6.1667914 | 1.3698449 |
| 2 | 9.4559282 | -22.11354 | 8 | -6 | 0 |
| 3 | 9.4559282 | 22.11354 | 9 | -6 | 0 |
| 4 | -9.8876231 | -7.4197467 | 10 | -6 | 0 |
| 5 | -9.8876231 | 7.4197467 | 11 | -5.495258 | -1.7638941 |
| 6 | -6.1667914 | -1.3698449 | 12 | -5.495258 | 1.7638941 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | $-1,\ -1,\ -1$ | $0,\ 0,\ 0$ | complete / recursion |
| $p_{2}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
Recursion obstruction for $p_{1}$: $\frac{\left(s + 1\right)^{3}}{144}$.

**Search aliases:** PROD5-A01; dimension 5; fivefold; Complete intersection in a product of projective spaces; Fano; quantum cohomology; Gromov-Witten; Hodge diamond; quantum multiplication; connection exponents; Complete intersection of multidegrees (2,2) in P² × P⁴; product of projective spaces.
