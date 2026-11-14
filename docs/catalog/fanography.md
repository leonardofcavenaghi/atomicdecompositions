---
description: Computed small quantum multiplication matrices for Fano threefolds, with Fanography family identifiers and executable virtual-localization inputs.
---

# Fanography 3-Folds

This section records the 105 smooth Fano threefold families from Fanography.
Entries with supported flag-variety inputs include computed ambient matrices;
entries marked **Catalog only** have reference descriptions without a computed matrix.

**Realization types.** Entries labelled direct flag variety or complete intersection can be entered in gwflags. Homogeneous-bundle entries require the corresponding bundle constructor. Catalog-only entries link to reference information; no executable input or computed matrix is provided here.

The displayed matrices are \(A(\mathbf 1)\), first-Chern quantum multiplication on the returned ambient space, with columns as images of the ordered basis. The returned grading is \(G=\operatorname{diag}(\operatorname{codim} e_i-\dim X/2)\). Spectral tables state their own parameter point. See [notation and scope](notation.md).

### Fano Variety 1-1
??? example "1-1"

    **Description:** Double cover / weighted degree-6 hypersurface (Fanography).
    **Realization type:** Catalog only — not represented by the current gwflags flag-variety/ordinary complete-intersection input model.


### Fano Variety 1-2
??? example "1-2"

    - **Ambient Space:** `$A4$`
    - **Keep Nodes:** `1`
    - **Bundle K:** `4`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Hypersurface of degree 4 in $\mathbb{P}^4$; double cover of 1-16 with branch locus a divisor of degree 8.
    - **Realization type:** Line-bundle complete intersection.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z - 232\) | 1 | 1 |
        | \(z + 24\) | 1 | 3 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda - 232=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda + 24=0\) | \(\{\!\{0,\frac{1}{4},\frac{3}{4}\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#1c4486700490). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 3888 & 504576 & 18323712\\1 & 80 & 13600 & 504576\\0 & 1 & 80 & 3888\\0 & 0 & 1 & 0\end{bmatrix}
        $$


### Fano Variety 1-3
??? example "1-3"

    - **Ambient Space:** `$A5$`
    - **Keep Nodes:** `1`
    - **Bundle K:** `2;3`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Complete intersection of a quadric and a cubic in $\mathbb{P}^5$.
    - **Realization type:** Line-bundle complete intersection.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z - 96\) | 1 | 1 |
        | \(z + 12\) | 1 | 3 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda - 96=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda + 12=0\) | \(\{\!\{0,\frac{1}{6},\frac{5}{6}\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#3834707b4d89). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 792 & 43632 & 793152\\1 & 30 & 2340 & 43632\\0 & 1 & 30 & 792\\0 & 0 & 1 & 0\end{bmatrix}
        $$


### Fano Variety 1-4
??? example "1-4"

    - **Ambient Space:** `$A6$`
    - **Keep Nodes:** `1`
    - **Bundle K:** `2;2;2`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Complete intersection of three quadrics in $\mathbb{P}^6$.
    - **Realization type:** Line-bundle complete intersection.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z - 56\) | 1 | 1 |
        | \(z + 8\) | 1 | 3 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda - 56=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda + 8=0\) | \(\{\!\{0,0,0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#352c4508e307). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 304 & 9984 & 121088\\1 & 16 & 800 & 9984\\0 & 1 & 16 & 304\\0 & 0 & 1 & 0\end{bmatrix}
        $$


### Fano Variety 1-5
??? example "1-5"

    - **Ambient Space:** `$A4$`
    - **Keep Nodes:** `2`
    - **Bundle K:** `1;1;2`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Gushel–Mukai threefold: section of Gr(2,5) by two hyperplanes and a quadric.
    - **Realization type:** Line-bundle complete intersection.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 6\) | 1 | 2 |
        | \(z^{2} - 32 z - 244\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=\frac{25}{4}\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 6=0\) | \(\{\!\{0,0\}\!\}\) |
        | \(\lambda^{2} - 32 \lambda - 244=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#4a1a8491be38). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 156 & 1440 & 13248\\1 & 10 & 152 & 1440\\0 & 5/2 & 10 & 156\\0 & 0 & 1 & 0\end{bmatrix}
        $$


### Fano Variety 1-6
??? example "1-6"

    - **Ambient Space:** `$D5$`
    - **Keep Nodes:** `5`
    - **Bundle K:** `1;1;1;1;1;1;1`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Section of the half-spinor embedding of a connected component of $\mathrm{OGr}_+(5,10)$ by codimension 7 subspace.
    - **Realization type:** Line-bundle complete intersection.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y5=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 5\) | 1 | 2 |
        | \(z^{2} - 24 z - 144\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=\frac{12}{7}\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 5=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
        | \(\lambda^{2} - 24 \lambda - 144=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#e3f3a551d928). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 96 & 1692 & 7476\\1 & 7 & 216 & 987\\0 & 1 & 7 & 56\\0 & 0 & \frac{12}{7} & 0\end{bmatrix}
        $$


### Fano Variety 1-7
??? example "1-7"

    - **Ambient Space:** `$A5$`
    - **Keep Nodes:** `2`
    - **Bundle K:** `1;1;1;1;1`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Section of the Plücker embedding of $\mathrm{Gr}(2,6)$ by codimension 5 subspace.
    - **Realization type:** Line-bundle complete intersection.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 5\) | 1 | 1 |
        | \(z - 23\) | 1 | 1 |
        | \(z + 4\) | 1 | 2 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=\frac{196}{25}\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 5=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 23=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda + 4=0\) | \(\{\!\{\frac{1}{6},\frac{5}{6}\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#541768cd0738). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 64 & 330 & 2120\\1 & 5 & 50 & 330\\0 & \frac{14}{5} & 5 & 64\\0 & 0 & 1 & 0\end{bmatrix}
        $$


### Fano Variety 1-8
??? example "1-8"

    - **Ambient Space:** `$C3$`
    - **Keep Nodes:** `3`
    - **Bundle K:** `1;1;1`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Section of the Plücker embedding of $\mathrm{SGr}(3,6)$ by codimension 3 subspace.
    - **Realization type:** Line-bundle complete intersection.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 4\) | 1 | 2 |
        | \(z^{2} - 16 z - 64\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=16\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 4=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
        | \(\lambda^{2} - 16 \lambda - 64=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#8f9e7a526fba). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 48 & 288 & 416\\1 & 4 & 48 & 72\\0 & 2 & 4 & 12\\0 & 0 & 4 & 0\end{bmatrix}
        $$


### Fano Variety 1-9
??? example "1-9"

    - **Ambient Space:** `$G2$`
    - **Keep Nodes:** `2`
    - **Bundle K:** `1;1`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Section of the adjoint $\mathrm{G}_2$-Grassmannian $\mathrm{G}_2\mathrm{Gr}(2,7)$ by codimension 2 subspace.
    - **Realization type:** Line-bundle complete intersection.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 3\) | 1 | 2 |
        | \(z^{2} - 12 z - 72\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=18\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 3=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
        | \(\lambda^{2} - 12 \lambda - 72=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#6f17aaf4290d). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 36 & 126 & 324\\1 & 3 & 24 & 63\\0 & 3 & 3 & 18\\0 & 0 & 2 & 0\end{bmatrix}
        $$


### Fano Variety 1-10
??? example "1-10"

    - **Ambient Space:** `$A6$`
    - **Keep Nodes:** `3`
    - **Bundle K:** `osum(wedge(2, dual(taut_sub(X, 3))), wedge(2, dual(taut_sub(X, 3))), wedge(2, dual(taut_sub(X, 3))))`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Zero locus of $(\bigwedge^2\mathcal{U}^\vee)^{\oplus 3}$ on $\mathrm{Gr}(3,7)$.
    - **Realization type:** Homogeneous-bundle zero locus; independently recomputed with `gwflags`.
    - **Regularized period:** Agrees with the smooth-Fano database entry for $V(3,22)$.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 4\) | 1 | 1 |
        | \(z^{3} - 8 z^{2} - 56 z - 76\) | 3 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=\frac{121}{5}\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 4=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{3} - 8 \lambda^{2} - 56 \lambda - 76=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#7d708946a6fa). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 24 & 90 & 80\\1 & 2 & 20 & 18\\0 & 11/5 & 2 & 24/5\\0 & 0 & 5 & 0\end{bmatrix}
        $$




### Fano Variety 1-11
??? example "1-11"

    **Description:** Double Veronese cone / weighted degree-6 hypersurface (Fanography).
    **Realization type:** Catalog only — not represented by the current gwflags flag-variety/ordinary complete-intersection input model.


### Fano Variety 1-12
??? example "1-12"

    **Description:** Quartic double solid / weighted degree-4 hypersurface (Fanography).
    **Realization type:** Catalog only — not represented by the current gwflags flag-variety/ordinary complete-intersection input model.


### Fano Variety 1-13
??? example "1-13"

    - **Ambient Space:** `$A4$`
    - **Keep Nodes:** `1`
    - **Bundle K:** `3`
    - **Ambient Index:** `2`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Hypersurface of degree 3 in $\mathbb{P}^4$ (smooth cubic threefold).
    - **Realization type:** Line-bundle complete intersection.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 2 |
        | \(z^{2} - 108\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=64\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{\frac{1}{6},\frac{5}{6}\}\!\}\) |
        | \(\lambda^{2} - 108=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#0743d9764a4a). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 12 & 0 & 72\\2 & 0 & 30 & 0\\0 & 2 & 0 & 12\\0 & 0 & 2 & 0\end{bmatrix}
        $$


### Fano Variety 1-14
??? example "1-14"

    - **Ambient Space:** `$A5$`
    - **Keep Nodes:** `1`
    - **Bundle K:** `2;2`
    - **Ambient Index:** `2`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Complete intersection of two quadrics in P⁵.
    - **Realization type:** Line-bundle complete intersection.


    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 8\) | 1 | 1 |
        | \(z - 8\) | 1 | 1 |
        | \(z\) | 1 | 2 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=64\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 8=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 8=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#420c622c9cb3). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 8 & 0 & 32\\2 & 0 & 16 & 0\\0 & 2 & 0 & 8\\0 & 0 & 2 & 0\end{bmatrix}
        $$


### Fano Variety 1-15
??? example "1-15"

    - **Ambient Space:** `$A4$`
    - **Keep Nodes:** `2`
    - **Bundle K:** `1;1;1`
    - **Ambient Index:** `2`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Quintic del Pezzo threefold; section of Plücker embedding of $\mathrm{Gr}(2,5)$ by codimension 3 subspace.
    - **Realization type:** Line-bundle complete intersection.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{4} - 44 z^{2} - 16\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=400\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{4} - 44 \lambda^{2} - 16=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#f443674348ad). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 6 & 0 & 8\\2 & 0 & 4 & 0\\0 & 5 & 0 & 6\\0 & 0 & 2 & 0\end{bmatrix}
        $$


### Fano Variety 1-16
??? example "1-16"

    - **Ambient Space:** `$A4$`
    - **Keep Nodes:** `1`
    - **Bundle K:** `2`
    - **Ambient Index:** `3`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Hypersurface of degree 2 in $\mathbb{P}^4$ (smooth quadric threefold).
    - **Realization type:** Line-bundle complete intersection.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 1 |
        | \(z^{3} - 108\) | 3 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=729\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{3} - 108=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#6ceccace2e40). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 6 & 0\\3 & 0 & 0 & 6\\0 & 3 & 0 & 0\\0 & 0 & 3 & 0\end{bmatrix}
        $$


### Fano Variety 1-17
??? example "1-17"

    - **Ambient Space:** `$A3$`
    - **Keep Nodes:** `1`
    - **Bundle K:** *(none — projective space itself)*
    - **Ambient Index:** `4`
    - **Dimension:** `3`
    - **Basis Rank:** `4`
    - **Description:** Projective space $\mathbb{P}^3$.
    - **Realization type:** Direct flag variety.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 4\) | 1 | 1 |
        | \(z - 4\) | 1 | 1 |
        | \(z^{2} + 16\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=4096\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 4=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 4=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{2} + 16=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#ebd198ca1849). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 4\\4 & 0 & 0 & 0\\0 & 4 & 0 & 0\\0 & 0 & 4 & 0\end{bmatrix}
        $$


### Fano Variety 2-1
??? example "2-1"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-1](https://fanography.info/2-1).


### Fano Variety 2-2
??? example "2-2"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-2](https://fanography.info/2-2).


### Fano Variety 2-3
??? example "2-3"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-3](https://fanography.info/2-3).


### Fano Variety 2-4
??? example "2-4"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-4](https://fanography.info/2-4).


### Fano Variety 2-5
??? example "2-5"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-5](https://fanography.info/2-5).


### Fano Variety 2-6
??? example "2-6"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-6](https://fanography.info/2-6).


### Fano Variety 2-7
??? example "2-7"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-7](https://fanography.info/2-7).


### Fano Variety 2-8
??? example "2-8"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-8](https://fanography.info/2-8).


### Fano Variety 2-9
??? example "2-9"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-9](https://fanography.info/2-9).


### Fano Variety 2-10
??? example "2-10"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-10](https://fanography.info/2-10).


### Fano Variety 2-11
??? example "2-11"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-11](https://fanography.info/2-11).


### Fano Variety 2-12
??? example "2-12"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-12](https://fanography.info/2-12).


### Fano Variety 2-13
??? example "2-13"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-13](https://fanography.info/2-13).


### Fano Variety 2-14
??? example "2-14"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-14](https://fanography.info/2-14).


### Fano Variety 2-15
??? example "2-15"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-15](https://fanography.info/2-15).


### Fano Variety 2-16
??? example "2-16"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-16](https://fanography.info/2-16).


### Fano Variety 2-17
??? example "2-17"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-17](https://fanography.info/2-17).


### Fano Variety 2-18
??? example "2-18"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-18](https://fanography.info/2-18).


### Fano Variety 2-19
??? example "2-19"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-19](https://fanography.info/2-19).


### Fano Variety 2-20
??? example "2-20"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-20](https://fanography.info/2-20).


### Fano Variety 2-21
??? example "2-21"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-21](https://fanography.info/2-21).


### Fano Variety 2-22
??? example "2-22"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-22](https://fanography.info/2-22).


### Fano Variety 2-23
??? example "2-23"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-23](https://fanography.info/2-23).


### Fano Variety 2-24
??? example "2-24"
    - **Ambient Space:** `A2xA2`
    - **Keep Nodes:** `1,3`
    - **Bundle K:** `1,2`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `6`
    - **Description:** Divisor of type (1,2) in P² × P².
    - **Realization type:** Line-bundle complete intersection.



    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=1, y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{2} - 6 z - 23\) | 2 | 1 |
        | \(z^{4} + 6 z^{3} + 35 z^{2} + 78 z + 61\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=21587148\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{2} - 6 \lambda - 23=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{4} + 6 \lambda^{3} + 35 \lambda^{2} + 78 \lambda + 61=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#3538d68c1866). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 2 & 4 & 12 & 12 & 16\\2 & 0 & 3 & 4 & 0 & 3\\1 & 0 & 0 & 2 & 4 & 6\\0 & 1 & 5/2 & 0 & 0 & 1\\0 & 2 & -1/4 & 3 & 0 & 3/2\\0 & 0 & 0 & 5 & 2 & 0\end{bmatrix}
        $$
### Fano Variety 2-25
??? example "2-25"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-25](https://fanography.info/2-25).


### Fano Variety 2-26
??? example "2-26"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-26](https://fanography.info/2-26).


### Fano Variety 2-27
??? example "2-27"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-27](https://fanography.info/2-27).


### Fano Variety 2-28
??? example "2-28"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-28](https://fanography.info/2-28).


### Fano Variety 2-29
??? example "2-29"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-29](https://fanography.info/2-29).


### Fano Variety 2-30
??? example "2-30"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-30](https://fanography.info/2-30).


### Fano Variety 2-31
??? example "2-31"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-31](https://fanography.info/2-31).


### Fano Variety 2-32
??? example "2-32"
    - **Ambient Space:** `A2`
    - **Keep Nodes:** `1,2`
    - **Bundle K:** `—`
    - **Ambient Index:** `2`
    - **Dimension:** `3`
    - **Basis Rank:** `6`
    - **Description:** Full flag variety $Fl(1,2;\mathbb{C}^3)$; divisor of bidegree $(1,1)$ in $\mathbb{P}^2 \times \mathbb{P}^2$.
    - **Realization type:** Direct flag variety (also a divisor in the product embedding).

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=2, y2=3`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{6} - 60 z^{4} - 1392 z^{2} - 8000\) | 6 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=119439360\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{6} - 60 \lambda^{4} - 1392 \lambda^{2} - 8000=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#a6cb2e5a95bb). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix (symbolic in y1, y2)"
        $$
        \begin{bmatrix}0 & 2*y1 & 2*y2 & 0 & 0 & 4*y1*y2\\2 & 0 & 0 & 2*y2 & 0 & 0\\2 & 0 & 0 & 0 & 2*y1 & 0\\0 & 2 & 4 & 0 & 0 & 2*y1\\0 & 4 & 2 & 0 & 0 & 2*y2\\0 & 0 & 0 & 2 & 2 & 0\end{bmatrix}
        $$

### Fano Variety 2-33
??? example "2-33"

    **Description:** Blow-up of P³ along a line (Fanography; outside the current flag/ordinary-CI input model).
    **Realization type:** Catalog only — not represented by the current gwflags flag-variety/ordinary complete-intersection input model.


### Fano Variety 2-34
??? example "2-34"
    - **Ambient Space:** `A1xA2`
    - **Keep Nodes:** `1,2`
    - **Bundle K:** `—`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `6`
    - **Description:** P¹ × P².
    - **Realization type:** Direct product of flag varieties.



    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=1, y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z - 1\) | 1 | 1 |
        | \(z - 5\) | 1 | 1 |
        | \(z^{2} + 7 z + 19\) | 2 | 1 |
        | \(z^{2} - z + 7\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-138679128\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda - 1=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 5=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{2} + 7 \lambda + 19=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{2} - \lambda + 7=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#ea3e323d9fcb). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 2 & 0 & 0 & 3 & 0\\2 & 0 & 0 & 0 & 0 & 3\\3 & 0 & 0 & 2 & 0 & 0\\0 & 3 & 2 & 0 & 0 & 0\\0 & 0 & 3 & 0 & 0 & 2\\0 & 0 & 0 & 3 & 2 & 0\end{bmatrix}
        $$
### Fano Variety 2-35
??? example "2-35"

    **Description:** Blow-up of P³ at a point (Fanography; outside the current flag/ordinary-CI input model).
    **Realization type:** Catalog only — not represented by the current gwflags flag-variety/ordinary complete-intersection input model.


### Fano Variety 2-36
??? example "2-36"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 2-36](https://fanography.info/2-36).


### Fano Variety 3-1
??? example "3-1"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-1](https://fanography.info/3-1).


### Fano Variety 3-2
??? example "3-2"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-2](https://fanography.info/3-2).


### Fano Variety 3-3
??? example "3-3"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-3](https://fanography.info/3-3).


### Fano Variety 3-4
??? example "3-4"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-4](https://fanography.info/3-4).


### Fano Variety 3-5
??? example "3-5"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-5](https://fanography.info/3-5).


### Fano Variety 3-6
??? example "3-6"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-6](https://fanography.info/3-6).


### Fano Variety 3-7
??? example "3-7"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-7](https://fanography.info/3-7).


### Fano Variety 3-8
??? example "3-8"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-8](https://fanography.info/3-8).


### Fano Variety 3-9
??? example "3-9"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-9](https://fanography.info/3-9).


### Fano Variety 3-10
??? example "3-10"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-10](https://fanography.info/3-10).


### Fano Variety 3-11
??? example "3-11"
    - **Ambient Space:** `A1xA1xA2`
    - **Keep Nodes:** `1,2,3`
    - **Bundle K:** `1,1,1`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `8`
    - **Description:** Divisor of tridegree $(1,1,1)$ in $\mathbb{P}^1 \times \mathbb{P}^1 \times \mathbb{P}^2$; a blow-up of the quadric $Q^3$ along a conic.
    - **Realization type:** Line-bundle complete intersection.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=2, y2=3, y3=5`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{8} + 10 z^{7} - 127 z^{6} - 2920 z^{5} - 33342 z^{4} - 234470 z^{3} - 670544 z^{2} - 309240 z + 353425\) | 8 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=13834679905648998704\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{8} + 10 \lambda^{7} - 127 \lambda^{6} - 2920 \lambda^{5} - 33342 \lambda^{4} - 234470 \lambda^{3} - 670544 \lambda^{2} - 309240 \lambda + 353425=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#a8e28f47c77f). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 2 & 2 & 2 & 0 & 3 & 3 & 8\\1 & -1 & 1 & 0 & 0 & 2 & 0 & 3\\1 & 1 & -1 & 0 & 0 & 0 & 2 & 3\\2 & 1 & 1 & 0 & 2 & 2 & 2 & 0\\0 & 1 & 1 & -4 & -2 & -2 & -2 & -2\\0 & 2 & 0 & 3 & 1 & 0 & 2 & 2\\0 & 0 & 2 & 3 & 1 & 2 & 0 & 2\\0 & 0 & 0 & 0 & 2 & 3 & 3 & 0\end{bmatrix}
        $$

### Fano Variety 3-12
??? example "3-12"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-12](https://fanography.info/3-12).


### Fano Variety 3-13
??? example "3-13"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-13](https://fanography.info/3-13).


### Fano Variety 3-14
??? example "3-14"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-14](https://fanography.info/3-14).


### Fano Variety 3-15
??? example "3-15"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-15](https://fanography.info/3-15).


### Fano Variety 3-16
??? example "3-16"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-16](https://fanography.info/3-16).


### Fano Variety 3-17
??? example "3-17"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-17](https://fanography.info/3-17).


### Fano Variety 3-18
??? example "3-18"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-18](https://fanography.info/3-18).


### Fano Variety 3-19
??? example "3-19"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-19](https://fanography.info/3-19).


### Fano Variety 3-20
??? example "3-20"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-20](https://fanography.info/3-20).


### Fano Variety 3-21
??? example "3-21"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-21](https://fanography.info/3-21).


### Fano Variety 3-22
??? example "3-22"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-22](https://fanography.info/3-22).


### Fano Variety 3-23
??? example "3-23"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-23](https://fanography.info/3-23).


### Fano Variety 3-24
??? example "3-24"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-24](https://fanography.info/3-24).


### Fano Variety 3-25
??? example "3-25"

    **Description:** Blow-up of P³ along two lines (Fanography; outside the current flag/ordinary-CI input model).
    **Realization type:** Catalog only — not represented by the current gwflags flag-variety/ordinary complete-intersection input model.


### Fano Variety 3-26
??? example "3-26"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-26](https://fanography.info/3-26).


### Fano Variety 3-27
??? example "3-27"

    - **Ambient Space:** `A1xA1xA1`
    - **Keep Nodes:** `1,2,3`
    - **Bundle K:** *(none — product flag variety)*
    - **Ambient Index:** `2`
    - **Dimension:** `3`
    - **Basis Rank:** `8`
    - **Description:** Product $(\mathbb{P}^1)^3$.
    - **Realization type:** Direct product of flag varieties.

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=2, y2=3, y3=5`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{8} - 160 z^{6} + 5632 z^{4} - 61440 z^{2} + 147456\) | 8 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=15199648742375424\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{8} - 160 \lambda^{6} + 5632 \lambda^{4} - 61440 \lambda^{2} + 147456=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#292efbd7ade0). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 2 & 2 & 2 & 0 & 0 & 0 & 0\\2 & 0 & 0 & 0 & 2 & 2 & 0 & 0\\2 & 0 & 0 & 0 & 2 & 0 & 2 & 0\\2 & 0 & 0 & 0 & 0 & 2 & 2 & 0\\0 & 2 & 2 & 0 & 0 & 0 & 0 & 2\\0 & 2 & 0 & 2 & 0 & 0 & 0 & 2\\0 & 0 & 2 & 2 & 0 & 0 & 0 & 2\\0 & 0 & 0 & 0 & 2 & 2 & 2 & 0\end{bmatrix}
        $$

### Fano Variety 3-28
??? example "3-28"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-28](https://fanography.info/3-28).


### Fano Variety 3-29
??? example "3-29"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-29](https://fanography.info/3-29).


### Fano Variety 3-30
??? example "3-30"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-30](https://fanography.info/3-30).


### Fano Variety 3-31
??? example "3-31"

    **Realization type:** Catalog only — no computed matrix is provided here.

    **Reference:** [Fanography 3-31](https://fanography.info/3-31).


### Fano Variety 4-1
??? example "4-1"
    - **Ambient Space:** `A1xA1xA1xA1`
    - **Keep Nodes:** `1,2,3,4`
    - **Bundle K:** `1,1,1,1`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `10`
    - **Description:** Smooth (1,1,1,1) hypersurface in (P¹)⁴.
    - **Realization type:** Line-bundle complete intersection on a product of flag varieties.



    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y1=1, y2=1, y3=1, y4=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z - 12\) | 1 | 1 |
        | \(z\) | 1 | 4 |
        | \(z + 4\) | 1 | 5 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda - 12=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda=0\) | \(\{\!\{0,0,0,0\}\!\}\) |
        | \(\lambda + 4=0\) | \(\{\!\{0,0,0,\frac{1}{2},\frac{1}{2}\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#96d957608200). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 6 & 6 & 6 & 6 & 12 & 12 & 12 & 12 & 24\\1 & -1 & 1 & 1 & 1 & 4 & 4 & 4 & 2 & 6\\1 & 1 & -1 & 1 & 1 & 4 & 2 & 2 & 4 & 6\\1 & 1 & 1 & -1 & 1 & 2 & 4 & 2 & 4 & 6\\1 & 1 & 1 & 1 & -1 & 2 & 2 & 4 & 2 & 6\\0 & 1 & 1 & -1 & -1 & -2 & 0 & 0 & 0 & 0\\0 & 1 & -1 & 1 & -1 & 0 & -2 & 0 & 0 & 0\\0 & 1 & 1 & 1 & 3 & 2 & 2 & 0 & 2 & 6\\0 & 0 & 2 & 2 & 2 & 2 & 2 & 2 & 0 & 6\\0 & 0 & 0 & 0 & 0 & 2 & 2 & 2 & 2 & 0\end{bmatrix}
        $$
### Fano Variety 4-2
??? example "4-2"
    **Description:** 3-31


### Fano Variety 4-3
??? example "4-3"
    **Description:** 3-17 , 3-27 , 3-28


### Fano Variety 4-4
??? example "4-4"
    **Description:** 3-18 , 3-19 , 3-30


### Fano Variety 4-5
??? example "4-5"
    **Description:** 3-21 , 3-28 , 3-31


### Fano Variety 4-6
??? example "4-6"
    **Description:** 3-25 , 3-27


### Fano Variety 4-7
??? example "4-7"
    **Description:** 3-24 , 3-28


### Fano Variety 4-8
??? example "4-8"
    **Description:** 3-27 , 3-31


### Fano Variety 4-9
??? example "4-9"
    **Description:** 3-25 , 3-26 , 3-28 , 3-30


### Fano Variety 4-10
??? example "4-10"
    **Description:** 3-27 , 3-28


### Fano Variety 4-11
??? example "4-11"
    **Description:** 3-28 , 3-31


### Fano Variety 4-12
??? example "4-12"
    **Description:** 3-30


### Fano Variety 4-13
??? example "4-13"
    **Description:** 3-27 , 3-31


### Fano Variety 5-1
??? example "5-1"
    **Description:** 4-4 , 4-12


### Fano Variety 5-2
??? example "5-2"
    **Description:** 4-9 , 4-11 , 4-12


### Fano Variety 5-3
??? example "5-3"
    **Description:** 4-10


### Fano Variety 6-1
??? example "6-1"
    **Description:** 5-3


### Fano Variety 7-1
??? example "7-1"
    **Description:** 6-1


### Fano Variety 8-1
??? example "8-1"
    **Description:** 7-1


### Fano Variety 9-1
??? example "9-1"
    **Description:** 8-1


### Fano Variety 10-1
??? example "10-1"
    **Description:** yes

