---
description: Download exact catalogue inputs, quantum matrices, ordered bases, gradings and atomic invariant data.
---

# Exact datasets

Download the exact inputs and results underlying the catalogue. Each dataset retains its coordinate conventions, ordered bases, gradings and specialization data.

| Dataset | Records | Contents |
|---|---:|---|
| [Original exact matrix dataset](../data/localization-results.json) | 131 | Root-system and bundle inputs, curve lists, symbolic and y=1 matrices, Schubert bases and grading |
| [Toric fourfolds](../data/toric-fourfolds.json) | 96 | Fans, defining divisors, Novikov divisors, sparse exact symbolic matrices, ordered ambient bases and grading |
| [Toric fivefolds](../data/toric-fivefolds.json) | 72 | Same fan/divisor contract, with construction data and connection analysis |
| [Regularized exponent multisets](../data/connection-exponents.json) | 168 | Exact power and residue-class multisets per characteristic factor, with specialization and unresolved status |
| [Additional homogeneous fourfolds](../data/flag-fourfolds.json) | 2 | Exact matrices, automatic curves, Schubert bases, cyclic determinants, connection multisets and generic atomic invariants |
| [Atomic Hodge invariants](../data/atomic-invariants.json) | 301 | Full Hodge data, exact point tests, determinants, factor scope and certified atomic polynomials |
| [Universal catalogue index](../data/catalog-records.json) | 301 | Canonical record links, dimension, recorded index, matrix rank and search terms |

The [fourfold computation notes](../downloads/toric-fourfolds-completed.tex) and [fivefold computation notes](../downloads/toric-fivefolds-completed.tex) contain the characteristic factors and connection exponents. Unresolved connection factors are marked explicitly.

Sources for the fourfold constructions include Coates–Kasprzyk–Prince, [1409.5030v3](https://arxiv.org/abs/1409.5030v3), and Hausen–Laface–Mauz, [1907.08000v3](https://arxiv.org/abs/1907.08000v3). CKP identifiers denote period buckets; equality of periods does not identify varieties up to isomorphism. The [fivefold page](fivefolds.md) describes its constructions.

The matrices act on the returned ambient sector. Their columns are images of the ordered basis; grading and Novikov maps are part of the data. Full Hodge numbers do not supply missing primitive quantum operators. Use the [root-system](../methodology.md) or [fan/divisor](../toric/mathematics.md) mathematical conventions for the relevant presentation, and the version-specific [software guides](../software/index.md) to reproduce its input.

Consistency checks of the stored matrices, gradings and characteristic polynomials do not rerun localization. [Original dataset usage](computed.md) gives a Python example for its schema.

Exponent multisets apply separately at each eigenvalue, with multiplicities retained. An unresolved factor has no assigned multiset. The original matrix dataset does not include connection exponents.

Full atomic Hodge polynomials require unit cyclicity, identification of the entire Hodge-invariant sector and a justified primitive-cohomology assignment. The [atomic invariants](atomic-invariants.md) state the hypotheses and distinguish full decompositions from partial ambient information.
