---
title: "Section of P_{P³}(O ⊕ O(2)^2) by 2ξ (HLM-27)"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Section of P_{P³}(O ⊕ O(2)^2) by 2ξ (HLM-27)."
keywords: ["HLM-27", "dimension 4", "fourfold", "Complete intersection of codimension 1", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Hausen Laface Mauz", "HLM", "Section of P_{P³}(O ⊕ O(2)^2) by 2ξ", "split projective bundle", "regularized exponent multiset", "repeated exponents"]
---

# Complete intersection in \(\mathbb P_{\mathbb P^{3}}(\mathcal O\oplus \mathcal O(2)^{\oplus 2})\)

**Geometric presentation.** Ambient variety: \(\mathbb P_{\mathbb P^{3}}(\mathcal O\oplus \mathcal O(2)^{\oplus 2})\), in the quotient convention. With \(H\) the pullback of the base hyperplane class and \(\xi=c_1(\mathcal O(1))\), the defining divisors are \(2\xi\).

Source identifier: **HLM-27**; see [CKP and HLM terminology](../sources.md). [Geometric identification](../sources.md#geometric-identification).

**Construction:** Complete intersection of codimension 1. **Dimension:** 4. **Index:** 1. **h(1,1):** 2.


[Catalogue](../index.md) · [4-folds](../fourfolds.md)



## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 6\) | 1 | 4 |
| \(z^{4} - 24 z^{3} - 9000 z^{2} - 775008 z + 15594768\) | 4 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 6=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2}\}\!\}\) |
| \(\lambda^{4} - 24 \lambda^{3} - 9000 \lambda^{2} - 775008 \lambda + 15594768=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-fourfolds.json) · [Hodge data and atomic invariants](../invariants-fourfolds.md#hlm-27). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef defining divisors.
**Hodge source:**  HLM-27, HLM Proposition 7.2, [1907.08000v3](https://arxiv.org/abs/1907.08000v3).
$\dim X=4$, $\dim Y=5$, codimension $1$, index $1$, $(-K_X)^4=64$, $e(X)=184$.


$$
\begin{array}{ccccccccc}&&&&1&&&&\\&&&0&&0&&&\\&&0&&2&&0&&\\&0&&0&&0&&0&\\0&&20&&138&&20&&0\\&0&&0&&0&&0&\\&&0&&2&&0&&\\&&&0&&0&&&\\&&&&1&&&&\end{array}
$$


Ambient rank: 8; full even rank: 184; full odd rank: 0. The complement of the ambient image in middle cohomology has dimension 176.


$$
\begin{aligned}\int_Xc_1^4&=64,&\int_Xc_1^2c_2&=112\\\int_Xc_2^2&=192,&\int_Xc_1c_3&=-56\\\int_Xc_4&=184,&\chi(\mathcal O_X)&=1.\end{aligned}
$$


Minimum wall degrees of the defining bundles: [0]; minimum adjunction wall degree: 0.

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
weights = [[1, 1, 1, 0, 0, 0, 0], [0, 0, 2, 1, 1, 1, 1]]
bundles = [[2, 4]]
rays = [[-1, -1, 0, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [-2, 0, -1, -1, -1],
 [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
cones = [[0, 1, 3, 4, 5], [0, 1, 3, 4, 6], [0, 1, 3, 5, 6], [0, 1, 4, 5, 6], [0, 2, 3, 4, 5],
 [0, 2, 3, 4, 6], [0, 2, 3, 5, 6], [0, 2, 4, 5, 6], [1, 2, 3, 4, 5], [1, 2, 3, 4, 6],
 [1, 2, 3, 5, 6], [1, 2, 4, 5, 6]]
K = [[2, 0, 0, 4, 0, 0, 0]]
novikov_divisors = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:** 

```python
['1', 'x2', 'x0', 'x2^2', 'x0*x2', 'x2^3', 'x0*x2^2', 'x0*x2^3']
```

Curve enumeration: mori; 11 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x2', 'x0', 'x2^2', 'x0*x2', 'x2^3', 'x0*x2^2', 'x0*x2^3']
```


$$
G=\operatorname{diag}(-2,-1,-1,0,0,1,1,2)
$$


| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $48 y_{1} y_{2}^{2} + 4 y_{2}^{2}$ |
| 0 | 2 | $4 y_{2}^{2}$ |
| 0 | 3 | $2304 y_{1} y_{2}^{3}$ |
| 0 | 4 | $576 y_{1} y_{2}^{3}$ |
| 0 | 5 | $2304 y_{1}^{2} y_{2}^{4} + 22528 y_{1} y_{2}^{4}$ |
| 0 | 6 | $6144 y_{1} y_{2}^{4}$ |
| 0 | 7 | $46080 y_{1}^{2} y_{2}^{5} + 10240 y_{1} y_{2}^{5}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $4 y_{2}$ |
| 1 | 2 | $4 y_{2}$ |
| 1 | 3 | $160 y_{1} y_{2}^{2} + 8 y_{2}^{2}$ |
| 1 | 4 | $4 y_{2}^{2}$ |
| 1 | 5 | $7680 y_{1} y_{2}^{3}$ |
| 1 | 6 | $1920 y_{1} y_{2}^{3}$ |
| 1 | 7 | $6144 y_{1} y_{2}^{4}$ |
| 2 | 1 | $- 4 y_{2}$ |
| 2 | 2 | $- 4 y_{2}$ |
| 2 | 3 | $192 y_{1} y_{2}^{2} - 8 y_{2}^{2}$ |
| 2 | 4 | $48 y_{1} y_{2}^{2} - 4 y_{2}^{2}$ |
| 2 | 5 | $- 384 y_{1} y_{2}^{3}$ |
| 2 | 7 | $2304 y_{1}^{2} y_{2}^{4} - 2048 y_{1} y_{2}^{4}$ |
| 3 | 1 | $1$ |
| 3 | 3 | $8 y_{2}$ |
| 3 | 4 | $4 y_{2}$ |
| 3 | 5 | $48 y_{1} y_{2}^{2} + 12 y_{2}^{2}$ |
| 3 | 6 | $4 y_{2}^{2}$ |
| 3 | 7 | $576 y_{1} y_{2}^{3}$ |
| 4 | 2 | $1$ |
| 4 | 3 | $- 16 y_{2}$ |
| 4 | 4 | $- 8 y_{2}$ |
| 4 | 5 | $640 y_{1} y_{2}^{2} - 24 y_{2}^{2}$ |
| 4 | 6 | $160 y_{1} y_{2}^{2} - 8 y_{2}^{2}$ |
| 5 | 3 | $1$ |
| 5 | 5 | $12 y_{2}$ |
| 5 | 6 | $4 y_{2}$ |
| 5 | 7 | $4 y_{2}^{2}$ |
| 6 | 4 | $1$ |
| 6 | 5 | $- 36 y_{2}$ |
| 6 | 6 | $- 12 y_{2}$ |
| 6 | 7 | $48 y_{1} y_{2}^{2} - 12 y_{2}^{2}$ |
| 7 | 5 | $4$ |
| 7 | 6 | $1$ |
