import glob
import re

for filename in glob.glob("docs/catalog/*.md"):
    with open(filename, "r") as f:
        text = f.read()

    # Apply substitutions
    text = text.replace(
        '    ??? note "Quantum Matrix ($y=1$)"',
        '    <details><summary>Quantum Matrix ($y=1$)</summary>'
    )
    text = text.replace(
        '    ??? note "Hodge Diamond ($h^{p,q}$)"',
        '    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>'
    )
    text = text.replace(
        '    ??? note "Hodge Diamond"',
        '    <details><summary>Hodge Diamond</summary>'
    )
    
    text = re.sub(r'\\left\[\\begin\{array\}\{[a-z]+\}', r'\\begin{bmatrix}', text)
    text = text.replace(r'\end{array}\right]', r'\end{bmatrix}')
    text = text.replace(r'\left[\begin{matrix}', r'\begin{bmatrix}')
    text = text.replace(r'\end{matrix}\right]', r'\end{bmatrix}')
    
    lines = text.split('\n')
    new_lines = []
    in_details = 0
    in_math = False
    for line in lines:
        new_lines.append(line)
        if '<details>' in line:
            in_details += 1
        if line.strip() == '$$':
            in_math = not in_math
            if not in_math and in_details > 0:
                new_lines.append('')
                new_lines.append('    </details>')
                in_details -= 1
                
    with open(filename, "w") as f:
        f.write('\n'.join(new_lines))

print("Patched all markdown files!")
