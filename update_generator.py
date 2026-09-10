with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

import re

# We will replace `append_and_push(card)` with a dictionary collection and write at the end.
# Wait, let's just make it write a fresh file at the start, and append to it properly!

new_main = '''
def init_catalog():
    with open("docs/catalog.md", "w") as f:
        f.write("""# Quantum Geometry Catalog

Welcome to the automated catalog. Below you will find geometric and quantum properties computed for various complete intersections.

## Glossary

- **Ambient Space**: The ambient flag variety $G/P$ in which the complete intersection $X$ is embedded.
- **Dimension**: The complex dimension of the resulting geometric space $X$. Computed by subtracting the rank of the intersecting bundle from the dimension of the ambient space.
- **Fano Index**: The greatest integer $I_X$ dividing the anticanonical class $-K_X$. It dictates the powers of the Novikov parameters in quantum multiplication.
- **Basis Rank**: The number of dimensions in the projected flag-ambient cohomology ring $H_{amb}^*(X)$. This equals the size of the square quantum multiplication matrix.
- **Eigenvalues**: The eigenvalues of the small quantum multiplication matrix $c_1(TX)\\\\star$ evaluated at $y=1$, along with their algebraic multiplicities. These values govern the spectrum of the quantum connection.
- **Hodge Diamond**: The geometric $h^{p,q}$ Hodge numbers of the space.

***

<div class="grid cards" markdown>

</div>

***
*Note: This catalog is automatically generated.*
""")

def append_and_push(card):
    with open("docs/catalog.md", "r") as f:
        content = f.read()
    
    new_content = content.replace("</div>\\n\\n***", card + "\\n\\n</div>\\n\\n***")
    
    with open("docs/catalog.md", "w") as f:
        f.write(new_content)
        
    subprocess.run(["git", "add", "docs/catalog.md"])

if __name__ == '__main__':
    init_catalog()
    args_list = [(idx, *case) for idx, case in enumerate(CASES)]
    cores = max(1, mp.cpu_count() - 1)
    print(f"Starting multiprocessing pool with {cores} cores...")
    
    with mp.Pool(cores) as pool:
        for result in pool.imap_unordered(process_case, args_list):
            if result:
                idx, card = result
                print(f"[{idx+1}] Success! Pushing to git...")
                append_and_push(card)
'''

# Replace from `def append_and_push` to the end.
pattern = r'def append_and_push\(card\):.*'
code = re.sub(pattern, new_main, code, flags=re.DOTALL)

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)

