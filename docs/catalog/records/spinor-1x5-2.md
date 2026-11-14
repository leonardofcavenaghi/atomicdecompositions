---
title: "Five hyperplanes and a quadric in the spinor tenfold"
description: "Exact inputs, quantum multiplication, connection exponents and atomic Hodge invariants for Five hyperplanes and a quadric in the spinor tenfold."
keywords: ["Five hyperplanes and a quadric in the spinor tenfold", "spinor tenfold", "orthogonal Grassmannian", "five hyperplanes", "quadric section", "D5", "fourfold", "dimension 4", "Fano", "index one", "irrationality", "very general", "regularized exponent multiset", "Hodge polynomial", "atomic invariants", "quantum cohomology"]
---

# Five hyperplanes and a quadric in the spinor tenfold

[Universal catalogue](../index.md) · [Fourfolds](../fourfolds.md) · [Exact data](../../data/flag-fourfolds.json)

Let \(S=\operatorname{OGr}_+(5,10)\subset\mathbb P^{15}\) be a connected component of the maximal orthogonal Grassmannian, in its half-spinor embedding. A smooth zero locus of \(\mathcal O_S(1)^{\oplus5}\oplus\mathcal O_S(2)\) is a fourfold with Picard rank one and \(-K_X=h\). **A very general smooth member is irrational.**

## Reproduce the calculation

```python
from gwflags import FlagVariety

S = FlagVariety("D5", [4])
K = [[1], [1], [1], [1], [1], [2]]
M, G, indices = S.small_quantum_multiplication(K, workers=0)
```

In the flag interface, enter algebra `D5`, kept roots `4` and **Bundle K** `1;1;1;1;1;2`, then choose **Compute quantum matrix**. This is a substantial localization calculation; use the checkpoint and progress controls in flag 1.1.0.dev1 or the combined application for a long run.

```python
basis_indices = [0, 1, 2, 3, 5]
basis_words = [[], [4], [3, 4], [2, 3, 4], [1, 2, 3, 4]]
curve_classes = [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 2, 0], [0, 0, 0, 3, 0], [0, 0, 0, 4, 0], [0, 0, 0, 5, 0]]
```

The exact matrix uses the returned Schubert basis and the complete automatically supported curve list. It was computed with the existing virtual-localization routines and checked at two independent exact torus evaluations.

## Exact operator and grading

Columns are images of the ordered ambient basis. The Python variable `M` holds the first-Chern operator \(A(y_1)\).

$$
A(y_1)=\left[\begin{matrix}0 & 676 y_{1}^{2} & 55584 y_{1}^{3} & 1773408 y_{1}^{4} & 9838080 y_{1}^{5}\\1 & 24 y_{1} & 2736 y_{1}^{2} & 89376 y_{1}^{3} & 506688 y_{1}^{4}\\0 & 1 & 38 y_{1} & 1596 y_{1}^{2} & 9264 y_{1}^{3}\\0 & 0 & \frac{12}{7} & 24 y_{1} & \frac{1352 y_{1}^{2}}{7}\\0 & 0 & 0 & \frac{7}{2} & 0\end{matrix}\right],\qquad G=\left[\begin{matrix}-2 & 0 & 0 & 0 & 0\\0 & -1 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 1 & 0\\0 & 0 & 0 & 0 & 2\end{matrix}\right].
$$

## Spectrum and connection exponents

**Parameter point:** `y1=1`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z + 10\) | 1 | 3 |
| \(z^{2} - 116 z - 1244\) | 2 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=\frac{72}{7}\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda + 10=0\) | \(\{\!\{0,\frac{1}{2},\frac{1}{2}\}\!\}\) |
| \(\lambda^{2} - 116 \lambda - 1244=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/flag-fourfolds.json) · [Hodge data and atomic invariants](../invariants-fourfolds.md#spinor-1x5-2). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

The cyclic rank-three factor at \(\lambda=-10\) has exponent multiset \(\{\!\{0,\tfrac12,\tfrac12\}\!\}\). The fourfold rationality criterion permits only \((1,\{\!\{0\}\!\})\), \((2,\{\!\{\tfrac12,\tfrac12\}\!\})\), and \((3,\{\!\{0,0,0\}\!\})\). Together with the very-general Hodge identification, this excludes rationality for a very general smooth member.

## Full Hodge and atomic invariants

The Hodge numbers are \(h^{0,0}=h^{1,1}=h^{3,3}=h^{4,4}=1\), \(h^{2,2}=112\), and \(h^{3,1}=h^{1,3}=16\); all other entries vanish. Hence \(P_X(t)=16t^2+116+16t^{-2}\) and the full cohomology has dimension \(148\). The Hodge computation satisfies the Euler and Todd identities at two exact torus points.

| Spectral condition | Number of conjugate atoms | \(\rho_\alpha\) per atom | Full dimension per atom | \(P_\alpha(t)\) per atom |
|---|---:|---:|---:|---|
| \(\lambda=-10\) | 1 | 3 | 146 | \(16t^2+114+16t^{-2}\) |
| \(\lambda^2-116\lambda-1244=0\) | 2 | 1 | 1 | \(1\) |

For a very general member, the ambient space is the full rational Hodge-invariant sector. Monodromy acts irreducibly on the vanishing middle cohomology, so first-Chern multiplication acts there by a rational scalar. The ambient characteristic relation annihilates the unit and hence the full quantum ring by associativity. Its only rational root is \(-10\); the vanishing cohomology therefore belongs to that factor. Its Hodge dimensions are \(16,111,16\). Adding its three ambient classes gives the polynomial above; the other two atoms are Tate. The polynomials sum to \(P_X(t)\), and their dimensions sum to \(148\). See the [atomic criterion and proof rules](../atomic-invariants.md).
