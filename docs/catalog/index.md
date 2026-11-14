---
description: A universal catalogue of varieties and complete intersections, organized by dimension and geometric construction, with exact quantum multiplication and Hodge invariants.
---

# Catalogue of varieties

Browse by dimension and geometric construction. Projective spaces, Grassmannians, homogeneous spaces, projective bundles and their complete intersections belong to the same catalogue. Distinct presentations retain their own curve coordinates and ordered cohomology bases.

<div class="catalog-collections" markdown>

- [**Points and curves**](points-curves.md)
- [**Surfaces**](surfaces.md)
- [**Threefolds**](threefolds.md)
- [**Fourfolds**](fourfolds.md)
- [**Fivefolds**](fivefolds.md)
- [**Dimension six and higher**](higher-dimensional.md)

</div>

## Reading the computations

For a variety \(X\) of dimension \(d\), let \((e_1,\ldots,e_N)\) be the returned homogeneous basis of its ambient cohomology. The matrix

$$
A(\mathbf y)=\left[c_1(TX)\star(-)\right]_{\mathrm{amb}},
\qquad
G=\operatorname{diag}\left(\operatorname{codim}(e_i)-\frac d2\right)
$$

represents the ambient projection of small quantum multiplication by the first Chern class, and \(G\) is its grading. Column \(j\) of \(A\) is the image of \(e_j\); row \(i\) gives the coefficient of \(e_i\). The parameters \(\mathbf y\) are the Novikov coordinates; exact software outputs may name them `y1`, `y2`, and so on.

At a stated coordinate assignment \(\mathbf a\), write \(A(\mathbf a)\) for the specialized matrix. Its characteristic polynomial is \(\chi_{A(\mathbf a)}(z)=\det(zI_N-A(\mathbf a))=\prod_jp_j(z)^{m_j}\), where \(I_N\) is the identity matrix and the \(p_j\) are monic, pairwise coprime, square-free factors. Each root \(\lambda\) of \(p_j\) is an eigenvalue of multiplicity \(m_j\). If \(\mathbf 1\) is the coordinate column of the unit, the **unit cyclic determinant** is

$$
\Delta_A(\mathbf a)=\det\bigl[\mathbf 1,A(\mathbf a)\mathbf 1,\ldots,A(\mathbf a)^{N-1}\mathbf 1\bigr].
$$

Its nonvanishing proves that these quantum powers span the computed space. The **regularized-exponent multiset** \(F_{\mathbf a,\lambda}\) records the classes \(-\theta+\mathbb Z\) of residue eigenvalues \(\theta\) of the regular-singular connection factor at \(\lambda\), with repetitions retained. For a coarse Hodge atom \(\alpha\), \(\rho_\alpha\) counts rational Hodge-invariant directions, and \(P_\alpha(t)=\sum_{p,q}h^{p,q}(E^\alpha)t^{p-q}\) records the Hodge-cocharacter weights with positive multiplicities.

The matrix size \(N\) is the ambient cohomology dimension, which may differ from both the full rational Hodge-invariant dimension and the total cohomology dimension. Atomic interpretations drawn from these matrices require the cohomological and genericity hypotheses stated with each result. A zero cyclic determinant at a particular point does not imply vanishing at every point.

The **Recorded Chern index** uses the presentation's convention. In the original flag collection it is an ambient Chern gcd: a conic has ambient gcd one in \(\mathbb P^2\), but intrinsic Fano index two. A point has no geometric Fano index defined by that gcd. In the table, \(h(1,1)\) means \(h^{1,1}(X)\); a dash indicates that no value is asserted in this summary.

[Complete notation key](notation.md) · [Geometric constructions and references](sources.md) · [Exact datasets](datasets.md) · [Atomic invariants](atomic-invariants.md)

## Search the catalogue

Search by geometric name, construction, dimension or numerical data. The table filters the collection; site search includes descriptions, exact inputs and scientific keywords. The [Fano threefold reference](fanography.md) also lists classification families beyond those with quantum matrices in the catalogue.

| Geometry | Ambient presentation | Dimension | Recorded Chern index | Ambient dimension | h(1,1) | Analysis |
|---|---|---:|---:|---:|---:|---|
| [P8  Fano index 9](projective.md#p8fanoindex9) | A8 | 8 | 9 | 9 | 1 | [Operator](projective.md#p8fanoindex9) · [Hodge and atomic data](invariants-higher-dimensional.md#38cfb4dd44e9) |
| [Gr(2,6)](grassmannians.md#gr26) | A5 | 8 | 6 | 15 | 1 | [Operator](grassmannians.md#gr26) · [Hodge and atomic data](invariants-higher-dimensional.md#1251e5bfa1a6) |
| [P7  Fano index 8](projective.md#p7fanoindex8) | A7 | 7 | 8 | 8 | 1 | [Operator](projective.md#p7fanoindex8) · [Hodge and atomic data](invariants-higher-dimensional.md#2b39fd310de2) |
| [P8 / O(2)](projective.md#p8o2) | A8 | 7 | 7 | 8 | 1 | [Operator](projective.md#p8o2) · [Hodge and atomic data](invariants-higher-dimensional.md#4ffe1ade62f4) |
| [P8 / O(3)](projective.md#p8o3) | A8 | 7 | 6 | 8 | 1 | [Operator](projective.md#p8o3) · [Hodge and atomic data](invariants-higher-dimensional.md#765c6cbd0f13) |
| [Gr(2,6) / O(1)](grassmannians.md#gr26o1) | A5 | 7 | 5 | 12 | 1 | [Operator](grassmannians.md#gr26o1) · [Hodge and atomic data](invariants-higher-dimensional.md#a1cae496a552) |
| [P8 / O(4)](projective.md#p8o4) | A8 | 7 | 5 | 8 | 1 | [Operator](projective.md#p8o4) · [Hodge and atomic data](invariants-higher-dimensional.md#6604d561e8a4) |
| [Fl(1,4,5)](additional.md#fl145) | A4 | 7 | 4 | 20 | 2 | [Operator](additional.md#fl145) · [Hodge and atomic data](invariants-higher-dimensional.md#6d625eb08919) |
| [P8 / O(5)](projective.md#p8o5) | A8 | 7 | 4 | 8 | 1 | [Operator](projective.md#p8o5) · [Hodge and atomic data](invariants-higher-dimensional.md#15b578599b32) |
| [P8 / O(6)](projective.md#p8o6) | A8 | 7 | 3 | 8 | 1 | [Operator](projective.md#p8o6) · [Hodge and atomic data](invariants-higher-dimensional.md#b7e34220e954) |
| [P8 / O(7)](projective.md#p8o7) | A8 | 7 | 2 | 8 | 1 | [Operator](projective.md#p8o7) · [Hodge and atomic data](invariants-higher-dimensional.md#bcd0369eeffc) |
| [P6  Fano index 7](projective.md#p6fanoindex7) | A6 | 6 | 7 | 7 | 1 | [Operator](projective.md#p6fanoindex7) · [Hodge and atomic data](invariants-higher-dimensional.md#7dbd349ec9ab) |
| [P7 / O(2)](projective.md#p7o2) | A7 | 6 | 6 | 7 | 1 | [Operator](projective.md#p7o2) · [Hodge and atomic data](invariants-higher-dimensional.md#12203c19a2ac) |
| [Gr(2,5)](grassmannians.md#gr25) | A4 | 6 | 5 | 10 | 1 | [Operator](grassmannians.md#gr25) · [Hodge and atomic data](invariants-higher-dimensional.md#add4e2cdc0c7) |
| [Gr(3,5)](grassmannians.md#gr35) | A4 | 6 | 5 | 10 | 1 | [Operator](grassmannians.md#gr35) · [Hodge and atomic data](invariants-higher-dimensional.md#9d177386f50d) |
| [P7 / O(3)](projective.md#p7o3) | A7 | 6 | 5 | 7 | 1 | [Operator](projective.md#p7o3) · [Hodge and atomic data](invariants-higher-dimensional.md#c48a08dcc0ef) |
| [P8 / O(2)+O(2)](projective.md#p8o2o2) | A8 | 6 | 5 | 7 | 1 | [Operator](projective.md#p8o2o2) · [Hodge and atomic data](invariants-higher-dimensional.md#e0a0b3d40922) |
| [Gr(2,6) / O(1)+O(1)](grassmannians.md#gr26o1o1) | A5 | 6 | 4 | 10 | 1 | [Operator](grassmannians.md#gr26o1o1) · [Hodge and atomic data](invariants-higher-dimensional.md#92c91f67a0db) |
| [P7 / O(4)](projective.md#p7o4) | A7 | 6 | 4 | 7 | 1 | [Operator](projective.md#p7o4) · [Hodge and atomic data](invariants-higher-dimensional.md#4d98dba9cf55) |
| [P8 / O(2)+O(3)](projective.md#p8o2o3) | A8 | 6 | 4 | 7 | 1 | [Operator](projective.md#p8o2o3) · [Hodge and atomic data](invariants-higher-dimensional.md#99ac9ea3af4c) |
| [Gr(2,6) / O(1)+O(2)](grassmannians.md#gr26o1o2) | A5 | 6 | 3 | 10 | 1 | [Operator](grassmannians.md#gr26o1o2) · [Hodge and atomic data](invariants-higher-dimensional.md#58854a726a80) |
| [P7 / O(5)](projective.md#p7o5) | A7 | 6 | 3 | 7 | 1 | [Operator](projective.md#p7o5) · [Hodge and atomic data](invariants-higher-dimensional.md#8547b3f70ef7) |
| [P8 / O(2)+O(4)](projective.md#p8o2o4) | A8 | 6 | 3 | 7 | 1 | [Operator](projective.md#p8o2o4) · [Hodge and atomic data](invariants-higher-dimensional.md#d5cc160f2e6a) |
| [P8 / O(3)+O(3)](projective.md#p8o3o3) | A8 | 6 | 3 | 7 | 1 | [Operator](projective.md#p8o3o3) · [Hodge and atomic data](invariants-higher-dimensional.md#53a423286d87) |
| [P7 / O(6)](projective.md#p7o6) | A7 | 6 | 2 | 7 | 1 | [Operator](projective.md#p7o6) · [Hodge and atomic data](invariants-higher-dimensional.md#8c15f95b6325) |
| [P8 / O(2)+O(5)](projective.md#p8o2o5) | A8 | 6 | 2 | 7 | 1 | [Operator](projective.md#p8o2o5) · [Hodge and atomic data](invariants-higher-dimensional.md#11d7c5142e09) |
| [P8 / O(3)+O(4)](projective.md#p8o3o4) | A8 | 6 | 2 | 7 | 1 | [Operator](projective.md#p8o3o4) · [Hodge and atomic data](invariants-higher-dimensional.md#d8d261b9c52c) |
| [P5  Fano index 6](projective.md#p5fanoindex6) | A5 | 5 | 6 | 6 | 1 | [Operator](projective.md#p5fanoindex6) · [Hodge and atomic data](invariants-fivefolds.md#75f4cdb8997b) |
| [G2/P1](additional.md#g2p1) | G2 | 5 | 5 | 6 | 1 | [Operator](additional.md#g2p1) · [Hodge and atomic data](invariants-fivefolds.md#fd2bd6eae26b) |
| [P6 / O(2)](projective.md#p6o2) | A6 | 5 | 5 | 6 | 1 | [Operator](projective.md#p6o2) · [Hodge and atomic data](invariants-fivefolds.md#7ccb7c3e0b6b) |
| [Gr(2,5) / O(1)](grassmannians.md#gr25o1) | A4 | 5 | 4 | 8 | 1 | [Operator](grassmannians.md#gr25o1) · [Hodge and atomic data](invariants-fivefolds.md#1584955327b7) |
| [Gr(3,5) / O(1)](grassmannians.md#gr35o1) | A4 | 5 | 4 | 8 | 1 | [Operator](grassmannians.md#gr35o1) · [Hodge and atomic data](invariants-fivefolds.md#1e7394ef8632) |
| [OG(3,7) / O(2)](additional.md#og37o2) | B3 | 5 | 4 | 6 | 1 | [Operator](additional.md#og37o2) · [Hodge and atomic data](invariants-fivefolds.md#76928fabba80) |
| [P6 / O(3)](projective.md#p6o3) | A6 | 5 | 4 | 6 | 1 | [Operator](projective.md#p6o3) · [Hodge and atomic data](invariants-fivefolds.md#c44e0fd4a5b0) |
| [P7 / O(2)+O(2)](projective.md#p7o2o2) | A7 | 5 | 4 | 6 | 1 | [Operator](projective.md#p7o2o2) · [Hodge and atomic data](invariants-fivefolds.md#75efe609f198) |
| [Quartic double cover of P⁵](records/qd5-001.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 4 | 6 | 1 | [Operator](records/qd5-001.md) · [Hodge and atomic data](invariants-fivefolds.md#qd5-001) |
| [Complete intersection (2,3) in P⁷](records/qc5-001.md) | Smooth projective 7-fold (ambient Picard rank 1) | 5 | 3 | 6 | 1 | [Operator](records/qc5-001.md) · [Hodge and atomic data](invariants-fivefolds.md#qc5-001) |
| [G2/P2](additional.md#g2p2) | G2 | 5 | 3 | 6 | 1 | [Operator](additional.md#g2p2) · [Hodge and atomic data](invariants-fivefolds.md#834882311808) |
| [Gr(2,5) / O(2)](grassmannians.md#gr25o2) | A4 | 5 | 3 | 8 | 1 | [Operator](grassmannians.md#gr25o2) · [Hodge and atomic data](invariants-fivefolds.md#1cd0a9ffb74e) |
| [Gr(2,6) / O(1)+O(1)+O(1)](grassmannians.md#gr26o1o1o1) | A5 | 5 | 3 | 8 | 1 | [Operator](grassmannians.md#gr26o1o1o1) · [Hodge and atomic data](invariants-fivefolds.md#51706ac77ff7) |
| [Gr(3,5) / O(2)](grassmannians.md#gr35o2) | A4 | 5 | 3 | 8 | 1 | [Operator](grassmannians.md#gr35o2) · [Hodge and atomic data](invariants-fivefolds.md#d7857b18eb8e) |
| [LG(3,6) / O(1)](additional.md#lg36o1) | C3 | 5 | 3 | 6 | 1 | [Operator](additional.md#lg36o1) · [Hodge and atomic data](invariants-fivefolds.md#141c91366f21) |
| [OG(3,7) / O(3)](additional.md#og37o3) | B3 | 5 | 3 | 6 | 1 | [Operator](additional.md#og37o3) · [Hodge and atomic data](invariants-fivefolds.md#29e94da02c49) |
| [P6 / O(4)](projective.md#p6o4) | A6 | 5 | 3 | 6 | 1 | [Operator](projective.md#p6o4) · [Hodge and atomic data](invariants-fivefolds.md#b740ed7ac87d) |
| [P7 / O(2)+O(3)](projective.md#p7o2o3) | A7 | 5 | 3 | 6 | 1 | [Operator](projective.md#p7o2o3) · [Hodge and atomic data](invariants-fivefolds.md#86a2cd927e5d) |
| [P8 / O(2)+O(2)+O(2)](projective.md#p8o2o2o2) | A8 | 5 | 3 | 6 | 1 | [Operator](projective.md#p8o2o2o2) · [Hodge and atomic data](invariants-fivefolds.md#649a71c1db0a) |
| [Quartic fivefold in P⁶](records/pci5-4.md) | Smooth projective 6-fold (ambient Picard rank 1) | 5 | 3 | 6 | 1 | [Operator](records/pci5-4.md) · [Hodge and atomic data](invariants-fivefolds.md#pci5-4) |
| [Complete intersection (2,2,2,2) in P⁹](records/pci5-2-2-2-2.md) | Smooth projective 9-fold (ambient Picard rank 1) | 5 | 2 | 6 | 1 | [Operator](records/pci5-2-2-2-2.md) · [Hodge and atomic data](invariants-fivefolds.md#pci5-2-2-2-2) |
| [Complete intersection (2,2,3) in P⁸](records/pci5-2-2-3.md) | Smooth projective 8-fold (ambient Picard rank 1) | 5 | 2 | 6 | 1 | [Operator](records/pci5-2-2-3.md) · [Hodge and atomic data](invariants-fivefolds.md#pci5-2-2-3) |
| [Complete intersection (2,4) in P⁷](records/pci5-2-4.md) | Smooth projective 7-fold (ambient Picard rank 1) | 5 | 2 | 6 | 1 | [Operator](records/pci5-2-4.md) · [Hodge and atomic data](invariants-fivefolds.md#pci5-2-4) |
| [Complete intersection (3,3) in P⁷](records/pci5-3-3.md) | Smooth projective 7-fold (ambient Picard rank 1) | 5 | 2 | 6 | 1 | [Operator](records/pci5-3-3.md) · [Hodge and atomic data](invariants-fivefolds.md#pci5-3-3) |
| [Complete intersection of multidegrees (2,2) in P³ × P³](records/pb5-028.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 2 | 12 | 2 | [Operator](records/pb5-028.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-028) |
| [Complete intersection of multidegrees (2,2) in P³ × P³](records/prod5-b01.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 2 | 12 | 2 | [Operator](records/prod5-b01.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-b01) |
| [Fl(1,4,5) / O(1,1)+O(1,1)](additional.md#fl145o11o11) | A4 | 5 | 2 | 12 | 2 | [Operator](additional.md#fl145o11o11) · [Hodge and atomic data](invariants-fivefolds.md#9cb29c69a3f5) |
| [Gr(2,5) / O(3)](grassmannians.md#gr25o3) | A4 | 5 | 2 | 8 | 1 | [Operator](grassmannians.md#gr25o3) · [Hodge and atomic data](invariants-fivefolds.md#dd16e36a8997) |
| [Gr(2,6) / O(1)+O(1)+O(2)](grassmannians.md#gr26o1o1o2) | A5 | 5 | 2 | 8 | 1 | [Operator](grassmannians.md#gr26o1o1o2) · [Hodge and atomic data](invariants-fivefolds.md#c7da579d09a1) |
| [Gr(3,5) / O(3)](grassmannians.md#gr35o3) | A4 | 5 | 2 | 8 | 1 | [Operator](grassmannians.md#gr35o3) · [Hodge and atomic data](invariants-fivefolds.md#ffb644472d2c) |
| [OG(3,7) / O(4)](additional.md#og37o4) | B3 | 5 | 2 | 6 | 1 | [Operator](additional.md#og37o4) · [Hodge and atomic data](invariants-fivefolds.md#10e047830d24) |
| [P6 / O(5)](projective.md#p6o5) | A6 | 5 | 2 | 6 | 1 | [Operator](projective.md#p6o5) · [Hodge and atomic data](invariants-fivefolds.md#ee9c4f882e7c) |
| [P7 / O(2)+O(4)](projective.md#p7o2o4) | A7 | 5 | 2 | 6 | 1 | [Operator](projective.md#p7o2o4) · [Hodge and atomic data](invariants-fivefolds.md#bbd63cac242a) |
| [P7 / O(3)+O(3)](projective.md#p7o3o3) | A7 | 5 | 2 | 6 | 1 | [Operator](projective.md#p7o3o3) · [Hodge and atomic data](invariants-fivefolds.md#0dfe4b49547a) |
| [P8 / O(2)+O(2)+O(3)](projective.md#p8o2o2o3) | A8 | 5 | 2 | 6 | 1 | [Operator](projective.md#p8o2o2o3) · [Hodge and atomic data](invariants-fivefolds.md#819481252d0a) |
| [Quintic fivefold in P⁶](records/pci5-5.md) | Smooth projective 6-fold (ambient Picard rank 1) | 5 | 2 | 6 | 1 | [Operator](records/pci5-5.md) · [Hodge and atomic data](invariants-fivefolds.md#pci5-5) |
| [Complete intersection (2,2,2,2,2) in P¹⁰](records/pci5-2-2-2-2-2.md) | Smooth projective 10-fold (ambient Picard rank 1) | 5 | 1 | 6 | 1 | [Operator](records/pci5-2-2-2-2-2.md) · [Hodge and atomic data](invariants-fivefolds.md#pci5-2-2-2-2-2) |
| [Complete intersection (2,2,2,3) in P⁹](records/pci5-2-2-2-3.md) | Smooth projective 9-fold (ambient Picard rank 1) | 5 | 1 | 6 | 1 | [Operator](records/pci5-2-2-2-3.md) · [Hodge and atomic data](invariants-fivefolds.md#pci5-2-2-2-3) |
| [Complete intersection (2,2,4) in P⁸](records/pci5-2-2-4.md) | Smooth projective 8-fold (ambient Picard rank 1) | 5 | 1 | 6 | 1 | [Operator](records/pci5-2-2-4.md) · [Hodge and atomic data](invariants-fivefolds.md#pci5-2-2-4) |
| [Complete intersection (2,3,3) in P⁸](records/pci5-2-3-3.md) | Smooth projective 8-fold (ambient Picard rank 1) | 5 | 1 | 6 | 1 | [Operator](records/pci5-2-3-3.md) · [Hodge and atomic data](invariants-fivefolds.md#pci5-2-3-3) |
| [Complete intersection (2,5) in P⁷](records/pci5-2-5.md) | Smooth projective 7-fold (ambient Picard rank 1) | 5 | 1 | 6 | 1 | [Operator](records/pci5-2-5.md) · [Hodge and atomic data](invariants-fivefolds.md#pci5-2-5) |
| [Complete intersection (3,4) in P⁷](records/pci5-3-4.md) | Smooth projective 7-fold (ambient Picard rank 1) | 5 | 1 | 6 | 1 | [Operator](records/pci5-3-4.md) · [Hodge and atomic data](invariants-fivefolds.md#pci5-3-4) |
| [Complete intersection of multidegrees (1,1), (1,1), (1,2) in P³ × P⁵](records/pb5-060.md) | Smooth projective 8-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-060.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-060) |
| [Complete intersection of multidegrees (1,3) in P¹ × P⁵](records/pb5-003.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 10 | 2 | [Operator](records/pb5-003.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-003) |
| [Complete intersection of multidegrees (2,1), (1,2) in P³ × P⁴](records/pb5-051.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-051.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-051) |
| [Complete intersection of multidegrees (2,1), (1,2) in P³ × P⁴](records/prod5-d02.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/prod5-d02.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-d02) |
| [Complete intersection of multidegrees (2,1), (1,2), (1,1) in P⁴ × P⁴](records/prod5-e02.md) | Smooth projective 8-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/prod5-e02.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-e02) |
| [Complete intersection of multidegrees (2,1), (1,3) in P³ × P⁴](records/prod5-d04.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/prod5-d04.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-d04) |
| [Complete intersection of multidegrees (2,2) in P² × P⁴](records/prod5-a01.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/prod5-a01.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-a01) |
| [Complete intersection of multidegrees (2,2), (1,1) in P³ × P⁴](records/prod5-d01.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/prod5-d01.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-d01) |
| [Complete intersection of multidegrees (2,2), (1,1), (1,1) in P⁴ × P⁴](records/prod5-e01.md) | Smooth projective 8-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/prod5-e01.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-e01) |
| [Complete intersection of multidegrees (2,2), (1,2) in P³ × P⁴](records/prod5-d05.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/prod5-d05.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-d05) |
| [Complete intersection of multidegrees (2,2,2) in P² × P² × P²](records/prod5-c01.md) | Smooth projective 6-fold (ambient Picard rank 3) | 5 | 1 | 20 | 3 | [Operator](records/prod5-c01.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-c01) |
| [Complete intersection of multidegrees (2,3) in P² × P⁴](records/prod5-a02.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/prod5-a02.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-a02) |
| [Complete intersection of multidegrees (2,3) in P³ × P³](records/prod5-b02.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/prod5-b02.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-b02) |
| [Complete intersection of multidegrees (2,3), (1,1) in P³ × P⁴](records/prod5-d03.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/prod5-d03.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-d03) |
| [Complete intersection of multidegrees (2,4) in P² × P⁴](records/prod5-a03.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/prod5-a03.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-a03) |
| [Complete intersection of multidegrees (3,3) in P³ × P³](records/prod5-b03.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/prod5-b03.md) · [Hodge and atomic data](invariants-fivefolds.md#prod5-b03) |
| [Degree-6 fivefold in P⁶](records/pci5-6.md) | Smooth projective 6-fold (ambient Picard rank 1) | 5 | 1 | 6 | 1 | [Operator](records/pci5-6.md) · [Hodge and atomic data](invariants-fivefolds.md#pci5-6) |
| [Section of P_{P²}(O^4 ⊕ O(1)) by 3ξ+H](records/pb5-016.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-016.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-016) |
| [Section of P_{P²}(O^4 ⊕ O(1)) by 4ξ+H](records/pb5-017.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-017.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-017) |
| [Section of P_{P³}(O^2 ⊕ O(1)^2) by 2ξ+H](records/pb5-043.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-043.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-043) |
| [Section of P_{P³}(O^2 ⊕ O(1)^2) by 3ξ+H](records/pb5-044.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-044.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-044) |
| [Section of P_{P³}(O^3 ⊕ O(1)) by 2ξ+2H](records/pb5-036.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-036.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-036) |
| [Section of P_{P³}(O^3 ⊕ O(1)) by 3ξ+2H](records/pb5-038.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-038.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-038) |
| [Section of P_{P³}(O^3 ⊕ O(1)) by 3ξ+H](records/pb5-037.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-037.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-037) |
| [Section of P_{P³}(O^3 ⊕ O(2)) by 2ξ+H](records/pb5-040.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-040.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-040) |
| [Section of P_{P³}(O^3 ⊕ O(2)) by 3ξ+H](records/pb5-041.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-041.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-041) |
| [Section of P_{P³}(O^4 ⊕ O(1)) by 2ξ+H, 2ξ+H](records/pb5-058.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-058.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-058) |
| [Section of P_{P³}(O^4 ⊕ O(1)) by ξ+H, 2ξ+H](records/pb5-056.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-056.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-056) |
| [Section of P_{P³}(O^4 ⊕ O(1)) by ξ+H, 3ξ+H](records/pb5-057.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-057.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-057) |
| [Section of P_{P⁴}(O ⊕ O(1) ⊕ O(2)) by 2ξ+H](records/pb5-088.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-088.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-088) |
| [Section of P_{P⁴}(O ⊕ O(1)^2) by 2ξ+2H](records/pb5-086.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-086.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-086) |
| [Section of P_{P⁴}(O ⊕ O(1)^2) by 2ξ+H](records/pb5-085.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-085.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-085) |
| [Section of P_{P⁴}(O^2 ⊕ O(1)) by 2ξ+2H](records/pb5-075.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-075.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-075) |
| [Section of P_{P⁴}(O^2 ⊕ O(1)) by 2ξ+3H](records/pb5-076.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-076.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-076) |
| [Section of P_{P⁴}(O^2 ⊕ O(1)^2) by ξ+H, 2ξ+H](records/pb5-107.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-107.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-107) |
| [Section of P_{P⁴}(O^2 ⊕ O(2)) by 2ξ+2H](records/pb5-080.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-080.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-080) |
| [Section of P_{P⁴}(O^2 ⊕ O(2)) by 2ξ+H](records/pb5-079.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-079.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-079) |
| [Section of P_{P⁴}(O^2 ⊕ O(3)) by 2ξ+H](records/pb5-082.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-082.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-082) |
| [Section of P_{P⁴}(O^3 ⊕ O(1)) by ξ+2H, 2ξ+H](records/pb5-103.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-103.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-103) |
| [Section of P_{P⁴}(O^3 ⊕ O(1)) by ξ+H, 2ξ+2H](records/pb5-102.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-102.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-102) |
| [Section of P_{P⁴}(O^3 ⊕ O(1)) by ξ+H, 2ξ+H](records/pb5-101.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-101.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-101) |
| [Section of P_{P⁴}(O^3 ⊕ O(2)) by ξ+H, 2ξ+H](records/pb5-105.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-105.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-105) |
| [Section of P_{P⁴}(O^4 ⊕ O(1)) by ξ+H, ξ+H, 2ξ+H](records/pb5-114.md) | Smooth projective 8-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-114.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-114) |
| [Section of P_{P⁵}(O ⊕ O(1) ⊕ O(2)) by ξ+H, ξ+H](records/pb5-147.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-147.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-147) |
| [Section of P_{P⁵}(O ⊕ O(1)) by ξ+3H](records/pb5-124.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 10 | 2 | [Operator](records/pb5-124.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-124) |
| [Section of P_{P⁵}(O ⊕ O(2)) by ξ+2H](records/pb5-127.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 10 | 2 | [Operator](records/pb5-127.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-127) |
| [Section of P_{P⁵}(O ⊕ O(2)) by ξ+3H](records/pb5-128.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 10 | 2 | [Operator](records/pb5-128.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-128) |
| [Section of P_{P⁵}(O ⊕ O(3)) by ξ+2H](records/pb5-130.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 10 | 2 | [Operator](records/pb5-130.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-130) |
| [Section of P_{P⁵}(O ⊕ O(4)) by ξ+H](records/pb5-131.md) | Smooth projective 6-fold (ambient Picard rank 2) | 5 | 1 | 10 | 2 | [Operator](records/pb5-131.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-131) |
| [Section of P_{P⁵}(O^2 ⊕ O(1)) by ξ+H, ξ+2H](records/pb5-139.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-139.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-139) |
| [Section of P_{P⁵}(O^2 ⊕ O(1)^2) by ξ+H, ξ+H, ξ+H](records/pb5-155.md) | Smooth projective 8-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-155.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-155) |
| [Section of P_{P⁵}(O^2 ⊕ O(2)) by ξ+H, ξ+2H](records/pb5-143.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-143.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-143) |
| [Section of P_{P⁵}(O^2 ⊕ O(3)) by ξ+H, ξ+H](records/pb5-144.md) | Smooth projective 7-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-144.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-144) |
| [Section of P_{P⁵}(O^3 ⊕ O(1)) by ξ+H, ξ+H, ξ+2H](records/pb5-153.md) | Smooth projective 8-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-153.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-153) |
| [Section of P_{P⁵}(O^3 ⊕ O(2)) by ξ+H, ξ+H, ξ+H](records/pb5-154.md) | Smooth projective 8-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-154.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-154) |
| [Section of P_{P⁵}(O^4 ⊕ O(1)) by ξ+H, ξ+H, ξ+H, ξ+H](records/pb5-158.md) | Smooth projective 9-fold (ambient Picard rank 2) | 5 | 1 | 12 | 2 | [Operator](records/pb5-158.md) · [Hodge and atomic data](invariants-fivefolds.md#pb5-158) |
| [Gr(4,5)](grassmannians.md#gr45) | A4 | 4 | 5 | 5 | 1 | [Operator](grassmannians.md#gr45) · [Hodge and atomic data](invariants-fourfolds.md#139781d9fb14) |
| [P4  Fano index 5](projective.md#p4fanoindex5) | A4 | 4 | 5 | 5 | 1 | [Operator](projective.md#p4fanoindex5) · [Hodge and atomic data](invariants-fourfolds.md#53078b491137) |
| [P⁴ (CKP-001)](records/ckp-001.md) | Smooth projective 5-fold (ambient Picard rank 1) | 4 | 5 | 5 | 1 | [Operator](records/ckp-001.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-001) |
| [Gr(2,4)](grassmannians.md#gr24) | A3 | 4 | 4 | 6 | 1 | [Operator](grassmannians.md#gr24) · [Hodge and atomic data](invariants-fourfolds.md#51615a7643a1) |
| [P5 / O(2)](projective.md#p5o2) | A5 | 4 | 4 | 5 | 1 | [Operator](projective.md#p5o2) · [Hodge and atomic data](invariants-fourfolds.md#8884770b89b8) |
| [Quadric fourfold in P⁵ (CKP-003)](records/ckp-003.md) | Smooth projective 5-fold (ambient Picard rank 1) | 4 | 4 | 5 | 1 | [Operator](records/ckp-003.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-003) |
| [Complete intersection (2,2) in P⁶ (CKP-033)](records/ckp-033.md) | Smooth projective 6-fold (ambient Picard rank 1) | 4 | 3 | 5 | 1 | [Operator](records/ckp-033.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-033) |
| [Cubic fourfold in P⁵ (CKP-037)](records/ckp-037.md) | Smooth projective 5-fold (ambient Picard rank 1) | 4 | 3 | 5 | 1 | [Operator](records/ckp-037.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-037) |
| [Gr(2,5) / O(1)+O(1)](grassmannians.md#gr25o1o1) | A4 | 4 | 3 | 6 | 1 | [Operator](grassmannians.md#gr25o1o1) · [Hodge and atomic data](invariants-fourfolds.md#3c0ee725b9d8) |
| [Gr(3,5) / O(1)+O(1)](grassmannians.md#gr35o1o1) | A4 | 4 | 3 | 6 | 1 | [Operator](grassmannians.md#gr35o1o1) · [Hodge and atomic data](invariants-fourfolds.md#fbeb5f79765b) |
| [P5 / O(3)](projective.md#p5o3) | A5 | 4 | 3 | 5 | 1 | [Operator](projective.md#p5o3) · [Hodge and atomic data](invariants-fourfolds.md#31aadf32267f) |
| [P6 / O(2)+O(2)](projective.md#p6o2o2) | A6 | 4 | 3 | 5 | 1 | [Operator](projective.md#p6o2o2) · [Hodge and atomic data](invariants-fourfolds.md#e4065b55a49a) |
| [Complete intersection (2,2,2) in P⁷ (CKP-596)](records/ckp-596.md) | Smooth projective 7-fold (ambient Picard rank 1) | 4 | 2 | 5 | 1 | [Operator](records/ckp-596.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-596) |
| [Complete intersection (2,3) in P⁶ (CKP-640)](records/ckp-640.md) | Smooth projective 6-fold (ambient Picard rank 1) | 4 | 2 | 5 | 1 | [Operator](records/ckp-640.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-640) |
| [Complete intersection of multidegrees (0,3) in P¹ × P⁴ (CKP-567)](records/ckp-567.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 2 | 8 | 2 | [Operator](records/ckp-567.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-567) |
| [Complete intersection of multidegrees (1,1), (1,1) in P³ × P³ (CKP-189)](records/ckp-189.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 2 | 9 | 2 | [Operator](records/ckp-189.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-189) |
| [Complete intersection of multidegrees (1,2) in P² × P³ (CKP-327)](records/ckp-327.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 2 | 9 | 2 | [Operator](records/ckp-327.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-327) |
| [Fl(1,3,4) / O(1,1)](additional.md#fl134o11) | A3 | 4 | 2 | 9 | 2 | [Operator](additional.md#fl134o11) · [Hodge and atomic data](invariants-fourfolds.md#3ed191207b19) |
| [G2/P2 / O(1)](additional.md#g2p2o1) | G2 | 4 | 2 | 5 | 1 | [Operator](additional.md#g2p2o1) · [Hodge and atomic data](invariants-fourfolds.md#b9a91f8b2a8f) |
| [Gr(2,5) / O(1)+O(2)](grassmannians.md#gr25o1o2) | A4 | 4 | 2 | 6 | 1 | [Operator](grassmannians.md#gr25o1o2) · [Hodge and atomic data](invariants-fourfolds.md#5a3a05721152) |
| [Gr(3,5) / O(1)+O(2)](grassmannians.md#gr35o1o2) | A4 | 4 | 2 | 6 | 1 | [Operator](grassmannians.md#gr35o1o2) · [Hodge and atomic data](invariants-fourfolds.md#0c8674c9ad6f) |
| [LG(3,6) / O(1)+O(1)](additional.md#lg36o1o1) | C3 | 4 | 2 | 5 | 1 | [Operator](additional.md#lg36o1o1) · [Hodge and atomic data](invariants-fourfolds.md#5a3d521e7212) |
| [OG(3,7) / O(2)+O(2)](additional.md#og37o2o2) | B3 | 4 | 2 | 5 | 1 | [Operator](additional.md#og37o2o2) · [Hodge and atomic data](invariants-fourfolds.md#176397975a00) |
| [P5 / O(4)](projective.md#p5o4) | A5 | 4 | 2 | 5 | 1 | [Operator](projective.md#p5o4) · [Hodge and atomic data](invariants-fourfolds.md#8bd58b781863) |
| [P6 / O(2)+O(3)](projective.md#p6o2o3) | A6 | 4 | 2 | 5 | 1 | [Operator](projective.md#p6o2o3) · [Hodge and atomic data](invariants-fourfolds.md#6324179fa1e1) |
| [P7 / O(2)+O(2)+O(2)](projective.md#p7o2o2o2) | A7 | 4 | 2 | 5 | 1 | [Operator](projective.md#p7o2o2o2) · [Hodge and atomic data](invariants-fourfolds.md#d68ecb775686) |
| [Quartic fourfold in P⁵ (CKP-682)](records/ckp-682.md) | Smooth projective 5-fold (ambient Picard rank 1) | 4 | 2 | 5 | 1 | [Operator](records/ckp-682.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-682) |
| [Section of P_{P²}(O^3 ⊕ O(1)) by 2ξ (CKP-186)](records/ckp-186.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 2 | 9 | 2 | [Operator](records/ckp-186.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-186) |
| [Section of P_{P³}(O^2 ⊕ O(1)) by ξ+H (CKP-061)](records/ckp-061.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 2 | 9 | 2 | [Operator](records/ckp-061.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-061) |
| [Section of P_{P⁴}(O ⊕ O(1)) by 2H (CKP-060)](records/ckp-060.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 2 | 8 | 2 | [Operator](records/ckp-060.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-060) |
| [Verra fourfold (HLM-29)](records/hlm-29.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 2 | 9 | 2 | [Operator](records/hlm-29.md) · [Hodge and atomic data](invariants-fourfolds.md#hlm-29) |
| [Complete intersection (2,2,2,2) in P⁸ (CKP-731)](records/ckp-731.md) | Smooth projective 8-fold (ambient Picard rank 1) | 4 | 1 | 5 | 1 | [Operator](records/ckp-731.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-731) |
| [Complete intersection (2,2,3) in P⁷ (CKP-735)](records/ckp-735.md) | Smooth projective 7-fold (ambient Picard rank 1) | 4 | 1 | 5 | 1 | [Operator](records/ckp-735.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-735) |
| [Complete intersection (2,4) in P⁶ (CKP-737)](records/ckp-737.md) | Smooth projective 6-fold (ambient Picard rank 1) | 4 | 1 | 5 | 1 | [Operator](records/ckp-737.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-737) |
| [Complete intersection (3,3) in P⁶ (CKP-736)](records/ckp-736.md) | Smooth projective 6-fold (ambient Picard rank 1) | 4 | 1 | 5 | 1 | [Operator](records/ckp-736.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-736) |
| [Complete intersection of multidegrees (0,2) in P¹ × P⁴ (CKP-111)](records/ckp-111.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-111.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-111) |
| [Complete intersection of multidegrees (1,1) in P² × P³ (CKP-078)](records/ckp-078.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-078.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-078) |
| [Complete intersection of multidegrees (1,1) in P¹ × P⁴ (CKP-002)](records/ckp-002.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-002.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-002) |
| [Complete intersection of multidegrees (1,1), (1,1) in P² × P⁴ (CKP-018)](records/ckp-018.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-018.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-018) |
| [Complete intersection of multidegrees (1,1), (1,1), (1,1) in P³ × P⁴ (CKP-175)](records/ckp-175.md) | Smooth projective 7-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-175.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-175) |
| [Complete intersection of multidegrees (1,1), (1,1), (1,1), (1,1) in P⁴ × P⁴ (CKP-665)](records/ckp-665.md) | Smooth projective 8-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-665.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-665) |
| [Complete intersection of multidegrees (1,1), (1,1), (1,2) in P³ × P⁴ (CKP-681)](records/ckp-681.md) | Smooth projective 7-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-681.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-681) |
| [Complete intersection of multidegrees (1,1), (1,2) in P² × P⁴ (CKP-322)](records/ckp-322.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-322.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-322) |
| [Complete intersection of multidegrees (1,1), (1,3) in P² × P⁴ (CKP-722)](records/ckp-722.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-722.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-722) |
| [Complete intersection of multidegrees (1,1), (2,1) in P³ × P³ (CKP-323)](records/ckp-323.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-323.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-323) |
| [Complete intersection of multidegrees (1,1), (2,2) in P³ × P³ (CKP-715)](records/ckp-715.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-715.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-715) |
| [Complete intersection of multidegrees (1,1,1) in P¹ × P² × P² (CKP-247)](records/ckp-247.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 13 | 3 | [Operator](records/ckp-247.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-247) |
| [Complete intersection of multidegrees (1,1,1) in P¹ × P¹ × P³ (CKP-102)](records/ckp-102.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 12 | 3 | [Operator](records/ckp-102.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-102) |
| [Complete intersection of multidegrees (1,1,1), (1,1,1) in P² × P² × P² (CKP-623)](records/ckp-623.md) | Smooth projective 6-fold (ambient Picard rank 3) | 4 | 1 | 14 | 3 | [Operator](records/ckp-623.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-623) |
| [Complete intersection of multidegrees (1,1,1,1) in P¹ × P¹ × P¹ × P² (CKP-475)](records/ckp-475.md) | Smooth projective 5-fold (ambient Picard rank 4) | 4 | 1 | 17 | 4 | [Operator](records/ckp-475.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-475) |
| [Complete intersection of multidegrees (1,1,1,1,1) in P¹ × P¹ × P¹ × P¹ × P¹ (CKP-628)](records/ckp-628.md) | Smooth projective 5-fold (ambient Picard rank 5) | 4 | 1 | 22 | 5 | [Operator](records/ckp-628.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-628) |
| [Complete intersection of multidegrees (1,1,1,2) in P¹ × P¹ × P¹ × P² (CKP-667)](records/ckp-667.md) | Smooth projective 5-fold (ambient Picard rank 4) | 4 | 1 | 17 | 4 | [Operator](records/ckp-667.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-667) |
| [Complete intersection of multidegrees (1,1,2) in P¹ × P¹ × P³ (CKP-432)](records/ckp-432.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 12 | 3 | [Operator](records/ckp-432.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-432) |
| [Complete intersection of multidegrees (1,1,3) in P¹ × P¹ × P³ (CKP-721)](records/ckp-721.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 12 | 3 | [Operator](records/ckp-721.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-721) |
| [Complete intersection of multidegrees (1,2) in P¹ × P⁴ (CKP-030)](records/ckp-030.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-030.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-030) |
| [Complete intersection of multidegrees (1,2), (1,2) in P² × P⁴ (CKP-711)](records/ckp-711.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-711.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-711) |
| [Complete intersection of multidegrees (1,2,1) in P¹ × P² × P² (CKP-560)](records/ckp-560.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 13 | 3 | [Operator](records/ckp-560.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-560) |
| [Complete intersection of multidegrees (1,2,2) in P¹ × P² × P² (CKP-698)](records/ckp-698.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 13 | 3 | [Operator](records/ckp-698.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-698) |
| [Complete intersection of multidegrees (1,3) in P² × P³ (CKP-694)](records/ckp-694.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-694.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-694) |
| [Complete intersection of multidegrees (1,3) in P¹ × P⁴ (CKP-566)](records/ckp-566.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-566.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-566) |
| [Complete intersection of multidegrees (1,4) in P¹ × P⁴ (CKP-734)](records/ckp-734.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-734.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-734) |
| [Complete intersection of multidegrees (2,1) in P² × P³ (CKP-107)](records/ckp-107.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-107.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-107) |
| [Complete intersection of multidegrees (2,1), (1,2) in P³ × P³ (CKP-705)](records/ckp-705.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-705.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-705) |
| [Complete intersection of multidegrees (2,2) in P² × P³ (CKP-439)](records/ckp-439.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-439.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-439) |
| [Complete intersection of multidegrees (2,3) in P² × P³ (CKP-726)](records/ckp-726.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-726.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-726) |
| [Five hyperplanes and a quadric in the spinor tenfold](records/spinor-1x5-2.md) | D5 / kept root 4 | 4 | 1 | 5 | 1 | [Operator](records/spinor-1x5-2.md) · [Hodge and atomic data](invariants-fourfolds.md#spinor-1x5-2) |
| [Fl(1,2,5) / O(0,1)+O(0,2)+O(1,0)](additional.md#fl125o01o02o10gm20) | A4 | 4 | 1 | 9 | 2 | [Operator](additional.md#fl125o01o02o10gm20) · [Hodge and atomic data](invariants-fourfolds.md#e1322438fd01) |
| [Gr(2,5) / O(1)+O(3)](grassmannians.md#gr25o1o3) | A4 | 4 | 1 | 6 | 1 | [Operator](grassmannians.md#gr25o1o3) · [Hodge and atomic data](invariants-fourfolds.md#d2a92bddd407) |
| [Gr(2,5) / O(2)+O(2)](grassmannians.md#gr25o2o2) | A4 | 4 | 1 | 6 | 1 | [Operator](grassmannians.md#gr25o2o2) · [Hodge and atomic data](invariants-fourfolds.md#71c4061dbdf2) |
| [Gr(3,5) / O(1)+O(3)](grassmannians.md#gr35o1o3) | A4 | 4 | 1 | 6 | 1 | [Operator](grassmannians.md#gr35o1o3) · [Hodge and atomic data](invariants-fourfolds.md#f418dda622c4) |
| [Gr(3,5) / O(2)+O(2)](grassmannians.md#gr35o2o2) | A4 | 4 | 1 | 6 | 1 | [Operator](grassmannians.md#gr35o2o2) · [Hodge and atomic data](invariants-fourfolds.md#a6bf73eeb7fb) |
| [Hyperplane and quadric section of LG(3,6)](records/lg3-1-2.md) | C3 / kept root 3 | 4 | 1 | 5 | 1 | [Operator](records/lg3-1-2.md) · [Hodge and atomic data](invariants-fourfolds.md#lg3-1-2) |
| [Hypersurface in a toric fivefold (CKP-172)](records/ckp-172.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 12 | 3 | [Operator](records/ckp-172.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-172) |
| [Hypersurface in a toric fivefold (CKP-320)](records/ckp-320.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 13 | 3 | [Operator](records/ckp-320.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-320) |
| [P5 / O(5)](projective.md#p5o5) | A5 | 4 | 1 | 5 | 1 | [Operator](projective.md#p5o5) · [Hodge and atomic data](invariants-fourfolds.md#61e63b38f5a8) |
| [P6 / O(2)+O(4)](projective.md#p6o2o4) | A6 | 4 | 1 | 5 | 1 | [Operator](projective.md#p6o2o4) · [Hodge and atomic data](invariants-fourfolds.md#3150500f5723) |
| [P6 / O(3)+O(3)](projective.md#p6o3o3) | A6 | 4 | 1 | 5 | 1 | [Operator](projective.md#p6o3o3) · [Hodge and atomic data](invariants-fourfolds.md#de2575bbb840) |
| [P7 / O(2)+O(2)+O(3)](projective.md#p7o2o2o3) | A7 | 4 | 1 | 5 | 1 | [Operator](projective.md#p7o2o2o3) · [Hodge and atomic data](invariants-fourfolds.md#5ae4d92d2f20) |
| [Quadric section of the adjoint G₂ variety](records/g2-quadric.md) | G2 / kept root 2 | 4 | 1 | 5 | 1 | [Operator](records/g2-quadric.md) · [Hodge and atomic data](invariants-fourfolds.md#g2-quadric) |
| [Quintic fourfold in P⁵ (CKP-738)](records/ckp-738.md) | Smooth projective 5-fold (ambient Picard rank 1) | 4 | 1 | 5 | 1 | [Operator](records/ckp-738.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-738) |
| [Section of P_{P² × P²}(O ⊕ O(1,0)) by ξ+H1+2H2 (CKP-594)](records/ckp-594.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 13 | 3 | [Operator](records/ckp-594.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-594) |
| [Section of P_{P² × P²}(O ⊕ O(1,0)) by ξ+H1+H2 (CKP-363)](records/ckp-363.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 13 | 3 | [Operator](records/ckp-363.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-363) |
| [Section of P_{P² × P²}(O ⊕ O(1,1)) by ξ+H1+H2 (CKP-450)](records/ckp-450.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 13 | 3 | [Operator](records/ckp-450.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-450) |
| [Section of P_{P² × P²}(O(0,1) ⊕ O(1,0)) by ξ+H1+H2 (CKP-492)](records/ckp-492.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 13 | 3 | [Operator](records/ckp-492.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-492) |
| [Section of P_{P²}(O^2 ⊕ O(1)^2) by 2ξ (CKP-233)](records/ckp-233.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-233.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-233) |
| [Section of P_{P²}(O^2 ⊕ O(1)^2) by 3ξ (CKP-702)](records/ckp-702.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-702.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-702) |
| [Section of P_{P²}(O^3 ⊕ O(1)) by 2ξ+H (CKP-314)](records/ckp-314.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-314.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-314) |
| [Section of P_{P²}(O^3 ⊕ O(1)) by 3ξ (CKP-688)](records/ckp-688.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-688.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-688) |
| [Section of P_{P²}(O^3 ⊕ O(1)) by 3ξ+H (CKP-718)](records/ckp-718.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-718.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-718) |
| [Section of P_{P²}(O^3 ⊕ O(1)) by ξ+H (CKP-014)](records/ckp-014.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-014.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-014) |
| [Section of P_{P²}(O^3 ⊕ O(2)) by 2ξ (CKP-182)](records/ckp-182.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-182.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-182) |
| [Section of P_{P²}(O^3 ⊕ O(2)) by 3ξ (CKP-691)](records/ckp-691.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-691.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-691) |
| [Section of P_{P³}(O ⊕ O(1)^2) by 2ξ (CKP-145)](records/ckp-145.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-145.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-145) |
| [Section of P_{P³}(O ⊕ O(1)^2) by 2ξ+H (CKP-595)](records/ckp-595.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-595.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-595) |
| [Section of P_{P³}(O ⊕ O(1)^2) by ξ+H (CKP-114)](records/ckp-114.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-114.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-114) |
| [Section of P_{P³}(O ⊕ O(2)^2) by 2ξ (HLM-27)](records/hlm-27.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/hlm-27.md) · [Hodge and atomic data](invariants-fourfolds.md#hlm-27) |
| [Section of P_{P³}(O^2 ⊕ O(1)) by 2ξ+2H (CKP-685)](records/ckp-685.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-685.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-685) |
| [Section of P_{P³}(O^2 ⊕ O(1)) by 2ξ+H (CKP-174)](records/ckp-174.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-174.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-174) |
| [Section of P_{P³}(O^2 ⊕ O(1)) by ξ+2H (CKP-170)](records/ckp-170.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-170.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-170) |
| [Section of P_{P³}(O^2 ⊕ O(2)) by 2ξ+H (CKP-179)](records/ckp-179.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-179.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-179) |
| [Section of P_{P³}(O^2 ⊕ O(2)) by ξ+H (CKP-049)](records/ckp-049.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-049.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-049) |
| [Section of P_{P³}(O^3 ⊕ O(1)) by ξ+H, 2ξ+H (CKP-656)](records/ckp-656.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-656.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-656) |
| [Section of P_{P³}(O^3 ⊕ O(1)) by ξ+H, ξ+H (CKP-160)](records/ckp-160.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-160.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-160) |
| [Section of P_{P¹ × P²}(O^2 ⊕ O(0,1)) by 2ξ+H1+H2 (CKP-639)](records/ckp-639.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 13 | 3 | [Operator](records/ckp-639.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-639) |
| [Section of P_{P¹ × P²}(O^2 ⊕ O(0,1)) by ξ+H1+H2 (CKP-155)](records/ckp-155.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 13 | 3 | [Operator](records/ckp-155.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-155) |
| [Section of P_{P¹ × P³}(O ⊕ O(0,1)) by ξ+H1+2H2 (CKP-593)](records/ckp-593.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 12 | 3 | [Operator](records/ckp-593.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-593) |
| [Section of P_{P¹ × P³}(O ⊕ O(0,1)) by ξ+H1+H2 (CKP-144)](records/ckp-144.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 12 | 3 | [Operator](records/ckp-144.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-144) |
| [Section of P_{P¹ × P³}(O ⊕ O(0,2)) by ξ+H1+H2 (CKP-157)](records/ckp-157.md) | Smooth projective 5-fold (ambient Picard rank 3) | 4 | 1 | 12 | 3 | [Operator](records/ckp-157.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-157) |
| [Section of P_{P¹ × P¹ × P²}(O ⊕ O(0,0,1)) by ξ+H1+H2+H3 (CKP-535)](records/ckp-535.md) | Smooth projective 5-fold (ambient Picard rank 4) | 4 | 1 | 17 | 4 | [Operator](records/ckp-535.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-535) |
| [Section of P_{P¹}(O^4 ⊕ O(1)) by 2ξ (CKP-026)](records/ckp-026.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-026.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-026) |
| [Section of P_{P¹}(O^4 ⊕ O(1)) by 3ξ (CKP-551)](records/ckp-551.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-551.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-551) |
| [Section of P_{P¹}(O^4 ⊕ O(1)) by 4ξ (CKP-733)](records/ckp-733.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-733.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-733) |
| [Section of P_{P⁴}(O ⊕ O(1)) by 3H (CKP-169)](records/ckp-169.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-169.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-169) |
| [Section of P_{P⁴}(O ⊕ O(1)) by ξ+2H (CKP-039)](records/ckp-039.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-039.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-039) |
| [Section of P_{P⁴}(O ⊕ O(1)) by ξ+3H (CKP-683)](records/ckp-683.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-683.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-683) |
| [Section of P_{P⁴}(O ⊕ O(1)) by ξ+H (CKP-004)](records/ckp-004.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-004.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-004) |
| [Section of P_{P⁴}(O ⊕ O(1)^2) by ξ+H, ξ+H (CKP-498)](records/ckp-498.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-498.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-498) |
| [Section of P_{P⁴}(O ⊕ O(2)) by 2H (CKP-046)](records/ckp-046.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-046.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-046) |
| [Section of P_{P⁴}(O ⊕ O(2)) by ξ+2H (CKP-041)](records/ckp-041.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-041.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-041) |
| [Section of P_{P⁴}(O ⊕ O(2)) by ξ+H (CKP-005)](records/ckp-005.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-005.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-005) |
| [Section of P_{P⁴}(O ⊕ O(3)) by ξ+H (CKP-006)](records/ckp-006.md) | Smooth projective 5-fold (ambient Picard rank 2) | 4 | 1 | 8 | 2 | [Operator](records/ckp-006.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-006) |
| [Section of P_{P⁴}(O^2 ⊕ O(1)) by ξ+H, ξ+2H (CKP-645)](records/ckp-645.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-645.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-645) |
| [Section of P_{P⁴}(O^2 ⊕ O(1)) by ξ+H, ξ+H (CKP-036)](records/ckp-036.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-036.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-036) |
| [Section of P_{P⁴}(O^2 ⊕ O(2)) by ξ+H, ξ+H (CKP-040)](records/ckp-040.md) | Smooth projective 6-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-040.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-040) |
| [Section of P_{P⁴}(O^3 ⊕ O(1)) by ξ+H, ξ+H, ξ+H (CKP-611)](records/ckp-611.md) | Smooth projective 7-fold (ambient Picard rank 2) | 4 | 1 | 9 | 2 | [Operator](records/ckp-611.md) · [Hodge and atomic data](invariants-fourfolds.md#ckp-611) |
| [Gr(3,4)](grassmannians.md#gr34) | A3 | 3 | 4 | 4 | 1 | [Operator](grassmannians.md#gr34) · [Hodge and atomic data](invariants-threefolds.md#92f8f69bd1f8) |
| [Gr(4,5) / O(1)](grassmannians.md#gr45o1) | A4 | 3 | 4 | 4 | 1 | [Operator](grassmannians.md#gr45o1) · [Hodge and atomic data](invariants-threefolds.md#005416420233) |
| [P3  Fano index 4](projective.md#p3fanoindex4) | A3 | 3 | 4 | 4 | 1 | [Operator](projective.md#p3fanoindex4) · [Hodge and atomic data](invariants-threefolds.md#ebd198ca1849) |
| [Gr(2,4) / O(1)](grassmannians.md#gr24o1) | A3 | 3 | 3 | 4 | 1 | [Operator](grassmannians.md#gr24o1) · [Hodge and atomic data](invariants-threefolds.md#1841f3a70f74) |
| [Gr(4,5) / O(2)](grassmannians.md#gr45o2) | A4 | 3 | 3 | 4 | 1 | [Operator](grassmannians.md#gr45o2) · [Hodge and atomic data](invariants-threefolds.md#6ce465296672) |
| [P4 / O(2)](projective.md#p4o2) | A4 | 3 | 3 | 4 | 1 | [Operator](projective.md#p4o2) · [Hodge and atomic data](invariants-threefolds.md#6ceccace2e40) |
| [Fanography 2-32](fanography.md#fano-variety-2-32) | A2 | 3 | 2 | 6 | 2 | [Operator](fanography.md#fano-variety-2-32) · [Hodge and atomic data](invariants-threefolds.md#a6cb2e5a95bb) |
| [Fanography 3-27](fanography.md#fano-variety-3-27) | A1xA1xA1 | 3 | 2 | 8 | 3 | [Operator](fanography.md#fano-variety-3-27) · [Hodge and atomic data](invariants-threefolds.md#292efbd7ade0) |
| [Gr(2,4) / O(2)](grassmannians.md#gr24o2) | A3 | 3 | 2 | 4 | 1 | [Operator](grassmannians.md#gr24o2) · [Hodge and atomic data](invariants-threefolds.md#0156965bbcb0) |
| [Gr(2,5) / O(1)+O(1)+O(1)](grassmannians.md#gr25o1o1o1) | A4 | 3 | 2 | 4 | 1 | [Operator](grassmannians.md#gr25o1o1o1) · [Hodge and atomic data](invariants-threefolds.md#f443674348ad) |
| [Gr(3,5) / O(1)+O(1)+O(1)](grassmannians.md#gr35o1o1o1) | A4 | 3 | 2 | 4 | 1 | [Operator](grassmannians.md#gr35o1o1o1) · [Hodge and atomic data](invariants-threefolds.md#70aac1aaa08e) |
| [Gr(4,5) / O(3)](grassmannians.md#gr45o3) | A4 | 3 | 2 | 4 | 1 | [Operator](grassmannians.md#gr45o3) · [Hodge and atomic data](invariants-threefolds.md#a408b7769859) |
| [P4 / O(3)](projective.md#p4o3) | A4 | 3 | 2 | 4 | 1 | [Operator](projective.md#p4o3) · [Hodge and atomic data](invariants-threefolds.md#0743d9764a4a) |
| [P5 / O(2)+O(2)](projective.md#p5o2o2) | A5 | 3 | 2 | 4 | 1 | [Operator](projective.md#p5o2o2) · [Hodge and atomic data](invariants-threefolds.md#420c622c9cb3) |
| [B2/B / O(1,1)](additional.md#b2bo11) | B2 | 3 | 1 | 6 | 2 | [Operator](additional.md#b2bo11) · [Hodge and atomic data](invariants-threefolds.md#34fec398819e) |
| [Fanography 1-10](fanography.md#fano-variety-1-10) | A6 | 3 | 1 | 4 | 1 | [Operator](fanography.md#fano-variety-1-10) · [Hodge and atomic data](invariants-threefolds.md#7d708946a6fa) |
| [Fanography 1-6](fanography.md#fano-variety-1-6) | D5 | 3 | 1 | 4 | 1 | [Operator](fanography.md#fano-variety-1-6) · [Hodge and atomic data](invariants-threefolds.md#e3f3a551d928) |
| [Fanography 1-7](fanography.md#fano-variety-1-7) | A5 | 3 | 1 | 4 | 1 | [Operator](fanography.md#fano-variety-1-7) · [Hodge and atomic data](invariants-threefolds.md#541768cd0738) |
| [Fanography 1-8](fanography.md#fano-variety-1-8) | C3 | 3 | 1 | 4 | 1 | [Operator](fanography.md#fano-variety-1-8) · [Hodge and atomic data](invariants-threefolds.md#8f9e7a526fba) |
| [Fanography 1-9](fanography.md#fano-variety-1-9) | G2 | 3 | 1 | 4 | 1 | [Operator](fanography.md#fano-variety-1-9) · [Hodge and atomic data](invariants-threefolds.md#6f17aaf4290d) |
| [Fanography 2-24](fanography.md#fano-variety-2-24) | A2xA2 | 3 | 1 | 6 | 2 | [Operator](fanography.md#fano-variety-2-24) · [Hodge and atomic data](invariants-threefolds.md#3538d68c1866) |
| [Fanography 2-34](fanography.md#fano-variety-2-34) | A1xA2 | 3 | 1 | 6 | 2 | [Operator](fanography.md#fano-variety-2-34) · [Hodge and atomic data](invariants-threefolds.md#ea3e323d9fcb) |
| [Fanography 3-17](fanography.md#fano-variety-3-17) | A1xA1xA2 | 3 | 1 | 8 | 3 | [Operator](fanography.md#fano-variety-3-17) · [Hodge and atomic data](invariants-threefolds.md#a8e28f47c77f) |
| [Fanography 4-1](fanography.md#fano-variety-4-1) | A1xA1xA1xA1 | 3 | 1 | 10 | 4 | [Operator](fanography.md#fano-variety-4-1) · [Hodge and atomic data](invariants-threefolds.md#96d957608200) |
| [Fl(1,3,4) / O(1,1)+O(1,1)](additional.md#fl134o11o11) | A3 | 3 | 1 | 6 | 2 | [Operator](additional.md#fl134o11o11) · [Hodge and atomic data](invariants-threefolds.md#d3154e614ad6) |
| [Gr(2,4) / O(3)](grassmannians.md#gr24o3) | A3 | 3 | 1 | 4 | 1 | [Operator](grassmannians.md#gr24o3) · [Hodge and atomic data](invariants-threefolds.md#83c013d9bdf4) |
| [Gr(2,5) / O(1)+O(1)+O(2)](grassmannians.md#gr25o1o1o2) | A4 | 3 | 1 | 4 | 1 | [Operator](grassmannians.md#gr25o1o1o2) · [Hodge and atomic data](invariants-threefolds.md#4a1a8491be38) |
| [Gr(3,5) / O(1)+O(1)+O(2)](grassmannians.md#gr35o1o1o2) | A4 | 3 | 1 | 4 | 1 | [Operator](grassmannians.md#gr35o1o1o2) · [Hodge and atomic data](invariants-threefolds.md#d1339713ede4) |
| [Gr(4,5) / O(4)](grassmannians.md#gr45o4) | A4 | 3 | 1 | 4 | 1 | [Operator](grassmannians.md#gr45o4) · [Hodge and atomic data](invariants-threefolds.md#490a4dc43960) |
| [P4 / O(4)](projective.md#p4o4) | A4 | 3 | 1 | 4 | 1 | [Operator](projective.md#p4o4) · [Hodge and atomic data](invariants-threefolds.md#1c4486700490) |
| [P5 / O(2)+O(3)](projective.md#p5o2o3) | A5 | 3 | 1 | 4 | 1 | [Operator](projective.md#p5o2o3) · [Hodge and atomic data](invariants-threefolds.md#3834707b4d89) |
| [P6 / O(2)+O(2)+O(2)](projective.md#p6o2o2o2) | A6 | 3 | 1 | 4 | 1 | [Operator](projective.md#p6o2o2o2) · [Hodge and atomic data](invariants-threefolds.md#352c4508e307) |
| [Gr(3,4) / O(1)](grassmannians.md#gr34o1) | A3 | 2 | 3 | 3 | 1 | [Operator](grassmannians.md#gr34o1) · [Hodge and atomic data](invariants-surfaces.md#892655959f06) |
| [Gr(4,5) / O(1)+O(1)](grassmannians.md#gr45o1o1) | A4 | 2 | 3 | 3 | 1 | [Operator](grassmannians.md#gr45o1o1) · [Hodge and atomic data](invariants-surfaces.md#5bdf83aa585a) |
| [P2 Fano index 3](projective.md#p2fanoindex3) | A2 | 2 | 3 | 3 | 1 | [Operator](projective.md#p2fanoindex3) · [Hodge and atomic data](invariants-surfaces.md#7bea0424f8dd) |
| [Gr(2,4) / O(1)+O(1)](grassmannians.md#gr24o1o1) | A3 | 2 | 2 | 3 | 2 | [Operator](grassmannians.md#gr24o1o1) · [Hodge and atomic data](invariants-surfaces.md#1d67c54eac18) |
| [Gr(3,4) / O(2)](grassmannians.md#gr34o2) | A3 | 2 | 2 | 3 | 2 | [Operator](grassmannians.md#gr34o2) · [Hodge and atomic data](invariants-surfaces.md#53ee7c8af21e) |
| [Gr(4,5) / O(1)+O(2)](grassmannians.md#gr45o1o2) | A4 | 2 | 2 | 3 | 2 | [Operator](grassmannians.md#gr45o1o2) · [Hodge and atomic data](invariants-surfaces.md#04f8ea67b0d4) |
| [P3 / O(2)](projective.md#p3o2) | A3 | 2 | 2 | 3 | 2 | [Operator](projective.md#p3o2) · [Hodge and atomic data](invariants-surfaces.md#c26b71c1c385) |
| [Gr(2,4) / O(1)+O(2)](grassmannians.md#gr24o1o2) | A3 | 2 | 1 | 3 | 6 | [Operator](grassmannians.md#gr24o1o2) · [Hodge and atomic data](invariants-surfaces.md#c5377008d724) |
| [Gr(3,4) / O(3)](grassmannians.md#gr34o3) | A3 | 2 | 1 | 3 | 7 | [Operator](grassmannians.md#gr34o3) · [Hodge and atomic data](invariants-surfaces.md#1fe2cc704593) |
| [Gr(4,5) / O(1)+O(3)](grassmannians.md#gr45o1o3) | A4 | 2 | 1 | 3 | 7 | [Operator](grassmannians.md#gr45o1o3) · [Hodge and atomic data](invariants-surfaces.md#b1aa6f89ec3e) |
| [Gr(4,5) / O(2)+O(2)](grassmannians.md#gr45o2o2) | A4 | 2 | 1 | 3 | 6 | [Operator](grassmannians.md#gr45o2o2) · [Hodge and atomic data](invariants-surfaces.md#2dd604001dc5) |
| [P3 / O(3)](projective.md#p3o3) | A3 | 2 | 1 | 3 | 7 | [Operator](projective.md#p3o3) · [Hodge and atomic data](invariants-surfaces.md#785f6e8bcd76) |
| [P4 / O(2)+O(2)](projective.md#p4o2o2) | A4 | 2 | 1 | 3 | 6 | [Operator](projective.md#p4o2o2) · [Hodge and atomic data](invariants-surfaces.md#904c41fdd438) |
| [Gr(3,4) / O(1)+O(1)](grassmannians.md#gr34o1o1) | A3 | 1 | 2 | 2 | 1 | [Operator](grassmannians.md#gr34o1o1) · [Hodge and atomic data](invariants-points-curves.md#375785af1f22) |
| [Gr(4,5) / O(1)+O(1)+O(1)](grassmannians.md#gr45o1o1o1) | A4 | 1 | 2 | 2 | 1 | [Operator](grassmannians.md#gr45o1o1o1) · [Hodge and atomic data](invariants-points-curves.md#8156468b738f) |
| [Gr(2,4) / O(1)+O(1)+O(1)](grassmannians.md#gr24o1o1o1) | A3 | 1 | 1 | 2 | 1 | [Operator](grassmannians.md#gr24o1o1o1) · [Hodge and atomic data](invariants-points-curves.md#8b39618f3aed) |
| [Gr(3,4) / O(1)+O(2)](grassmannians.md#gr34o1o2) | A3 | 1 | 1 | 2 | 1 | [Operator](grassmannians.md#gr34o1o2) · [Hodge and atomic data](invariants-points-curves.md#79dd3601d09b) |
| [Gr(4,5) / O(1)+O(1)+O(2)](grassmannians.md#gr45o1o1o2) | A4 | 1 | 1 | 2 | 1 | [Operator](grassmannians.md#gr45o1o1o2) · [Hodge and atomic data](invariants-points-curves.md#af3a5033ba7a) |
| [P2 / O(2)](projective.md#p2o2) | A2 | 1 | 1 | 2 | 1 | [Operator](projective.md#p2o2) · [Hodge and atomic data](invariants-points-curves.md#81b66f277517) |
| [Gr(3,4) / O(1)+O(1)+O(1)](grassmannians.md#gr34o1o1o1) | A3 | 0 | 1 | 1 | 0 | [Operator](grassmannians.md#gr34o1o1o1) · [Hodge and atomic data](invariants-points-curves.md#c427c3fda1be) |
