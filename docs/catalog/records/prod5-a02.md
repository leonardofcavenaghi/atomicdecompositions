---
title: "Complete intersection of multidegrees (2,3) in P² × P⁴"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Complete intersection of multidegrees (2,3) in P² × P⁴."
keywords: ["dimension 5", "fivefold", "Complete intersection in a product of projective spaces", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Complete intersection of multidegrees (2,3) in P² × P⁴", "product of projective spaces", "regularized exponent multiset", "repeated exponents"]
---

# Complete intersection in \(\mathbb P^{2}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{2}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[2, 3]]`.

[Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)



## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 6\) | 1 | 6 |
| \(z^{6} - 24 z^{5} - 468 z^{4} - 243324 z^{3} - 8079912 z^{2} - 91955952 z - 323829900\) | 6 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 6=0\) | \(\{\!\{\frac{1}{6},\frac{1}{6},\frac{1}{6},\frac{5}{6},\frac{5}{6},\frac{5}{6}\}\!\}\) |
| \(\lambda^{6} - 24 \lambda^{5} - 468 \lambda^{4} - 243324 \lambda^{3} - 8079912 \lambda^{2} - 91955952 \lambda - 323829900=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-fivefolds.json) · [Hodge data and atomic invariants](../invariants-fivefolds.md#prod5-a02). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{2}\times\mathbb P^{4}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 3]]
residual_product_degrees = [1, 2]
```

The residual product degrees give the anticanonical class. 

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=400$, $e(X)=-818$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&15&&400&&400&&15&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=15$, $h^{3,2}=400$; even rank 12; odd rank 830.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 13, -397)$.

```python
chern_numbers = {'c1_5': 400, 'c1_3_c2': 608, 'c1_c2_2': 912, 'c1_2_c3': -110, 'c2_c3': -150, 'c1_c4': 578, 'c5': -818}
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
K = [[2, 0, 0, 3, 0, 0, 0, 0]]
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
| 0 | 1 | $12 y_{1}$ |
| 0 | 2 | $4 y_{2}^{2}$ |
| 0 | 3 | $324 y_{1} y_{2}$ |
| 0 | 4 | $162 y_{1} y_{2}$ |
| 0 | 5 | $324 y_{1} y_{2}$ |
| 0 | 6 | $72 y_{1}^{2} + 1408 y_{1} y_{2}^{2}$ |
| 0 | 7 | $3168 y_{1} y_{2}^{2}$ |
| 0 | 8 | $2448 y_{1} y_{2}^{2}$ |
| 0 | 9 | $4320 y_{1}^{2} y_{2} + 1280 y_{1} y_{2}^{3}$ |
| 0 | 10 | $10260 y_{1}^{2} y_{2} + 6720 y_{1} y_{2}^{3}$ |
| 0 | 11 | $48384 y_{1}^{2} y_{2}^{2} + 3072 y_{1} y_{2}^{4}$ |
| 1 | 0 | $2$ |
| 1 | 2 | $9 y_{2}$ |
| 1 | 3 | $30 y_{1}$ |
| 1 | 4 | $6 y_{2}^{2}$ |
| 1 | 5 | $4 y_{2}^{2}$ |
| 1 | 6 | $864 y_{1} y_{2}$ |
| 1 | 7 | $1134 y_{1} y_{2}$ |
| 1 | 8 | $567 y_{1} y_{2}$ |
| 1 | 9 | $1664 y_{1} y_{2}^{2}$ |
| 1 | 10 | $6720 y_{1} y_{2}^{2}$ |
| 1 | 11 | $3780 y_{1}^{2} y_{2} + 4800 y_{1} y_{2}^{3}$ |
| 2 | 0 | $1$ |
| 2 | 3 | $44 y_{1}$ |
| 2 | 5 | $12 y_{1}$ |
| 2 | 6 | $432 y_{1} y_{2}$ |
| 2 | 7 | $756 y_{1} y_{2}$ |
| 2 | 8 | $486 y_{1} y_{2}$ |
| 2 | 9 | $48 y_{1}^{2} + 512 y_{1} y_{2}^{2}$ |
| 2 | 10 | $72 y_{1}^{2} + 2432 y_{1} y_{2}^{2}$ |
| 2 | 11 | $4320 y_{1}^{2} y_{2} + 1280 y_{1} y_{2}^{3}$ |
| 3 | 1 | $2$ |
| 3 | 4 | $9 y_{2}$ |
| 3 | 5 | $9 y_{2}$ |
| 3 | 6 | $12 y_{1}$ |
| 3 | 7 | $4 y_{2}^{2}$ |
| 3 | 8 | $6 y_{2}^{2}$ |
| 3 | 9 | $324 y_{1} y_{2}$ |
| 3 | 10 | $864 y_{1} y_{2}$ |
| 3 | 11 | $1632 y_{1} y_{2}^{2}$ |
| 4 | 2 | $1$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 6 | $48 y_{1}$ |
| 4 | 7 | $44 y_{1}$ |
| 4 | 8 | $12 y_{1}$ |
| 4 | 9 | $96 y_{1} y_{2}$ |
| 4 | 10 | $384 y_{1} y_{2}$ |
| 4 | 11 | $48 y_{1}^{2} + 256 y_{1} y_{2}^{2}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $2$ |
| 5 | 4 | $3 y_{2}$ |
| 5 | 6 | $56 y_{1}$ |
| 5 | 7 | $30 y_{1}$ |
| 5 | 9 | $288 y_{1} y_{2}$ |
| 5 | 10 | $936 y_{1} y_{2}$ |
| 5 | 11 | $1024 y_{1} y_{2}^{2}$ |
| 6 | 3 | $2$ |
| 6 | 7 | $9 y_{2}$ |
| 6 | 8 | $9 y_{2}$ |
| 6 | 10 | $4 y_{2}^{2}$ |
| 6 | 11 | $108 y_{1} y_{2}$ |
| 7 | 3 | $1$ |
| 7 | 5 | $2$ |
| 7 | 8 | $3 y_{2}$ |
| 7 | 9 | $8 y_{1}$ |
| 7 | 10 | $12 y_{1}$ |
| 7 | 11 | $144 y_{1} y_{2}$ |
| 8 | 4 | $2$ |
| 8 | 5 | $1$ |
| 8 | 8 | $- 2 y_{2}$ |
| 8 | 9 | $24 y_{1}$ |
| 8 | 10 | $56 y_{1}$ |
| 8 | 11 | $120 y_{1} y_{2}$ |
| 9 | 6 | $2$ |
| 9 | 7 | $- \frac{9}{4}$ |
| 9 | 8 | $- \frac{9}{2}$ |
| 9 | 10 | $9 y_{2}$ |
| 9 | 11 | $- 18 y_{1} + 4 y_{2}^{2}$ |
| 10 | 6 | $1$ |
| 10 | 7 | $\frac{7}{2}$ |
| 10 | 8 | $3$ |
| 10 | 11 | $12 y_{1}$ |
| 11 | 9 | $1$ |
| 11 | 10 | $\frac{7}{2}$ |

Curve enumeration: positive; 14 curve classes including zero.
