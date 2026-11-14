---
description: Definitions of the geometric, quantum-cohomological, spectral and Hodge-theoretic notation used throughout the catalogue.
---

# Catalogue notation

An example specifies a smooth projective variety \(X\), its geometric construction, and an ordered basis for the computed ambient cohomology. This page fixes the notation used for its matrix, grading, spectral factors and atomic invariants.

## Geometric constructions

| Notation | Meaning |
|---|---|
| \(\mathbb P^n\) | Complex projective space of dimension \(n\) |
| \(\mathrm{Gr}(k,n)\) | Grassmannian of \(k\)-dimensional subspaces of \(\mathbb C^n\) |
| \(\mathrm{LG}(n,2n)\) | Lagrangian Grassmannian for a nondegenerate symplectic form on \(\mathbb C^{2n}\) |
| \(\alpha_i\) | Simple root at Dynkin node \(i\), numbered according to the stated root-system convention |
| \(F=\mathcal G/P\) | Flag variety for a complex semisimple algebraic group \(\mathcal G\) and a parabolic subgroup \(P\) |
| \(\mathcal O_Y(d_1,\ldots,d_r)\) | Line bundle with first Chern class \(\sum_i d_iH_i\) in the stated ordered divisor basis |
| \(Z(Y,E)\) | Zero locus in \(Y\) of a regular section of a vector bundle \(E\) |
| \(\mathbb P_B(E)\) | Projective bundle of one-dimensional quotients of the fibres of \(E\) |
| \(\xi\) | First Chern class of the tautological quotient line bundle \(\mathcal O_{\mathbb P_B(E)}(1)\) |
| \(K_X\) | Canonical divisor of \(X\); \(-K_X=c_1(TX)\) as a divisor class |

A catalogue label such as \(\mathbb P^n/\mathcal O(d_1)+\mathcal O(d_2)\) denotes the zero locus of a section of \(\mathcal O(d_1)\oplus\mathcal O(d_2)\). The slash is shorthand for this construction, not a quotient of varieties. For an ordinary Grassmannian, \(\mathcal O(1)\) is the Plücker line bundle; other homogeneous constructions specify their ample generator and embedding.

The software input `K` describes the defining bundle. For a sum of line bundles, its rows give their coefficients in the stated basis. It is distinct from the canonical divisor \(K_X\). Dynkin labels such as \(\mathsf A_n\) and \(\mathsf C_n\) identify root systems; they are not quantum matrices. Kept roots are the simple roots omitted from the parabolic subsystem, entered by their one-based node numbers. See [flag inputs](../lie-algebras.md) and [geometric identification](sources.md#geometric-identification).

### Chern index

For a positive-dimensional Fano variety, the intrinsic index is the largest positive integer \(I\) for which \(-K_X=IH\) with \(H\in\operatorname{Pic}(X)\). The catalogue's **Recorded Chern index** retains the convention of the given presentation; for the original flag computations it is the gcd of the ambient first-Chern coefficients. A smooth conic has ambient gcd one in \(\mathbb P^2\) and intrinsic index two. For a zero-dimensional variety this gcd is not a geometric Fano index.

## Basis, matrix and grading

Let \(\iota:X\hookrightarrow Y\) be the construction in a flag or toric ambient variety. Write

$$
V=H^*_{\mathrm{amb}}(X,\mathbb Q)
=\operatorname{im}\bigl(\iota^*:H^*(Y,\mathbb Q)\longrightarrow H^*(X,\mathbb Q)\bigr).
$$

Choose the returned homogeneous basis \((e_1,\ldots,e_N)\) of \(V\), and put \(d=\dim X\) and \(d_i=\operatorname{codim}_{\mathbb C}(e_i)\). Thus \(N=\dim_{\mathbb Q}V\) is the matrix size. The unit \(1\in V\) has a coordinate column \(\mathbf 1\) in this basis. The symbol \(\star\) denotes the small quantum product.

The displayed matrix is

$$
A(\mathbf y)=\left[\operatorname{pr}_{V}\circ
\bigl(c_1(TX)\star(-)\bigr)\big|_V\right],
\qquad
A(\mathbf y)e_j=\sum_{i=1}^{N}A_{ij}(\mathbf y)e_i.
$$

Here \(\operatorname{pr}_{V}\) is the projection determined by the nondegenerate restricted Poincaré pairing. **Column \(j\) is the image of \(e_j\); row \(i\) gives its coefficient along \(e_i\).** Matrix entries must be read with the returned basis order. The restricted Poincaré pairing has matrix \(g_{ij}=\int_Xe_i\smile e_j\); the entries of its inverse are denoted \(g^{ij}\).

The grading matrix is

$$
G=\operatorname{diag}\left(d_1-\frac d2,\ldots,d_N-\frac d2\right).
$$

It uses complex codimension: a class in \(H^{2d_i}(X)\) has grading \(d_i-d/2\). This matrix is unchanged by specializing the quantum parameters.

An empty Schubert word, written `[]` or `()`, denotes the unit class. Entries of a nonempty reduced word are one-based simple-reflection labels; the order of the returned words fixes the matrix basis.

## Quantum parameters and spectral factors

The tuple \(\mathbf y=(y_i)_{i\in I}\) consists of the reported Novikov coordinates, in their stated order. The label set \(I\) need not be consecutive. If \(\eta_i\) is the divisor class defining coordinate \(y_i\), then the formal curve monomial is

$$
q^\beta=\prod_{i\in I}y_i^{\eta_i\cdot\beta}.
$$

The software names these coordinates `y1`, `y2`, and so on, retaining ambient node labels in the type-A convention. The accompanying map identifies the variables with the kept roots or chosen Novikov divisors; variable names alone do not identify curve coordinates.

An **analysis point** \(\mathbf a\) is the stated assignment of values to these coordinates, at which all matrix entries are defined. Write \(A(\mathbf a)=A(\mathbf y)|_{\mathbf y=\mathbf a}\). A label \(A(1)\) means that every Novikov coordinate is set to one. The characteristic polynomial and unit cyclic determinant are

$$
\chi_{A(\mathbf a)}(z)=\det(zI_N-A(\mathbf a)),
\qquad
\Delta_A(\mathbf a)=\det\bigl[\mathbf 1,A(\mathbf a)\mathbf 1,\ldots,A(\mathbf a)^{N-1}\mathbf 1\bigr].
$$

The symbol \(I_N\) is the \(N\)-by-\(N\) identity matrix, and \(z\) is a polynomial variable. An eigenvalue \(\lambda\) satisfies \(\chi_{A(\mathbf a)}(\lambda)=0\). In a factorization into monic, pairwise coprime, square-free factors, if \(p_j(z)\) occurs to power \(m_j\), each of its distinct roots is an eigenvalue of algebraic multiplicity \(m_j\).

Nonvanishing of \(\Delta_A(\mathbf a)\) means that the quantum powers of the unit form a basis of the computed space. Its numerical value depends on the basis and point; its nonvanishing is the cyclicity assertion. A zero value at one point does not imply that the determinant vanishes identically.

## Connection exponents

With auxiliary connection coordinate \(u\), the small-locus connection has convention

$$
\nabla_{\partial_{u}}
=\partial_{u}
-\frac{A(\mathbf y)}{u^2}
+\frac{G}{u}.
$$

For an eigenvalue \(\lambda\) at \(\mathbf a\), unramified exponential type means a formal decomposition

$$
M_{\mathbf a,\lambda}\simeq\mathcal E^{\lambda/u}\otimes R_{\mathbf a,\lambda}
$$

without a substitution by fractional powers of \(u\). Here \(\mathcal E^{\lambda/u}\) is the rank-one connection \(\partial_u-\lambda/u^2\), and \(R_{\mathbf a,\lambda}\) is regular singular, meaning that a meromorphic change of basis reduces its pole to order at most one. Its regularized-exponent multiset is

$$
F_{\mathbf a,\lambda}
=\{\!\{-\theta+\mathbb Z:
\theta\text{ is a residue eigenvalue of }R_{\mathbf a,\lambda}\}\!\}.
$$

The residue eigenvalues are required to be rational. Each class lies in \(\mathbb Q/\mathbb Z\) and is counted with its algebraic multiplicity. The multiset has as many entries as the rank of \(R_{\mathbf a,\lambda}\). The notation \(\{\!\{\cdot\}\!\}\) denotes a multiset: \(\{\!\{0,\tfrac12,\tfrac12\}\!\}\) has three entries. The powers \(s=-\theta\) give the displayed classes modulo \(\mathbb Z\), usually represented in \([0,1)\).

A multiset is attached to a particular eigenvalue at a particular point. A row whose spectral condition is \(p_j(\lambda)=0\) applies separately at each root of that factor. The grading diagonal is not, by itself, the list of residue eigenvalues of the formal factors. The [exact spectral data](../data/spectral-data.json) give the point, determinant and characteristic factors of \(A(\mathbf a)\) together. Atomic calculations can use a different point; compare their eigenvalue labels only after checking that assignment. See the [localization conventions](../toric/mathematics.md#regularized-exponent-multisets) for the connection.

## Full cohomology and atomic invariants

The ambient dimension \(N\), the full Hodge-invariant dimension and the total cohomology dimension are different quantities. The rational Hodge-invariant subspace is

$$
H^*_{\mathrm{Hod}}(X)
=\bigoplus_p\left(H^{2p}(X,\mathbb Q)\cap H^{p,p}(X)\right).
$$

Its complexification is the invariant space for the Hodge group. Ambient classes lie in this subspace, but additional rational Hodge classes may occur in primitive cohomology. The full Hodge numbers are \(h^{p,q}(X)=\dim_{\mathbb C}H^q(X,\Omega_X^p)\), and the total cohomology dimension is \(\sum_{p,q}h^{p,q}(X)\). In particular, neither the sum of diagonal Hodge numbers nor the matrix size automatically equals the rational Hodge-invariant dimension.

A coarse Hodge atom is the rational Hodge-group representation attached to a generic local spectral component of the quantum connection. For an atom represented by \(E^\alpha\), write \(E^\alpha_{\mathbb C}=E^\alpha\otimes_{\mathbb Q}\mathbb C\). The Hodge group \(\mathrm{Hod}\) is the kernel of the Mumford–Tate group's character on the Tate line \(\mathbb Q(1)\). The atomic invariants are

$$
\rho_\alpha
=\dim_{\mathbb C}\bigl(E^\alpha_{\mathbb C}\bigr)^{\mathrm{Hod}_{\mathbb C}},
\qquad
P_\alpha(t)=\sum_{k\in\mathbb Z}
\dim_{\mathbb C}\bigl(E^\alpha_{\mathbb C}\bigr)^k t^k,
$$

where \(k\) is the weight of the Hodge cocharacter. A class of Hodge type \((p,q)\) has weight \(p-q\). Thus the full Hodge polynomial is

$$
P_X(t)=\sum_{p,q}h^{p,q}(X)t^{p-q}.
$$

All coefficients are nonnegative dimensions; no alternating signs are inserted for odd cohomology. The value \(P_\alpha(1)\) is the full rank of the atom. The constant coefficient of \(P_\alpha\) counts cocharacter-weight-zero directions and can exceed \(\rho_\alpha\).

The unit-cyclic criterion identifies full coarse factors only after the computed space is identified with the full Hodge-invariant sector and unit cyclicity is established at an admissible point with the required geometric persistence. Determining their full Hodge polynomials also requires the action on the remaining cohomology. In a full coarse decomposition, sum one \(P_\alpha\) for each atom, with the indicated multiplicity, to obtain \(P_X\). A rational characteristic factor alone does not determine the Hodge polynomial of each conjugate root. See [atomic invariants](atomic-invariants.md).

## Export compatibility

Some connection-analysis exports use the negative of the matrix displayed here. If such an export has a monic characteristic factor \(p(z)\) of degree \(r\), the corresponding monic factor of \(A\) is \((-1)^r p(-z)\). If \(B=-A\) uses the same basis and unit, its cyclic determinant satisfies \(\Delta_A=(-1)^{N(N-1)/2}\Delta_B\). The grading matrix and the underlying connection are unchanged. All catalogue eigenvalue labels and spectral conditions refer to \(A(\mathbf a)\).

In exact-data exports, `null` in an exponent field supplies no exponent value. It must not be interpreted as an empty multiset or as the zero exponent.
