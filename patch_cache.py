import json
import re

with open("catalog_cache.json", "r") as f:
    cache = json.load(f)

for case in cache["cases"]:
    text = case["text"]
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
    
    # Carefully insert </details>
    # Find block of $$ ... $$ after <details>
    def close_details(match):
        return match.group(0) + "\n\n    </details>\n"
    text = re.sub(r'(<details>.*?<summary>.*?</summary>\n\n\s*\$\$.*?\$\$)', close_details, text, flags=re.DOTALL)
    
    # Actually wait, `re.sub` with DOTALL on `.*?\$\$` might match everything. 
    # Better logic: split text by "\n        $$"
    # Actually, let's just append `</details>` whenever we see `$$` that corresponds to an open `<details>`.
    # Let's do it manually line by line.
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
    case["text"] = '\n'.join(new_lines)

with open("catalog_cache.json", "w") as f:
    json.dump(cache, f, indent=2)
