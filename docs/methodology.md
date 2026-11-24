---
description: Gromov–Witten invariants and quantum multiplication for flag varieties, computed by equivariant localization.
---

# Localization on flag varieties

Root systems describe the ambient flag variety, its Schubert classes and effective curves. Euler-twisted virtual localization supplies the invariants of a supported smooth complete intersection and its ambient quantum operator.

## The flag variety and its inputs

Let \(F=\mathcal G/P\), with \(T\subset B\subset P\), simple roots \(\Pi=\{\alpha_1,\ldots,\alpha_r\}\), and positive roots \(R^+\). Set


$$
\Pi_F=\Pi\setminus\Pi_P,\qquad R_F^+=R^+\setminus R_P^+,
\qquad \dim F=|R_F^+|.
$$


The minimal representatives \(W^F\) of \(W/W_P\) index the Schubert basis \(\sigma_w\), with \(\operatorname{codim}\sigma_w=\ell(w)\). The software's **kept roots** are \(\Pi_F\), entered as **one-based** ambient Dynkin-node numbers. Schubert basis indices are different from these node numbers.

Curve coordinates use the reduced coroot lattice. A compact beta vector follows the declared kept-root order; the equivalent ambient vector has zeros on removed nodes. Line-bundle rows of `K` have one coefficient per kept root. Supported homogeneous bundle expressions use the fiber-weight and curve-restriction constructions described in the [bundle API](api-reference.md); fixed-point weight containment alone does not prove a geometric quotient-bundle construction.

## Complete intersections and pushed curve classes

Let \(X=Z(F,E)\) be the smooth zero locus of a regular section of a globally generated homogeneous bundle, with inclusion \(\iota:X\hookrightarrow F\). Then


$$
\dim X=\dim F-\operatorname{rk}E,\qquad
\widehat c_1(TX)=c_1(TF)-c_1(E),\qquad
c_1(TX)=\iota^*\widehat c_1(TX).
$$


The hat matters: an ambient curve class \(\beta\) pairs with \(\widehat c_1(TX)\), whereas a class \(\beta'\) on \(X\) pairs with \(c_1(TX)\). Their pairings agree when \(\iota_*\beta'=\beta\).

For primary insertions \(\gamma_k=\iota^*\sigma_{u_k}\), the dimensional condition is


$$
\sum_{k=1}^{m}\ell(u_k)
=\dim X+\int_\beta\widehat c_1(TX)+m-3.
$$


The Euler-twisted virtual localization formula for complete intersections in \(F\) evaluates the pushed-forward sum


$$
\sum_{\substack{\beta'\in\mathrm{NE}(X)\\\iota_*\beta'=\beta}}
\langle\gamma_1,\ldots,\gamma_m\rangle^X_{0,\beta'}.
$$


It should be called an individual curve-class invariant only when the relevant identification of curve classes is justified. Different target classes with the same ambient image contribute to the same Novikov monomial.

## The decorated-tree formula

For nonzero effective degree \(\beta\), torus-fixed loci in \(\overline{\mathcal M}_{0,m}(F,\beta)\) are indexed by decorated trees \(\Gamma=(\mathcal T,\ell,\mathbf d,\mathrm{mk})\). Here \(\mathcal T\) is the underlying tree, with vertex set \(V(\Gamma)\) and edge set \(E(\Gamma)\). Vertices carry fixed-point labels \(w_v\in W^F\), edges carry invariant curves and covering degrees \(d_e>0\), and \(\mathrm{mk}\) assigns the markings to vertices. The twisted localization contribution is


$$
\sum_\Gamma
\frac{
 \displaystyle\prod_{v\in V(\Gamma)}e_{w_v}^{\operatorname{val}(v)-1}
 \prod_{e\in E(\Gamma)}\Omega_e\prod_{v\in V(\Gamma)}I_v\,
 \operatorname{Tw}(\Gamma)
 \prod_{k=1}^{m}\sigma_{u_k}|_{p_{w_{\mathrm{mk}(k)}}}
}{|\operatorname{Aut}\Gamma|\displaystyle\prod_{e\in E(\Gamma)}d_e}.
$$


Here \(e_w=e_T(T_{p_w}F)\) is the fixed-point tangent Euler class, \(\Omega_e\) is the invariant-curve edge factor, and \(\operatorname{Tw}(\Gamma)\) is the Euler twist of the bundle \(E\) on the decorated tree (omitted when computing on the ambient flag variety \(F\) itself). The root and bundle conventions determine these weights.

The number \(\operatorname{val}(v)\) counts incident edges, and \(\omega_{v,e}\) is the tangent weight on the covering source at that endpoint: the corresponding target tangent weight divided by \(d_e\). Put \(n_v=\operatorname{val}(v)+|\mathrm{mk}^{-1}(v)|\). For \(n_v\ge3\),


$$
I_v=\left(\prod_{e\ni v}\omega_{v,e}^{-1}\right)
\left(\sum_{e\ni v}\omega_{v,e}^{-1}\right)^{n_v-3}.
$$


For the unstable vertex conventions, \(I_v=\Theta_v\): one edge and no markings contributes \(\omega_{v,e}\), one edge and one marking contributes \(1\), and two edges with no markings contribute \((\omega_{v,e_1}+\omega_{v,e_2})^{-1}\). These are the formula's vertex factors, not instructions to add marked insertions.

In particular, the cubic-surface line count is **27 with zero insertions**. The software's empty list `[]` expresses this unmarked invariant. The degree-zero API's classical cup-integral shortcut, including unstable pairing inputs, is a separate implementation convention and is not a definition of unstable degree-zero stable-map invariants.

## The flag-ambient operator

Set


$$
V=H^*_{\mathrm{amb}}(X)=\operatorname{im}\bigl(H^*(F,\mathbb Q)\to H^*(X,\mathbb Q)\bigr),
\qquad
A(\mathbf y)=\operatorname{pr}_{V}\circ\bigl(c_1(TX)\star_{\mathrm{small}}(-)\bigr)
\big|_{H^*_{\mathrm{amb}}(X)}.
$$


The map \(\operatorname{pr}_{V}\) is the projection onto the ambient sector determined by its nondegenerate restricted pairing. That pairing is \(g_{ij}=\int_F\sigma_i\sigma_j e(E)\). The software chooses a nondegenerate reduced ambient basis. In the reduced ambient basis,


$$
A(\mathbf y)\sigma_i=\sum_{\beta\in\mathrm{NE}(F)}\sum_{j,k}
\left(\sum_{\iota_*\beta'=\beta}
\langle c_1(TX),\sigma_i,\sigma_j\rangle^X_{0,\beta'}\right)
q^\beta g^{jk}\sigma_k.
$$


An ambient projection need not be the full quantum operator. Primitive cohomology is not supplied by reducing the ambient pairing, and identifying the result with the Hodge-invariant sector requires the ambient/Hodge comparison and persistence hypotheses described below.

## Novikov names and finite enumeration

The formal monomial is \(q^\beta\), written in the coordinates \(\mathbf y\) using the recorded curve-to-parameter map. The software names these coordinates `y1`, `y2`, and so on; these are Novikov names, distinct from additive coordinates for big quantum cohomology. In the default flag convention, type A retains kept-node labels and other families use consecutive kept-root names. Explicit `ambient` and `compact` conventions are documented in the [notation guide](software/notation.md).

<span id="4a-coordinate-contract-used-by-the-software"></span>

The dimension axiom bounds degrees contributing to multiplication by \(c_1\) by \(\int_\beta\widehat c_1(TX)\le\dim X+1\). A finite automatic search additionally requires positive bounds on the supported effective generators. Zero or negative directions cannot be cut off solely by that inequality. Preserve the actual curve list with the result.

The recorded ambient Chern gcd is not automatically the intrinsic Fano index; for instance a conic has ambient gcd 1 in \(\mathbb P^2\), but intrinsic index 2. For a point this gcd does not define a geometric Fano index.

## Quantum connection, spectra and atomic invariants

On the returned homogeneous basis \((e_1,\ldots,e_N)\) of \(V\), the ambient first-Chern operator \(A(\mathbf y)\) and grading \(G=\operatorname{diag}\bigl(\operatorname{codim}(e_i)-d/2\bigr)\) (columns as images of basis vectors) determine the small-locus quantum connection

$$
\nabla_{\partial_u}=\partial_u-\frac{A(\mathbf y)}{u^2}+\frac{G}{u}.
$$

At a stated Novikov assignment \(\mathbf a\), the characteristic polynomial \(\chi_{A(\mathbf a)}(z)=\det(zI_N-A(\mathbf a))=\prod_j p_j(z)^{m_j}\), unit cyclic determinant \(\Delta_A(\mathbf a)=\det[\mathbf 1,A(\mathbf a)\mathbf 1,\ldots,A(\mathbf a)^{N-1}\mathbf 1]\), and regularized-exponent multisets \(F_{\mathbf a,\lambda}\) (classes \(-\theta+\mathbb Z\) of regular-singular residue eigenvalues \(\theta\)) are defined uniformly across the catalogue in the [catalogue notation key](catalog/notation.md).

Interpreting ambient spectral factors as coarse Hodge atoms—with rational Hodge-invariant count \(\rho_\alpha=\dim_{\mathbb C}\bigl((E^\alpha_{\mathbb C})^{\mathrm{Hod}_{\mathbb C}}\bigr)\) and Hodge polynomial \(P_\alpha(t)=\sum_{p,q}h^{p,q}(E^\alpha)t^{p-q}\)—requires identifying \(V\) with \(H^*_{\mathrm{Hod}}(X)=\bigoplus_p(H^{2p}(X,\mathbb Q)\cap H^{p,p}(X))\), a complete curve list, and the geometric persistence and primitive-assignment hypotheses documented in [atomic invariants](catalog/atomic-invariants.md).

<span id="verification"></span>

## Sources and reproducibility

References: B. Alexeev et al., [*On the atomic decomposition of complete intersection in flag varieties*](https://arxiv.org/abs/2609.21914) (decorated-tree twisted localization and spectral/atomic framework), and T. Graber and R. Pandharipande, [*Localization of virtual classes*](https://arxiv.org/abs/alg-geom/9708001).

The [exact datasets](catalog/datasets.md) provide coefficients, curve coordinates, ordered bases and grading. See [software input/output formats](software/input-output.md) and [validation scope](software/launch-plan.md).

The verification procedures compare exact matrix contracts, mathematical regression identities and documented inputs. Fresh matrix calculations use the localization routines and retain their complete curve list, basis, grading and parameter map.
