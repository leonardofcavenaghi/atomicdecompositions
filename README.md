# gwflags — GW invariants of flag varieties (Python / SageMath)

A translation of `V3.nb` (Mathematica + LieART) into a fast Python
package; runs on plain Python and inside SageMath.

It computes, for a flag variety **G/P** — of any simple type A–G *or a
product* (`'A3xA3'` for P³×P³-type flags, `'A1xA1xA4'`, …):

- genus-0 **Gromov–Witten invariants** by Bott localization: sums over
  decorated trees (fixed loci of stable maps), equivariant Schubert classes
  restricted to fixed points via **Billey's formula**;
- the same for **complete intersections** in G/P (twisted invariants with
  the Euler class of `E = O(K_1) ⊕ O(K_2) ⊕ …`);
- the **small quantum multiplication matrix `c1(TX)⋆`**, its grading
  operator, and its **eigenvalues** (Conjecture 𝒪 / Gamma-conjecture
  asymptotics), plus the **Fano index** and the curve classes to sum over.

## How it is fast

The notebook carried symbolic rational functions through every step and
took `x → prime·t, t → 0` limits at the end.  This package instead:

- **gates every invariant by the dimension axiom** (`expected_degree`) —
  mismatched insertions return 0 exactly, which is what the notebook's
  limits computed;
- **evaluates the gated localization sum exactly at two independent random
  rational points** of the equivariant torus (`NumericBackend`): the gated
  sum is a constant, so the evaluation *is* the invariant, agreement of the
  two points guards against accidental poles, and no CAS ever runs in the
  hot loop (plain `fractions.Fraction`);
- keeps all Weyl/root data as **integer-normalized exact tuples** (fast
  hashing), turns decorated-tree vertex computation into **precomputed
  integer table lookups**, canonicalizes trees by **AHU hashing from the
  center** (no permutation sweeps; automorphism orders fall out of the same
  pass), and enumerates edge decorations by a **pruned per-edge DFS**;
- **caches everything class-independent** across the quantum-matrix pair
  loops: decorations per (tree, β, marks) on the flag, per-decoration base
  factors, edge factors, Billey restrictions, R-factors, CI twists;
- optionally distributes per-β blocks over processes
  (`small_quantum_multiplication(..., workers=N)`, fork-based; verified
  bit-identical to serial).

sympy (or Sage, auto-detected) only assembles the final matrices with the
quantum variables `y_i` and extracts eigenvalues.  The raw symbolic sums
remain available via `FlagVariety.gw_raw` / the `.sym` calculator.

## Requirements

- Plain Python ≥ 3.9 with `sympy` (`pip install sympy`), **or**
- SageMath (no extra dependencies; the package detects Sage and uses its
  symbolic ring — same code, faster algebra).

## Usage

```python
from gwflags import FlagVariety, projective_space, grassmannian, full_flag

X = projective_space(2)               # = FlagVariety('A2', [1])
X.gw([X.pt, X.pt], beta=(1, 0))       # 1   — one line through two points
X.gw([X.pt]*5,      beta=(2, 0))      # 1   — one conic through five points

G = grassmannian(2, 4)                # A3 / P_2
# sigma_1 * sigma_21 = sigma_22 + q  (Bertram):
G.gw([G.schubert((2,)), G.schubert((1, 2, 3)), G.pt], beta=(0, 1, 0))  # 1

M, Gr, idx = X.small_quantum_multiplication()
X.eigenvalues(M)                      # [3*y1**(1/3), 3*y1**(1/3)*zeta_3, ...]

# complete intersection: quadric surface in P^3
Q = projective_space(3)
M, Gr, idx = Q.small_quantum_multiplication(K=[[2]])
Q.eigenvalues(M)                      # [4*sqrt(y1), -4*sqrt(y1), 0]
```

In SageMath the same code applies (`sage -python`, or `import gwflags`
from a Sage session with the package on `sys.path`).

GUI (local web app, stdlib-only server — the modern replacement for the
notebook's dialog screens): `python3 -m gwflags.gui`, with presets for
every benchmark and reference example.

Command line (**see [cli.md](cli.md) for the full guide** — setup, all
subcommands, and every benchmark example as a copy-pasteable command):

```bash
python3 -m gwflags.cli A2 --keep 1 info
python3 -m gwflags.cli A2 --keep 1 gw --beta 1,0 --classes pt,pt
python3 -m gwflags.cli A3 --keep 2 gw --beta 0,1,0 --classes "2|1 2 3|pt"
python3 -m gwflags.cli A2 --keep 1 sqm
python3 -m gwflags.cli A3 --keep 1 sqm -K 2          # quadric in P^3
```

`--keep` is the notebook's `m` (RootsThatStay): the 1-based simple roots
**not** in the parabolic — `1` for Pⁿ, `k` for Gr(k, n). Schubert classes
are entered as reduced words in the simple reflections (`pt`, `id`
accepted). `-K` rows are the multidegrees of the bundle summands over the
Picard generators (the notebook's `{{1,2},{1,1}}` becomes `"1,2;1,1"`).

Tests (all values independently known from Schubert calculus):

```bash
python3 tests/test_gwflags.py
```

## Where each notebook function lives

| V3.nb | gwflags |
|---|---|
| LieART data (`PositiveRoots`, `OrthogonalBasis`, `ReflectionMatrices`, `CartanMatrix`, `Coroots`, `OmegaBasis`) | `rootsystem.RootSystemData` (pure Python, exact `Fraction` arithmetic, Bourbaki realizations) |
| `WeylGroupWords`, `GenerateGroup`, `FindCosets`, `ProjectionMap`, `ReflextionRoots` | `weyl` (`WeylData`) |
| `AllTrees(N)`, `nonnegCompositions`, `congruentModGensQ`, `FindExpandedAssociations`, `AllPossibleMarks`, `DecoratedTrees`, `VertexComputation`, `TableOfTheTree`, `RemoveIsomorphicDuplicates`, `DecoratedAutomorphismGroupSize`, `IntegerCombination` | `trees` |
| `ChangeToPolynom(Byll)`, `LinearMapToPolynomial`, `InvertVariables`, `RFactor`, `Bylleys`, `OmegaLie`, `KappaGamma`, `IVertex`, `GWInvariant` | `localization.GWCalculator` |
| `mu`, `EulerCompleteIntersection`, `hCompleteIntersection`, `OmegaCompleteIntersection`, `GWCOMPLETEINTERSECTION` | `cintersection` |
| `MetricCompletInter`, `LinesLI`/`ColumnsLI`/`ReduceMatrix`, `VectorsWithSupport`, `BetasAndFanoIndex`, `SmallQuantumMultiplication` | `quantum` |
| `DialogInput` GUI screens, progress bars | `cli` (argparse) / `progress=` callbacks |
| final `x -> prime * t`, `Limit[t -> 0]` evaluation | `symbolic.Backend.evaluate_gw` |

Conventions: simple roots are numbered as in Bourbaki (for type A this
matches LieART). Equivariant variables `x_i` correspond to the simple
roots α_i (a root's polynomial is its expansion in simple roots);
quantum variables `y_i` track the curve class over the kept simple roots.
All Weyl-group elements are matrices in the orthogonal realization;
Schubert classes are minimal coset representatives (`FlagVariety.classes`,
`.schubert(word)`, `.pt`).

## Translation notes (deliberate differences / notebook quirks)

- **Edge labels in isomorphism tests compare degree only.** The notebook's
  `EffectiveEdgeLabel[{_, lbl_}] := lbl` drops the root part of an edge
  label in `RemoveIsomorphicDuplicates` and in the automorphism count.
  This is not an accident but load-bearing: the same fixed curve seen from
  its two endpoints carries *different* root labels in a partial flag, and
  only the degree-blind comparison merges the two copies. The translation
  reproduces this exactly (`DecoratedTree.canonical_key`,
  `.automorphism_group_size`); with full edge labels P² ⟨pt,pt⟩₁ would
  come out wrong.
- **Parent vertex lookup.** `KappaGamma` finds the Weyl element across the
  incoming edge by comparing `PropertyValue[...][[1]][[1]]` against the
  *list-wrapped* `TreeTable[[i]][[1]]`, which never matches, so it always
  takes the edge's first endpoint; that is the parent for the tree
  representatives the notebook generates. The translation uses the rooted
  tree's actual parent, which is the intended (and equivalent) semantics.
  Contributions were verified to be independent of the rooting.
- **`ChangeToPolynomByll`'s inverted-variables branch** (for negative
  roots) is preserved but is dead code in practice: BFS words are reduced,
  so Billey's β_i are always positive roots.
- **Two latent bugs of the notebook are fixed rather than reproduced**
  (both found by adversarial review with concrete wrong outputs):
  (1) the notebook pairs the bundle multidegrees `K` with the ascending
  positions of positive c1 entries in `BetasAndFanoIndex` /
  `SmallQuantumMultiplication` but with `RootsThatStay` order in `mu` — the
  two disagree when `RootsThatStay` is not sorted; `chern_class_ci` now
  always uses `roots_that_stay` order, matching the localization twist.
  (2) the notebook bounds the curve-class enumeration by total degree
  `(dim+1)/min(positive c1 entries)`, which silently drops contributing
  classes whenever c1 of the complete intersection has a *zero* entry on a
  kept node (e.g. a (1,2)-curve in P¹×P¹ lost its quantum term and got a
  nilpotent c1⋆); the enumeration is now `⟨c1, β⟩ ≤ dim+1` with
  zero-coefficient directions capped at `dim+1`, which the dimension axiom
  makes exhaustive.  A Calabi–Yau intersection (c1 = 0) now returns the
  zero operator instead of crashing.
- **`Bylleys` subset size.** The notebook enumerates subsets of size ≤
  ℓ(shubert); products of fewer than ℓ simple reflections can never equal
  an element of length ℓ, so the translation enumerates size exactly ℓ.
- **Parallelism.** `LaunchKernels/ParallelTable` are replaced by optional
  fork-based process workers over the per-β blocks of the quantum matrix
  (`small_quantum_multiplication(..., workers=N)`, CLI `--workers N`),
  verified bit-identical to the serial path.
- **GW number extraction.** The notebook substituted every equivariant
  variable by a random prime times `t` and took `t → 0`; the package gates
  by the dimension axiom and evaluates the (then constant) sum exactly at
  two independent random points — same numbers, no symbolic limits.  The
  notebook-style raw symbolic sum remains available via
  `FlagVariety.gw_raw` and `symbolic` backends' `evaluate_gw`.

## Verified against known values

| invariant | value |
|---|---|
| P¹, P², P³: ⟨pt, pt⟩ degree 1 | 1 |
| P²: ⟨pt, pt, h⟩₁ (divisor axiom), ⟨pt⁵⟩₂ (conics through 5 points) | 1 |
| Fl(3) = A2/B: ⟨pt, pt⟩₍₁,₁₎ | 1 |
| Gr(2,4): ⟨σ₁, σ₂₁, pt⟩ degree 1 (σ₁⋆σ₂₁ = σ₂₂ + q) | 1 |
| P¹: c1⋆ eigenvalues ±2√y, Fano index 2; P²: 3·y^{1/3}·µ₃, Fano index 3 | ✓ |
| Quadric surface in P³ (K=[[2]]): twisted metric, rank reduction, eigenvalues {±4√y, 0} | ✓ |
| P¹×P¹: divisor axiom per factor; c1⋆ eigenvalues {±4, 0, 0} at y=1 | ✓ |
| (1,2)-curve in P¹×P¹ (K=[[1,2]]): c1⋆ eigenvalues ±2 at y=1 (ambient QH of a P¹) | ✓ |
| Quartic K3 in P³ (K=[[4]]): c1⋆ = 0 (Calabi–Yau) | ✓ |
| Quadric threefold Q³ in P⁴ (K=[[2]]): Fano index, full SQM matrix, grading, and eigenvalues {0} ∪ 3·2^{2/3}y^{1/3}µ₃ agree **exactly with V3.nb's cached Mathematica output** (the notebook's one completely saved run) | ✓ |
| **Quantum-connection asymptotics** (`gwflags/quantum_connection.py`, `tests/test_quantum_connection.py`): formal exponents of ∇ = d/du + K/u² + G/u per spectral sector (exact δ = u²d/du scalar reduction + indicial polynomials; handles nilpotent blocks/fractional exponents/logs) and Kontsevich "dimension" candidates −2·min s. Validated: cubic threefold z=0 exponents **{−1/6, −5/6}, dim 5/3** (Kontsevich's slides, on the nose); cubic fourfold **dim 2 = K3**; quadrics 0; Pⁿ all 0; *predictive*: quartic threefold degenerate sector dim **5/2** = (n+1)(d−2)/d; new data: V₈ degenerate sector exponents [−1,−1,−1], dim 2 | ✓ |
| **Homogeneous-bundle twists** (`gwflags/bundles.py`, `tests/test_bundles.py`): complete intersections in arbitrary curve-wise-convex homogeneous bundles via fiber-weight multisets — tautological Q and S\*, duals, ⊕/⊗/Sym/Λ, cross-factor box products. Verified by classical isomorphisms: Z(Gr(2,4), Q) = P² and Z(Gr(2,5), Q) = P³ (**twisted SQM equals the native matrix entry-for-entry**), Z(Gr(2,5), Sym²S\*) = OG(2,5) = B₂/P₂ (**cross-Dynkin-type spectral agreement**); legacy split rows reproduce exactly; non-convex bundles (e.g. S) rejected with guidance | ✓ |
| **Second, formula-independent engine** (`gwflags/gkm.py`, `tests/test_gkm_engine.py`): the Holmes–Muratore GKM localization formula (arXiv:2509.07562, Thm 3.4) implemented from their statement — intrinsic GKM-graph trees, connection-based edge factors, uniform vertex factor — and diffed against the classical engine **at the same random torus point: raw localization sums agree exactly as rational numbers** across P², Fl(3), Gr(2,4), SO(5)/B, P²×P² (incl. degree-2, 5-mark, and non-gated homogeneous sums); h(e,d) flag-independence (their Thm 3.6) verified; no parallel GKM edges in the battery (documents the dedup assumption) | ✓ |
| **Full reference campaign** (`tests/reference_cases.py` / `test_reference_list.py`, from `tests/full_test_list.tex`): ~30 externally computed quantum matrices — hypersurfaces/CIs in P⁴ and P⁵, Gr(2,4)/Gr(2,5) families (incl. del Pezzo and Gushel–Mukai sections), Gr(2,6)∩O(1,1,2), Fl(1,3,4) (both sections), Fl(1,4,5) (flag 20×20 + double section), B2/B∩O(1,1), **G₂/P₁, G₂/P₂ (±O(1)), OG(3,7)=B₃ (four sections), LG(3,6)=C₃ (two sections)** — all match exactly. Two reference discrepancies adjudicated with independent mathematics (see [discrepancy.md](discrepancy.md)): the V₈ corner entry is a genuine factor-2 error in the reference (quantum-period referee: T = 56 exactly); the Fl(1,2,5)/GM-20 reference is **correct at curve degrees ≤ 4 up to an explicit degree-3 basis change** (`tests/gm20_forensics.py` exhibits the conjugation) but misses the degree-5 classes, which are certified nonzero by the divisor axiom | ✓ |
| AHU canonicalization + automorphism orders ≡ brute-force n! reference on 4600 random labeled trees; DFS decoration enumeration ≡ compositions/permutations reference | ✓ |

## Benchmark suite

`benchmarks/run_benchmarks.py` encodes the 11 quantum-multiplication
examples of `tests/Tests_for_the_software (1).pdf` (ids `a`–`k`; `d1`/`d2`
are the two models of example (d)).  It builds each flag, enumerates curve
classes, assembles c1(TX)⋆, and reports eigenvalues at y=1 with timings;
the document's two coincidence requirements — (a)≡(b) and (d1)≡(d2) — are
checked on the eigenvalue spectra automatically.

    python3 -u benchmarks/run_benchmarks.py --workers 8        # all
    python3 -u benchmarks/run_benchmarks.py h k                # a selection

Results land in `benchmarks/results.json` (matrices, gradings, spectra,
timings).  See the table in the repository discussion / commit message for
current timings — everything runs in seconds except the degree-5 cases
(f, g, h, i), which run in tens of seconds with `--workers 8`.
