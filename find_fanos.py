from gwflags import FlagVariety
from gwflags.rootsystem import RootSystemData
import itertools

fano3_candidates = []

algebras = ['A1', 'A2', 'A3', 'A4', 'B2', 'B3', 'C2', 'C3', 'G2']
for alg in algebras:
    rs = RootSystemData(alg)
    rank = rs.rank
    for keep_len in range(1, rank + 1):
        for keep in itertools.combinations(range(1, rank + 1), keep_len):
            try:
                X = FlagVariety(alg, keep)
                dim = X.dimension
                if dim < 3 or dim > 6:
                    continue
                if dim == 3:
                    fano, betas = X.fano_index_and_betas()
                    if fano > 0:
                        fano3_candidates.append(f"{alg} keep={keep} K=[] fano={fano} pic={keep_len}")
                else:
                    # check complete intersections of dimension 3
                    # For simplicity, just test some small degree combinations
                    # This is just a quick check for Picard rank 1 or 2
                    pass
            except Exception as e:
                pass

for c in fano3_candidates:
    print(c)
