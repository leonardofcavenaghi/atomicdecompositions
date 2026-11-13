from gwflags import FlagVariety

print("Example 1: P^2 GW invariant <pt, pt>_{d=1}")
X = FlagVariety('A2', [1])
val = X.gw([X.pt, X.pt], beta=(1, 0))
print("val:", val)

print("\nExample 2: Gr(2,4) GW invariant <pt, pt>_{d=1}")
X2 = FlagVariety('A3', [2])
# Beta is one for Grassmanian, wait A3 has 3 roots. So beta=(0, 1, 0)? Let's check fano_index_and_betas
fano, betas = X2.fano_index_and_betas()
print("Betas for Gr(2,4):", betas)
val2 = X2.gw([X2.pt, X2.pt], beta=betas[0])
print("val2:", val2)

print("\nExample 3: Cubic surface in P^3")
X3 = FlagVariety('A3', [1])
fano3, betas3 = X3.fano_index_and_betas([[3]])
print("Betas for cubic surface:", betas3)
# To do GW invariant for complete intersection, we need K!
# Let's see if we can do something like <1>_{d=0}? Or some points?
val3 = X3.gw([X3.pt], beta=betas3[0], K=[[3]])
print("val3:", val3)
