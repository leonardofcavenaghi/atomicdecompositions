---
title: "Complete intersection of multidegrees (2,2) in P³ × P³ — PROD5-B01"
description: Exact fan inputs, ordered ambient basis, symbolic quantum multiplication and saved computation notes for PROD5-B01.
---

# Complete intersection in \(\mathbb P^{3}\times \mathbb P^{3}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{3}\times \mathbb P^{3}\). Defining multidegrees in this factor order: `[[2, 2]]`.

Source identifier: **PROD5-B01**; see [CKP and HLM terminology](../sources.md). The presentation is verified by the [fan and divisor certificate](../../data/geometric-presentations.json).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index in source:** 2. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)

Saved record: **complete with notes**. Matrix coefficients are exact; connection-factor notes below are retained. This page transcribes a completed computation, without rerunning localization.

## PROD5-B01 --- construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{3}\times\mathbb P^{3}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 2]]
residual_product_degrees = [2, 2]
```

The residual product degrees give the anticanonical class. 
Related workbook IDs: [28].

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $2$, $(-K_X)^5=1280$, $e(X)=-128$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&1&&69&&69&&1&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=1$, $h^{3,2}=69$; even rank 12; odd rank 140.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, -1, -66)$.

```python
chern_numbers = {'c1_5': 1280, 'c1_3_c2': 1024, 'c1_c2_2': 832, 'c1_2_c3': 192, 'c2_c3': 160, 'c1_c4': 224, 'c5': -128}
```

### Exact software inputs

Executable input: `examples/fivefolds_positive/inputs/PROD5-B01.py`. Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

```python
rays = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [-1, -1, -1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, -1, -1, -1]]
cones = [[0, 1, 2, 4, 5, 6], [0, 1, 2, 4, 5, 7], [0, 1, 2, 4, 6, 7], [0, 1, 2, 5, 6, 7],
 [0, 1, 3, 4, 5, 6], [0, 1, 3, 4, 5, 7], [0, 1, 3, 4, 6, 7], [0, 1, 3, 5, 6, 7],
 [0, 2, 3, 4, 5, 6], [0, 2, 3, 4, 5, 7], [0, 2, 3, 4, 6, 7], [0, 2, 3, 5, 6, 7],
 [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7], [1, 2, 3, 4, 6, 7], [1, 2, 3, 5, 6, 7]]
K = [[2, 0, 0, 0, 2, 0, 0, 0]]
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

**Status:**  complete with notes. Snapshot: 2026-11-09 18:05 UTC.
Checkpoint directory: `examples/fivefolds_positive/batch_results/PROD5-B01/`.

### Computed quantum multiplication

Write $M=c_1(X)\star$ and use the ordered basis $e_0,\ldots,e_{11}$ below. Columns are images: $M e_j=\sum_i M_{ij}e_i$.

```python
basis = ['1', 'x4', 'x0', 'x4^2', 'x0^2', 'x0*x4', 'x4^3', 'x0^3', 'x0*x4^2', 'x0*x4^3', 'x0^3*x4', 'x0^2*x4^3']
```



$$
\mathrm{Gr}=\operatorname{diag}\!\left(- \frac{5}{2},- \frac{3}{2},- \frac{3}{2},- \frac{1}{2},- \frac{1}{2},- \frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{3}{2},\frac{3}{2},\frac{5}{2}\right).
$$


**Exact matrix:**  every nonzero entry is listed below; all omitted entries are zero. Indices are zero based. No Novikov specialization has been made in this table.

| Row $i$ | Column $j$ | $M_{ij}$ |
|---|---|---|
| Row $i$ | Column $j$ | $M_{ij}$ |
| 0 | 1 | $4 y_{1}$ |
| 0 | 2 | $4 y_{2}$ |
| 0 | 6 | $32 y_{1} y_{2}$ |
| 0 | 7 | $32 y_{1} y_{2}$ |
| 0 | 8 | $80 y_{1} y_{2}$ |
| 0 | 11 | $96 y_{1}^{2} y_{2} + 96 y_{1} y_{2}^{2}$ |
| 1 | 0 | $2$ |
| 1 | 3 | $4 y_{1}$ |
| 1 | 4 | $12 y_{2}$ |
| 1 | 5 | $4 y_{2}$ |
| 1 | 9 | $80 y_{1} y_{2}$ |
| 1 | 10 | $64 y_{1} y_{2}$ |
| 2 | 0 | $2$ |
| 2 | 3 | $12 y_{1}$ |
| 2 | 4 | $4 y_{2}$ |
| 2 | 5 | $4 y_{1}$ |
| 2 | 9 | $64 y_{1} y_{2}$ |
| 2 | 10 | $80 y_{1} y_{2}$ |
| 3 | 1 | $2$ |
| 3 | 7 | $8 y_{2}$ |
| 3 | 8 | $4 y_{2}$ |
| 3 | 11 | $32 y_{1} y_{2}$ |
| 4 | 2 | $2$ |
| 4 | 6 | $8 y_{1}$ |
| 4 | 8 | $12 y_{1}$ |
| 4 | 11 | $32 y_{1} y_{2}$ |
| 5 | 1 | $2$ |
| 5 | 2 | $2$ |
| 5 | 6 | $4 y_{1}$ |
| 5 | 7 | $4 y_{2}$ |
| 5 | 8 | $4 y_{1}$ |
| 5 | 11 | $48 y_{1} y_{2}$ |
| 6 | 3 | $2$ |
| 6 | 4 | $-2$ |
| 6 | 5 | $-2$ |
| 6 | 9 | $- 4 y_{1} + 4 y_{2}$ |
| 6 | 10 | $8 y_{2}$ |
| 7 | 4 | $4$ |
| 7 | 5 | $2$ |
| 7 | 9 | $12 y_{1}$ |
| 7 | 10 | $4 y_{1}$ |
| 8 | 3 | $2$ |
| 8 | 4 | $2$ |
| 8 | 5 | $4$ |
| 8 | 9 | $4 y_{1}$ |
| 8 | 10 | $4 y_{2}$ |
| 9 | 6 | $2$ |
| 9 | 8 | $4$ |
| 9 | 11 | $4 y_{2}$ |
| 10 | 7 | $2$ |
| 10 | 8 | $2$ |
| 10 | 11 | $4 y_{1}$ |
| 11 | 9 | $2$ |
| 11 | 10 | $2$ |

Enumeration mode: positive; 8 curve classes including zero. Matrix computation time: 1.48 minutes.
Saved checks: matrix rank, basis, Poincare pairing, unit column, c1 homogeneity.

## PROD5-B01 --- spectrum and connection

**Specialization:**  $y_1=2,\ y_2=3$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$



$$
\det(xI-K^F)=p_{1}(x)^{4}\,p_{2}(x).
$$




$$
\begin{aligned}p_{1}(x)&=x.\end{aligned}
$$




$$
\begin{aligned}p_{2}(x)&=x^{8} - 320 x^{6} - 170496 x^{4} - 15810560 x^{2} + 65536.\end{aligned}
$$


Cyclic determinant: $\Delta=0$. The specialized operator is not cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 25.105734 | 0 | 7 | 0.064380839 | 0 |
| 2 | -25.105734 | 0 | 8 | -0.064380839 | 0 |
| 3 | 1.271349 | -12.520677 | 9 | 0 | 0 |
| 4 | 1.271349 | 12.520677 | 10 | 0 | 0 |
| 5 | -1.271349 | -12.520677 | 11 | 0 | 0 |
| 6 | -1.271349 | 12.520677 | 12 | 0 | 0 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | unresolved | unresolved | not computed |
| $p_{2}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
**Unresolved factor $p_{1}$:**  the eigenvalue 0 has a 3-dimensional kernel, so its generalized eigenspace is not a single Jordan block and the factor is not cyclic (check cyclic_determinant first).

**Search aliases:** PROD5-B01; dimension 5; fivefold; Complete intersection in a product of projective spaces; Fano; quantum cohomology; Gromov-Witten; Hodge diamond; quantum multiplication; connection exponents; Complete intersection of multidegrees (2,2) in P³ × P³; product of projective spaces.
