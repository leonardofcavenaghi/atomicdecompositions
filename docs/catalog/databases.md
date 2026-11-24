---
title: "Fanography and algebraic-geometry databases"
description: "Overview of Fanography-type classification databases in algebraic geometry, Fano classification, and mirror symmetry, and how GEOATOMS connects to and complements them."
keywords: ["Fanography", "FanoBase", "type-a.fanobase.net", "ZL62", "Fanography-type databases", "algebraic geometry databases", "Fano classification", "Fano threefolds", "Fano fourfolds", "Grassmannian.info", "hyperkaehler.info", "superficie.info", "Mgnbar.info", "Hodge diamond cutter", "Graded Ring Database", "GRDB", "Fanosearch", "Periodic Table of Shapes", "polyDB", "polymake", "Kreuzer-Skarke", "CYTools", "LMFDB", "MathBases", "Iskovskikh", "Mori-Mukai", "CKP", "Coates Kasprzyk Prince", "HLM", "Hausen Laface Mauz", "regularized quantum period", "quantum cohomology", "atomic decompositions", "mirror symmetry"]
---

# Fanography and algebraic-geometry databases

Modern classification theory in algebraic geometry — from smooth Fano threefolds, smooth Fano fourfolds, and generalized Grassmannians to reflexive polytopes and toric complete intersections — increasingly relies on structured, online classification databases. Rather than leaving explicit constructions, numerical invariants, birational maps, and derived-category data dispersed across decades of papers, projects such as **Fanography**, **FanoBase**, **Grassmannian.info**, the **Graded Ring Database (GRDB)**, the **Fanosearch** quantum-period datasets, **polyDB**, and the **Kreuzer–Skarke** Calabi–Yau archive assemble them into searchable, cross-linked references.

GEOATOMS sits alongside these databases as a specialized **quantum-cohomological and Hodge-atomic companion** — and in the case of [**FanoBase**](https://type-a.fanobase.net/), its flag localization engine `gwflags` directly computes the database's quantum periods and flag-ambient quantum spectra. Where classification atlases index classical geometry, birational structure, polytopes, homogeneous zero-locus enumerations, and one-parameter quantum periods, GEOATOMS provides exact multi-parameter symbolic small quantum multiplication matrices \(A(\mathbf{y}) = c_1(TX)\star\), unit cyclic determinants \(\Delta_A(\mathbf{a})\), regularized-exponent multisets \(F_{\mathbf{a},\lambda}\) of the quantum connection, and coarse Hodge-atom invariants \((\rho_\alpha, P_\alpha(t))\), cross-referenced directly to Fanography, FanoBase, CKP, and HLM identifiers.

[Universal catalogue](index.md) · [Fano threefold reference](fanography.md) · [Sources and terminology](sources.md) · [Atomic invariants](atomic-invariants.md) · [Exact datasets](datasets.md)

## What distinguishes a Fanography-type database

In algebraic geometry, the informal label *Fanography-type database* refers to an interactive, invariant-indexed classification browser modeled on [Fanography](https://fanography.info/) and its sister sites. Five structural features distinguish these resources from static tables in research articles or raw data archives:

1. **Canonical family identifiers.** Every deformation family or combinatorial equivalence class carries a stable, human-readable label (for example, `r-n` in Fanography, `rho-c1^4-h0-letter` and `ZL62` presentation codes in FanoBase, Dynkin-type and node pairs in Grassmannian.info, or sequential database IDs in GRDB) that serves as a shared citation key across papers and software.
2. **Invariant-indexed geography.** Varieties can be browsed, plotted, or filtered by discrete numerical invariants — such as anticanonical degree \((-K_X)^3\), genus \(g\), Picard rank \(\rho\), intermediate-Jacobian dimension \(h^{1,2}\), Chern numbers \((c_1^2, c_2)\), Hilbert series, or period-sequence coefficients — exposing both populated regions and open gaps in geography.
3. **Explicit geometric realizations.** Entries record concrete constructions (complete intersections, zero loci of homogeneous vector bundles, projective bundles, weighted hypersurfaces, or lattice polytopes and fans), often listing multiple equivalent presentations of the same deformation family.
4. **Inter-object relations.** Objects are linked by geometric morphisms and equivalences: blow-ups and extremal contractions between Fano threefolds, Type I–IV projections and unprojections of \(\mathbb{Q}\)-Fano varieties, mutations of mirror Laurent polynomials, and projective or homological projective dualities.
5. **Per-property provenance and machine-readable exports.** Individual assertions carry direct literature citations, while underlying datasets are exposed as structured files, versioned archives (such as Zenodo DOIs), or programmatic APIs — an architecture exemplified more broadly in mathematics by the [LMFDB](https://www.lmfdb.org/).

## Directory of verified databases

The table below collects verified live databases and closely coupled computational companions spanning Fano classification, homogeneous spaces, mirror symmetry, lattice polytopes, and algebraic-geometry geography.

| Database | Maintainers / Project | Objects classified | Key invariants and data | Link |
|---|---|---|---|---|
| **Fanography** | Pieter Belmans | All 105 deformation families of smooth Fano 3-folds (Iskovskikh–Mori–Mukai) | \((-K_X)^3\), \(g\), \(\rho\), \(h^{1,2}\), Hodge diamond, polyvector parallelogram, blow-up/extremal-ray graph, rationality, \(\mathrm{Aut}^0(X)\), K-stability, semiorthogonal decompositions, coregularity, GRDB period links | [fanography.info](https://fanography.info/) |
| **FanoBase (type A)** | P. Belmans, V. Benedetti, F. Denisi, E. Fatighenti, J. Fernández Píriz, A. Frassineti, L. Manivel, F. Papa, F. Tanturri, F. Tufo | Smooth Fano 4-folds realized as strongly Fano zero loci of homogeneous bundles on products of type-\(A\) partial flag varieties (823 families, 919 presentations) | \(\rho\)–\(c_1^4\)–\(h^0\) family labels, `ZL62` presentation codes, Hodge and Chern numbers, Hochschild/polyvector parallelograms, primitive Hilbert series, regularized quantum periods (652 distinct, 58 new) and flag-ambient quantum spectra computed via `gwflags` | [fanobase.net](https://fanobase.net/) · [type-a.fanobase.net](https://type-a.fanobase.net/) |
| **Grassmannian.info** | Pieter Belmans | Generalized Grassmannians and rational homogeneous spaces \(G/P\) (classical and exceptional types) | Dimension, Fano index, Betti numbers, \(\mathrm{Aut}^0(G/P)\), minimal embeddings, Hilbert series, projective duality, exceptional collections, homological projective duality, small/big quantum semisimplicity, \(k\)-Fanoness | [grassmannian.info](https://grassmannian.info/) |
| **hyperkaehler.info** | Pieter Belmans | Known deformation types of compact irreducible holomorphic symplectic (hyperkähler) manifolds | Deformation-invariant topology and geometry of the two infinite families and two sporadic types, Betti/Hodge data, bibliographic references | [hyperkaehler.info](https://hyperkaehler.info/) |
| **le superficie algebriche** | Pieter Belmans | Minimal complex smooth algebraic surfaces (Enriques–Kodaira geography) | Chern numbers \((c_1^2, c_2)\), Kodaira dimension, Hodge diamond, Betti numbers, geometric genus \(p_g\), irregularity \(q\), Euler characteristic | [superficie.info](https://superficie.info/) |
| **Mgnbar.info** | Ignacio Barros, Pieter Belmans | Moduli spaces of pointed curves \(\overline{\mathrm{M}}_{g,n}\) and \(\mathrm{M}_{g,n}\) | Kodaira dimension, tautological generation of the Chow ring, polynomiality of finite-field point counts, per-cell citations | [mgnbar.info](https://mgnbar.info/) |
| **Hodge diamond cutter** | Pieter Belmans | Computational companion for smooth projective varieties (flag varieties, complete intersections, blow-ups) | Python/Sage computation and display of Hodge diamonds \(h^{p,q}(X)\), Lefschetz decompositions, and Euler numbers | [cutter.ncag.info](https://cutter.ncag.info/) |
| **Graded Ring Database (GRDB)** | Gavin Brown, Alexander M. Kasprzyk (with Miles Reid et al.) | Polarized varieties and graded rings: \(\mathbb{Q}\)-Fano 3-folds, K3 surfaces, toric Fano varieties, CY 3-folds, Fano/CY 4-fold hypersurfaces | Anticanonical Hilbert series, weights, singularity baskets, projections/unprojections, smooth/canonical/terminal toric Fano lists, 3D Minkowski and 4D quantum period search | [grdb.co.uk](https://www.grdb.co.uk/) |
| **Fanosearch quantum period archives** | Tom Coates, Alessio Corti, Sergey Galkin, Vasily Golyshev, Alexander M. Kasprzyk, Thomas Prince et al. | Regularized quantum periods of smooth Fano manifolds in dimensions 1–4 ("Periodic Table of Shapes") | Regularized quantum period sequences \(\widehat{G}_X(t)\), candidate Picard–Fuchs differential operators, Minkowski Laurent polynomials, cross-classification names (CC0 Zenodo records & GRDB search) | [GRDB 3D](https://www.grdb.co.uk/forms/period3) · [GRDB 4D](https://www.grdb.co.uk/forms/smoothfano4) · [Zenodo 4D](https://doi.org/10.5281/zenodo.5708307) |
| **polyDB** | Andreas Paffenholz and the `polymake` team | Discrete geometric objects: smooth reflexive and reflexive lattice polytopes, combinatorial polytopes, matroids, tropical objects | `SmoothReflexive` (smooth toric Fano varieties up to dimension 8), `Reflexive`, Ehrhart data, web interface, REST API, `polymake`/OSCAR/Python/Julia bindings | [db.polymake.org](https://db.polymake.org/) |
| **Calabi–Yau data (Kreuzer–Skarke)** | Maximilian Kreuzer, Harald Skarke (TU Wien) | Reflexive 3- and 4-polytopes (\(473{,}800{,}776\) reflexive 4-polytopes), Calabi–Yau hypersurfaces, reflexive Gorenstein cones | Vertex/point counts, Hodge pairs \((h^{1,1}, h^{1,2})\), Euler numbers, weight systems, `PALP` lattice-polytope software | [hep.itp.tuwien.ac.at/~kreuzer/CY](https://hep.itp.tuwien.ac.at/~kreuzer/CY/) |
| **CYTools** | Mehmet Demirtas, Andres Rios-Tascon, Liam McAllister | Python computational interface to the Kreuzer–Skarke database and toric Calabi–Yau hypersurfaces | Fine regular star triangulations, toric fans, Mori and Kähler cones, intersection numbers, Hodge data, Gopakumar–Vafa invariants | [cy.tools](https://cy.tools/) |
| **LMFDB** | LMFDB Collaboration | L-functions, modular forms, elliptic curves, genus-2 curves, abelian varieties, number fields, Galois representations | Benchmark cross-linked mathematical database architecture: canonical labels, contextual definitions ("knowls"), explicit provenance, invariant queries | [lmfdb.org](https://www.lmfdb.org/) |
| **MathBases** | MathBases community | Meta-directory of mathematical databases across algebraic geometry, number theory, combinatorics, and topology | Structured metadata index (scope, maintainers, access formats, schemas) cataloging Fanography, GRDB, hyperkaehler.info, Kreuzer–Skarke, LMFDB, and others | [mathbases.org](https://mathbases.org/) |

## Families of algebraic-geometry databases

### Interactive geometric atlases: Fanography, FanoBase, Grassmannian.info, and sister sites

[Fanography](https://fanography.info/) is the canonical visual atlas of the **105 deformation families of smooth Fano threefolds** established by Iskovskikh and Mori–Mukai. Families are indexed as `r-n`, where \(r = \rho(X) = b_2(X) = h^{1,1}(X) \in \{1,\ldots,10\}\) is the Picard rank (17 families with \(\rho = 1\), 36 with \(\rho = 2\), 31 with \(\rho = 3\), 13 with \(\rho = 4\), 3 with \(\rho = 5\), and one family \(\mathbb{P}^1 \times S_{10-\rho}\) for each \(\rho \in \{6,7,8,9,10\}\)). Each family page aggregates classical numerical invariants — anticanonical degree \((-K_X)^3\), genus \(g = h^0(X,-K_X) - 2 = \tfrac{1}{2}(-K_X)^3 + 1\), Fano index, \(h^{1,2}(X)\), full Hodge diamond, and polyvector parallelogram — alongside deformation data (\(\dim\mathrm{Aut}^0(X)\), moduli counts), birational geometry (rationality, unirationality, stable rationality, primitivity, and the directed graph of blow-ups and extremal contractions), homogeneous zero-locus descriptions, semiorthogonal decompositions, K-stability status, coregularity, Futaki invariants, generic semisimplicity of quantum cohomology, and direct links to regularized quantum periods in GRDB.

[**FanoBase**](https://fanobase.net/) ([type-\(A\) catalogue](https://type-a.fanobase.net/), [project blog](https://blog.fanobase.net/posts/fanobase-beta/)) brings the Fanography paradigm to **dimension four**. Developed by Pieter Belmans, Vladimiro Benedetti, Francesco Denisi, Enrico Fatighenti, Javier Fernández Píriz, Alessandro Frassineti, Laurent Manivel, Federico Papa, Fabio Tanturri, and Federico Tufo — building on the earlier database of Bernardara, Fatighenti, Manivel, and Tanturri ([`arXiv:2111.13030`](https://arxiv.org/abs/2111.13030)) — its initial type-\(A\) beta release catalogues **smooth Fano fourfolds realized as zero loci of globally generated, completely reducible homogeneous vector bundles** \(\mathcal{E}\) on products of type-\(A\) partial flag varieties \(Y\) satisfying the *strongly Fano* condition (\(\omega_Y^\vee \otimes (\det\mathcal{E})^\vee\) ample on \(Y\)). Distilling over \(2{,}000\) constructions under systematic equivalence rules, the beta release organizes **919 representative zero-locus presentations** (indexed by compact, case-sensitive `ZL62` labels `<ambient>.<bundle>`) into **823 clusters** with family labels `rho-c1^4-h0-letter`, spanning **197 distinct Hodge diamonds**, Picard ranks up to \(\rho = 8\), and **652 distinct regularized quantum periods** (including **58 new period sequences** beyond previously published lists). Sheaf cohomology and Chern invariants are computed via [`HomogeneousTools` / `PartialFlagVarieties.jl`](https://github.com/HomogeneousTools/PartialFlagVarieties.jl) and OSCAR's `IntersectionTheory`, while the regularized quantum periods and flag-ambient quantum spectra on [type-a.fanobase.net](https://type-a.fanobase.net/) are computed directly with GEOATOMS's [`gwflags`](../software/flags-1.1.0.md) localization engine. Future FanoBase releases aim to incorporate general Lie types, classical and orbital degeneracy loci, and a navigable birational network of Fano fourfolds.

[Grassmannian.info](https://grassmannian.info/) extends the same design to **rational homogeneous varieties** \(G/P\) — a "periodic table of generalized Grassmannians" covering classical and exceptional Dynkin types, the Freudenthal magic square, the Vogel plane, and horospherical varieties. Alongside basic invariants (dimension, Fano index, Betti numbers, \(\mathrm{Aut}^0(G/P)\), minimal projective embeddings, and Hilbert series), individual entries document projective duality, full exceptional collections in \(\mathbf{D}^{\mathrm{b}}(G/P)\), Lefschetz collections and homological projective duals, \(k\)-Fanoness, and known results on small and big quantum cohomology semisimplicity together with eigenvalue multiplicities of \(c_1(G/P)\star\).

Three closely related interactive browsers complete this cluster: [hyperkaehler.info](https://hyperkaehler.info/) catalogs deformation invariants of the known compact hyperkähler families; [le superficie algebriche](https://superficie.info/) plots the Enriques–Kodaira geography of minimal smooth complex surfaces in the \((c_1^2, c_2)\)-plane; and [Mgnbar.info](https://mgnbar.info/) charts the Kodaira dimension, tautological Chow generation, and finite-field point-count polynomiality of \(\overline{\mathrm{M}}_{g,n}\) and \(\mathrm{M}_{g,n}\). Their computational companion, the [Hodge diamond cutter](https://cutter.ncag.info/), computes Hodge diamonds for flag varieties, complete intersections, and blow-ups.

### Graded rings and mirror-symmetry period databases: GRDB and Fanosearch

The [Graded Ring Database (GRDB)](https://www.grdb.co.uk/), built by Gavin Brown and Alexander Kasprzyk with foundational input from Miles Reid and collaborators, organizes algebraic varieties through their polarized graded rings \(R(X, A) = \bigoplus_{m \ge 0} H^0(X, mA)\). Its search tables span polarized and elliptic [K3 surfaces](https://www.grdb.co.uk/forms/k3), [\(\mathbb{Q}\)-Fano 3-folds with terminal quotient singularities](https://www.grdb.co.uk/forms/fano3) (indexed by Hilbert series, weights, singularity baskets, Kawamata and Bogomolov numbers, and Type I–IV projections and unprojections), [terminal](https://www.grdb.co.uk/forms/toricf3t) and [canonical](https://www.grdb.co.uk/forms/toricf3c) toric Fano 3-folds, [smooth toric Fano varieties up to dimension 6](https://www.grdb.co.uk/forms/toricsmooth) (from Øbro's algorithm, [`arXiv:0704.0049`](https://arxiv.org/abs/0704.0049)), Calabi–Yau 3-fold hypersurfaces and orbifolds, and quasismooth Fano and Calabi–Yau 4-fold weighted hypersurfaces.

Closely integrated with GRDB is the **Fanosearch** programme ("Periodic Table of Shapes", Coates–Corti–Galkin–Golyshev–Kasprzyk–Prince et al.; [`arXiv:1212.1722`](https://arxiv.org/abs/1212.1722), [`arXiv:1212.1785`](https://arxiv.org/abs/1212.1785), [`arXiv:1303.3288`](https://arxiv.org/abs/1303.3288)), which approaches Fano classification via mirror symmetry. To a smooth Fano manifold \(X\) one associates its **regularized quantum period**,

$$
\widehat{G}_X(t) = 1 + \sum_{d \ge 2} c_d\, t^d,
$$

a power series encoding descendant one-point genus-zero Gromov–Witten invariants of anticanonical degree \(d\), together with an annihilating Picard–Fuchs differential operator \(L\) and mirror Laurent polynomials (Minkowski polynomials up to mutation equivalence). The complete databases in dimensions 1, 2, and 3 and the expanding database in dimension 4 are published under a public-domain (CC0) license on Zenodo alongside Coates–Kasprzyk ([`arXiv:2112.00632`](https://arxiv.org/abs/2112.00632)):

- Dimension 1: [`doi:10.5281/zenodo.5708188`](https://doi.org/10.5281/zenodo.5708188)
- Dimension 2 (del Pezzo surfaces): [`doi:10.5281/zenodo.5708232`](https://doi.org/10.5281/zenodo.5708232)
- Dimension 3 (all 105 smooth Fano threefolds): [`doi:10.5281/zenodo.5708272`](https://doi.org/10.5281/zenodo.5708272)
- Dimension 4 (known four-dimensional Fano manifolds, including CKP toric complete intersections): [`doi:10.5281/zenodo.5708307`](https://doi.org/10.5281/zenodo.5708307)

Interactive search interfaces for these period sequences are hosted directly on GRDB as [3d Minkowski period sequences](https://www.grdb.co.uk/forms/period3) and [4-dimensional quantum periods](https://www.grdb.co.uk/forms/smoothfano4).

### Polytope, toric, and Calabi–Yau repositories: polyDB, Kreuzer–Skarke, and CYTools

Toric geometry and mirror symmetry link smooth Fano and Calabi–Yau classifications to finite combinatorial lists of lattice polytopes:

- [**polyDB**](https://db.polymake.org/) (Andreas Paffenholz and the [`polymake`](https://polymake.org/) team; [`arXiv:1711.02936`](https://arxiv.org/abs/1711.02936)) is a software-independent repository for discrete geometric objects with a web interface, REST API, and bindings for `polymake`, OSCAR, Python, and Julia. Its `LatticePolytopes` namespace includes the `SmoothReflexive` collection — cataloging smooth reflexive lattice polytopes (hence smooth toric Fano varieties) up to dimension 8 — as well as reflexive polytopes, combinatorial polytopes, matroids, and tropical objects.
- [**Calabi–Yau data (Kreuzer–Skarke)**](https://hep.itp.tuwien.ac.at/~kreuzer/CY/) (Maximilian Kreuzer and Harald Skarke; [`arXiv:hep-th/0002240`](https://arxiv.org/abs/hep-th/0002240), [`arXiv:math/0001106`](https://arxiv.org/abs/math/0001106)) hosts the complete classification of all \(473{,}800{,}776\) reflexive 4-polytopes and their associated Batyrev Calabi–Yau threefold hypersurfaces (yielding \(30{,}108\) distinct Hodge pairs \((h^{1,1}, h^{1,2})\)), together with reflexive 3-polytopes, reflexive Gorenstein cones, and the lattice-polytope package `PALP`.
- [**CYTools**](https://cy.tools/) (Demirtas–Rios-Tascon–McAllister; [`arXiv:2211.03823`](https://arxiv.org/abs/2211.03823)) provides a modern Python environment built to parse the Kreuzer–Skarke list at scale, compute fine regular star triangulations, construct the associated smooth toric ambient fans, and extract Mori/Kähler cones, intersection numbers, and Calabi–Yau invariants.

### Broader mathematical database models: LMFDB and MathBases

Outside Fano geometry, the [L-functions and Modular Forms Database (LMFDB)](https://www.lmfdb.org/) established the prevailing design template for collaborative mathematical databases: permanent object labels, explicit bidirectional links connecting distinct mathematical objects, contextual inline definitions, and machine-verifiable provenance. Across disciplines, [MathBases](https://mathbases.org/) maintains an open catalog indexing Fanography, hyperkaehler.info, GRDB, Kreuzer–Skarke, LMFDB, and related mathematical datasets by mathematical subject, maintainers, and access format.

## How GEOATOMS fits into the ecosystem

Existing Fano and homogeneous-space databases focus primarily on **classical geometry, birational classification, polytope combinatorics, derived-category decompositions, and one-parameter regularized quantum periods**. GEOATOMS complements them by computing and archiving the **multi-parameter small quantum cohomology operator on ambient cohomology, its spectral and quantum-connection invariants, and its coarse Hodge-atom decomposition**.

| Mathematical layer | Fanography / FanoBase / Grassmannian.info | GRDB / Fanosearch / polyDB | GEOATOMS |
|---|---|---|---|
| **Classification scope** | All 105 smooth Fano 3-folds; 823 type-\(A\) homogeneous Fano 4-fold families (919 presentations); rational homogeneous spaces \(G/P\) | \(\mathbb{Q}\)-Fano 3-folds, K3s, smooth/reflexive toric Fanos, 1D–4D quantum periods | 364 catalogue records in dimensions 0–8 (flag, homogeneous, projective-bundle, and toric complete intersections) |
| **Classical & birational invariants** | \((-K_X)^d\), \(h^0(-K_X)\), \(\rho\), Hodge/Chern numbers, Hochschild/polyvector parallelograms, blow-ups, rationality, K-stability | Hilbert series, weights, baskets, projections/unprojections, polytope Ehrhart data | Full Hodge diamonds, Chern numbers, explicit fan/divisor or root-system/bundle realizations |
| **Mirror-symmetry / Gromov–Witten data** | Semisimplicity status, eigenvalue counts for \(G/P\), GRDB period links, and (in FanoBase) 652 regularized quantum periods & flag-ambient spectra via `gwflags` | Regularized quantum period \(\widehat{G}_X(t)\), Picard–Fuchs operators, Minkowski Laurent polynomials | Exact symbolic operator \(A(\mathbf{y}) = [c_1(TX)\star(-)]_{\mathrm{amb}}\), grading \(G\), reproducible localization inputs |
| **Spectral & atomic invariants** | Semiorthogonal decompositions, naive atom dimensions, HPD duals | — | Characteristic factors \(\chi_{A(\mathbf{a})}(z)\), unit cyclic determinant \(\Delta_A(\mathbf{a})\), regularized-exponent multisets \(F_{\mathbf{a},\lambda}\), coarse Hodge-atom invariants \((\rho_\alpha, P_\alpha(t))\) |

Concretely, for a smooth projective variety \(X\) of dimension \(d\) realized in a flag or toric ambient space \(\iota: X \hookrightarrow Y\) with ambient cohomology sector \(V = H^*_{\mathrm{amb}}(X,\mathbb{Q}) = \operatorname{im}(\iota^*)\) and ordered homogeneous basis \((e_1,\ldots,e_N)\), GEOATOMS records four coupled layers of exact data (see [notation](notation.md) and [atomic invariants](atomic-invariants.md)):

**Exact small quantum multiplication operator and grading.** The symbolic matrix in the Novikov coordinates \(\mathbf{y}\) and its centered codimension grading,

$$
A(\mathbf{y}) = \left[\operatorname{pr}_{V}\circ\bigl(c_1(TX)\star(-)\bigr)\big|_{V}\right],
\qquad
G = \operatorname{diag}\left(\operatorname{codim}_{\mathbb{C}}(e_i) - \frac{d}{2}\right),
$$

together with exact localization inputs (root systems, kept roots, and defining bundles for flag models; primitive rays, maximal cones, defining divisor rows `K`, and Novikov divisor maps for toric models).

**Factorized spectrum and unit cyclic determinant.** At a stated parameter point \(\mathbf{a}\), the monic square-free factorization \(\chi_{A(\mathbf{a})}(z) = \prod_i p_i(z)^{m_i}\) and the **unit cyclic determinant**

$$
\Delta_A(\mathbf{a}) = \det\bigl[\mathbf{1}, A(\mathbf{a})\mathbf{1}, \ldots, A(\mathbf{a})^{N-1}\mathbf{1}\bigr],
$$

whose nonvanishing proves that quantum powers of the unit \(\mathbf{1}\) span \(V\).

**Quantum-connection regularized-exponent multisets.** For each spectral factor and eigenvalue \(\lambda\), the multiset \(F_{\mathbf{a},\lambda}\) of residue classes \(-\theta + \mathbb{Z} \in \mathbb{Q}/\mathbb{Z}\) of the regular-singular connection factor at \(\lambda\), retaining multiplicities.

**Coarse Hodge-atom invariants.** Under explicit cohomological, cyclicity, and primitive-assignment hypotheses, the rational Hodge-invariant rank \(\rho_\alpha = \dim_{\mathbb{C}}\bigl((E^\alpha_{\mathbb{C}})^{\mathrm{Hod}_{\mathbb{C}}}\bigr)\) and Hodge-cocharacter polynomial

$$
P_\alpha(t) = \sum_{p,q} h^{p,q}(E^\alpha)\, t^{p-q}
$$

for each coarse atom \(\alpha\).

While the regularized quantum period \(\widehat{G}_X(t)\) in Fanosearch/GRDB projects the genus-zero theory onto the one-parameter anticanonical direction, the symbolic matrix \(A(\mathbf{y})\) retains all ambient Novikov variables \(\mathbf{y}\), the full action of \(c_1(TX)\star\) on \(H^*_{\mathrm{amb}}(X,\mathbb{Q})\), and the Jordan/connection structure needed to separate and certify coarse Hodge atoms.

## Navigating between identifiers across databases

GEOATOMS cross-references major classification numbering schemes alongside geometric construction names. Each scheme carries its own conventions and scope caveats.

### FanoBase family and `ZL62` labels and GEOATOMS fourfolds

In [FanoBase (`type-a.fanobase.net`)](https://type-a.fanobase.net/), two complementary identifiers distinguish deformation clusters from explicit ambient realizations ([explained guide](https://type-a.fanobase.net/explained)):

- **Family labels (`rho-c1^4-h0-letter`).** Record the Picard rank \(\rho(X)\), anticanonical degree \(c_1(X)^4 = (-K_X)^4\), and anticanonical section count \(h^0(X, \omega_X^\vee)\), followed by a letter separating families with matching triple (for example, `5-120-31-a` denotes \(\rho = 5\), \(c_1^4 = 120\), \(h^0(\omega_X^\vee) = 31\), and `1-20-10-a` has \(\rho = 1\), \(c_1^4 = 20\), \(h^0(\omega_X^\vee) = 10\)).
- **`ZL62` presentation labels.** Each zero-locus presentation \(X = Z(Y, \mathcal{E})\) in a product of type-\(A\) partial flag varieties carries a case-sensitive `ZL62` string `<ambient>.<bundle>` (for instance, `40` encodes \(\mathbb{P}^4\) with zero bundle), with an interactive encoder/decoder on [type-a.fanobase.net/explained/zl62](https://type-a.fanobase.net/explained/zl62).

Because FanoBase computes its [quantum periods](https://type-a.fanobase.net/quantum) and flag-ambient quantum spectra using `gwflags`, every type-\(A\) zero-locus presentation in FanoBase translates directly into a `gwflags` input (`FlagVariety` with simple or product type-\(A\) root system, kept roots, and homogeneous bundle summands). Conversely, GEOATOMS's [Fourfolds](fourfolds.md) catalogue complements FanoBase by archiving multi-variable symbolic Novikov operators \(A(\mathbf{y})\), regularized quantum-connection exponent multisets \(F_{\mathbf{a},\lambda}\), unit cyclic determinants \(\Delta_A(\mathbf{a})\), certified atomic Hodge polynomials, non-type-\(A\) homogeneous fourfolds (such as sections of \(\operatorname{LG}(3,6)\), \(G_2/P_2\), and the spinor tenfold), and toric complete-intersection fourfolds (`CKP` and `HLM`).

### Fanography `r-n`, GRDB periods, and GEOATOMS threefolds

A Fanography identifier `r-n` specifies Picard rank \(r = \rho(X)\) and Iskovskikh / Mori–Mukai family index \(n\). All 105 families are listed in [Fano threefold reference](fanography.md), where **81 of the 105 families** carry exact computed ambient operators and spectral/connection tables — 20 flag-variety and homogeneous-bundle realizations (`gwflags`) and 62 positive smooth toric and toric complete-intersection presentations (`gwtoric`, stored in [`toric-threefolds.json`](../data/toric-threefolds.json), with family `2-32` realized in both models and 12 flag entries independently cross-verified symbolically in `gwtoric`) — while the remaining 24 are listed as catalog-only reference entries.

- **Example (`1-2`, quartic threefold in \(\mathbb{P}^4\)).** On [Fanography 1-2](https://fanography.info/1-2/), one finds \((-K_X)^3 = 4\), \(h^{1,2} = 30\), K-stability, the semiorthogonal decomposition \(\langle \operatorname{Ku}(X), \mathcal{O}_X \rangle\), and the link to GRDB 3D period `#165`. In GEOATOMS ([fanography.md#fano-variety-1-2](fanography.md#fano-variety-1-2) and [invariants-threefolds.md](invariants-threefolds.md#1c4486700490)), one finds the exact \(4\times 4\) ambient operator \(A(\mathbf{y})\), characteristic factorization \((z - 232)(z + 24)^3\) at \(y_1 = 1\), unit cyclic determinant \(\Delta_A(1) = 1\), regularized-exponent multisets \(\{\!\{0\}\!\}\) and \(\{\!\{0, \tfrac{1}{4}, \tfrac{3}{4}\}\!\}\), and the atomic Hodge invariants.
- **Example (`2-32`, flag threefold \(\operatorname{Fl}(1,2;\mathbb{C}^3)\)).** On [Fanography 2-32](https://fanography.info/2-32/), one inspects its blow-up relations (to `3-7`, `3-13`, `3-16`, `3-20`, `3-24`), generic semisimplicity, and GRDB period `#24`. In GEOATOMS ([fanography.md#fano-variety-2-32](fanography.md#fano-variety-2-32)), one accesses its \(6\times 6\) small quantum multiplication matrix, irreducible sextic characteristic polynomial at \((y_1, y_2) = (2, 3)\), and nonzero cyclic determinant \(\Delta_A = 119{,}439{,}360\).

### CKP period buckets, GRDB 4D periods, and GEOATOMS fourfolds

The prefix **CKP** refers to Coates–Kasprzyk–Prince, *Four-dimensional Fano toric complete intersections* ([`arXiv:1409.5030`](https://arxiv.org/abs/1409.5030)), which constructed smooth four-dimensional Fano complete intersections of codimension at most 4 in smooth toric Fano varieties and distinguished 738 regularized quantum period sequences (at least 527 yielding new Fano fourfolds). Their period sequences can be queried on GRDB's [4-dimensional quantum periods](https://www.grdb.co.uk/forms/smoothfano4) page and downloaded from [`doi:10.5281/zenodo.5708307`](https://doi.org/10.5281/zenodo.5708307).

In GEOATOMS, [Fourfolds](fourfolds.md) includes 94 CKP-tagged toric complete-intersection presentations (stored in [`toric-fourfolds.json`](../data/toric-fourfolds.json)), such as the complete intersection of multidegrees \((1,1), (1,1)\) in \(\mathbb{P}^3 \times \mathbb{P}^3\) ([`CKP-189`](records/ckp-189.md)), with explicit fans, defining divisors, symbolic operators, and Hodge/atomic data.

**Caveat on period buckets.** CKP numbers index **period buckets**, not proven isomorphism classes. Equality of regularized quantum periods \(\widehat{G}_X(t) = \widehat{G}_{X'}(t)\) is a necessary condition for deformation equivalence, not a sufficient one: distinct presentations or non-isomorphic varieties can share a period sequence. GEOATOMS therefore always identifies examples primarily by their explicit geometric construction and keeps distinct presentations separate, each retaining its own curve coordinates, Novikov divisors, and ordered cohomology basis (see [sources and terminology](sources.md)).

### HLM fourfold cases and GEOATOMS fourfolds

The prefix **HLM** refers to Hausen–Laface–Mauz, *On smooth Fano fourfolds of Picard number two* ([`arXiv:1907.08000`](https://arxiv.org/abs/1907.08000)), classifying smooth Fano fourfolds of Picard rank two with a general hypersurface Cox ring. GEOATOMS records explicit HLM constructions — including the Verra fourfold ([`HLM-29`](records/hlm-29.md), a section of \(\mathbb{P}_{\mathbb{P}^2}(\mathcal{O}\oplus\mathcal{O}(1)^{\oplus 3})\) by \(2\xi\)) and [`HLM-27`](records/hlm-27.md) — alongside their fans, Hodge diamonds, and exact quantum operators.

**Caveats on presentations and ambient sectors.** Two technical conventions should be kept in mind when translating between external classifications and GEOATOMS:

- **Toric and projective-bundle conventions.** Split projective bundles \(\mathbb{P}_B(E)\) in GEOATOMS use the **quotient convention**, and identifying an ambient toric variety from a fan requires an invertible integral lattice change matching all rays and all maximal cones, not merely ray counts or primitive relations ([geometric identification](sources.md#geometric-identification)).
- **Ambient vs. full cohomology.** Localization computes \(A(\mathbf{y})\) on the ambient image \(V = H^*_{\mathrm{amb}}(X,\mathbb{Q})\) and sums over target curve classes sharing the same ambient pushforward \(\iota_*\beta' = \beta\). When cross-checking GEOATOMS spectra against full Hodge diamonds or semiorthogonal decompositions on Fanography or Grassmannian.info, primitive cohomology and the genericity and cyclicity hypotheses stated in [atomic invariants](atomic-invariants.md) must be accounted for separately.

## References

- M. Akhtar, T. Coates, S. Galkin, A. M. Kasprzyk, *Minkowski polynomials and mutations*, SIGMA **8** (2012), 094, [`arXiv:1212.1785`](https://arxiv.org/abs/1212.1785).
- P. Belmans, V. Benedetti, F. Denisi, E. Fatighenti, J. Fernández Píriz, A. Frassineti, L. Manivel, F. Papa, F. Tanturri, F. Tufo, *Fano fourfolds in type A (FanoBase)*, [type-a.fanobase.net](https://type-a.fanobase.net/) and [blog.fanobase.net](https://blog.fanobase.net/posts/fanobase-beta/).
- V. Benedetti, J. Guéré, L. Manivel, N. Perrin, *Quantum cohomology and birational geometry of Verra fourfolds*, [`arXiv:2605.30450`](https://arxiv.org/abs/2605.30450).
- V. Benedetti, L. Manivel, N. Perrin, *Quantum cohomology and irrationality of Gushel–Mukai fourfolds*, [`arXiv:2603.17487`](https://arxiv.org/abs/2603.17487).
- M. Bernardara, E. Fatighenti, L. Manivel, F. Tanturri, *Fano fourfolds of K3 type*, [`arXiv:2111.13030`](https://arxiv.org/abs/2111.13030).
- T. Coates, A. Corti, S. Galkin, V. Golyshev, A. M. Kasprzyk, *Mirror symmetry and Fano manifolds*, European Congress of Mathematics, Eur. Math. Soc. (2013), 285–300, [`arXiv:1212.1722`](https://arxiv.org/abs/1212.1722).
- T. Coates, A. Corti, S. Galkin, A. M. Kasprzyk, *Quantum periods for 3-dimensional Fano manifolds*, Geom. Topol. **20** (2016), 103–256, [`arXiv:1303.3288`](https://arxiv.org/abs/1303.3288).
- T. Coates, A. M. Kasprzyk, *Databases of quantum periods for Fano manifolds*, Scientific Data **9** (2022), 163, [`arXiv:2112.00632`](https://arxiv.org/abs/2112.00632).
- T. Coates, A. M. Kasprzyk, T. Prince, *Four-dimensional Fano toric complete intersections*, Proc. R. Soc. A **471** (2015), 20140704, [`arXiv:1409.5030`](https://arxiv.org/abs/1409.5030).
- M. Demirtas, A. Rios-Tascon, L. McAllister, *CYTools: A software package for analyzing Calabi–Yau manifolds*, [`arXiv:2211.03823`](https://arxiv.org/abs/2211.03823).
- J. Hausen, A. Laface, C. Mauz, *On smooth Fano fourfolds of Picard number two*, Rev. Mat. Iberoam. **38** (2022), 53–93, [`arXiv:1907.08000`](https://arxiv.org/abs/1907.08000).
- M. Kreuzer, H. Skarke, *Complete classification of reflexive polyhedra in four dimensions*, Adv. Theor. Math. Phys. **4** (2000), 1209–1230, [`arXiv:hep-th/0002240`](https://arxiv.org/abs/hep-th/0002240).
- M. Øbro, *An algorithm for the classification of smooth Fano polytopes*, [`arXiv:0704.0049`](https://arxiv.org/abs/0704.0049).
- A. Paffenholz, *polyDB: A database for polytopes and related objects*, [`arXiv:1711.02936`](https://arxiv.org/abs/1711.02936).
