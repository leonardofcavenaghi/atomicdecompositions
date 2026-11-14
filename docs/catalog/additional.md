---
description: Exact quantum multiplication matrices and reproducible inputs for additional flag varieties and their complete intersections.
---

# Flag varieties and sections

These entries include orthogonal, symplectic, exceptional and partial flag varieties, and complete intersections in them. Each displayed matrix comes from exact `gwflags` virtual localization using the full automatically supported curve list.

For a worked full-flag example, see [Fl(1,2,3)](flag_varieties.md#afl123).

Matrices represent multiplication by $c_1(TX)$ on the returned ambient sector, with every Novikov variable set to $1$. Columns are inputs and rows are outputs. The ordered basis below uses reduced Schubert words; `()` is the unit. Basis indices in the download are zero-based.

[Download all symbolic matrices, bases, gradings and curve classes](../data/localization-results.json) or browse [Download matrices and inputs](computed.md). See [How to Use](../how-to-use.md) for input conventions.

| Geometry | Dimension | Ambient index | Basis rank |
|---|---|---|---|
| [Fl(1,4,5)](#fl145) | 7 | 4 | 20 |
| [Fl(1,4,5) / O(1,1)+O(1,1)](#fl145o11o11) | 5 | 2 | 12 |
| [G2/P1](#g2p1) | 5 | 5 | 6 |
| [G2/P2](#g2p2) | 5 | 3 | 6 |
| [LG(3,6) / O(1)](#lg36o1) | 5 | 3 | 6 |
| [OG(3,7) / O(2)](#og37o2) | 5 | 4 | 6 |
| [OG(3,7) / O(3)](#og37o3) | 5 | 3 | 6 |
| [OG(3,7) / O(4)](#og37o4) | 5 | 2 | 6 |
| [Fl(1,2,5) / O(0,1)+O(0,2)+O(1,0)](#fl125o01o02o10gm20) | 4 | 1 | 9 |
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
    - **Ambient Index:** $4$
    - **Basis Rank:** $20$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=2, y4=3`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{20} - 6400 z^{16} - 229376000 z^{12} - 964689920000 z^{8} + 93952409600000 z^{4} - 3435973836800000\) | 20 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=123132100092197157611761412271350402846525195494450646698395299600708971388952916064230858727526878588511525158256640000000000000000000000000000000000000000000000\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{20} - 6400 \lambda^{16} - 229376000 \lambda^{12} - 964689920000 \lambda^{8} + 93952409600000 \lambda^{4} - 3435973836800000=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-higher-dimensional.md#6d625eb08919). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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
    - **Ambient Index:** $2$
    - **Basis Rank:** $12$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=2, y4=3`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 2 |
        | \(z^{10} - 100 z^{8} - 56000 z^{6} - 3680000 z^{4} + 5600000 z^{2} - 3200000\) | 10 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1031207821410880716800000000000000000000000000\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
        | \(\lambda^{10} - 100 \lambda^{8} - 56000 \lambda^{6} - 3680000 \lambda^{4} + 5600000 \lambda^{2} - 3200000=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#9cb29c69a3f5). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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
    - **Ambient Index:** $5$
    - **Basis Rank:** $6$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 1 |
        | \(z^{5} - 12500\) | 5 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=244140625000\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{5} - 12500=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#fd2bd6eae26b). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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
    - **Ambient Index:** $3$
    - **Basis Rank:** $6$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{6} - 486 z^{3} - 19683\) | 6 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=83682825624\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{6} - 486 \lambda^{3} - 19683=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#834882311808). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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
    - **Ambient Index:** $3$
    - **Basis Rank:** $6$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{6} - 648 z^{3} + 11664\) | 6 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=29386561536\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{6} - 648 \lambda^{3} + 11664=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#141c91366f21). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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
    - **Ambient Index:** $4$
    - **Basis Rank:** $6$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 8\) | 1 | 1 |
        | \(z - 8\) | 1 | 1 |
        | \(z\) | 1 | 2 |
        | \(z^{2} + 64\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=8589934592\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 8=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 8=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
        | \(\lambda^{2} + 64=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#76928fabba80). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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
    - **Ambient Index:** $3$
    - **Basis Rank:** $6$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 3 |
        | \(z^{3} - 2916\) | 3 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=114791256\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0,\frac{1}{2},\frac{1}{2}\}\!\}\) |
        | \(\lambda^{3} - 2916=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#29e94da02c49). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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
    - **Ambient Index:** $2$
    - **Basis Rank:** $6$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 64\) | 1 | 1 |
        | \(z - 64\) | 1 | 1 |
        | \(z\) | 1 | 4 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=262144\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 64=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 64=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda=0\) | \(\{\!\{0,0,\frac{1}{2},\frac{1}{2}\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#10e047830d24). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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

??? example "Fl(1,2,5) / O(0,1)+O(0,2)+O(1,0)"
    - **Ambient Space:** `A4`
    - **Keep Nodes:** `1,2`
    - **Bundle K:** `0,1;0,2;1,0`
    - **Dimension:** $4$
    - **Ambient Index:** $1$
    - **Basis Rank:** $9$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=1, y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 3\) | 1 | 2 |
        | \(z + 2\) | 1 | 2 |
        | \(z^{5} - 5 z^{4} - 192 z^{3} - 3848 z^{2} - 17040 z - 22928\) | 5 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-61355573168046080\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 3=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
        | \(\lambda + 2=0\) | \(\{\!\{0,0\}\!\}\) |
        | \(\lambda^{5} - 5 \lambda^{4} - 192 \lambda^{3} - 3848 \lambda^{2} - 17040 \lambda - 22928=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#e1322438fd01). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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

    The full matrix includes nonzero contributions from curve classes of anticanonical degree 5.

---

<span id="fl134o11"></span>

??? example "Fl(1,3,4) / O(1,1)"
    - **Ambient Space:** `A3`
    - **Keep Nodes:** `1,3`
    - **Bundle K:** `1,1`
    - **Dimension:** $4$
    - **Ambient Index:** $2$
    - **Basis Rank:** $9$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=2, y3=3`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 1 |
        | \(z^{8} - 80 z^{6} - 10656 z^{4} - 247040 z^{2} + 256\) | 8 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-1708917900203498930176\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{8} - 80 \lambda^{6} - 10656 \lambda^{4} - 247040 \lambda^{2} + 256=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#3ed191207b19). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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
    - **Ambient Index:** $2$
    - **Basis Rank:** $5$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 1 |
        | \(z^{4} - 72 z^{2} - 432\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=331776\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{4} - 72 \lambda^{2} - 432=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#b9a91f8b2a8f). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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
    - **Ambient Index:** $2$
    - **Basis Rank:** $5$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 1 |
        | \(z^{2} + 8 z - 16\) | 2 | 1 |
        | \(z^{2} - 8 z - 16\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=131072\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{2} + 8 \lambda - 16=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{2} - 8 \lambda - 16=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#5a3d521e7212). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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
    - **Ambient Index:** $2$
    - **Basis Rank:** $5$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 16\) | 1 | 1 |
        | \(z - 16\) | 1 | 1 |
        | \(z\) | 1 | 3 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=4096\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 16=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 16=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda=0\) | \(\{\!\{0,0,0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#176397975a00). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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
    - **Ambient Index:** $1$
    - **Basis Rank:** $6$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=1, y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 2\) | 1 | 2 |
        | \(z^{4} - 90 z^{2} - 428 z - 391\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 2=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
        | \(\lambda^{4} - 90 \lambda^{2} - 428 \lambda - 391=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#34fec398819e). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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
    - **Ambient Index:** $1$
    - **Basis Rank:** $6$

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=2, y3=3`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 5\) | 1 | 2 |
        | \(z^{4} - 816 z^{2} - 11520 z - 37824\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=- \frac{315392}{3}\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 5=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
        | \(\lambda^{4} - 816 \lambda^{2} - 11520 \lambda - 37824=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#d3154e614ad6). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

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
