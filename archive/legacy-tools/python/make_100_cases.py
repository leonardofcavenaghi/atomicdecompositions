import sys
import sympy
from gwflags import FlagVariety

def fano_check(alg, keep, degrees):
    try:
        var = FlagVariety(alg, keep, degrees)
        fano, _ = var.fano_index_and_betas()
        if fano > 0:
            return True
        return False
    except Exception:
        return False

valid = []

# P^n
for n in range(2, 9):
    alg = f"A{n}"
    keep = [1]
    valid.append((f"P{n} Fano index {n+1}", alg, keep, []))
    for d1 in range(2, n+2):
        if fano_check(alg, keep, [[d1]]):
            valid.append((f"P{n} / O({d1})", alg, keep, [[d1]]))
        for d2 in range(d1, n+2):
            if fano_check(alg, keep, [[d1], [d2]]):
                valid.append((f"P{n} / O({d1})+O({d2})", alg, keep, [[d1], [d2]]))

# Gr(2, n)
for n in range(4, 9):
    alg = f"A{n-1}"
    keep = [2]
    valid.append((f"Gr(2,{n})", alg, keep, []))
    for d1 in range(1, n+1):
        if fano_check(alg, keep, [[d1]]):
            valid.append((f"Gr(2,{n}) / O({d1})", alg, keep, [[d1]]))
        for d2 in range(d1, n+1):
            if fano_check(alg, keep, [[d1], [d2]]):
                valid.append((f"Gr(2,{n}) / O({d1})+O({d2})", alg, keep, [[d1], [d2]]))

print(f"Total valid Fano cases generated: {len(valid)}")
with open('generated_fano_cases.py', 'w') as f:
    f.write("CASES_100 = [\n")
    for name, alg, keep, degs in valid:
        f.write(f"    ('{name}', '{alg}', {keep}, {degs}),\n")
    f.write("]\n")
