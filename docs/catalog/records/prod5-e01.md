---
title: "Complete intersection of multidegrees (2,2), (1,1), (1,1) in P⁴ × P⁴"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Complete intersection of multidegrees (2,2), (1,1), (1,1) in P⁴ × P⁴."
keywords: ["dimension 5", "fivefold", "Complete intersection in a product of projective spaces", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Complete intersection of multidegrees (2,2), (1,1), (1,1) in P⁴ × P⁴", "product of projective spaces", "regularized exponent multiset", "repeated exponents"]
---

# Complete intersection in \(\mathbb P^{4}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{4}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[2, 2], [1, 1], [1, 1]]`.

[Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)



## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 10\) | 1 | 7 |
| \(z^{5} - 50 z^{4} - 59000 z^{3} - 5410000 z^{2} - 85150000 z - 372100000\) | 5 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 10=0\) | \(\{\!\{0,0,0,0,0,\frac{1}{2},\frac{1}{2}\}\!\}\) |
| \(\lambda^{5} - 50 \lambda^{4} - 59000 \lambda^{3} - 5410000 \lambda^{2} - 85150000 \lambda - 372100000=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-fivefolds.json) · [Hodge data and atomic invariants](../invariants-fivefolds.md#prod5-e01). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{4}\times\mathbb P^{4}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 2], [1, 1], [1, 1]]
residual_product_degrees = [1, 1]
```

The residual product degrees give the anticanonical class. 

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

### Computed quantum multiplication

Write $A(\mathbf y)=c_1(X)\star$ and use the ordered basis $e_0,\ldots,e_{11}$ below. Columns are images: $A(\mathbf y)e_j=\sum_i A_{ij}(\mathbf y)e_i$.

```python
basis = ['1', 'x5', 'x0', 'x5^2', 'x0^2', 'x0*x5', 'x5^3', 'x0^3', 'x0*x5^2', 'x5^4', 'x0^4', 'x0*x5^4']
```


$$
G=\operatorname{diag}\!\left(- \frac{5}{2},- \frac{3}{2},- \frac{3}{2},- \frac{1}{2},- \frac{1}{2},- \frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{3}{2},\frac{3}{2},\frac{5}{2}\right).
$$


**Exact matrix:**  every nonzero entry is listed below; all omitted entries are zero. Indices are zero based. No Novikov specialization has been made in this table.

| Row $i$ | Column $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
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

Curve enumeration: positive; 26 curve classes including zero.
