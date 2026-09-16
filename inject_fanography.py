import sympy
from gwflags import FlagVariety
from catalog_inputs import selected_legacy_specs

specs = selected_legacy_specs("inject_verify")

# The records above are loaded from catalog_inputs.json; keep the rest of this
# legacy injector unchanged.


def generate_markdown(alg, keep, K):
    X = FlagVariety(alg, keep)
    K_arg = K if len(K) > 0 else None
    fano, betas = X.fano_index_and_betas(K_arg)
    M, Gr, idx = X.small_quantum_multiplication(K_arg, betas)
    
    subs_dict = {sympy.Symbol(f'y{i}'): 1 for i in range(1, 10)}
    M_subs = [[sympy.sympify(elem).subs(subs_dict) for elem in row] for row in M]
    matrix_latex = "\n".join("        " + line for line in sympy.latex(sympy.Matrix(M_subs)).split("\n"))
    
    md = f"""??? example "{var_id}"
    - **Ambient Space:** `${alg}$`
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
