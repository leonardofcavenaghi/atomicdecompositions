import sympy
from gwflags import FlagVariety

specs = {
    # Picard Rank 1
    "1-17": ("A3", [1], []),
    "1-16": ("A4", [1], [[2]]),
    "1-15": ("A4", [2], [[1], [1], [1]]),
    "1-14": ("A5", [1], [[2], [2]]),
    "1-13": ("A4", [1], [[3]]),
    "1-7":  ("A5", [2], [[1], [1], [1], [1], [1]]),
    "1-5":  ("A4", [2], [[1], [1], [2]]),
    "1-4":  ("A6", [1], [[2], [2], [2]]),
    "1-3":  ("A5", [1], [[2], [3]]),
    "1-2":  ("A4", [1], [[4]]),
    "1-6":  ("D5", [5], [[1]] * 7),
    "1-8":  ("C3", [3], [[1]] * 3),
    "1-9":  ("G2", [2], [[1]] * 2),
    # Picard Rank > 1
    "2-24": ("A2", [1, 2], []),
    "2-35": ("A1xA2", [1, 2], []),
    "3-27": ("A1xA1xA1", [1, 2, 3], [])
}

def generate_markdown(alg, keep, K):
    X = FlagVariety(alg, keep)
    K_arg = K if len(K) > 0 else None
    fano, betas = X.fano_index_and_betas(K_arg)
    M, Gr, idx = X.small_quantum_multiplication(K_arg, betas)
    
    subs_dict = {sympy.Symbol(f'y{i}'): 1 for i in range(1, 10)}
    M_subs = [[sympy.sympify(elem).subs(subs_dict) for elem in row] for row in M]
    matrix_latex = sympy.latex(sympy.Matrix(M_subs))
    
    md = f"""- **Ambient Space:** `${alg}$`
- **Fano Index:** `{fano}`
- **Basis Rank:** `{len(idx)}`

??? note "Quantum Matrix ($y=1$)"
    $$
    {matrix_latex}
    $$
"""
    return md

filepath = 'docs/catalog/fanography.md'
with open(filepath, 'r') as f:
    lines = f.readlines()

out_lines = []
for line in lines:
    out_lines.append(line)
    if line.startswith("### Fano Variety "):
        var_id = line.strip().replace("### Fano Variety ", "")
        if var_id in specs:
            print(f"Computing {var_id}...")
            alg, keep, K = specs[var_id]
            md_block = generate_markdown(alg, keep, K)
            out_lines.append(md_block + "\n")

with open(filepath, 'w') as f:
    f.writelines(out_lines)
