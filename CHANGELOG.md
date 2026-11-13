# Development version 1.0.6.dev0

This development source distribution is published; no new stable tag is implied.

- Default flag parameter names retain ambient nodes for type A and use consecutive kept-root labels for other root-system families. Thus C3/keep 3, G2/keep 2 and D5/keep 4 use y1.
- Python: `FlagVariety(..., novikov_convention="ambient")` retains the previous names; `"compact"` is also available. The CLI and interface expose the same choice and results record the map.
- Renaming preserves exact coefficients, beta coordinates, the ordered basis and grading.
- An empty flag CLI `--classes ""` now means no insertions, matching Python and the interface. The unmarked cubic-surface line count remains 27.
- The standalone flag interface reports bundle rank and clarifies serial worker settings and quotient-bundle validation.
- Adopted verified unmarked-tree generation from Giovane commit 7f167e17a35069ac1ff1cefecce2ac8a0be8231c. It preserves tree representatives, ordering and vertex labels; compatibility was independently checked through six edges.

## Documentation prepared for launch

The repository now includes [LAUNCH.md](LAUNCH.md), a complete change overview, a shared input/output reference with generated records, separate usage guides, preserved legacy instructions and the remaining publication checks. These documents describe the published development sources; the preserved stable tag remains v1.0.5.

## Website launch — 2026-11-13

Universal catalogue organized by dimension and construction, with separate flag and toric mathematical descriptions; versioned individual and combined source downloads; revised installation and usage guides; contributor credits updated. The 1.0.6.dev0 and 1.1.0.dev1 sources retain development version labels.

## Contributors and mathematical display

Contributors are listed alphabetically by surname. Browser checks report navigation-to-rendered times and formula counts for full-page loads, instant navigation and rapid page changes, and reject missing, duplicate or errored formula displays. These timings describe the CI browser environment, rather than a guaranteed time on every connection.

Math rendering now retries failed initial runtime downloads using an alternate provider and watches for late-arriving mathematical content. Browser tests disable the cache, abort the first runtime request and delay startup while navigating, and require successful rendering without a page reload.

## Mathematical notation

The flag and toric mathematical descriptions now use the papers’ notation and formulae, including ambient pushforward sums and the sign relation K^F=-A(q). They distinguish computed ambient data from full Hodge-invariant factors and retain the hypotheses needed for atomic and rationality interpretations.
