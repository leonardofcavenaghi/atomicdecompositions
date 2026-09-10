import sys
import os
import json
import sympy
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import multiprocessing as mp

sys.path.insert(0, os.path.abspath('.'))
from gwflags import FlagVariety
from generated_fano_cases import CASES_100 as CASES

# [Copy compute_hodge_pn and indent_latex and hodge_matrix_str verbatim from generate_catalog_fast.py]
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
    "Gr(2,5) / O(2)  Gushel-Mukai 5-fold": r"""    ??? note "Hodge Diamond ($h^{p,q}$)"
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
    "Gr(2,5) / O(1)+O(2)  Gushel-Mukai 4-fold": r"""    ??? note "Hodge Diamond ($h^{p,q}$)"
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
        # Numeric backend to prevent sympy timeouts
        X = FlagVariety(alg, keep, backend='numeric')
        raw_matrix, Gr, v = X.small_quantum_multiplication(K_multidegs, workers=0)
        c1TX = sympy.Matrix(raw_matrix)
        
        # We don't have symbols in numeric, but just in case:
        ns = {f'y{i}': 1 for i in range(1, 10)}
        matrix_1 = c1TX.subs(ns)
        matrix_tex = indent_latex(sympy.latex(matrix_1), 4)
        
        # Calculate eigenvalues if small enough
        try:
            eigenvals = matrix_1.eigenvals()
            ev_list = []
            for ev, mult in eigenvals.items():
                ev_list.append(f"${sympy.latex(ev)}$ (mult: {mult})")
            eigenvals_str = ", ".join(ev_list)
        except Exception:
            eigenvals_str = "Skipped (Timeout)"
        
        dim = X.dimension
        if K_multidegs:
            for deg in K_multidegs:
                # If vector bundle, reduce dimension
                dim -= 1

        fano_idx = X.fano_index_and_betas()[0]
        if K_multidegs:
            for deg in K_multidegs:
                fano_idx -= sum(deg)
                
        rank = matrix_1.shape[0]

        card = f"""### {label}\n- **Ambient Space:** `${alg}$`
- **Dimension:** ${dim}$
- **Fano Index:** ${fano_idx}$
- **Basis Rank:** ${rank}$
- **Eigenvalues:** {eigenvals_str}

??? note "Quantum Matrix ($y=1$)"
    $$
{matrix_tex}
    $$
"""
        if label in SCRAPED_HODGE:
            card += "\n" + SCRAPED_HODGE[label] + "\n"
        elif is_pn and dim <= 8:
            try:
                h, _ = compute_hodge_pn(n, degrees)
                mat_str = hodge_matrix_str(h, dim)
                card += f"""
??? note "Hodge Diamond ($h^{{p,q}}$)"
    $$
{mat_str}
    $$
"""
            except Exception:
                pass

        if label.startswith("P"):
            category = "projective"
        elif label.startswith("Gr"):
            category = "grassmannians"
        else:
            category = "flag_varieties"

        case_dict = {
            "id": str(idx + 1),
            "label": label,
            "dim": str(dim),
            "fano": str(fano_idx),
            "rank": str(rank),
            "category": category,
            "text": card
        }

        return idx, case_dict


    except Exception as e:
        import traceback
        return idx, f"Error: {e}\n{traceback.format_exc()}"



def run_worker(args):
    idx, case_dict = process_case(args)
    return idx, case_dict

def main():
    with open("catalog_cache.json", "r") as f:
        cache = json.load(f)
    
    computed_labels = {c["label"] for c in cache["cases"]}
    args_list = [(idx, *case) for idx, case in enumerate(CASES) if case[0] not in computed_labels]
    
    print(f"Resuming computation for {len(args_list)} missing cases...")


    with ThreadPoolExecutor(max_workers=1) as pool:
        futures = {pool.submit(run_worker, arg): arg for arg in args_list}
        for future in as_completed(futures):
            idx, result = future.result()
            if isinstance(result, dict):
                print(f"[{idx+1}] Success: {result['label']}")
                cache["cases"].append(result)
                with open("catalog_cache.json", "w") as f:
                    json.dump(cache, f, indent=2)
                subprocess.run(["python3", "restructure_catalog.py"], check=True)
                subprocess.run("./new_mkdocs_env/bin/mkdocs gh-deploy --force", shell=True)
                subprocess.run("git add docs/catalog/ catalog_cache.json && git commit -m 'chore: cache computed cases' && git push", shell=True)
            else:
                print(f"[{idx+1}] Failed: {result}")


if __name__ == "__main__":
    main()
