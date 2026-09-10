with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

import re

# We will add a new helper function
helper_func = '''def indent_latex(latex_str, spaces=8):
    indentation = " " * spaces
    return "\\n".join(indentation + line for line in latex_str.split("\\n"))

def hodge_matrix_str(h, dim):'''
code = code.replace("def hodge_matrix_str(h, dim):", helper_func)

# Now we extract matrix_1 and indent it
# In process_case, after matrix_1 = c1TX.subs(ns)
add_matrix_tex = '''        matrix_1 = c1TX.subs(ns)
        matrix_tex = indent_latex(sympy.latex(matrix_1), 8)'''
code = code.replace("        matrix_1 = c1TX.subs(ns)", add_matrix_tex)

# Now we add it to the markdown template
old_card = '''    - **Basis Rank:** ${rank}$
    - **Eigenvalues:** {", ".join(eigen_strs)}
"""'''

new_card = '''    - **Basis Rank:** ${rank}$
    - **Quantum Matrix ($y=1$):**
        $$
{matrix_tex}
        $$
    - **Eigenvalues:** {", ".join(eigen_strs)}
"""'''
code = code.replace(old_card, new_card)

# And add the glossary entry
old_glossary = '''- **Eigenvalues**: The eigenvalues'''
new_glossary = '''- **Quantum Matrix ($y=1$)**: The small quantum multiplication matrix $c_1(TX)\\\\star$ projected onto the flag-ambient cohomology ring, evaluated at Novikov parameters $y=1$.
- **Eigenvalues**: The eigenvalues'''
code = code.replace(old_glossary, new_glossary)

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
