from gwflags import FlagVariety

specs = [
    ("1-17", "A3", [1], []),
    ("1-16", "A4", [1], [[2]]),
    ("1-15", "A4", [2], [[1], [1], [1]]),
    ("1-14", "A5", [1], [[2], [2]]),
    ("1-13", "A4", [1], [[3]]),
    ("1-7", "A5", [2], [[1], [1], [1], [1], [1]]),
    ("1-5", "A4", [2], [[1], [1], [2]]),
    ("1-4", "A6", [1], [[2], [2], [2]]),
    ("1-3", "A5", [1], [[2], [3]]),
    ("2-24", "A2", [1, 2], [])
]

for name, alg, keep, K in specs:
    print(f"Generating for {name} ({alg} {keep} K={K})")
    try:
        X = FlagVariety(alg, keep)
        if len(K) == 0:
            K_arg = None
        else:
            K_arg = K
        fano, betas = X.fano_index_and_betas(K_arg)
        M, Gr, idx = X.small_quantum_multiplication(K_arg, betas)
        print(f"  Fano index: {fano}")
    except Exception as e:
        print(f"  Error: {e}")

