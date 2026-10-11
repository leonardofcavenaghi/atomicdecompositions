---
description: Download exact symbolic quantum multiplication matrices, ordered bases, gradings and supported curve classes for 131 completed localization computations.
---

# Download matrices and inputs

This download lets you reuse the matrices displayed in the catalog in Python, SageMath or other software, or repeat the computations from their original inputs. It includes the basis order and grading needed to interpret each matrix.

You can read the examples directly in the [catalog](index.md); the download is optional. **Exact** means that fractions and symbolic expressions are preserved instead of rounded decimal approximations.

The `fano_index` field uses the software’s ambient Chern-lattice convention; it need not be the intrinsic Fano index of a low-dimensional section. For example, a conic is `P1` with geometric index 2 even when the ambient gcd is 1. See [catalog conventions](index.md).

This collection contains **131 completed exact localization computations**, including **32 threefold realizations**. Different realizations are listed separately even when the resulting varieties are isomorphic.

[Download the complete JSON dataset](../data/localization-results.json)

Each record contains the executable algebra/kept-root/bundle input, the full automatically supported curve list in ambient coordinates, the symbolic $c_1(TY)$ multiplication matrix, its specialization at all $y_i=1$, the ordered Schubert basis, and the grading. Rational numbers are stored as exact strings. The matrix acts on the returned ambient sector, with columns as inputs and rows as outputs.

These are the same results displayed in the [catalog](index.md). See [Methods and conventions](../methodology.md) for their mathematical scope.

## Use a saved result

```python
import json
from pathlib import Path

data = json.loads(Path("localization-results.json").read_text())
example = next(r for r in data["examples"] if r["id"] == "e1322438fd01")
print(example["input"])
print(example["matrix_symbolic"])
print(example["basis_words"])
```

To recompute a record, construct `FlagVariety` with its algebra and kept roots, parse its bundle using the documented input syntax, and call `small_quantum_multiplication(K)` without restricting the automatic curve list.
