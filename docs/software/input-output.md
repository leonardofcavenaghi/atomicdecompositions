---
description: Exact input and output conventions for Python, CLI, flag and toric forms, matrices, selected-point analysis and exported results.
---

# Input and output conventions

This reference covers flag 1.0.6.dev0 and the flag, toric and combined 1.1.0.dev1 distributions. The [preserved v1.0.5 guide](flags-legacy.md) describes the archived runtime separately.

Run the examples using both Python APIs in the complete combined installation, which contains both APIs. The dedicated flag guide provides flag-only examples for the standalone flag installation.

Exact input/output examples are available for [flags 1.0.6.dev0](examples/io-1.0.6.json) and [flag, toric and combined 1.1.0.dev1](examples/io-1.1.0.json). Runtimes in those records are incidental and can vary.

## 1. Geometric inputs

| Item | Flag Python API | Flag form / CLI | Toric Python API | Toric form / CLI |
|---|---|---|---|---|
| Ambient target | FlagVariety("A3",[1]) | Algebra A3; keep 1 | projective_space(3), or ToricVariety(rays,cones) | Product/preset P3, or explicit fan |
| Node/ray numbering | 1-based kept root nodes | Same | 0-based ray indices | Same |
| Cubic defining bundle | K=[[3]], or O(X,3) | K field 3 or O(3); CLI -K 3 | K=[[3]] in the displayed divisor basis | Complete intersection 3; CLI --K 3 |
| Unmarked insertions | [] | Empty field; --classes "" | [] | Empty field; --classes "" |
| Cubic line beta | (1,) in kept-root order | 1 | (1,1,1,1) as a ray relation | 1,1,1,1 |
| One unit insertion | [X.schubert(())] | id or e | [T.one] | one |

Commas separate entries of a vector. Semicolons separate bundle summands or fan rows. Insertion expressions are separated by `|`. Flag words use spaces between simple-reflection labels; toric insertions are polynomials such as x0*x1.

The toric interface also accepts newlines between fan/divisor rows. The toric CLI uses semicolon-separated rows. Python lists and explicit ambient arguments belong to Python; a form field does not accept a nested list such as [[3]].

For flags, an ambient-root beta vector is also accepted when it is zero off the kept roots. For toric targets, coordinates in the displayed integral H2 basis are an alternative to the full ray relation. These alternatives must be read from the relevant engine, rather than inferred from the number of displayed parameters.

## 2. Example: the 27 lines on a cubic surface

Python:

```python
from fractions import Fraction
from gwflags import FlagVariety
from gwtoric import projective_space as toric_projective_space

F = FlagVariety("A3", [1])
T = toric_projective_space(3)

flag_value = F.gw([], beta=(1,), K=[[3]])
toric_value = T.gw([], beta=(1,1,1,1), K=[[3]])

assert flag_value == toric_value == 27
assert isinstance(flag_value, Fraction)
assert isinstance(toric_value, Fraction)
```

These are unmarked calculations: there are no point insertions.

Flag CLI:

```bash
python -m gwflags.cli A3 --keep 1 -K 3 gw --beta 1 --classes ""
```

Expected stdout:

```text
beta = [1, 0, 0]  # ambient node order
GW invariant = 27
```

Toric CLI:

```bash
python -m gwtoric.cli --preset P3 --K 3 gw --beta 1,1,1,1 --classes ""
```

Expected stdout:

```text
beta = [1, 1, 1, 1]  (c1.beta = 1 on Z)
GW invariant = 27
```

In either flag interface, use algebra A3, kept root 1, bundle 3, beta 1 and an empty insertion field. In the toric interface, choose the product P3, set Complete intersection to 3, beta to 1,1,1,1 and leave insertions empty.

An interface serializes the scalar as a string, "27", preserving exact rational spelling. A nonintegral rational uses a fraction string rather than a rounded decimal. Numerical spectra use numerical fields separately.

The standalone flag result includes:

```json
{
  "value": "27",
  "insertions": [],
  "beta_input": [1],
  "beta": [1, 0, 0],
  "bundle_rank": 1
}
```

The toric result instead contains beta [1,1,1,1], c1_beta 1 and Novikov exponent list [1]. The combined flag worker returns value, insertions, canonical beta, evaluation count and its parameter map; it does not promise every standalone flag field. The full subprocess result adds the submitted input and runtime.

Result fields depend on the interface and engine.

## 3. Quantum matrix outputs

The Python APIs return different third components:

```python
P2_flag = FlagVariety("A2", [1])
P2_toric = toric_projective_space(2)

FM, FG, indices = P2_flag.small_quantum_multiplication()
TM, TG, names = P2_toric.small_quantum_multiplication(cache=False)

assert indices == [0,1,2]
assert names == ["1","x0","x0^2"]
assert [[str(v) for v in row] for row in FM] == [
    ["0","0","3*y1"], ["3","0","0"], ["0","3","0"]
]
assert [[str(v) for v in row] for row in TM] == [
    ["0","0","3*y1"], ["3","0","0"], ["0","3","0"]
]
```

| Output | Flag | Toric |
|---|---|---|
| M | Matrix of multiplication by c1 in the returned ambient sector | Same operator type in its toric ambient basis |
| G | Full square diagonal grading matrix in the Python API | Full square diagonal grading matrix |
| Third return value | Zero-based indices into X.classes and X.class_words() | Names of the returned divisor-monomial basis |
| Interface matrix | Array of expression strings | Array of expression strings |
| Interface grading | Diagonal entries, rather than a second displayed full square matrix | Diagonal entries |
| Interpretation | Input columns, output rows | Input columns, output rows |

For the P2 example the diagonal grading is [-1,0,1]. The basis labels and parameter maps must accompany a matrix, even when two displayed matrices happen to agree.

A flag basis index is not a root number. A toric basis name is not a curve coordinate. A numerical eigenvalue list is not a substitute for either basis.

## 4. Parameter names and the two meanings of novikov

Flag names follow the selected convention: paper by default, ambient for the old node names, or compact for consecutive labels in every family.

For C3/keep 3, the default parameter is y1; ambient gives y3. Type A retains node labels by default. Describe the space or read X.novikov_metadata before entering a specialization.

The flag result's novikov field is a metadata object. For example:

```json
{
  "convention": "paper",
  "variables": [{"node": 1, "name": "y1"}],
  "beta_coordinates": "kept-root order or zero-padded ambient roots"
}
```

The toric scalar-GW result's novikov field is instead the exponent list of the current beta. Its matrix/info results report the Novikov divisor basis. The same field name therefore does not mean the same data type across the two engines.

In toric mode, short K rows use the displayed cohomology divisor basis, while quantum monomials use the reported Novikov divisors. These bases can differ. Effective relation vectors can have negative entries; fallback quantum coordinates can produce Laurent monomials.

## 5. Symbolic matrices and Novikov specializations

| Launch mode | Blank evaluation field | Custom assignment |
|---|---|---|
| Standalone flag GUI | Returns a symbolic matrix and separately attempts the y=1 numerical spectrum | Substitutes into the returned matrix/characteristic polynomial; suppresses that separate numerical spectrum |
| Enhanced combined flag workspace | Retains the symbolic matrix; analysis defaults omitted parameters to 1 | Retains the symbolic matrix and analyzes the selected exact point |
| Toric workspace | Retains the symbolic matrix; analysis defaults omitted parameters to 1 | Retains the symbolic matrix and analyzes the selected point |

The combined flag **Update spectrum & exponents** action reuses a completed matrix for matching inputs. The toric **Update spectrum & cyclic determinant** action reuses its previous matrix; changing the geometry, bundle or curve list requires computing a new one.

Flag exact exponent analysis currently requires rational specialized entries. Unsupported sectors remain unresolved. Connection eigenvalue selection uses K=-M, so its sign differs from multiplication eigenvalues.

Characteristic-polynomial text uses a mathematical symbol named lambda. It is display text, not a Python lambda expression to paste directly into source code.

## 6. What to retain with a result

For reproducibility, keep:

- The program version and source revision.
- Ambient target, bundle, beta or full quantum curve list, and insertion input.
- Selected flag naming convention, or the toric divisor/Novikov basis.
- Ordered basis and grading.
- Symbolic versus specialized matrix status and the exact evaluation point.
- Curve-list completeness mode and any cutoff or geometric inequalities.
- Evaluation count where configurable.
- The exact scalar or matrix expressions, with numerical spectra clearly identified as numerical.

The flag toolbar provides copied input JSON and downloadable result JSON. The toric interface has its own controls; it does not share every flag toolbar action. Its Python API can be used to save a result with the relevant metadata.

Checkpoints store execution state; use a result export for the mathematical output. Newly tagged large-fraction checkpoints require the updated reader.

## 7. Mathematical interpretation

For complete intersections, the returned matrix is the supported ambient operator; a Hodge diamond does not provide a primitive quantum basis. The curve list may be complete under the stated positivity assumptions, conditional on additional geometry, or truncated at an ample degree.

The flag degree-zero API deliberately has a classical cup-integral shortcut, including unstable pairing inputs. The toric degree-zero GW entry path returns the classical integral only for three insertions meeting its dimension check; other insertion counts return zero. These conventions should not be described as identical degree-zero GW definitions.

Use [flag 1.0.6.dev0 guide](flags-1.0.6.md), [version 1.1.0.dev1 flag guide](flags-1.1.0.md), [toric guide](toric-1.1.0.md), and [combined guide](combined.md) for the actual controls and supported operations.

