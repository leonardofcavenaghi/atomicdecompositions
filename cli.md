# gwflags — command-line usage

Everything runs locally from a terminal. All you need is Python ≥ 3.9 with
`sympy` (`pip3 install --user sympy`), or a SageMath installation.

## Graphical interface

If you prefer not to type commands at all:

    python3 -m gwflags.gui          # from the repository root

opens a local web page (http://127.0.0.1:8642, served only on your
machine) with a curated preset menu for common benchmark examples,
forms for arbitrary flags/bundles, and three buttons: the c₁(TX)⋆ matrix
(with grading and eigenvalues at y=1), variety info (Schubert basis, c₁,
Fano index), and single GW invariants. Long computations stream their
progress into the log panel. `--port N` and `--no-browser` are available;
after `pip install -e .` the launcher is just `gwflags-gui`.

## Running the CLI

From the repository root:

```bash
python3 -m gwflags.cli <algebra> --keep <nodes> [-K "<rows>"] <subcommand> [...]
```

Or install once (editable, picks up code changes automatically):

```bash
pip3 install --user -e .
gwflags <algebra> --keep <nodes> [-K "<rows>"] <subcommand> [...]
```

If your shell can't find `gwflags`, add the user scripts directory to your
PATH (it's `$(python3 -m site --user-base)/bin`).

## Describing the variety

| argument | meaning | examples |
|---|---|---|
| `<algebra>` | simple Lie algebra or a product (`x`-separated) | `A2`, `B3`, `A3xA3`, `A1xA1xA4` |
| `--keep` | 1-based simple roots **kept out of** the parabolic (the notebook's `m` / RootsThatStay), comma-separated; nodes are numbered consecutively across product factors (Bourbaki order) | `1` for Pⁿ, `2` for Gr(2,·), `1,2` for a full A2 flag, `1,4` for P³×P³ |
| `-K` | complete-intersection multidegrees: one row per line-bundle summand, rows separated by `;`, entries by `,` — one entry per kept node, **in `--keep` order**; entries must be ≥ 0. The expression forms `O(...)`, `S(node)`, `Q(node)`, `osum(...)`, `tensor(...)`, `sym(...)`, `wedge(...)`, and `quot(E,F)` (also `Quot(E,F)`) are accepted. | `-K 2` = O(2); `-K "1,1;2,2"` = O(1,1)⊕O(2,2) |

Common varieties:

| variety | invocation |
|---|---|
| Pⁿ | `An --keep 1` |
| Gr(k, n) | `A(n-1) --keep k` |
| Fl(1,2,3) | `A2 --keep 1,2` |
| Fl(1,3,4) | `A3 --keep 1,3` |
| P²×P² | `A2xA2 --keep 1,3` |
| P³×P³ | `A3xA3 --keep 1,4` |
| P¹×P⁵ | `A1xA5 --keep 1,2` |
| SO(5)/B | `B2 --keep 1,2` |
| quadric Qⁿ⁻¹ ⊂ Pⁿ | `An --keep 1 -K 2` |

## Subcommands

### `info` — basis and first Chern class

```bash
python3 -m gwflags.cli A3 --keep 2 info
```

Prints the Schubert basis (reduced words + degrees), the zero-locus dimension
(after subtracting the rank of `-K`, with the ambient dimension shown when a
bundle is present), and c₁ (of the complete intersection when `-K` is given).
Use this first: the words shown here are what `gw --classes` accepts, and
c₁ = 0 tells you the variety is Calabi–Yau (then `sqm` is the zero operator by
design).

### `gw` — one Gromov–Witten invariant

```bash
# P^2: one line through two points                                   -> 1
python3 -m gwflags.cli A2 --keep 1 gw --beta 1 --classes pt,pt
# Gr(2,4): <sigma_1, sigma_21, pt> in degree 1 (Bertram)             -> 1
python3 -m gwflags.cli A3 --keep 2 gw --beta 1 --classes "2|1 3 2|pt"
# quadric threefold in P^4: a degree-1 twisted invariant             -> 4
python3 -m gwflags.cli A4 --keep 1 -K 2 gw --beta 1 --classes "2 1|3 2 1"
```

- `--beta`: the curve class, normally entered in kept-root order. A zero-padded vector with one entry per ambient simple root is
  also accepted; entries at removed roots are rejected. For example, a line on
  `A3 --keep 2` is `--beta 1` or `--beta 0,1,0`. The printed result uses the
  canonical ambient node order.
- `--classes`: the insertions, separated by `|` (or `,` when no `|` is
  used). Each token is `pt` (point class), `id`/`e` (fundamental class),
  or a reduced word for a minimal parabolic-coset representative, with spaces
  between letters (`"3 2 1"` = s₃s₂s₁). The CLI rejects nonreduced or
  nonminimal words; copy the words printed by `info`.

The value printed is exact (a rational number; the dimension axiom makes
mismatched insertions 0 instantly).

### `sqm` — small quantum multiplication by c₁(TX)

```bash
python3 -m gwflags.cli A2 --keep 1 sqm
python3 -m gwflags.cli A6 --keep 1 -K "2;2;2" sqm --workers 8
```

Prints the Fano index, the enumerated curve classes, the matrix of
c₁(TX)⋆ in the (reduced) Schubert basis, with quantum variables `y<node>`
labelled by ambient node number (zero off kept nodes), the grading operator
and the eigenvalues. Automatic enumeration requires nonnegative c₁ pairings
in every kept direction; pass explicit Python `betas` for a formal/truncated
non-nef calculation. `--workers N` distributes the per-β blocks over N
processes — recommended for index-1 Fano cases, which need curve degrees up to
dim+1.

## Reproducible validation

The executable validation campaign is kept in `tests/` rather than a separate
benchmark package. Run the complete suite with:

```bash
python3 -m pytest tests/ -q
```

`tests/test_reference_list.py` checks the transcribed external reference
matrices. `tests/test_gwflags.py` covers known enumerative values, and
`tests/test_bundles.py` covers quotient bundles and bundle combinations.

## Tests

```bash
python3 tests/test_gwflags.py        # 20 checks, ~10 s
```

## Notes and limits

- Bundle entries in `-K` must be ≥ 0 (convexity — the mathematics of both
  this package and the original notebook requires it). Bundle expressions also
  accept compact aliases `O(1)`, `S(node)`, and `Q(node)`; `quot(E,F)`
  (or `Quot(E,F)`) checks the subbundle condition; explicit Python
  forms such as `O(X,1)` and `taut_quot(X,1)` remain valid.
- Calabi–Yau intersections (c₁ = 0, e.g. `A5 --keep 1 -K "2;2;2"`, a K3)
  give Fano index 0 and the zero operator. The degree-zero `gw` convenience
  path returns classical cup integrals; the degree-zero potential keeps only
  stable three-point terms and omits unstable cases.
- Automatic `sqm` beta enumeration is intended for Fano or nef c₁ data. If a
  kept c₁ coordinate is negative, the routine asks for an explicit `betas`
  list so that a formal/truncated calculation is not mistaken for a finite
  Fano matrix.
- Runtime scales with the curve classes satisfying ⟨c₁(TX),β⟩ ≤ dim+1.
  Directions with zero c₁ coefficient are capped separately; index-2+ examples
  usually run in seconds, while index-1 examples can take minutes.
- Everything the CLI prints is also available programmatically
  (`from gwflags import FlagVariety`; see README.md) — the Python API
  additionally exposes custom β lists, raw symbolic localization sums
  (`gw_raw`), and eigenvalues at y=1 (`eigenvalues(M, at_one=True)`).
