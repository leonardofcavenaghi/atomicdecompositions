with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

scraped_dict = '''
SCRAPED_HODGE = {
    "Gr(2,5) / O(2)  Gushel-Mukai 5-fold": r"""
        <details>
          <summary><strong>Hodge Diamond:</strong></summary>
          <div style="padding: 5px 10px; margin-top: 5px; background-color: rgba(0,0,0,0.05); border-left: 3px solid #007bff; overflow-x: auto;">
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
          </div>
        </details>
""",
    "Gr(2,5) / O(1)+O(2)  Gushel-Mukai 4-fold": r"""
        <details>
          <summary><strong>Hodge Diamond:</strong></summary>
          <div style="padding: 5px 10px; margin-top: 5px; background-color: rgba(0,0,0,0.05); border-left: 3px solid #007bff; overflow-x: auto;">
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
          </div>
        </details>
"""
}
'''

code = code.replace("def process_case(args):", scraped_dict + "\ndef process_case(args):")

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
