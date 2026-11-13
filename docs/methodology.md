---
description: Gromov–Witten invariants and quantum multiplication for flag varieties, computed by equivariant localization.
---

# Localization on flag varieties

Root systems describe the ambient flag variety, its Schubert classes and effective curves. Euler-twisted virtual localization supplies the invariants of a supported smooth complete intersection and its ambient quantum operator.

## The flag variety and its inputs

Let \(F=G/P\), with \(T\subset B\subset P\), simple roots \(\Pi\), and positive roots \(R^+\). Set


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

For nonzero effective degree, Theorems 3.26 and 3.28 sum over decorated trees \(\Gamma=(G,\ell,d,\mathrm{mk})\). Vertices carry fixed-point labels \(w_v\in W^F\), edges carry invariant curves and covering degrees \(d_e>0\), and \(\mathrm{mk}\) assigns the markings to vertices. With the factors defined in those statements, the complete-intersection contribution is


$$
\sum_\Gamma
\frac{
 \displaystyle\prod_{v\in V}e_{w_v}^{\operatorname{val}(v)-1}
 \prod_{e\in E}\Omega_e\prod_{v\in V}I_v\,
 \operatorname{Tw}(\Gamma)
 \prod_{k=1}^{m}\sigma_{u_k}|_{p_{w_{\mathrm{mk}(k)}}}
}{|\operatorname{Aut}\Gamma|\displaystyle\prod_{e\in E}d_e}.
$$


Here \(e_w=e_T(T_{p_w}F)\), \(\Omega_e\) is the edge factor, and \(\operatorname{Tw}(\Gamma)\) is the Euler twist of Proposition 3.27; omit this twist for the ambient target itself. The flags' root and bundle conventions determine these weights.

Put \(n_v=\operatorname{val}(v)+|\mathrm{mk}^{-1}(v)|\). For \(n_v\ge3\),


$$
I_v=\left(\prod_{e\ni v}\omega_{v,e}^{-1}\right)
\left(\sum_{e\ni v}\omega_{v,e}^{-1}\right)^{n_v-3}.
$$


For the unstable vertex conventions, \(I_v=\Theta_v\): one edge and no markings contributes \(\omega_{v,e}\), one edge and one marking contributes \(1\), and two edges with no markings contribute \((\omega_{v,e_1}+\omega_{v,e_2})^{-1}\). These are the formula's vertex factors, not instructions to add marked insertions.

In particular, the cubic-surface line count is **27 with zero insertions**. The software's empty list `[]` expresses this unmarked invariant. The degree-zero API's classical cup-integral shortcut, including unstable pairing inputs, is a separate implementation convention and is not a definition of unstable degree-zero stable-map invariants.

## The flag-ambient operator

Set


$$
H^*_{\mathrm{amb}}(X)=\operatorname{im}\bigl(H^*(F,\mathbb Q)\to H^*(X,\mathbb Q)\bigr),
\qquad
A(q)=\operatorname{pr}_F\circ\bigl(c_1(TX)\star_{\mathrm{small}}(-)\bigr)
\big|_{H^*_{\mathrm{amb}}(X)}.
$$


The restricted pairing is \(g_{ij}=\int_F\sigma_i\sigma_j e(E)\). The software chooses a nondegenerate reduced ambient basis. In the reduced ambient basis,


$$
A(q)\sigma_i=\sum_{\beta\in\mathrm{NE}(F)}\sum_{j,k}
\left(\sum_{\iota_*\beta'=\beta}
\langle c_1(TX),\sigma_i,\sigma_j\rangle^X_{0,\beta'}\right)
q^\beta g^{jk}\sigma_k.
$$


An ambient projection need not be the full quantum operator. Primitive cohomology is not supplied by reducing the ambient pairing, and identifying the result with the Hodge-invariant sector requires the ambient/Hodge comparison and persistence hypotheses described below.

## Novikov names and finite enumeration

The theoretical variable is \(q^\beta\). The software writes its monomials using the displayed `y` variables; these are Novikov names, distinct from additive coordinates for big quantum cohomology. In the default flag convention, type A retains kept-node labels and other families use consecutive kept-root names. Explicit `ambient` and `compact` conventions are documented in the [notation guide](software/notation.md).

<span id="4a-coordinate-contract-used-by-the-software"></span>

The dimension axiom bounds degrees contributing to multiplication by \(c_1\) by \(\int_\beta\widehat c_1(TX)\le\dim X+1\). A finite automatic search additionally requires positive bounds on the supported effective generators. Zero or negative directions cannot be cut off solely by that inequality. Preserve the actual curve list with the result.

The recorded ambient Chern gcd is not automatically the intrinsic Fano index; for instance a conic has ambient gcd 1 in \(\mathbb P^2\), but intrinsic index 2. For a point this gcd does not define a geometric Fano index.

## Quantum multiplication, grading and the connection

Choose a homogeneous basis \(\{T_i\}\), the Poincaré pairing
\(g_{ab}=\int_Z T_a\smile T_b\), and its inverse \((g^{ab})\). In this notation,


$$
T_i\star_{\mathrm{small}}T_j
=\sum_{a,b}\left(\sum_{\beta\in\mathrm{NE}(Z)}
\langle T_i,T_j,T_a\rangle^Z_{0,\beta}\,q^\beta\right)g^{ab}T_b.
$$


Here \(Z\) denotes the target of this full-cohomology formula. The zero-class term is cup product. A matrix requires the inverse pairing, not merely a table of three-point invariants. A three-point genus-zero bracket has three insertions; subscripts indicating the number of markings and the genus are distinguished by context.

The matrix returned by the software is denoted **\(A(q)\)**. It represents the ambient projection of multiplication by the first Chern class. Columns are images of basis vectors. In a homogeneous basis the grading matrix is \(G=[\mathrm{Gr}]\), with


$$
\mathrm{Gr}|_{H^a(Z)}=\frac{a-\dim Z}{2}\,\mathrm{id},\qquad
G_{ii}=\operatorname{codim}(T_i)-\frac{\dim Z}{2}.
$$


When the computed sector is identified with the Hodge-invariant module under the required geometric hypotheses, the small-locus connection has the convention


$$
\nabla_{\partial_u}=\partial_u-\frac{A(q)}{u^2}+\frac{G}{u}.
$$


The connection analysis uses \(K^F=-A(q)\), so the same connection is \(\partial_u+K^F/u^2+G/u\). A characteristic factor \(p(z)\) of \(K^F\) corresponds to eigenvalues \(\lambda\) of \(A\) satisfying **\(p(-\lambda)=0\)**. This sign change must accompany the eigenvalue labels; the grading is unchanged.

## Regularized-exponent multisets

Write a supported formal factor as


$$
M_{b,\alpha}\simeq\mathcal E^{\lambda(b)/u}\otimes R_{b,\lambda}.
$$


Here \(\lambda(b)\) is an eigenvalue of \(\kappa_b=\mathrm{Eu}\star_b(-)\); on the small locus the Euler class is \(c_1(TZ)\). If \(R_{b,\lambda}\) is regular singular with rational residue eigenvalues, its regularized-exponent multiset is


$$
F_{b,\lambda}
=\{\!\{-\theta+\mathbb Z:\theta\text{ is a residue eigenvalue of }R_{b,\lambda}\}\!\}.
$$


Every occurrence is retained with its algebraic multiplicity. Thus \(\{\!\{0,\tfrac12,\tfrac12\}\!\}\) has three entries; it must not be simplified to a two-element set. The software's admissible powers \(s=-\theta\) give these classes modulo \(\mathbb Z\). The powers and residue-class lists are multisets, not a termwise pairing of sorted lists.

Catalogue summaries keep the specialization point and factor association. When one rational characteristic factor has several roots, the displayed multiset applies **separately at each indicated eigenvalue**. Partial and unresolved calculations remain labelled; a missing exponent is not zero.

The unit cyclic determinant is


$$
\Delta(b)=\det\bigl(1,A(b)1,\ldots,A(b)^{N-1}1\bigr),
$$


where \(N\) is the dimension of the space on which the matrix acts. Its nonvanishing proves that the unit is cyclic on that space. Identifying this with a generic Hodge factor additionally requires the ambient/Hodge comparison and persistence hypotheses. A numerical specialization used to display eigenvalues does not itself verify those hypotheses or the admissibility of a point in the theoretical parameter domain.

## Sources and verification

References: B. Alexeev et al., [*On the atomic decomposition of complete intersection in flag varieties*](https://arxiv.org/abs/2609.21914), Theorems 3.26 and 3.28 and Definitions 4.5–4.6. Virtual localization follows Graber–Pandharipande, [*Localization of virtual classes*](https://arxiv.org/abs/alg-geom/9708001). 

The [exact datasets](catalog/datasets.md) provide coefficients, curve coordinates, ordered bases and grading. See [software input/output formats](software/input-output.md) and [validation scope](software/launch-plan.md).

## Verification

Retain the exact matrix together with its ordered basis, grading, curve list and Novikov-coordinate map. The automated checks compare exact localization results, validate catalogue formulas and exercise the displayed software inputs. A numerical specialization or a rendered spectrum does not supply the additional geometric hypotheses needed for a full atomic decomposition.
