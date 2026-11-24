---
title: GKMtools.jl — Companion GKM software in Julia and OSCAR
description: An overview of GKMtools.jl by Daniel Holmes and Giosuè Muratore, its equivariant Gromov–Witten and quantum Schubert tools in Julia/OSCAR, and how it complements GEOATOMS.
keywords: ["GKMtools.jl", "GKM spaces", "GKM graphs", "Daniel Holmes", "Giosuè Muratore", "Julia", "OSCAR", "equivariant Gromov-Witten invariants", "equivariant quantum cohomology", "quantum Schubert calculus", "Mihalcea algorithm", "quantum Chevalley formula", "exceptional Grassmannians", "orbifold GKM graphs", "Seidel spaces", "weighted blowups", "gwflags", "gwtoric", "gwapp", "GEOATOMS", "cross-verification"]
---

# GKMtools.jl

[**GKMtools.jl**](https://github.com/mgemath/GKMtools.jl) is an open-source Julia package (MIT License, current release [`v1.0.0`](https://github.com/mgemath/GKMtools.jl/releases/tag/v1.0.0)) developed by [Daniel Holmes](https://www.daniel-holmes.at/) (ISTA) and [Giosuè Muratore](https://sites.google.com/view/giosue-muratore) (CEMS.UL, University of Lisbon, and COPELABS/DEISI, Lusófona University). Built directly on the [OSCAR](https://www.oscar-system.org/) computer algebra system, it provides a general-purpose computational environment for Goresky–Kottwitz–MacPherson (GKM) spaces, their equivariant cohomology and vector bundles, equivariant Gromov–Witten invariants, and quantum cohomology.

While GEOATOMS (`gwflags`, `gwtoric`, `gwapp`) and GKMtools.jl share the same torus-localization foundations on flag and toric targets, the two projects are designed around complementary scopes, ecosystems, and mathematical questions. This page introduces GKMtools.jl, summarizes its capabilities, and outlines how the two tools complement and cross-verify one another.

[GKMtools.jl documentation](https://mgemath.github.io/GKMtools.jl/stable/){ .md-button .md-button--primary }
[GitHub repository](https://github.com/mgemath/GKMtools.jl){ .md-button }
[arXiv:2509.07562](https://arxiv.org/abs/2509.07562){ .md-button }
[arXiv:2610.37273](https://arxiv.org/abs/2610.37273){ .md-button }

## What GKMtools.jl excels at

GKMtools.jl represents spaces directly by their combinatorial GKM graphs—vertices for torus fixed points, edges (and standalone flags in the non-compact setting) for one-dimensional orbits, axial weights in the character lattice, and compatible GKM connections—rather than restricting to a single projective ambient presentation. Its architecture spans three main strengths.

### 1. General smooth, non-compact, and orbifold GKM geometry in OSCAR

- **Beyond flag and toric varieties.** Because computations operate on abstract GKM graphs, GKMtools.jl handles not only generalized flag varieties \(G/P\) and smooth toric varieties (imported directly from OSCAR's `NormalToricVariety`), but also smooth Schubert varieties, Bott–Samelson varieties, non-compact total spaces of equivariant vector bundles, non-algebraic Hamiltonian GKM manifolds (such as the twisted flag manifold), and abstract GKM graphs arising in realizability questions.
- **Orbifold GKM graphs.** Version `1.0.0` includes active support for orbifold and stacky GKM graphs encoding finite abelian vertex and flag isotropy groups, tangent representations, stacky weighted projective spaces, inertia stacks and twisted sectors, and orbifold vector bundles.
- **Geometric operations and cohomology.** The library implements smooth and weighted blowups along GKM subgraphs, products, projectivizations, Seidel spaces \(S_X \to \mathbb{P}^1\), and compatible connections (`:birkhoff_grothendieck`, `:cartan`, and `:algorithm`). Elements of the equivariant cohomology ring \(H_T^*(X;\mathbb{Q})\) are represented explicitly as GKM splines in \(\bigoplus_{p\in V} \mathbb{Q}[t_1,\ldots,t_r]\), with exact Chern classes, Poincaré duals, and equivariant integration inside OSCAR.

### 2. Full equivariant, descendent, and higher-genus Gromov–Witten theory

- **Equivariant invariants.** Starting from the GKM graph, `gromov_witten` computes \(T\)-equivariant invariants

$$
\mathrm{GW}^T_{X,g,m,\beta}(y_1,\ldots,y_m)
= \int_{\left[\overline{\mathcal{M}}_{g,m}(X,\beta)\right]_T^{\mathrm{vir}}}
\prod_{i=1}^{m} \operatorname{ev}_i^*(y_i)
\in H_T^*(\mathrm{pt};\mathbb{Q}) \cong \mathbb{Q}[t_1,\ldots,t_r],
$$

retaining full symbolic dependence on the equivariant parameters \(t_1,\ldots,t_r\) (and specializing to ordinary invariants when \(t_i = 0\)).
- **Positive genus, \(\psi\)-classes, and bundle twists.** In addition to primary genus-zero invariants, GKMtools.jl supports descendent insertions (`Psi`) on \(\overline{\mathcal{M}}_{g,m}(X,\beta)\), positive genus \(g \ge 0\) via precomputed Hodge integral tables, and twists by both convex (`virtual_zero_section`) and concave (`derivated_functor`) equivariant vector bundles.
- **Quantum multiplication and Conjecture \(\mathcal{O}\).** The package computes equivariant and non-equivariant small quantum products, multiplication matrices (`matrix_small_quantum_product`, `twisted_matrix_small_quantum_product`), graded OSCAR quotient models (`small_quantum_cohomology_ring`), and exact algebraic eigenvalues of \(c_1(TX)\star\) at \(q=1, t=0\) (`conjecture_O_eigenvalues`).

### 3. Algorithmic advances in `v1.0.0` and exceptional Grassmannians

Release `v1.0.0` accompanies [Holmes–Muratore (2026)](https://arxiv.org/abs/2610.37273) and introduces four substantial computational improvements:

1. **Refined divisor equation.** Complexity in the number of marked points is reduced from exponential to linear.
2. **Accelerated \(H_2\) curve-class relations.** Complete sets of linear relations among invariant curve classes \([C_e] \in H_2(X;\mathbb{Z})\) are computed via a deterministic generic rank-two subtorus restriction, fundamental cycles of a spanning forest, and a Chern-number \(\gcd\) shortcut whenever \(b_2(X) = 1\).
3. **Mihalcea's equivariant quantum Chevalley algorithm.** For homogeneous spaces \(G/P\) in any simple root system—including the exceptional types \(F_4, E_6, E_7, E_8\)—`quantum_schubert_context` and `quantum_schubert_product` reconstruct ordinary small quantum Schubert structure constants directly from root data without decorated-tree localization.
4. **Fast quantum multiplication and semisimplicity at scale.** Combining Mihalcea's algorithm with Wiedemann's method to certify nonvanishing characteristic-polynomial discriminants without explicitly forming the characteristic polynomial—including a \(60{,}480 \times 60{,}480\) quantum multiplication matrix for \(E_8/P_6\)—Holmes and Muratore proved generic semisimplicity of small quantum cohomology for \(E_7/P_2\), \(E_7/P_4\), \(E_7/P_5\), and \(E_8/P_6\), settling the remaining open exceptional generalized Grassmannians.

## Shared ground and complementary strengths

GKMtools.jl and GEOATOMS intersect naturally on smooth projective flag varieties \(G/P\), smooth projective toric varieties, and convex complete intersections inside them. Both rely on exact torus localization over decorated trees and exact rational or algebraic arithmetic, avoiding floating-point approximations.

There is also a direct algorithmic connection inside `gwflags`: the Python module `gwflags/gkm.py` implements the genus-zero specialization of Theorem 3.4 of [Holmes–Muratore (2025)](https://arxiv.org/abs/2509.07562) on flag-variety GKM graphs (`gkm_graph_of_flag`, `GKMEngine`). Its purpose inside GEOATOMS is deliberately focused—serving as a formula-independent internal cross-check of the root-system localization engine on \(G/P\)—rather than duplicating GKMtools.jl's general smooth, non-compact, and orbifold GKM infrastructure in Julia and OSCAR.

The table below compares the two ecosystems side by side.

| Aspect | GKMtools.jl (`v1.0.0`) | GEOATOMS (`gwflags` / `gwtoric` / `gwapp` `1.1.0.dev1`) |
|---|---|---|
| **Language & algebra stack** | Julia + [OSCAR](https://www.oscar-system.org/) (plus `Graphs`, `Combinatorics`, `nauty_jll`) | Python + SymPy / mpmath (optional SageMath backend for `gwflags`) |
| **User interfaces** | Julia REPL, scripts, OSCAR notebooks; serialization (`.jls`) | Python API, CLI, and local browser GUI (`gwflags.gui`, `gwtoric.gui`, `gwapp`) |
| **Target geometries** | Arbitrary smooth, non-compact, and orbifold GKM graphs; \(G/P\) (all types including \(F_4, E_6, E_7, E_8\)), smooth Schubert, toric, weighted projective, blowups, Seidel spaces, Hamiltonian GKM manifolds | Flag varieties \(G/P\) (root systems and kept roots), smooth projective toric varieties (fans, products, split projective bundles, blowups), and their smooth complete intersections |
| **Gromov–Witten scope** | \(T\)-equivariant and non-equivariant; genus \(g \ge 0\) (Hodge integrals); primary and descendent \(\psi\)-classes; convex and concave bundle twists | Non-equivariant genus-zero primary invariants, with exact two-point rational torus evaluations (plus symbolic `gw_raw` in `gwflags`) and Euler twists for convex homogeneous or nef toric bundles |
| **Quantum cohomology & large \(G/P\)** | Equivariant and non-equivariant small quantum products, OSCAR graded quotient rings, multiplication matrices at \(q=1\) or fixed \(\beta\), Conjecture \(\mathcal{O}\) eigenvalues, and Mihalcea's quantum Chevalley algorithm for large/exceptional \(G/P\) | Symbolic multi-variable Novikov matrices \(A(\mathbf y) = [c_1(TX)\star(-)]_{\mathrm{amb}}\) and centered codimension grading \(G\) on the reduced ambient cohomology sector |
| **Connections & atomic invariants** | Exact characteristic polynomials and algebraic eigenvalues (`QQBar`); Wiedemann semisimplicity workflows for large matrices | Exact irregular quantum-connection analysis: monic spectral factors, unit cyclic determinants \(\Delta_A(\mathbf a)\), regularized-exponent multisets \(F_{\mathbf a,\lambda}\), Hodge diamonds, and atomic Hodge invariants \((\rho_\alpha, P_\alpha(t))\) |
| **Precomputed data** | Reproducible article notebooks and examples in the documentation | [Universal catalogue](../catalog/index.md) of 302 precomputed geometric presentations (surfaces through eightfolds) with downloadable exact JSON datasets |
| **Long-run execution** | Compiled Julia performance, `fast_mode`, serialization of graphs and Schubert products | Parallel per-\(\beta\) workers, staged exact large-fraction checkpoints, and resumable workspaces in `1.1.0.dev1` |

## When to use GKMtools.jl, GEOATOMS, or both

### Choose GKMtools.jl when your problem involves

- **General or non-projective GKM spaces:** abstract GKM graphs, non-algebraic Hamiltonian GKM manifolds, realizability tests, smooth Schubert varieties, non-compact bundle total spaces, Seidel spaces, or orbifold GKM graphs such as weighted projective spaces and weighted blowups.
- **Equivariant, higher-genus, or descendent invariants:** symbolic \(T\)-equivariant Gromov–Witten invariants keeping \(t_1,\ldots,t_r\), \(\psi\)-class integrals, positive-genus invariants, or concave bundle twists.
- **Large homogeneous spaces and exceptional Grassmannians:** ordinary small quantum Schubert products for \(G/P\) (including types \(F_4, E_6, E_7, E_8\)) via Mihalcea's equivariant quantum Chevalley algorithm, or semisimplicity studies at scale inside Julia and OSCAR.

### Choose GEOATOMS when your problem involves

- **Complete intersections and symbolic Novikov operators:** Euler-twisted genus-zero localization for smooth complete intersections \(X = Z(F, E)\) in flag or toric ambient varieties, outputting symbolic multi-variable matrices \(A(\mathbf y) = [c_1(TX)\star(-)]_{\mathrm{amb}}\) and their grading \(G\).
- **Irregular connections and Hodge-atom invariants:** exact factorization of \(\chi_{A(\mathbf a)}(z)\), unit cyclic determinants \(\Delta_A(\mathbf a)\), regularized-exponent multisets \(F_{\mathbf a,\lambda}\), Hodge-diamond calculations, and the cyclicity criteria documented in [Atomic invariants](../catalog/atomic-invariants.md).
- **Immediate reference data or a browser workflow:** browsing or downloading exact matrices and invariants from the [catalogue of 302 varieties](../catalog/index.md), or running flag and toric calculations from a plain Python environment and local web interface ([Installation](../installation.md), [Combined software](combined.md)) with resumable flag checkpoints.

### Use both together for independent cross-verification

On the substantial overlap of flag varieties, smooth projective toric varieties, and convex complete intersections, running the same computation in both **GKMtools.jl** and **GEOATOMS** provides an unusually strong independent check:

- The two packages share no code and run on entirely separate stacks (Julia/OSCAR versus Python/SymPy or SageMath).
- GKMtools.jl builds the combinatorial GKM graph and performs symbolic equivariant localization (or Mihalcea's quantum Chevalley reconstruction for \(G/P\)), whereas GEOATOMS encodes root systems or fans directly and evaluates exact localization sums at independent rational torus points.
- Matching Gromov–Witten numbers, Euler-twisted matrices, or spectra across both systems simultaneously certifies coordinate conventions, bundle restrictions, curve-class maps, and exact arithmetic.

!!! note "Parabolic-root convention between GKMtools.jl and `gwflags`"
    For a generalized flag variety \(G/P\) with simple roots \(\Pi\), **GKMtools.jl** specifies \(P\) by the subset \(S = \Pi_P \subset \Pi\) of simple roots generating the **Levi factor** of \(P\) (for example, \(C_3/P_2\) uses `S = [1, 3]`, and \(\mathbb{P}^6 = A_6/P_1\) uses `S = [2, 3, 4, 5, 6]`). **GEOATOMS (`gwflags`)** specifies the complementary subset of **kept roots** \(\Pi_F = \Pi \setminus \Pi_P\) (crossed-out nodes: `[2]` for \(C_3/P_2\), and `[1]` for \(\mathbb{P}^6\)).

## Quick start with GKMtools.jl

First install **OSCAR** following the [OSCAR installation instructions](https://www.oscar-system.org/install/). Inside the same Julia environment, install GKMtools.jl `v1.0.0` from GitHub:

```julia
using Pkg
Pkg.add(url="https://github.com/mgemath/GKMtools.jl", rev="v1.0.0")
```

Load both packages in a Julia session with `using Oscar, GKMtools`.

### Example 1: Quantum Schubert matrix of \(C_3/P_2\) via Mihalcea's algorithm

The following snippet (from the [GKMtools.jl documentation](https://mgemath.github.io/GKMtools.jl/stable/Article/Quantum_Products/)) computes the \(12 \times 12\) small quantum multiplication matrix of the divisor class on the symplectic partial flag variety \(C_3/P_2\) directly from root data, without decorated-tree localization:

```julia
using Oscar, GKMtools

R = root_system(:C, 3)
I = [1, 3]  # Levi simple roots; corresponds to kept root [2] in gwflags
X = generalized_gkm_flag(R, I)
Q = quantum_schubert_context(X)

products = all_quantum_schubert_products(Q, 2; show_bar = false)
M = quantum_schubert_matrix(products; at_q1 = false)
```

### Example 2: Cross-verifying the cubic fourfold \(Z(\mathbb{P}^5, \mathcal{O}(3))\)

Both tools compute the ambient small quantum multiplication operator \(c_1(TX)\star\) on a smooth cubic fourfold \(X \subset \mathbb{P}^5\) in the basis \((1, H, H^2, H^3, H^4)\).

=== "GKMtools.jl (Julia + OSCAR)"

    ```julia
    using Oscar, GKMtools

    V = vector_bundle_O(5, [3])
    P5 = baseof(V)
    H = first_chern_class(V) / 3
    basis = [H^i for i in 0:(num_vertices(P5) - 2)]

    M = twisted_matrix_small_quantum_product_tangent_class(
        V; basis = basis, show_bar = false
    )
    ```

=== "GEOATOMS (`gwflags`, Python + SymPy)"

    ```python
    import sympy as sp
    from gwflags import FlagVariety

    F = FlagVariety("A5", [1])
    M_sym, grading, basis = F.small_quantum_multiplication(K=[[3]])
    M = sp.Matrix(M_sym).subs(sp.Symbol("y1"), 1)
    ```

Both calculations agree identically at \(q = y_1 = 1\), yielding the matrix recorded in the GEOATOMS entry [`P5 / O(3)`](../catalog/projective.md#p5o3):

$$
M =
\begin{bmatrix}
0 & 0 & 18 & 0 & 0 \\
3 & 0 & 0 & 45 & 0 \\
0 & 3 & 0 & 0 & 18 \\
0 & 0 & 3 & 0 & 0 \\
0 & 0 & 0 & 3 & 0
\end{bmatrix}.
$$

From this same operator, GEOATOMS additionally records the symbolic Novikov dependence, the grading \(G = \operatorname{diag}(-2,-1,0,1,2)\), the unit cyclic determinant \(\Delta_A(1) = 59049\), and the regularized-exponent multisets attached to each spectral factor, while GKMtools.jl extends seamlessly to equivariant parameters, descendent insertions, blowups, and general GKM targets.

## Links and references

- **Software repository:** [github.com/mgemath/GKMtools.jl](https://github.com/mgemath/GKMtools.jl) (MIT License; release [`v1.0.0`](https://github.com/mgemath/GKMtools.jl/releases/tag/v1.0.0))
- **Official documentation:** [mgemath.github.io/GKMtools.jl/stable/](https://mgemath.github.io/GKMtools.jl/stable/) — including [Equivariant Gromov–Witten invariants](https://mgemath.github.io/GKMtools.jl/stable/GW/GW/), [Quantum Schubert calculus](https://mgemath.github.io/GKMtools.jl/stable/GW/QuantumSchubert/), and [reproducible article examples](https://mgemath.github.io/GKMtools.jl/stable/Article/Quantum_Products/)
- **Underlying computer algebra system:** [OSCAR](https://www.oscar-system.org/) ([installation guide](https://www.oscar-system.org/install/))
- **Foundational paper:** Daniel Holmes and Giosuè Muratore, *Computations in equivariant Gromov–Witten theory of GKM spaces*, [arXiv:2509.07562](https://arxiv.org/abs/2509.07562) [math.AG, math.SG], September 2025 (v3, November 2025)
- **Version 1.0.0 algorithms and semisimplicity paper:** Daniel Holmes and Giosuè Muratore, *Effective Gromov–Witten computations for GKM spaces and a semisimple application*, [arXiv:2610.37273](https://arxiv.org/abs/2610.37273) [math.AG, math.SG], October 2026 (v2, November 2026)

Related GEOATOMS pages: [Choose software](index.md) · [Localization on flag varieties](../methodology.md) · [Localization on toric varieties](../toric/mathematics.md) · [Catalogue of varieties](../catalog/index.md) · [Atomic invariants](../catalog/atomic-invariants.md)
