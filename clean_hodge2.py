with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

import re

new_hodge = r'''SCRAPED_HODGE = {
    "Gr(2,5) / O(2)  Gushel-Mukai 5-fold": r"""    - **Hodge Diamond:**
        $$
        \begin{matrix}
        & & & & & 1 & & & & & \\
        & & & & 0 & & 0 & & & & \\
        & & & 0 & & 1 & & 0 & & & \\
        & & 0 & & 0 & & 0 & & 0 & & \\
        & 0 & & 0 & & 2 & & 0 & & 0 & \\
        0 & & 0 & & 10 & & 10 & & 0 & & 0 \\
        & 0 & & 0 & & 2 & & 0 & & 0 & \\
        & & 0 & & 0 & & 0 & & 0 & & \\
        & & & 0 & & 1 & & 0 & & & \\
        & & & & 0 & & 0 & & & & \\
        & & & & & 1 & & & & & \\
        \end{matrix}
        $$""",
    "Gr(2,5) / O(1)+O(2)  Gushel-Mukai 4-fold": r"""    - **Hodge Diamond:**
        $$
        \begin{matrix}
        & & & & 1 & & & & \\
        & & & 0 & & 0 & & & \\
        & & 0 & & 1 & & 0 & & \\
        & 0 & & 0 & & 0 & & 0 & \\
        0 & & 1 & & 22 & & 1 & & 0 \\
        & 0 & & 0 & & 0 & & 0 & \\
        & & 0 & & 1 & & 0 & & \\
        & & & 0 & & 0 & & & \\
        & & & & 1 & & & & \\
        \end{matrix}
        $$"""
}'''

start = code.find("SCRAPED_HODGE = {")
end = code.find("def process_case(args):")
old_chunk = code[start:end]

code = code.replace(old_chunk, new_hodge + "\n\n")

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
