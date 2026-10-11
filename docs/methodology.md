---
description: Virtual localization, ambient quantum multiplication, curve degrees and verification conventions used by gwflags.
---

# Methods and conventions

`gwflags` computes genus-zero Gromov–Witten invariants and small quantum
multiplication by the first Chern class. For a flag variety \(F=G/P\), it
uses Schubert classes. For a complete intersection \(Y\subset F\), the
returned matrix describes the **flag-ambient sector**: the cohomology classes
obtained by restriction from \(F\).

## Quantum multiplication

Let \(\{\phi_i\}\) be a cohomology basis and \(\{\phi^i\}\) its dual
for the Poincaré pairing. The small quantum product is
\[
\alpha\star\delta
=\sum_{\beta,i}q^\beta
\langle\alpha,\delta,\phi_i\rangle_{0,3,\beta}\,\phi^i.
\]
The degree-zero term is the cup product. In a general basis, forming its
matrix requires the inverse pairing as well as the three-point invariants.
The software specializes to \(\alpha=c_1(TY)\).

Matrix columns are inputs and rows are outputs. The returned grading is
diagonal, with entries \(\operatorname{codim}(\phi_i)-\dim(Y)/2\).
Catalog matrices use all Novikov variables \(y_i=1\) unless explicitly
labelled symbolic. The [download](catalog/computed.md) preserves both forms
and the ordered basis.

## Virtual localization

The torus action on \(G/P\) induces an action on the moduli space of stable
maps. Its genus-zero fixed loci are indexed by decorated trees: vertices map
to torus-fixed points and edges cover invariant curves. The software sums
their contributions using the virtual-localization formula of Graber and
Pandharipande, [Localization of virtual classes](https://arxiv.org/abs/alg-geom/9708001).

Calculations use exact rational arithmetic. The default implementation
evaluates the localization sum at two rational torus points and compares the
results; the symbolic path is also available. Agreement is a consistency check,
not an independent proof of every formula in the implementation.

## Complete intersections and the ambient sector

For a bundle \(E\) on \(F\), the supported Euler-twisted calculation
requires nonnegative splitting degrees along the relevant invariant curves.
A standard geometric interpretation assumes a globally generated bundle and a
regular section with smooth zero locus \(Y\). Then
\[
\dim Y=\dim F-\operatorname{rank}E,\qquad
c_1(TY)=\bigl(c_1(TF)-c_1(E)\bigr)|_Y.
\]

The software forms the classical twisted pairing
\[
g_{ij}=\int_F\sigma_i\sigma_j e(E)
\]
and selects a nondegenerate submatrix to obtain its ambient basis. Primitive
cohomology is not supplied by this reduction. Identifying the output with the
full quantum-cohomology operator requires the corresponding homology and
ambient-completeness hypotheses.

Fixed-point weights alone do not determine the curve restrictions of an
arbitrary non-split bundle. Quotient constructions must come from a genuine
geometric quotient with supported restriction data; weight containment is a
consistency check rather than a proof of a bundle embedding.

<span id="4a-coordinate-contract-used-by-the-software"></span>

## Curve degrees and index

For positive degree and \(n\) primary insertions, the dimension axiom is
\[
\sum_i\operatorname{codim}(\alpha_i)
=\dim Y+\langle c_1(TY),\beta\rangle+n-3.
\]
For multiplication by \(c_1\), it bounds contributing degrees by
\(\langle c_1(TY),\beta\rangle\leq\dim Y+1\). This gives a finite
automatic list when every enumerated curve generator has positive Chern
pairing. A zero direction in an otherwise nonzero Chern vector is not bounded
by this inequality. Such cases, and negative pairings, require explicit curve
lists unless a supported constructor supplies effective generators with a
positive bound. If the entire Chern class vanishes, its multiplication
operator is zero.

The catalog’s **Ambient Index** is the gcd of the Chern pairings in the
specified ambient curve lattice (or a constructor’s effective generators).
It agrees with the geometric Fano index when the relevant integral-lattice
identification holds. A smooth conic illustrates the distinction: it is
\(\mathbb P^1\), with geometric index 2, while its ambient Chern gcd in
\(\mathbb P^2\) is 1. This gcd does not define a geometric Fano index for a
point. The software and JSON retain the field name `fano_index`.

The [Python API](api-reference.md) specifies kept-root coordinates, basis
indices and the degree-zero classical-pairing shortcut. The
[user guide](how-to-use.md) gives copyable inputs.

## Verification

The test suite checks known enumerative values, including the line through
two points of \(\mathbb P^2\), 27 lines on a cubic surface and 2875 lines on
a quintic threefold. Catalog checks compare saved matrices with their inputs,
bases, gradings, degree constraints and characteristic polynomials. Displayed
spectra are checked numerically, while projective Hodge diamonds are checked
by exact Riemann–Roch and Lefschetz calculations.

These checks are reproducible in the repository:

```bash
python -m pip install -r requirements-test.txt
python -m pytest tests/ -q
python scripts/validate_localization_results.py
python scripts/validate_catalog_math.py
```

Checking saved outputs does not rerun all localization sums or prove every
geometric realization in the reference catalog. To reproduce a matrix, use
its input with the [software](how-to-use.md); **Catalog only** entries have no
supported computed matrix.
