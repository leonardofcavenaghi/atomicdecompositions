# Mathematical Methodology and Replication

This document explains the mathematical foundations underpinning the `gwflags` software and how the computed invariants of complete intersections in flag varieties are calculated.

## 1. Goal of the Software

The `gwflags` library computes the **small quantum multiplication by the first Chern class**, $c_1(TX) \star (-)$, for complete intersections $X$ in flag varieties. This operator is crucial in understanding the spectral properties of the quantum connection and irrationality obstructions.

Specifically, for a complete intersection defined by a homogeneous vector bundle $\mathcal{E}$ on an ambient flag variety $F = G/P$, the software evaluates the equivariant Gromov-Witten invariants and constructs the small quantum multiplication matrix projected onto the flag-ambient cohomology $H^*_{\text{amb}}(X)$.

**Reference:** [On the Atomic Decomposition of Complete Intersection in Flag Varieties (Cavenaghi et al.)](https://arxiv.org/abs/2405.01358)

## 2. Atiyah-Bott Equivariant Localization

Directly integrating Gromov-Witten classes over the moduli space of stable maps is generally computationally infeasible. Instead, `gwflags` relies on the algebraic torus action $T \subset G$ acting on the flag variety $F = G/P$ and the corresponding induced action on the moduli space of maps.

By applying the **Atiyah-Bott Localization Theorem**, the integrals are reduced to finite sums over the $T$-fixed loci of the moduli space. The fixed loci correspond to decorated trees (or graphs) where:
- Vertices map to fixed points of $F$ (which are in bijection with the Weyl group quotient $W/W_P$).
- Edges correspond to invariant curves connecting these fixed points.

The software recursively generates these graphs for a given curve degree $\beta$, calculates the equivariant Euler classes of the normal bundles (using the roots of $G$ and weights of $\mathcal{E}$), and computes the intersection numbers programmatically. 

**Reference:** [The Moment Map and Equivariant Cohomology (Atiyah & Bott, 1984)](https://doi.org/10.1016/0040-9383(84)90021-1)

## 3. Borel-Weil-Bott and Flag Ambient Cohomology

For the ambient space $F$, the cohomology basis consists of Schubert classes $\sigma_w$. When intersecting with the zero locus of $\mathcal{E}$, not all Schubert classes survive.

The dimension and basis rank are derived using Lie theory. 
- The dimension is exactly $|R^+ \setminus R^+_P| - \text{rank}(\mathcal{E})$.
- The flag-ambient cohomology $H^*_{\text{amb}}(X)$ is exactly the image of the restriction map $i^*: H^*(F, \mathbb{Q}) \to H^*(X, \mathbb{Q})$.

**Reference:** [Homogeneous Vector Bundles (Bott, 1957)](https://doi.org/10.2307/1970105)

## 4. Replicating the Computations

Because `gwflags` explicitly computes the exact localization graphs, all geometric values (Fano index, dimension, basis rank, and the quantum multiplication matrix $A^{\text{alg}}(1)$) can be natively replicated by a researcher on their local machine.

To replicate a result found in our [Catalog](catalog.md):
1. Install `gwflags` (see [Installation](installation.md)).
2. Instantiate the flag variety using `X = FlagVariety(algebra, roots_that_stay)`.
3. Invoke `X.small_quantum_multiplication(K)` where $K$ specifies the multidegrees of the vector bundle.
4. Evaluate the resulting symbolic matrix by setting all $y_i = 1$ to find the roots of the quantum connection (eigenvalues).

All eigenvalues, dimensions, and algebraic multiplicities are exact algebraic consequences of these Lie-theoretic constraints.
