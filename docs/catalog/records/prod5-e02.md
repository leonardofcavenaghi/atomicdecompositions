---
title: "Complete intersection of multidegrees (2,1), (1,2), (1,1) in P⁴ × P⁴"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Complete intersection of multidegrees (2,1), (1,2), (1,1) in P⁴ × P⁴."
keywords: ["dimension 5", "fivefold", "Complete intersection in a product of projective spaces", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Complete intersection of multidegrees (2,1), (1,2), (1,1) in P⁴ × P⁴", "product of projective spaces", "regularized exponent multiset", "repeated exponents"]
---

# Complete intersection in \(\mathbb P^{4}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{4}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[2, 1], [1, 2], [1, 1]]`.

See the [fan and divisor certificate](../../data/geometric-presentations.json).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)


<!-- saved-exponent-summary:start -->
## Regularized exponent multisets

Analysis point: `y1=2, y2=3`. These lists describe the computed ambient connection. Every row applies **separately to each eigenvalue** satisfying the displayed condition; repeated entries retain their multiplicity.

The characteristic factors below use \(K^F=-A\), so an eigenvalue \(\lambda\) of \(A=c_1\star\) satisfies \(p_i(-\lambda)=0\). The classes are powers modulo \(\mathbb Z\); their order does not pair them term by term with the powers.

| Spectral condition | Multiplicity per eigenvalue | \(F_{b,\lambda}\) | Computation |
|---|---:|---|---|
| \(p_{1}(-\lambda)=0\) | 6 | Unresolved | Unresolved |
| \(p_{2}(-\lambda)=0\) | 1 | \(\{\!\{0\}\!\}\) | Complete |

Unresolved factors have no computed multiset here. These ambient data alone do not identify full atoms or establish a rationality result. See the [connection conventions](../../toric/mathematics.md).
<!-- saved-exponent-summary:end -->

## Construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{4}\times\mathbb P^{4}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 1], [1, 2], [1, 1]]
residual_product_degrees = [1, 1]
```

The residual product degrees give the anticanonical class. 
Related workbook IDs: [112].

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=160$, $e(X)=-548$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&11&&269&&269&&11&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=11$, $h^{3,2}=269$; even rank 12; odd rank 560.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 9, -266)$.

```python
chern_numbers = {'c1_5': 160, 'c1_3_c2': 344, 'c1_c2_2': 752, 'c1_2_c3': -68, 'c2_c3': -140, 'c1_c4': 404, 'c5': -548}
```

### Exact software inputs

Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

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
K = [[2, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 2, 0, 0, 0, 0],
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
| 0 | 1 | $4 y_{1}^{2} + 136 y_{1} y_{2}$ |
| 0 | 2 | $136 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 0 | 3 | $2940 y_{1}^{2} y_{2} + 1140 y_{1} y_{2}^{2}$ |
| 0 | 4 | $1140 y_{1}^{2} y_{2} + 2940 y_{1} y_{2}^{2}$ |
| 0 | 5 | $2388 y_{1}^{2} y_{2} + 2388 y_{1} y_{2}^{2}$ |
| 0 | 6 | $12176 y_{1}^{3} y_{2} + 76816 y_{1}^{2} y_{2}^{2} + 2432 y_{1} y_{2}^{3}$ |
| 0 | 7 | $2432 y_{1}^{3} y_{2} + 76816 y_{1}^{2} y_{2}^{2} + 12176 y_{1} y_{2}^{3}$ |
| 0 | 8 | $16272 y_{1}^{3} y_{2} + 151056 y_{1}^{2} y_{2}^{2} + 9312 y_{1} y_{2}^{3}$ |
| 0 | 9 | $6080 y_{1}^{4} y_{2} + 362520 y_{1}^{3} y_{2}^{2} + 229680 y_{1}^{2} y_{2}^{3} + 1280 y_{1} y_{2}^{4}$ |
| 0 | 10 | $1280 y_{1}^{4} y_{2} + 229680 y_{1}^{3} y_{2}^{2} + 362520 y_{1}^{2} y_{2}^{3} + 6080 y_{1} y_{2}^{4}$ |
| 0 | 11 | $3072 y_{1}^{5} y_{2} + 1154880 y_{1}^{4} y_{2}^{2} + 6253824 y_{1}^{3} y_{2}^{3} + 1154880 y_{1}^{2} y_{2}^{4} + 3072 y_{1} y_{2}^{5}$ |
| 1 | 0 | $1$ |
| 1 | 2 | $9 y_{2}$ |
| 1 | 3 | $362 y_{1} y_{2}$ |
| 1 | 4 | $252 y_{1} y_{2} + 14 y_{2}^{2}$ |
| 1 | 5 | $388 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 1 | 6 | $3126 y_{1}^{2} y_{2} + 2304 y_{1} y_{2}^{2}$ |
| 1 | 7 | $816 y_{1}^{2} y_{2} + 5601 y_{1} y_{2}^{2}$ |
| 1 | 8 | $4422 y_{1}^{2} y_{2} + 6402 y_{1} y_{2}^{2}$ |
| 1 | 9 | $2176 y_{1}^{3} y_{2} + 39656 y_{1}^{2} y_{2}^{2} + 2176 y_{1} y_{2}^{3}$ |
| 1 | 10 | $512 y_{1}^{3} y_{2} + 34448 y_{1}^{2} y_{2}^{2} + 6912 y_{1} y_{2}^{3}$ |
| 1 | 11 | $1280 y_{1}^{4} y_{2} + 229680 y_{1}^{3} y_{2}^{2} + 362520 y_{1}^{2} y_{2}^{3} + 6080 y_{1} y_{2}^{4}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $9 y_{1}$ |
| 2 | 3 | $14 y_{1}^{2} + 252 y_{1} y_{2}$ |
| 2 | 4 | $362 y_{1} y_{2}$ |
| 2 | 5 | $4 y_{1}^{2} + 388 y_{1} y_{2}$ |
| 2 | 6 | $5601 y_{1}^{2} y_{2} + 816 y_{1} y_{2}^{2}$ |
| 2 | 7 | $2304 y_{1}^{2} y_{2} + 3126 y_{1} y_{2}^{2}$ |
| 2 | 8 | $8757 y_{1}^{2} y_{2} + 2772 y_{1} y_{2}^{2}$ |
| 2 | 9 | $6912 y_{1}^{3} y_{2} + 34448 y_{1}^{2} y_{2}^{2} + 512 y_{1} y_{2}^{3}$ |
| 2 | 10 | $2176 y_{1}^{3} y_{2} + 39656 y_{1}^{2} y_{2}^{2} + 2176 y_{1} y_{2}^{3}$ |
| 2 | 11 | $6080 y_{1}^{4} y_{2} + 362520 y_{1}^{3} y_{2}^{2} + 229680 y_{1}^{2} y_{2}^{3} + 1280 y_{1} y_{2}^{4}$ |
| 3 | 1 | $1$ |
| 3 | 3 | $- 2 y_{1}$ |
| 3 | 4 | $14 y_{2}$ |
| 3 | 5 | $9 y_{2}$ |
| 3 | 6 | $252 y_{1} y_{2}$ |
| 3 | 7 | $112 y_{1} y_{2} + 14 y_{2}^{2}$ |
| 3 | 8 | $408 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 3 | 9 | $336 y_{1}^{2} y_{2} + 756 y_{1} y_{2}^{2}$ |
| 3 | 10 | $96 y_{1}^{2} y_{2} + 1278 y_{1} y_{2}^{2}$ |
| 3 | 11 | $256 y_{1}^{3} y_{2} + 15200 y_{1}^{2} y_{2}^{2} + 3040 y_{1} y_{2}^{3}$ |
| 4 | 2 | $1$ |
| 4 | 3 | $14 y_{1}$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 5 | $9 y_{1}$ |
| 4 | 6 | $14 y_{1}^{2} + 112 y_{1} y_{2}$ |
| 4 | 7 | $252 y_{1} y_{2}$ |
| 4 | 8 | $14 y_{1}^{2} + 308 y_{1} y_{2}$ |
| 4 | 9 | $1278 y_{1}^{2} y_{2} + 96 y_{1} y_{2}^{2}$ |
| 4 | 10 | $756 y_{1}^{2} y_{2} + 336 y_{1} y_{2}^{2}$ |
| 4 | 11 | $3040 y_{1}^{3} y_{2} + 15200 y_{1}^{2} y_{2}^{2} + 256 y_{1} y_{2}^{3}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $1$ |
| 5 | 3 | $7 y_{1}$ |
| 5 | 4 | $7 y_{2}$ |
| 5 | 6 | $296 y_{1} y_{2}$ |
| 5 | 7 | $296 y_{1} y_{2}$ |
| 5 | 8 | $602 y_{1} y_{2}$ |
| 5 | 9 | $1128 y_{1}^{2} y_{2} + 480 y_{1} y_{2}^{2}$ |
| 5 | 10 | $480 y_{1}^{2} y_{2} + 1128 y_{1} y_{2}^{2}$ |
| 5 | 11 | $1536 y_{1}^{3} y_{2} + 23616 y_{1}^{2} y_{2}^{2} + 1536 y_{1} y_{2}^{3}$ |
| 6 | 3 | $1$ |
| 6 | 4 | $- \frac{5}{7}$ |
| 6 | 5 | $- \frac{5}{7}$ |
| 6 | 6 | $- 7 y_{1}$ |
| 6 | 7 | $9 y_{2}$ |
| 6 | 8 | $- 5 y_{1} + 9 y_{2}$ |
| 6 | 9 | $\frac{52 y_{1} y_{2}}{7}$ |
| 6 | 10 | $- 24 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 6 | 11 | $- \frac{1584 y_{1}^{2} y_{2}}{7} + 288 y_{1} y_{2}^{2}$ |
| 7 | 4 | $\frac{12}{7}$ |
| 7 | 5 | $\frac{5}{7}$ |
| 7 | 6 | $14 y_{1}$ |
| 7 | 7 | $- 2 y_{2}$ |
| 7 | 8 | $19 y_{1}$ |
| 7 | 9 | $4 y_{1}^{2} + \frac{312 y_{1} y_{2}}{7}$ |
| 7 | 10 | $76 y_{1} y_{2}$ |
| 7 | 11 | $\frac{4776 y_{1}^{2} y_{2}}{7} + 168 y_{1} y_{2}^{2}$ |
| 8 | 3 | $1$ |
| 8 | 4 | $1$ |
| 8 | 5 | $2$ |
| 8 | 6 | $7 y_{1}$ |
| 8 | 7 | $7 y_{2}$ |
| 8 | 8 | $5 y_{1}$ |
| 8 | 9 | $96 y_{1} y_{2}$ |
| 8 | 10 | $96 y_{1} y_{2}$ |
| 8 | 11 | $552 y_{1}^{2} y_{2} + 552 y_{1} y_{2}^{2}$ |
| 9 | 6 | $\frac{9}{2}$ |
| 9 | 7 | $1$ |
| 9 | 8 | $7$ |
| 9 | 10 | $9 y_{2}$ |
| 9 | 11 | $136 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 10 | 6 | $1$ |
| 10 | 7 | $\frac{9}{2}$ |
| 10 | 8 | $\frac{9}{2}$ |
| 10 | 9 | $9 y_{1}$ |
| 10 | 11 | $4 y_{1}^{2} + 136 y_{1} y_{2}$ |
| 11 | 9 | $1$ |
| 11 | 10 | $1$ |

Curve enumeration: positive; 26 curve classes including zero.

## Spectrum and connection

**Specialization:**  $y_1=2,\ y_2=3$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$


$$
\det(xI-K^F)=p_{1}(x)^{6}\,p_{2}(x).
$$


$$
\begin{aligned}p_{1}(x)&=x - 10.\end{aligned}
$$


$$
\begin{aligned}p_{2}(x)&=x^{6} + 40 x^{5} - 40456 x^{4} + 3436380 x^{3} - 79886516 x^{2}\\&+726083000 x - 2308999372.\end{aligned}
$$


Cyclic determinant: $\Delta=0$. The specialized operator is not cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 255.71203 | 0 | 7 | -10 | 0 |
| 2 | -92.717389 | -13.697531 | 8 | -10 | 0 |
| 3 | -92.717389 | 13.697531 | 9 | -10 | 0 |
| 4 | -10.14293 | 0 | 10 | -10 | 0 |
| 5 | -10.096649 | 0 | 11 | -10 | 0 |
| 6 | -10.03767 | 0 | 12 | -10 | 0 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | unresolved | unresolved | not computed |
| $p_{2}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
**Unresolved factor $p_{1}$:**  the eigenvalue 10 has a 2-dimensional kernel, so its generalized eigenspace is not a single Jordan block and the factor is not cyclic (check cyclic_determinant first).
