---
description: Exact unit-cyclicity and Hodge-invariant audit of every published computation record, with full atomic invariants where the criterion applies.
---

# Cyclicity and atomic Hodge invariants

The audit covers **301 computation records**. It tests the unit cyclic determinant at the saved Novikov point and, when needed, additional exact rational points. It combines the result with a full Hodge-space identification and a justified primitive-cohomology assignment. A cyclic ambient matrix alone does not identify the full atoms.

| Outcome | Records |
|---|---:|
| Full coarse factors and Hodge invariants identified under the stated geometric hypotheses | 147 |
| Cyclic ambient operator, with additional Hodge-invariant classes outside that matrix | 46 |
| Unit cyclicity not found at the tested points | 108 |

[Download exact points, determinants, Hodge data and factors](../data/atomic-invariants.json). These are exact post-calculations on existing matrices; selected fresh localization checks and Hodge calculations are identified by their provenance.

## What the invariants mean

For a coarse atom \(\alpha\), \(\rho_\alpha=\dim_{\mathbb C}\bigl((E^\alpha_{\mathbb C})^{\mathrm{Hod}_{\mathbb C}}\bigr)\) counts rational Hodge-invariant directions. The Hodge-character polynomial is

$$
P_\alpha(t)=\sum_{p,q}h^{p,q}(E^\alpha)t^{p-q}.
$$

It records the Hodge cocharacter with positive multiplicities. Its constant coefficient can exceed \(\rho_\alpha\); it does not count only rational Hodge classes. For the added LG(3,6) example, \(\rho=3\), while \(P(t)=14t^2+102+14t^{-2}\).

A characteristic factor of degree d describes d conjugate eigenvalues. A listed atomic polynomial applies separately at each root; the consistency checks sum over all these roots. The audit polynomials refer to A=c1 multiplication. The saved connection pages also use K=-A; their factor numbering and sign convention are kept separate.

## When a full certificate is given

The matrix must span the full Hodge-invariant sector, have a nonzero unit determinant, and represent a complete curve calculation. For an ample complete intersection, weak Lefschetz identifies the fixed ambient part. Irreducible non-Tate vanishing cohomology has no rational Hodge classes for a very general member. The primitive assignment uses monodromy, the first-Chern degree, the rational characteristic relation, or the stated projective-bundle argument. Very-general qualifications remain explicit.

The finite numerical point is a display normalization. The corresponding admissible small-locus point is obtained by homogeneous Novikov rescaling along the ample anticanonical class. The non-further-splitting criterion then identifies the local coarse factors. The [mathematical conventions](../toric/mathematics.md) state the criterion and the distinction between ambient computations and full Hodge data.

For projective complete intersections of index one, the primitive eigenvalue uses the factorial correction described in [Hu, Proposition 5.9 and the index-one shift](https://arxiv.org/html/1501.03683v6). The two exceptional Hodge reconstructions use the projective incidence/blow-up model and [Mukai’s genus-twelve model](https://www.kurims.kyoto-u.ac.jp/~mukai/paper/Trieste.pdf); the ordinary Gushel–Mukai Hodge data appear in [Debarre, §5.1](https://arxiv.org/html/2001.03485). For those two Hodge reconstructions, characteristic numbers were checked independently at two exact torus points.

Two useful scope checks are GM-20 and CKP-551: their very-general Hodge-invariant ranks are both 14, while the stored matrices have ranks 9 and 8. Their nonzero ambient determinants therefore do not certify a full atomic decomposition.

## Primitive assignment rules

**Full Tate cohomology.** When the full cohomology is Tate and equals the recorded space, each eigenvalue factor of multiplicity m has rho=m and Hodge polynomial m.

**Chern index at least two.** For an ample intersection, monodromy acts irreducibly on the vanishing middle cohomology and quantum multiplication acts there by a scalar. Returning to the same degree requires a curve of Chern degree one. An index of at least two excludes it, so the scalar is zero.

**Unique rational eigenvalue.** The scalar action is rational. The ambient characteristic relation annihilates the full ring: it annihilates the unit, and multiplication is associative. If it has a single rational root, that root therefore carries all vanishing cohomology.

**Projective complete intersection of index one.** For a projective complete intersection of degrees d_i and index one, the primitive eigenvalue is minus the product of d_i factorials times q; the source and shift are cited above.

**Odd middle cohomology.** When all even cohomology is ambient and odd cohomology is middle-dimensional, its products lie in the ambient algebra. Choose paired odd classes u,v. The nonzero product Theta=u star v is a common eigenvector; associativity and v star v=0 imply Theta squared=0. Its supporting rational spectral factor must therefore be repeated. A unique repeated rational factor fixes the assignment.

**Projective bundle over a cubic threefold.** In CKP-169 and CKP-567, the projective-bundle theorem gives two Tate-shifted copies of the cubic threefold middle Hodge structure. A simple one-dimensional even spectral factor cannot carry odd cohomology: nondegeneracy and associativity would contradict the square-zero relation of an odd class. Hence all odd classes lie on the unique repeated quadratic factor. Irreducible cubic-threefold monodromy reduces the action to a rational two-by-two multiplicity operator; each of its two roots carries one copy, with polynomial 5t+5/t.

These rules give the full polynomial by adding the assigned vanishing-cohomology polynomial to the ambient contribution. Every certified decomposition is checked against the full Hodge polynomial and the total Hodge-invariant rank.

## Browse by dimension

- [Points and curves](invariants-points-curves.md)
- [Surfaces](invariants-surfaces.md)
- [Threefolds](invariants-threefolds.md)
- [Fourfolds](invariants-fourfolds.md)
- [Fivefolds](invariants-fivefolds.md)
- [Higher dimensions](invariants-higher-dimensional.md)

## All records

<div class="atomic-index" markdown>

| Geometric record | Dimension | Ambient rank | Full Hodge-invariant rank | Result |
|---|---:|---:|---:|---|
| [Gr(2,6)](grassmannians.md#gr26) | 8 | 15 | 15 | [No cyclic point found](invariants-higher-dimensional.md#1251e5bfa1a6) |
| [P8  Fano index 9](projective.md#p8fanoindex9) | 8 | 9 | 9 | [Full atomic invariants](invariants-higher-dimensional.md#38cfb4dd44e9) |
| [Fl(1,4,5)](additional.md#fl145) | 7 | 20 | 20 | [Full atomic invariants](invariants-higher-dimensional.md#6d625eb08919) |
| [Gr(2,6) / O(1)](grassmannians.md#gr26o1) | 7 | 12 | 12 | [No cyclic point found](invariants-higher-dimensional.md#a1cae496a552) |
| [P7  Fano index 8](projective.md#p7fanoindex8) | 7 | 8 | 8 | [Full atomic invariants](invariants-higher-dimensional.md#2b39fd310de2) |
| [P8 / O(2)](projective.md#p8o2) | 7 | 8 | 8 | [Full atomic invariants](invariants-higher-dimensional.md#4ffe1ade62f4) |
| [P8 / O(3)](projective.md#p8o3) | 7 | 8 | 8 | [Full atomic invariants](invariants-higher-dimensional.md#765c6cbd0f13) |
| [P8 / O(4)](projective.md#p8o4) | 7 | 8 | 8 | [Full atomic invariants](invariants-higher-dimensional.md#6604d561e8a4) |
| [P8 / O(5)](projective.md#p8o5) | 7 | 8 | 8 | [Full atomic invariants](invariants-higher-dimensional.md#15b578599b32) |
| [P8 / O(6)](projective.md#p8o6) | 7 | 8 | 8 | [Full atomic invariants](invariants-higher-dimensional.md#b7e34220e954) |
| [P8 / O(7)](projective.md#p8o7) | 7 | 8 | 8 | [Full atomic invariants](invariants-higher-dimensional.md#bcd0369eeffc) |
| [Gr(2,5)](grassmannians.md#gr25) | 6 | 10 | 10 | [Full atomic invariants](invariants-higher-dimensional.md#add4e2cdc0c7) |
| [Gr(2,6) / O(1)+O(1)](grassmannians.md#gr26o1o1) | 6 | 10 | 12 | [No cyclic point found](invariants-higher-dimensional.md#92c91f67a0db) |
| [Gr(2,6) / O(1)+O(2)](grassmannians.md#gr26o1o2) | 6 | 10 | 10 | [No cyclic point found](invariants-higher-dimensional.md#58854a726a80) |
| [Gr(3,5)](grassmannians.md#gr35) | 6 | 10 | 10 | [Full atomic invariants](invariants-higher-dimensional.md#9d177386f50d) |
| [P6  Fano index 7](projective.md#p6fanoindex7) | 6 | 7 | 7 | [Full atomic invariants](invariants-higher-dimensional.md#7dbd349ec9ab) |
| [P7 / O(2)](projective.md#p7o2) | 6 | 7 | 8 | [Ambient matrix incomplete](invariants-higher-dimensional.md#12203c19a2ac) |
| [P7 / O(3)](projective.md#p7o3) | 6 | 7 | 7 | [Full atomic invariants](invariants-higher-dimensional.md#c48a08dcc0ef) |
| [P7 / O(4)](projective.md#p7o4) | 6 | 7 | 7 | [Full atomic invariants](invariants-higher-dimensional.md#4d98dba9cf55) |
| [P7 / O(5)](projective.md#p7o5) | 6 | 7 | 7 | [Full atomic invariants](invariants-higher-dimensional.md#8547b3f70ef7) |
| [P7 / O(6)](projective.md#p7o6) | 6 | 7 | 7 | [Full atomic invariants](invariants-higher-dimensional.md#8c15f95b6325) |
| [P8 / O(2)+O(2)](projective.md#p8o2o2) | 6 | 7 | 16 | [Ambient matrix incomplete](invariants-higher-dimensional.md#e0a0b3d40922) |
| [P8 / O(2)+O(3)](projective.md#p8o2o3) | 6 | 7 | 7 | [Full atomic invariants](invariants-higher-dimensional.md#99ac9ea3af4c) |
| [P8 / O(2)+O(4)](projective.md#p8o2o4) | 6 | 7 | 7 | [Full atomic invariants](invariants-higher-dimensional.md#d5cc160f2e6a) |
| [P8 / O(2)+O(5)](projective.md#p8o2o5) | 6 | 7 | 7 | [Full atomic invariants](invariants-higher-dimensional.md#11d7c5142e09) |
| [P8 / O(3)+O(3)](projective.md#p8o3o3) | 6 | 7 | 7 | [Full atomic invariants](invariants-higher-dimensional.md#53a423286d87) |
| [P8 / O(3)+O(4)](projective.md#p8o3o4) | 6 | 7 | 7 | [Full atomic invariants](invariants-higher-dimensional.md#d8d261b9c52c) |
| [Complete intersection (2,2,2,2) in P⁹ (PCI5-2-2-2-2)](records/pci5-2-2-2-2.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#pci5-2-2-2-2) |
| [Complete intersection (2,2,2,2,2) in P¹⁰ (PCI5-2-2-2-2-2)](records/pci5-2-2-2-2-2.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#pci5-2-2-2-2-2) |
| [Complete intersection (2,2,2,3) in P⁹ (PCI5-2-2-2-3)](records/pci5-2-2-2-3.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#pci5-2-2-2-3) |
| [Complete intersection (2,2,3) in P⁸ (PCI5-2-2-3)](records/pci5-2-2-3.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#pci5-2-2-3) |
| [Complete intersection (2,2,4) in P⁸ (PCI5-2-2-4)](records/pci5-2-2-4.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#pci5-2-2-4) |
| [Complete intersection (2,3) in P⁷ (QC5-001)](records/qc5-001.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#qc5-001) |
| [Complete intersection (2,3,3) in P⁸ (PCI5-2-3-3)](records/pci5-2-3-3.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#pci5-2-3-3) |
| [Complete intersection (2,4) in P⁷ (PCI5-2-4)](records/pci5-2-4.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#pci5-2-4) |
| [Complete intersection (2,5) in P⁷ (PCI5-2-5)](records/pci5-2-5.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#pci5-2-5) |
| [Complete intersection (3,3) in P⁷ (PCI5-3-3)](records/pci5-3-3.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#pci5-3-3) |
| [Complete intersection (3,4) in P⁷ (PCI5-3-4)](records/pci5-3-4.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#pci5-3-4) |
| [Complete intersection of multidegrees (1,1), (1,1), (1,2) in P³ × P⁵ (PB5-060)](records/pb5-060.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-060) |
| [Complete intersection of multidegrees (1,3) in P¹ × P⁵ (PB5-003)](records/pb5-003.md) | 5 | 10 | 10 | [No cyclic point found](invariants-fivefolds.md#pb5-003) |
| [Complete intersection of multidegrees (2,1), (1,2) in P³ × P⁴ (PB5-051)](records/pb5-051.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-051) |
| [Complete intersection of multidegrees (2,1), (1,2) in P³ × P⁴ (PROD5-D02)](records/prod5-d02.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#prod5-d02) |
| [Complete intersection of multidegrees (2,1), (1,2), (1,1) in P⁴ × P⁴ (PROD5-E02)](records/prod5-e02.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#prod5-e02) |
| [Complete intersection of multidegrees (2,1), (1,3) in P³ × P⁴ (PROD5-D04)](records/prod5-d04.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#prod5-d04) |
| [Complete intersection of multidegrees (2,2) in P² × P⁴ (PROD5-A01)](records/prod5-a01.md) | 5 | 12 | 12 | [Full atomic invariants](invariants-fivefolds.md#prod5-a01) |
| [Complete intersection of multidegrees (2,2) in P³ × P³ (PB5-028)](records/pb5-028.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-028) |
| [Complete intersection of multidegrees (2,2) in P³ × P³ (PROD5-B01)](records/prod5-b01.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#prod5-b01) |
| [Complete intersection of multidegrees (2,2), (1,1) in P³ × P⁴ (PROD5-D01)](records/prod5-d01.md) | 5 | 12 | 12 | [Full atomic invariants](invariants-fivefolds.md#prod5-d01) |
| [Complete intersection of multidegrees (2,2), (1,1), (1,1) in P⁴ × P⁴ (PROD5-E01)](records/prod5-e01.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#prod5-e01) |
| [Complete intersection of multidegrees (2,2), (1,2) in P³ × P⁴ (PROD5-D05)](records/prod5-d05.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#prod5-d05) |
| [Complete intersection of multidegrees (2,2,2) in P² × P² × P² (PROD5-C01)](records/prod5-c01.md) | 5 | 20 | 20 | [No cyclic point found](invariants-fivefolds.md#prod5-c01) |
| [Complete intersection of multidegrees (2,3) in P² × P⁴ (PROD5-A02)](records/prod5-a02.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#prod5-a02) |
| [Complete intersection of multidegrees (2,3) in P³ × P³ (PROD5-B02)](records/prod5-b02.md) | 5 | 12 | 12 | [Full atomic invariants](invariants-fivefolds.md#prod5-b02) |
| [Complete intersection of multidegrees (2,3), (1,1) in P³ × P⁴ (PROD5-D03)](records/prod5-d03.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#prod5-d03) |
| [Complete intersection of multidegrees (2,4) in P² × P⁴ (PROD5-A03)](records/prod5-a03.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#prod5-a03) |
| [Complete intersection of multidegrees (3,3) in P³ × P³ (PROD5-B03)](records/prod5-b03.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#prod5-b03) |
| [Degree-6 fivefold in P⁶ (PCI5-6)](records/pci5-6.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#pci5-6) |
| [Fl(1,4,5) / O(1,1)+O(1,1)](additional.md#fl145o11o11) | 5 | 12 | 12 | [Full atomic invariants](invariants-fivefolds.md#9cb29c69a3f5) |
| [G2/P1](additional.md#g2p1) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#fd2bd6eae26b) |
| [G2/P2](additional.md#g2p2) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#834882311808) |
| [Gr(2,5) / O(1)](grassmannians.md#gr25o1) | 5 | 8 | 8 | [Full atomic invariants](invariants-fivefolds.md#1584955327b7) |
| [Gr(2,5) / O(2)](grassmannians.md#gr25o2) | 5 | 8 | 8 | [No cyclic point found](invariants-fivefolds.md#1cd0a9ffb74e) |
| [Gr(2,5) / O(3)](grassmannians.md#gr25o3) | 5 | 8 | 8 | [No cyclic point found](invariants-fivefolds.md#dd16e36a8997) |
| [Gr(2,6) / O(1)+O(1)+O(1)](grassmannians.md#gr26o1o1o1) | 5 | 8 | 8 | [No cyclic point found](invariants-fivefolds.md#51706ac77ff7) |
| [Gr(2,6) / O(1)+O(1)+O(2)](grassmannians.md#gr26o1o1o2) | 5 | 8 | 8 | [No cyclic point found](invariants-fivefolds.md#c7da579d09a1) |
| [Gr(3,5) / O(1)](grassmannians.md#gr35o1) | 5 | 8 | 8 | [Full atomic invariants](invariants-fivefolds.md#1e7394ef8632) |
| [Gr(3,5) / O(2)](grassmannians.md#gr35o2) | 5 | 8 | 8 | [No cyclic point found](invariants-fivefolds.md#d7857b18eb8e) |
| [Gr(3,5) / O(3)](grassmannians.md#gr35o3) | 5 | 8 | 8 | [No cyclic point found](invariants-fivefolds.md#ffb644472d2c) |
| [LG(3,6) / O(1)](additional.md#lg36o1) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#141c91366f21) |
| [OG(3,7) / O(2)](additional.md#og37o2) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#76928fabba80) |
| [OG(3,7) / O(3)](additional.md#og37o3) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#29e94da02c49) |
| [OG(3,7) / O(4)](additional.md#og37o4) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#10e047830d24) |
| [P5  Fano index 6](projective.md#p5fanoindex6) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#75f4cdb8997b) |
| [P6 / O(2)](projective.md#p6o2) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#7ccb7c3e0b6b) |
| [P6 / O(3)](projective.md#p6o3) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#c44e0fd4a5b0) |
| [P6 / O(4)](projective.md#p6o4) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#b740ed7ac87d) |
| [P6 / O(5)](projective.md#p6o5) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#ee9c4f882e7c) |
| [P7 / O(2)+O(2)](projective.md#p7o2o2) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#75efe609f198) |
| [P7 / O(2)+O(3)](projective.md#p7o2o3) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#86a2cd927e5d) |
| [P7 / O(2)+O(4)](projective.md#p7o2o4) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#bbd63cac242a) |
| [P7 / O(3)+O(3)](projective.md#p7o3o3) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#0dfe4b49547a) |
| [P8 / O(2)+O(2)+O(2)](projective.md#p8o2o2o2) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#649a71c1db0a) |
| [P8 / O(2)+O(2)+O(3)](projective.md#p8o2o2o3) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#819481252d0a) |
| [Quartic double cover of P⁵ (QD5-001)](records/qd5-001.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#qd5-001) |
| [Quartic fivefold in P⁶ (PCI5-4)](records/pci5-4.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#pci5-4) |
| [Quintic fivefold in P⁶ (PCI5-5)](records/pci5-5.md) | 5 | 6 | 6 | [Full atomic invariants](invariants-fivefolds.md#pci5-5) |
| [Section of P_{P²}(O^4 ⊕ O(1)) by 3ξ+H (PB5-016)](records/pb5-016.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-016) |
| [Section of P_{P²}(O^4 ⊕ O(1)) by 4ξ+H (PB5-017)](records/pb5-017.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-017) |
| [Section of P_{P³}(O^2 ⊕ O(1)^2) by 2ξ+H (PB5-043)](records/pb5-043.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-043) |
| [Section of P_{P³}(O^2 ⊕ O(1)^2) by 3ξ+H (PB5-044)](records/pb5-044.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-044) |
| [Section of P_{P³}(O^3 ⊕ O(1)) by 2ξ+2H (PB5-036)](records/pb5-036.md) | 5 | 12 | 12 | [Full atomic invariants](invariants-fivefolds.md#pb5-036) |
| [Section of P_{P³}(O^3 ⊕ O(1)) by 3ξ+2H (PB5-038)](records/pb5-038.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-038) |
| [Section of P_{P³}(O^3 ⊕ O(1)) by 3ξ+H (PB5-037)](records/pb5-037.md) | 5 | 12 | 12 | [Full atomic invariants](invariants-fivefolds.md#pb5-037) |
| [Section of P_{P³}(O^3 ⊕ O(2)) by 2ξ+H (PB5-040)](records/pb5-040.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-040) |
| [Section of P_{P³}(O^3 ⊕ O(2)) by 3ξ+H (PB5-041)](records/pb5-041.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-041) |
| [Section of P_{P³}(O^4 ⊕ O(1)) by 2ξ+H, 2ξ+H (PB5-058)](records/pb5-058.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-058) |
| [Section of P_{P³}(O^4 ⊕ O(1)) by ξ+H, 2ξ+H (PB5-056)](records/pb5-056.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-056) |
| [Section of P_{P³}(O^4 ⊕ O(1)) by ξ+H, 3ξ+H (PB5-057)](records/pb5-057.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-057) |
| [Section of P_{P⁴}(O ⊕ O(1) ⊕ O(2)) by 2ξ+H (PB5-088)](records/pb5-088.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-088) |
| [Section of P_{P⁴}(O ⊕ O(1)^2) by 2ξ+2H (PB5-086)](records/pb5-086.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-086) |
| [Section of P_{P⁴}(O ⊕ O(1)^2) by 2ξ+H (PB5-085)](records/pb5-085.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-085) |
| [Section of P_{P⁴}(O^2 ⊕ O(1)) by 2ξ+2H (PB5-075)](records/pb5-075.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-075) |
| [Section of P_{P⁴}(O^2 ⊕ O(1)) by 2ξ+3H (PB5-076)](records/pb5-076.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-076) |
| [Section of P_{P⁴}(O^2 ⊕ O(1)^2) by ξ+H, 2ξ+H (PB5-107)](records/pb5-107.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-107) |
| [Section of P_{P⁴}(O^2 ⊕ O(2)) by 2ξ+2H (PB5-080)](records/pb5-080.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-080) |
| [Section of P_{P⁴}(O^2 ⊕ O(2)) by 2ξ+H (PB5-079)](records/pb5-079.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-079) |
| [Section of P_{P⁴}(O^2 ⊕ O(3)) by 2ξ+H (PB5-082)](records/pb5-082.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-082) |
| [Section of P_{P⁴}(O^3 ⊕ O(1)) by ξ+2H, 2ξ+H (PB5-103)](records/pb5-103.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-103) |
| [Section of P_{P⁴}(O^3 ⊕ O(1)) by ξ+H, 2ξ+2H (PB5-102)](records/pb5-102.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-102) |
| [Section of P_{P⁴}(O^3 ⊕ O(1)) by ξ+H, 2ξ+H (PB5-101)](records/pb5-101.md) | 5 | 12 | 12 | [Full atomic invariants](invariants-fivefolds.md#pb5-101) |
| [Section of P_{P⁴}(O^3 ⊕ O(2)) by ξ+H, 2ξ+H (PB5-105)](records/pb5-105.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-105) |
| [Section of P_{P⁴}(O^4 ⊕ O(1)) by ξ+H, ξ+H, 2ξ+H (PB5-114)](records/pb5-114.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-114) |
| [Section of P_{P⁵}(O ⊕ O(1) ⊕ O(2)) by ξ+H, ξ+H (PB5-147)](records/pb5-147.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-147) |
| [Section of P_{P⁵}(O ⊕ O(1)) by ξ+3H (PB5-124)](records/pb5-124.md) | 5 | 10 | 10 | [Full atomic invariants](invariants-fivefolds.md#pb5-124) |
| [Section of P_{P⁵}(O ⊕ O(2)) by ξ+2H (PB5-127)](records/pb5-127.md) | 5 | 10 | 10 | [No cyclic point found](invariants-fivefolds.md#pb5-127) |
| [Section of P_{P⁵}(O ⊕ O(2)) by ξ+3H (PB5-128)](records/pb5-128.md) | 5 | 10 | 10 | [Full atomic invariants](invariants-fivefolds.md#pb5-128) |
| [Section of P_{P⁵}(O ⊕ O(3)) by ξ+2H (PB5-130)](records/pb5-130.md) | 5 | 10 | 10 | [Full atomic invariants](invariants-fivefolds.md#pb5-130) |
| [Section of P_{P⁵}(O ⊕ O(4)) by ξ+H (PB5-131)](records/pb5-131.md) | 5 | 10 | 10 | [No cyclic point found](invariants-fivefolds.md#pb5-131) |
| [Section of P_{P⁵}(O^2 ⊕ O(1)) by ξ+H, ξ+2H (PB5-139)](records/pb5-139.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-139) |
| [Section of P_{P⁵}(O^2 ⊕ O(1)^2) by ξ+H, ξ+H, ξ+H (PB5-155)](records/pb5-155.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-155) |
| [Section of P_{P⁵}(O^2 ⊕ O(2)) by ξ+H, ξ+2H (PB5-143)](records/pb5-143.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-143) |
| [Section of P_{P⁵}(O^2 ⊕ O(3)) by ξ+H, ξ+H (PB5-144)](records/pb5-144.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-144) |
| [Section of P_{P⁵}(O^3 ⊕ O(1)) by ξ+H, ξ+H, ξ+2H (PB5-153)](records/pb5-153.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-153) |
| [Section of P_{P⁵}(O^3 ⊕ O(2)) by ξ+H, ξ+H, ξ+H (PB5-154)](records/pb5-154.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-154) |
| [Section of P_{P⁵}(O^4 ⊕ O(1)) by ξ+H, ξ+H, ξ+H, ξ+H (PB5-158)](records/pb5-158.md) | 5 | 12 | 12 | [No cyclic point found](invariants-fivefolds.md#pb5-158) |
| [CKP-172 — Complete intersection of codimension 1](records/ckp-172.md) | 4 | 12 | 12 | [No cyclic point found](invariants-fourfolds.md#ckp-172) |
| [CKP-320 — Complete intersection of codimension 1](records/ckp-320.md) | 4 | 13 | 13 | [No cyclic point found](invariants-fourfolds.md#ckp-320) |
| [Complete intersection (2,2) in P⁶ (CKP-033)](records/ckp-033.md) | 4 | 5 | 12 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-033) |
| [Complete intersection (2,2,2) in P⁷ (CKP-596)](records/ckp-596.md) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#ckp-596) |
| [Complete intersection (2,2,2,2) in P⁸ (CKP-731)](records/ckp-731.md) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#ckp-731) |
| [Complete intersection (2,2,3) in P⁷ (CKP-735)](records/ckp-735.md) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#ckp-735) |
| [Complete intersection (2,3) in P⁶ (CKP-640)](records/ckp-640.md) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#ckp-640) |
| [Complete intersection (2,4) in P⁶ (CKP-737)](records/ckp-737.md) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#ckp-737) |
| [Complete intersection (3,3) in P⁶ (CKP-736)](records/ckp-736.md) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#ckp-736) |
| [Complete intersection of multidegrees (0,2) in P¹ × P⁴ (CKP-111)](records/ckp-111.md) | 4 | 8 | 8 | [Full atomic invariants](invariants-fourfolds.md#ckp-111) |
| [Complete intersection of multidegrees (0,3) in P¹ × P⁴ (CKP-567)](records/ckp-567.md) | 4 | 8 | 8 | [Full atomic invariants](invariants-fourfolds.md#ckp-567) |
| [Complete intersection of multidegrees (1,1) in P² × P³ (CKP-078)](records/ckp-078.md) | 4 | 9 | 9 | [Full atomic invariants](invariants-fourfolds.md#ckp-078) |
| [Complete intersection of multidegrees (1,1) in P¹ × P⁴ (CKP-002)](records/ckp-002.md) | 4 | 8 | 8 | [Full atomic invariants](invariants-fourfolds.md#ckp-002) |
| [Complete intersection of multidegrees (1,1), (1,1) in P² × P⁴ (CKP-018)](records/ckp-018.md) | 4 | 9 | 9 | [Full atomic invariants](invariants-fourfolds.md#ckp-018) |
| [Complete intersection of multidegrees (1,1), (1,1) in P³ × P³ (CKP-189)](records/ckp-189.md) | 4 | 9 | 12 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-189) |
| [Complete intersection of multidegrees (1,1), (1,1), (1,1) in P³ × P⁴ (CKP-175)](records/ckp-175.md) | 4 | 9 | 18 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-175) |
| [Complete intersection of multidegrees (1,1), (1,1), (1,1), (1,1) in P⁴ × P⁴ (CKP-665)](records/ckp-665.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-665) |
| [Complete intersection of multidegrees (1,1), (1,1), (1,2) in P³ × P⁴ (CKP-681)](records/ckp-681.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-681) |
| [Complete intersection of multidegrees (1,1), (1,2) in P² × P⁴ (CKP-322)](records/ckp-322.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-322) |
| [Complete intersection of multidegrees (1,1), (1,3) in P² × P⁴ (CKP-722)](records/ckp-722.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-722) |
| [Complete intersection of multidegrees (1,1), (2,1) in P³ × P³ (CKP-323)](records/ckp-323.md) | 4 | 9 | 23 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-323) |
| [Complete intersection of multidegrees (1,1), (2,2) in P³ × P³ (CKP-715)](records/ckp-715.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-715) |
| [Complete intersection of multidegrees (1,1,1) in P¹ × P² × P² (CKP-247)](records/ckp-247.md) | 4 | 13 | 15 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-247) |
| [Complete intersection of multidegrees (1,1,1) in P¹ × P¹ × P³ (CKP-102)](records/ckp-102.md) | 4 | 12 | 12 | [Full atomic invariants](invariants-fourfolds.md#ckp-102) |
| [Complete intersection of multidegrees (1,1,1), (1,1,1) in P² × P² × P² (CKP-623)](records/ckp-623.md) | 4 | 14 | 14 | [No cyclic point found](invariants-fourfolds.md#ckp-623) |
| [Complete intersection of multidegrees (1,1,1,1) in P¹ × P¹ × P¹ × P² (CKP-475)](records/ckp-475.md) | 4 | 17 | 22 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-475) |
| [Complete intersection of multidegrees (1,1,1,1,1) in P¹ × P¹ × P¹ × P¹ × P¹ (CKP-628)](records/ckp-628.md) | 4 | 22 | 22 | [No cyclic point found](invariants-fourfolds.md#ckp-628) |
| [Complete intersection of multidegrees (1,1,1,2) in P¹ × P¹ × P¹ × P² (CKP-667)](records/ckp-667.md) | 4 | 17 | 17 | [No cyclic point found](invariants-fourfolds.md#ckp-667) |
| [Complete intersection of multidegrees (1,1,2) in P¹ × P¹ × P³ (CKP-432)](records/ckp-432.md) | 4 | 12 | 12 | [No cyclic point found](invariants-fourfolds.md#ckp-432) |
| [Complete intersection of multidegrees (1,1,3) in P¹ × P¹ × P³ (CKP-721)](records/ckp-721.md) | 4 | 12 | 12 | [No cyclic point found](invariants-fourfolds.md#ckp-721) |
| [Complete intersection of multidegrees (1,2) in P² × P³ (CKP-327)](records/ckp-327.md) | 4 | 9 | 16 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-327) |
| [Complete intersection of multidegrees (1,2) in P¹ × P⁴ (CKP-030)](records/ckp-030.md) | 4 | 8 | 13 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-030) |
| [Complete intersection of multidegrees (1,2), (1,2) in P² × P⁴ (CKP-711)](records/ckp-711.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-711) |
| [Complete intersection of multidegrees (1,2,1) in P¹ × P² × P² (CKP-560)](records/ckp-560.md) | 4 | 13 | 24 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-560) |
| [Complete intersection of multidegrees (1,2,2) in P¹ × P² × P² (CKP-698)](records/ckp-698.md) | 4 | 13 | 13 | [No cyclic point found](invariants-fourfolds.md#ckp-698) |
| [Complete intersection of multidegrees (1,3) in P² × P³ (CKP-694)](records/ckp-694.md) | 4 | 9 | 35 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-694) |
| [Complete intersection of multidegrees (1,3) in P¹ × P⁴ (CKP-566)](records/ckp-566.md) | 4 | 8 | 8 | [Full atomic invariants](invariants-fourfolds.md#ckp-566) |
| [Complete intersection of multidegrees (1,4) in P¹ × P⁴ (CKP-734)](records/ckp-734.md) | 4 | 8 | 8 | [Full atomic invariants](invariants-fourfolds.md#ckp-734) |
| [Complete intersection of multidegrees (2,1) in P² × P³ (CKP-107)](records/ckp-107.md) | 4 | 9 | 9 | [Full atomic invariants](invariants-fourfolds.md#ckp-107) |
| [Complete intersection of multidegrees (2,1), (1,2) in P³ × P³ (CKP-705)](records/ckp-705.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-705) |
| [Complete intersection of multidegrees (2,2) in P² × P³ (CKP-439)](records/ckp-439.md) | 4 | 9 | 9 | [Full atomic invariants](invariants-fourfolds.md#ckp-439) |
| [Complete intersection of multidegrees (2,3) in P² × P³ (CKP-726)](records/ckp-726.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-726) |
| [Cubic fourfold in P⁵ (CKP-037)](records/ckp-037.md) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#ckp-037) |
| [Fl(1,2,5) / O(0,1)+O(0,2)+O(1,0) (GM-20)](additional.md#fl125o01o02o10gm20) | 4 | 9 | 14 | [Ambient matrix incomplete](invariants-fourfolds.md#e1322438fd01) |
| [Fl(1,3,4) / O(1,1)](additional.md#fl134o11) | 4 | 9 | 12 | [Ambient matrix incomplete](invariants-fourfolds.md#3ed191207b19) |
| [G2/P2 / O(1)](additional.md#g2p2o1) | 4 | 5 | 6 | [Ambient matrix incomplete](invariants-fourfolds.md#b9a91f8b2a8f) |
| [Gr(2,4)](grassmannians.md#gr24) | 4 | 6 | 6 | [No cyclic point found](invariants-fourfolds.md#51615a7643a1) |
| [Gr(2,5) / O(1)+O(1)](grassmannians.md#gr25o1o1) | 4 | 6 | 6 | [Full atomic invariants](invariants-fourfolds.md#3c0ee725b9d8) |
| [Gr(2,5) / O(1)+O(2)](grassmannians.md#gr25o1o2) | 4 | 6 | 6 | [No cyclic point found](invariants-fourfolds.md#5a3a05721152) |
| [Gr(2,5) / O(1)+O(3)](grassmannians.md#gr25o1o3) | 4 | 6 | 6 | [No cyclic point found](invariants-fourfolds.md#d2a92bddd407) |
| [Gr(2,5) / O(2)+O(2)](grassmannians.md#gr25o2o2) | 4 | 6 | 6 | [No cyclic point found](invariants-fourfolds.md#71c4061dbdf2) |
| [Gr(3,5) / O(1)+O(1)](grassmannians.md#gr35o1o1) | 4 | 6 | 6 | [Full atomic invariants](invariants-fourfolds.md#fbeb5f79765b) |
| [Gr(3,5) / O(1)+O(2)](grassmannians.md#gr35o1o2) | 4 | 6 | 6 | [No cyclic point found](invariants-fourfolds.md#0c8674c9ad6f) |
| [Gr(3,5) / O(1)+O(3)](grassmannians.md#gr35o1o3) | 4 | 6 | 6 | [No cyclic point found](invariants-fourfolds.md#f418dda622c4) |
| [Gr(3,5) / O(2)+O(2)](grassmannians.md#gr35o2o2) | 4 | 6 | 6 | [No cyclic point found](invariants-fourfolds.md#a6bf73eeb7fb) |
| [Gr(4,5)](grassmannians.md#gr45) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#139781d9fb14) |
| [Hyperplane and quadric section of LG(3,6)](records/lg3-1-2.md) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#lg3-1-2) |
| [LG(3,6) / O(1)+O(1)](additional.md#lg36o1o1) | 4 | 5 | 8 | [Ambient matrix incomplete](invariants-fourfolds.md#5a3d521e7212) |
| [OG(3,7) / O(2)+O(2)](additional.md#og37o2o2) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#176397975a00) |
| [P4  Fano index 5](projective.md#p4fanoindex5) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#53078b491137) |
| [P5 / O(2)](projective.md#p5o2) | 4 | 5 | 6 | [Ambient matrix incomplete](invariants-fourfolds.md#8884770b89b8) |
| [P5 / O(3)](projective.md#p5o3) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#31aadf32267f) |
| [P5 / O(4)](projective.md#p5o4) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#8bd58b781863) |
| [P5 / O(5)](projective.md#p5o5) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#61e63b38f5a8) |
| [P6 / O(2)+O(2)](projective.md#p6o2o2) | 4 | 5 | 12 | [Ambient matrix incomplete](invariants-fourfolds.md#e4065b55a49a) |
| [P6 / O(2)+O(3)](projective.md#p6o2o3) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#6324179fa1e1) |
| [P6 / O(2)+O(4)](projective.md#p6o2o4) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#3150500f5723) |
| [P6 / O(3)+O(3)](projective.md#p6o3o3) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#de2575bbb840) |
| [P7 / O(2)+O(2)+O(2)](projective.md#p7o2o2o2) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#d68ecb775686) |
| [P7 / O(2)+O(2)+O(3)](projective.md#p7o2o2o3) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#5ae4d92d2f20) |
| [P⁴ (CKP-001)](records/ckp-001.md) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#ckp-001) |
| [Quadric fourfold in P⁵ (CKP-003)](records/ckp-003.md) | 4 | 5 | 6 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-003) |
| [Quadric section of the adjoint G₂ variety](records/g2-quadric.md) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#g2-quadric) |
| [Quartic fourfold in P⁵ (CKP-682)](records/ckp-682.md) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#ckp-682) |
| [Quintic fourfold in P⁵ (CKP-738)](records/ckp-738.md) | 4 | 5 | 5 | [Full atomic invariants](invariants-fourfolds.md#ckp-738) |
| [Section of P_{P² × P²}(O ⊕ O(1,0)) by ξ+H1+2H2 (CKP-594)](records/ckp-594.md) | 4 | 13 | 13 | [No cyclic point found](invariants-fourfolds.md#ckp-594) |
| [Section of P_{P² × P²}(O ⊕ O(1,0)) by ξ+H1+H2 (CKP-363)](records/ckp-363.md) | 4 | 13 | 19 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-363) |
| [Section of P_{P² × P²}(O ⊕ O(1,1)) by ξ+H1+H2 (CKP-450)](records/ckp-450.md) | 4 | 13 | 13 | [No cyclic point found](invariants-fourfolds.md#ckp-450) |
| [Section of P_{P² × P²}(O(0,1) ⊕ O(1,0)) by ξ+H1+H2 (CKP-492)](records/ckp-492.md) | 4 | 13 | 13 | [No cyclic point found](invariants-fourfolds.md#ckp-492) |
| [Section of P_{P²}(O^2 ⊕ O(1)^2) by 2ξ (CKP-233)](records/ckp-233.md) | 4 | 9 | 16 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-233) |
| [Section of P_{P²}(O^2 ⊕ O(1)^2) by 3ξ (CKP-702)](records/ckp-702.md) | 4 | 9 | not identified | [No cyclic point found](invariants-fourfolds.md#ckp-702) |
| [Section of P_{P²}(O^3 ⊕ O(1)) by 2ξ (CKP-186)](records/ckp-186.md) | 4 | 9 | 10 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-186) |
| [Section of P_{P²}(O^3 ⊕ O(1)) by 2ξ+H (CKP-314)](records/ckp-314.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-314) |
| [Section of P_{P²}(O^3 ⊕ O(1)) by 3ξ (CKP-688)](records/ckp-688.md) | 4 | 9 | not identified | [No cyclic point found](invariants-fourfolds.md#ckp-688) |
| [Section of P_{P²}(O^3 ⊕ O(1)) by 3ξ+H (CKP-718)](records/ckp-718.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-718) |
| [Section of P_{P²}(O^3 ⊕ O(1)) by ξ+H (CKP-014)](records/ckp-014.md) | 4 | 9 | 9 | [Full atomic invariants](invariants-fourfolds.md#ckp-014) |
| [Section of P_{P²}(O^3 ⊕ O(2)) by 2ξ (CKP-182)](records/ckp-182.md) | 4 | 9 | 16 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-182) |
| [Section of P_{P²}(O^3 ⊕ O(2)) by 3ξ (CKP-691)](records/ckp-691.md) | 4 | 9 | not identified | [No cyclic point found](invariants-fourfolds.md#ckp-691) |
| [Section of P_{P³}(O ⊕ O(1)^2) by 2ξ (CKP-145)](records/ckp-145.md) | 4 | 8 | 16 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-145) |
| [Section of P_{P³}(O ⊕ O(1)^2) by 2ξ+H (CKP-595)](records/ckp-595.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-595) |
| [Section of P_{P³}(O ⊕ O(1)^2) by ξ+H (CKP-114)](records/ckp-114.md) | 4 | 9 | 12 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-114) |
| [Section of P_{P³}(O ⊕ O(2)^2) by 2ξ (HLM-27)](records/hlm-27.md) | 4 | 8 | not identified | [No cyclic point found](invariants-fourfolds.md#hlm-27) |
| [Section of P_{P³}(O^2 ⊕ O(1)) by 2ξ+2H (CKP-685)](records/ckp-685.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-685) |
| [Section of P_{P³}(O^2 ⊕ O(1)) by 2ξ+H (CKP-174)](records/ckp-174.md) | 4 | 9 | 9 | [Full atomic invariants](invariants-fourfolds.md#ckp-174) |
| [Section of P_{P³}(O^2 ⊕ O(1)) by ξ+2H (CKP-170)](records/ckp-170.md) | 4 | 9 | 20 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-170) |
| [Section of P_{P³}(O^2 ⊕ O(1)) by ξ+H (CKP-061)](records/ckp-061.md) | 4 | 9 | 10 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-061) |
| [Section of P_{P³}(O^2 ⊕ O(2)) by 2ξ+H (CKP-179)](records/ckp-179.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-179) |
| [Section of P_{P³}(O^2 ⊕ O(2)) by ξ+H (CKP-049)](records/ckp-049.md) | 4 | 9 | 11 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-049) |
| [Section of P_{P³}(O^3 ⊕ O(1)) by ξ+H, 2ξ+H (CKP-656)](records/ckp-656.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-656) |
| [Section of P_{P³}(O^3 ⊕ O(1)) by ξ+H, ξ+H (CKP-160)](records/ckp-160.md) | 4 | 9 | 15 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-160) |
| [Section of P_{P¹ × P²}(O^2 ⊕ O(0,1)) by 2ξ+H1+H2 (CKP-639)](records/ckp-639.md) | 4 | 13 | 13 | [No cyclic point found](invariants-fourfolds.md#ckp-639) |
| [Section of P_{P¹ × P²}(O^2 ⊕ O(0,1)) by ξ+H1+H2 (CKP-155)](records/ckp-155.md) | 4 | 13 | 17 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-155) |
| [Section of P_{P¹ × P³}(O ⊕ O(0,1)) by ξ+H1+2H2 (CKP-593)](records/ckp-593.md) | 4 | 12 | 12 | [No cyclic point found](invariants-fourfolds.md#ckp-593) |
| [Section of P_{P¹ × P³}(O ⊕ O(0,1)) by ξ+H1+H2 (CKP-144)](records/ckp-144.md) | 4 | 12 | 17 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-144) |
| [Section of P_{P¹ × P³}(O ⊕ O(0,2)) by ξ+H1+H2 (CKP-157)](records/ckp-157.md) | 4 | 12 | 12 | [No cyclic point found](invariants-fourfolds.md#ckp-157) |
| [Section of P_{P¹ × P¹ × P²}(O ⊕ O(0,0,1)) by ξ+H1+H2+H3 (CKP-535)](records/ckp-535.md) | 4 | 17 | 17 | [No cyclic point found](invariants-fourfolds.md#ckp-535) |
| [Section of P_{P¹}(O^4 ⊕ O(1)) by 2ξ (CKP-026)](records/ckp-026.md) | 4 | 8 | 10 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-026) |
| [Section of P_{P¹}(O^4 ⊕ O(1)) by 3ξ (CKP-551)](records/ckp-551.md) | 4 | 8 | 14 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-551) |
| [Section of P_{P¹}(O^4 ⊕ O(1)) by 4ξ (CKP-733)](records/ckp-733.md) | 4 | 8 | not identified | [No cyclic point found](invariants-fourfolds.md#ckp-733) |
| [Section of P_{P⁴}(O ⊕ O(1)) by 2H (CKP-060)](records/ckp-060.md) | 4 | 8 | 8 | [Full atomic invariants](invariants-fourfolds.md#ckp-060) |
| [Section of P_{P⁴}(O ⊕ O(1)) by 3H (CKP-169)](records/ckp-169.md) | 4 | 8 | 8 | [Full atomic invariants](invariants-fourfolds.md#ckp-169) |
| [Section of P_{P⁴}(O ⊕ O(1)) by ξ+2H (CKP-039)](records/ckp-039.md) | 4 | 8 | 8 | [No cyclic point found](invariants-fourfolds.md#ckp-039) |
| [Section of P_{P⁴}(O ⊕ O(1)) by ξ+3H (CKP-683)](records/ckp-683.md) | 4 | 8 | 8 | [Full atomic invariants](invariants-fourfolds.md#ckp-683) |
| [Section of P_{P⁴}(O ⊕ O(1)) by ξ+H (CKP-004)](records/ckp-004.md) | 4 | 8 | 9 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-004) |
| [Section of P_{P⁴}(O ⊕ O(1)^2) by ξ+H, ξ+H (CKP-498)](records/ckp-498.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-498) |
| [Section of P_{P⁴}(O ⊕ O(2)) by 2H (CKP-046)](records/ckp-046.md) | 4 | 8 | 8 | [Full atomic invariants](invariants-fourfolds.md#ckp-046) |
| [Section of P_{P⁴}(O ⊕ O(2)) by ξ+2H (CKP-041)](records/ckp-041.md) | 4 | 8 | 8 | [Full atomic invariants](invariants-fourfolds.md#ckp-041) |
| [Section of P_{P⁴}(O ⊕ O(2)) by ξ+H (CKP-005)](records/ckp-005.md) | 4 | 8 | 14 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-005) |
| [Section of P_{P⁴}(O ⊕ O(3)) by ξ+H (CKP-006)](records/ckp-006.md) | 4 | 8 | 8 | [No cyclic point found](invariants-fourfolds.md#ckp-006) |
| [Section of P_{P⁴}(O^2 ⊕ O(1)) by ξ+H, ξ+2H (CKP-645)](records/ckp-645.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-645) |
| [Section of P_{P⁴}(O^2 ⊕ O(1)) by ξ+H, ξ+H (CKP-036)](records/ckp-036.md) | 4 | 9 | 16 | [Ambient matrix incomplete](invariants-fourfolds.md#ckp-036) |
| [Section of P_{P⁴}(O^2 ⊕ O(2)) by ξ+H, ξ+H (CKP-040)](records/ckp-040.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-040) |
| [Section of P_{P⁴}(O^3 ⊕ O(1)) by ξ+H, ξ+H, ξ+H (CKP-611)](records/ckp-611.md) | 4 | 9 | 9 | [No cyclic point found](invariants-fourfolds.md#ckp-611) |
| [Verra fourfold (HLM-29)](records/hlm-29.md) | 4 | 9 | not identified | [No cyclic point found](invariants-fourfolds.md#hlm-29) |
| [B2/B / O(1,1)](additional.md#b2bo11) | 3 | 6 | 6 | [No cyclic point found](invariants-threefolds.md#34fec398819e) |
| [Fanography 1-10](fanography.md#fano-variety-1-10) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#7d708946a6fa) |
| [Fanography 1-6](fanography.md#fano-variety-1-6) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#e3f3a551d928) |
| [Fanography 1-7](fanography.md#fano-variety-1-7) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#541768cd0738) |
| [Fanography 1-8](fanography.md#fano-variety-1-8) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#8f9e7a526fba) |
| [Fanography 1-9](fanography.md#fano-variety-1-9) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#6f17aaf4290d) |
| [Fanography 2-24](fanography.md#fano-variety-2-24) | 3 | 6 | 6 | [Full atomic invariants](invariants-threefolds.md#3538d68c1866) |
| [Fanography 2-32](fanography.md#fano-variety-2-32) | 3 | 6 | 6 | [Full atomic invariants](invariants-threefolds.md#a6cb2e5a95bb) |
| [Fanography 2-34](fanography.md#fano-variety-2-34) | 3 | 6 | 6 | [Full atomic invariants](invariants-threefolds.md#ea3e323d9fcb) |
| [Fanography 3-11](fanography.md#fano-variety-3-11) | 3 | 8 | 8 | [Full atomic invariants](invariants-threefolds.md#a8e28f47c77f) |
| [Fanography 3-27](fanography.md#fano-variety-3-27) | 3 | 8 | 8 | [Full atomic invariants](invariants-threefolds.md#292efbd7ade0) |
| [Fanography 4-1](fanography.md#fano-variety-4-1) | 3 | 10 | 10 | [No cyclic point found](invariants-threefolds.md#96d957608200) |
| [Fl(1,3,4) / O(1,1)+O(1,1)](additional.md#fl134o11o11) | 3 | 6 | 6 | [Full atomic invariants](invariants-threefolds.md#d3154e614ad6) |
| [Gr(2,4) / O(1)](grassmannians.md#gr24o1) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#1841f3a70f74) |
| [Gr(2,4) / O(2)](grassmannians.md#gr24o2) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#0156965bbcb0) |
| [Gr(2,4) / O(3)](grassmannians.md#gr24o3) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#83c013d9bdf4) |
| [Gr(2,5) / O(1)+O(1)+O(1)](grassmannians.md#gr25o1o1o1) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#f443674348ad) |
| [Gr(2,5) / O(1)+O(1)+O(2)](grassmannians.md#gr25o1o1o2) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#4a1a8491be38) |
| [Gr(3,4)](grassmannians.md#gr34) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#92f8f69bd1f8) |
| [Gr(3,5) / O(1)+O(1)+O(1)](grassmannians.md#gr35o1o1o1) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#70aac1aaa08e) |
| [Gr(3,5) / O(1)+O(1)+O(2)](grassmannians.md#gr35o1o1o2) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#d1339713ede4) |
| [Gr(4,5) / O(1)](grassmannians.md#gr45o1) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#005416420233) |
| [Gr(4,5) / O(2)](grassmannians.md#gr45o2) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#6ce465296672) |
| [Gr(4,5) / O(3)](grassmannians.md#gr45o3) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#a408b7769859) |
| [Gr(4,5) / O(4)](grassmannians.md#gr45o4) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#490a4dc43960) |
| [P3  Fano index 4](projective.md#p3fanoindex4) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#ebd198ca1849) |
| [P4 / O(2)](projective.md#p4o2) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#6ceccace2e40) |
| [P4 / O(3)](projective.md#p4o3) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#0743d9764a4a) |
| [P4 / O(4)](projective.md#p4o4) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#1c4486700490) |
| [P5 / O(2)+O(2)](projective.md#p5o2o2) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#420c622c9cb3) |
| [P5 / O(2)+O(3)](projective.md#p5o2o3) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#3834707b4d89) |
| [P6 / O(2)+O(2)+O(2)](projective.md#p6o2o2o2) | 3 | 4 | 4 | [Full atomic invariants](invariants-threefolds.md#352c4508e307) |
| [Gr(2,4) / O(1)+O(1)](grassmannians.md#gr24o1o1) | 2 | 3 | 4 | [Ambient matrix incomplete](invariants-surfaces.md#1d67c54eac18) |
| [Gr(2,4) / O(1)+O(2)](grassmannians.md#gr24o1o2) | 2 | 3 | 8 | [Ambient matrix incomplete](invariants-surfaces.md#c5377008d724) |
| [Gr(3,4) / O(1)](grassmannians.md#gr34o1) | 2 | 3 | 3 | [Full atomic invariants](invariants-surfaces.md#892655959f06) |
| [Gr(3,4) / O(2)](grassmannians.md#gr34o2) | 2 | 3 | 4 | [Ambient matrix incomplete](invariants-surfaces.md#53ee7c8af21e) |
| [Gr(3,4) / O(3)](grassmannians.md#gr34o3) | 2 | 3 | 9 | [Ambient matrix incomplete](invariants-surfaces.md#1fe2cc704593) |
| [Gr(4,5) / O(1)+O(1)](grassmannians.md#gr45o1o1) | 2 | 3 | 3 | [Full atomic invariants](invariants-surfaces.md#5bdf83aa585a) |
| [Gr(4,5) / O(1)+O(2)](grassmannians.md#gr45o1o2) | 2 | 3 | 4 | [Ambient matrix incomplete](invariants-surfaces.md#04f8ea67b0d4) |
| [Gr(4,5) / O(1)+O(3)](grassmannians.md#gr45o1o3) | 2 | 3 | 9 | [Ambient matrix incomplete](invariants-surfaces.md#b1aa6f89ec3e) |
| [Gr(4,5) / O(2)+O(2)](grassmannians.md#gr45o2o2) | 2 | 3 | 8 | [Ambient matrix incomplete](invariants-surfaces.md#2dd604001dc5) |
| [P2 Fano index 3](projective.md#p2fanoindex3) | 2 | 3 | 3 | [Full atomic invariants](invariants-surfaces.md#7bea0424f8dd) |
| [P3 / O(2)](projective.md#p3o2) | 2 | 3 | 4 | [Ambient matrix incomplete](invariants-surfaces.md#c26b71c1c385) |
| [P3 / O(3)](projective.md#p3o3) | 2 | 3 | 9 | [Ambient matrix incomplete](invariants-surfaces.md#785f6e8bcd76) |
| [P4 / O(2)+O(2)](projective.md#p4o2o2) | 2 | 3 | 8 | [Ambient matrix incomplete](invariants-surfaces.md#904c41fdd438) |
| [Gr(2,4) / O(1)+O(1)+O(1)](grassmannians.md#gr24o1o1o1) | 1 | 2 | 2 | [Full atomic invariants](invariants-points-curves.md#8b39618f3aed) |
| [Gr(3,4) / O(1)+O(1)](grassmannians.md#gr34o1o1) | 1 | 2 | 2 | [Full atomic invariants](invariants-points-curves.md#375785af1f22) |
| [Gr(3,4) / O(1)+O(2)](grassmannians.md#gr34o1o2) | 1 | 2 | 2 | [Full atomic invariants](invariants-points-curves.md#79dd3601d09b) |
| [Gr(4,5) / O(1)+O(1)+O(1)](grassmannians.md#gr45o1o1o1) | 1 | 2 | 2 | [Full atomic invariants](invariants-points-curves.md#8156468b738f) |
| [Gr(4,5) / O(1)+O(1)+O(2)](grassmannians.md#gr45o1o1o2) | 1 | 2 | 2 | [Full atomic invariants](invariants-points-curves.md#af3a5033ba7a) |
| [P2 / O(2)](projective.md#p2o2) | 1 | 2 | 2 | [Full atomic invariants](invariants-points-curves.md#81b66f277517) |
| [Gr(3,4) / O(1)+O(1)+O(1)](grassmannians.md#gr34o1o1o1) | 0 | 1 | 1 | [Full atomic invariants](invariants-points-curves.md#c427c3fda1be) |

</div>
