# How to use `gwflags`

`gwflags` computes Gromov–Witten invariants and small quantum multiplication for flag varieties `G/P` and supported complete intersections. The browser interface is the easiest starting point; the Python and CLI interfaces are documented later.

## Install and launch

### If you already use Python

From the repository root:

```bash
python3 -m pip install -e .
python3 -m gwflags.gui --no-browser
```

Open <http://127.0.0.1:8642>. Use `--port 9000` if that port is occupied.

### If Python is new to you

Install Python 3.9 or newer (Python 3.10+ is recommended), open a terminal in the downloaded repository, and run the same two commands above. The GUI uses only the Python standard library plus the packages declared by the project. If `python3` is unavailable on Windows, use `py -m pip` and `py -m gwflags.gui --no-browser`.

The server is local to your computer (`127.0.0.1`). Stop it with `Ctrl-C` in the terminal.

## Fastest path: load an example

1. Choose an item from **Preset library**.
2. Read the recommended action and expected result shown below the selector.
3. Click **Describe this space**, **Compute quantum matrix**, or **Compute one GW invariant** as recommended.
4. Follow progress in the status and log areas. Large index-1 examples can take several minutes.

The preset fills every dependent field, so an old β or insertion cannot accidentally remain in a new example.

## The five core inputs

- **Lie algebra**: `A3`, `B2`, `C3`, `D5`, `G2`, or a product such as `A3xA3`.
- **Kept simple roots**: comma-separated Bourbaki node numbers, for example `1` for projective space or `2` for `Gr(2,4)` in type `A3`.
- **Bundle K** (optional): leave blank for `G/P`; enter `3` for `O(3)`, or
  `1,1;2,2` for two line-bundle summands when the variety has two kept roots
  (use `1;2` on a Picard-rank-one variety). You can also enter
  `taut_quot(X, 2)` for a quotient bundle. The GUI uses compact text: Python
  API notation such as `[[3]]` is not valid in this field.
- **Curve class β**: one nonnegative integer per ambient simple root, such as `1,0,0` for lines on the cubic surface.
- **Insertions**: `pt`, `id`, or space-separated reduced Weyl words separated by `|`. You can click **Add** beside a basis word in Space Info instead of typing it.

`Evaluate y` is optional and applies to quantum matrices only. Leave it blank for symbolic Novikov variables, or enter assignments such as `y1=1,y2=1`.

## Copyable examples

### Beginner path: direct flags and products

For an untwisted direct flag, leave `K` blank. For example, `A2` with
kept roots `1` is `P²`; choose **Describe this space** first, then choose
**Compute quantum matrix**. A product flag can be entered in the same form:
`A1xA1`, kept roots `1,2`, and blank `K` describes `(P¹)²`.

### Advanced path: bundle expressions and GW insertions

After **Space Info** displays the Schubert basis, use its **Add** controls to
build a valid insertion list. This avoids having to know reduced Weyl words in
advance. For a homogeneous bundle, first describe the space with the bundle
expression, then run the desired matrix or invariant action.
`taut_quot(X, 2)` is directly convex on `A4`, kept roots `2`. The parser also
accepts `taut_sub(X, 2)`, but its negative splitting degrees make the
untwisted genus-0 theory reject that direct computation; use
`dual(taut_sub(X, 2))` for the convex dual bundle.

| Goal | Algebra | Kept roots | K | β / insertions |
|---|---|---|---|---|
| `P²` matrix | `A2` | `1` | *(blank)* | matrix action |
| evaluated `P²` matrix | `A2` | `1` | *(blank)* | matrix action with `Evaluate y: y1=2` |
| product flag info | `A1xA1` | `1,2` | *(blank)* | info action |
| 27 lines on a cubic surface | `A3` | `1` | `3` | β `1,0,0`, insertions blank |
| 2875 lines on a quintic | `A4` | `1` | `5` | β `1,0,0,0`, insertions blank |
| `Gr(2,4)` invariant | `A3` | `2` | *(blank)* | β `0,1,0`; `2 1 3 2|1 2|3 2` |
| quotient bundle | `A4` | `2` | `taut_quot(X, 2)` | describe or matrix action |
| convex dual subbundle | `A4` | `2` | `dual(taut_sub(X, 2))` | describe action |

## Reading results

**Space Info** reports dimension, Fano index, first Chern class, number of curve classes, and the Schubert basis. Use the **Add** buttons to build insertion lists.

**Quantum matrix** reports the matrix, grading, characteristic polynomial, and numerical eigenvalues only when all Novikov variables are specialized to one. A custom `Evaluate y` value is reported separately and does not claim to be the `y=1` spectrum.

**GW invariant** reports the insertion list, β, and the computed number.

## Advanced bundle syntax

Supported constructors include `taut_quot(X, k)`, `taut_sub(X, k)`, `dual(...)`, `osum(...)`, `tensor(...)`, `sym(...)`, and `wedge(...)`. Use the GUI help text for compact line-bundle rows. Nested lists such as `[[3]]` belong to the Python API only.

## Troubleshooting

- Check that kept roots are valid, distinct node numbers in the algebra and in the intended order.
- β must have one entry per ambient simple root.
- Insertion words must contain integers separated by spaces; separate multiple insertions with `|`.
- A catalog entry marked **Catalog only** is not represented by the current flag-variety/complete-intersection input model.
- If a computation is slow, lower the worker count or start with a preset of lower degree.

## Python and CLI

```python
from gwflags import FlagVariety
X = FlagVariety('A3', [1])
print(X.gw([], beta=(1, 0, 0), K=[[3]]))  # 27
```

For the CLI, put bundle options before the subcommand:

```bash
python3 -m gwflags.cli A3 --keep 1 -K 3 sqm
```

## Bundle combinations: detailed walkthroughs

All bundle examples below use the same ambient variety:
`X = Gr(2,5)`, entered as algebra `A4` with kept roots `2`. Begin with
**Describe this space** to confirm the basis and dimension. Then enter one of
the following expressions in **Bundle K** and choose **Compute quantum matrix**
or **Describe this space**.

### 1. Quotient bundle

GUI input:

```text
taut_quot(X, 2)
```

This is the rank-3 tautological quotient bundle. Leave `Evaluate y` blank for
symbolic variables, or use `y2=1` for specialization. The result summary shows
`K=taut_quot(X, 2)` and the matrix is computed using the quotient-bundle twist.

Equivalent Python:

```python
from gwflags import FlagVariety
from gwflags.bundles import taut_quot

X = FlagVariety('A4', [2])
Q = taut_quot(X, 2)
M, grading, basis = X.small_quantum_multiplication(K=Q)
```

### 2. Dual of the tautological subbundle

The subbundle itself is generally not convex for the twisted genus-0 theory.
Use its dual instead:

```text
dual(taut_sub(X, 2))
```

Equivalent Python:

```python
from gwflags.bundles import taut_sub, dual
K = dual(taut_sub(X, 2))
M, grading, basis = X.small_quantum_multiplication(K=K)
```

The GUI accepts the expression, while a direct `taut_sub(X, 2)` computation
may be rejected when its curve splitting degrees are negative.

### 3. Direct sum of bundles

Use `osum` to combine summands. This example combines the rank-3 quotient with
a line bundle `O(1)` on this Picard-rank-one Grassmannian:

```text
osum(taut_quot(X, 2), O(X, 1))
```

On `Gr(2,5)` there is one kept node, so `O(X, 1)` takes one degree. A
two-entry constructor such as `O(X, 1, 1)` belongs on a two-generator product
(for example `A2xA2`, kept roots `1,3`). In the compact GUI syntax, separate
summands are written as rows such as `1;2`.

Python:

```python
from gwflags.bundles import O, osum, taut_quot
K = osum(taut_quot(X, 2), O(X, 1))
print(K.rank)  # 4
```

### 4. Tensor product

`tensor` forms all pairwise sums of fiber weights:

```text
tensor(taut_quot(X, 2), O(X, 1))
```

Python:

```python
from gwflags.bundles import O, tensor, taut_quot
K = tensor(taut_quot(X, 2), O(X, 1))
print(K.rank)  # 3
```

### 5. Symmetric and exterior powers

These constructors derive new bundles from a homogeneous bundle:

```text
sym(2, taut_quot(X, 2))
wedge(2, taut_quot(X, 2))
```

The first has rank 6 and the second rank 3. In Python:

```python
from gwflags.bundles import taut_quot, sym, wedge
Q = taut_quot(X, 2)
print(sym(2, Q).rank)    # 6
print(wedge(2, Q).rank)  # 3
```

### Combining several operations

Expressions can be nested, provided every component is built on the same
`X`:

```text
osum(
  tensor(taut_quot(X, 2), O(X, 1)),
  wedge(2, dual(taut_sub(X, 2)))
)
```

For long expressions, Python is easier to read and debug. The GUI parser only
allows the documented constructors and rejects arbitrary Python code.

### What to check before computing

1. Confirm that every component uses the same algebra and kept nodes.
2. Use **Describe this space** first; it reports the resulting bundle rank.
3. Ensure the combined bundle is curvewise convex for the requested twisted
   computation. A non-convex bundle is reported as an error rather than being
   silently accepted.
4. Start with symbolic `y` variables. Specialize with `Evaluate y` only after
the symbolic matrix has been assembled.
