with open("inject_fanography.py", "r") as f:
    text = f.read()

text = text.replace('matrix_latex = sympy.latex(sympy.Matrix(M_subs))', 'matrix_latex = "\\n".join("        " + line for line in sympy.latex(sympy.Matrix(M_subs)).split("\\n"))')

target = '''    md = f"""- **Ambient Space:** `${alg}$`
- **Fano Index:** `{fano}`
- **Basis Rank:** `{len(idx)}`

??? note "Quantum Matrix ($y=1$)"
    $$
    {matrix_latex}
    $$
"""'''

replacement = '''    md = f"""??? example "{var_id}"
    - **Ambient Space:** `${alg}$`
    - **Fano Index:** `{fano}`
    - **Basis Rank:** `{len(idx)}`

    ??? note "Quantum Matrix ($y=1$)"
        $$
{matrix_latex}
        $$
"""'''

text = text.replace(target, replacement)

with open("inject_fanography.py", "w") as f:
    f.write(text)
