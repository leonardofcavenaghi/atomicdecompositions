# GeoAtoms Workspace Rules

These universal rules must be followed when working within this repository:

## Rule 1: Strict Mathematical Typography
Whenever generating mathematical output, flashcards, or documentation values (e.g., Eigenvalues, Dimensions, Matrices) from Python scripts, you MUST NOT output raw `sympy` Python strings (e.g., `CRootOf(...)`, `sqrt(...)`, or `Matrix(...)`). All mathematical values must be strictly compiled through `sympy.latex()` and encapsulated in Markdown math mode (`$ ... $` or `$$ ... $$`) so they render as academic typography.

## Rule 2: Strict Prohibition on Unproven Theory & Unpublished Papers
Whenever drafting methodology, README files, or theoretical guides for the `GEOATOMS` software, the documentation must remain strictly constrained to the defined tasks (testing rationality criteria, generating Gromov-Witten invariants, constructing flag varieties). You MUST NOT invent, assert, or mention theoretical constructs such as "Conjecture O", nor hallucinate or cite unpublished papers (e.g., "Cavenaghi et al."). Stick entirely to the functional mechanics of the `gwflags` library.

## Rule 3: MkDocs Material Math Block Indentation
Whenever generating MkDocs Material collapsible blocks (`??? note`, `??? example`) that contain multi-line LaTeX math blocks (`$$ \begin{matrix} ... \end{matrix} $$`), you must adhere to the following strict indentation:
1. The `??? note "Title"` block must be indented by exactly 4 spaces if it is nested inside another block.
2. The `$$` delimiters must be indented by exactly 4 spaces (or 8 spaces if nested).
3. The internal LaTeX content (e.g., `\left[\begin{matrix}...`) MUST be uniformly indented by exactly the same number of spaces as the `$$` delimiters. Failure to do this will cause the parser to break and the matrices to render as raw text.

## Rule 4: Fast Fano Index Combinatorial Filtering
Whenever writing loops to programmatically search, discover, or filter hundreds of Fano varieties (especially Complete Intersections in Grassmannians or Projective spaces), you **DO NOT** instantiate `gwflags.FlagVariety` objects inside the loop to check the Fano index. The intersection ring computations are computationally prohibitive. Instead, use direct combinatorial index formulas to filter candidates:
- Projective Space $\mathbb{P}^n$: `index = (n + 1) - sum(degrees)`
- Grassmannian $Gr(k, n)$: `index = n - sum(degrees)`
- Quadrics $Q^n$: `index = n - sum(degrees)`
Only instantiate `FlagVariety` objects for cases where the theoretical index is strictly positive (`index > 0`).

## Rule 5: Always Use gwflags via Miniconda Runtime
You MUST always use the `gwflags` library for computations. All `gwflags` library executions (CLI, GUI, tests, scripts) MUST use the miniconda Python interpreter at `/home/leonardofcavenaghi/miniconda/bin/python3` with `BypassSandbox: true`. Do NOT use system Python, venv Python, or sandbox Python — they lack required dependencies (`sympy`, `mpmath`). Git push operations also require `BypassSandbox: true` for DNS resolution.

## Rule 6: Mathematical Assertions in Tests
When writing new test cases for `gwflags`, you MUST NOT assume mathematical values (Fano indices, dimensions, GW invariants, eigenvalues). Instead:
1. First run the computation with `gwflags` to obtain the ACTUAL value.
2. Only then write the assertion using the computed value.
3. For product algebras (e.g., `A1xA2`), beta vectors must have length equal to the root system rank, and for GKM engine tests, nonzero beta entries must correspond to kept nodes only.

## Rule 7: Localization Theorem Attribution
The localization technique used by `gwflags` on the moduli space of stable maps is the **Graber-Pandharipande Virtual Localization Theorem**, NOT the Atiyah-Bott Localization Theorem (which applies only to smooth manifolds). All documentation, comments, and generated text must use "virtual localization" or "Graber-Pandharipande" when referring to this technique.
