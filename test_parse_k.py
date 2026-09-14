from gwflags import FlagVariety
from gwflags.bundles import O, taut_sub, taut_quot, dual, osum, tensor, sym, wedge

def parse_k(spec, X):
    spec = spec.strip()
    if not spec:
        return []
    if any(c.isalpha() for c in spec):
        return eval(spec, {"X": X, "O": O, "taut_sub": taut_sub, "taut_quot": taut_quot, "dual": dual, "osum": osum, "tensor": tensor, "sym": sym, "wedge": wedge})
    return [[int(v) for v in row.split(',')] for row in spec.split(';')]

X = FlagVariety('A3', [2])
# Gr(2,4) has taut_sub(X, 2) and taut_quot(X, 2)
K = parse_k("taut_quot(X, 2)", X)
print("Parsed K:", K)
print("Is valid?", X._check_K(K))

