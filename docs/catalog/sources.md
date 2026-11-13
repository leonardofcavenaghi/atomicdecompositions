---
description: Geometric constructions, identification from toric fans and the meaning of CKP and HLM references.
---

# Geometric constructions and references

Examples are named by their geometric construction: projective spaces, complete intersections in products, or projectivizations of explicit split bundles. CKP and HLM provide references to published classifications.

**CKP** means Coates–Kasprzyk–Prince, [*Four-dimensional Fano toric complete intersections*](https://arxiv.org/abs/1409.5030). The CKP numbers denote period buckets in their dataset of presentations. Equality of periods alone does not identify varieties up to isomorphism.

**HLM** means Hausen–Laface–Mauz, [*On smooth Fano fourfolds of Picard number two*](https://arxiv.org/abs/1907.08000). HLM numbers denote cases in their classification. For example, HLM-29 is the Verra fourfold.

## Geometric identification

A **fan** is a collection of strongly convex rational polyhedral cones in a lattice, closed under taking faces, whose cones meet along common faces. It determines a toric variety by gluing affine toric charts. The catalogue specifies its primitive ray generators and maximal cones; completeness means that the cones cover the real vector space of the lattice.

A **primitive collection** is a minimal set of rays not contained together in a cone: every proper subset is contained in a cone. These sets and the integral relations among their generators suggest projective-space, product and split-projective-bundle presentations. To identify the ambient toric variety, one also needs an invertible integral change of lattice coordinates carrying all rays and all maximal cones to the proposed fan. Matching only the rays, primitive relations or dimensions is insufficient.

For a full-dimensional smooth cone, its ray generators form a lattice basis: the determinant is plus or minus one. Expressing every ray in this basis makes the coordinate change integral and excludes an unnoticed finite lattice quotient. For a product of projective spaces, the standard ray blocks each sum to zero, and its maximal cones omit one ray from each block. For a split projective bundle, the twisting data enter the corresponding ray relations. In either case, matching the entire collection of maximal cones gives an isomorphism of the ambient toric varieties.

The defining divisor classes must be identified as well. If a ray has primitive generator \(v_i\) and invariant divisor \(D_i\), the principal divisor of a torus character satisfies

$$
\operatorname{div}(\chi^m)=\sum_i\langle m,v_i\rangle D_i.
$$

These relations convert each full ray-coefficient row of `K` into a divisor class in the geometric basis. In a product of projective spaces, the resulting coefficients are the defining multidegrees.

For a split bundle \(E=\bigoplus_j L_j\) on a base \(B\), the catalogue uses the **quotient convention** for \(\mathbb P_B(E)\). Write \(\pi\) for the projection and \(\xi=c_1(\mathcal O_{\mathbb P_B(E)}(1))\). The fibre-coordinate divisors have classes \(\xi-\pi^*c_1(L_j)\). Thus the converted rows are expressed in \(\xi\) and the pullbacks of the base hyperplane classes. Tensoring every summand by the same line bundle preserves the projective bundle; its tautological class changes accordingly, so the defining divisor classes must be transformed at the same time.

The [exact fan and divisor data](../data/geometric-presentations.json) give the lattice blocks, twisting data and converted degrees for the displayed constructions. This identification concerns the ambient variety and the defining divisor classes. Gromov–Witten computations require their own localization and curve-completeness arguments; primitive cohomology and full atomic decompositions require the separate Hodge-theoretic hypotheses stated with the results.
