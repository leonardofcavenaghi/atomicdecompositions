with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

import re

new_hodge = '''
SCRAPED_HODGE = {
    "Gr(2,5) / O(2)  Gushel-Mukai 5-fold": r"""    - **Hodge Diamond:**
        $$
        \\begin{matrix}
        & & & & & 1 & & & & & \\\\
        & & & & 0 & & 0 & & & & \\\\
        & & & 0 & & 1 & & 0 & & & \\\\
        & & 0 & & 0 & & 0 & & 0 & & \\\\
        & 0 & & 0 & & 2 & & 0 & & 0 & \\\\
        0 & & 0 & & 10 & & 10 & & 0 & & 0 \\\\
        & 0 & & 0 & & 2 & & 0 & & 0 & \\\\
        & & 0 & & 0 & & 0 & & 0 & & \\\\
        & & & 0 & & 1 & & 0 & & & \\\\
        & & & & 0 & & 0 & & & & \\\\
        & & & & & 1 & & & & & \\\\
        \\end{matrix}
        $$""",
    "Gr(2,5) / O(1)+O(2)  Gushel-Mukai 4-fold": r"""    - **Hodge Diamond:**
        $$
        \\begin{matrix}
        & & & & 1 & & & & \\\\
        & & & 0 & & 0 & & & \\\\
        & & 0 & & 1 & & 0 & & \\\\
        & 0 & & 0 & & 0 & & 0 & \\\\
        0 & & 1 & & 22 & & 1 & & 0 \\\\
        & 0 & & 0 & & 0 & & 0 & \\\\
        & & 0 & & 1 & & 0 & & \\\\
        & & & 0 & & 0 & & & \\\\
        & & & & 1 & & & & \\\\
        \\end{matrix}
        $$"""
}
'''

pattern = r'SCRAPED_HODGE = \{.*?\}\n'
code = re.sub(pattern, new_hodge, code, flags=re.DOTALL)

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
