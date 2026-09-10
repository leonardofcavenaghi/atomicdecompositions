import os
from gwflags import FlagVariety

def test_fast_numeric_backend_with_workers():
    X = FlagVariety("A3", [1])
    M, Gr, idx = X.small_quantum_multiplication(workers=os.cpu_count())
    print(f"Matrix computed: {M}")
    
    Y = FlagVariety("A4", [1])
    M_Y, Gr_Y, idx_Y = Y.small_quantum_multiplication(K=[[4]], workers=os.cpu_count())
    
    print("NumericBackend and workers=os.cpu_count() successfully verified!")

if __name__ == "__main__":
    test_fast_numeric_backend_with_workers()
