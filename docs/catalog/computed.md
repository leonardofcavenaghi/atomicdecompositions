---
description: Download exact symbolic quantum multiplication matrices, ordered bases, gradings and supported curve classes for 131 completed localization computations.
---

# Exact computation data

This collection contains **131 completed exact localization computations**, including **32 threefold realizations**. Different realizations are listed separately even when the resulting varieties are isomorphic.

[Download the complete JSON dataset](../data/localization-results.json)

Each record contains the executable algebra/kept-root/bundle input, the full automatically supported curve list in ambient coordinates, the symbolic $c_1(TY)$ multiplication matrix, its specialization at all $y_i=1$, the ordered Schubert basis, and the grading. Rational numbers are stored as exact strings. The matrix acts on the returned ambient sector, with columns as inputs and rows as outputs.

The [additional flag varieties and sections](additional.md) page presents 15 more catalog entries, including the full GM-20 fourfold matrix. Existing projective, Grassmannian and Fanography matrices are linked below.

The dataset was assembled from completed runs of the existing `gwflags` virtual-localization engine. Validation checks executable geometry, supported curve lists, ordered bases, grading, exact specialization, characteristic polynomials and agreement with the displayed matrices. The scope of the ambient computation is described in [Methodology](../methodology.md).

## Use a saved result

```python
import json
from pathlib import Path

data = json.loads(Path("localization-results.json").read_text())
example = next(r for r in data["examples"] if r["id"] == "e1322438fd01")
print(example["input"])
print(example["matrix_symbolic"])
print(example["basis_words"])
```

To recompute a record, construct `FlagVariety` with its algebra and kept roots, parse its bundle using the documented input syntax, and call `small_quantum_multiplication(K)` without restricting the automatic curve list.

| Geometry | Dimension | Fano index | Basis rank | Data identifier |
|---|---|---|---|---|
| [Gr(2,6)](grassmannians.md#gr26) | 8 | 6 | 15 | `1251e5bfa1a6` |
| [P8  Fano index 9](projective.md#p8fanoindex9) | 8 | 9 | 9 | `38cfb4dd44e9` |
| [Fl(1,4,5)](additional.md#fl145) | 7 | 4 | 20 | `6d625eb08919` |
| [Gr(2,6) / O(1)](grassmannians.md#gr26o1) | 7 | 5 | 12 | `a1cae496a552` |
| [P7  Fano index 8](projective.md#p7fanoindex8) | 7 | 8 | 8 | `2b39fd310de2` |
| [P8 / O(2)](projective.md#p8o2) | 7 | 7 | 8 | `4ffe1ade62f4` |
| [P8 / O(3)](projective.md#p8o3) | 7 | 6 | 8 | `765c6cbd0f13` |
| [P8 / O(4)](projective.md#p8o4) | 7 | 5 | 8 | `6604d561e8a4` |
| [P8 / O(5)](projective.md#p8o5) | 7 | 4 | 8 | `15b578599b32` |
| [P8 / O(6)](projective.md#p8o6) | 7 | 3 | 8 | `b7e34220e954` |
| [P8 / O(7)](projective.md#p8o7) | 7 | 2 | 8 | `bcd0369eeffc` |
| [Gr(2,5)](grassmannians.md#gr25) | 6 | 5 | 10 | `add4e2cdc0c7` |
| [Gr(2,6) / O(1)+O(1)](grassmannians.md#gr26o1o1) | 6 | 4 | 10 | `92c91f67a0db` |
| [Gr(2,6) / O(1)+O(2)](grassmannians.md#gr26o1o2) | 6 | 3 | 10 | `58854a726a80` |
| [Gr(3,5)](grassmannians.md#gr35) | 6 | 5 | 10 | `9d177386f50d` |
| [P6  Fano index 7](projective.md#p6fanoindex7) | 6 | 7 | 7 | `7dbd349ec9ab` |
| [P7 / O(2)](projective.md#p7o2) | 6 | 6 | 7 | `12203c19a2ac` |
| [P7 / O(3)](projective.md#p7o3) | 6 | 5 | 7 | `c48a08dcc0ef` |
| [P7 / O(4)](projective.md#p7o4) | 6 | 4 | 7 | `4d98dba9cf55` |
| [P7 / O(5)](projective.md#p7o5) | 6 | 3 | 7 | `8547b3f70ef7` |
| [P7 / O(6)](projective.md#p7o6) | 6 | 2 | 7 | `8c15f95b6325` |
| [P8 / O(2)+O(2)](projective.md#p8o2o2) | 6 | 5 | 7 | `e0a0b3d40922` |
| [P8 / O(2)+O(3)](projective.md#p8o2o3) | 6 | 4 | 7 | `99ac9ea3af4c` |
| [P8 / O(2)+O(4)](projective.md#p8o2o4) | 6 | 3 | 7 | `d5cc160f2e6a` |
| [P8 / O(2)+O(5)](projective.md#p8o2o5) | 6 | 2 | 7 | `11d7c5142e09` |
| [P8 / O(3)+O(3)](projective.md#p8o3o3) | 6 | 3 | 7 | `53a423286d87` |
| [P8 / O(3)+O(4)](projective.md#p8o3o4) | 6 | 2 | 7 | `d8d261b9c52c` |
| [Fl(1,4,5) / O(1,1)+O(1,1)](additional.md#fl145o11o11) | 5 | 2 | 12 | `9cb29c69a3f5` |
| [G2/P1](additional.md#g2p1) | 5 | 5 | 6 | `fd2bd6eae26b` |
| [G2/P2](additional.md#g2p2) | 5 | 3 | 6 | `834882311808` |
| [Gr(2,5) / O(1)](grassmannians.md#gr25o1) | 5 | 4 | 8 | `1584955327b7` |
| [Gr(2,5) / O(2)](grassmannians.md#gr25o2) | 5 | 3 | 8 | `1cd0a9ffb74e` |
| [Gr(2,5) / O(3)](grassmannians.md#gr25o3) | 5 | 2 | 8 | `dd16e36a8997` |
| [Gr(2,6) / O(1)+O(1)+O(1)](grassmannians.md#gr26o1o1o1) | 5 | 3 | 8 | `51706ac77ff7` |
| [Gr(2,6) / O(1)+O(1)+O(2)](grassmannians.md#gr26o1o1o2) | 5 | 2 | 8 | `c7da579d09a1` |
| [Gr(3,5) / O(1)](grassmannians.md#gr35o1) | 5 | 4 | 8 | `1e7394ef8632` |
| [Gr(3,5) / O(2)](grassmannians.md#gr35o2) | 5 | 3 | 8 | `d7857b18eb8e` |
| [Gr(3,5) / O(3)](grassmannians.md#gr35o3) | 5 | 2 | 8 | `ffb644472d2c` |
| [LG(3,6) / O(1)](additional.md#lg36o1) | 5 | 3 | 6 | `141c91366f21` |
| [OG(3,7) / O(2)](additional.md#og37o2) | 5 | 4 | 6 | `76928fabba80` |
| [OG(3,7) / O(3)](additional.md#og37o3) | 5 | 3 | 6 | `29e94da02c49` |
| [OG(3,7) / O(4)](additional.md#og37o4) | 5 | 2 | 6 | `10e047830d24` |
| [P5  Fano index 6](projective.md#p5fanoindex6) | 5 | 6 | 6 | `75f4cdb8997b` |
| [P6 / O(2)](projective.md#p6o2) | 5 | 5 | 6 | `7ccb7c3e0b6b` |
| [P6 / O(3)](projective.md#p6o3) | 5 | 4 | 6 | `c44e0fd4a5b0` |
| [P6 / O(4)](projective.md#p6o4) | 5 | 3 | 6 | `b740ed7ac87d` |
| [P6 / O(5)](projective.md#p6o5) | 5 | 2 | 6 | `ee9c4f882e7c` |
| [P7 / O(2)+O(2)](projective.md#p7o2o2) | 5 | 4 | 6 | `75efe609f198` |
| [P7 / O(2)+O(3)](projective.md#p7o2o3) | 5 | 3 | 6 | `86a2cd927e5d` |
| [P7 / O(2)+O(4)](projective.md#p7o2o4) | 5 | 2 | 6 | `bbd63cac242a` |
| [P7 / O(3)+O(3)](projective.md#p7o3o3) | 5 | 2 | 6 | `0dfe4b49547a` |
| [P8 / O(2)+O(2)+O(2)](projective.md#p8o2o2o2) | 5 | 3 | 6 | `649a71c1db0a` |
| [P8 / O(2)+O(2)+O(3)](projective.md#p8o2o2o3) | 5 | 2 | 6 | `819481252d0a` |
| [Fl(1,2,5) / O(0,1)+O(0,2)+O(1,0) (GM-20)](additional.md#fl125o01o02o10gm20) | 4 | 1 | 9 | `e1322438fd01` |
| [Fl(1,3,4) / O(1,1)](additional.md#fl134o11) | 4 | 2 | 9 | `3ed191207b19` |
| [G2/P2 / O(1)](additional.md#g2p2o1) | 4 | 2 | 5 | `b9a91f8b2a8f` |
| [Gr(2,4)](grassmannians.md#gr24) | 4 | 4 | 6 | `51615a7643a1` |
| [Gr(2,5) / O(1)+O(1)](grassmannians.md#gr25o1o1) | 4 | 3 | 6 | `3c0ee725b9d8` |
| [Gr(2,5) / O(1)+O(2)](grassmannians.md#gr25o1o2) | 4 | 2 | 6 | `5a3a05721152` |
| [Gr(2,5) / O(1)+O(3)](grassmannians.md#gr25o1o3) | 4 | 1 | 6 | `d2a92bddd407` |
| [Gr(2,5) / O(2)+O(2)](grassmannians.md#gr25o2o2) | 4 | 1 | 6 | `71c4061dbdf2` |
| [Gr(3,5) / O(1)+O(1)](grassmannians.md#gr35o1o1) | 4 | 3 | 6 | `fbeb5f79765b` |
| [Gr(3,5) / O(1)+O(2)](grassmannians.md#gr35o1o2) | 4 | 2 | 6 | `0c8674c9ad6f` |
| [Gr(3,5) / O(1)+O(3)](grassmannians.md#gr35o1o3) | 4 | 1 | 6 | `f418dda622c4` |
| [Gr(3,5) / O(2)+O(2)](grassmannians.md#gr35o2o2) | 4 | 1 | 6 | `a6bf73eeb7fb` |
| [Gr(4,5)](grassmannians.md#gr45) | 4 | 5 | 5 | `139781d9fb14` |
| [LG(3,6) / O(1)+O(1)](additional.md#lg36o1o1) | 4 | 2 | 5 | `5a3d521e7212` |
| [OG(3,7) / O(2)+O(2)](additional.md#og37o2o2) | 4 | 2 | 5 | `176397975a00` |
| [P4  Fano index 5](projective.md#p4fanoindex5) | 4 | 5 | 5 | `53078b491137` |
| [P5 / O(2)](projective.md#p5o2) | 4 | 4 | 5 | `8884770b89b8` |
| [P5 / O(3)](projective.md#p5o3) | 4 | 3 | 5 | `31aadf32267f` |
| [P5 / O(4)](projective.md#p5o4) | 4 | 2 | 5 | `8bd58b781863` |
| [P5 / O(5)](projective.md#p5o5) | 4 | 1 | 5 | `61e63b38f5a8` |
| [P6 / O(2)+O(2)](projective.md#p6o2o2) | 4 | 3 | 5 | `e4065b55a49a` |
| [P6 / O(2)+O(3)](projective.md#p6o2o3) | 4 | 2 | 5 | `6324179fa1e1` |
| [P6 / O(2)+O(4)](projective.md#p6o2o4) | 4 | 1 | 5 | `3150500f5723` |
| [P6 / O(3)+O(3)](projective.md#p6o3o3) | 4 | 1 | 5 | `de2575bbb840` |
| [P7 / O(2)+O(2)+O(2)](projective.md#p7o2o2o2) | 4 | 2 | 5 | `d68ecb775686` |
| [P7 / O(2)+O(2)+O(3)](projective.md#p7o2o2o3) | 4 | 1 | 5 | `5ae4d92d2f20` |
| [B2/B / O(1,1)](additional.md#b2bo11) | 3 | 1 | 6 | `34fec398819e` |
| [Fanography 1-10](fanography.md#fano-variety-1-10) | 3 | 1 | 4 | `7d708946a6fa` |
| [Fanography 1-6](fanography.md#fano-variety-1-6) | 3 | 1 | 4 | `e3f3a551d928` |
| [Fanography 1-7](fanography.md#fano-variety-1-7) | 3 | 1 | 4 | `541768cd0738` |
| [Fanography 1-8](fanography.md#fano-variety-1-8) | 3 | 1 | 4 | `8f9e7a526fba` |
| [Fanography 1-9](fanography.md#fano-variety-1-9) | 3 | 1 | 4 | `6f17aaf4290d` |
| [Fanography 2-24](fanography.md#fano-variety-2-24) | 3 | 1 | 6 | `3538d68c1866` |
| [Fanography 2-32](fanography.md#fano-variety-2-32) | 3 | 2 | 6 | `a6cb2e5a95bb` |
| [Fanography 2-34](fanography.md#fano-variety-2-34) | 3 | 1 | 6 | `ea3e323d9fcb` |
| [Fanography 3-11](fanography.md#fano-variety-3-11) | 3 | 1 | 8 | `a8e28f47c77f` |
| [Fanography 3-27](fanography.md#fano-variety-3-27) | 3 | 2 | 8 | `292efbd7ade0` |
| [Fanography 4-1](fanography.md#fano-variety-4-1) | 3 | 1 | 10 | `96d957608200` |
| [Fl(1,3,4) / O(1,1)+O(1,1)](additional.md#fl134o11o11) | 3 | 1 | 6 | `d3154e614ad6` |
| [Gr(2,4) / O(1)](grassmannians.md#gr24o1) | 3 | 3 | 4 | `1841f3a70f74` |
| [Gr(2,4) / O(2)](grassmannians.md#gr24o2) | 3 | 2 | 4 | `0156965bbcb0` |
| [Gr(2,4) / O(3)](grassmannians.md#gr24o3) | 3 | 1 | 4 | `83c013d9bdf4` |
| [Gr(2,5) / O(1)+O(1)+O(1)](grassmannians.md#gr25o1o1o1) | 3 | 2 | 4 | `f443674348ad` |
| [Gr(2,5) / O(1)+O(1)+O(2)](grassmannians.md#gr25o1o1o2) | 3 | 1 | 4 | `4a1a8491be38` |
| [Gr(3,4)](grassmannians.md#gr34) | 3 | 4 | 4 | `92f8f69bd1f8` |
| [Gr(3,5) / O(1)+O(1)+O(1)](grassmannians.md#gr35o1o1o1) | 3 | 2 | 4 | `70aac1aaa08e` |
| [Gr(3,5) / O(1)+O(1)+O(2)](grassmannians.md#gr35o1o1o2) | 3 | 1 | 4 | `d1339713ede4` |
| [Gr(4,5) / O(1)](grassmannians.md#gr45o1) | 3 | 4 | 4 | `005416420233` |
| [Gr(4,5) / O(2)](grassmannians.md#gr45o2) | 3 | 3 | 4 | `6ce465296672` |
| [Gr(4,5) / O(3)](grassmannians.md#gr45o3) | 3 | 2 | 4 | `a408b7769859` |
| [Gr(4,5) / O(4)](grassmannians.md#gr45o4) | 3 | 1 | 4 | `490a4dc43960` |
| [P3  Fano index 4](projective.md#p3fanoindex4) | 3 | 4 | 4 | `ebd198ca1849` |
| [P4 / O(2)](projective.md#p4o2) | 3 | 3 | 4 | `6ceccace2e40` |
| [P4 / O(3)](projective.md#p4o3) | 3 | 2 | 4 | `0743d9764a4a` |
| [P4 / O(4)](projective.md#p4o4) | 3 | 1 | 4 | `1c4486700490` |
| [P5 / O(2)+O(2)](projective.md#p5o2o2) | 3 | 2 | 4 | `420c622c9cb3` |
| [P5 / O(2)+O(3)](projective.md#p5o2o3) | 3 | 1 | 4 | `3834707b4d89` |
| [P6 / O(2)+O(2)+O(2)](projective.md#p6o2o2o2) | 3 | 1 | 4 | `352c4508e307` |
| [Gr(2,4) / O(1)+O(1)](grassmannians.md#gr24o1o1) | 2 | 2 | 3 | `1d67c54eac18` |
| [Gr(2,4) / O(1)+O(2)](grassmannians.md#gr24o1o2) | 2 | 1 | 3 | `c5377008d724` |
| [Gr(3,4) / O(1)](grassmannians.md#gr34o1) | 2 | 3 | 3 | `892655959f06` |
| [Gr(3,4) / O(2)](grassmannians.md#gr34o2) | 2 | 2 | 3 | `53ee7c8af21e` |
| [Gr(3,4) / O(3)](grassmannians.md#gr34o3) | 2 | 1 | 3 | `1fe2cc704593` |
| [Gr(4,5) / O(1)+O(1)](grassmannians.md#gr45o1o1) | 2 | 3 | 3 | `5bdf83aa585a` |
| [Gr(4,5) / O(1)+O(2)](grassmannians.md#gr45o1o2) | 2 | 2 | 3 | `04f8ea67b0d4` |
| [Gr(4,5) / O(1)+O(3)](grassmannians.md#gr45o1o3) | 2 | 1 | 3 | `b1aa6f89ec3e` |
| [Gr(4,5) / O(2)+O(2)](grassmannians.md#gr45o2o2) | 2 | 1 | 3 | `2dd604001dc5` |
| [P2 Fano index 3](projective.md#p2fanoindex3) | 2 | 3 | 3 | `7bea0424f8dd` |
| [P3 / O(2)](projective.md#p3o2) | 2 | 2 | 3 | `c26b71c1c385` |
| [P3 / O(3)](projective.md#p3o3) | 2 | 1 | 3 | `785f6e8bcd76` |
| [P4 / O(2)+O(2)](projective.md#p4o2o2) | 2 | 1 | 3 | `904c41fdd438` |
| [Gr(2,4) / O(1)+O(1)+O(1)](grassmannians.md#gr24o1o1o1) | 1 | 1 | 2 | `8b39618f3aed` |
| [Gr(3,4) / O(1)+O(1)](grassmannians.md#gr34o1o1) | 1 | 2 | 2 | `375785af1f22` |
| [Gr(3,4) / O(1)+O(2)](grassmannians.md#gr34o1o2) | 1 | 1 | 2 | `79dd3601d09b` |
| [Gr(4,5) / O(1)+O(1)+O(1)](grassmannians.md#gr45o1o1o1) | 1 | 2 | 2 | `8156468b738f` |
| [Gr(4,5) / O(1)+O(1)+O(2)](grassmannians.md#gr45o1o1o2) | 1 | 1 | 2 | `af3a5033ba7a` |
| [P2 / O(2)](projective.md#p2o2) | 1 | 1 | 2 | `81b66f277517` |
| [Gr(3,4) / O(1)+O(1)+O(1)](grassmannians.md#gr34o1o1o1) | 0 | 1 | 1 | `c427c3fda1be` |
