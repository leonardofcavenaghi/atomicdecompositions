---
description: The virtual-localization and Euler-twisted decorated-tree formulas used by gwflags for genus-zero Gromov-Witten invariants.
---

# Mathematical Methodology and Replication

This document explains the mathematical foundations underpinning the `gwflags` software and how the computed invariants of complete intersections in flag varieties are calculated.

## 1. Goal of the Software

The `gwflags` library computes the **small quantum multiplication by the first Chern class**, $c_1(TX) \star (-)$, for complete intersections $X$ in flag varieties. The software returns its exact matrix together with the grading and basis used in the calculation.

Specifically, for a complete intersection defined by a homogeneous vector bundle $\mathcal{E}$ on an ambient flag variety $F = G/P$, the software evaluates the equivariant Gromov-Witten invariants and constructs the small quantum multiplication matrix projected onto the flag-ambient cohomology $H^*_{\text{amb}}(X)$.



## 2. Virtual Localization (Graber-Pandharipande)

Directly integrating Gromov-Witten classes over the moduli space of stable maps is generally computationally infeasible. Instead, `gwflags` relies on the algebraic torus action $T \subset G$ acting on the flag variety $F = G/P$ and the corresponding induced action on the moduli space of maps.

By applying the **Graber-Pandharipande Virtual Localization Theorem**, the integrals are reduced to finite sums over the $T$-fixed loci of the moduli space. The fixed loci correspond to decorated trees (or graphs) where:
- Vertices map to fixed points of $F$ (which are in bijection with the Weyl group quotient $W/W_P$).
- Edges correspond to invariant curves connecting these fixed points.

The software recursively generates these graphs for a given curve degree $\beta$, calculates the equivariant Euler classes of the virtual normal bundles (using the roots of $G$ and weights of $\mathcal{E}$), and computes the intersection numbers programmatically. 

**Reference:** Graber and Pandharipande,
[Localization of virtual classes](https://arxiv.org/abs/alg-geom/9708001).

## 3. Schubert classes and flag-ambient cohomology

For the ambient space $F$, the cohomology basis consists of Schubert classes $\sigma_w$. When intersecting with the zero locus of $\mathcal{E}$, not all Schubert classes survive.

The expected dimension and ambient pairing come from the flag and bundle data.
- For a regular section with smooth zero locus, the dimension is $|R^+ \setminus R^+_P| - \text{rank}(\mathcal{E})$.
- The flag-ambient cohomology $H^*_{\text{amb}}(X)$ is exactly the image of the restriction map $i^*: H^*(F, \mathbb{Q}) \to H^*(X, \mathbb{Q})$.

The software forms the Euler-twisted classical pairing
\[
g_{ij}=\int_F\sigma_i\sigma_j e(\mathcal E)
\]
and selects a nondegenerate submatrix to obtain its returned ambient basis.
It does not compute primitive cohomology by this reduction. Identifying this
sector with all cohomology requires additional geometric hypotheses.

## 4. Replicating the Computations

Because `gwflags` explicitly computes the exact localization graphs, all geometric values (Fano index, dimension, basis rank, and the quantum multiplication matrix $A^{\text{alg}}(1)$) can be natively replicated by a researcher on their local machine.

To replicate a result found in our [Catalog](catalog/index.md):
1. Install `gwflags` (see [Installation](installation.md)).
2. Instantiate the flag variety using `X = FlagVariety(algebra, roots_that_stay)`.
3. Invoke `X.small_quantum_multiplication(K)` where $K$ specifies the multidegrees of the vector bundle. The Python API accepts legacy rows such as `[[2]]` or a `HomogeneousBundle`; the browser/CLI accepts compact rows such as `2` and compact aliases such as `Q(2)`.
4. Evaluate the resulting symbolic matrix by setting all `y<node> = 1` to specialize the small quantum multiplication matrix. The variable label is the ambient Bourbaki node, not the position in an abbreviated kept-root list.

The saved matrix entries, dimensions, basis and grading can be compared exactly with the software output.

## 4a. Coordinate contract used by the software

A curve degree is a vector in the simple-coroot basis of the kept
roots `roots_that_stay`, in that declared order. For example, a line on
`Gr(2,4) = A3/P2` is `beta=(1,)`. Internally it is embedded as the ambient
vector `(0,1,0)`; both forms are accepted by `FlagVariety.gw` and by the
website. A full ambient vector is valid only when all removed-root coordinates
are zero. The dimension gate uses
\(\sum \ell(u_i)=\dim X+\langle c_1(TX),\beta\rangle+n-3\).

The matrix returned by `small_quantum_multiplication` is the
flag-ambient operator described above. It is the full small quantum
cohomology operator only when the homology and ambient-completeness hypotheses
are satisfied. The dimension axiom bounds contributing degrees by
\(\langle c_1(TX),\beta\rangle\leq\dim X+1\). This gives a finite
automatic list when every enumerated curve generator has strictly positive
Chern pairing. A zero pairing in an otherwise nonzero Chern vector is not
bounded by this inequality; such cases and negative pairings require explicit
curve lists unless a supported geometric constructor supplies effective
generators with positive pairings. If the entire Chern vector is zero, the
operator is zero.

The reported index is computed in the specified ambient curve lattice (or
from a constructor's effective generators). It equals the geometric Fano
index only when the relevant integral-lattice identification holds. For
example, a smooth `(1,2)` curve in `P¹ × P¹` is `P¹` with Fano index 2,
although the ambient Chern vector `(1,0)` has gcd 1.

## 5. Gromov-Witten Invariants: Theory and Examples

To fully understand the output of `gwflags`, one must understand the underlying objects being computed: **Gromov-Witten (GW) Invariants**.

At a macroscopic level, Gromov-Witten invariants are rational numbers that count the "virtual" number of complex curves of a given genus $g$ and degree $\beta$ that intersect a specified collection of subvarieties inside a target space $X$. 

### Intuitive Exemplification
In classical enumerative geometry, a foundational question is: *"How many lines pass through two generic points in the projective plane $\mathbb{P}^2$?"* 
The classical answer is exactly **1**. 

In the language of Gromov-Witten theory, a line has degree $d=1$ and genus $g=0$. A point represents a specific cohomology class in $H^*(\mathbb{P}^2)$. The fact that exactly one line passes through two points is encoded as a 2-point Gromov-Witten invariant:
$$ \langle \text{point}, \text{point} \rangle_{0, 1} = 1 $$

Another classic example: *"How many rational curves of degree $d$ pass through $3d-1$ general points in $\mathbb{P}^2$?"* 
For $d=1$, we get 1 line through 2 points. For $d=2$, we get 1 conic through 5 points. For $d=3$, we get 12 nodal cubics through 8 points. These values ($1, 1, 12, \dots$) are all Gromov-Witten invariants.

### Quantum Cohomology
Gromov-Witten invariants allow us to "deform" the classical cohomology ring $H^*(X)$ into the **Quantum Cohomology Ring** $QH^*(X)$.

The small quantum product adds genus-zero, three-point GW invariants to the
classical cup product. If \(\{\phi_i\}\) is a basis and \(\{\phi^i\}\)
its Poincaré-dual basis, then
\[
\alpha\star\delta
=\sum_{\beta,i}q^\beta
\langle\alpha,\delta,\phi_i\rangle_{0,3,\beta}\,\phi^i.
\]
Thus a matrix in a general basis uses the **inverse pairing**, not just the
array of three-point invariants. The degree-zero term is the ordinary cup
product. The ambient operator uses the reduced twisted pairing above.

### Why `gwflags` Computes $c_1(TX) \star (-)$
The software specializes in computing the quantum multiplication by a very specific class: the first Chern class of the tangent bundle, $c_1(TX)$. 

The matrix represents the small quantum multiplication operator $c_1(TX) \star (-)$ in the returned basis. Its entries record the classical product and the Gromov–Witten corrections, with Novikov variables keeping track of curve degrees.
