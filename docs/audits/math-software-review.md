# Mathematics and software audit

This report records the independent review of the maintained website catalog,
its examples, and the `gwflags` implementation. The catalog validator and the
software tests are intended to be rerun whenever a generated page or core
algorithm changes.

## Mathematical checks

- Every maintained Projective card satisfies
  `dimension = n - number of line-bundle rows` and
  `Fano index = n + 1 - sum(degrees)`. The displayed square-matrix size agrees
  with its Basis Rank for all 54 cards.
- Every maintained Grassmannian card satisfies
  `dimension = k(n-k) - number of line-bundle rows` and
  `Fano index = n - sum(degrees)`. The displayed square-matrix size agrees with
  its Basis Rank for all 51 cards.
- The Fanography cards 1-5 through 1-9 now use inputs matching their stated
  homogeneous spaces. Fanography 2-24 is the `(1,2)` divisor in `P2 x P2`,
  and 4-1 contains the audited matrix entry in row 2, column 9 equal to `2`.
- Fanography 2-32 is explicitly labelled symbolic because its matrix contains
  `y1` and `y2`; it is not presented as a matrix evaluated at `y=1`.
- Fanography 1-10 now records the supported homogeneous-bundle input on
  `Gr(3,7)`: three copies of `wedge(2, dual(taut_sub(X, 3)))`. Its dimension,
  index, rank, and convexity were checked, while its quantum matrix is clearly
  marked pending independent recomputation rather than presented as verified.

The catalog also distinguishes entries outside the current flag-variety and
ordinary complete-intersection model (weighted spaces, double covers, and
blow-ups) as **Catalog only**.

## Independent functionality checks

The software review exercised the complete test suite, GUI presets, CLI/Python
examples, quotient bundles, dual/subbundles, direct sums, tensor products,
symmetric and exterior powers, and nested bundle expressions. The documented
reference values include:

- one line through two points in `P1` and `P2`: `1`;
- one conic through five points in `P2`: `1`;
- the corrected `Gr(2,4)` degree-one example: `1`;
- 27 lines on the cubic surface and 2875 lines on the quintic threefold;
- quotient-bundle sections on `Gr(2,4)` and `Gr(2,5)`, agreeing with `P2` and
  `P3` quantum matrices respectively.

The GUI and CLI reject malformed vectors, invalid reduced words, nonconvex
bundles, attributes in bundle expressions, cross-variety bundle combinations,
non-kept tautological nodes, and invalid symmetric/exterior degrees with
user-readable errors.

## Reproduce the review

From the repository root:

```bash
python3 scripts/validate_catalog.py
python3 -m pytest tests/ -q
mkdocs build --strict
```

The category pages explain how to translate each displayed card into the
`A(n)`/kept-root/Bundle-K fields. The [How to use](../how-to-use.md) guide
contains copyable GUI, Python, and CLI examples.
