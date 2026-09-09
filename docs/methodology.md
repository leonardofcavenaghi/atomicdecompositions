# Methodology of the Software

The `gwflags` package algorithmically implements the **root-theoretic localization formalism** detailed in the accompanying paper for genus-zero Gromov-Witten invariants of flag varieties.

## Mathematical Translation

Computing Gromov-Witten invariants of a complex projective variety is classically difficult. However, by leveraging **Kontsevich's localization method** on varieties carrying torus actions (like flag varieties \(G/P\)), the integrations can be reduced to a purely combinatorial problem over decorated trees. 

### Bott Localization & Decorated Trees

The software reduces the computations to sums over fixed loci of stable maps—represented as decorated trees.

1. **Roots and Weights**: The geometry of flag varieties is entirely controlled by root systems and Weyl groups. Tangent weights at every fixed point satisfy the GKM independence condition. The software holds all Weyl and root data as integer-normalized exact tuples.
2. **Billey's Formula**: Evaluates equivariant Schubert classes restricted to fixed points.
3. **Graph Enumeration**: The software Canonicalizes trees by AHU hashing from the center, bypassing the need for computationally heavy permutation sweeps. The generation of edge decorations operates via a pruned per-edge Depth-First Search (DFS).

## Fast Numerical Evaluations

One of the significant methodological contributions of this software compared to earlier computational iterations (like the original Mathematica `V3.nb` implementation) is its transition from heavy symbolic manipulation to swift numerical evaluation.

- **Dimension Axiom Gating**: Every invariant is gated by the dimension axiom. If the dimensions do not match the expected degrees, the software returns `0` instantly.
- **Exact Rational Evaluations**: Instead of carrying symbolic rational functions through all steps and taking limits at the end, the software evaluates the gated localization sum **exactly at two independent random rational points** of the equivariant torus. 
- Because the gated sum must evaluate to a constant (the invariant), this numeric substitution *is* the invariant itself. Checking against two points securely guards against accidental poles.
- **Caching**: Class-independent data (decorations, edge factors, Billey restrictions) are aggressively cached to ensure that loops over the quantum matrix pairs are optimized.

## Quantum Cohomology & Functoriality

The software extends the computations from the ambient flag variety to smooth zero loci of globally generated homogeneous vector bundles (complete intersections).

Using the **Kim-Kresch-Pantev** functoriality theorem, the Gromov-Witten invariants of a complete intersection \( X \subset F \) are pulled back to integrals over the moduli stack of the ambient flag variety \( F \). 

Ultimately, the software extracts the **flag-ambient matrix of small quantum multiplication by the first Chern class**, \( c_1(TX)\star \), and computes its characteristic polynomial and eigenvalues. These outputs are precisely the ingredients required by the theoretical non-rationality criteria described in the paper.
