---
title: "Quintic fivefold in P⁶ — PCI5-5"
description: Exact fan inputs, ordered ambient basis, symbolic quantum multiplication and saved computation notes for PCI5-5.
---

# Quintic fivefold in \(\mathbb P^{6}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{6}\). Defining multidegrees in this factor order: `[[5]]`.

Source identifier: **PCI5-5**; see [CKP and HLM terminology](../sources.md). The presentation is verified by the [fan and divisor certificate](../../data/geometric-presentations.json).

**Construction:** Projective complete intersection. **Dimension:** 5. **Index in source:** 2. **h(1,1):** 1.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)

Saved record: **complete**. Matrix coefficients are exact; connection-factor notes below are retained. This page transcribes a completed computation, without rerunning localization.

## PCI5-5 --- construction and Hodge data

A smooth complete intersection of multidegree $(5)$ in $\mathbb P^{6}$.
Adjunction gives $-K_X=2H$.

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=1$, index $2$, $(-K_X)^5=160$, $e(X)=-3270$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&1&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&1&&0&&0&\\0&&84&&1554&&1554&&84&&0\\&0&&0&&1&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&1&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=84$, $h^{3,2}=1554$; even rank 6; odd rank 3276.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 83, -1553)$.

```python
chern_numbers = {'c1_5': 160, 'c1_3_c2': 440, 'c1_c2_2': 1210, 'c1_2_c3': -400, 'c2_c3': -1100, 'c1_c4': 1350, 'c5': -3270}
```

### Exact software inputs

Executable input: `examples/fivefolds_positive/inputs/PCI5-5.py`. Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

```python
rays = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [-1, -1, -1, -1, -1, -1]]
cones = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 6], [0, 1, 2, 3, 5, 6], [0, 1, 2, 4, 5, 6],
 [0, 1, 3, 4, 5, 6], [0, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
K = [[5, 0, 0, 0, 0, 0, 0]]
eval_y = {'y1': 2}
```

### Ordered basis and curve conventions

```python
ambient_basis = ['1', 'x0', 'x0^2', 'x0^3', 'x0^4', 'x0^5']
ambient_rank = 6
novikov_divisors = [[1, 0, 0, 0, 0, 0, 0]]
h2_basis = [[1, 1, 1, 1, 1, 1, 1]]
```

### Computation record

**Status:**  complete. Snapshot: 2026-11-09 18:05 UTC.
Checkpoint directory: `examples/fivefolds_positive/batch_results/PCI5-5/`.

### Computed quantum multiplication

Write $M=c_1(X)\star$ and use the ordered basis $e_0,\ldots,e_{5}$ below. Columns are images: $M e_j=\sum_i M_{ij}e_i$.

```python
basis = ['1', 'x0', 'x0^2', 'x0^3', 'x0^4', 'x0^5']
```



$$
\mathrm{Gr}=\operatorname{diag}\!\left(- \frac{5}{2},- \frac{3}{2},- \frac{1}{2},\frac{1}{2},\frac{3}{2},\frac{5}{2}\right).
$$


**Exact matrix:**  every nonzero entry is listed below; all omitted entries are zero. Indices are zero based. No Novikov specialization has been made in this table.

| Row $i$ | Column $j$ | $M_{ij}$ |
|---|---|---|
| Row $i$ | Column $j$ | $M_{ij}$ |
| 0 | 1 | $240 y_{1}$ |
| 0 | 3 | $422400 y_{1}^{2}$ |
| 0 | 5 | $62640000 y_{1}^{3}$ |
| 1 | 0 | $2$ |
| 1 | 2 | $1540 y_{1}$ |
| 1 | 4 | $1385000 y_{1}^{2}$ |
| 2 | 1 | $2$ |
| 2 | 3 | $2690 y_{1}$ |
| 2 | 5 | $422400 y_{1}^{2}$ |
| 3 | 2 | $2$ |
| 3 | 4 | $1540 y_{1}$ |
| 4 | 3 | $2$ |
| 4 | 5 | $240 y_{1}$ |
| 5 | 4 | $2$ |

Enumeration mode: positive; 4 curve classes including zero. Matrix computation time: 0.12 minutes.
Saved checks: matrix rank, basis, Poincare pairing, unit column, c1 homogeneity.

## PCI5-5 --- spectrum and connection

**Specialization:**  $y_1=2$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$



$$
\det(xI-K^F)=p_{1}(x)^{4}\,p_{2}(x).
$$




$$
\begin{aligned}p_{1}(x)&=x.\end{aligned}
$$




$$
\begin{aligned}p_{2}(x)&=x^{2} - 25000.\end{aligned}
$$


Cyclic determinant: $\Delta=-32768$. The specialized operator is cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 158.11388 | 0 | 4 | 0 | 0 |
| 2 | -158.11388 | 0 | 5 | 0 | 0 |
| 3 | 0 | 0 | 6 | 0 | 0 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | $- \frac{21}{10},\ - \frac{17}{10},\ - \frac{13}{10},\ - \frac{9}{10}$ | $\frac{1}{10},\ \frac{3}{10},\ \frac{7}{10},\ \frac{9}{10}$ | complete / recursion |
| $p_{2}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
Recursion obstruction for $p_{1}$: $\frac{\left(10 s + 9\right) \left(10 s + 13\right) \left(10 s + 17\right) \left(10 s + 21\right)}{2549760}$.

**Search aliases:** PCI5-5; dimension 5; fivefold; Projective complete intersection; Fano; quantum cohomology; Gromov-Witten; Hodge diamond; quantum multiplication; connection exponents; Quintic fivefold in P⁶; projective space.
