with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

import re

new_card_str = r'''card = f"""??? example "Case #{idx+1}: {label}"
    - **Ambient Space:** `{alg}`
    - **Dimension:** {dim}
    - **Fano Index:** {fano}
    - **Basis Rank:** {rank}
    - **Eigenvalues:** {", ".join(eigen_strs)}
"""'''

pattern = r'card = f"""\?\?\? example.*?Eigenvalues:.*?</ul>\n"""'

code = re.sub(pattern, new_card_str, code, flags=re.DOTALL)

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
