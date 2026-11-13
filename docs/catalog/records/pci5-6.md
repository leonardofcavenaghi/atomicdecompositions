---
title: PCI5-6 — 5-fold complete intersection
description: Exact fan inputs, ordered ambient basis, symbolic quantum multiplication and saved computation notes for PCI5-6.
---

# PCI5-6

**Construction:** Projective complete intersection. **Dimension:** 5. **Index in source:** 1. **h(1,1):** 1.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)

Saved record: **complete**. Matrix coefficients are exact; connection-factor notes below are retained. This page transcribes a completed computation, without rerunning localization.

## PCI5-6 --- construction and Hodge data

A smooth complete intersection of multidegree $(6)$ in $\mathbb P^{6}$.
Adjunction gives $-K_X=1H$.

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=1$, index $1$, $(-K_X)^5=6$, $e(X)=-13014$.
\[\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&1&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&1&&0&&0&\\0&&455&&6055&&6055&&455&&0\\&0&&0&&1&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&1&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}\]
$h^{4,1}=455$, $h^{3,2}=6055$; even rank 6; odd rank 13020.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 454, -6054)$.

```python
chern_numbers = {'c1_5': 6, 'c1_3_c2': 90, 'c1_c2_2': 1350, 'c1_2_c3': -330, 'c2_c3': -4950, 'c1_c4': 2190, 'c5': -13014}
```

### Exact software inputs

Executable input: `examples/fivefolds_positive/inputs/PCI5-6.py`. Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

```python
rays = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [-1, -1, -1, -1, -1, -1]]
cones = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 6], [0, 1, 2, 3, 5, 6], [0, 1, 2, 4, 5, 6],
 [0, 1, 3, 4, 5, 6], [0, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
K = [[6, 0, 0, 0, 0, 0, 0]]
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
Checkpoint directory: `examples/fivefolds_positive/batch_results/PCI5-6/`.

### Computed quantum multiplication

Write $M=c_1(X)\star$ and use the ordered basis $e_0,\ldots,e_{5}$ below. Columns are images: $M e_j=\sum_i M_{ij}e_i$.

```python
basis = ['1', 'x0', 'x0^2', 'x0^3', 'x0^4', 'x0^5']
```

\[\mathrm{Gr}=\operatorname{diag}\!\left(- \frac{5}{2},- \frac{3}{2},- \frac{1}{2},\frac{1}{2},\frac{3}{2},\frac{5}{2}\right).\]
**Exact matrix:**  every nonzero entry is listed below; all omitted entries are zero. Indices are zero based. No Novikov specialization has been made in this table.

| Row $i$ | Column $j$ | $M_{ij}$ |
|---|---|---|
| Row $i$ | Column $j$ | $M_{ij}$ |
| 0 | 1 | $13932000 y_{1}^{2}$ |
| 0 | 2 | $432265248000 y_{1}^{3}$ |
| 0 | 3 | $10524957538752000 y_{1}^{4}$ |
| 0 | 4 | $110441973189864960000 y_{1}^{5}$ |
| 0 | 5 | $261960335825727283200000 y_{1}^{6}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $5544 y_{1}$ |
| 1 | 2 | $177529968 y_{1}^{2}$ |
| 1 | 3 | $4331668617216 y_{1}^{3}$ |
| 1 | 4 | $46081933709444352 y_{1}^{4}$ |
| 1 | 5 | $110441973189864960000 y_{1}^{5}$ |
| 2 | 1 | $1$ |
| 2 | 2 | $15624 y_{1}$ |
| 2 | 3 | $398584800 y_{1}^{2}$ |
| 2 | 4 | $4331668617216 y_{1}^{3}$ |
| 2 | 5 | $10524957538752000 y_{1}^{4}$ |
| 3 | 2 | $1$ |
| 3 | 3 | $15624 y_{1}$ |
| 3 | 4 | $177529968 y_{1}^{2}$ |
| 3 | 5 | $432265248000 y_{1}^{3}$ |
| 4 | 3 | $1$ |
| 4 | 4 | $5544 y_{1}$ |
| 4 | 5 | $13932000 y_{1}^{2}$ |
| 5 | 4 | $1$ |

Enumeration mode: positive; 7 curve classes including zero. Matrix computation time: 140.07 minutes.
Saved checks: matrix rank, basis, Poincare pairing, unit column, c1 homogeneity.

## PCI5-6 --- spectrum and connection

**Specialization:**  $y_1=2$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$

\[\det(xI-K^F)=p_{1}(x)^{5}\,p_{2}(x).\]
\[\begin{aligned}p_{1}(x)&=x - 1440.\end{aligned}\]
\[\begin{aligned}p_{2}(x)&=x + 91872.\end{aligned}\]
Cyclic determinant: $\Delta=-1$. The specialized operator is cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 91872 | 0 | 4 | -1440 | 0 |
| 2 | -1440 | 0 | 5 | -1440 | 0 |
| 3 | -1440 | 0 | 6 | -1440 | 0 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | $- \frac{7}{3},\ - \frac{13}{6},\ -2,\ - \frac{11}{6},\ - \frac{5}{3}$ | $0,\ \frac{1}{6},\ \frac{1}{3},\ \frac{2}{3},\ \frac{5}{6}$ | complete / recursion |
| $p_{2}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
Recursion obstruction for $p_{1}$: $\frac{\left(s + 2\right) \left(3 s + 5\right) \left(3 s + 7\right) \left(6 s + 11\right) \left(6 s + 13\right)}{252844002938880000}$.

**Search aliases:** PCI5-6; dimension 5; fivefold; Projective complete intersection; Fano; quantum cohomology; Gromov-Witten; Hodge diamond; quantum multiplication; connection exponents.
