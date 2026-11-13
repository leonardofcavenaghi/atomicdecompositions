valid = []

# P^n: Fano index = (n+1) - sum(deg)
for n in range(2, 9):
    alg = f"A{n}"
    keep = [1]
    valid.append((f"P{n}  Fano index {n+1}", alg, keep, []))
    for d1 in range(2, n+2):
        if n + 1 - d1 > 0:
            valid.append((f"P{n} / O({d1})", alg, keep, [[d1]]))
        for d2 in range(d1, n+2):
            if n + 1 - (d1 + d2) > 0:
                valid.append((f"P{n} / O({d1})+O({d2})", alg, keep, [[d1], [d2]]))
            for d3 in range(d2, n+2):
                if n + 1 - (d1 + d2 + d3) > 0:
                    valid.append((f"P{n} / O({d1})+O({d2})+O({d3})", alg, keep, [[d1], [d2], [d3]]))

# Gr(k, n): Fano index = n - sum(deg)
for n in range(4, 8):
    for k in range(2, n):
        alg = f"A{n-1}"
        keep = [k]
        valid.append((f"Gr({k},{n})", alg, keep, []))
        for d1 in range(1, n+1):
            if n - d1 > 0:
                valid.append((f"Gr({k},{n}) / O({d1})", alg, keep, [[d1]]))
            for d2 in range(d1, n+1):
                if n - (d1 + d2) > 0:
                    valid.append((f"Gr({k},{n}) / O({d1})+O({d2})", alg, keep, [[d1], [d2]]))
                for d3 in range(d2, n+1):
                    if n - (d1 + d2 + d3) > 0:
                        valid.append((f"Gr({k},{n}) / O({d1})+O({d2})+O({d3})", alg, keep, [[d1], [d2], [d3]]))

print(f"Total valid Fano cases generated: {len(valid)}")
with open('generated_fano_cases.py', 'w') as f:
    f.write("CASES_100 = [\n")
    for name, alg, keep, degs in valid:
        f.write(f"    ('{name}', '{alg}', {keep}, {degs}, None),\n")
    f.write("]\n")
