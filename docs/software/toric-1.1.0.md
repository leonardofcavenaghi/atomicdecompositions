---
description: Compute toric GW invariants, ambient quantum multiplication and supported Hodge data through Python, CLI and the local interface.
---

# How to use version 1.1.0.dev1 toric software

This guide describes the development version `1.1.0.dev1`. Install the complete bundle as described in [Installation](../installation.md). The toric engine imports shared `gwflags` infrastructure; `gwtoric/` alone is not a complete distribution.

## Launch the interface

```bash
python -m gwtoric.gui --no-browser
```

Open <http://127.0.0.1:8643>. The same interface is available at <http://127.0.0.1:8650/toric/> when using the [combined application](combined.md). Stop a server with Ctrl-C.

## Load a preset

1. Choose **P2** from **Preset library**, or use the **Product of Pⁿ** tab with factor `2`.
2. Click **Fan, cohomology & curves** to see the basis, divisor generators and curve coordinates.
3. For one line through two points, enter beta `1,1,1` and insertions `pt|pt`.
4. Click **Compute invariant**. The answer is 1.
5. To compute multiplication by c1 instead, leave the optional curve list blank and click **Compute c1(TX)⋆ matrix**. Read the returned curve-list mode.

## Input fields

| Field | Accepted form |
|---|---|
| Rays | Integral primitive vectors, with comma-separated coordinates; separate rays by semicolons or newlines |
| Maximal cones | Zero-based ray indices, with commas within a cone and semicolons/newlines between cones |
| Complete intersection | One nontrivial nef divisor per row, with one coefficient per ray or coefficients on the displayed cohomology divisor basis |
| Curve class beta | A relation vector with one entry per ray, or coordinates in the displayed integral H2 basis |
| Insertions | Divisor polynomials such as `x0*x1`, the unit `one`, or ambient `pt`; separate insertions by `\|` |

For the fan of P²:

```text
Rays:           1,0;0,1;-1,-1
Maximal cones:  0,1;1,2;0,2
```

Enter only the contents after each label. The fan must define a supported smooth projective toric variety.

For P³, `K=3` describes a cubic surface. In the **One GW invariant** area, beta `1,1,1,1` and **empty insertions** return 27. No point insertion is used.

Different line-bundle summands use different rows: `2;3` gives O(2) plus O(3) on projective space. A divisor with negative ray coefficients can still be nef; the program checks its degrees on invariant curves. Trivial and nonnef defining divisors are rejected.

The **Projective bundle** tab accepts one divisor per summand of the ambient split bundle. These summands describe the projective-bundle target and are distinct from the later **Complete intersection** field.

## Novikov coordinates and spectrum controls

Describe the space first. The displayed cohomology divisor basis used by short K rows can differ from the chosen nef Novikov basis. Variables `y1,y2,...` follow the reported Novikov divisors, not the raw ray numbers.

Negative entries of an effective beta relation are permitted. If no nef integral Novikov basis is found, the fallback coordinates can give Laurent monomials. Do not replace this with a nonnegativity test on all ray entries.

**Novikov point for spectrum & cyclic determinant** analyzes the symbolic matrix at selected values; omitted variables equal one. Fractions, decimals, sqrt(...) and I are accepted. The symbolic matrix is retained. The optional eigenvalue selection refers to K=-c1⋆, including its sign. The interface reports unsupported factors without giving a rationality verdict.

**Update spectrum & cyclic determinant** reuses the previous matrix. After changing the target, K or curve list, compute a new matrix first.

## Curve-list scope

The result reports whether the automatic calculation uses positive ambient bounds, a conditional Mori search, automatically suggested Mori inequalities, or an ample-degree cutoff.

A cutoff matrix has exact coefficients within its selected region; it is not a complete infinite quantum series. A sampled check of suggested inequalities is evidence, not a proof of the target's Mori cone. User-supplied inequalities must hold on every target curve.

**Stop the running computation** requests cancellation. It is separate from closing the browser. Durability depends on the selected execution/checkpoint path; do not assume every standalone toric GUI job has the combined flag worker's completed-matrix storage.

## Python and CLI

```python
from gwtoric import projective_space

P2 = projective_space(2)
assert P2.gw([P2.pt, P2.pt], beta=(1,1,1)) == 1
M, grading, names = P2.small_quantum_multiplication(cache=False)
assert len(M) == len(names) == 3

P3 = projective_space(3)
assert P3.gw([], beta=(1,1,1,1), K=[[3]]) == 27
```

The toric API returns basis **names**, rather than the flag API's Schubert **indices**.

An explicit fan and supported Hodge data:

```python
from gwtoric import ToricVariety

P2 = ToricVariety([(1,0),(0,1),(-1,-1)], [(0,1),(1,2),(0,2)])
assert P2.divisor([3]) == P2.divisor([3,0,0])

P4 = projective_space(4)
assert P4.hodge_report([[3]])["hodge"][1][2] == 5
```

CLI rows use semicolons. Put ambient and K options before the subcommand:

```bash
python -m gwtoric.cli --preset P2 gw --beta 1,1,1 --classes "pt|pt"
python -m gwtoric.cli --preset P3 --K 3 gw --beta 1,1,1,1 --classes ""
python -m gwtoric.cli --preset P2 sqm --workers 1
```

## Reading results and mathematical scope

The matrix describes c1 multiplication on the returned ambient sector for complete intersections. Retain its basis, grading, Novikov divisors, curve list and completeness mode.

Ambient toric Hodge diamonds come from the fan. Full CI Hodge support is limited to dimensions 3–5 and requires the implemented ampleness and Fano checks to pass; separate Chern-number calculations have a wider supported scope. A supported GW input does not guarantee a supported full Hodge calculation.

## Troubleshooting

- Ray indices start at zero; flag root indices start at one.
- Use the displayed H2 basis for short beta vectors, and the displayed divisor basis for short K vectors.
- The ambient point class can restrict to zero on a lower-dimensional complete intersection.
- Leave insertions empty for an unmarked invariant; `one` means one marked unit insertion.
- Inspect warnings about truncation or Mori assumptions before treating a matrix as complete.

See [Notation and compatibility](notation.md) and [Changes](changes.md).


See [Input/output conventions](input-output.md) for result formats and [Version comparison](launch-2026-11.md) for the differences between distributions.
