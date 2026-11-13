---
description: Geometric names, exact fan identifications and the meaning of CKP and HLM catalogue identifiers.
---

# Geometric descriptions and source identifiers

Examples are displayed by their geometric construction whenever it has been established: projective spaces, complete intersections in products, and projectivizations of explicit split bundles. CKP and HLM remain reference identifiers and searchable aliases.

**CKP** means Coates–Kasprzyk–Prince, [*Four-dimensional Fano toric complete intersections*](https://arxiv.org/abs/1409.5030). The CKP numbers used here refer to period buckets in their dataset of presentations. Equal periods alone do not identify varieties.

**HLM** means Hausen–Laface–Mauz, [*On smooth Fano fourfolds of Picard number two*](https://arxiv.org/abs/1907.08000). HLM numbers refer to cases in their classification. For example, HLM-29 is the Verra fourfold.

The explicit projective-space, product and split-projective-bundle descriptions in this catalogue are verified from the saved fan: primitive collections, maximal cones, an integral cone basis and divisor linear equivalences. See the [certificates](../data/geometric-presentations.json). These checks identify the presentation; they do not rerun its localization computation or automatically identify all repeated presentations.

For a projective bundle we use the quotient convention, with tautological class xi and the displayed base hyperplane classes. The defining divisor classes are transformed from the original full ray-coefficient rows. Twisting every summand by the same line bundle does not change the projectivization; the displayed normalized summands use this equivalence.

A fan presentation that has not been identified by these checks retains its source identifier and full fan/Cox inputs. Such an entry is not silently assigned an unverified projective-bundle description.
