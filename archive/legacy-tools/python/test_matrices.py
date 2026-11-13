from gwflags import FlagVariety
import sympy

print("=== Example: P^2 Quantum Matrix ===")
X = FlagVariety('A2', [1])
M, Gr, basis = X.small_quantum_multiplication()
print("M for P^2:")
for row in M:
    print([str(sym) for sym in row])

print("\n=== Example: Quadric 3-fold (B2, keep 1) ===")
X2 = FlagVariety('B2', [1])
M2, Gr2, basis2 = X2.small_quantum_multiplication()
print("M for Quadric 3-fold:")
for row in M2:
    print([str(sym) for sym in row])

print("\n=== Example: Gr(2,4) ===")
X3 = FlagVariety('A3', [2])
M3, Gr3, basis3 = X3.small_quantum_multiplication()
print("M for Gr(2,4):")
for row in M3:
    print([str(sym) for sym in row])
