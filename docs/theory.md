# Mathematical Background

This document provides a theoretical overview of the geometry and quantum cohomology of complete intersections in flag varieties.

## 1. The Projected Flag-Ambient Small Quantum Multiplication

For a complete intersection $X = \mathcal{Z}(F, \mathcal{E})$ defined by a homogeneous vector bundle $\mathcal{E}$ on an ambient flag variety $F = G/P$, computing the full quantum cohomology is generally extremely difficult. However, equivariant localization naturally yields the quantum invariants for classes inherited from the ambient space.

Let $\iota: X \hookrightarrow F$ be the inclusion. The *flag-ambient cohomology* of $X$ is defined as the image of the restriction map:
$$H^*_{\text{amb}}(X) := \text{im}\left( \iota^* : H^*(F, \mathbb{Q}) \to H^*(X, \mathbb{Q}) \right)$$

Because the restriction of the Poincaré pairing to $H^*_{\text{amb}}(X)$ is typically nondegenerate, there exists a well-defined orthogonal projection $\text{pr}_F : H^*(X, \mathbb{Q}) \to H^*_{\text{amb}}(X)$. The *projected flag-ambient small quantum product* of two ambient classes $\alpha, \eta \in H^*_{\text{amb}}(X)$ is given by:
$$\alpha \star_F \eta := \text{pr}_F(\alpha \star \eta)$$

The `gwflags` software explicitly computes the matrix representation of the operator $c_1(TX) \star_F (-)$. When the flag-ambient cohomology coincides entirely with the monodromy-fixed part of the cohomology of $X$, this projected matrix captures the necessary data to study the spectral properties of the quantum connection.

## 2. Fano Index for Complete Intersections in Flag Varieties

The Fano index of a variety is the largest integer $q$ such that the anticanonical bundle $K^{-1}$ is the $q$-th tensor power of some ample line bundle $L$. 

For a flag variety $F = G/P$, the tangent bundle $TF$ is globally generated and its first Chern class is completely determined by the sum of the positive roots indexing the tangent directions. When taking a smooth complete intersection $X = \mathcal{Z}(F, \mathcal{E})$, the adjunction formula relates the canonical bundles:
$$K_X = (K_F \otimes \det \mathcal{E})|_X$$

Correspondingly, the anticanonical class used for small quantum multiplication is given by restricting the difference of the Chern classes:
$$c_1(TX) = \iota^*(c_1(TF) - c_1(\mathcal{E}))$$

If $X$ is a Fano variety, $c_1(TX)$ is ample. The Fano index is exactly the greatest common divisor of the coefficients when $c_1(TX)$ is expressed in the basis of fundamental weights.

## 3. Eigenvalues and Multiplicities

The spectral properties of the small quantum multiplication operator by $c_1(TX)$ yield important structural invariants. By specializing the Novikov variables algebraically (setting $y_i = 1$), we obtain a finite matrix $A^{\text{alg}}(1)$.

The decomposition of this matrix is characterized by its eigenvalues $\lambda$, their algebraic multiplicities $m_a(\lambda)$, and their geometric multiplicities $m_g(\lambda)$. 

These spectral data dictate the structure of the quantum connection:
*   **Semisimplicity:** A semisimple eigenvalue implies that the generalized eigenspace does not contain a non-trivial Jordan block, which differentiates the deformation behavior of the structure and imposes distinct cohomological constraints.

## 4. Dimension and Basis Rank

The geometric dimensions and the rank of the cohomology rings for these spaces are deeply tied to the representation theory of the underlying Lie group $G$.

*   **Dimension:** The dimension of the ambient flag variety $F$ is strictly the number of roots in $R^+_F = R^+ \setminus R^+_P$ (positive roots not in the parabolic subsystem). If $\mathcal{E}$ is a vector bundle of rank $r$, the complete intersection $X$ has dimension $\dim X = \dim F - r$.
*   **Basis Rank:** The cohomology $H^*(F, \mathbb{Q})$ has a canonical homogeneous basis given by Schubert classes $\sigma_w$, which are indexed by the minimal-length representatives $W_F$ of the Weyl group quotient $W/W_P$. The rank of the flag-ambient cohomology $H^*_{\text{amb}}(X)$ is the number of such Schubert classes that do not vanish upon restriction to $X$.
