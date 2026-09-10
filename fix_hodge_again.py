with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

import re

# Remove the 8 spaces before {hodge_matrix_str} in the f-string
old_str = """    - **Hodge Diamond ($h^{{p,q}}$):**
        $$
        {hodge_matrix_str(h, hdim)}
        $$"""

new_str = """    - **Hodge Diamond ($h^{{p,q}}$):**
        $$
{hodge_matrix_str(h, hdim)}
        $$"""
code = code.replace(old_str, new_str)

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
