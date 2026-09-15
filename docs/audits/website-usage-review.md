# Website usage review — 15 September 2026

This review records the website-facing checks performed during the interface
and documentation update. It is deliberately kept beside the source so that
future interface changes can be checked against the same contract.

## Input contract checked

| Area | Accepted website form | Check |
|---|---|---|
| Algebra | `A3`, `A3xA3`, `G2` | Passed through `FlagVariety` |
| Kept roots | comma-separated 1-based integers, e.g. `1,3` | Passed through `FlagVariety` |
| Compact line bundles | `3`, `1,1;2,2` | Parsed as rows of integer multidegrees |
| Homogeneous bundles | `taut_quot(X,2)`, `taut_sub(X,2)` | Restricted constructor parser |
| Empty K | blank | Means untwisted computation |
| GW insertions | `pt`, `id`, or space-separated reduced words joined with `\|` | Empty input remains `[]` |
| Curve class | comma-separated integers, e.g. `1,0,0` | One coordinate per ambient simple root |

The website deliberately does not accept Mathematica/Python list notation
such as `[[3]]`. Python code uses the separate API form `K=[[3]]`.

## Examples checked

- `A3`, `keep=1`, `K=3`, `beta=1,0,0`, empty insertions: cubic surface,
  invariant `27`.
- `A4`, `keep=1`, `K=5`, `beta=1,0,0,0`, empty insertions: quintic
  threefold, invariant `2875`.
- `A3`, `keep=2`, no `K`, `beta=0,1,0`, insertions
  `2 1 3 2|1 2|3 2`: `Gr(2,4)` invariant `1`.
- `A4`, `keep=2`, `K=taut_quot(X,2)`: quotient bundle expression parses as a
  `HomogeneousBundle`.
- Empty insertion syntax returns `([], [])`; it does not insert the identity.

## Documentation changes

`docs/how-to-use.md` now documents the five core inputs, compact versus Python
bundle syntax, insertion parsing, copyable examples, quotient bundles,
command-line equivalents, and troubleshooting. The guide describes the
current local server URL and the actual result panels.

## Repeatable checks

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 /home/leonardofcavenaghi/miniconda/bin/python3 - <<'PY'
from gwflags.gui import parse_k, parse_classes
from gwflags import FlagVariety
X = FlagVariety('A4', [2])
assert parse_k('taut_quot(X,2)', X).rank == 3
assert parse_classes('', X) == ([], [])
PY
python3 -m mkdocs build --strict --site-dir /tmp/gwflags-docs-check
```

The parser assertions passed and the strict documentation build completed.
