# Repository working instructions

- Keep documentation, the website change log, release notes, version metadata,
  and download instructions synchronized with every relevant change. Explain
  the resulting behavior and its validation in the files where users encounter
  it. Distinguish a tagged stable snapshot from an unreleased development build.
- Mathematical input matrices must be computed with the existing gwflags
  virtual-localization routines. A stored catalogue matrix is a comparison
  target, not evidence of a fresh localization run. Preserve exact arithmetic,
  the full automatic supported curve list, and the returned grading and basis.
- Keep incomplete examples outside the published documentation tree and public
  GUI presets until their computations are complete and reviewed.
- Keep unpublished research, manuscript comparisons and internal conversation
  details in local files outside this repository. Public documentation and
  release notes cover user-facing software changes and their verification;
  they are not a record of private research or chat decisions.
