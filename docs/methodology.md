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


The twisted localization calculation of Theorem 3.28 computes


$$
\sum_{\substack{\beta'\in\mathrm{NE}(X)\\\iota_*\beta'=\beta}}
\langle\gamma_1,\ldots,\gamma_m\rangle^X_{0,\beta'}.
$$


It should be called an individual curve-class invariant only when the relevant identification of curve classes is justified. Different target classes with the same ambient image contribute to the same Novikov monomial.

## The decorated-tree formula

For nonzero effective degree, Theorems 3.26 and 3.28 sum over decorated trees \(\Gamma=(\mathcal T,\ell,\mathbf d,\mathrm{mk})\). Here \(\mathcal T\) is the underlying tree, with vertex set \(V(\Gamma)\) and edge set \(E(\Gamma)\). Vertices carry fixed-point labels \(w_v\in W^F\), edges carry invariant curves and covering degrees \(d_e>0\), and \(\mathrm{mk}\) assigns the markings to vertices. With the factors defined in those statements, the complete-intersection contribution is


$$
\sum_\Gamma
\frac{
 \displaystyle\prod_{v\in V(\Gamma)}e_{w_v}^{\operatorname{val}(v)-1}
 \prod_{e\in E(\Gamma)}\Omega_e\prod_{v\in V(\Gamma)}I_v\,
 \operatorname{Tw}(\Gamma)
 \prod_{k=1}^{m}\sigma_{u_k}|_{p_{w_{\mathrm{mk}(k)}}}
}{|\operatorname{Aut}\Gamma|\displaystyle\prod_{e\in E(\Gamma)}d_e}.
$$


Here \(e_w=e_T(T_{p_w}F)\), \(\Omega_e\) is the edge factor, and \(\operatorname{Tw}(\Gamma)\) is the Euler twist of Proposition 3.27; omit this twist for the ambient target itself. The flags' root and bundle conventions determine these weights.

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

## Quantum multiplication and grading

For a homogeneous basis \((T_i)\) of the full cohomology of \(X\), let \(g_{ab}=\int_X T_a\smile T_b\), with inverse \((g^{ab})\). The small quantum product is

$$
T_i\star T_j
=\sum_{a,b}\left(\sum_{\beta\in\mathrm{NE}(X)}
\langle T_i,T_j,T_a\rangle^X_{0,\beta}\,q^\beta\right)g^{ab}T_b.
$$

The degree-zero term is cup product. The inverse pairing is part of the product; three-point invariants alone are not its matrix coefficients.

For the returned ambient sector \(V\), let \((e_1,\ldots,e_N)\) be the ordered homogeneous basis and \(d=\dim X\). The Novikov coordinates are \(\mathbf y\), and the displayed matrix is \(A(\mathbf y)\), the ambient projection of \(c_1(TX)\star(-)\). The symbol \(\star\) denotes the small quantum product. Its entries and grading satisfy

$$
A(\mathbf y)e_j=\sum_{i=1}^{N}A_{ij}(\mathbf y)e_i,
\qquad
G=\operatorname{diag}\left(\operatorname{codim}(e_i)-\frac d2\right).
$$

Thus columns are images of basis vectors, and the grading uses complex codimension. The matrix size \(N\) is the dimension of the computed space, not automatically the full cohomology dimension.

At the stated parameter assignment \(\mathbf a\), write \(A(\mathbf a)=A(\mathbf y)|_{\mathbf y=\mathbf a}\). The characteristic polynomial is

$$
\chi_{A(\mathbf a)}(z)=\det(zI_N-A(\mathbf a))
=\prod_jp_j(z)^{m_j},
$$

where the \(p_j\) are monic, pairwise coprime, square-free factors. Each root \(\lambda\) of \(p_j\) is an eigenvalue of \(A(\mathbf a)\) with algebraic multiplicity \(m_j\). Let \(\mathbf 1\) be the coordinate column of the unit in the returned basis. The unit cyclic determinant is

$$
\Delta_A(\mathbf a)
=\det\bigl[\mathbf 1,A(\mathbf a)\mathbf 1,\ldots,
A(\mathbf a)^{N-1}\mathbf 1\bigr].
$$

Its nonvanishing proves that the quantum powers of the unit span \(V\). Its vanishing at a particular assignment does not imply vanishing at every point.

## Regularized-exponent multisets

With auxiliary coordinate \(u\), the small-locus quantum connection has convention

$$
\nabla_{\partial_u}=\partial_u-\frac{A(\mathbf y)}{u^2}+\frac{G}{u}.
$$

For an eigenvalue \(\lambda\) at \(\mathbf a\), a formal factor of unramified exponential type has the form

$$
M_{\mathbf a,\lambda}\simeq\mathcal E^{\lambda/u}\otimes R_{\mathbf a,\lambda},
$$

without a substitution by fractional powers of \(u\). Here \(\mathcal E^{\lambda/u}\) denotes the rank-one connection \(\partial_u-\lambda/u^2\), and \(R_{\mathbf a,\lambda}\) is regular singular. If its residue eigenvalues \(\theta\) are rational, the regularized-exponent multiset is

$$
F_{\mathbf a,\lambda}
=\{\!\{-\theta+\mathbb Z:
\theta\text{ is a residue eigenvalue of }R_{\mathbf a,\lambda}\}\!\}.
$$

Each class in \(\mathbb Q/\mathbb Z\) is counted with its algebraic multiplicity. In particular, \(\{\!\{0,\tfrac12,\tfrac12\}\!\}\) has three entries. The reported powers \(s=-\theta\) give these classes modulo \(\mathbb Z\), usually represented in \([0,1)\). Neither multiset is a termwise pairing of independently sorted lists.

A condition \(p_j(\lambda)=0\) refers to an eigenvalue of \(A(\mathbf a)\). A row grouping several roots applies separately at each indicated root and at that analysis point. The grading diagonal alone is not the residue spectrum of the formal factors.

## Hodge data and atomic invariants

The rational Hodge-invariant subspace is

$$
H^*_{\mathrm{Hod}}(X)
=\bigoplus_p\bigl(H^{2p}(X,\mathbb Q)\cap H^{p,p}(X)\bigr).
$$

Ambient classes lie in this space, but primitive cohomology can contain additional rational Hodge classes. Equality of the ambient sector with \(H^*_{\mathrm{Hod}}(X)\), a complete curve calculation and the geometric persistence hypotheses are required to interpret ambient cyclicity as the generic Hodge-factor criterion. A finite numerical specialization is not by itself an admissibility or persistence argument.

Let \(E^\alpha\) be a coarse Hodge atom and \(E^\alpha_{\mathbb C}=E^\alpha\otimes_{\mathbb Q}\mathbb C\). The Hodge group \(\mathrm{Hod}\) is the kernel of the Mumford–Tate group's character on \(\mathbb Q(1)\). Its invariant space and Hodge-cocharacter weight spaces define

$$
\rho_\alpha=\dim_{\mathbb C}
\bigl(E^\alpha_{\mathbb C}\bigr)^{\mathrm{Hod}_{\mathbb C}},
\qquad
P_\alpha(t)=\sum_k\dim_{\mathbb C}
\bigl(E^\alpha_{\mathbb C}\bigr)^k t^k.
$$

A Hodge type \((p,q)\) has cocharacter weight \(p-q\). Hence the full Hodge polynomial is \(P_X(t)=\sum_{p,q}h^{p,q}(X)t^{p-q}\), with nonnegative dimensions and no alternating signs for odd cohomology. The constant coefficient of \(P_\alpha\) can exceed \(\rho_\alpha\); \(P_\alpha(1)\) is its full rank. Full atomic polynomials require the geometric assignment of cohomology beyond the ambient sector. See the [catalogue notation key](catalog/notation.md) and [atomic invariants](catalog/atomic-invariants.md) for the definitions and their use in examples.

## Sources and reproducibility

References: B. Alexeev et al., [*On the atomic decomposition of complete intersection in flag varieties*](https://arxiv.org/abs/2609.21914), Theorems 3.26 and 3.28 and Definitions 4.5–4.6. Virtual localization follows Graber–Pandharipande, [*Localization of virtual classes*](https://arxiv.org/abs/alg-geom/9708001). 

The [exact datasets](catalog/datasets.md) provide coefficients, curve coordinates, ordered bases and grading. See [software input/output formats](software/input-output.md) and [validation scope](software/launch-plan.md).


The verification procedures compare exact matrix contracts, mathematical regression identities and documented inputs. Fresh matrix calculations use the localization routines and retain their complete curve list, basis, grading and parameter map.
