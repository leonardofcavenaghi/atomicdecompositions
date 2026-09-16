from gwflags import FlagVariety
from catalog_inputs import selected_legacy_specs

specs = [
    (name, alg, keep, K)
    for name, (alg, keep, K) in selected_legacy_specs("matrix_generation").items()
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

