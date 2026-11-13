---
title: "Quartic fivefold in P⁶"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Quartic fivefold in P⁶."
keywords: ["dimension 5", "fivefold", "Projective complete intersection", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Quartic fivefold in P⁶", "projective space", "regularized exponent multiset", "repeated exponents"]
---

# Quartic fivefold in \(\mathbb P^{6}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{6}\). Defining multidegrees in this factor order: `[[4]]`.

See the [fan and divisor certificate](../../data/geometric-presentations.json).

**Construction:** Projective complete intersection. **Dimension:** 5. **Index:** 3. **h(1,1):** 1.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)


<!-- saved-exponent-summary:start -->
## Regularized exponent multisets

Analysis point: `y1=2`. These lists describe the computed ambient connection. Every row applies **separately to each eigenvalue** satisfying the displayed condition; repeated entries retain their multiplicity.

The characteristic factors below use \(K^F=-A\), so an eigenvalue \(\lambda\) of \(A=c_1\star\) satisfies \(p_i(-\lambda)=0\). The classes are powers modulo \(\mathbb Z\); their order does not pair them term by term with the powers.

| Spectral condition | Multiplicity per eigenvalue | \(F_{b,\lambda}\) | Computation |
|---|---:|---|---|
| \(p_{1}(-\lambda)=0\) | 3 | \(\{\!\{0,\ \frac{1}{4},\ \frac{3}{4}\}\!\}\) | Complete |
| \(p_{2}(-\lambda)=0\) | 1 | \(\{\!\{0\}\!\}\) | Complete |
| \(p_{3}(-\lambda)=0\) | 1 | \(\{\!\{0\}\!\}\) | Complete |

These ambient data alone do not identify full atoms or establish a rationality result. See the [connection conventions](../../toric/mathematics.md).
<!-- saved-exponent-summary:end -->

## Construction and Hodge data

A smooth complete intersection of multidegree $(4)$ in $\mathbb P^{6}$.
Adjunction gives $-K_X=3H$.

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=1$, index $3$, $(-K_X)^5=972$, $e(X)=-540$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&1&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&1&&0&&0&\\0&&7&&266&&266&&7&&0\\&0&&0&&1&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&1&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=7$, $h^{3,2}=266$; even rank 6; odd rank 546.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 6, -265)$.

```python
chern_numbers = {'c1_5': 972, 'c1_3_c2': 972, 'c1_c2_2': 972, 'c1_2_c3': -36, 'c2_c3': -36, 'c1_c4': 468, 'c5': -540}
```

### Exact software inputs

Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

```python
rays = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [-1, -1, -1, -1, -1, -1]]
cones = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 6], [0, 1, 2, 3, 5, 6], [0, 1, 2, 4, 5, 6],
 [0, 1, 3, 4, 5, 6], [0, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
K = [[4, 0, 0, 0, 0, 0, 0]]
eval_y = {'y1': 2}
```

### Ordered basis and curve conventions

```python
ambient_basis = ['1', 'x0', 'x0^2', 'x0^3', 'x0^4', 'x0^5']
ambient_rank = 6
novikov_divisors = [[1, 0, 0, 0, 0, 0, 0]]
h2_basis = [[1, 1, 1, 1, 1, 1, 1]]
```

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
| 0 | 2 | $72 y_{1}$ |
| 0 | 5 | $1728 y_{1}^{2}$ |
| 1 | 0 | $3$ |
| 1 | 3 | $312 y_{1}$ |
| 2 | 1 | $3$ |
| 2 | 4 | $312 y_{1}$ |
| 3 | 2 | $3$ |
| 3 | 5 | $72 y_{1}$ |
| 4 | 3 | $3$ |
| 5 | 4 | $3$ |

Curve enumeration: positive; 3 curve classes including zero.

## Spectrum and connection

**Specialization:**  $y_1=2$. The connection operator is $K^F=-M$. The exact factors below refer to $K^F$; the numerical eigenvalues refer to $M=c_1\star$.

### Exact characteristic polynomial of $K^F$


$$
\det(xI-K^F)=p_{1}(x)^{3}\,p_{2}(x)\,p_{3}(x).
$$


$$
\begin{aligned}p_{1}(x)&=x.\end{aligned}
$$


$$
\begin{aligned}p_{2}(x)&=x + 24.\end{aligned}
$$


$$
\begin{aligned}p_{3}(x)&=x^{2} - 24 x + 576.\end{aligned}
$$


Cyclic determinant: $\Delta=-14348907$. The specialized operator is cyclic.

### Numerical eigenvalues of $c_1\star$

Values are rounded to eight significant digits; repeated eigenvalues are retained with multiplicity.

| $j$ | Real part | Imaginary part | $j$ | Real part | Imaginary part |
|---|---|---|---|---|---|
| 1 | 24 | 0 | 4 | 0 | 0 |
| 2 | -12 | -20.78461 | 5 | 0 | 0 |
| 3 | -12 | 20.78461 | 6 | 0 | 0 |

### Connection exponents

| Factor | Powers | Classes mod $\mathbb Z$ | Status / method |
|---|---|---|---|
| $p_{1}$ | $- \frac{7}{4},\ -1,\ - \frac{1}{4}$ | $0,\ \frac{1}{4},\ \frac{3}{4}$ | complete / recursion |
| $p_{2}$ | $0$ | $0$ | complete / residue |
| $p_{3}$ | $0$ | $0$ | complete / residue |

Powers and residue classes are multisets for each eigenvalue in the indicated factor, not paired lists. A simple-factor power applies at every root of that factor.
Recursion obstruction for $p_{1}$: $\frac{\left(2 s + 2\right) \left(4 s + 1\right) \left(4 s + 7\right)}{27}$.
