---
title: "Complete intersection of multidegrees (3,3) in P³ × P³"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Complete intersection of multidegrees (3,3) in P³ × P³."
keywords: ["dimension 5", "fivefold", "Complete intersection in a product of projective spaces", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Complete intersection of multidegrees (3,3) in P³ × P³", "product of projective spaces", "regularized exponent multiset", "repeated exponents"]
---

# Complete intersection in \(\mathbb P^{3}\times \mathbb P^{3}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{3}\times \mathbb P^{3}\). Defining multidegrees in this factor order: `[[3, 3]]`.

[Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)


<!-- saved-exponent-summary:start -->
## Regularized exponent multisets

Analysis point: `y1=2, y2=3`. These lists describe the computed ambient connection. Every row applies **separately to each eigenvalue** satisfying the displayed condition; repeated entries retain their multiplicity.

The characteristic factors below use \(K^F=-A\), so an eigenvalue \(\lambda\) of \(A=c_1\star\) satisfies \(p_i(-\lambda)=0\). The classes are powers modulo \(\mathbb Z\); their order does not pair them term by term with the powers.

| Spectral condition | Multiplicity per eigenvalue | \(F_{b,\lambda}\) | Computation |
|---|---:|---|---|
| \(p_{1}(-\lambda)=0\) | 8 | Unresolved | Unresolved |
| \(p_{2}(-\lambda)=0\) | 1 | \(\{\!\{0\}\!\}\) | Complete |

Unresolved factors have no computed multiset here. These ambient data alone do not identify full atoms or establish a rationality result. See the [connection conventions](../../toric/mathematics.md).
<!-- saved-exponent-summary:end -->

## Construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{3}\times\mathbb P^{3}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[3, 3]]
residual_product_degrees = [1, 1]
```

The residual product degrees give the anticanonical class. 

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=60$, $e(X)=-3492$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&100&&1652&&1652&&100&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=100$, $h^{3,2}=1652$; even rank 12; odd rank 3504.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 98, -1649)$.

```python
chern_numbers = {'c1_5': 60, 'c1_3_c2': 252, 'c1_c2_2': 1068, 'c1_2_c3': -300, 'c2_c3': -1260, 'c1_c4': 1212, 'c5': -3492}
```

### Exact software inputs

Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

```python
rays = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [-1, -1, -1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, -1, -1, -1]]
cones = [[0, 1, 2, 4, 5, 6], [0, 1, 2, 4, 5, 7], [0, 1, 2, 4, 6, 7], [0, 1, 2, 5, 6, 7],
 [0, 1, 3, 4, 5, 6], [0, 1, 3, 4, 5, 7], [0, 1, 3, 4, 6, 7], [0, 1, 3, 5, 6, 7],
 [0, 2, 3, 4, 5, 6], [0, 2, 3, 4, 5, 7], [0, 2, 3, 4, 6, 7], [0, 2, 3, 5, 6, 7],
 [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7], [1, 2, 3, 4, 6, 7], [1, 2, 3, 5, 6, 7]]
K = [[3, 0, 0, 0, 3, 0, 0, 0]]
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
| 0 | 1 | $108 y_{1}^{2} + 1368 y_{1} y_{2}$ |
| 0 | 2 | $1368 y_{1} y_{2} + 108 y_{2}^{2}$ |
| 0 | 3 | $756 y_{1}^{3} + 133488 y_{1}^{2} y_{2} + 49572 y_{1} y_{2}^{2}$ |
| 0 | 4 | $49572 y_{1}^{2} y_{2} + 133488 y_{1} y_{2}^{2} + 756 y_{2}^{3}$ |
| 0 | 5 | $109836 y_{1}^{2} y_{2} + 109836 y_{1} y_{2}^{2}$ |
| 0 | 6 | $2409264 y_{1}^{3} y_{2} + 9633168 y_{1}^{2} y_{2}^{2} + 419904 y_{1} y_{2}^{3}$ |
| 0 | 7 | $419904 y_{1}^{3} y_{2} + 9633168 y_{1}^{2} y_{2}^{2} + 2409264 y_{1} y_{2}^{3}$ |
| 0 | 8 | $4217184 y_{1}^{3} y_{2} + 25496208 y_{1}^{2} y_{2}^{2} + 2227824 y_{1} y_{2}^{3}$ |
| 0 | 9 | $29218320 y_{1}^{4} y_{2} + 844483320 y_{1}^{3} y_{2}^{2} + 634414680 y_{1}^{2} y_{2}^{3} + 11022480 y_{1} y_{2}^{4}$ |
| 0 | 10 | $11022480 y_{1}^{4} y_{2} + 634414680 y_{1}^{3} y_{2}^{2} + 844483320 y_{1}^{2} y_{2}^{3} + 29218320 y_{1} y_{2}^{4}$ |
| 0 | 11 | $90699264 y_{1}^{5} y_{2} + 10420057728 y_{1}^{4} y_{2}^{2} + 42205624128 y_{1}^{3} y_{2}^{3} + 10420057728 y_{1}^{2} y_{2}^{4} + 90699264 y_{1} y_{2}^{5}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $9 y_{1}$ |
| 1 | 2 | $33 y_{2}$ |
| 1 | 3 | $108 y_{1}^{2} + 4878 y_{1} y_{2}$ |
| 1 | 4 | $3726 y_{1} y_{2} + 468 y_{2}^{2}$ |
| 1 | 5 | $5688 y_{1} y_{2} + 108 y_{2}^{2}$ |
| 1 | 6 | $180549 y_{1}^{2} y_{2} + 95499 y_{1} y_{2}^{2}$ |
| 1 | 7 | $45927 y_{1}^{2} y_{2} + 251181 y_{1} y_{2}^{2} + 756 y_{2}^{3}$ |
| 1 | 8 | $343845 y_{1}^{2} y_{2} + 365715 y_{1} y_{2}^{2}$ |
| 1 | 9 | $3093876 y_{1}^{3} y_{2} + 30607632 y_{1}^{2} y_{2}^{2} + 3093876 y_{1} y_{2}^{3}$ |
| 1 | 10 | $1285956 y_{1}^{3} y_{2} + 28707696 y_{1}^{2} y_{2}^{2} + 6405156 y_{1} y_{2}^{3}$ |
| 1 | 11 | $11022480 y_{1}^{4} y_{2} + 634414680 y_{1}^{3} y_{2}^{2} + 844483320 y_{1}^{2} y_{2}^{3} + 29218320 y_{1} y_{2}^{4}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $33 y_{1}$ |
| 2 | 2 | $9 y_{2}$ |
| 2 | 3 | $468 y_{1}^{2} + 3726 y_{1} y_{2}$ |
| 2 | 4 | $4878 y_{1} y_{2} + 108 y_{2}^{2}$ |
| 2 | 5 | $108 y_{1}^{2} + 5688 y_{1} y_{2}$ |
| 2 | 6 | $756 y_{1}^{3} + 251181 y_{1}^{2} y_{2} + 45927 y_{1} y_{2}^{2}$ |
| 2 | 7 | $95499 y_{1}^{2} y_{2} + 180549 y_{1} y_{2}^{2}$ |
| 2 | 8 | $756 y_{1}^{3} + 521397 y_{1}^{2} y_{2} + 209223 y_{1} y_{2}^{2}$ |
| 2 | 9 | $6405156 y_{1}^{3} y_{2} + 28707696 y_{1}^{2} y_{2}^{2} + 1285956 y_{1} y_{2}^{3}$ |
| 2 | 10 | $3093876 y_{1}^{3} y_{2} + 30607632 y_{1}^{2} y_{2}^{2} + 3093876 y_{1} y_{2}^{3}$ |
| 2 | 11 | $29218320 y_{1}^{4} y_{2} + 844483320 y_{1}^{3} y_{2}^{2} + 634414680 y_{1}^{2} y_{2}^{3} + 11022480 y_{1} y_{2}^{4}$ |
| 3 | 1 | $1$ |
| 3 | 4 | $54 y_{2}$ |
| 3 | 5 | $33 y_{2}$ |
| 3 | 6 | $2988 y_{1} y_{2}$ |
| 3 | 7 | $1458 y_{1} y_{2} + 360 y_{2}^{2}$ |
| 3 | 8 | $6714 y_{1} y_{2} + 108 y_{2}^{2}$ |
| 3 | 9 | $95499 y_{1}^{2} y_{2} + 180549 y_{1} y_{2}^{2}$ |
| 3 | 10 | $45927 y_{1}^{2} y_{2} + 251181 y_{1} y_{2}^{2} + 756 y_{2}^{3}$ |
| 3 | 11 | $419904 y_{1}^{3} y_{2} + 9633168 y_{1}^{2} y_{2}^{2} + 2409264 y_{1} y_{2}^{3}$ |
| 4 | 2 | $1$ |
| 4 | 3 | $54 y_{1}$ |
| 4 | 5 | $33 y_{1}$ |
| 4 | 6 | $360 y_{1}^{2} + 1458 y_{1} y_{2}$ |
| 4 | 7 | $2988 y_{1} y_{2}$ |
| 4 | 8 | $468 y_{1}^{2} + 5184 y_{1} y_{2}$ |
| 4 | 9 | $756 y_{1}^{3} + 251181 y_{1}^{2} y_{2} + 45927 y_{1} y_{2}^{2}$ |
| 4 | 10 | $180549 y_{1}^{2} y_{2} + 95499 y_{1} y_{2}^{2}$ |
| 4 | 11 | $2409264 y_{1}^{3} y_{2} + 9633168 y_{1}^{2} y_{2}^{2} + 419904 y_{1} y_{2}^{3}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $1$ |
| 5 | 3 | $42 y_{1}$ |
| 5 | 4 | $42 y_{2}$ |
| 5 | 5 | $9 y_{1} + 9 y_{2}$ |
| 5 | 6 | $108 y_{1}^{2} + 3726 y_{1} y_{2}$ |
| 5 | 7 | $3726 y_{1} y_{2} + 108 y_{2}^{2}$ |
| 5 | 8 | $108 y_{1}^{2} + 10170 y_{1} y_{2}$ |
| 5 | 9 | $270216 y_{1}^{2} y_{2} + 163296 y_{1} y_{2}^{2}$ |
| 5 | 10 | $163296 y_{1}^{2} y_{2} + 270216 y_{1} y_{2}^{2}$ |
| 5 | 11 | $1807920 y_{1}^{3} y_{2} + 15863040 y_{1}^{2} y_{2}^{2} + 1807920 y_{1} y_{2}^{3}$ |
| 6 | 3 | $1$ |
| 6 | 4 | $-1$ |
| 6 | 5 | $-1$ |
| 6 | 6 | $- 33 y_{1}$ |
| 6 | 7 | $21 y_{2}$ |
| 6 | 8 | $- 42 y_{1} + 33 y_{2}$ |
| 6 | 9 | $- 108 y_{1}^{2} - 810 y_{1} y_{2} + 108 y_{2}^{2}$ |
| 6 | 10 | $- 1962 y_{1} y_{2} + 360 y_{2}^{2}$ |
| 6 | 11 | $- 60264 y_{1}^{2} y_{2} + 23652 y_{1} y_{2}^{2} + 756 y_{2}^{3}$ |
| 7 | 4 | $2$ |
| 7 | 5 | $1$ |
| 7 | 6 | $54 y_{1}$ |
| 7 | 8 | $96 y_{1}$ |
| 7 | 9 | $468 y_{1}^{2} + 3726 y_{1} y_{2}$ |
| 7 | 10 | $108 y_{1}^{2} + 4878 y_{1} y_{2}$ |
| 7 | 11 | $756 y_{1}^{3} + 133488 y_{1}^{2} y_{2} + 49572 y_{1} y_{2}^{2}$ |
| 8 | 3 | $1$ |
| 8 | 4 | $1$ |
| 8 | 5 | $2$ |
| 8 | 6 | $33 y_{1}$ |
| 8 | 7 | $33 y_{2}$ |
| 8 | 8 | $42 y_{1} + 9 y_{2}$ |
| 8 | 9 | $108 y_{1}^{2} + 5688 y_{1} y_{2}$ |
| 8 | 10 | $5688 y_{1} y_{2} + 108 y_{2}^{2}$ |
| 8 | 11 | $109836 y_{1}^{2} y_{2} + 109836 y_{1} y_{2}^{2}$ |
| 9 | 6 | $1$ |
| 9 | 8 | $2$ |
| 9 | 9 | $9 y_{2}$ |
| 9 | 10 | $33 y_{2}$ |
| 9 | 11 | $1368 y_{1} y_{2} + 108 y_{2}^{2}$ |
| 10 | 7 | $1$ |
| 10 | 8 | $1$ |
| 10 | 9 | $33 y_{1}$ |
| 10 | 10 | $9 y_{1}$ |
| 10 | 11 | $108 y_{1}^{2} + 1368 y_{1} y_{2}$ |
| 11 | 9 | $1$ |
| 11 | 10 | $1$ |

Curve enumeration: positive; 26 curve classes including zero.

## Spectrum and connection

**Specialization:**  $y_1=2,\ y_2=3$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$


$$
\det(xI-K^F)=p_{1}(x)^{8}\,p_{2}(x).
$$


$$
\begin{aligned}p_{1}(x)&=x - 30.\end{aligned}
$$


$$
\begin{aligned}p_{2}(x)&=x^{4} + 420 x^{3} - 528714 x^{2} + 106457220 x - 2729492559.\end{aligned}
$$


Cyclic determinant: $\Delta=0$. The specialized operator is not cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 1033.6277 | 0 | 7 | -30 | 0 |
| 2 | -291.81734 | -53.723755 | 8 | -30 | 0 |
| 3 | -291.81734 | 53.723755 | 9 | -30 | 0 |
| 4 | -30 | 0 | 10 | -30 | 0 |
| 5 | -30 | 0 | 11 | -30 | 0 |
| 6 | -30 | 0 | 12 | -29.993005 | 0 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | unresolved | unresolved | not computed |
| $p_{2}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
**Unresolved factor $p_{1}$:**  the eigenvalue 30 has a 3-dimensional kernel, so its generalized eigenspace is not a single Jordan block and the factor is not cyclic (check cyclic_determinant first).
