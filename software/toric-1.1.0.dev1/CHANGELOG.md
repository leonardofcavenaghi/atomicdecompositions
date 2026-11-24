# GEOATOMS 1.1.0.dev1

Development source distribution for the GEOATOMS flag, toric, and combined software suite.

- Default flag Novikov parameter names retain ambient Dynkin nodes for type A and use consecutive kept-root labels for other root-system families (e.g., `C3` keep `3`, `G2` keep `2`, and `D5` keep `4` use `y1`).
- Python: `FlagVariety(..., novikov_convention="ambient")` retains legacy ambient-node names; `"compact"` uses consecutive labels for all types. The CLI and interface expose the same choice and results record the map.
- Renaming preserves exact coefficients, beta coordinates, the ordered basis, and grading.
- An empty flag CLI `--classes ""` means zero insertions, matching Python and the browser interface. The unmarked cubic-surface line count is 27.
- The standalone flag interface reports bundle rank and clarifies serial worker settings and quotient-bundle validation.
- Combined flag matrix caches distinguish naming conventions so symbolic matrices under different conventions are not silently reused.
- Toric inputs and Novikov names retain their fan/divisor conventions; interface text clarifies automatic curve-list scope.
- Unmarked flag tree generation uses rooted level sequences with AHU deduplication and lexicographic relabeling, preserving tree representatives, ordering, and vertex labels.
- Staged flag checkpoints store large exact fractions using tagged hexadecimal values; ordinary decimal checkpoints remain readable.

## Documentation and website

See [LAUNCH.md](LAUNCH.md) for the software overview, input/output conventions, and validation guides, and visit the [GEOATOMS website](https://leonardofcavenaghi.github.io/atomicdecompositions/) for the full geometric catalogue.
