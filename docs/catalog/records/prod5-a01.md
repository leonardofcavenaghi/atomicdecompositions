---
title: "Complete intersection of multidegrees (2,2) in P² × P⁴"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Complete intersection of multidegrees (2,2) in P² × P⁴."
keywords: ["dimension 5", "fivefold", "Complete intersection in a product of projective spaces", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Complete intersection of multidegrees (2,2) in P² × P⁴", "product of projective spaces", "regularized exponent multiset", "repeated exponents"]
---

# Complete intersection in \(\mathbb P^{2}\times \mathbb P^{4}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{2}\times \mathbb P^{4}\). Defining multidegrees in this factor order: `[[2, 2]]`.

[Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection in a product of projective spaces. **Dimension:** 5. **Index:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)



## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 6\) | 1 | 3 |
| \(z^{9} - 6 z^{8} - 144 z^{7} + 216 z^{6} - 176256 z^{5} - 6850080 z^{4} - 99116352 z^{3} - 704153088 z^{2} - 2492052480 z - 3546878976\) | 9 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-9627879200246720310068419083055793112346911571968\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 6=0\) | \(\{\!\{0,0,0\}\!\}\) |
| \(\lambda^{9} - 6 \lambda^{8} - 144 \lambda^{7} + 216 \lambda^{6} - 176256 \lambda^{5} - 6850080 \lambda^{4} - 99116352 \lambda^{3} - 704153088 \lambda^{2} - 2492052480 \lambda - 3546878976=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-fivefolds.json) · [Hodge data and atomic invariants](../invariants-fivefolds.md#prod5-a01). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Construction and Hodge data

A smooth complete intersection in $Y=\mathbb P^{2}\times\mathbb P^{4}$; the rows below are the defining multidegrees in the displayed factor order.

```python
multidegrees = [[2, 2]]
residual_product_degrees = [1, 3]
```

The residual product degrees give the anticanonical class. 

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=2$, index $1$, $(-K_X)^5=1350$, $e(X)=-58$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&2&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&3&&0&&0&\\0&&0&&35&&35&&0&&0\\&0&&0&&3&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&2&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=0$, $h^{3,2}=35$; even rank 12; odd rank 70.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, -2, -32)$.

```python
chern_numbers = {'c1_5': 1350, 'c1_3_c2': 1098, 'c1_c2_2': 822, 'c1_2_c3': 250, 'c2_c3': 200, 'c1_c4': 178, 'c5': -58}
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
K = [[2, 0, 0, 2, 0, 0, 0, 0]]
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
| 0 | 2 | $4 y_{2}^{2}$ |
| 0 | 3 | $6 y_{1}$ |
| 0 | 6 | $80 y_{1} y_{2}$ |
| 0 | 7 | $80 y_{1} y_{2}$ |
| 0 | 8 | $32 y_{1} y_{2}$ |
| 0 | 9 | $160 y_{1} y_{2}^{2}$ |
| 0 | 10 | $440 y_{1} y_{2}^{2}$ |
| 0 | 11 | $384 y_{1} y_{2}^{3}$ |
| 1 | 0 | $3$ |
| 1 | 2 | $6 y_{2}$ |
| 1 | 4 | $4 y_{2}^{2}$ |
| 1 | 5 | $4 y_{2}^{2}$ |
| 1 | 6 | $6 y_{1}$ |
| 1 | 9 | $80 y_{1} y_{2}$ |
| 1 | 10 | $144 y_{1} y_{2}$ |
| 1 | 11 | $280 y_{1} y_{2}^{2}$ |
| 2 | 0 | $1$ |
| 2 | 6 | $18 y_{1}$ |
| 2 | 7 | $6 y_{1}$ |
| 2 | 9 | $64 y_{1} y_{2}$ |
| 2 | 10 | $144 y_{1} y_{2}$ |
| 2 | 11 | $160 y_{1} y_{2}^{2}$ |
| 3 | 1 | $3$ |
| 3 | 4 | $4 y_{2}$ |
| 3 | 5 | $6 y_{2}$ |
| 3 | 7 | $4 y_{2}^{2}$ |
| 3 | 8 | $4 y_{2}^{2}$ |
| 3 | 11 | $32 y_{1} y_{2}$ |
| 4 | 2 | $1$ |
| 4 | 4 | $- 2 y_{2}$ |
| 4 | 9 | $12 y_{1}$ |
| 4 | 10 | $18 y_{1}$ |
| 4 | 11 | $32 y_{1} y_{2}$ |
| 5 | 1 | $1$ |
| 5 | 2 | $3$ |
| 5 | 4 | $2 y_{2}$ |
| 5 | 9 | $6 y_{1}$ |
| 5 | 10 | $6 y_{1}$ |
| 5 | 11 | $48 y_{1} y_{2}$ |
| 6 | 3 | $3$ |
| 6 | 7 | $6 y_{2}$ |
| 6 | 8 | $4 y_{2}$ |
| 6 | 10 | $4 y_{2}^{2}$ |
| 7 | 3 | $1$ |
| 7 | 5 | $3$ |
| 7 | 8 | $2 y_{2}$ |
| 8 | 4 | $3$ |
| 8 | 5 | $1$ |
| 8 | 8 | $- 2 y_{2}$ |
| 8 | 11 | $6 y_{1}$ |
| 9 | 6 | $3$ |
| 9 | 7 | $-1$ |
| 9 | 8 | $-3$ |
| 9 | 10 | $6 y_{2}$ |
| 9 | 11 | $4 y_{2}^{2}$ |
| 10 | 6 | $1$ |
| 10 | 7 | $4$ |
| 10 | 8 | $3$ |
| 11 | 9 | $1$ |
| 11 | 10 | $4$ |

Curve enumeration: positive; 10 curve classes including zero.
