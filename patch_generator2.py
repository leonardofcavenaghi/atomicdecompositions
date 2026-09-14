import re

with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

# Replace ??? note with <details><summary>
code = code.replace(
    r'    ??? note "Hodge Diamond"',
    r'    <details><summary>Hodge Diamond</summary>'
)

code = code.replace(
    r'        \end{matrix}',
    r'        \end{matrix}'
)

code = code.replace(
    r'        $$""",',
    r'        $$\n    </details>""",'
)
code = code.replace(
    r'        $$"""',
    r'        $$\n    </details>"""'
)

code = code.replace(
    r'    ??? note "Quantum Matrix ($y=1$)"',
    r'    <details><summary>Quantum Matrix ($y=1$)</summary>'
)
code = code.replace(
    r'        $$',
    r'        $$', 1 # not replacing all
)

code = re.sub(
    r'    \?\?\? note "Quantum Matrix \(\$y=1\$\)"\n        \$\$\n\{matrix_tex\}\n        \$\$\n',
    r'    <details><summary>Quantum Matrix ($y=1$)</summary>\n\n        $$\n{matrix_tex}\n        $$\n\n    </details>\n',
    code
)

code = re.sub(
    r'    \?\?\? note "Hodge Diamond \(\$h\^\{\{p,q\}\}\$\)"\n        \$\$\n\{hodge_matrix_str\(h, hdim\)\}\n        \$\$\n',
    r'    <details><summary>Hodge Diamond ($h^{{p,q}}$)</summary>\n\n        $$\n{hodge_matrix_str(h, hdim)}\n        $$\n\n    </details>\n',
    code
)

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
