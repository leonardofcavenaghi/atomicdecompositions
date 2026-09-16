# Website usage review — 16 September 2026

This review records the browser-facing input contract and the checks that keep
it aligned with the Python/CLI interfaces and the supplied paper. The generated
site is rebuilt from `docs/`; there is no separate hand-edited website copy.

## Input contract checked

| Area | Accepted website form | Check |
|---|---|---|
| Algebra | `A3`, `A3xA3`, `G2` | Validated by `FlagVariety` |
| Kept roots | comma-separated 1-based integers, e.g. `1,3` | Validated in Bourbaki order |
| Compact line bundles | `3`, `1,1;2,2` | Parsed as one row per summand |
| Paper bundle aliases | `O(1)`, `S(2)`, `Q(2)` and nested `osum`, `tensor`, `sym`, `wedge` | Bound to the current variety by a restricted AST parser |
| Explicit bundle constructors | `taut_quot(X,2)`, `dual(taut_sub(X,2))` | Same-variety and constructor checks |
| Empty K | blank | Means untwisted computation |
| GW insertions | `pt`, `id`, or space-separated reduced minimal words joined with `\|` | `Space Info` and **Add** buttons provide valid words |
| Curve class | one integer per kept root in the paper order, or a zero-padded ambient vector | Removed-root entries are rejected; output is canonical ambient order |
| Novikov assignments | `y1=1,y3=1` | Names use ambient node labels |

The website deliberately does not accept Mathematica/Python list notation such
as `[[3]]`. Python code uses the separate API form `K=[[3]]`.

## Examples checked

- `A2`, `keep=1`, beta `1`, `pt|pt`: one line through two points, value `1`;
  the equivalent ambient beta `1,0` gives the same result.
- `A3`, `keep=2`, beta `1` or `0,1,0`, insertions
  `2 1 3 2|1 3 2|pt`: the `Gr(2,4)` benchmark gives `1`.
- `A3`, `keep=1`, `K=3`, beta `1`, empty insertions: cubic-surface line count
  `27`.
- `A4`, `keep=1`, `K=5`, beta `1`, empty insertions: quintic line count
  `2875`.
- `A4`, `keep=2`, `K=Q(2)` or `taut_quot(X,2)`: quotient-bundle expression
  parses and reports rank `3`.
- `A6`, `keep=3`,
  `osum(wedge(2,dual(S(3))),wedge(3,Q(3)),O(1))`: the paper's Küchle c5
  bundle expression parses with rank `8` and first Chern coordinate `6`.
- Invalid nonreduced/nonminimal words, removed-root beta entries, nonconvex
  bundles, attribute access, cross-variety bundles, and malformed Novikov
  assignments produce readable errors.

## Documentation and rendering

[`docs/how-to-use.md`](../how-to-use.md) explains beginner and experienced
installation paths, the five inputs, paper aliases, kept/ambient beta forms,
copyable examples, bundle combinations, result interpretation, and
troubleshooting. The [API reference](../api-reference.md) gives the exact
method signatures and mathematical scope. The TeX/PDF paper template is in the
[theory-alignment addendum](theory-alignment-addendum.md).

## Repeatable checks

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_gui_api.py -q
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_catalog.py
mkdocs build --strict --site-dir /tmp/gwflags-website-check
```

The generated page contains the same field help as `gwflags.gui.PAGE`; the
catalog validator and strict build must pass before publishing.
