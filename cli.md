# gwflags — command-line usage

Everything runs locally from a terminal. All you need is Python ≥ 3.9 with
`sympy` (`pip3 install --user sympy`), or a SageMath installation.

## Graphical interface

If you prefer not to type commands at all:

    python3 -m gwflags.gui          # from the repository root

opens a local web page (http://127.0.0.1:8642, served only on your
machine) with a preset menu covering all benchmark and reference examples,
forms for arbitrary flags/bundles, and three buttons: the c₁(TX)⋆ matrix
(with grading and eigenvalues at y=1), variety info (Schubert basis, c₁,
Fano index), and single GW invariants. Long computations stream their
progress into the log panel. `--port N` and `--no-browser` are available;
after `pip install -e .` the launcher is just `gwflags-gui`.

## Running the CLI

From the repository:

```bash
cd /Users/bogdan/projects/gw_asymptotics
python3 -m gwflags.cli <algebra> --keep <nodes> [-K "<rows>"] <subcommand> [...]
```

Or install once (editable, picks up code changes automatically):

```bash
pip3 install --user -e /Users/bogdan/projects/gw_asymptotics
gwflags <algebra> --keep <nodes> [-K "<rows>"] <subcommand> [...]
```

If your shell can't find `gwflags`, add the user scripts directory to your
PATH (it's `$(python3 -m site --user-base)/bin`).

## Describing the variety

| argument | meaning | examples |
|---|---|---|
| `<algebra>` | simple Lie algebra or a product (`x`-separated) | `A2`, `B3`, `A3xA3`, `A1xA1xA4` |
| `--keep` | 1-based simple roots **kept out of** the parabolic (the notebook's `m` / RootsThatStay), comma-separated; nodes are numbered consecutively across product factors (Bourbaki order) | `1` for Pⁿ, `2` for Gr(2,·), `1,2` for a full A2 flag, `1,4` for P³×P³ |
| `-K` | complete-intersection multidegrees: one row per line-bundle summand, rows separated by `;`, entries by `,` — one entry per kept node, **in `--keep` order**; entries must be ≥ 0 | `-K 2` = O(2); `-K "1,1;2,2"` = O(1,1)⊕O(2,2) |

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

Prints the Schubert basis (reduced words + degrees) and c₁ (of the
complete intersection when `-K` is given). Use this first: the words shown
here are what `gw --classes` accepts, and c₁ = 0 tells you the variety is
Calabi–Yau (then `sqm` is the zero operator by design).

### `gw` — one Gromov–Witten invariant

```bash
# P^2: one line through two points                                   -> 1
python3 -m gwflags.cli A2 --keep 1 gw --beta 1,0 --classes pt,pt
# Gr(2,4): <sigma_1, sigma_21, pt> in degree 1 (Bertram)             -> 1
python3 -m gwflags.cli A3 --keep 2 gw --beta 0,1,0 --classes "2|1 3 2|pt"
# quadric threefold in P^4: a degree-1 twisted invariant             -> 4
python3 -m gwflags.cli A4 --keep 1 -K 2 gw --beta 1,0,0,0 --classes "2 1|3 2 1"
```

- `--beta`: the curve class, one integer per simple root (of the ambient
  algebra, product factors concatenated). Only kept-node entries can be
  nonzero.
- `--classes`: the insertions, separated by `|` (or `,` when no `|` is
  used). Each token is `pt` (point class), `id`/`e` (fundamental class),
  or a reduced word in the simple reflections with spaces between letters
  (`"3 2 1"` = s₃s₂s₁). Words are projected to their minimal coset
  representative automatically — note this means a word that is *not*
  minimal lands in a possibly shorter class (e.g. on Gr(2,4), `"1 2 3"`
  projects into the length-2 cell, not the length-3 one). Safest is to
  copy the words printed by `info`.

The value printed is exact (a rational number; the dimension axiom makes
mismatched insertions 0 instantly).

### `sqm` — small quantum multiplication by c₁(TX)

```bash
python3 -m gwflags.cli A2 --keep 1 sqm
python3 -m gwflags.cli A6 --keep 1 -K "2;2;2" sqm --workers 8
```

Prints the Fano index, the enumerated curve classes, the matrix of
c₁(TX)⋆ in the (reduced) Schubert basis with quantum variables `y1, y2,
…` (one per kept node, in `--keep` order), the grading operator diagonal,
and the eigenvalues. `--workers N` distributes the per-β blocks over N
processes — recommended for index-1 Fano cases, which need curve degrees
up to dim+1.

## The benchmark examples as commands

```bash
python3 -m gwflags.cli A2     --keep 1,2                     sqm            # (a)  Fl(1,2,3)
python3 -m gwflags.cli A2xA2  --keep 1,3 -K "1,1"            sqm            # (b)
python3 -m gwflags.cli A4     --keep 1   -K 4                sqm            # (c)  P4 ∩ O(4)
python3 -m gwflags.cli A3xA3  --keep 1,4 -K "1,1;1,1"        sqm            # (d1)
python3 -m gwflags.cli A3     --keep 1,3 -K "1,1"            sqm            # (d2)
python3 -m gwflags.cli B2     --keep 1,2 -K "1,1"            sqm            # (e)
python3 -m gwflags.cli A3xA3  --keep 1,4 -K "1,1;1,1;1,1"    sqm --workers 8  # (f)
python3 -m gwflags.cli A4     --keep 2   -K "1;1;2"          sqm --workers 8  # (g)
python3 -m gwflags.cli A3xA3  --keep 1,4 -K "1,1;2,2"        sqm --workers 8  # (h)  ~10 min
python3 -m gwflags.cli A4     --keep 1,2 -K "0,1;0,2;1,0"    sqm --workers 8  # (i)
python3 -m gwflags.cli A1xA5  --keep 1,2 -K "1,1;0,3"        sqm            # (j)
python3 -m gwflags.cli A1xA1xA4 --keep 1,2,3 -K "1,1,1;0,0,3" sqm --workers 8 # (k)  ~15 min
```

Or run the whole suite with timings, JSON output and eigenvalues at y=1:

```bash
python3 -u benchmarks/run_benchmarks.py --workers 8          # all, ~25 min
python3 -u benchmarks/run_benchmarks.py a b d1 d2            # a selection
```

Results land in `benchmarks/results.json`; regenerate the PDF report
tables with `python3 reports/make_tables.py && python3
reports/make_symbolic.py` (see `reports/README.md`).

## Tests

```bash
python3 tests/test_gwflags.py        # 20 checks, ~10 s
```

## Notes and limits

- Bundle entries in `-K` must be ≥ 0 (convexity — the mathematics of both
  this package and the original notebook requires it).
- Calabi–Yau intersections (c₁ = 0, e.g. `A5 --keep 1 -K "2;2;2"`, a K3)
  give Fano index 0 and the zero operator; ordinary genus-0 GW theory is
  trivial there, and primary invariants with an identity insertion vanish
  by the string equation.
- Runtime scales with the maximal curve degree = ⌊(dim+1)/min c₁
  coefficient⌋: index-2+ examples run in seconds; index-1 threefolds in
  minutes.
- Everything the CLI prints is also available programmatically
  (`from gwflags import FlagVariety`; see README.md) — the Python API
  additionally exposes custom β lists, raw symbolic localization sums
  (`gw_raw`), and eigenvalues at y=1 (`eigenvalues(M, at_one=True)`).
