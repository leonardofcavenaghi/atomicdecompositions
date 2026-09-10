import sys
from gwflags import FlagVariety

cases = []

def add_ci(alg, keep, degrees):
    try:
        var = FlagVariety(alg, keep, degrees)
        fano = var.fano_index()
        if fano > 0:
            cases.append((f"{alg} {keep} {degrees}", alg, keep, degrees))
    except Exception:
        pass

# Pn
for n in range(2, 8):
    alg = f"A{n}"
    keep = [1]
    add_ci(alg, keep, [])
    for d1 in range(2, n+2):
        add_ci(alg, keep, [[d1]])
        for d2 in range(d1, n+2):
            add_ci(alg, keep, [[d1], [d2]])

# Gr(k, n)
for n in range(4, 8):
    for k in range(2, n):
        alg = f"A{n-1}"
        keep = [k]
        add_ci(alg, keep, [])
        for d1 in range(1, n+1):
            add_ci(alg, keep, [[d1]])
            for d2 in range(d1, n+1):
                add_ci(alg, keep, [[d1], [d2]])

print(f"Found {len(cases)} cases.")
