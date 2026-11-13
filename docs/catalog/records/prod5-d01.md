---
title: "Complete intersection of multidegrees (2,2), (1,1) in P³ × P⁴"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Complete intersection of multidegrees (2,2), (1,1) in P³ × P⁴."
keywords: ["dimension 5", "fivefold", "Complete intersection in a product of projective spaces", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Complete intersection of multidegrees (2,2), (1,1) in P³ × P⁴", "product of projective spaces", "regularized exponent multiset", "repeated exponents"]
---

# Complete intersection in \(\mathbb P^{3}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{3}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[2, 2], [1, 1]]`.

See the [fan and divisor certificate](../../data/geometric-presentations.json).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)


<!-- saved-exponent-summary:start -->
## Regularized exponent multisets

Analysis point: `y1=2, y2=3`. These lists describe the computed ambient connection. Every row applies **separately to each eigenvalue** satisfying the displayed condition; repeated entries retain their multiplicity.

The characteristic factors below use \(K^F=-A\), so an eigenvalue \(\lambda\) of \(A=c_1\star\) satisfies \(p_i(-\lambda)=0\). The classes are powers modulo \(\mathbb Z\); their order does not pair them term by term with the powers.

| Spectral condition | Multiplicity per eigenvalue | \(F_{b,\lambda}\) | Computation |
|---|---:|---|---|
| \(p_{1}(-\lambda)=0\) | 4 | \(\{\!\{\frac{1}{2},\ \frac{1}{2},\ \frac{1}{2},\ \frac{1}{2}\}\!\}\) | Complete |
| \(p_{2}(-\lambda)=0\) | 1 | \(\{\!\{0\}\!\}\) | Complete |

These ambient data alone do not identify full atoms or establish a rationality result. See the [connection conventions](../../toric/mathematics.md).
<!-- saved-exponent-summary:end -->

## Construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{3}\times\mathbb P^{4}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 2], [1, 1]]
residual_product_degrees = [1, 2]
```

The residual product degrees give the anticanonical class. 
Related workbook IDs: [48, 93].

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=560$, $e(X)=-324$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&4&&164&&164&&4&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=4$, $h^{3,2}=164$; even rank 12; odd rank 336.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 2, -161)$.

```python
chern_numbers = {'c1_5': 560, 'c1_3_c2': 688, 'c1_c2_2': 818, 'c1_2_c3': 22, 'c2_c3': 54, 'c1_c4': 348, 'c5': -324}
```

### Exact software inputs

Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

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
K = [[2, 0, 0, 0, 2, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0]]
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
| 0 | 1 | $4 y_{1}$ |
| 0 | 2 | $4 y_{2}^{2}$ |
| 0 | 3 | $132 y_{1} y_{2}$ |
| 0 | 4 | $84 y_{1} y_{2}$ |
| 0 | 5 | $132 y_{1} y_{2}$ |
| 0 | 6 | $640 y_{1} y_{2}^{2}$ |
| 0 | 7 | $512 y_{1} y_{2}^{2}$ |
| 0 | 8 | $1408 y_{1} y_{2}^{2}$ |
| 0 | 9 | $360 y_{1}^{2} y_{2} + 640 y_{1} y_{2}^{3}$ |
| 0 | 10 | $880 y_{1}^{2} y_{2} + 3200 y_{1} y_{2}^{3}$ |
| 0 | 11 | $5376 y_{1}^{2} y_{2}^{2} + 1536 y_{1} y_{2}^{4}$ |
| 1 | 0 | $2$ |
| 1 | 2 | $8 y_{2}$ |
| 1 | 3 | $4 y_{1}$ |
| 1 | 4 | $8 y_{2}^{2}$ |
| 1 | 5 | $4 y_{2}^{2}$ |
| 1 | 6 | $264 y_{1} y_{2}$ |
| 1 | 7 | $48 y_{1} y_{2}$ |
| 1 | 8 | $324 y_{1} y_{2}$ |
| 1 | 9 | $640 y_{1} y_{2}^{2}$ |
| 1 | 10 | $2432 y_{1} y_{2}^{2}$ |
| 1 | 11 | $160 y_{1}^{2} y_{2} + 1920 y_{1} y_{2}^{3}$ |
| 2 | 0 | $1$ |
| 2 | 3 | $16 y_{1}$ |
| 2 | 5 | $4 y_{1}$ |
| 2 | 6 | $192 y_{1} y_{2}$ |
| 2 | 7 | $84 y_{1} y_{2}$ |
| 2 | 8 | $324 y_{1} y_{2}$ |
| 2 | 9 | $256 y_{1} y_{2}^{2}$ |
| 2 | 10 | $1152 y_{1} y_{2}^{2}$ |
| 2 | 11 | $360 y_{1}^{2} y_{2} + 640 y_{1} y_{2}^{3}$ |
| 3 | 1 | $2$ |
| 3 | 4 | $10 y_{2}$ |
| 3 | 5 | $8 y_{2}$ |
| 3 | 7 | $4 y_{2}^{2}$ |
| 3 | 8 | $4 y_{2}^{2}$ |
| 3 | 9 | $84 y_{1} y_{2}$ |
| 3 | 10 | $216 y_{1} y_{2}$ |
| 3 | 11 | $512 y_{1} y_{2}^{2}$ |
| 4 | 2 | $1$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 6 | $20 y_{1}$ |
| 4 | 8 | $16 y_{1}$ |
| 4 | 9 | $48 y_{1} y_{2}$ |
| 4 | 10 | $180 y_{1} y_{2}$ |
| 4 | 11 | $128 y_{1} y_{2}^{2}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $2$ |
| 5 | 4 | $4 y_{2}$ |
| 5 | 6 | $8 y_{1}$ |
| 5 | 8 | $4 y_{1}$ |
| 5 | 9 | $96 y_{1} y_{2}$ |
| 5 | 10 | $288 y_{1} y_{2}$ |
| 5 | 11 | $384 y_{1} y_{2}^{2}$ |
| 6 | 3 | $2$ |
| 6 | 4 | $- \frac{2}{3}$ |
| 6 | 5 | $- \frac{1}{3}$ |
| 6 | 7 | $4 y_{2}$ |
| 6 | 8 | $8 y_{2}$ |
| 6 | 9 | $- \frac{4 y_{1}}{3}$ |
| 6 | 10 | $- \frac{8 y_{1}}{3} + 4 y_{2}^{2}$ |
| 6 | 11 | $12 y_{1} y_{2}$ |
| 7 | 4 | $\frac{11}{3}$ |
| 7 | 5 | $\frac{4}{3}$ |
| 7 | 7 | $- 2 y_{2}$ |
| 7 | 9 | $\frac{40 y_{1}}{3}$ |
| 7 | 10 | $\frac{92 y_{1}}{3}$ |
| 7 | 11 | $72 y_{1} y_{2}$ |
| 8 | 3 | $1$ |
| 8 | 4 | $\frac{4}{3}$ |
| 8 | 5 | $\frac{8}{3}$ |
| 8 | 7 | $2 y_{2}$ |
| 8 | 9 | $\frac{8 y_{1}}{3}$ |
| 8 | 10 | $\frac{16 y_{1}}{3}$ |
| 8 | 11 | $60 y_{1} y_{2}$ |
| 9 | 6 | $2$ |
| 9 | 7 | $-4$ |
| 9 | 8 | $-3$ |
| 9 | 10 | $8 y_{2}$ |
| 9 | 11 | $- 8 y_{1} + 4 y_{2}^{2}$ |
| 10 | 6 | $1$ |
| 10 | 7 | $2$ |
| 10 | 8 | $4$ |
| 10 | 11 | $4 y_{1}$ |
| 11 | 9 | $1$ |
| 11 | 10 | $4$ |

Curve enumeration: positive; 14 curve classes including zero.

## Spectrum and connection

**Specialization:**  $y_1=2,\ y_2=3$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$


$$
\det(xI-K^F)=p_{1}(x)^{4}\,p_{2}(x).
$$


$$
\begin{aligned}p_{1}(x)&=x - 6.\end{aligned}
$$


$$
\begin{aligned}p_{2}(x)&=x^{8} + 12 x^{7} - 200 x^{6} + 90192 x^{5} - 4845504 x^{4} + 91651392 x^{3}\\&- 789420416 x^{2} + 3185087232 x - 4904234240.\end{aligned}
$$


Cyclic determinant: $\Delta=- \frac{429702116898067728563330602412370770066931712}{3}$. The specialized operator is cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 63.302893 | 0 | 7 | -6 | 0 |
| 2 | -2.7045334 | -44.65939 | 8 | -6 | 0 |
| 3 | -2.7045334 | 44.65939 | 9 | -6 | 0 |
| 4 | -14.404898 | -0.59964837 | 10 | -5.7016838 | -0.51689102 |
| 5 | -14.404898 | 0.59964837 | 11 | -5.7016838 | 0.51689102 |
| 6 | -6 | 0 | 12 | -5.6806629 | 0 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | $- \frac{3}{2},\ - \frac{3}{2},\ - \frac{3}{2},\ - \frac{3}{2}$ | $\frac{1}{2},\ \frac{1}{2},\ \frac{1}{2},\ \frac{1}{2}$ | complete / recursion |
| $p_{2}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
Recursion obstruction for $p_{1}$: $- \frac{\left(2 s + 3\right)^{4}}{7296}$.
