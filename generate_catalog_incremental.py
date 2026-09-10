import sys
import os
import sympy
import subprocess

sys.path.insert(0, os.path.abspath('.'))

from gwflags import FlagVariety
from tests.reference_cases import CASES

def compute_hodge_pn(n, degrees):
    x, y = sympy.symbols('x y')
    k = len(degrees)
    dimX = n - k
    prod = sympy.S(1)
    for d in degrees:
        num = (1+x)**d - (1+y)**d
        den = -(1+x)**d * y + (1+y)**d * x
        factor = sympy.cancel(num / den)
        prod = prod * factor
    gen_func = sympy.cancel((prod - 1) / ((1+x)*(1+y)))
    t = sympy.symbols('t')
    gf_t = gen_func.subs({x: t*x, y: t*y})
    series_exp = sympy.series(gf_t, t, 0, dimX + 1).removeO()
    term_dimX = series_exp.coeff(t, dimX)
    poly_expr = sympy.expand(term_dimX)
    poly = sympy.Poly(poly_expr, x, y)
    hodge = {}
    for p in range(dimX + 1):
        for q in range(dimX + 1):
            if p + q == dimX:
                coeff = poly.coeff_monomial(x**p * y**q)
                h_prim = abs(int(coeff))
                base_h = 1 if p == q else 0
                hodge[(p,q)] = base_h + h_prim
            else:
                base_h = 1 if p == q else 0
                hodge[(p,q)] = base_h
    return hodge, dimX

def hodge_matrix_str(h, dim):
    rows = []
    for p in range(dim+1):
        row = []
        for q in range(dim+1):
            row.append(str(h.get((p,q), 0)))
        rows.append(" & ".join(row))
    out = "\\begin{pmatrix}\n"
    for r in rows:
        out += "        " + r + " \\\\\n"
    out += "        \\end{pmatrix}"
    return out

# Load existing markdown cards from catalog.md
def get_existing_cards():
    if not os.path.exists("docs/catalog.md"):
        return []
    with open("docs/catalog.md", "r") as f:
        content = f.read()
    if "## Geometry Catalog" not in content:
        return []
    
    parts = content.split("<div class=\"grid cards\" markdown>")
    if len(parts) < 2:
        return []
    
    cards_text = parts[1].split("</div>")[0]
    return cards_text

def append_to_catalog(card):
    with open("docs/catalog.md", "r") as f:
        content = f.read()
    
    header = content.split("## Geometry Catalog")[0] + "## Geometry Catalog\n\n<div class=\"grid cards\" markdown>\n\n"
    
    if "## Geometry Catalog" in content and "<div class=\"grid cards\" markdown>" in content:
        parts = content.split("<div class=\"grid cards\" markdown>")
        existing_cards = parts[1].split("</div>")[0].strip()
        if existing_cards:
            existing_cards += "\n\n"
    else:
        existing_cards = ""
        
    footer = "\n\n</div>\n\n***\n\n*Note: This catalog is automatically generated.*"
    
    new_content = header + existing_cards + card + footer
    with open("docs/catalog.md", "w") as f:
        f.write(new_content)
        
    # Git push
    subprocess.run(["git", "add", "docs/catalog.md"])
    subprocess.run(["git", "commit", "-m", "Auto-update catalog with new case"])
    subprocess.run(["git", "push", "origin", "main"])


# Clear existing cards to start fresh
with open("docs/catalog.md", "r") as f:
    content = f.read()
header = content.split("## Geometry Catalog")[0] + "## Geometry Catalog\n\n<div class=\"grid cards\" markdown>\n\n</div>\n\n***\n\n*Note: This catalog is automatically generated.*\n"
with open("docs/catalog.md", "w") as f:
    f.write(header)

subprocess.run(["git", "add", "docs/catalog.md"])
subprocess.run(["git", "commit", "-m", "Reset catalog cards"])
subprocess.run(["git", "push", "origin", "main"])

for idx, (label, alg, keep, K_multidegs, _) in enumerate(CASES):
    print(f"Computing case {idx+1}/{len(CASES)}: {label}")
    degrees = []
    is_pn = False
    
    if alg.startswith('A') and len(keep) == 1 and keep[0] == 1:
        n = int(alg[1:])
        is_pn = True
        
    if K_multidegs:
        for row in K_multidegs:
            if is_pn:
                degrees.append(int(row[0]))
        
    try:
        X = FlagVariety(alg, keep, backend='sympy')
        c1TX = X.small_quantum_multiplication(K_multidegs)[0]
        ns = {f'y{i}': 1 for i in range(1, 10)}
        matrix_1 = c1TX.subs(ns)
        
        eigenvals = matrix_1.eigenvals()
        eigen_strs = []
        for ev, mult in eigenvals.items():
            try:
                ev_float = round(float(ev.evalf()), 3)
                eigen_strs.append(f"{ev_float} (mult: {mult})")
            except:
                eigen_strs.append(f"{ev} (mult: {mult})")
            
        dim = X.dimension()
        if K_multidegs:
            dim -= len(K_multidegs)
            
        res = X.fano_index_and_betas(K_multidegs)
        if isinstance(res, tuple) and len(res) == 2:
            fano = res[0]
        else:
            fano = res
            
        rank = len(X.classes())
        
        card = f"""-   __Case #{idx+1}: {label}__

    ---
    
    - **Ambient Space:** `{alg}`
    - **Dimension:** {dim}
    - **Fano Index:** {fano}
    - **Basis Rank:** {rank}
    - **Eigenvalues:** {", ".join(eigen_strs)}
"""
        if is_pn and K_multidegs:
            h, hdim = compute_hodge_pn(n, degrees)
            card += f"""    - **Hodge Diamond ($h^{{p,q}}$):**
        $$
        {hodge_matrix_str(h, hdim)}
        $$
"""
        append_to_catalog(card)
        print(f"Pushed case {idx+1}")
    except Exception as e:
        print(f"Failed {label}: {e}")

