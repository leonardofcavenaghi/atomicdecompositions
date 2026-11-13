---
title: "Complete intersection of multidegrees (2,2), (1,1), (1,1) in P⁴ × P⁴ — PROD5-E01"
description: Exact fan inputs, ordered ambient basis, symbolic quantum multiplication and saved computation notes for PROD5-E01.
---

# Complete intersection in \(\mathbb P^{4}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{4}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[2, 2], [1, 1], [1, 1]]`.

Source identifier: **PROD5-E01**; see [CKP and HLM terminology](../sources.md). The presentation is verified by the [fan and divisor certificate](../../data/geometric-presentations.json).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index in source:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)

Saved record: **complete with notes**. Matrix coefficients are exact; connection-factor notes below are retained. This page transcribes a completed computation, without rerunning localization.

<!-- saved-exponent-summary:start -->
## Regularized exponent multisets

Analysis point: `y1=2, y2=3`. These lists describe the computed ambient connection. Every row applies **separately to each eigenvalue** satisfying the displayed condition; repeated entries retain their multiplicity.

The characteristic factors below use \(K^F=-A\), so an eigenvalue \(\lambda\) of \(A=c_1\star\) satisfies \(p_i(-\lambda)=0\). The classes are powers modulo \(\mathbb Z\); their order does not pair them term by term with the powers.

| Spectral condition | Multiplicity per eigenvalue | \(F_{b,\lambda}\) | Saved computation |
|---|---:|---|---|
| \(p_{1}(-\lambda)=0\) | 7 | Unresolved | Unresolved |
| \(p_{2}(-\lambda)=0\) | 1 | \(\{\!\{0\}\!\}\) | Complete |

Unresolved factors have no computed multiset here. These ambient data alone do not identify full atoms or establish a rationality result. See the [connection conventions](../../toric/mathematics.md).
<!-- saved-exponent-summary:end -->

## PROD5-E01 --- construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{4}\times\mathbb P^{4}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 2], [1, 1], [1, 1]]
residual_product_degrees = [1, 1]
```

The residual product degrees give the anticanonical class. 
Related workbook IDs: [111].

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=140$, $e(X)=-1080$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&25&&521&&521&&25&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=25$, $h^{3,2}=521$; even rank 12; odd rank 1092.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 23, -518)$.

```python
chern_numbers = {'c1_5': 140, 'c1_3_c2': 340, 'c1_c2_2': 840, 'c1_2_c3': -140, 'c2_c3': -340, 'c1_c4': 600, 'c5': -1080}
```

### Exact software inputs

Executable input: `examples/fivefolds_positive/inputs/PROD5-E01.py`. Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

```python
rays = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 0], [-1, -1, -1, -1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, -1, -1, -1, -1]]
cones = [[0, 1, 2, 3, 5, 6, 7, 8], [0, 1, 2, 3, 5, 6, 7, 9], [0, 1, 2, 3, 5, 6, 8, 9],
 [0, 1, 2, 3, 5, 7, 8, 9], [0, 1, 2, 3, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8],
 [0, 1, 2, 4, 5, 6, 7, 9], [0, 1, 2, 4, 5, 6, 8, 9], [0, 1, 2, 4, 5, 7, 8, 9],
 [0, 1, 2, 4, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8], [0, 1, 3, 4, 5, 6, 7, 9],
 [0, 1, 3, 4, 5, 6, 8, 9], [0, 1, 3, 4, 5, 7, 8, 9], [0, 1, 3, 4, 6, 7, 8, 9],
 [0, 2, 3, 4, 5, 6, 7, 8], [0, 2, 3, 4, 5, 6, 7, 9], [0, 2, 3, 4, 5, 6, 8, 9],
 [0, 2, 3, 4, 5, 7, 8, 9], [0, 2, 3, 4, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8],
 [1, 2, 3, 4, 5, 6, 7, 9], [1, 2, 3, 4, 5, 6, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9],
 [1, 2, 3, 4, 6, 7, 8, 9]]
K = [[2, 0, 0, 0, 0, 2, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

### Ordered basis and curve conventions

```python
ambient_basis = ['1', 'x5', 'x0', 'x5^2', 'x0^2', 'x0*x5', 'x5^3', 'x0^3', 'x0*x5^2', 'x5^4', 'x0^4',
 'x0*x5^4']
ambient_rank = 12
novikov_divisors = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
h2_basis = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]
```

### Computation record

**Status:**  complete with notes. Snapshot: 2026-11-09 18:05 UTC.
Checkpoint directory: `examples/fivefolds_positive/batch_results/PROD5-E01/`.

### Computed quantum multiplication

Write $M=c_1(X)\star$ and use the ordered basis $e_0,\ldots,e_{11}$ below. Columns are images: $M e_j=\sum_i M_{ij}e_i$.

```python
basis = ['1', 'x5', 'x0', 'x5^2', 'x0^2', 'x0*x5', 'x5^3', 'x0^3', 'x0*x5^2', 'x5^4', 'x0^4', 'x0*x5^4']
```



$$
\mathrm{Gr}=\operatorname{diag}\!\left(- \frac{5}{2},- \frac{3}{2},- \frac{3}{2},- \frac{1}{2},- \frac{1}{2},- \frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{3}{2},\frac{3}{2},\frac{5}{2}\right).
$$


**Exact matrix:**  every nonzero entry is listed below; all omitted entries are zero. Indices are zero based. No Novikov specialization has been made in this table.

| Row $i$ | Column $j$ | $M_{ij}$ |
|---|---|---|
| Row $i$ | Column $j$ | $M_{ij}$ |
| 0 | 1 | $4 y_{1}^{2} + 184 y_{1} y_{2}$ |
| 0 | 2 | $184 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 0 | 3 | $4680 y_{1}^{2} y_{2} + 1800 y_{1} y_{2}^{2}$ |
| 0 | 4 | $1800 y_{1}^{2} y_{2} + 4680 y_{1} y_{2}^{2}$ |
| 0 | 5 | $3720 y_{1}^{2} y_{2} + 3720 y_{1} y_{2}^{2}$ |
| 0 | 6 | $21056 y_{1}^{3} y_{2} + 160768 y_{1}^{2} y_{2}^{2} + 4352 y_{1} y_{2}^{3}$ |
| 0 | 7 | $4352 y_{1}^{3} y_{2} + 160768 y_{1}^{2} y_{2}^{2} + 21056 y_{1} y_{2}^{3}$ |
| 0 | 8 | $27200 y_{1}^{3} y_{2} + 298144 y_{1}^{2} y_{2}^{2} + 16064 y_{1} y_{2}^{3}$ |
| 0 | 9 | $12160 y_{1}^{4} y_{2} + 959520 y_{1}^{3} y_{2}^{2} + 597120 y_{1}^{2} y_{2}^{3} + 2560 y_{1} y_{2}^{4}$ |
| 0 | 10 | $2560 y_{1}^{4} y_{2} + 597120 y_{1}^{3} y_{2}^{2} + 959520 y_{1}^{2} y_{2}^{3} + 12160 y_{1} y_{2}^{4}$ |
| 0 | 11 | $6144 y_{1}^{5} y_{2} + 3153600 y_{1}^{4} y_{2}^{2} + 18995712 y_{1}^{3} y_{2}^{3} + 3153600 y_{1}^{2} y_{2}^{4} + 6144 y_{1} y_{2}^{5}$ |
| 1 | 0 | $1$ |
| 1 | 2 | $10 y_{2}$ |
| 1 | 3 | $544 y_{1} y_{2}$ |
| 1 | 4 | $376 y_{1} y_{2} + 12 y_{2}^{2}$ |
| 1 | 5 | $560 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 1 | 6 | $5400 y_{1}^{2} y_{2} + 4080 y_{1} y_{2}^{2}$ |
| 1 | 7 | $1440 y_{1}^{2} y_{2} + 10200 y_{1} y_{2}^{2}$ |
| 1 | 8 | $7320 y_{1}^{2} y_{2} + 10920 y_{1} y_{2}^{2}$ |
| 1 | 9 | $4352 y_{1}^{3} y_{2} + 96064 y_{1}^{2} y_{2}^{2} + 4352 y_{1} y_{2}^{3}$ |
| 1 | 10 | $1024 y_{1}^{3} y_{2} + 82912 y_{1}^{2} y_{2}^{2} + 14208 y_{1} y_{2}^{3}$ |
| 1 | 11 | $2560 y_{1}^{4} y_{2} + 597120 y_{1}^{3} y_{2}^{2} + 959520 y_{1}^{2} y_{2}^{3} + 12160 y_{1} y_{2}^{4}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $10 y_{1}$ |
| 2 | 3 | $12 y_{1}^{2} + 376 y_{1} y_{2}$ |
| 2 | 4 | $544 y_{1} y_{2}$ |
| 2 | 5 | $4 y_{1}^{2} + 560 y_{1} y_{2}$ |
| 2 | 6 | $10200 y_{1}^{2} y_{2} + 1440 y_{1} y_{2}^{2}$ |
| 2 | 7 | $4080 y_{1}^{2} y_{2} + 5400 y_{1} y_{2}^{2}$ |
| 2 | 8 | $15000 y_{1}^{2} y_{2} + 4680 y_{1} y_{2}^{2}$ |
| 2 | 9 | $14208 y_{1}^{3} y_{2} + 82912 y_{1}^{2} y_{2}^{2} + 1024 y_{1} y_{2}^{3}$ |
| 2 | 10 | $4352 y_{1}^{3} y_{2} + 96064 y_{1}^{2} y_{2}^{2} + 4352 y_{1} y_{2}^{3}$ |
| 2 | 11 | $12160 y_{1}^{4} y_{2} + 959520 y_{1}^{3} y_{2}^{2} + 597120 y_{1}^{2} y_{2}^{3} + 2560 y_{1} y_{2}^{4}$ |
| 3 | 1 | $1$ |
| 3 | 3 | $- 2 y_{1}$ |
| 3 | 4 | $18 y_{2}$ |
| 3 | 5 | $10 y_{2}$ |
| 3 | 6 | $432 y_{1} y_{2}$ |
| 3 | 7 | $192 y_{1} y_{2} + 12 y_{2}^{2}$ |
| 3 | 8 | $656 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 3 | 9 | $672 y_{1}^{2} y_{2} + 1512 y_{1} y_{2}^{2}$ |
| 3 | 10 | $192 y_{1}^{2} y_{2} + 2712 y_{1} y_{2}^{2}$ |
| 3 | 11 | $512 y_{1}^{3} y_{2} + 36832 y_{1}^{2} y_{2}^{2} + 6080 y_{1} y_{2}^{3}$ |
| 4 | 2 | $1$ |
| 4 | 3 | $18 y_{1}$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 5 | $10 y_{1}$ |
| 4 | 6 | $12 y_{1}^{2} + 192 y_{1} y_{2}$ |
| 4 | 7 | $432 y_{1} y_{2}$ |
| 4 | 8 | $12 y_{1}^{2} + 496 y_{1} y_{2}$ |
| 4 | 9 | $2712 y_{1}^{2} y_{2} + 192 y_{1} y_{2}^{2}$ |
| 4 | 10 | $1512 y_{1}^{2} y_{2} + 672 y_{1} y_{2}^{2}$ |
| 4 | 11 | $6080 y_{1}^{3} y_{2} + 36832 y_{1}^{2} y_{2}^{2} + 512 y_{1} y_{2}^{3}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $1$ |
| 5 | 3 | $6 y_{1}$ |
| 5 | 4 | $6 y_{2}$ |
| 5 | 6 | $432 y_{1} y_{2}$ |
| 5 | 7 | $432 y_{1} y_{2}$ |
| 5 | 8 | $816 y_{1} y_{2}$ |
| 5 | 9 | $2064 y_{1}^{2} y_{2} + 864 y_{1} y_{2}^{2}$ |
| 5 | 10 | $864 y_{1}^{2} y_{2} + 2064 y_{1} y_{2}^{2}$ |
| 5 | 11 | $2816 y_{1}^{3} y_{2} + 50272 y_{1}^{2} y_{2}^{2} + 2816 y_{1} y_{2}^{3}$ |
| 6 | 3 | $1$ |
| 6 | 4 | $- \frac{2}{3}$ |
| 6 | 5 | $- \frac{2}{3}$ |
| 6 | 6 | $- 6 y_{1}$ |
| 6 | 7 | $14 y_{2}$ |
| 6 | 8 | $- 4 y_{1} + 10 y_{2}$ |
| 6 | 9 | $\frac{88 y_{1} y_{2}}{3}$ |
| 6 | 10 | $- \frac{80 y_{1} y_{2}}{3} + 4 y_{2}^{2}$ |
| 6 | 11 | $- 336 y_{1}^{2} y_{2} + 624 y_{1} y_{2}^{2}$ |
| 7 | 4 | $\frac{5}{3}$ |
| 7 | 5 | $\frac{2}{3}$ |
| 7 | 6 | $18 y_{1}$ |
| 7 | 7 | $- 2 y_{2}$ |
| 7 | 8 | $22 y_{1}$ |
| 7 | 9 | $4 y_{1}^{2} + \frac{224 y_{1} y_{2}}{3}$ |
| 7 | 10 | $\frac{392 y_{1} y_{2}}{3}$ |
| 7 | 11 | $1248 y_{1}^{2} y_{2} + 288 y_{1} y_{2}^{2}$ |
| 8 | 3 | $1$ |
| 8 | 4 | $1$ |
| 8 | 5 | $2$ |
| 8 | 6 | $6 y_{1}$ |
| 8 | 7 | $6 y_{2}$ |
| 8 | 8 | $4 y_{1}$ |
| 8 | 9 | $152 y_{1} y_{2}$ |
| 8 | 10 | $152 y_{1} y_{2}$ |
| 8 | 11 | $936 y_{1}^{2} y_{2} + 936 y_{1} y_{2}^{2}$ |
| 9 | 6 | $4$ |
| 9 | 7 | $1$ |
| 9 | 8 | $6$ |
| 9 | 10 | $10 y_{2}$ |
| 9 | 11 | $184 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 10 | 6 | $1$ |
| 10 | 7 | $4$ |
| 10 | 8 | $4$ |
| 10 | 9 | $10 y_{1}$ |
| 10 | 11 | $4 y_{1}^{2} + 184 y_{1} y_{2}$ |
| 11 | 9 | $1$ |
| 11 | 10 | $1$ |

Enumeration mode: positive; 26 curve classes including zero. Matrix computation time: 282.46 minutes.
Saved checks: matrix rank, basis, Poincare pairing, unit column, c1 homogeneity.

## PROD5-E01 --- spectrum and connection

**Specialization:**  $y_1=2,\ y_2=3$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$



$$
\det(xI-K^F)=p_{1}(x)^{7}\,p_{2}(x).
$$




$$
\begin{aligned}p_{1}(x)&=x - 10.\end{aligned}
$$




$$
\begin{aligned}p_{2}(x)&=x^{5} + 50 x^{4} - 59000 x^{3} + 5410000 x^{2} - 85150000 x\\&+372100000.\end{aligned}
$$


Cyclic determinant: $\Delta=0$. The specialized operator is not cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 304.82563 | 0 | 7 | -10 | 0 |
| 2 | -118.16301 | -16.034351 | 8 | -10 | 0 |
| 3 | -118.16301 | 16.034351 | 9 | -10 | 0 |
| 4 | -10 | 0 | 10 | -10 | 0 |
| 5 | -10 | 0 | 11 | -9.2498019 | -0.53602781 |
| 6 | -10 | 0 | 12 | -9.2498019 | 0.53602781 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | unresolved | unresolved | not computed |
| $p_{2}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
**Unresolved factor $p_{1}$:**  the eigenvalue 10 has a 3-dimensional kernel, so its generalized eigenspace is not a single Jordan block and the factor is not cyclic (check cyclic_determinant first).

**Search aliases:** PROD5-E01; dimension 5; fivefold; Complete intersection in a product of projective spaces; Fano; quantum cohomology; Gromov-Witten; Hodge diamond; quantum multiplication; connection exponents; Complete intersection of multidegrees (2,2), (1,1), (1,1) in P⁴ × P⁴; product of projective spaces; regularized exponent multiset; repeated exponents.
