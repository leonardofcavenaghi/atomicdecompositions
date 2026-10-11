---
description: Exact quantum multiplication matrices and reproducible inputs for additional flag varieties and their complete intersections.
---

# Additional flag varieties and sections

These entries include orthogonal, symplectic, exceptional and partial flag varieties, and complete intersections in them. Each displayed matrix comes from exact `gwflags` virtual localization using the full automatically supported curve list.

Matrices represent multiplication by $c_1(TY)$ on the returned ambient sector, with every Novikov variable set to $1$. Columns are inputs and rows are outputs. The ordered basis below uses reduced Schubert words; `()` is the unit. Basis indices in the download are zero-based.

[Download all symbolic matrices, bases, gradings and curve classes](../data/localization-results.json) or browse [Download matrices and inputs](computed.md). See [How to Use](../how-to-use.md) for input conventions.

| Geometry | Dimension | Fano index | Basis rank |
|---|---|---|---|
| [Fl(1,4,5)](#fl145) | 7 | 4 | 20 |
| [Fl(1,4,5) / O(1,1)+O(1,1)](#fl145o11o11) | 5 | 2 | 12 |
| [G2/P1](#g2p1) | 5 | 5 | 6 |
| [G2/P2](#g2p2) | 5 | 3 | 6 |
| [LG(3,6) / O(1)](#lg36o1) | 5 | 3 | 6 |
| [OG(3,7) / O(2)](#og37o2) | 5 | 4 | 6 |
| [OG(3,7) / O(3)](#og37o3) | 5 | 3 | 6 |
| [OG(3,7) / O(4)](#og37o4) | 5 | 2 | 6 |
| [Fl(1,2,5) / O(0,1)+O(0,2)+O(1,0) (GM-20)](#fl125o01o02o10gm20) | 4 | 1 | 9 |
| [Fl(1,3,4) / O(1,1)](#fl134o11) | 4 | 2 | 9 |
| [G2/P2 / O(1)](#g2p2o1) | 4 | 2 | 5 |
| [LG(3,6) / O(1)+O(1)](#lg36o1o1) | 4 | 2 | 5 |
| [OG(3,7) / O(2)+O(2)](#og37o2o2) | 4 | 2 | 5 |
| [B2/B / O(1,1)](#b2bo11) | 3 | 1 | 6 |
| [Fl(1,3,4) / O(1,1)+O(1,1)](#fl134o11o11) | 3 | 1 | 6 |

---

<span id="fl145"></span>

??? example "Fl(1,4,5)"
    - **Ambient Space:** `A4`
    - **Keep Nodes:** `1,4`
    - **Bundle K:** empty (the flag variety itself)
    - **Dimension:** $7$
    - **Fano Index:** $4$
    - **Basis Rank:** $20$
    - **Exact data identifier:** `6d625eb08919`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 8\\4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 4 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0 & 0 & 0\\0 & 0 & 0 & 4 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 4 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0\\0 & 0 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 4 & 0 & 8 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4\\0 & 0 & 0 & 0 & 0 & 0 & 8 & 4 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 4 & 8 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0 & 8 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 4 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 4 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 4 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 4 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(1)` | 1 |
        | 3 | `(4)` | 1 |
        | 4 | `(1 4)` | 2 |
        | 5 | `(2 1)` | 2 |
        | 6 | `(3 4)` | 2 |
        | 7 | `(1 3 4)` | 3 |
        | 8 | `(2 1 4)` | 3 |
        | 9 | `(2 3 4)` | 3 |
        | 10 | `(3 2 1)` | 3 |
        | 11 | `(1 2 3 4)` | 4 |
        | 12 | `(2 1 3 4)` | 4 |
        | 13 | `(3 2 1 4)` | 4 |
        | 14 | `(4 3 2 1)` | 4 |
        | 15 | `(1 2 1 3 4)` | 5 |
        | 16 | `(2 3 2 1 4)` | 5 |
        | 17 | `(3 4 3 2 1)` | 5 |
        | 18 | `(1 2 3 2 1 4)` | 6 |
        | 19 | `(2 3 4 3 2 1)` | 6 |
        | 20 | `(1 2 3 4 3 2 1)` | 7 |

---

<span id="fl145o11o11"></span>

??? example "Fl(1,4,5) / O(1,1)+O(1,1)"
    - **Ambient Space:** `A4`
    - **Keep Nodes:** `1,4`
    - **Bundle K:** `1,1;1,1`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $12$
    - **Exact data identifier:** `9cb29c69a3f5`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 2 & 2 & 0 & 0 & 0 & 28 & 28 & 16 & 0 & 0 & 12\\2 & 0 & 0 & 2 & 0 & 6 & 0 & 0 & 0 & 4 & 16 & 0\\2 & 0 & 0 & 2 & 6 & 0 & 0 & 0 & 0 & 8 & 20 & 0\\0 & 2 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4\\0 & 2 & 0 & 0 & 0 & 0 & 6 & 2 & 6 & 0 & 0 & 4\\0 & 0 & 2 & 0 & 0 & 0 & 2 & 6 & 0 & 0 & 0 & 4\\0 & 0 & 0 & 2 & -3 & 2 & 0 & 0 & 0 & -3 & -6 & 0\\0 & 0 & 0 & 2 & 5 & 0 & 0 & 0 & 0 & 3 & 6 & 0\\0 & 0 & 0 & 0 & 2 & 2 & 0 & 0 & 0 & 2 & 6 & 0\\0 & 0 & 0 & 0 & 0 & 0 & -4 & -16 & 4 & 0 & 0 & -2\\0 & 0 & 0 & 0 & 0 & 0 & 8 & 12 & 2 & 0 & 0 & 2\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 6 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(1)` | 1 |
        | 3 | `(4)` | 1 |
        | 4 | `(1 4)` | 2 |
        | 5 | `(2 1)` | 2 |
        | 6 | `(3 4)` | 2 |
        | 7 | `(1 3 4)` | 3 |
        | 8 | `(2 1 4)` | 3 |
        | 9 | `(2 3 4)` | 3 |
        | 10 | `(1 2 3 4)` | 4 |
        | 11 | `(2 1 3 4)` | 4 |
        | 12 | `(1 2 1 3 4)` | 5 |

---

<span id="g2p1"></span>

??? example "G2/P1"
    - **Ambient Space:** `G2`
    - **Keep Nodes:** `1`
    - **Bundle K:** empty (the flag variety itself)
    - **Dimension:** $5$
    - **Fano Index:** $5$
    - **Basis Rank:** $6$
    - **Exact data identifier:** `fd2bd6eae26b`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 0 & 5 & 0\\5 & 0 & 0 & 0 & 0 & 5\\0 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 10 & 0 & 0 & 0\\0 & 0 & 0 & 5 & 0 & 0\\0 & 0 & 0 & 0 & 5 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(1)` | 1 |
        | 3 | `(2 1)` | 2 |
        | 4 | `(1 2 1)` | 3 |
        | 5 | `(2 1 2 1)` | 4 |
        | 6 | `(1 2 1 2 1)` | 5 |

---

<span id="g2p2"></span>

??? example "G2/P2"
    - **Ambient Space:** `G2`
    - **Keep Nodes:** `2`
    - **Bundle K:** empty (the flag variety itself)
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $6$
    - **Exact data identifier:** `834882311808`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 3 & 0 & 0 & 6\\3 & 0 & 0 & 3 & 0 & 0\\0 & 9 & 0 & 0 & 3 & 0\\0 & 0 & 6 & 0 & 0 & 3\\0 & 0 & 0 & 9 & 0 & 0\\0 & 0 & 0 & 0 & 3 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(2)` | 1 |
        | 3 | `(1 2)` | 2 |
        | 4 | `(2 1 2)` | 3 |
        | 5 | `(1 2 1 2)` | 4 |
        | 6 | `(2 1 2 1 2)` | 5 |

---

<span id="lg36o1"></span>

??? example "LG(3,6) / O(1)"
    - **Ambient Space:** `C3`
    - **Keep Nodes:** `3`
    - **Bundle K:** `1`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $6$
    - **Exact data identifier:** `141c91366f21`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 6 & 0 & 0 & 0\\3 & 0 & 0 & 3 & 0 & 0\\0 & 6 & 0 & 0 & 6 & 0\\0 & 0 & 12 & 0 & 0 & 6\\0 & 0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 6 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(3)` | 1 |
        | 3 | `(2 3)` | 2 |
        | 4 | `(1 2 3)` | 3 |
        | 5 | `(1 3 2 3)` | 4 |
        | 6 | `(2 1 3 2 3)` | 5 |

---

<span id="og37o2"></span>

??? example "OG(3,7) / O(2)"
    - **Ambient Space:** `B3`
    - **Keep Nodes:** `3`
    - **Bundle K:** `2`
    - **Dimension:** $5$
    - **Fano Index:** $4$
    - **Basis Rank:** $6$
    - **Exact data identifier:** `76928fabba80`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 8 & 0 & 0\\4 & 0 & 0 & 0 & 16 & 0\\0 & 4 & 0 & 0 & 0 & 8\\0 & 0 & 8 & 0 & 0 & 0\\0 & 0 & 0 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 4 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(3)` | 1 |
        | 3 | `(2 3)` | 2 |
        | 4 | `(1 2 3)` | 3 |
        | 5 | `(1 3 2 3)` | 4 |
        | 6 | `(2 1 3 2 3)` | 5 |

---

<span id="og37o3"></span>

??? example "OG(3,7) / O(3)"
    - **Ambient Space:** `B3`
    - **Keep Nodes:** `3`
    - **Bundle K:** `3`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $6$
    - **Exact data identifier:** `29e94da02c49`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 36 & 0 & 0 & 216\\3 & 0 & 0 & 63 & 0 & 0\\0 & 3 & 0 & 0 & 63 & 0\\0 & 0 & 6 & 0 & 0 & 36\\0 & 0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 3 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(3)` | 1 |
        | 3 | `(2 3)` | 2 |
        | 4 | `(1 2 3)` | 3 |
        | 5 | `(1 3 2 3)` | 4 |
        | 6 | `(2 1 3 2 3)` | 5 |

---

<span id="og37o4"></span>

??? example "OG(3,7) / O(4)"
    - **Ambient Space:** `B3`
    - **Keep Nodes:** `3`
    - **Bundle K:** `4`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $6$
    - **Exact data identifier:** `10e047830d24`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 96 & 0 & 26688 & 0 & 1603584\\2 & 0 & 512 & 0 & 78976 & 0\\0 & 2 & 0 & 416 & 0 & 26688\\0 & 0 & 4 & 0 & 512 & 0\\0 & 0 & 0 & 2 & 0 & 96\\0 & 0 & 0 & 0 & 2 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(3)` | 1 |
        | 3 | `(2 3)` | 2 |
        | 4 | `(1 2 3)` | 3 |
        | 5 | `(1 3 2 3)` | 4 |
        | 6 | `(2 1 3 2 3)` | 5 |

---

<span id="fl125o01o02o10gm20"></span>

??? example "Fl(1,2,5) / O(0,1)+O(0,2)+O(1,0) (GM-20)"
    - **Ambient Space:** `A4`
    - **Keep Nodes:** `1,2`
    - **Bundle K:** `0,1;0,2;1,0`
    - **Dimension:** $4$
    - **Fano Index:** $1$
    - **Basis Rank:** $9$
    - **Exact data identifier:** `e1322438fd01`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 12 & 16 & 96 & 84 & 156 & 512 & 672 & 880\\1 & -1 & 6 & 4 & 0 & 8 & 72 & 72 & 160\\1 & 1 & 0 & 12 & 20 & 20 & 132 & 168 & 176\\0 & 1 & 2 & 0 & 0 & 4 & 8 & 8 & 36\\0 & 2 & 1 & 6 & -1 & 10 & 4 & 8 & 36\\0 & 0 & 1 & 0 & 1 & -2 & 16 & 16 & 24\\0 & 0 & 0 & 1 & 3 & 1 & 5 & 12 & 4\\0 & 0 & 0 & 1 & -1 & 2 & -2 & -6 & 4\\0 & 0 & 0 & 0 & 0 & 0 & 3 & 4 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(1)` | 1 |
        | 3 | `(2)` | 1 |
        | 4 | `(1 2)` | 2 |
        | 5 | `(2 1)` | 2 |
        | 6 | `(3 2)` | 2 |
        | 7 | `(1 2 1)` | 3 |
        | 8 | `(1 3 2)` | 3 |
        | 9 | `(1 3 2 1)` | 4 |

    This matrix includes the nonzero degree-5 contributions. The earlier reference stopped at degree 4 and used a different basis in degree 3; see [Reference discrepancies](../discrepancy.md).

---

<span id="fl134o11"></span>

??? example "Fl(1,3,4) / O(1,1)"
    - **Ambient Space:** `A3`
    - **Keep Nodes:** `1,3`
    - **Bundle K:** `1,1`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $9$
    - **Exact data identifier:** `3ed191207b19`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 2 & 2 & 0 & 0 & 0 & 4 & 8 & 0\\2 & 0 & 0 & 2 & 0 & 4 & 0 & 0 & 4\\2 & 0 & 0 & 2 & 4 & 0 & 0 & 0 & 4\\0 & 2 & 2 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 2 & 0 & 0 & 0 & 0 & 2 & 2 & 0\\0 & 0 & 2 & 0 & 0 & 0 & 0 & 2 & 0\\0 & 0 & 0 & 0 & -4 & 4 & 0 & 0 & 0\\0 & 0 & 0 & 6 & 6 & 2 & 0 & 0 & 2\\0 & 0 & 0 & 0 & 0 & 0 & 2 & 4 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(1)` | 1 |
        | 3 | `(3)` | 1 |
        | 4 | `(1 3)` | 2 |
        | 5 | `(2 1)` | 2 |
        | 6 | `(2 3)` | 2 |
        | 7 | `(1 2 3)` | 3 |
        | 8 | `(2 1 3)` | 3 |
        | 9 | `(1 2 1 3)` | 4 |

---

<span id="g2p2o1"></span>

??? example "G2/P2 / O(1)"
    - **Ambient Space:** `G2`
    - **Keep Nodes:** `2`
    - **Bundle K:** `1`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $5$
    - **Exact data identifier:** `b9a91f8b2a8f`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 6 & 0 & 12 & 0\\2 & 0 & 4 & 0 & 4\\0 & 6 & 0 & 6 & 0\\0 & 0 & 4 & 0 & 2\\0 & 0 & 0 & 6 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(2)` | 1 |
        | 3 | `(1 2)` | 2 |
        | 4 | `(2 1 2)` | 3 |
        | 5 | `(1 2 1 2)` | 4 |

---

<span id="lg36o1o1"></span>

??? example "LG(3,6) / O(1)+O(1)"
    - **Ambient Space:** `C3`
    - **Keep Nodes:** `3`
    - **Bundle K:** `1;1`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $5$
    - **Exact data identifier:** `5a3d521e7212`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 8 & 0 & 8 & 0\\2 & 0 & 8 & 0 & 8\\0 & 4 & 0 & 4 & 0\\0 & 0 & 8 & 0 & 8\\0 & 0 & 0 & 2 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(3)` | 1 |
        | 3 | `(2 3)` | 2 |
        | 4 | `(1 2 3)` | 3 |
        | 5 | `(1 3 2 3)` | 4 |

---

<span id="og37o2o2"></span>

??? example "OG(3,7) / O(2)+O(2)"
    - **Ambient Space:** `B3`
    - **Keep Nodes:** `3`
    - **Bundle K:** `2;2`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $5$
    - **Exact data identifier:** `176397975a00`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 16 & 0 & 224 & 0\\2 & 0 & 48 & 0 & 224\\0 & 2 & 0 & 24 & 0\\0 & 0 & 4 & 0 & 16\\0 & 0 & 0 & 2 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(3)` | 1 |
        | 3 | `(2 3)` | 2 |
        | 4 | `(1 2 3)` | 3 |
        | 5 | `(1 3 2 3)` | 4 |

---

<span id="b2bo11"></span>

??? example "B2/B / O(1,1)"
    - **Ambient Space:** `B2`
    - **Keep Nodes:** `1,2`
    - **Bundle K:** `1,1`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $6$
    - **Exact data identifier:** `34fec398819e`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 10 & 10 & 24 & 18 & 24\\1 & -1 & 2 & 8 & 6 & 6\\1 & 3 & -1 & 6 & 2 & 6\\0 & 1 & 2 & -1 & 2 & 2\\0 & 3 & 1 & 3 & -1 & 4\\0 & 0 & 0 & 4 & 3 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(1)` | 1 |
        | 3 | `(2)` | 1 |
        | 4 | `(1 2)` | 2 |
        | 5 | `(2 1)` | 2 |
        | 6 | `(1 2 1)` | 3 |

---

<span id="fl134o11o11"></span>

??? example "Fl(1,3,4) / O(1,1)+O(1,1)"
    - **Ambient Space:** `A3`
    - **Keep Nodes:** `1,3`
    - **Bundle K:** `1,1;1,1`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $6$
    - **Exact data identifier:** `d3154e614ad6`

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 14 & 14 & 72 & 48 & 56\\1 & -1 & 3 & 18 & 14 & 12\\1 & 3 & -1 & 18 & 10 & 12\\0 & 1 & \frac{7}{3} & 2 & 4 & \frac{14}{3}\\0 & 1 & -1 & 0 & -4 & 0\\0 & 0 & 0 & 6 & 4 & 0\end{bmatrix}
        $$

    ??? note "Ordered basis and degrees"

        | Position | Schubert word | Complex codimension |
        |---|---|---|
        | 1 | `()` | 0 |
        | 2 | `(1)` | 1 |
        | 3 | `(3)` | 1 |
        | 4 | `(1 3)` | 2 |
        | 5 | `(2 1)` | 2 |
        | 6 | `(1 2 3)` | 3 |
