with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

import re

# Fix hodge_matrix_str indentation
code = code.replace('out = "\\\\begin{matrix}\\n"', 'out = "        \\\\begin{matrix}\\n"')

# Fix SCRAPED_HODGE append logic
code = code.replace('card += f"""    ??? note "Hodge Diamond"\\n{SCRAPED_HODGE[label]}\\n"""', 'card += f"""\\n{SCRAPED_HODGE[label]}\\n"""')

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
