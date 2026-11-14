---
title: "Verra fourfold (HLM-29)"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Verra fourfold (HLM-29)."
keywords: ["HLM-29", "dimension 4", "fourfold", "Verra fourfold", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "Hausen Laface Mauz", "HLM", "split projective bundle", "regularized exponent multiset", "repeated exponents"]
---

# Verra fourfold

**Geometric presentation.** Ambient variety: \(\mathbb P_{\mathbb P^{2}}(\mathcal O\oplus \mathcal O(1)^{\oplus 3})\), in the quotient convention. With \(H\) the pullback of the base hyperplane class and \(\xi=c_1(\mathcal O(1))\), the defining divisors are \(2\xi\).

Source identifier: **HLM-29**; see [CKP and HLM terminology](../sources.md). [Geometric identification](../sources.md#geometric-identification).

**Construction:** Verra fourfold. **Dimension:** 4. **Index:** 2. **h(1,1):** 2.


[Catalogue](../index.md) · [4-folds](../fourfolds.md)



## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z\) | 1 | 3 |
| \(z^{6} - 432 z^{4} - 62208 z^{2} - 2985984\) | 6 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda=0\) | \(\{\!\{0,0,0\}\!\}\) |
| \(\lambda^{6} - 432 \lambda^{4} - 62208 \lambda^{2} - 2985984=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-fourfolds.json) · [Hodge data and atomic invariants](../invariants-fourfolds.md#hlm-29). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** nef defining divisors.
Verra fourfold
**Hodge source:**  HLM-29, HLM Proposition 7.2, [1907.08000v3](https://arxiv.org/abs/1907.08000v3).
$\dim X=4$, $\dim Y=5$, codimension $1$, index $2$, $(-K_X)^4=192$, $e(X)=30$.


$$
\begin{array}{ccccccccc}&&&&1&&&&\\&&&0&&0&&&\\&&0&&2&&0&&\\&0&&0&&0&&0&\\0&&1&&22&&1&&0\\&0&&0&&0&&0&\\&&0&&2&&0&&\\&&&0&&0&&&\\&&&&1&&&&\end{array}
$$


Ambient rank: 9; full even rank: 30; full odd rank: 0. The complement of the ambient image in middle cohomology has dimension 21.


$$
\begin{aligned}\int_Xc_1^4&=192,&\int_Xc_1^2c_2&=144\\\int_Xc_2^2&=114,&\int_Xc_1c_3&=24\\\int_Xc_4&=30,&\chi(\mathcal O_X)&=1.\end{aligned}
$$



### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
weights = [[1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1]]
bundles = [[2, 2]]
rays = [[-1, -1, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, -1, -1, -1], [0, 0, 1, 0, 0],
 [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
cones = [[0, 1, 2, 4, 5], [0, 1, 2, 4, 6], [0, 1, 2, 5, 6], [0, 1, 3, 4, 5], [0, 1, 3, 4, 6],
 [0, 1, 3, 5, 6], [0, 2, 3, 4, 5], [0, 2, 3, 4, 6], [0, 2, 3, 5, 6], [1, 2, 3, 4, 5],
 [1, 2, 3, 4, 6], [1, 2, 3, 5, 6]]
K = [[2, 0, 0, 0, 2, 0, 0]]
novikov_divisors = [[0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0]]
eval_y = {'y1': 2, 'y2': 3}
```

**Ordered ambient basis:** 

```python
['1', 'x3', 'x0', 'x3^2', 'x0^2', 'x0*x3', 'x0*x3^2', 'x0^2*x3', 'x0*x3^3']
```

## Complete curve images

The quadric is disjoint from the section corresponding to the trivial summand. Indeed, a quadric containing that section would have anticanonical degree zero on its base curves and would not be Fano. Projection from the section realizes the fourfold as a finite double cover of \(\mathbb P^2\times\mathbb P^2\), branched in bidegree \((2,2)\). If \(H,L\) are the two hyperplane classes, then \(\xi|_X=H+L\) and \(c_1(TX)=2(H+L)\).

For an effective curve put \(a=H\cdot C\) and \(b=L\cdot C\). These are nonnegative integers. A contribution to the fourfold operator has \(2(a+b)\le5\), so \(a+b\le2\). In the stated ray order, its ambient image is \((b,b,b,a+b,a,a,a)\). This gives the exhaustive list below; it does not assert existence of a curve for every candidate image.

```python
from gwtoric import ToricVariety

ambient = ToricVariety(rays, cones)
betas = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 2, 2, 2, 2],
         [1, 1, 1, 2, 1, 1, 1],
         [2, 2, 2, 2, 0, 0, 0]]
A, G, basis = ambient.small_quantum_multiplication(
    betas=betas, K=K, workers=1, cache=False)
```

The existing localization routine on this list reproduces the displayed symbolic matrix, ordered basis and grading exactly.
