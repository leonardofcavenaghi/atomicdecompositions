---
description: Exact downloadable inputs, matrices, bases and gradings for all 301 saved catalogue computation records.
---

# Exact datasets and source records

The catalogue is organized by geometry. Downloads retain their original schemas so that no coordinate map, basis order or specialization is silently changed. There are 301 computation records across the four primary datasets, without a claim that they describe distinct varieties.

| Dataset | Records | Contents |
|---|---:|---|
| [Original exact matrix dataset](../data/localization-results.json) | 131 | Root-system and bundle inputs, curve lists, symbolic and y=1 matrices, Schubert bases and grading |
| [New fourfold records](../data/toric-fourfolds.json) | 96 | Fans, defining divisors, Novikov divisors, sparse exact symbolic matrices, ordered ambient bases and grading |
| [New fivefold records](../data/toric-fivefolds.json) | 72 | Same fan/divisor contract, with construction data and saved analysis notes in the linked records |
| [Regularized exponent multisets](../data/connection-exponents.json) | 168 | Exact saved power and residue-class multisets per characteristic factor, with specialization and unresolved status |
| [Additional homogeneous fourfolds](../data/flag-fourfolds.json) | 2 | Fresh exact matrices, automatic curves, Schubert bases, cyclic determinants, connection multisets and generic atomic invariants |
| [Atomic and Hodge invariant audit](../data/atomic-invariants.json) | 301 | Derived view: full Hodge data, exact point tests, determinants, factor scope and certified atomic polynomials |
| [Universal catalogue index](../data/catalog-records.json) | 301 | Canonical record links, dimension, recorded index, matrix rank and search terms |

The [completed fourfold TeX source](../downloads/toric-fourfolds-completed.tex) and [completed fivefold TeX source](../downloads/toric-fivefolds-completed.tex) retain the full saved calculation notes, characteristic factors and connection exponents. Unfinished matrix records are removed. A completed matrix can have unresolved connection factors; those notes are preserved.

The fourfold source follows Coates–Kasprzyk–Prince, [1409.5030v3](https://arxiv.org/abs/1409.5030v3), and Hausen–Laface–Mauz, [1907.08000v3](https://arxiv.org/abs/1907.08000v3). CKP IDs are period buckets, not an assertion of isomorphism. Fivefold construction sources and evaluation counts are stated on the [fivefold page](fivefolds.md).

The matrices act on the returned ambient sector. Their columns are images of the ordered basis; grading and Novikov maps are part of the data. Full Hodge numbers do not supply missing primitive quantum operators. Use the [root-system](../methodology.md) or [fan/divisor](../toric/mathematics.md) mathematical conventions for the relevant presentation, and the version-specific [software guides](../software/index.md) to reproduce its input.

These are saved outputs. Exact consistency checks of their gradings and characteristic polynomials do not rerun localization. [Original dataset usage](computed.md) gives a Python example for its schema.

The exponent summary contains 251 completed factor multisets and 92 unresolved factors. All factors are complete in 77 records; the other 91 records preserve their unresolved sectors. Multiplicities are retained separately at each eigenvalue. No exponent lists are invented for the original dataset, which does not store them.

The derived exponent and atomic views do not add new localization records to the catalogue count. The atomic view certifies 147 full decompositions under their stated hypotheses; 46 cyclic ambient matrices have a larger full Hodge-invariant space, and 108 records did not yield unit cyclicity at the tested points.
