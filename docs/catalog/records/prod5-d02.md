---
title: "Complete intersection of multidegrees (2,1), (1,2) in P³ × P⁴"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Complete intersection of multidegrees (2,1), (1,2) in P³ × P⁴."
keywords: ["dimension 5", "fivefold", "Complete intersection in a product of projective spaces", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Complete intersection of multidegrees (2,1), (1,2) in P³ × P⁴", "product of projective spaces", "regularized exponent multiset", "repeated exponents"]
---

# Complete intersection in \(\mathbb P^{3}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{3}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[2, 1], [1, 2]]`.

[Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)



## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 6\) | 1 | 4 |
| \(z^{8} - 12 z^{7} - 200 z^{6} - 59952 z^{5} - 2777844 z^{4} - 47551872 z^{3} - 385153376 z^{2} - 1500089472 z - 2265748124\) | 8 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 6=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2}\}\!\}\) |
| \(\lambda^{8} - 12 \lambda^{7} - 200 \lambda^{6} - 59952 \lambda^{5} - 2777844 \lambda^{4} - 47551872 \lambda^{3} - 385153376 \lambda^{2} - 1500089472 \lambda - 2265748124=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-fivefolds.json) · [Hodge data and atomic invariants](../invariants-fivefolds.md#prod5-d02). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{3}\times\mathbb P^{4}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 1], [1, 2]]
residual_product_degrees = [1, 2]
```

The residual product degrees give the anticanonical class. 

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=640$, $e(X)=-128$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&1&&69&&69&&1&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=1$, $h^{3,2}=69$; even rank 12; odd rank 140.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, -1, -66)$.

```python
chern_numbers = {'c1_5': 640, 'c1_3_c2': 704, 'c1_c2_2': 752, 'c1_2_c3': 112, 'c2_c3': 140, 'c1_c4': 224, 'c5': -128}
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
K = [[2, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 2, 0, 0, 0, 0]]
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

Write $A(\mathbf y)=c_1(X)\star$ and use the ordered basis $e_0,\ldots,e_{11}$ below. Columns are images: $A(\mathbf y)e_j=\sum_i A_{ij}(\mathbf y)e_i$.

```python
basis = ['1', 'x4', 'x0', 'x4^2', 'x0^2', 'x0*x4', 'x4^3', 'x0^3', 'x0*x4^2', 'x4^4', 'x0*x4^3', 'x0*x4^4']
```


$$
G=\operatorname{diag}\!\left(- \frac{5}{2},- \frac{3}{2},- \frac{3}{2},- \frac{1}{2},- \frac{1}{2},- \frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{3}{2},\frac{3}{2},\frac{5}{2}\right).
$$


**Exact matrix:**  every nonzero entry is listed below; all omitted entries are zero. Indices are zero based. No Novikov specialization has been made in this table.

| Row $i$ | Column $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $4 y_{1}$ |
| 0 | 2 | $4 y_{2}^{2}$ |
| 0 | 3 | $96 y_{1} y_{2}$ |
| 0 | 4 | $54 y_{1} y_{2}$ |
| 0 | 5 | $96 y_{1} y_{2}$ |
| 0 | 6 | $384 y_{1} y_{2}^{2}$ |
| 0 | 7 | $256 y_{1} y_{2}^{2}$ |
| 0 | 8 | $880 y_{1} y_{2}^{2}$ |
| 0 | 9 | $180 y_{1}^{2} y_{2} + 320 y_{1} y_{2}^{3}$ |
| 0 | 10 | $530 y_{1}^{2} y_{2} + 1760 y_{1} y_{2}^{3}$ |
| 0 | 11 | $2400 y_{1}^{2} y_{2}^{2} + 768 y_{1} y_{2}^{4}$ |
| 1 | 0 | $2$ |
| 1 | 2 | $7 y_{2}$ |
| 1 | 3 | $4 y_{1}$ |
| 1 | 4 | $10 y_{2}^{2}$ |
| 1 | 5 | $4 y_{2}^{2}$ |
| 1 | 6 | $165 y_{1} y_{2}$ |
| 1 | 7 | $24 y_{1} y_{2}$ |
| 1 | 8 | $216 y_{1} y_{2}$ |
| 1 | 9 | $320 y_{1} y_{2}^{2}$ |
| 1 | 10 | $1352 y_{1} y_{2}^{2}$ |
| 1 | 11 | $80 y_{1}^{2} y_{2} + 960 y_{1} y_{2}^{3}$ |
| 2 | 0 | $1$ |
| 2 | 3 | $14 y_{1}$ |
| 2 | 5 | $4 y_{1}$ |
| 2 | 6 | $120 y_{1} y_{2}$ |
| 2 | 7 | $42 y_{1} y_{2}$ |
| 2 | 8 | $216 y_{1} y_{2}$ |
| 2 | 9 | $128 y_{1} y_{2}^{2}$ |
| 2 | 10 | $640 y_{1} y_{2}^{2}$ |
| 2 | 11 | $180 y_{1}^{2} y_{2} + 320 y_{1} y_{2}^{3}$ |
| 3 | 1 | $2$ |
| 3 | 4 | $7 y_{2}$ |
| 3 | 5 | $7 y_{2}$ |
| 3 | 7 | $4 y_{2}^{2}$ |
| 3 | 8 | $4 y_{2}^{2}$ |
| 3 | 9 | $42 y_{1} y_{2}$ |
| 3 | 10 | $129 y_{1} y_{2}$ |
| 3 | 11 | $256 y_{1} y_{2}^{2}$ |
| 4 | 2 | $1$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 6 | $14 y_{1}$ |
| 4 | 8 | $14 y_{1}$ |
| 4 | 9 | $24 y_{1} y_{2}$ |
| 4 | 10 | $102 y_{1} y_{2}$ |
| 4 | 11 | $64 y_{1} y_{2}^{2}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $2$ |
| 5 | 4 | $5 y_{2}$ |
| 5 | 6 | $10 y_{1}$ |
| 5 | 8 | $4 y_{1}$ |
| 5 | 9 | $60 y_{1} y_{2}$ |
| 5 | 10 | $210 y_{1} y_{2}$ |
| 5 | 11 | $224 y_{1} y_{2}^{2}$ |
| 6 | 3 | $2$ |
| 6 | 4 | $- \frac{8}{21}$ |
| 6 | 5 | $- \frac{4}{21}$ |
| 6 | 7 | $2 y_{2}$ |
| 6 | 8 | $7 y_{2}$ |
| 6 | 9 | $- \frac{16 y_{1}}{21}$ |
| 6 | 10 | $- \frac{40 y_{1}}{21} + 4 y_{2}^{2}$ |
| 6 | 11 | $\frac{52 y_{1} y_{2}}{7}$ |
| 7 | 4 | $\frac{106}{21}$ |
| 7 | 5 | $\frac{85}{42}$ |
| 7 | 7 | $- 2 y_{2}$ |
| 7 | 9 | $\frac{254 y_{1}}{21}$ |
| 7 | 10 | $\frac{719 y_{1}}{21}$ |
| 7 | 11 | $\frac{424 y_{1} y_{2}}{7}$ |
| 8 | 3 | $1$ |
| 8 | 4 | $\frac{20}{21}$ |
| 8 | 5 | $\frac{52}{21}$ |
| 8 | 7 | $2 y_{2}$ |
| 8 | 9 | $\frac{40 y_{1}}{21}$ |
| 8 | 10 | $\frac{100 y_{1}}{21}$ |
| 8 | 11 | $\frac{248 y_{1} y_{2}}{7}$ |
| 9 | 6 | $2$ |
| 9 | 7 | $-5$ |
| 9 | 8 | $- \frac{21}{4}$ |
| 9 | 10 | $7 y_{2}$ |
| 9 | 11 | $- 10 y_{1} + 4 y_{2}^{2}$ |
| 10 | 6 | $1$ |
| 10 | 7 | $2$ |
| 10 | 8 | $\frac{9}{2}$ |
| 10 | 11 | $4 y_{1}$ |
| 11 | 9 | $1$ |
| 11 | 10 | $\frac{9}{2}$ |

Curve enumeration: positive; 14 curve classes including zero.
