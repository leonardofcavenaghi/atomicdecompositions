---
title: Toric methods and conventions
description: Fan, divisor, curve and Novikov conventions for toric virtual localization, ambient quantum multiplication and Hodge calculations.
---

# Toric methods and conventions

Let \(Y=X_\Sigma\) be a supported smooth projective toric variety. The rays \(v_\rho\in N\) and maximal cones of \(\Sigma\) determine the target. The order of the rays is part of the input: each cone contains **zero-based indices** into that list.

## Divisors and complete intersections

Write \(D_\rho\) for the invariant divisors. Over the rationals, the Chow ring is the polynomial ring in these classes modulo the linear relations \(\sum_\rho\langle m,v_\rho\rangle D_\rho=0\) and Stanley–Reisner monomials for sets of rays not lying in a cone.

A defining row of `K` represents a divisor \(L_a=\sum_\rho k_{a\rho}D_\rho\); a full row has one coefficient per ray. Short rows instead use the **displayed cohomology divisor basis**. These are different from the chosen Novikov divisor coordinates. Negative coefficients in a full row do not by themselves imply non-nefness: degrees on invariant curves determine the supported nefness check.

For a regular section of \(E=\bigoplus_a L_a\), assume the zero locus \(X\subset Y\) is smooth and the supported Euler-twisted localization hypotheses hold. Then
\[
\dim X=\dim Y-\operatorname{rank}E,\qquad
c_1(TX)=\left(\sum_\rho D_\rho-\sum_a L_a\right)|_X.
\]
The interface rejects trivial and non-nef defining summands. A software check of restriction degrees does not certify smoothness of a chosen section.

## Curves and Novikov variables

A curve is represented by an integral relation \(\beta=(b_\rho)\) satisfying \(\sum_\rho b_\rho v_\rho=0\). The API also accepts coordinates in its reported integral `h2_basis`. Keep the basis and ray order with the calculation. Effective relations may have negative entries.

The chosen `novikov_divisors` \(H_j\) define
\[
y^\beta=\prod_j y_j^{\langle H_j,\beta\rangle}.
\]
Names `y1,y2,...` follow that ordered list, not raw ray indices. A fallback without a nef integral basis may produce Laurent monomials. Do not reorder variables from a saved catalogue independently of the basis.

## Virtual localization and primary invariants

As in the [flag calculation](../methodology.md), fixed stable maps are indexed by decorated trees. Vertices correspond to fixed points (maximal cones), edges to invariant curves with positive covering degrees, and markings carry evaluation insertions. Tangent weights come from the fan; defining divisors supply the Euler twist.

The software uses exact rational arithmetic and the virtual-localization formula of Graber and Pandharipande, [Localization of virtual classes](https://arxiv.org/abs/alg-geom/9708001). Auxiliary torus evaluations cancel in the final invariant. Independent evaluations provide a consistency check when enabled; they are not a proof of every implementation formula. New fivefold queue records explicitly used **one** exact evaluation per curve class, while older cached records may have two-point validation.

For primary insertions,
\[
\sum_i\operatorname{codim}\alpha_i=\dim X+\langle c_1(TX),\beta\rangle+n-3.
\]
An empty insertion list means \(n=0\). In particular, a cubic surface in \(\mathbb P^3\) has **27 unmarked degree-one maps**; no point insertion is used. In Python: `projective_space(3).gw([], beta=(1,1,1,1), K=[[3]])`.

## Quantum multiplication and ambient reduction

The small product is
\[
\alpha\star\delta=\sum_{\beta,i}y^\beta
\langle\alpha,\delta,\phi_i\rangle_{0,3,\beta}\,\phi^i,
\]
where the dual basis uses the inverse pairing. The complete-intersection pairing is \(g_{ij}=\int_Y\phi_i\phi_j\prod_a L_a\). Selecting a nondegenerate ambient subspace removes its radical; it does not add primitive cohomology.

The returned operator is multiplication by \(c_1(TX)\) on the reported **toric-ambient sector**. Columns are images of basis vectors: \(Me_j=\sum_iM_{ij}e_i\). Basis entries are divisor-polynomial names; flag API entries instead use Schubert indices. The grading is \(\mathrm{Gr}_{ii}=\operatorname{codim}e_i-\dim X/2\).

## Automatic curve enumeration

The dimension axiom bounds contributing degrees by \(\langle c_1(TX),\beta\rangle\leq\dim X+1\). This is a finite bound only with appropriate positivity and effective-cone information. The result distinguishes positive ambient bounds, conditional Mori searches, suggested inequalities and ample-degree cutoffs. Retain its curve list and completeness mode. A cutoff is exact on its chosen region; a sampled inequality check does not prove a Mori cone.

## Spectra, connections and Hodge data

Matrices in this toric collection remain symbolic until the displayed `eval_y` is applied. Unspecified spectrum variables default to one in the software. Saved spectra of \(M\) and connection factors of \(K^F=-M\) have opposite sign conventions; each record states which operator is used. Connection exponents are recorded per factor and per eigenvalue, with multiplicity. Unresolved or noncyclic factors remain explicit.

Fan cohomology gives ambient toric Hodge data. Full complete-intersection Hodge support in the software requires dimensions 3–5 and its implemented positivity certificates; some nef fourfolds instead use attributed literature Hodge numbers. Full Hodge data and ambient quantum matrices have different scopes. Middle \(H^5\) is odd in the fivefold examples and is absent from these even-sector matrices. The automatic irrationality criterion is restricted to dimensions 2–4; the fivefold catalogue assigns no rationality verdict.

## Reproducibility and sources

Each catalogue entry includes the exact input and sparse symbolic matrix, ordered basis and grading. Published data are transcribed from completed saved records. Validation of those records does not rerun the localization sums. The software guides give [Python, CLI and interface syntax](../software/input-output.md).

Fourfold sources: Coates–Kasprzyk–Prince, [Four-dimensional Fano toric complete intersections](https://arxiv.org/abs/1409.5030v3), and Hausen–Laface–Mauz, [On smooth Fano fourfolds of Picard number two](https://arxiv.org/abs/1907.08000v3). Fivefold construction sources and computational caveats accompany their catalogue.
