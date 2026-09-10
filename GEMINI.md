# GeoAtoms Workspace Rules

These universal rules must be followed when working within this repository:

## Rule 1: Strict Mathematical Typography
Whenever generating mathematical output, flashcards, or documentation values (e.g., Eigenvalues, Dimensions, Matrices) from Python scripts, you MUST NOT output raw `sympy` Python strings (e.g., `CRootOf(...)`, `sqrt(...)`, or `Matrix(...)`). All mathematical values must be strictly compiled through `sympy.latex()` and encapsulated in Markdown math mode (`$ ... $` or `$$ ... $$`) so they render as academic typography.

## Rule 2: Strict Prohibition on Unproven Theory & Unpublished Papers
Whenever drafting methodology, README files, or theoretical guides for the `GEOATOMS` software, the documentation must remain strictly constrained to the defined tasks (testing rationality criteria, generating Gromov-Witten invariants, constructing flag varieties). You MUST NOT invent, assert, or mention theoretical constructs such as "Conjecture O", nor hallucinate or cite unpublished papers (e.g., "Cavenaghi et al."). Stick entirely to the functional mechanics of the `gwflags` library.

## Rule 3: MkDocs Material Math Block Indentation
Whenever generating MkDocs Material collapsible blocks (`??? note`, `??? example`) that contain multi-line LaTeX math blocks (`$$ \begin{matrix} ... \end{matrix} $$`), you must adhere to the following strict indentation:
1. The `??? note "Title"` block must be indented by exactly 4 spaces if it is nested inside another block.
2. The `$$` delimiters must be indented by exactly 8 spaces.
3. The internal LaTeX content (e.g., `\left[\begin{matrix}...`) MUST be uniformly indented by exactly 8 spaces on every line. Failure to do this will cause the parser to break and the matrices to render as raw text.
