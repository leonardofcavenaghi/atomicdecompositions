from gwflags import FlagVariety

X = FlagVariety('A3', [1])
val = X.gw([], beta=(1, 0, 0), K=[[3]])
print("Number of lines on a cubic surface:", val)
