with open("resume_catalog.py", "r") as f:
    text = f.read()

text = text.replace('matrix_tex = indent_latex(sympy.latex(matrix_1), 4)', 'matrix_tex = indent_latex(sympy.latex(matrix_1), 8)')

target = '''        card = f"""### {label}\\n- **Ambient Space:** `${alg}$`
- **Dimension:** ${dim}$
- **Fano Index:** ${fano_idx}$
- **Basis Rank:** ${rank}$
- **Eigenvalues:** {eigenvals_str}

??? note "Quantum Matrix ($y=1$)"
    $$
{matrix_tex}
    $$
"""'''

replacement = '''        card = f"""??? example "{label}"
    - **Ambient Space:** `${alg}$`
    - **Dimension:** ${dim}$
    - **Fano Index:** ${fano_idx}$
    - **Basis Rank:** ${rank}$
    - **Eigenvalues:** {eigenvals_str}

    ??? note "Quantum Matrix ($y=1$)"
        $$
{matrix_tex}
        $$
"""'''

text = text.replace(target, replacement)

target2 = '''        if label in SCRAPED_HODGE:
            card += "\\n" + SCRAPED_HODGE[label] + "\\n"'''

replacement2 = '''        if label in SCRAPED_HODGE:
            hodge_content = indent_latex(SCRAPED_HODGE[label], 4)
            card += "\\n" + hodge_content + "\\n"'''

text = text.replace(target2, replacement2)

target3 = '''                mat_str = hodge_matrix_str(h, dim)
                card += f"""
??? note "Hodge Diamond ($h^{{p,q}}$)"
    $$
{mat_str}
    $$
"""'''

replacement3 = '''                mat_str = indent_latex(hodge_matrix_str(h, dim), 8)
                card += f"""
    ??? note "Hodge Diamond ($h^{{p,q}}$)"
        $$
{mat_str}
        $$
"""'''

text = text.replace(target3, replacement3)

with open("resume_catalog.py", "w") as f:
    f.write(text)
