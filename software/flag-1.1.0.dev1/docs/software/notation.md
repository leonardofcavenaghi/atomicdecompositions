---
description: Parameter naming, beta coordinates and compatibility choices for the flag and toric engines.
---

# Notation and compatibility

The prepared flag builds default to Paper notation. Naming is separate from the curve lattice and does not change any localization coefficient.

| Target family | Default paper labels | Example |
|---|---|---|
| All factors of type A | Ambient Bourbaki node labels | A4/keep 2 uses y2; A2xA4/keep 1,3 uses y1,y3 |
| Other root-system families | Consecutive labels in the entered kept-root order | C3/keep 3, G2/keep 2 and D5/keep 4 each use y1 |

For mixed-family targets not illustrated above, Paper notation follows the second row: consecutive labels in entered kept-root order. Read the returned mapping rather than guessing a variable name.

Choose the convention explicitly in Python:

```python
from gwflags import FlagVariety

X = FlagVariety("C2", [2])
assert X.novikov_names == ("y1",)
assert X.novikov_metadata["variables"] == [{"node":2,"name":"y1"}]

old = FlagVariety("C2", [2], novikov_convention="ambient")
assert old.novikov_names == ("y2",)
```

The accepted conventions are paper, ambient and compact. Ambient preserves the previous names for every family. Compact uses consecutive kept-root labels for every family, including type A. The CLI exposes `--novikov-convention`; the flag interface exposes **Novikov notation**. Results record the selected convention and node-to-variable map.

Flag beta vectors retain their original meanings under all three choices: kept-root order, or an ambient-root vector zero off the kept nodes. Bases and gradings are preserved.

Toric variable names remain unchanged. They follow the reported Novikov divisor basis; short K rows use the displayed cohomology divisor basis. These bases can differ. A beta relation still has one entry per ray and may contain negative entries.

The preserved original v1.0.5 software retains ambient-node labels. It does not have the new selector or constructor option. Use its [legacy guide](flags-legacy.md) when reproducing archived calculations.

