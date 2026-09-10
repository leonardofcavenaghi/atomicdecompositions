with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

import re
old_card_str = '''card = f"""# ??? example "Case #{idx+1}: {label}__

    ---
    
    - **Ambient Space:** `{alg}`
    - **Dimension:** {dim}
    - **Fano Index:** {fano}
    - **Basis Rank:** {rank}
    - **Eigenvalues:** {", ".join(eigen_strs)}
"""'''

new_card_str = '''card = f"""??? example "Case #{idx+1}: {label}"
    - **Ambient Space:** `{alg}`
    - **Dimension:** {dim}
    - **Fano Index:** {fano}
    - **Basis Rank:** {rank}
    - **Eigenvalues:** {", ".join(eigen_strs)}
"""'''

if old_card_str in code:
    code = code.replace(old_card_str, new_card_str)
else:
    # use regex
    code = re.sub(r'card = f"""# \?\?\? example.*?Eigenvalues:[^\n]*\n"""', new_card_str, code, flags=re.DOTALL)

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
