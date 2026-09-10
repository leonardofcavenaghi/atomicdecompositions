import re

with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

scraped_dict = '''
SCRAPED_HODGE = {
    "Gr(2,5) / O(2)  Gushel-Mukai 5-fold": r"""
        $$
        \\begin{matrix}
        & & & & & 1 & & & & & \\\\
        & & & & 0 & & 0 & & & & \\\\
        & & & 0 & & 1 & & 0 & & & \\\\
        & & 0 & & 0 & & 0 & & 0 & & \\\\
        & 0 & & 0 & & 2 & & 0 & & 0 & \\\\
        0 & & 0 & & 10 & & 10 & & 0 & & 0 \\\\
        & 0 & & 0 & & 2 & & 0 & & 0 & \\\\
        & & 0 & & 0 & & 0 & & 0 & & \\\\
        & & & 0 & & 1 & & 0 & & & \\\\
        & & & & 0 & & 0 & & & & \\\\
        & & & & & 1 & & & & & \\\\
        \\end{matrix}
        $$
""",
    "Gr(2,5) / O(1)+O(2)  Gushel-Mukai 4-fold": r"""
        $$
        \\begin{matrix}
        & & & & 1 & & & & \\\\
        & & & 0 & & 0 & & & \\\\
        & & 0 & & 1 & & 0 & & \\\\
        & 0 & & 0 & & 0 & & 0 & \\\\
        0 & & 1 & & 22 & & 1 & & 0 \\\\
        & 0 & & 0 & & 0 & & 0 & \\\\
        & & 0 & & 1 & & 0 & & \\\\
        & & & 0 & & 0 & & & \\\\
        & & & & 1 & & & & \\\\
        \\end{matrix}
        $$
"""
}
'''

if "SCRAPED_HODGE" not in code:
    # Insert it near the top
    code = code.replace("def process_case(args):", scraped_dict + "\ndef process_case(args):")

# Now append it in the card string
hook = "if is_pn and K_multidegs:"
replacement = '''if label in SCRAPED_HODGE:
            card += f"""    ??? note "Hodge Diamond"\\n{SCRAPED_HODGE[label]}\\n"""
        elif is_pn and K_multidegs:'''
        
if "if label in SCRAPED_HODGE" not in code:
    code = code.replace(hook, replacement)
    
# Wait, the `is_pn` one also needs to be a nested flashcard!
old_pn = '''card += f"""    - **Hodge Diamond ($h^{{p,q}}$):**
        $$
        {hodge_matrix_str(h, hdim)}
        $$
"""'''
new_pn = '''card += f"""    ??? note "Hodge Diamond ($h^{{p,q}}$)"
        $$
        {hodge_matrix_str(h, hdim)}
        $$
"""'''
code = code.replace(old_pn, new_pn)

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
