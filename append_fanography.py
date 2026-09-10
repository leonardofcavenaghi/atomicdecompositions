import sympy
from gwflags import FlagVariety
from gwflags.bundles import taut_sub, dual, wedge, osum
import os

fano_cases = [
    ("1-2", "A4", [1], [[4]]),
    ("1-3", "A5", [1], [[2], [3]]),
    ("1-17", "A3", [1], []),
]

def render_case(name, algebra, keep, K_desc):
    X = FlagVariety(algebra, keep)
    if K_desc == "1-10_special":
        W = wedge(2, dual(taut_sub(X, 3)))
        K = osum(W, osum(W, W))
    else:
        K = K_desc
    
    M, Gr, idx = X.small_quantum_multiplication(K=K, workers=os.cpu_count())
    matrix_latex = sympy.latex(M)
    
    return f"""
### Fanography ID: {name}
- **Algebra**: `{algebra}`
- **Keep**: `{keep}`
- **Degrees/Bundle**: `{K_desc}`

??? note "Quantum Matrix"
        $$
        {matrix_latex}
        $$

"""

def append_to_catalog():
    with open("docs/catalog.md", "a") as f:
        f.write("\n\n## Verified Fanography Examples (Fast Numeric Backend)\n")
        for case in fano_cases:
            print(f"Generating markdown for {case[0]}...")
            md = render_case(*case)
            f.write(md)

if __name__ == "__main__":
    append_to_catalog()
