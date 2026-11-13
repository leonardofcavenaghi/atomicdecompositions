# Contributing to GEOATOMS

Use the [repository map](docs/development/repository-map.md) to identify the maintained source, distribution, dataset or guide affected by a change. The [maintenance guide](docs/development/maintenance.md) describes catalogue updates, validation and publication.

## Choose the source and environment

The repository root is the flag package. Versioned sources under `software/` are independently installable distributions. Use separate virtual environments for distributions sharing the same import names, and follow their [installation instructions](docs/installation.md).

For repository-root development:

```bash
python -m venv .venv
```

Activate the environment using the command for your operating system, then install the package and test dependencies:

```bash
python -m pip install -e ".[test]"
python -m pip install -r requirements-test.txt
```

The [installation guide](docs/installation.md) also gives commands that use the environment's Python directly without activation.

## Mathematical changes

Implement the conventions in the mathematical sources; correct implementation errors without changing the source mathematics to accommodate them. Compute new quantum multiplication matrices with the existing localization routines. Preserve exact arithmetic, the complete supported curve list, basis order, grading and Novikov-coordinate map.

A numerical spectrum, a matrix copied from a reference or a consistency check of stored results is not a fresh localization calculation. State the assumptions needed to identify the ambient operator with full cohomology. Assign full atomic invariants only when cyclicity and the Hodge-theoretic hypotheses have been established.

Add a regression with an independently known invariant or mathematical identity when changing computation behavior. For example, the cubic-surface line count is 27 with an empty insertion list. The [versioned usage guides](docs/software/index.md) specify the correct flag and toric curve coordinates.

## Documentation and data

Document the resulting user behavior and its mathematical scope. Keep version metadata, source archives, checksums, installation instructions and release notes consistent. Follow [the catalogue update procedure](docs/development/maintenance.md#adding-or-correcting-an-example) for new examples.

Use geometric names for examples and explain published classification references. Preserve stable data keys and existing links. Keep private manuscripts, research comparisons, execution logs and incomplete computations outside the published documentation and interface presets.

## Checks

Run the checks appropriate to the change, as listed in the [maintenance guide](docs/development/maintenance.md#validation). The main Python suite is:

```bash
python -m pytest tests/ -q
```

Documentation changes require a strict MkDocs build, equation rendering and browser checks; a Markdown-only preview does not reproduce the published mathematical display. Source-distribution changes also require installation checks on Linux and Windows. CI runs these checks and publishes documentation only after successful validation.
