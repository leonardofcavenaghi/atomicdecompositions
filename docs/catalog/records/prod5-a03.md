---
title: "Complete intersection of multidegrees (2,4) in P² × P⁴"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Complete intersection of multidegrees (2,4) in P² × P⁴."
keywords: ["dimension 5", "fivefold", "Complete intersection in a product of projective spaces", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Complete intersection of multidegrees (2,4) in P² × P⁴", "product of projective spaces", "regularized exponent multiset", "repeated exponents"]
---

# Complete intersection in \(\mathbb P^{2}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{2}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[2, 4]]`.

[Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)



## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 54\) | 1 | 7 |
| \(z^{5} - 1326 z^{4} - 19224 z^{3} - 192631280 z^{2} - 21539338416 z - 592705245024\) | 5 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 54=0\) | \(\{\!\{0,0,0,0,0,\frac{1}{2},\frac{1}{2}\}\!\}\) |
| \(\lambda^{5} - 1326 \lambda^{4} - 19224 \lambda^{3} - 192631280 \lambda^{2} - 21539338416 \lambda - 592705245024=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-fivefolds.json) · [Hodge data and atomic invariants](../invariants-fivefolds.md#prod5-a03). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{2}\times\mathbb P^{4}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 4]]
residual_product_degrees = [1, 1]
```

The residual product degrees give the anticanonical class. 

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=50$, $e(X)=-3678$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&105&&1740&&1740&&105&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=105$, $h^{3,2}=1740$; even rank 12; odd rank 3690.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 103, -1737)$.

```python
chern_numbers = {'c1_5': 50, 'c1_3_c2': 238, 'c1_c2_2': 1092, 'c1_2_c3': -320, 'c2_c3': -1340, 'c1_c4': 1278, 'c5': -3678}
```

### Exact software inputs

Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

```python
rays = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [-1, -1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, -1, -1, -1, -1]]
cones = [[0, 1, 3, 4, 5, 6], [0, 1, 3, 4, 5, 7], [0, 1, 3, 4, 6, 7], [0, 1, 3, 5, 6, 7],
 [0, 1, 4, 5, 6, 7], [0, 2, 3, 4, 5, 6], [0, 2, 3, 4, 5, 7], [0, 2, 3, 4, 6, 7],
 [0, 2, 3, 5, 6, 7], [0, 2, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7],
 [1, 2, 3, 4, 6, 7], [1, 2, 3, 5, 6, 7], [1, 2, 4, 5, 6, 7]]
K = [[2, 0, 0, 4, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

### Ordered basis and curve conventions

```python
ambient_basis = ['1', 'x3', 'x0', 'x3^2', 'x0^2', 'x0*x3', 'x3^3', 'x0*x3^2', 'x0^2*x3', 'x3^4',
 'x0*x3^3', 'x0*x3^4']
ambient_rank = 12
novikov_divisors = [[0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
h2_basis = [[1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1]]
```

### Computed quantum multiplication

Write $A(\mathbf y)=c_1(X)\star$ and use the ordered basis $e_0,\ldots,e_{11}$ below. Columns are images: $A(\mathbf y)e_j=\sum_i A_{ij}(\mathbf y)e_i$.

```python
basis = ['1', 'x3', 'x0', 'x3^2', 'x0^2', 'x0*x3', 'x3^3', 'x0*x3^2', 'x0^2*x3', 'x3^4', 'x0*x3^3', 'x0*x3^4']
```


$$
G=\operatorname{diag}\!\left(- \frac{5}{2},- \frac{3}{2},- \frac{3}{2},- \frac{1}{2},- \frac{1}{2},- \frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{3}{2},\frac{3}{2},\frac{5}{2}\right).
$$


**Exact matrix:**  every nonzero entry is listed below; all omitted entries are zero. Indices are zero based. No Novikov specialization has been made in this table.

| Row $i$ | Column $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $3888 y_{1}^{2} + 1344 y_{1} y_{2}$ |
| 0 | 2 | $1344 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 0 | 3 | $504576 y_{1}^{3} + 774144 y_{1}^{2} y_{2} + 10272 y_{1} y_{2}^{2}$ |
| 0 | 4 | $214272 y_{1}^{2} y_{2} + 19296 y_{1} y_{2}^{2}$ |
| 0 | 5 | $568512 y_{1}^{2} y_{2} + 21744 y_{1} y_{2}^{2}$ |
| 0 | 6 | $18323712 y_{1}^{4} + 162800640 y_{1}^{3} y_{2} + 14139840 y_{1}^{2} y_{2}^{2} + 20480 y_{1} y_{2}^{3}$ |
| 0 | 7 | $174219264 y_{1}^{3} y_{2} + 26532096 y_{1}^{2} y_{2}^{2} + 80128 y_{1} y_{2}^{3}$ |
| 0 | 8 | $64143360 y_{1}^{3} y_{2} + 19037952 y_{1}^{2} y_{2}^{2} + 94720 y_{1} y_{2}^{3}$ |
| 0 | 9 | $6246028800 y_{1}^{4} y_{2} + 2262188160 y_{1}^{3} y_{2}^{2} + 35276800 y_{1}^{2} y_{2}^{3} + 10240 y_{1} y_{2}^{4}$ |
| 0 | 10 | $17923507200 y_{1}^{4} y_{2} + 8146010880 y_{1}^{3} y_{2}^{2} + 171495040 y_{1}^{2} y_{2}^{3} + 87040 y_{1} y_{2}^{4}$ |
| 0 | 11 | $230549815296 y_{1}^{5} y_{2} + 293389765632 y_{1}^{4} y_{2}^{2} + 25165209600 y_{1}^{3} y_{2}^{3} + 157805568 y_{1}^{2} y_{2}^{4} + 24576 y_{1} y_{2}^{5}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $80 y_{1}$ |
| 1 | 2 | $12 y_{2}$ |
| 1 | 3 | $13600 y_{1}^{2} + 6304 y_{1} y_{2}$ |
| 1 | 4 | $4096 y_{1} y_{2} + 8 y_{2}^{2}$ |
| 1 | 5 | $7360 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 1 | 6 | $504576 y_{1}^{3} + 2380128 y_{1}^{2} y_{2} + 30144 y_{1} y_{2}^{2}$ |
| 1 | 7 | $3020928 y_{1}^{2} y_{2} + 88272 y_{1} y_{2}^{2}$ |
| 1 | 8 | $1358592 y_{1}^{2} y_{2} + 88224 y_{1} y_{2}^{2}$ |
| 1 | 9 | $125409280 y_{1}^{3} y_{2} + 15317440 y_{1}^{2} y_{2}^{2} + 24576 y_{1} y_{2}^{3}$ |
| 1 | 10 | $373633024 y_{1}^{3} y_{2} + 62480512 y_{1}^{2} y_{2}^{2} + 171520 y_{1} y_{2}^{3}$ |
| 1 | 11 | $5431449600 y_{1}^{4} y_{2} + 3621634560 y_{1}^{3} y_{2}^{2} + 100941440 y_{1}^{2} y_{2}^{3} + 66560 y_{1} y_{2}^{4}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $100 y_{1}$ |
| 2 | 3 | $19592 y_{1}^{2} + 2336 y_{1} y_{2}$ |
| 2 | 4 | $2624 y_{1} y_{2}$ |
| 2 | 5 | $3888 y_{1}^{2} + 3680 y_{1} y_{2}$ |
| 2 | 6 | $1257984 y_{1}^{3} + 1496640 y_{1}^{2} y_{2} + 6912 y_{1} y_{2}^{2}$ |
| 2 | 7 | $504576 y_{1}^{3} + 2182944 y_{1}^{2} y_{2} + 24096 y_{1} y_{2}^{2}$ |
| 2 | 8 | $1172928 y_{1}^{2} y_{2} + 26688 y_{1} y_{2}^{2}$ |
| 2 | 9 | $9161856 y_{1}^{4} + 110455808 y_{1}^{3} y_{2} + 6417920 y_{1}^{2} y_{2}^{2} + 4096 y_{1} y_{2}^{3}$ |
| 2 | 10 | $18323712 y_{1}^{4} + 346320896 y_{1}^{3} y_{2} + 28153280 y_{1}^{2} y_{2}^{2} + 32768 y_{1} y_{2}^{3}$ |
| 2 | 11 | $6246028800 y_{1}^{4} y_{2} + 2262188160 y_{1}^{3} y_{2}^{2} + 35276800 y_{1}^{2} y_{2}^{3} + 10240 y_{1} y_{2}^{4}$ |
| 3 | 1 | $1$ |
| 3 | 3 | $80 y_{1}$ |
| 3 | 4 | $16 y_{2}$ |
| 3 | 5 | $12 y_{2}$ |
| 3 | 6 | $3888 y_{1}^{2} + 6400 y_{1} y_{2}$ |
| 3 | 7 | $10816 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 3 | 8 | $6656 y_{1} y_{2} + 8 y_{2}^{2}$ |
| 3 | 9 | $586464 y_{1}^{2} y_{2} + 13344 y_{1} y_{2}^{2}$ |
| 3 | 10 | $1852224 y_{1}^{2} y_{2} + 70800 y_{1} y_{2}^{2}$ |
| 3 | 11 | $32071680 y_{1}^{3} y_{2} + 9518976 y_{1}^{2} y_{2}^{2} + 47360 y_{1} y_{2}^{3}$ |
| 4 | 2 | $1$ |
| 4 | 3 | $140 y_{1}$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 5 | $100 y_{1}$ |
| 4 | 6 | $23288 y_{1}^{2} + 960 y_{1} y_{2}$ |
| 4 | 7 | $19592 y_{1}^{2} + 2736 y_{1} y_{2}$ |
| 4 | 8 | $3888 y_{1}^{2} + 2656 y_{1} y_{2}$ |
| 4 | 9 | $502848 y_{1}^{3} + 349200 y_{1}^{2} y_{2} + 768 y_{1} y_{2}^{2}$ |
| 4 | 10 | $1257984 y_{1}^{3} + 1303056 y_{1}^{2} y_{2} + 5568 y_{1} y_{2}^{2}$ |
| 4 | 11 | $9161856 y_{1}^{4} + 45863424 y_{1}^{3} y_{2} + 2816640 y_{1}^{2} y_{2}^{2} + 2048 y_{1} y_{2}^{3}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $1$ |
| 5 | 3 | $260 y_{1}$ |
| 5 | 4 | $4 y_{2}$ |
| 5 | 5 | $80 y_{1}$ |
| 5 | 6 | $24448 y_{1}^{2} + 4160 y_{1} y_{2}$ |
| 5 | 7 | $13600 y_{1}^{2} + 9248 y_{1} y_{2}$ |
| 5 | 8 | $7488 y_{1} y_{2}$ |
| 5 | 9 | $252288 y_{1}^{3} + 798240 y_{1}^{2} y_{2} + 5376 y_{1} y_{2}^{2}$ |
| 5 | 10 | $504576 y_{1}^{3} + 2767296 y_{1}^{2} y_{2} + 32832 y_{1} y_{2}^{2}$ |
| 5 | 11 | $71073792 y_{1}^{3} y_{2} + 8506560 y_{1}^{2} y_{2}^{2} + 16384 y_{1} y_{2}^{3}$ |
| 6 | 3 | $1$ |
| 6 | 7 | $12 y_{2}$ |
| 6 | 8 | $16 y_{2}$ |
| 6 | 9 | $1312 y_{1} y_{2}$ |
| 6 | 10 | $4672 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 6 | 11 | $107136 y_{1}^{2} y_{2} + 9648 y_{1} y_{2}^{2}$ |
| 7 | 3 | $1$ |
| 7 | 5 | $1$ |
| 7 | 6 | $140 y_{1}$ |
| 7 | 7 | $80 y_{1}$ |
| 7 | 8 | $4 y_{2}$ |
| 7 | 9 | $1944 y_{1}^{2} + 1184 y_{1} y_{2}$ |
| 7 | 10 | $3888 y_{1}^{2} + 5024 y_{1} y_{2}$ |
| 7 | 11 | $230688 y_{1}^{2} y_{2} + 6048 y_{1} y_{2}^{2}$ |
| 8 | 4 | $1$ |
| 8 | 5 | $1$ |
| 8 | 6 | $200 y_{1}$ |
| 8 | 7 | $260 y_{1}$ |
| 8 | 8 | $80 y_{1} - 2 y_{2}$ |
| 8 | 9 | $8824 y_{1}^{2} + 576 y_{1} y_{2}$ |
| 8 | 10 | $24448 y_{1}^{2} + 2976 y_{1} y_{2}$ |
| 8 | 11 | $252288 y_{1}^{3} + 271728 y_{1}^{2} y_{2} + 2112 y_{1} y_{2}^{2}$ |
| 9 | 6 | $1$ |
| 9 | 7 | $-4$ |
| 9 | 8 | $-4$ |
| 9 | 9 | $- 200 y_{1}$ |
| 9 | 10 | $- 560 y_{1} + 12 y_{2}$ |
| 9 | 11 | $- 7776 y_{1}^{2} - 1344 y_{1} y_{2} + 4 y_{2}^{2}$ |
| 10 | 6 | $1$ |
| 10 | 7 | $3$ |
| 10 | 8 | $2$ |
| 10 | 9 | $100 y_{1}$ |
| 10 | 10 | $280 y_{1}$ |
| 10 | 11 | $3888 y_{1}^{2} + 1344 y_{1} y_{2}$ |
| 11 | 9 | $1$ |
| 11 | 10 | $3$ |

Curve enumeration: positive; 26 curve classes including zero.
