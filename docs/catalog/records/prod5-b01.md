---
title: "Complete intersection of multidegrees (2,2) in P³ × P³"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Complete intersection of multidegrees (2,2) in P³ × P³."
keywords: ["dimension 5", "fivefold", "Complete intersection in a product of projective spaces", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Complete intersection of multidegrees (2,2) in P³ × P³", "product of projective spaces", "regularized exponent multiset", "repeated exponents"]
---

# Complete intersection in \(\mathbb P^{3}\times \mathbb P^{3}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{3}\times \mathbb P^{3}\). Defining multidegrees in this factor order: `[[2, 2]]`.

[Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index:** 2. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)



## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z\) | 1 | 4 |
| \(z^{8} - 320 z^{6} - 170496 z^{4} - 15810560 z^{2} + 65536\) | 8 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2}\}\!\}\) |
| \(\lambda^{8} - 320 \lambda^{6} - 170496 \lambda^{4} - 15810560 \lambda^{2} + 65536=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-fivefolds.json) · [Hodge data and atomic invariants](../invariants-fivefolds.md#prod5-b01). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{3}\times\mathbb P^{3}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 2]]
residual_product_degrees = [2, 2]
```

The residual product degrees give the anticanonical class. 

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $2$, $(-K_X)^5=1280$, $e(X)=-128$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&1&&69&&69&&1&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=1$, $h^{3,2}=69$; even rank 12; odd rank 140.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, -1, -66)$.

```python
chern_numbers = {'c1_5': 1280, 'c1_3_c2': 1024, 'c1_c2_2': 832, 'c1_2_c3': 192, 'c2_c3': 160, 'c1_c4': 224, 'c5': -128}
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
K = [[2, 0, 0, 0, 2, 0, 0, 0]]
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

Write $A(\mathbf y)=c_1(X)\star$ and use the ordered basis $e_0,\ldots,e_{11}$ below. Columns are images: $A(\mathbf y)e_j=\sum_i A_{ij}(\mathbf y)e_i$.

```python
basis = ['1', 'x4', 'x0', 'x4^2', 'x0^2', 'x0*x4', 'x4^3', 'x0^3', 'x0*x4^2', 'x0*x4^3', 'x0^3*x4', 'x0^2*x4^3']
```


$$
G=\operatorname{diag}\!\left(- \frac{5}{2},- \frac{3}{2},- \frac{3}{2},- \frac{1}{2},- \frac{1}{2},- \frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{3}{2},\frac{3}{2},\frac{5}{2}\right).
$$


**Exact matrix:**  every nonzero entry is listed below; all omitted entries are zero. Indices are zero based. No Novikov specialization has been made in this table.

| Row $i$ | Column $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $4 y_{1}$ |
| 0 | 2 | $4 y_{2}$ |
| 0 | 6 | $32 y_{1} y_{2}$ |
| 0 | 7 | $32 y_{1} y_{2}$ |
| 0 | 8 | $80 y_{1} y_{2}$ |
| 0 | 11 | $96 y_{1}^{2} y_{2} + 96 y_{1} y_{2}^{2}$ |
| 1 | 0 | $2$ |
| 1 | 3 | $4 y_{1}$ |
| 1 | 4 | $12 y_{2}$ |
| 1 | 5 | $4 y_{2}$ |
| 1 | 9 | $80 y_{1} y_{2}$ |
| 1 | 10 | $64 y_{1} y_{2}$ |
| 2 | 0 | $2$ |
| 2 | 3 | $12 y_{1}$ |
| 2 | 4 | $4 y_{2}$ |
| 2 | 5 | $4 y_{1}$ |
| 2 | 9 | $64 y_{1} y_{2}$ |
| 2 | 10 | $80 y_{1} y_{2}$ |
| 3 | 1 | $2$ |
| 3 | 7 | $8 y_{2}$ |
| 3 | 8 | $4 y_{2}$ |
| 3 | 11 | $32 y_{1} y_{2}$ |
| 4 | 2 | $2$ |
| 4 | 6 | $8 y_{1}$ |
| 4 | 8 | $12 y_{1}$ |
| 4 | 11 | $32 y_{1} y_{2}$ |
| 5 | 1 | $2$ |
| 5 | 2 | $2$ |
| 5 | 6 | $4 y_{1}$ |
| 5 | 7 | $4 y_{2}$ |
| 5 | 8 | $4 y_{1}$ |
| 5 | 11 | $48 y_{1} y_{2}$ |
| 6 | 3 | $2$ |
| 6 | 4 | $-2$ |
| 6 | 5 | $-2$ |
| 6 | 9 | $- 4 y_{1} + 4 y_{2}$ |
| 6 | 10 | $8 y_{2}$ |
| 7 | 4 | $4$ |
| 7 | 5 | $2$ |
| 7 | 9 | $12 y_{1}$ |
| 7 | 10 | $4 y_{1}$ |
| 8 | 3 | $2$ |
| 8 | 4 | $2$ |
| 8 | 5 | $4$ |
| 8 | 9 | $4 y_{1}$ |
| 8 | 10 | $4 y_{2}$ |
| 9 | 6 | $2$ |
| 9 | 8 | $4$ |
| 9 | 11 | $4 y_{2}$ |
| 10 | 7 | $2$ |
| 10 | 8 | $2$ |
| 10 | 11 | $4 y_{1}$ |
| 11 | 9 | $2$ |
| 11 | 10 | $2$ |

Curve enumeration: positive; 8 curve classes including zero.
