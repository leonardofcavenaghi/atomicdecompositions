---
description: Computed small quantum multiplication matrices for Fano threefolds, with Fanography family identifiers and executable flag and toric localization inputs.
---

# Fanography 3-Folds

This section records all 105 smooth Fano threefold families from [Fanography](https://fanography.info/).
**81 of the 105 families** carry exact computed ambient quantum multiplication operators and connection-exponent data in GEOATOMS: 20 flag-variety and homogeneous-bundle realizations computed in `gwflags`, and 62 smooth toric and toric complete-intersection presentations computed in `gwtoric` (with family `2-32` realized in both models, and 12 additional flag entries independently cross-verified symbolically in `gwtoric`). The remaining 24 families are listed as **Catalog only** reference entries.

**Realization types.** Entries realized directly via root systems and homogeneous bundles display their `gwflags` inputs and \(A(\mathbf 1)\) matrices inline below. Entries realized via smooth projective toric fans and nef complete intersections link directly to their dedicated record pages ([`toric-threefolds.json`](../data/toric-threefolds.json)) with exact ray/cone inputs, symbolic operators \(A(\mathbf y)\), and connection exponents. Catalog-only entries provide geometric descriptions without a computed matrix.

The inline matrices display \(A(\mathbf 1)\), first-Chern quantum multiplication on the returned ambient space, with columns as images of the ordered basis. The returned grading is \(G=\operatorname{diag}(\operatorname{codim} e_i-\dim X/2)\). Spectral tables state their own parameter point. See [notation and scope](notation.md) and [Algebraic-geometry databases](databases.md).

### Fano Variety 1-1
??? example "1-1"

    **Description:** Double cover of $\mathbb{P}^3$ with branch locus a divisor of degree 6. ($\rho(X)=1$, $(-K_X)^3=2$, $h^{1,2}(X)=52$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


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
    - **Toric cross-verification:** Independently verified in `gwtoric` on the positive smooth toric model, matching symbolic operator $A_{\mathrm{flag}}(\mathbf q(\mathbf y))\,C = C\,A_{\mathrm{toric}}(\mathbf y)$ ($\det C = 1$).

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
    - **Toric cross-verification:** Independently verified in `gwtoric` on the positive smooth toric model, matching symbolic operator $A_{\mathrm{flag}}(\mathbf q(\mathbf y))\,C = C\,A_{\mathrm{toric}}(\mathbf y)$ ($\det C = 1$).

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
    - **Toric cross-verification:** Independently verified in `gwtoric` on the positive smooth toric model, matching symbolic operator $A_{\mathrm{flag}}(\mathbf q(\mathbf y))\,C = C\,A_{\mathrm{toric}}(\mathbf y)$ ($\det C = 1$).

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

    **Description:** Hypersurface of degree 6 in $\mathbb{P}(1,1,1,2,3)$. ($\rho(X)=1$, $(-K_X)^3=8$, $h^{1,2}(X)=21$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 1-12
??? example "1-12"

    **Description:** Double cover of $\mathbb{P}^3$ with branch locus a smooth quartic surface. ($\rho(X)=1$, $(-K_X)^3=16$, $h^{1,2}(X)=10$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


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
    - **Toric cross-verification:** Independently verified in `gwtoric` on the positive smooth toric model, matching symbolic operator $A_{\mathrm{flag}}(\mathbf q(\mathbf y))\,C = C\,A_{\mathrm{toric}}(\mathbf y)$ ($\det C = 1$).

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
    - **Toric cross-verification:** Independently verified in `gwtoric` on the positive smooth toric model, matching symbolic operator $A_{\mathrm{flag}}(\mathbf q(\mathbf y))\,C = C\,A_{\mathrm{toric}}(\mathbf y)$ ($\det C = 1$).


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
    - **Toric cross-verification:** Independently verified in `gwtoric` on the positive smooth toric model, matching symbolic operator $A_{\mathrm{flag}}(\mathbf q(\mathbf y))\,C = C\,A_{\mathrm{toric}}(\mathbf y)$ ($\det C = 1$).

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
    - **Toric cross-verification:** Independently verified in `gwtoric` on the positive smooth toric model, matching symbolic operator $A_{\mathrm{flag}}(\mathbf q(\mathbf y))\,C = C\,A_{\mathrm{toric}}(\mathbf y)$ ($\det C = 1$).

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

    **Description:** Blowup of [1-11](#fano-variety-1-11) in an elliptic curve which is the intersection of two divisors from half the anticanonical linear system. ($\rho(X)=2$, $(-K_X)^3=4$, $h^{1,2}(X)=22$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 2-2
??? example "2-2"

    **Description:** Double cover of [2-34](#fano-variety-2-34) with branch locus a $(2,4)$-divisor. ($\rho(X)=2$, $(-K_X)^3=6$, $h^{1,2}(X)=20$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 2-3
??? example "2-3"

    **Description:** Blowup of [1-12](#fano-variety-1-12) in an elliptic curve which is the intersection of two divisors from half the anticanonical linear system. ($\rho(X)=2$, $(-K_X)^3=8$, $h^{1,2}(X)=11$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 2-4
??? example "2-4"

    - **Description:** Blowup of [1-17](#fano-variety-1-17) in the intersection of two cubics.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=10$, $h^{1,2}(X)=10$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-4.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-4)


### Fano Variety 2-5
??? example "2-5"

    - **Description:** Blowup of [1-13](#fano-variety-1-13) in a plane cubic.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=12$, $h^{1,2}(X)=6$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-5.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-5)


### Fano Variety 2-6
??? example "2-6"

    - **Description:** $(2,2)$-divisor on $\mathbb{P}^2\times\mathbb{P}^2$; double cover of [2-32](#fano-variety-2-32) with branch locus an anticanonical divisor.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=12$, $h^{1,2}(X)=9$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-6.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-6)


### Fano Variety 2-7
??? example "2-7"

    - **Description:** Blowup of [1-16](#fano-variety-1-16) in the intersection of two divisors from $|\mathcal{O}_Q(2)|$.
    - **Realization type:** Toric complete intersection of codimension 2 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=14$, $h^{1,2}(X)=5$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-7.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-7)


### Fano Variety 2-8
??? example "2-8"

    **Description:** Double cover of [2-35](#fano-variety-2-35) with branch locus an anticanonical divisor such that the intersection with the exceptional divisor is smooth; double cover of [2-35](#fano-variety-2-35) with branch locus an anticanonical divisor such that the intersection with the exceptional divisor is singular but reduced. ($\rho(X)=2$, $(-K_X)^3=14$, $h^{1,2}(X)=9$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 2-9
??? example "2-9"

    - **Description:** Complete intersection of degree $(1,1)$ and $(2,1)$ in $\mathbb{P}^3\times\mathbb{P}^2$.
    - **Realization type:** Toric complete intersection of codimension 2 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=16$, $h^{1,2}(X)=5$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-9.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-9)


### Fano Variety 2-10
??? example "2-10"

    - **Description:** Blowup of [1-14](#fano-variety-1-14) in an elliptic curve which is an intersection of 2 hyperplanes.
    - **Realization type:** Toric complete intersection of codimension 2 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=16$, $h^{1,2}(X)=3$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-10.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-10)


### Fano Variety 2-11
??? example "2-11"

    - **Description:** Blowup of [1-13](#fano-variety-1-13) in a line.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=18$, $h^{1,2}(X)=5$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-11.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-11)


### Fano Variety 2-12
??? example "2-12"

    - **Description:** Intersection of 3 $(1,1)$-divisors in $\mathbb{P}^3\times\mathbb{P}^3$.
    - **Realization type:** Toric complete intersection of codimension 3 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=20$, $h^{1,2}(X)=3$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-12.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-12)


### Fano Variety 2-13
??? example "2-13"

    - **Description:** Blowup of [1-16](#fano-variety-1-16) in a curve of degree 6 and genus 2.
    - **Realization type:** Toric complete intersection of codimension 3 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=20$, $h^{1,2}(X)=2$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-13.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-13)


### Fano Variety 2-14
??? example "2-14"

    **Description:** Blowup of [1-15](#fano-variety-1-15) in an elliptic curve which is an intersection of 2 hyperplanes. ($\rho(X)=2$, $(-K_X)^3=20$, $h^{1,2}(X)=1$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 2-15
??? example "2-15"

    - **Description:** Blowup of [1-17](#fano-variety-1-17) in the intersection of a quadric and a cubic where the quadric is smooth; blowup of [1-17](#fano-variety-1-17) in the intersection of a quadric and a cubic where the quadric is singular but reduced.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=22$, $h^{1,2}(X)=4$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-15.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-15)


### Fano Variety 2-16
??? example "2-16"

    - **Description:** Blowup of [1-14](#fano-variety-1-14) in a conic.
    - **Realization type:** Toric complete intersection of codimension 2 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=22$, $h^{1,2}(X)=2$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-16.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-16)


### Fano Variety 2-17
??? example "2-17"

    **Description:** Blowup of [1-16](#fano-variety-1-16) in an elliptic curve of degree 5. ($\rho(X)=2$, $(-K_X)^3=24$, $h^{1,2}(X)=1$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 2-18
??? example "2-18"

    - **Description:** Double cover of [2-34](#fano-variety-2-34) with branch locus a divisor of degree $(2,2)$.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=24$, $h^{1,2}(X)=2$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-18.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-18)


### Fano Variety 2-19
??? example "2-19"

    - **Description:** Blowup of [1-14](#fano-variety-1-14) in a line.
    - **Realization type:** Toric complete intersection of codimension 2 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=26$, $h^{1,2}(X)=2$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-19.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-19)


### Fano Variety 2-20
??? example "2-20"

    **Description:** Blowup of [1-15](#fano-variety-1-15) in a twisted cubic. ($\rho(X)=2$, $(-K_X)^3=26$, $h^{1,2}(X)=0$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 2-21
??? example "2-21"

    **Description:** Blowup of [1-16](#fano-variety-1-16) in a twisted quartic. ($\rho(X)=2$, $(-K_X)^3=28$, $h^{1,2}(X)=0$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 2-22
??? example "2-22"

    **Description:** Blowup of [1-15](#fano-variety-1-15) in a conic. ($\rho(X)=2$, $(-K_X)^3=30$, $h^{1,2}(X)=0$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 2-23
??? example "2-23"

    - **Description:** Blowup of [1-16](#fano-variety-1-16) in an intersection of $A\in|\mathcal{O}_Q(1)|$ and $B\in|\mathcal{O}_Q(2)|$ such that $A$ is smooth; blowup of [1-16](#fano-variety-1-16) in an intersection of $A\in|\mathcal{O}_Q(1)|$ and $B\in|\mathcal{O}_Q(2)|$ such that $A$ is singular.
    - **Realization type:** Toric complete intersection of codimension 2 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=30$, $h^{1,2}(X)=1$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-23.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-23)


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
    - **Toric cross-verification:** Independently verified in `gwtoric` on the positive smooth toric model, matching symbolic operator $A_{\mathrm{flag}}(\mathbf q(\mathbf y))\,C = C\,A_{\mathrm{toric}}(\mathbf y)$ ($\det C = -1$).



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

    - **Description:** Blowup of [1-17](#fano-variety-1-17) in an elliptic curve which is an intersection of 2 quadrics.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=32$, $h^{1,2}(X)=1$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-25.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-25)


### Fano Variety 2-26
??? example "2-26"

    **Description:** Blowup of [1-15](#fano-variety-1-15) in a line. ($\rho(X)=2$, $(-K_X)^3=34$, $h^{1,2}(X)=0$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 2-27
??? example "2-27"

    - **Description:** Blowup of [1-17](#fano-variety-1-17) in a twisted cubic.
    - **Realization type:** Toric complete intersection of codimension 2 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=38$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-27.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-27)


### Fano Variety 2-28
??? example "2-28"

    - **Description:** Blowup of [1-17](#fano-variety-1-17) in a plane cubic.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=40$, $h^{1,2}(X)=1$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-28.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-28)


### Fano Variety 2-29
??? example "2-29"

    - **Description:** Blowup of [1-16](#fano-variety-1-16) in a conic.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=40$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-29.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-29)


### Fano Variety 2-30
??? example "2-30"

    - **Description:** Blowup of [1-17](#fano-variety-1-17) in a conic.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=46$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-30.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-30)


### Fano Variety 2-31
??? example "2-31"

    - **Description:** Blowup of [1-16](#fano-variety-1-16) in a line.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=46$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-31.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-31)


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
    - **Toric complete-intersection presentation:** [Divisor of bidegree $(1,1)$ in $\mathbb{P}^2 \times \mathbb{P}^2$](records/fanography-2-32.md) · [Toric atomic invariants](invariants-threefolds.md#fanography-2-32)

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

    - **Description:** Blowup of [1-17](#fano-variety-1-17) in a line.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=54$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-33.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-33)


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
    - **Toric cross-verification:** Independently verified in `gwtoric` on the positive smooth toric model, matching symbolic operator $A_{\mathrm{flag}}(\mathbf q(\mathbf y))\,C = C\,A_{\mathrm{toric}}(\mathbf y)$ ($\det C = 1$).



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

    - **Description:** $\mathrm{Bl}_p\mathbb{P}^3$.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=56$, $h^{1,2}(X)=0$, recorded Chern index $2$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-35.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-35)


### Fano Variety 2-36
??? example "2-36"

    - **Description:** $\mathbb{P}(\mathcal{O}_{\mathbb{P}^2}\oplus\mathcal{O}_{\mathbb{P}^2}(2))$.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=2$, $(-K_X)^3=62$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-2-36.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-2-36)


### Fano Variety 3-1
??? example "3-1"

    **Description:** Double cover of [3-27](#fano-variety-3-27) with branch locus a divisor of degree $(2,2,2)$. ($\rho(X)=3$, $(-K_X)^3=12$, $h^{1,2}(X)=8$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 3-2
??? example "3-2"

    **Description:** Divisor from $|\mathcal{L}^{\otimes 2}\otimes\mathcal{O}(2,3)|$ on the $\mathbb{P}^2$-bundle $\mathbb{P}(\mathcal{O}\oplus\mathcal{O}(-1,-1)^{\oplus 2})$ over $\mathbb{P}^1\times\mathbb{P}^1$ such that $X\cap Y$ is irreducible, and $\mathcal{L}$ is the tautological bundle, and $Y\in|\mathcal{L}|$. ($\rho(X)=3$, $(-K_X)^3=14$, $h^{1,2}(X)=3$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 3-3
??? example "3-3"

    - **Description:** Divisor on $\mathbb{P}^1\times\mathbb{P}^1\times\mathbb{P}^2$ of degree $(1,1,2)$.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=18$, $h^{1,2}(X)=3$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-3.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-3)


### Fano Variety 3-4
??? example "3-4"

    **Description:** Blowup of [2-18](#fano-variety-2-18) in a smooth fiber of the composition of the projection to $\mathbb{P}^1\times\mathbb{P}^2$ with the projection to $\mathbb{P}^2$ of the double cover with the projection. ($\rho(X)=3$, $(-K_X)^3=18$, $h^{1,2}(X)=2$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 3-5
??? example "3-5"

    **Description:** Blowup of [2-34](#fano-variety-2-34) in a curve $C$ of degree $(5,2)$ such that $C\hookrightarrow\mathbb{P}^1\times\mathbb{P}^2\to\mathbb{P}^2$ is an embedding. ($\rho(X)=3$, $(-K_X)^3=20$, $h^{1,2}(X)=0$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 3-6
??? example "3-6"

    - **Description:** Blowup of [1-17](#fano-variety-1-17) in the disjoint union of a line and an elliptic curve of degree 4.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=22$, $h^{1,2}(X)=1$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-6.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-6)


### Fano Variety 3-7
??? example "3-7"

    - **Description:** Blowup of [2-32](#fano-variety-2-32) in an elliptic curve which is the intersection of two divisors from $|-\frac{1}{2}\mathrm{K}_W|$.
    - **Realization type:** Toric complete intersection of codimension 2 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=24$, $h^{1,2}(X)=1$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-7.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-7)


### Fano Variety 3-8
??? example "3-8"

    - **Description:** Divisor from the linear system $|(\alpha\circ\pi_1)^*(\mathcal{O}_{\mathbb{P}^2}(1)\otimes\pi_2^*(\mathcal{O}_{\mathbb{P}^2}(2))|$ where $\pi_i\colon\mathrm{Bl}_1\mathbb{P}^2\times\mathbb{P}^2\to\mathrm{Bl}_1\mathbb{P}^2,\mathbb{P}^2$ are the projections, and $\alpha\colon\mathrm{Bl}_1\mathbb{P}^2\to\mathbb{P}^2$ is the blowup.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=24$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-8.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-8)


### Fano Variety 3-9
??? example "3-9"

    - **Description:** Blowup of the cone over the Veronese of $\mathbb{P}^2$ in $\mathbb{P}^5$ with center the disjoint union of the vertex and a quartic curve on $\mathbb{P}^2$.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=26$, $h^{1,2}(X)=3$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-9.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-9)


### Fano Variety 3-10
??? example "3-10"

    - **Description:** Blowup of [1-16](#fano-variety-1-16) in the disjoint union of 2 conics.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=26$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-10.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-10)


### Fano Variety 3-11
??? example "3-11"

    - **Description:** Blowup of [2-35](#fano-variety-2-35) in an elliptic curve which is the intersection of two divisors from $|-\frac{1}{2}\mathrm{K}_{V_7}|$.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=28$, $h^{1,2}(X)=1$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-11.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-11)


### Fano Variety 3-12
??? example "3-12"

    - **Description:** Blowup of [1-17](#fano-variety-1-17) in the disjoint union of a line and a twisted cubic.
    - **Realization type:** Toric complete intersection of codimension 2 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=28$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-12.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-12)


### Fano Variety 3-13
??? example "3-13"

    - **Description:** Blowup of [2-32](#fano-variety-2-32) in a curve $C$ of bidegree $(2,2)$ such that the composition $C\hookrightarrow W\hookrightarrow\mathbb{P}^2\times\mathbb{P}^2\overset{p_i}{\to}\mathbb{P}^2$ is an embedding for $i=1,2$.
    - **Realization type:** Toric complete intersection of codimension 3 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=30$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-13.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-13)


### Fano Variety 3-14
??? example "3-14"

    **Description:** Blowup of [1-17](#fano-variety-1-17) in the disjoint union of a plane cubic curve and a point outside the plane. ($\rho(X)=3$, $(-K_X)^3=32$, $h^{1,2}(X)=1$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 3-15
??? example "3-15"

    - **Description:** Blowup of [1-16](#fano-variety-1-16) in the disjoint union of a line and a conic.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=32$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-15.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-15)


### Fano Variety 3-16
??? example "3-16"

    **Description:** Blowup of [2-35](#fano-variety-2-35) in the proper transform of a twisted cubic containing the center of the blowup. ($\rho(X)=3$, $(-K_X)^3=34$, $h^{1,2}(X)=0$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 3-17
??? example "3-17"
    - **Ambient Space:** `A1xA1xA2`
    - **Keep Nodes:** `1,2,3`
    - **Bundle K:** `1,1,1`
    - **Ambient Index:** `1`
    - **Dimension:** `3`
    - **Basis Rank:** `8`
    - **Description:** Divisor of tridegree $(1,1,1)$ in $\mathbb P^1\times\mathbb P^1\times\mathbb P^2$, with anticanonical volume $36$ and $h^{1,2}=0$.
    - **Realization type:** Line-bundle complete intersection.
    - **Toric cross-verification:** Independently verified in `gwtoric` on the positive smooth toric model, matching symbolic operator $A_{\mathrm{flag}}(\mathbf q(\mathbf y))\,C = C\,A_{\mathrm{toric}}(\mathbf y)$ ($\det C = -2$).

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

    **Classification reference:** [Fanography 3-17](https://fanography.info/3-17/).

### Fano Variety 3-18
??? example "3-18"

    - **Description:** Blowup of [1-17](#fano-variety-1-17) in the disjoint union of a line and a conic.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=36$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-18.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-18)


### Fano Variety 3-19
??? example "3-19"

    - **Description:** Blowup of [1-16](#fano-variety-1-16) in two non-collinear points.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=38$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-19.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-19)


### Fano Variety 3-20
??? example "3-20"

    - **Description:** Blowup of [1-16](#fano-variety-1-16) in the disjoint union of two lines.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=38$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-20.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-20)


### Fano Variety 3-21
??? example "3-21"

    - **Description:** Blowup of [2-34](#fano-variety-2-34) in a curve of degree $(2,1)$.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=38$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-21.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-21)


### Fano Variety 3-22
??? example "3-22"

    - **Description:** Blowup of [2-34](#fano-variety-2-34) in a conic on $\{x\}\times\mathbb{P}^2$, $x\in\mathbb{P}^1$.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=40$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-22.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-22)


### Fano Variety 3-23
??? example "3-23"

    - **Description:** Blowup of [2-35](#fano-variety-2-35) in the proper transform of a conic containing the center of the blowup.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=42$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-23.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-23)


### Fano Variety 3-24
??? example "3-24"

    - **Description:** The fiber product of [2-32](#fano-variety-2-32) with $\mathrm{Bl}_p\mathbb{P}^2$ over $\mathbb{P}^2$.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=42$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-24.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-24)


### Fano Variety 3-25
??? example "3-25"

    - **Description:** Blowup of [1-17](#fano-variety-1-17) in the disjoint union of two lines.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=44$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-25.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-25)


### Fano Variety 3-26
??? example "3-26"

    - **Description:** Blowup of [1-17](#fano-variety-1-17) in the disjoint union of a point and a line.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=46$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-26.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-26)


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
    - **Toric cross-verification:** Independently verified in `gwtoric` on the positive smooth toric model, matching symbolic operator $A_{\mathrm{flag}}(\mathbf q(\mathbf y))\,C = C\,A_{\mathrm{toric}}(\mathbf y)$ ($\det C = 1$).

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

    - **Description:** $\mathbb{P}^1\times\mathrm{Bl}_p\mathbb{P}^2$.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=48$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-28.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-28)


### Fano Variety 3-29
??? example "3-29"

    - **Description:** Blowup of [2-35](#fano-variety-2-35) in a line on the exceptional divisor.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=50$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-29.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-29)


### Fano Variety 3-30
??? example "3-30"

    - **Description:** Blowup of [2-35](#fano-variety-2-35) in the proper transform of a line containing the center of the blowup.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=50$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-30.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-30)


### Fano Variety 3-31
??? example "3-31"

    - **Description:** Blowup of the cone over a smooth quadric in $\mathbb{P}^3$ in the vertex.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=3$, $(-K_X)^3=52$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-3-31.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-3-31)


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
    - **Toric cross-verification:** Independently verified in `gwtoric` on the positive smooth toric model, matching symbolic operator $A_{\mathrm{flag}}(\mathbf q(\mathbf y))\,C = C\,A_{\mathrm{toric}}(\mathbf y)$ ($\det C = -1$).



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

    - **Description:** Blowup of the cone over a smooth quadric in $\mathbb{P}^3$ in the disjoint union of the vertex and an elliptic curve on the quadric.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=4$, $(-K_X)^3=28$, $h^{1,2}(X)=1$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-4-2.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-4-2)


### Fano Variety 4-3
??? example "4-3"

    - **Description:** Blowup of [3-27](#fano-variety-3-27) in a curve of degree $(1,1,2)$.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=4$, $(-K_X)^3=30$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $10$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-4-3.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-4-3)


### Fano Variety 4-4
??? example "4-4"

    - **Description:** Blowup of [3-19](#fano-variety-3-19) in the proper transform of a conic through the points.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=4$, $(-K_X)^3=32$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-4-4.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-4-4)


### Fano Variety 4-5
??? example "4-5"

    **Description:** Blowup of [2-34](#fano-variety-2-34) in the disjoint union of a curve of degree $(2,1)$ and a curve of degree $(1,0)$. ($\rho(X)=4$, $(-K_X)^3=32$, $h^{1,2}(X)=0$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 4-6
??? example "4-6"

    - **Description:** Blowup of [1-17](#fano-variety-1-17) in the disjoint union of 3 lines.
    - **Realization type:** Toric complete intersection of codimension 2 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=4$, $(-K_X)^3=34$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $10$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-4-6.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-4-6)


### Fano Variety 4-7
??? example "4-7"

    - **Description:** Blowup of [2-32](#fano-variety-2-32) in the disjoint union of a curve of degree $(0,1)$ and a curve of degree $(1,0)$.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=4$, $(-K_X)^3=36$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $10$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-4-7.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-4-7)


### Fano Variety 4-8
??? example "4-8"

    - **Description:** Blowup of [3-27](#fano-variety-3-27) in a curve of degree $(0,1,1)$.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=4$, $(-K_X)^3=38$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $10$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-4-8.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-4-8)


### Fano Variety 4-9
??? example "4-9"

    - **Description:** Blowup of [3-25](#fano-variety-3-25) in an exceptional curve of the blowup.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=4$, $(-K_X)^3=40$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $10$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-4-9.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-4-9)


### Fano Variety 4-10
??? example "4-10"

    - **Description:** $\mathbb{P}^1\times\mathrm{Bl}_2\mathbb{P}^2$.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=4$, $(-K_X)^3=42$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $10$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-4-10.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-4-10)


### Fano Variety 4-11
??? example "4-11"

    - **Description:** Blowup of [3-28](#fano-variety-3-28) in $\{x\}\times E$, $x\in\mathbb{P}^1$ and $E$ the $(-1)$-curve.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=4$, $(-K_X)^3=44$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $10$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-4-11.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-4-11)


### Fano Variety 4-12
??? example "4-12"

    - **Description:** Blowup of [2-33](#fano-variety-2-33) in the disjoint union of two exceptional lines of the blowup.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=4$, $(-K_X)^3=46$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $10$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-4-12.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-4-12)


### Fano Variety 4-13
??? example "4-13"

    **Description:** Blowup of [3-27](#fano-variety-3-27) in a curve of degree $(1,1,3)$. ($\rho(X)=4$, $(-K_X)^3=26$, $h^{1,2}(X)=0$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 5-1
??? example "5-1"

    **Description:** Blowup of [2-29](#fano-variety-2-29) in the disjoint union of three exceptional lines of the blowup. ($\rho(X)=5$, $(-K_X)^3=28$, $h^{1,2}(X)=0$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 5-2
??? example "5-2"

    - **Description:** Blowup of [3-25](#fano-variety-3-25) in the disjoint union of two exceptional lines on the same irreducible component.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=5$, $(-K_X)^3=36$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $12$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-5-2.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-5-2)


### Fano Variety 5-3
??? example "5-3"

    - **Description:** $\mathbb{P}^1\times\mathrm{Bl}_3\mathbb{P}^2$.
    - **Realization type:** Smooth projective toric threefold (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=5$, $(-K_X)^3=36$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $12$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-5-3.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-5-3)


### Fano Variety 6-1
??? example "6-1"

    - **Description:** $\mathbb{P}^1\times\mathrm{Bl}_4\mathbb{P}^2$.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=6$, $(-K_X)^3=30$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $8$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-6-1.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-6-1)


### Fano Variety 7-1
??? example "7-1"

    - **Description:** $\mathbb{P}^1\times\mathrm{Bl}_5\mathbb{P}^2$.
    - **Realization type:** Toric complete intersection of codimension 2 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=7$, $(-K_X)^3=24$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-7-1.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-7-1)


### Fano Variety 8-1
??? example "8-1"

    - **Description:** $\mathbb{P}^1\times\mathrm{Bl}_6\mathbb{P}^2$.
    - **Realization type:** Toric complete intersection of codimension 1 (`gwtoric` positive curve enumeration).
    - **Invariants:** $\rho(X)=8$, $(-K_X)^3=18$, $h^{1,2}(X)=0$, recorded Chern index $1$, ambient rank $6$.
    - **Exact data and invariants:** [Exact toric inputs, symbolic operator $A(\mathbf y)$, and connection exponents](records/fanography-8-1.md) · [Hodge data and atomic invariants](invariants-threefolds.md#fanography-8-1)


### Fano Variety 9-1
??? example "9-1"

    **Description:** $\mathbb{P}^1\times\mathrm{Bl}_7\mathbb{P}^2$. ($\rho(X)=9$, $(-K_X)^3=12$, $h^{1,2}(X)=0$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.


### Fano Variety 10-1
??? example "10-1"

    **Description:** $\mathbb{P}^1\times\mathrm{Bl}_8\mathbb{P}^2$. ($\rho(X)=10$, $(-K_X)^3=6$, $h^{1,2}(X)=0$).
    **Realization type:** Catalog only — outside the current flag and positive-toric complete-intersection models.

See [Algebraic-geometry databases](databases.md) for Fanography and related algebraic-geometry databases.
