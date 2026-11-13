---
title: "Quadric section of the adjoint G₂ variety"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Quadric section of the adjoint G₂ variety."
keywords: ["Quadric section of the adjoint G₂ variety", "dimension 4", "fourfold", "Fano", "index one", "irrationality", "very general", "regularized exponent multiset", "Hodge polynomial", "atomic invariants", "quantum cohomology", "adjoint G2", "quadric section"]
---

# Quadric section of the adjoint G₂ variety

[Universal catalogue](../index.md) · [Fourfolds](../fourfolds.md) · [Exact data](../../data/flag-fourfolds.json)

The smooth complete intersection \(G_2/P_2\cap Q\) has dimension four, Picard rank one and \(-K_X=h\). **A very general smooth member is irrational.** The conclusion uses the generic Hodge factor and connection exponents below.

## Reproduce the calculation

```python
from gwflags import FlagVariety

X = FlagVariety('G2', [2])
K = [[2]]
M, G, indices = X.small_quantum_multiplication(K, workers=0)
```

In the flag interface, enter algebra `G2`, kept roots `2` and **Bundle K** `2`, then choose **Compute quantum matrix**. The Python output uses the returned Schubert ordering, listed below.

```python
basis_indices = [0, 1, 2, 3, 4]
basis_words = [[], [2], [1, 2], [2, 1, 2], [1, 2, 1, 2]]
curve_classes = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
```

The matrix is computed by virtual localization over the complete automatically supported curve list. The exact result includes the ordered basis, grading and full curve list.

## Exact operator and grading

Columns are images of the ordered ambient basis. Write \(A(y_1)=c_1(TX)\star\).

$$
A(y_1)=\left[\begin{matrix}0 & 252 y_{1}^{2} & 4032 y_{1}^{3} & 68256 y_{1}^{4} & 285120 y_{1}^{5}\\1 & 12 y_{1} & 312 y_{1}^{2} & 5328 y_{1}^{3} & 22752 y_{1}^{4}\\0 & 3 & 18 y_{1} & 468 y_{1}^{2} & 2016 y_{1}^{3}\\0 & 0 & 2 & 12 y_{1} & 84 y_{1}^{2}\\0 & 0 & 0 & 3 & 0\end{matrix}\right],\qquad G=\left[\begin{matrix}-2 & 0 & 0 & 0 & 0\\0 & -1 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 1 & 0\\0 & 0 & 0 & 0 & 2\end{matrix}\right].
$$

At \(y_1=1\),

$$
\chi_{A(1)}(\lambda)=\left(\lambda + 6\right)^{3} \left(\lambda^{2} - 60 \lambda - 828\right),\qquad\Delta(1)=\det(1,A(1)1,\ldots,A(1)^4 1)=324\ne0.
$$

The determinant uses the returned basis. It proves cyclicity on the five-dimensional ambient sector. For a very general member, this sector equals the rational Hodge-invariant cohomology; the generic Hodge-factor criterion therefore applies. Homogeneous rescaling of the Novikov coordinate gives the corresponding admissible small-locus point.

## Regularized exponent multisets

The eigenvalues here are those of \(A\). The software’s characteristic factors for \(K^F=-A\) correspond by \(p(-\lambda)=0\). Repeated entries are retained.

| Eigenvalue of \(A(1)\) | Multiplicity per eigenvalue | \(F_{b,\lambda}\) |
|---|---:|---|
| \(-6\) | 3 | \(\{\!\{0,\tfrac12,\tfrac12\}\!\}\) |
| \(30 \pm 24\sqrt{3}\) (each) | 1 | \(\{\!\{0\}\!\}\) |

The fourfold rationality criterion permits only the pairs \((1,\{\!\{0\}\!\})\), \((2,\{\!\{\tfrac12,\tfrac12\}\!\})\), and \((3,\{\!\{0,0,0\}\!\})\). The cyclic rank-three factor above has a different exponent multiset. This gives irrationality for a **very general smooth** member, as in Theorem 6.16 of *On the atomic decomposition of complete intersection in flag varieties*. It is not a claim about every special member.

## Full atomic Hodge invariants

Here \(\rho_\alpha\) counts rational Hodge-invariant classes; \(P_\alpha(t)=\sum_{p,q}h^{p,q}(E_\alpha)t^{p-q}\) is the Hodge polynomial. Its constant coefficient need not equal \(\rho_\alpha\).

| Generic coarse atom | Number of conjugate atoms | \(\rho_\alpha\) | Full rank per atom | \(P_\alpha(t)\) |
|---|---:|---:|---:|---|
| Triple-eigenvalue factor | 1 | 3 | 130 | \(14t^2+102+14t^{-2}\) |
| Simple-eigenvalue factors | 2 | 1 | 1 | \(1\) (each) |

The full Hodge numbers are \(h^{0,0}=h^{1,1}=h^{3,3}=h^{4,4}=1\), \(h^{2,2}=100\), and \(h^{3,1}=h^{1,3}=14\). Thus \(P_X(t)=14t^2+104+14t^{-2}\), and the displayed atomic polynomials sum to it.

For the primitive assignment, the Lefschetz-pencil monodromy acts irreducibly on the vanishing middle cohomology, and quantum multiplication commutes with it. Its action there is therefore a rational scalar. The characteristic relation of the ambient operator annihilates the full quantum ring, since it annihilates the unit and multiplication is associative. The only rational root at this point is \(-6\), so all vanishing cohomology belongs to that factor. Its \((3,1),(2,2),(1,3)\) dimensions are \(14,99,14\). Adding the three ambient classes gives its stated polynomial and full rank. The other two factors are Tate. This uses the very-general Hodge identification and the monodromy hypotheses, in addition to the cyclic determinant.
