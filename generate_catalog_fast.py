import sys
import os
import sympy
import subprocess
import multiprocessing as mp

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

def indent_latex(latex_str, spaces=8):
    indentation = " " * spaces
    return "\n".join(indentation + line for line in latex_str.split("\n"))

def hodge_matrix_str(h, dim):
    out = "        \\begin{matrix}\n"
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
    return out



SCRAPED_HODGE = {
    "Gr(2,5) / O(2)  Gushel-Mukai 5-fold": r"""    - **Hodge Diamond:**
        $$
        \begin{matrix}
        & & & & & 1 & & & & & \\
        & & & & 0 & & 0 & & & & \\
        & & & 0 & & 1 & & 0 & & & \\
        & & 0 & & 0 & & 0 & & 0 & & \\
        & 0 & & 0 & & 2 & & 0 & & 0 & \\
        0 & & 0 & & 10 & & 10 & & 0 & & 0 \\
        & 0 & & 0 & & 2 & & 0 & & 0 & \\
        & & 0 & & 0 & & 0 & & 0 & & \\
        & & & 0 & & 1 & & 0 & & & \\
        & & & & 0 & & 0 & & & & \\
        & & & & & 1 & & & & & \\
        \end{matrix}
        $$""",
    "Gr(2,5) / O(1)+O(2)  Gushel-Mukai 4-fold": r"""    - **Hodge Diamond:**
        $$
        \begin{matrix}
        & & & & 1 & & & & \\
        & & & 0 & & 0 & & & \\
        & & 0 & & 1 & & 0 & & \\
        & 0 & & 0 & & 0 & & 0 & \\
        0 & & 1 & & 22 & & 1 & & 0 \\
        & 0 & & 0 & & 0 & & 0 & \\
        & & 0 & & 1 & & 0 & & \\
        & & & 0 & & 0 & & & \\
        & & & & 1 & & & & \\
        \end{matrix}
        $$"""
}

def process_case(args):
    idx, label, alg, keep, K_multidegs, _ = args
    print(f"[{idx+1}] Started computing: {label}")
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
        c1TX = sympy.Matrix(X.small_quantum_multiplication(K_multidegs)[0])
        ns = {f'y{i}': 1 for i in range(1, 10)}
        matrix_1 = c1TX.subs(ns)
        matrix_tex = indent_latex(sympy.latex(matrix_1), 8)
        
        eigenvals = matrix_1.eigenvals()
        eigen_strs = []
        for ev, mult in eigenvals.items():
            ev_tex = sympy.latex(ev)
            eigen_strs.append(f"${ev_tex}$ (mult: {mult})")
            
        dim = X.dimension
        if K_multidegs:
            dim -= len(K_multidegs)
            
        res = X.fano_index_and_betas(K_multidegs)
        if isinstance(res, tuple) and len(res) == 2:
            fano = res[0]
        else:
            fano = res
            
        rank = len(X.classes)
        
        card = f"""??? example "Case #{idx+1}: {label}"
    - **Ambient Space:** `${alg}$`
    - **Dimension:** ${dim}$
    - **Fano Index:** ${fano}$
    - **Basis Rank:** ${rank}$
    - **Quantum Matrix ($y=1$):**
        $$
{matrix_tex}
        $$
    - **Eigenvalues:** {", ".join(eigen_strs)}
"""
        if label in SCRAPED_HODGE:
            card += f"""\n{SCRAPED_HODGE[label]}\n"""
        elif is_pn and K_multidegs:
            h, hdim = compute_hodge_pn(n, degrees)
            card += f"""    - **Hodge Diamond ($h^{{p,q}}$):**
        $$
        {hodge_matrix_str(h, hdim)}
        $$
"""
        return (idx, card)
    except Exception as e:
        print(f"[{idx+1}] Failed {label}: {e}")
        return None


def init_catalog():
    with open("docs/catalog.md", "w") as f:
        f.write("""# Quantum Geometry Catalog

Welcome to the automated catalog. Below you will find geometric and quantum properties computed for various complete intersections.

## Glossary

- **Ambient Space**: The ambient flag variety $G/P$ in which the complete intersection $X$ is embedded.
- **Dimension**: The complex dimension of the resulting geometric space $X$. Computed by subtracting the rank of the intersecting bundle from the dimension of the ambient space.
- **Fano Index**: The greatest integer $I_X$ dividing the anticanonical class $-K_X$. It dictates the powers of the Novikov parameters in quantum multiplication.
- **Basis Rank**: The number of dimensions in the projected flag-ambient cohomology ring $H_{amb}^*(X)$. This equals the size of the square quantum multiplication matrix.
- **Quantum Matrix ($y=1$)**: The small quantum multiplication matrix $c_1(TX)\\star$ projected onto the flag-ambient cohomology ring, evaluated at Novikov parameters $y=1$.
- **Eigenvalues**: The eigenvalues of the small quantum multiplication matrix $c_1(TX)\star$ evaluated at $y=1$, along with their algebraic multiplicities. These values govern the spectrum of the quantum connection.
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
    
    new_content = content.replace("</div>\n\n***", card + "\n\n</div>\n\n***")
    
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
