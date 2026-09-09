# Theoretical Basis

The theoretical foundation of this software is built upon the paper **"On the Atomic Decomposition of Complete Intersection in Flag Varieties."** It merges explicit combinatorial geometry with the **Theory of Hodge Atoms** developed by Katzarkov-Kontsevich-Pantev-Yu.

## Main Results

The paper derives four primary theorems:

### Theorem A: Explicit Localization Formula
Let \(\mathcal{E}\) be a globally generated homogeneous bundle on the flag variety \(F = G/P\), and let \(Z = \mathscr{Z}(F, \mathcal{E})\) be the smooth zero locus of a regular section. The theorem provides an explicit localization formula for genus-zero primary Gromov-Witten invariants of \(Z\) with Schubert insertions restricted from the ambient flag variety. The sum is finite over decorated trees and completely determined by root-theoretic data.

*This theorem serves as the strict blueprint for the `gwflags` software logic.*

### Theorem B: Spectral Irrationality Criterion (Hodge-General)
Let \(X\) be a Fano fourfold with \(h^{3,1}(X) = 1\) arising as a hyperplane section of a suitable Fano fivefold. Suppose \(X\) is Hodge general.

If every eigenvalue of the algebraic specialization of the small quantum multiplication matrix \(B^{\text{alg}}(1)\) has **algebraic multiplicity at most two**, then \(X\) is **irrational**.

*The software provides exactly the eigenvalues of this matrix.*

### Theorem C: Spectral Constraint for Rationality
Unlike Theorem B, this theorem does not require Hodge generality. 
If every eigenvalue of \(B^{\text{alg}}(1)\) has a **Jordan defect at most one** and \(X\) is rational, then every weak factorization contains a smooth surface center whose minimal model is a projective K3 surface.

### Theorem D: Numerical Irrationality Criterion
Under the same geometric assumptions as Theorem B, the paper also recovers a numerical criterion derived from the work of Benedetti-Fay-Guéré-Manivel-Perrin.

If \(b_4(Y) \leq h^{2,2}(X) - 20\), then \(X\) is irrational.

## The Theory of Coarse Hodge Atoms

The rationality criteria are deeply rooted in the concept of **Coarse Hodge Atoms**. The Fano fourfold \(X\) possesses a cohomology that decomposes into a monodromy-fixed part and a middle vanishing cohomology.

At the "small points" (points where all non-Novikov coordinates vanish), quantum multiplication by the first Chern class preserves this decomposition and acts purely by a scalar on the vanishing summand.

The algorithm developed here targets the flag-ambient subspace of the cohomology. When the flag-ambient subspace aligns with the full monodromy-fixed part (known as "ambient-complete in the middle degree"), the criteria from Theorem B and C can be read directly from the localization matrix calculated by the `gwflags` software.

## Examples Evaluated

The paper and software cross-validate these theorems on multiple Fano fourfolds:

- **Cubic Fourfolds**: The ambient and monodromy-fixed subspaces coincide. The zero eigenvalue of the quantum matrix has algebraic multiplicity two and geometric multiplicity one. The theorems successfully recover their irrationality.
- **Ordinary Gushel-Mukai Fourfolds**: Ambient completeness holds. The multiplicity bounds are satisfied, yielding irrationality and K3-center constraints.
- **Küchle Fourfolds of type (c5)**: Ambient-completeness fails, meaning the flag-ambient matrix misses two monodromy-fixed classes. Consequently, the numerical criterion (Theorem D) is heavily utilized over the spectral ones.
