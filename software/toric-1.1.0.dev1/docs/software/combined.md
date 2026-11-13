---
description: Install and launch the combined local application, choose a geometry, and use its separate flag and toric workflows.
---

# How to use the combined software

The combined development build `1.1.0.dev1` starts one local application with separate flag and toric workspaces. It is distributed as a development source bundle; no new stable tag is implied. Its two input formats follow their respective guides.

## Launch the interface

Install the complete source bundle using [Installation](../installation.md), then run:

```bash
python -m gwapp --workspace ./gw-work --no-browser
```

Open <http://127.0.0.1:8650>. Choose **Flag varieties** or **Toric varieties**. Use a writable workspace, and a separate workspace for each running combined server. Keep it between runs to retain flag checkpoints.

To choose another port:

```bash
python -m gwapp --port 8651 --workspace ./gw-work-8651 --no-browser
```

The installed `gw-combined` command starts the same server. On Windows, the provided launcher starts the application with its default workspace; the command above gives explicit control of its location.

## Choose the appropriate input guide

| Workspace | Target description | Input guide |
|---|---|---|
| /flag/ | Root system, 1-based kept roots, line or supported homogeneous bundles | [version 1.1.0.dev1 flag guide](flags-1.1.0.md) |
| /toric/ | Fan or toric constructors, 0-based rays, nef divisor rows | [Toric guide](toric-1.1.0.md) |

The two workspaces share infrastructure but keep different cohomology and curve-coordinate models. A type A name is not a substitute for a toric fan, and toric ray coordinates are not flag beta coordinates.

## Copyable first calculations

For unmarked cubic-surface lines in the flag workspace:

```text
Lie algebra:       A3
Kept simple roots: 1
Bundle K:          3
Curve class beta:  1
Insertions:        [leave empty]
```

Click **Compute one GW invariant**. The answer is 27.

For one line through two points in the toric workspace, choose P2, enter beta `1,1,1` and insertions `pt|pt`, then click **Compute invariant**. The answer is 1.

## Flag computations and saved progress

The flag workspace adds two-stage saved localization, evaluation-count controls, Hodge diamonds, cancellation, completed-matrix reuse and exact spectrum/exponent analysis.

Use two exact evaluations for the agreement check. Worker 1 is serial; worker 0 selects automatic allocation on the configured path, capped at 12. The process can be stopped through **Stop calculation**. Repeating the same inputs resumes committed flag tree work.

After **Compute quantum matrix** completes, **Update spectrum & exponents** uses the saved symbolic matrix at the selected Novikov values. Omitted values equal one. Naming conventions are included in the matrix-cache identity, so legacy and paper labels do not silently share a completed symbolic matrix.

The flag **Novikov notation** selector defaults to Paper notation; see [Notation](notation.md).

## Toric computations

The toric workspace retains its own fan/product/projective-bundle tabs, curve-list controls, Hodge support, cancellation and spectrum updates. It delegates to the toric engine. Read the reported completeness mode and the [toric guide](toric-1.1.0.md); do not assume all flag persistence controls apply to toric jobs.

## Python interfaces

The combined installation retains the two Python APIs:

```python
from gwflags import FlagVariety
from gwtoric import projective_space

F = FlagVariety("A3", [1])
T = projective_space(3)
assert F.gw([], beta=(1,), K=[[3]]) == 27
assert T.gw([], beta=(1,1,1,1), K=[[3]]) == 27
```

Flag matrices return Schubert basis indices; toric matrices return basis names. Keep each result with its own grading and coordinate map.

## Reading results and scope

A Hodge diamond supplies dimensions, not missing primitive quantum operators. Exponent analysis can be partial and does not infer a rationality verdict in this application. The scientific interpretation of a complete-intersection matrix still requires the stated smoothness, convexity, curve-list and ambient-sector assumptions.

## Troubleshooting

- Stop the server with Ctrl-C after stopping active computations.
- If a completed flag matrix is unavailable, compute it before requesting analysis.
- Use the same geometry, bundle, evaluation count and notation to reuse that flag matrix.
- Keep independent installations in separate virtual environments: both flag distributions use the package name `gwflags`.
- Do not identify exact arithmetic with exhaustive curve enumeration.

See [Changes](changes.md) for the explicit behavior changes.


For the common conventions and concrete result examples, see [Input/output](input-output.md). The [upcoming release overview](launch-2026-11.md) explains the differences between the offerings.
