with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

import re

old_str = r'''        elif is_pn and K_multidegs:
            h, hdim = compute_hodge_pn(n, degrees)
            card += f"""    ??? note "Hodge Diamond ($h^{{p,q}}$)"
        $$
        {hodge_matrix_str(h, hdim)}
        $$
"""'''

new_str = r'''        elif is_pn and K_multidegs:
            h, hdim = compute_hodge_pn(n, degrees)
            card += f"""    - **Hodge Diamond ($h^{{p,q}}$):**
        $$
        {hodge_matrix_str(h, hdim)}
        $$
"""'''

code = code.replace(old_str, new_str)

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
