with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

import re

old_func = r'''def hodge_matrix_str(h, dim):
    rows = \[\]
    for p in range\(dim\+1\):
        row = \[\]
        for q in range\(dim\+1\):
            row\.append\(str\(h\.get\(\(p,q\), 0\)\)\)
        rows\.append\(" & "\.join\(row\)\)
    out = "\\begin{pmatrix}\\n"
    for r in rows:
        out \+= "        " \+ r \+ " \\\\\\n"
    out \+= "        \\end{pmatrix}"
    return out'''

new_func = r'''def hodge_matrix_str(h, dim):
    out = "\\begin{matrix}\n"
    for k in range(2*dim + 1): 
        cols = []
        for i in range(2*dim + 1):
            if (k + i - dim) % 2 == 0:
                p = (k + i - dim) // 2
                q = (k - i + dim) // 2
                if 0 <= p <= dim and 0 <= q <= dim:
                    cols.append(str(h.get((p,q), 0)))
                else:
                    cols.append("")
            else:
                cols.append("")
        out += "        " + " & ".join(cols) + " \\\\\n"
    out += "        \\end{matrix}"
    return out'''

# Use literal string replacement
# Extract the exact string first:
start = code.find("def hodge_matrix_str(h, dim):")
end = code.find("def process_case(args):")
old_chunk = code[start:end]

code = code.replace(old_chunk, new_func + "\n\n\n")

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
