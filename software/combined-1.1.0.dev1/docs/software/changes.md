---
description: Behavior changes in the versioned standalone and combined development distributions.
---

# Version differences

These changes belong to development versions 1.0.6.dev0 and 1.1.0.dev1; they do not create a new stable tag. The preserved original flag release remains v1.0.5.

## Flag versions 1.0.6.dev0 and 1.1.0.dev1

- Default parameter names retain ambient nodes in type A and use consecutive kept-root labels for other families. The rank-one C3/keep 3, G2/keep 2 and D5/keep 4 examples therefore use y1.
- Python, CLI and interface expose the paper, ambient and compact conventions. The old names remain available explicitly; results record the selected mapping.
- Exact localization coefficients, beta vectors, basis ordering and grading are preserved under relabeling.
- Empty CLI insertion text now represents zero insertions. The unmarked cubic-surface line count is 27; no point insertion is needed.
- The standalone flag interface displays bundle rank and corrects its worker and quotient-validation help.
- The quartic-threefold preset now recommends describing the space, rather than an unmarked line calculation with a misleading benchmark hint.

## Combined version 1.1.0.dev1

- Completed flag matrix caches include the naming convention and mapping; matrices saved under different conventions cannot be confused.
- Toric input syntax and parameter names are retained. Interface wording distinguishes an automatic curve list from a guaranteed complete list.

## Validation

Fresh small quantum matrices were compared with the original source under legacy labels, including their exact entries, beta lists, bases and gradings. Paper-label versions were checked by exact symbolic substitution. Python documentation examples, empty-insertion CLI calls, flag/toric computation jobs, cached flag analysis and generated interface JavaScript were exercised locally.

A full browser/HTTP run was unavailable because the local execution sandbox does not permit sockets. The interface checks used its generated JavaScript and actual backend job functions. The deployment pipeline requires regression, clean-install and browser checks against the exact source archives before the website is deployed.


## Verified upstream execution updates

The prepared flag builds incorporate the unmarked tree generator from upstream commit 7f167e1. Exact representatives, vertex labels and ordering agree with legacy enumeration through six edges. The combined flag workspace also uses the new exact large-fraction checkpoint format. Ordinary old decimal checkpoints remain readable; newly tagged large values require the updated reader.

## Completed local checks

After the upstream execution update, 74 standalone flag tests passed in each prepared flag copy (one socket-dependent HTTP test excluded), 133 toric regression checks passed, and 19 toric Hodge/spectrum tests passed. The prepared combined runtime passed 19 worker/routing/subprocess checks. Clean-install, launcher and browser checks run in the GitHub deployment gate; the local worker checks alone do not establish live browser coverage.
