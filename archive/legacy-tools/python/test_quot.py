from gwflags import FlagVariety
from gwflags.bundles import taut_quot

X = FlagVariety('A4', [2])
Q = taut_quot(X, 2)
fano, betas = X.fano_index_and_betas(Q)

print("Fano Index:", fano)
print("Betas:", betas)
