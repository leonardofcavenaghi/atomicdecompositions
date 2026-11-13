with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

import re

# Update eigenvalue formatting
old_eigen = '''        eigen_strs = []
        for ev, mult in eigenvals.items():
            try:
                ev_float = round(float(ev.evalf()), 3)
                eigen_strs.append(f"{ev_float} (mult: {mult})")
            except:
                eigen_strs.append(f"{ev} (mult: {mult})")'''

new_eigen = '''        eigen_strs = []
        for ev, mult in eigenvals.items():
            ev_tex = sympy.latex(ev)
            eigen_strs.append(f"${ev_tex}$ (mult: {mult})")'''

code = code.replace(old_eigen, new_eigen)

# Update card string formatting
old_card = '''        card = f"""??? example "Case #{idx+1}: {label}"
    - **Ambient Space:** `{alg}`
    - **Dimension:** {dim}
    - **Fano Index:** {fano}
    - **Basis Rank:** {rank}
    - **Eigenvalues:** {", ".join(eigen_strs)}
"""'''

new_card = '''        card = f"""??? example "Case #{idx+1}: {label}"
    - **Ambient Space:** `${alg}$`
    - **Dimension:** ${dim}$
    - **Fano Index:** ${fano}$
    - **Basis Rank:** ${rank}$
    - **Eigenvalues:** {", ".join(eigen_strs)}
"""'''

code = code.replace(old_card, new_card)

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
