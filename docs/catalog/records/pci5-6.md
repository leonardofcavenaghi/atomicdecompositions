---
title: "Degree-6 fivefold in P⁶"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Degree-6 fivefold in P⁶."
keywords: ["dimension 5", "fivefold", "Projective complete intersection", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Degree-6 fivefold in P⁶", "projective space", "regularized exponent multiset", "repeated exponents"]
---

# Degree-6 fivefold in \(\mathbb P^{6}\)

**Geometric presentation.** Ambient variety: \(\mathbb P^{6}\). Defining multidegrees in this factor order: `[[6]]`.

[Geometric identification](../sources.md#geometric-identification).

**Construction:** Projective complete intersection. **Dimension:** 5. **Index:** 1. **h(1,1):** 1.


[Catalogue](../index.md) · [5-folds](../fivefolds.md)



## Spectrum and connection exponents

**Parameter point:** `y1=2`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 1440\) | 1 | 5 |
| \(z - 91872\) | 1 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 1440=0\) | \(\{\!\{0,\frac{1}{6},\frac{1}{3},\frac{2}{3},\frac{5}{6}\}\!\}\) |
| \(\lambda - 91872=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-fivefolds.json) · [Hodge data and atomic invariants](../invariants-fivefolds.md#pci5-6). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Construction and Hodge data

A smooth complete intersection of multidegree $(6)$ in $\mathbb P^{6}$.
Adjunction gives $-K_X=1H$.

### Invariants and full Hodge diamond

$\dim X=5$, $h^{1,1}=1$, index $1$, $(-K_X)^5=6$, $e(X)=-13014$.


$$
\begin{array}{ccccccccccc}&&&&&1&&&&&\\&&&&0&&0&&&&\\&&&0&&1&&0&&&\\&&0&&0&&0&&0&&\\&0&&0&&1&&0&&0&\\0&&455&&6055&&6055&&455&&0\\&0&&0&&1&&0&&0&\\&&0&&0&&0&&0&&\\&&&0&&1&&0&&&\\&&&&0&&0&&&&\\&&&&&1&&&&&\end{array}
$$


$h^{4,1}=455$, $h^{3,2}=6055$; even rank 6; odd rank 13020.
Independent K-theory check: $(\chi(\mathcal O_X),\chi(\Omega_X^1),\chi(\Omega_X^2))=(1, 454, -6054)$.

```python
chern_numbers = {'c1_5': 6, 'c1_3_c2': 90, 'c1_c2_2': 1350, 'c1_2_c3': -330, 'c2_c3': -4950, 'c1_c4': 2190, 'c5': -13014}
```

### Exact software inputs

Ray order and zero-based cone indices must be preserved; K consists of full ray-coefficient rows.

```python
rays = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [-1, -1, -1, -1, -1, -1]]
cones = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 6], [0, 1, 2, 3, 5, 6], [0, 1, 2, 4, 5, 6],
 [0, 1, 3, 4, 5, 6], [0, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
K = [[6, 0, 0, 0, 0, 0, 0]]
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
| 0 | 1 | $13932000 y_{1}^{2}$ |
| 0 | 2 | $432265248000 y_{1}^{3}$ |
| 0 | 3 | $10524957538752000 y_{1}^{4}$ |
| 0 | 4 | $110441973189864960000 y_{1}^{5}$ |
| 0 | 5 | $261960335825727283200000 y_{1}^{6}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $5544 y_{1}$ |
| 1 | 2 | $177529968 y_{1}^{2}$ |
| 1 | 3 | $4331668617216 y_{1}^{3}$ |
| 1 | 4 | $46081933709444352 y_{1}^{4}$ |
| 1 | 5 | $110441973189864960000 y_{1}^{5}$ |
| 2 | 1 | $1$ |
| 2 | 2 | $15624 y_{1}$ |
| 2 | 3 | $398584800 y_{1}^{2}$ |
| 2 | 4 | $4331668617216 y_{1}^{3}$ |
| 2 | 5 | $10524957538752000 y_{1}^{4}$ |
| 3 | 2 | $1$ |
| 3 | 3 | $15624 y_{1}$ |
| 3 | 4 | $177529968 y_{1}^{2}$ |
| 3 | 5 | $432265248000 y_{1}^{3}$ |
| 4 | 3 | $1$ |
| 4 | 4 | $5544 y_{1}$ |
| 4 | 5 | $13932000 y_{1}^{2}$ |
| 5 | 4 | $1$ |

Curve enumeration: positive; 7 curve classes including zero.
