# Unreleased 1.0.6.dev0

This is a prepared local development build, not a published release.

- Default flag parameter names retain ambient nodes for type A and use consecutive kept-root labels for other root-system families. Thus C3/keep 3, G2/keep 2 and D5/keep 4 use y1.
- Python: `FlagVariety(..., novikov_convention="ambient")` retains the previous names; `"compact"` is also available. The CLI and interface expose the same choice and results record the map.
- Renaming preserves exact coefficients, beta coordinates, the ordered basis and grading.
- An empty flag CLI `--classes ""` now means no insertions, matching Python and the interface. The unmarked cubic-surface line count remains 27.
- The standalone flag interface reports bundle rank and clarifies serial worker settings and quotient-bundle validation.
- Adopted verified unmarked-tree generation from Giovane commit 7f167e17a35069ac1ff1cefecce2ac8a0be8231c. It preserves tree representatives, ordering and vertex labels; compatibility was independently checked through six edges.

## Documentation prepared for launch

The repository now includes [LAUNCH.md](LAUNCH.md), a complete change overview, a shared input/output reference with generated records, separate usage guides, preserved legacy instructions and the remaining publication checks. These documents describe the prepared development sources and do not announce a completed release.

## Website launch — 2026-11-12

Universal catalogue organized by dimension and construction, with separate flag and toric mathematical descriptions; versioned individual and combined source downloads; revised installation and usage guides; contributor credits updated. The 1.0.6.dev0 and 1.1.0.dev1 sources retain development version labels.
