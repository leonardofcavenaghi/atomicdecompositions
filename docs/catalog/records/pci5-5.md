---
title: "Quintic fivefold in P⁶"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Quintic fivefold in P⁶."
keywords: ["dimension 5", "fivefold", "Projective complete intersection", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Quintic fivefold in P⁶", "projective space", "regularized exponent multiset", "repeated exponents"]
---

# Quintic fivefold in \(\mathbb P^{6}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{6}\). Defining multidegrees in this factor order: `[[5]]`.

[Geometric identification](../sources.md#geometric-identification).

**Construction:** Projective complete intersection. **Dimension:** 5. **Index:** 2. **h(1,1):** 1.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)



## Spectrum and connection exponents

**Parameter point:** `y1=2`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z\) | 1 | 4 |
| \(z^{2} - 25000\) | 2 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=32768\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda=0\) | \(\{\!\{\frac{1}{10},\frac{3}{10},\frac{7}{10},\frac{9}{10}\}\!\}\) |
| \(\lambda^{2} - 25000=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-fivefolds.json) · [Hodge data and atomic invariants](../invariants-fivefolds.md#pci5-5). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Construction and Hodge data

A smooth complete intersection of multidegree $(5)$ in $\mathbb P^{6}$.
Adjunction gives $-K_X=2H$.

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=1$, index $2$, $(-K_X)^5=160$, $e(X)=-3270$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&1&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&1&&0&&0&\\0&&84&&1554&&1554&&84&&0\\&0&&0&&1&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&1&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=84$, $h^{3,2}=1554$; even rank 6; odd rank 3276.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 83, -1553)$.

```python
chern_numbers = {'c1_5': 160, 'c1_3_c2': 440, 'c1_c2_2': 1210, 'c1_2_c3': -400, 'c2_c3': -1100, 'c1_c4': 1350, 'c5': -3270}
```

### Exact software inputs

Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

```python
rays = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [-1, -1, -1, -1, -1, -1]]
cones = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 6], [0, 1, 2, 3, 5, 6], [0, 1, 2, 4, 5, 6],
 [0, 1, 3, 4, 5, 6], [0, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
K = [[5, 0, 0, 0, 0, 0, 0]]
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

Write $A(\mathbf y)=c_1(X)\star$ and use the ordered basis $e_0,\ldots,e_{5}$ below. Columns are images: $A(\mathbf y)e_j=\sum_i A_{ij}(\mathbf y)e_i$.

```python
basis = ['1', 'x0', 'x0^2', 'x0^3', 'x0^4', 'x0^5']
```


$$
G=\operatorname{diag}\!\left(- \frac{5}{2},- \frac{3}{2},- \frac{1}{2},\frac{1}{2},\frac{3}{2},\frac{5}{2}\right).
$$


**Exact matrix:**  every nonzero entry is listed below; all omitted entries are zero. Indices are zero based. No Novikov specialization has been made in this table.

| Row $i$ | Column $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $240 y_{1}$ |
| 0 | 3 | $422400 y_{1}^{2}$ |
| 0 | 5 | $62640000 y_{1}^{3}$ |
| 1 | 0 | $2$ |
| 1 | 2 | $1540 y_{1}$ |
| 1 | 4 | $1385000 y_{1}^{2}$ |
| 2 | 1 | $2$ |
| 2 | 3 | $2690 y_{1}$ |
| 2 | 5 | $422400 y_{1}^{2}$ |
| 3 | 2 | $2$ |
| 3 | 4 | $1540 y_{1}$ |
| 4 | 3 | $2$ |
| 4 | 5 | $240 y_{1}$ |
| 5 | 4 | $2$ |

Curve enumeration: positive; 4 curve classes including zero.
