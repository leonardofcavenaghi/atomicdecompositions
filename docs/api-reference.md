# GWFlags API Reference

`gwflags` evaluates decorated-tree formulas with exact Python/Sage
computations. The default numerical path evaluates the
localization sum at two rational torus points; the symbolic path remains
available through `gw_raw`.

## 1. Root systems (`gwflags/rootsystem.py`)

`RootSystemData` stores Bourbaki-numbered simple and positive roots, Cartan and
reflection matrices, coroots, and fundamental weights. All root and weight
arithmetic is exact (`fractions.Fraction`) and semisimple products such as
`A2xA2` are supported.

## 2. Virtual localization (`gwflags/localization.py`)

`GWCalculator` implements Graber--Pandharipande genus-zero virtual
localization on decorated trees:

- `rfactor(w)` evaluates the fixed-point Euler factor;
- `billey(schubert, vertex)` evaluates a Schubert restriction by Billey's
  formula;
- `omega_lie(w, root_idx, d)` evaluates the invariant-curve edge factor;
- `kappa_gamma(dt)` and `i_vertex(dt, v)` evaluate tree edge/vertex factors;
- `gw_invariant(coh_classes, beta)` sums all valid decorated trees.

The low-level calculator uses an ambient vector indexed by all simple roots.
The public `FlagVariety` methods normalize kept-root coordinates before
calling it.

## 3. Complete-intersection twists (`gwflags/cintersection.py`)

A homogeneous bundle is represented by its multiset of torus weights. The
module implements the Euler-twisted factors:

- `euler_complete_intersection(gw, K, w)` gives the fixed-point Euler class;
- `h_complete_intersection(gw, K, w, root_idx, d)` gives the convex edge
  contribution;
- `gw_complete_intersection(gw, coh_classes, beta, K)` performs the twisted
  localization sum.

Every invariant-curve splitting degree must be nonnegative. This is the
curve-wise convexity condition used by the genus-zero twisted theory. A smooth
zero-locus interpretation additionally needs global generation and smoothness
of the expected codimension.

Bundles can be constructed with `O(X, a1, ...)`, `taut_sub(X, node)`,
`taut_quot(X, node)`, `dual`, `osum`, `tensor`, `sym`, `wedge`, and `quot`. The GUI and
CLI also accept compact aliases `O(a1,...)`, `S(node)`, and `Q(node)` with
`X` bound to the current flag. `quot(E, F)` (also `Quot(E, F)`) checks
that the fiber-weight multiset of `F` is contained in `E` with multiplicity
before constructing the quotient. A legacy split bundle is a list of rows, for
example `[[1], [2]]` for `O(1) + O(2)` on a one-generator space.

## 4. Main interface (`gwflags/__init__.py`)

### `FlagVariety(algebra, roots_that_stay, backend=None)`

`roots_that_stay` is a distinct list of 1-based simple-root nodes not in the
parabolic, in the order used for Picard coordinates. For example,
`FlagVariety("A4", [2])` is `Gr(2,5)`, while `[1,3]` describes the two-factor
product convention when the algebra is a product.

### Curve classes (`beta`)

A curve class is written
\[
  \beta=(b_{i_1},\ldots,b_{i_\rho}),
  \qquad (i_1,\ldots,i_\rho)=\texttt{roots\_that\_stay},
\]
where the entries are nonnegative integers in the kept simple-coroot basis.
The public methods accept this compact vector and embed it at the ambient
Bourbaki nodes. A zero-padded ambient vector of length `rank` is also accepted,
but every removed-node entry must be zero. For `A3 --keep 2`, `(1)` and
`(0,1,0)` therefore denote the same line class. The returned GW result and
progress messages use the canonical ambient vector.

### `gw(coh_classes, beta, K=None, progress=None)`

Returns the exact genus-zero invariant
\(\langle\sigma_{u_1},\ldots,\sigma_{u_n}\rangle_{0,n,\beta}\), optionally
Euler-twisted by `K`. The dimension axiom is checked before localization; a
mismatch returns zero. Degree zero uses the classical cup-integral shortcut
(the degree-zero path keeps stable three-point terms and omits unstable
cases).

### `expected_degree(beta, n_classes, K=None)`

Returns the codimension sum required by the dimension axiom after normalizing
`beta` and accounting for the bundle rank.

### `fano_index_and_betas(K=None)`

Returns `(I_X, betas)`, where `I_X` is the gcd of the first-Chern
coordinates and `betas` is the finite list needed for the ambient quantum
matrix. Automatic enumeration is justified for Fano/nef first-Chern data by
\(\langle c_1(TX),\beta\rangle\leq\dim X+1\). A zero-Chern Calabi--Yau case
returns index zero and only the zero class. If a kept Chern coordinate is
negative, automatic enumeration raises a `ValueError`; supply an explicit
`betas` list for a deliberately truncated/formal calculation.

### `small_quantum_multiplication(K=None, betas=None, progress=None, workers=0)`

Returns `(M, grading, basis_indices)` for multiplication by `c1(TX)` on the
flag-ambient Schubert sector. `M` is symbolic in `y<node>`, where `<node>` is
the ambient Bourbaki label of a kept root (so kept nodes `1,3` use `y1` and
`y3`). `betas` may be supplied in either accepted beta convention. The matrix
is the full small quantum-cohomology operator only when the relevant homology
and ambient-completeness hypotheses hold; otherwise it is the flag-ambient block. `workers=N` distributes independent
per-beta blocks over forked processes.

### Other useful methods

- `classes`, `class_words()`, `schubert(word)`, and `pt` expose the minimal
  Schubert representatives;
- `gw_raw(...)` returns the unspecialized symbolic localization sum;
- `eigenvalues(M, at_one=True)` computes the spectrum after setting all
  Novikov variables to one.

## 5. Schubert words and interface syntax

`FlagVariety.schubert(word)` projects an arbitrary Weyl word to its minimal
coset representative for low-level exploratory use. The CLI and browser form
use the safer published contract: each insertion word must be reduced and
minimal for the chosen parabolic. Run `info`/**Space Info**, then copy one of
the printed words (or use the **Add** button). Separate insertions with `|`;
`pt`, `id`, and `e` are accepted shortcuts.

For the compact GUI/CLI bundle field, use `3` or `1,1;2,2` for line-bundle
rows; Python list notation such as `[[3]]` belongs to the Python API. In a
symbolic matrix, variables are named by ambient nodes, while beta input is in
kept-root order unless zero-padded.

## 6. Minimal reproducible examples

```python
from gwflags import FlagVariety, grassmannian, projective_space
from gwflags.bundles import O, taut_quot, dual, taut_sub, osum, wedge, quot

P2 = projective_space(2)
assert P2.gw([P2.pt, P2.pt], beta=(1,)) == 1
assert P2.gw([P2.pt, P2.pt], beta=(1, 0)) == 1

G = grassmannian(2, 4)
s1, s21, pt = G.schubert((2,)), G.schubert((1, 3, 2)), G.pt
assert G.gw([s1, s21, pt], beta=(1,)) == 1

Q = taut_quot(G, 2)
K = osum(Q, O(G, 1))
M, grading, basis = G.small_quantum_multiplication(K=K)

E = osum(taut_sub(G, 2), Q)
Kq = quot(E, taut_sub(G, 2))
assert Kq.rank == 3
```
