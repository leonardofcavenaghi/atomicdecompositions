from gwflags import FlagVariety

print("=== Eigenvalues for P^2 ===")
X = FlagVariety('A2', [1])
M, Gr, basis = X.small_quantum_multiplication()
eigs = X.eigenvalues(M)
print(eigs)

print("\n=== Eigenvalues for Gr(2,4) ===")
X3 = FlagVariety('A3', [2])
M3, Gr3, basis3 = X3.small_quantum_multiplication()
eigs3 = X3.eigenvalues(M3)
print(eigs3)
