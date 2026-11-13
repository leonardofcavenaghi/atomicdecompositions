---
title: "Complete intersection of multidegrees (2,2), (1,2) in P³ × P⁴ — PROD5-D05"
description: Exact fan inputs, ordered ambient basis, symbolic quantum multiplication and saved computation notes for PROD5-D05.
---

# Complete intersection in \(\mathbb P^{3}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{3}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[2, 2], [1, 2]]`.

Source identifier: **PROD5-D05**; see [CKP and HLM terminology](../sources.md). The presentation is verified by the [fan and divisor certificate](../../data/geometric-presentations.json).

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

## PROD5-D05 --- construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{3}\times\mathbb P^{4}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 2], [1, 2]]
residual_product_degrees = [1, 1]
```

The residual product degrees give the anticanonical class. 
Related workbook IDs: [54, 97].

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=110$, $e(X)=-1058$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&25&&510&&510&&25&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=25$, $h^{3,2}=510$; even rank 12; odd rank 1070.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 23, -507)$.

```python
chern_numbers = {'c1_5': 110, 'c1_3_c2': 298, 'c1_c2_2': 818, 'c1_2_c3': -138, 'c2_c3': -368, 'c1_c4': 578, 'c5': -1058}
```

### Exact software inputs

Executable input: `examples/fivefolds_positive/inputs/PROD5-D05.py`. Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

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
K = [[2, 0, 0, 0, 2, 0, 0, 0, 0], [1, 0, 0, 0, 2, 0, 0, 0, 0]]
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
Checkpoint directory: `examples/fivefolds_positive/batch_results/PROD5-D05/`.

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
| 0 | 1 | $40 y_{1}^{2} + 272 y_{1} y_{2}$ |
| 0 | 2 | $272 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 0 | 3 | $192 y_{1}^{3} + 16464 y_{1}^{2} y_{2} + 2280 y_{1} y_{2}^{2}$ |
| 0 | 4 | $5760 y_{1}^{2} y_{2} + 5472 y_{1} y_{2}^{2}$ |
| 0 | 5 | $12720 y_{1}^{2} y_{2} + 4776 y_{1} y_{2}^{2}$ |
| 0 | 6 | $253696 y_{1}^{3} y_{2} + 396064 y_{1}^{2} y_{2}^{2} + 4864 y_{1} y_{2}^{3}$ |
| 0 | 7 | $28672 y_{1}^{3} y_{2} + 253312 y_{1}^{2} y_{2}^{2} + 15232 y_{1} y_{2}^{3}$ |
| 0 | 8 | $307712 y_{1}^{3} y_{2} + 754624 y_{1}^{2} y_{2}^{2} + 18624 y_{1} y_{2}^{3}$ |
| 0 | 9 | $555520 y_{1}^{4} y_{2} + 5731840 y_{1}^{3} y_{2}^{2} + 1141920 y_{1}^{2} y_{2}^{3} + 2560 y_{1} y_{2}^{4}$ |
| 0 | 10 | $1881600 y_{1}^{4} y_{2} + 22366400 y_{1}^{3} y_{2}^{2} + 5648800 y_{1}^{2} y_{2}^{3} + 21120 y_{1} y_{2}^{4}$ |
| 0 | 11 | $1204224 y_{1}^{5} y_{2} + 59013888 y_{1}^{4} y_{2}^{2} + 85209600 y_{1}^{3} y_{2}^{3} + 5550144 y_{1}^{2} y_{2}^{4} + 6144 y_{1} y_{2}^{5}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $4 y_{1}$ |
| 1 | 2 | $10 y_{2}$ |
| 1 | 3 | $40 y_{1}^{2} + 904 y_{1} y_{2}$ |
| 1 | 4 | $640 y_{1} y_{2} + 12 y_{2}^{2}$ |
| 1 | 5 | $992 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 1 | 6 | $27720 y_{1}^{2} y_{2} + 5328 y_{1} y_{2}^{2}$ |
| 1 | 7 | $4608 y_{1}^{2} y_{2} + 8688 y_{1} y_{2}^{2}$ |
| 1 | 8 | $36912 y_{1}^{2} y_{2} + 14952 y_{1} y_{2}^{2}$ |
| 1 | 9 | $84992 y_{1}^{3} y_{2} + 273120 y_{1}^{2} y_{2}^{2} + 4864 y_{1} y_{2}^{3}$ |
| 1 | 10 | $291840 y_{1}^{3} y_{2} + 1150752 y_{1}^{2} y_{2}^{2} + 32640 y_{1} y_{2}^{3}$ |
| 1 | 11 | $215040 y_{1}^{4} y_{2} + 5170880 y_{1}^{3} y_{2}^{2} + 2223040 y_{1}^{2} y_{2}^{3} + 13440 y_{1} y_{2}^{4}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $18 y_{1}$ |
| 2 | 3 | $180 y_{1}^{2} + 504 y_{1} y_{2}$ |
| 2 | 4 | $688 y_{1} y_{2}$ |
| 2 | 5 | $40 y_{1}^{2} + 776 y_{1} y_{2}$ |
| 2 | 6 | $288 y_{1}^{3} + 32808 y_{1}^{2} y_{2} + 1632 y_{1} y_{2}^{2}$ |
| 2 | 7 | $8832 y_{1}^{2} y_{2} + 3984 y_{1} y_{2}^{2}$ |
| 2 | 8 | $192 y_{1}^{3} + 49080 y_{1}^{2} y_{2} + 5544 y_{1} y_{2}^{2}$ |
| 2 | 9 | $158976 y_{1}^{3} y_{2} + 181792 y_{1}^{2} y_{2}^{2} + 1024 y_{1} y_{2}^{3}$ |
| 2 | 10 | $561920 y_{1}^{3} y_{2} + 818496 y_{1}^{2} y_{2}^{2} + 7936 y_{1} y_{2}^{3}$ |
| 2 | 11 | $555520 y_{1}^{4} y_{2} + 5731840 y_{1}^{3} y_{2}^{2} + 1141920 y_{1}^{2} y_{2}^{3} + 2560 y_{1} y_{2}^{4}$ |
| 3 | 1 | $1$ |
| 3 | 4 | $16 y_{2}$ |
| 3 | 5 | $10 y_{2}$ |
| 3 | 6 | $760 y_{1} y_{2}$ |
| 3 | 7 | $256 y_{1} y_{2} + 8 y_{2}^{2}$ |
| 3 | 8 | $1232 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 3 | 9 | $4416 y_{1}^{2} y_{2} + 1992 y_{1} y_{2}^{2}$ |
| 3 | 10 | $15552 y_{1}^{2} y_{2} + 10320 y_{1} y_{2}^{2}$ |
| 3 | 11 | $14336 y_{1}^{3} y_{2} + 126656 y_{1}^{2} y_{2}^{2} + 7616 y_{1} y_{2}^{3}$ |
| 4 | 2 | $1$ |
| 4 | 3 | $28 y_{1}$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 5 | $18 y_{1}$ |
| 4 | 6 | $200 y_{1}^{2} + 224 y_{1} y_{2}$ |
| 4 | 7 | $336 y_{1} y_{2}$ |
| 4 | 8 | $180 y_{1}^{2} + 616 y_{1} y_{2}$ |
| 4 | 9 | $96 y_{1}^{3} + 7680 y_{1}^{2} y_{2} + 192 y_{1} y_{2}^{2}$ |
| 4 | 10 | $288 y_{1}^{3} + 29976 y_{1}^{2} y_{2} + 1344 y_{1} y_{2}^{2}$ |
| 4 | 11 | $66816 y_{1}^{3} y_{2} + 80032 y_{1}^{2} y_{2}^{2} + 512 y_{1} y_{2}^{3}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $1$ |
| 5 | 3 | $24 y_{1}$ |
| 5 | 4 | $6 y_{2}$ |
| 5 | 5 | $4 y_{1}$ |
| 5 | 6 | $60 y_{1}^{2} + 688 y_{1} y_{2}$ |
| 5 | 7 | $512 y_{1} y_{2}$ |
| 5 | 8 | $40 y_{1}^{2} + 1424 y_{1} y_{2}$ |
| 5 | 9 | $9768 y_{1}^{2} y_{2} + 1056 y_{1} y_{2}^{2}$ |
| 5 | 10 | $36216 y_{1}^{2} y_{2} + 6192 y_{1} y_{2}^{2}$ |
| 5 | 11 | $53248 y_{1}^{3} y_{2} + 155968 y_{1}^{2} y_{2}^{2} + 3328 y_{1} y_{2}^{3}$ |
| 6 | 3 | $1$ |
| 6 | 4 | $- \frac{4}{7}$ |
| 6 | 5 | $- \frac{4}{7}$ |
| 6 | 6 | $- \frac{116 y_{1}}{7}$ |
| 6 | 7 | $8 y_{2}$ |
| 6 | 8 | $- \frac{96 y_{1}}{7} + 10 y_{2}$ |
| 6 | 9 | $- \frac{80 y_{1}^{2}}{7} + \frac{512 y_{1} y_{2}}{7}$ |
| 6 | 10 | $- \frac{240 y_{1}^{2}}{7} + \frac{1472 y_{1} y_{2}}{7} + 4 y_{2}^{2}$ |
| 6 | 11 | $- \frac{8160 y_{1}^{2} y_{2}}{7} + \frac{6864 y_{1} y_{2}^{2}}{7}$ |
| 7 | 4 | $\frac{29}{14}$ |
| 7 | 5 | $\frac{15}{14}$ |
| 7 | 6 | $\frac{291 y_{1}}{7}$ |
| 7 | 7 | $- 2 y_{2}$ |
| 7 | 8 | $\frac{376 y_{1}}{7}$ |
| 7 | 9 | $\frac{570 y_{1}^{2}}{7} + \frac{944 y_{1} y_{2}}{7}$ |
| 7 | 10 | $\frac{1850 y_{1}^{2}}{7} + \frac{4828 y_{1} y_{2}}{7}$ |
| 7 | 11 | $96 y_{1}^{3} + \frac{41424 y_{1}^{2} y_{2}}{7} + \frac{3552 y_{1} y_{2}^{2}}{7}$ |
| 8 | 3 | $1$ |
| 8 | 4 | $\frac{6}{7}$ |
| 8 | 5 | $\frac{13}{7}$ |
| 8 | 6 | $\frac{174 y_{1}}{7}$ |
| 8 | 7 | $4 y_{2}$ |
| 8 | 8 | $\frac{144 y_{1}}{7}$ |
| 8 | 9 | $\frac{120 y_{1}^{2}}{7} + \frac{1640 y_{1} y_{2}}{7}$ |
| 8 | 10 | $\frac{360 y_{1}^{2}}{7} + \frac{7256 y_{1} y_{2}}{7}$ |
| 8 | 11 | $\frac{32400 y_{1}^{2} y_{2}}{7} + \frac{8856 y_{1} y_{2}^{2}}{7}$ |
| 9 | 6 | $1$ |
| 9 | 7 | $-6$ |
| 9 | 8 | $-7$ |
| 9 | 9 | $- 54 y_{1}$ |
| 9 | 10 | $- 174 y_{1} + 10 y_{2}$ |
| 9 | 11 | $- 120 y_{1}^{2} - 544 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 10 | 6 | $1$ |
| 10 | 7 | $2$ |
| 10 | 8 | $4$ |
| 10 | 9 | $18 y_{1}$ |
| 10 | 10 | $58 y_{1}$ |
| 10 | 11 | $40 y_{1}^{2} + 272 y_{1} y_{2}$ |
| 11 | 9 | $1$ |
| 11 | 10 | $4$ |

Enumeration mode: positive; 26 curve classes including zero. Matrix computation time: 127.47 minutes.
Saved checks: matrix rank, basis, Poincare pairing, unit column, c1 homogeneity.

## PROD5-D05 --- spectrum and connection

**Specialization:**  $y_1=2,\ y_2=3$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$



$$
\det(xI-K^F)=p_{1}(x)^{7}\,p_{2}(x).
$$




$$
\begin{aligned}p_{1}(x)&=x - 14.\end{aligned}
$$




$$
\begin{aligned}p_{2}(x)&=x^{5} + 118 x^{4} - 87864 x^{3} + 9147888 x^{2} - 206522928 x\\&+1334372064.\end{aligned}
$$


Cyclic determinant: $\Delta=0$. The specialized operator is not cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 398.98695 | 0 | 7 | -14 | 0 |
| 2 | -126.44373 | -30.898339 | 8 | -14 | 0 |
| 3 | -126.44373 | 30.898339 | 9 | -14 | 0 |
| 4 | -14.078613 | 0 | 10 | -14 | 0 |
| 5 | -14.020875 | 0 | 11 | -14 | 0 |
| 6 | -14 | 0 | 12 | -14 | 0 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | unresolved | unresolved | not computed |
| $p_{2}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
**Unresolved factor $p_{1}$:**  the eigenvalue 14 has a 3-dimensional kernel, so its generalized eigenspace is not a single Jordan block and the factor is not cyclic (check cyclic_determinant first).

**Search aliases:** PROD5-D05; dimension 5; fivefold; Complete intersection in a product of projective spaces; Fano; quantum cohomology; Gromov-Witten; Hodge diamond; quantum multiplication; connection exponents; Complete intersection of multidegrees (2,2), (1,2) in P³ × P⁴; product of projective spaces; regularized exponent multiset; repeated exponents.
