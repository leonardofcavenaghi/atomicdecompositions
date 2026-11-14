---
description: Quantum multiplication matrices for Grassmannians and their Fano complete intersections, with reproducible gwflags inputs.
---

# Grassmannians

**Index convention:** the displayed **Ambient Index** is the software's ambient
Chern gcd. A smooth conic has geometric index 2 even when this field is 1;
the zero-dimensional linear section is a point, for which this gcd does not
define a geometric Fano index. See the [catalog conventions](index.md).

This section contains complete intersections inside this geometric family, systematically organized by dimension and ambient index.

For the kept-root beta convention and copyable browser/CLI syntax, see [How to Use](../how-to-use.md).

The displayed matrices are \(A(\mathbf 1)\), first-Chern quantum multiplication on the returned ambient space, with columns as images of the ordered basis. The returned grading is \(G=\operatorname{diag}(\operatorname{codim} e_i-\dim X/2)\). Spectral tables state their own parameter point. See [notation and scope](notation.md).

## Reproduce an entry in the software

For a Grassmannian `Gr(k,n)`, run `A(n-1)` with **Kept simple roots** `k`.
Each displayed `/ O(d)` is one row in **Bundle K**: enter `d`, or enter
`d1;d2;...` for several summands. For example, `Gr(2,6) / O(1)+O(2)` is
`A5`, kept roots `2`, and Bundle K `1;2` (or `[[1],[2]]` in Python). The
card's dimension is `k(n-k)` minus the number of rows, and its ambient index is
`n - sum(d)`. This convention also covers the dual presentation
`Gr(n-k,n)` shown in the catalog.

## 8-folds

| Geometry | Ambient Index | Basis Rank |
|---|---|---|
| [Gr(2,6)](#gr26) | 6 | 15 |

---

<span id="gr26"></span>
??? example "Gr(2,6)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $8$
    - **Ambient Index:** $6$
    - **Basis Rank:** $15$
    - **Eigenvalues:** $- 6 \sqrt{3}$ (mult: 1), $6 \sqrt{3}$ (mult: 1), $- 6 i$ (mult: 1), $6 i$ (mult: 1), $- 3 \sqrt{3} - 3 i$ (mult: 1), $- 3 \sqrt{3} + 3 i$ (mult: 1), $3 \sqrt{3} - 3 i$ (mult: 1), $3 \sqrt{3} + 3 i$ (mult: 1), $- 6 \sqrt{- \frac{3}{2} - \frac{3 \sqrt{3} i}{2}}$ (mult: 1), $- 6 \sqrt{- \frac{3}{2} + \frac{3 \sqrt{3} i}{2}}$ (mult: 1), $6 \sqrt{- \frac{3}{2} - \frac{3 \sqrt{3} i}{2}}$ (mult: 1), $6 \sqrt{- \frac{3}{2} + \frac{3 \sqrt{3} i}{2}}$ (mult: 1), $0$ (mult: 3)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 3 |
        | \(z^{2} - 108\) | 2 | 1 |
        | \(z^{2} + 36\) | 2 | 1 |
        | \(z^{4} - 36 z^{2} + 1296\) | 4 | 1 |
        | \(z^{4} + 108 z^{2} + 11664\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0,0,0\}\!\}\) |
        | \(\lambda^{2} - 108=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{2} + 36=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{4} - 36 \lambda^{2} + 1296=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{4} + 108 \lambda^{2} + 11664=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-higher-dimensional.md#1251e5bfa1a6). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 0 & 0 & 0 & 0 & 0\\6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 0 & 0 & 0\\0 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 0\\0 & 0 & 6 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6\\0 & 0 & 0 & 0 & 6 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 6 & 0 & 6 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 6 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 6 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 6 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 0\end{bmatrix}
        $$



---

## 7-folds

| Geometry | Ambient Index | Basis Rank |
|---|---|---|
| [Gr(2,6) / O(1)](#gr26o1) | 5 | 12 |

---

<span id="gr26o1"></span>
??? example "Gr(2,6) / O(1)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $7$
    - **Ambient Index:** $5$
    - **Basis Rank:** $12$
    - **Eigenvalues:** $-5$ (mult: 1), $- \frac{5 \sqrt{5}}{4} + \frac{5}{4} - 5 i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5 \sqrt{5}}{4} + \frac{5}{4} + 5 i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $\frac{5}{4} + \frac{5 \sqrt{5}}{4} - 5 i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $\frac{5}{4} + \frac{5 \sqrt{5}}{4} + 5 i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $5 \cdot 3^{\frac{3}{5}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} - \frac{5 \cdot 3^{\frac{3}{5}}}{4} - 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} - \frac{5 \cdot 3^{\frac{3}{5}}}{4} + 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}}}{4} + \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} - 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}}}{4} + \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} + 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $0$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 5\) | 1 | 1 |
        | \(z\) | 1 | 2 |
        | \(z^{4} - 5 z^{3} + 25 z^{2} - 125 z + 625\) | 4 | 1 |
        | \(z^{5} - 84375\) | 5 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 5=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda=0\) | \(\{\!\{\frac{1}{6},\frac{5}{6}\}\!\}\) |
        | \(\lambda^{4} - 5 \lambda^{3} + 25 \lambda^{2} - 125 \lambda + 625=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{5} - 84375=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-higher-dimensional.md#a1cae496a552). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 0 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & 0\\5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 5 & 0 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 0\\0 & 0 & 5 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5\\0 & 0 & 0 & 0 & 5 & 10 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 5 & -5 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 5 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 10 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 0\end{bmatrix}
        $$



---

## 6-folds

| Geometry | Ambient Index | Basis Rank |
|---|---|---|
| [Gr(2,5)](#gr25) | 5 | 10 |
| [Gr(3,5)](#gr35) | 5 | 10 |
| [Gr(2,6) / O(1)+O(1)](#gr26o1o1) | 4 | 10 |
| [Gr(2,6) / O(1)+O(2)](#gr26o1o2) | 3 | 10 |

---

<span id="gr25"></span>
??? example "Gr(2,5)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $6$
    - **Ambient Index:** $5$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $\frac{5}{2} - \frac{5 \sqrt{5}}{2}$ (mult: 1), $\frac{5}{2} + \frac{5 \sqrt{5}}{2}$ (mult: 1), $\frac{5}{2} - 5 \sqrt{- \frac{5}{4} - \frac{\sqrt{5}}{2}}$ (mult: 1), $\frac{5}{2} - 5 \sqrt{- \frac{5}{4} + \frac{\sqrt{5}}{2}}$ (mult: 1), $\frac{5}{2} + 5 \sqrt{- \frac{5}{4} - \frac{\sqrt{5}}{2}}$ (mult: 1), $\frac{5}{2} + 5 \sqrt{- \frac{5}{4} + \frac{\sqrt{5}}{2}}$ (mult: 1), $- \frac{15}{4} + \frac{5 \sqrt{5}}{4} - 5 \sqrt{- \frac{5}{8} + \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{15}{4} - \frac{5 \sqrt{5}}{4} - 5 \sqrt{- \frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{15}{4} - \frac{5 \sqrt{5}}{4} + 5 \sqrt{- \frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{15}{4} + \frac{5 \sqrt{5}}{4} + 5 \sqrt{- \frac{5}{8} + \frac{\sqrt{5}}{8}}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{2} - 5 z - 25\) | 2 | 1 |
        | \(z^{4} + 15 z^{3} + 100 z^{2} + 250 z + 625\) | 4 | 1 |
        | \(z^{4} - 10 z^{3} + 100 z^{2} - 375 z + 625\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=88817841970012523233890533447265625\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{2} - 5 \lambda - 25=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{4} + 15 \lambda^{3} + 100 \lambda^{2} + 250 \lambda + 625=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{4} - 10 \lambda^{3} + 100 \lambda^{2} - 375 \lambda + 625=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-higher-dimensional.md#add4e2cdc0c7). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 0 & 0 & 0 & 5 & 0 & 0 & 0\\5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5\\0 & 0 & 5 & 5 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 5 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 5 & 5 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 0\end{bmatrix}
        $$


---

<span id="gr35"></span>
??? example "Gr(3,5)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $6$
    - **Ambient Index:** $5$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $\frac{5}{2} - \frac{5 \sqrt{5}}{2}$ (mult: 1), $\frac{5}{2} + \frac{5 \sqrt{5}}{2}$ (mult: 1), $\frac{5}{2} - 5 \sqrt{- \frac{5}{4} - \frac{\sqrt{5}}{2}}$ (mult: 1), $\frac{5}{2} - 5 \sqrt{- \frac{5}{4} + \frac{\sqrt{5}}{2}}$ (mult: 1), $\frac{5}{2} + 5 \sqrt{- \frac{5}{4} - \frac{\sqrt{5}}{2}}$ (mult: 1), $\frac{5}{2} + 5 \sqrt{- \frac{5}{4} + \frac{\sqrt{5}}{2}}$ (mult: 1), $- \frac{15}{4} + \frac{5 \sqrt{5}}{4} - 5 \sqrt{- \frac{5}{8} + \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{15}{4} - \frac{5 \sqrt{5}}{4} - 5 \sqrt{- \frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{15}{4} - \frac{5 \sqrt{5}}{4} + 5 \sqrt{- \frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{15}{4} + \frac{5 \sqrt{5}}{4} + 5 \sqrt{- \frac{5}{8} + \frac{\sqrt{5}}{8}}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{2} - 5 z - 25\) | 2 | 1 |
        | \(z^{4} + 15 z^{3} + 100 z^{2} + 250 z + 625\) | 4 | 1 |
        | \(z^{4} - 10 z^{3} + 100 z^{2} - 375 z + 625\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=88817841970012523233890533447265625\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{2} - 5 \lambda - 25=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{4} + 15 \lambda^{3} + 100 \lambda^{2} + 250 \lambda + 625=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{4} - 10 \lambda^{3} + 100 \lambda^{2} - 375 \lambda + 625=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-higher-dimensional.md#9d177386f50d). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 0 & 0 & 0 & 5 & 0 & 0 & 0\\5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5\\0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 5 & 5 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 5 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 5 & 5 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 0\end{bmatrix}
        $$


---

<span id="gr26o1o1"></span>
??? example "Gr(2,6) / O(1)+O(1)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $6$
    - **Ambient Index:** $4$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 4 \cdot 3^{\frac{3}{4}}$ (mult: 1), $4 \cdot 3^{\frac{3}{4}}$ (mult: 1), $- 4 \cdot 3^{\frac{3}{4}} i$ (mult: 1), $4 \cdot 3^{\frac{3}{4}} i$ (mult: 1), $- 2 \sqrt{2} - 2 \sqrt{2} i$ (mult: 1), $- 2 \sqrt{2} + 2 \sqrt{2} i$ (mult: 1), $2 \sqrt{2} - 2 \sqrt{2} i$ (mult: 1), $2 \sqrt{2} + 2 \sqrt{2} i$ (mult: 1), $0$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 2 |
        | \(z^{4} - 6912\) | 4 | 1 |
        | \(z^{4} + 256\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{\frac{1}{3},\frac{2}{3}\}\!\}\) |
        | \(\lambda^{4} - 6912=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{4} + 256=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-higher-dimensional.md#92c91f67a0db). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 0 & 4 & 8 & 0 & 0 & 0 & 0\\4 & 0 & 0 & 0 & 0 & 0 & 8 & 4 & 0 & 0\\0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0\\0 & 0 & 4 & 4 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 4\\0 & 0 & 0 & 0 & 4 & 8 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 4 & -4 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 12 & 8 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0\end{bmatrix}
        $$



---

<span id="gr26o1o2"></span>
??? example "Gr(2,6) / O(1)+O(2)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $6$
    - **Ambient Index:** $3$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $9 \cdot 2^{\frac{2}{3}}$ (mult: 1), $- \frac{9 \cdot 2^{\frac{2}{3}}}{2} - \frac{9 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $- \frac{9 \cdot 2^{\frac{2}{3}}}{2} + \frac{9 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $- 3 \cdot 2^{\frac{2}{3}}$ (mult: 1), $\frac{3 \cdot 2^{\frac{2}{3}}}{2} - \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $\frac{3 \cdot 2^{\frac{2}{3}}}{2} + \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 4)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 4 |
        | \(z^{3} + 108\) | 3 | 1 |
        | \(z^{3} - 2916\) | 3 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0,0,\frac{1}{2},\frac{1}{2}\}\!\}\) |
        | \(\lambda^{3} + 108=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{3} - 2916=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-higher-dimensional.md#58854a726a80). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 6 & 18 & 0 & 0 & 0 & 0 & 72 & 0\\3 & 0 & 0 & 0 & 24 & 30 & 0 & 0 & 0 & 72\\0 & 3 & 0 & 0 & 0 & 0 & 12 & 6 & 0 & 0\\0 & 3 & 0 & 0 & 0 & 0 & 30 & 18 & 0 & 0\\0 & 0 & 3 & 3 & 0 & 0 & 0 & 0 & 6 & 0\\0 & 0 & 0 & 3 & 0 & 0 & 0 & 0 & 12 & 0\\0 & 0 & 0 & 0 & 3 & 6 & 0 & 0 & 0 & 12\\0 & 0 & 0 & 0 & 3 & -3 & 0 & 0 & 0 & -6\\0 & 0 & 0 & 0 & 0 & 0 & 9 & 6 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 3 & 0\end{bmatrix}
        $$



---

## 5-folds

| Geometry | Ambient Index | Basis Rank |
|---|---|---|
| [Gr(2,5) / O(1)](#gr25o1) | 4 | 8 |
| [Gr(3,5) / O(1)](#gr35o1) | 4 | 8 |
| [Gr(2,5) / O(2)](#gr25o2) | 3 | 8 |
| [Gr(3,5) / O(2)](#gr35o2) | 3 | 8 |
| [Gr(2,6) / O(1)+O(1)+O(1)](#gr26o1o1o1) | 3 | 8 |
| [Gr(2,5) / O(3)](#gr25o3) | 2 | 8 |
| [Gr(3,5) / O(3)](#gr35o3) | 2 | 8 |
| [Gr(2,6) / O(1)+O(1)+O(2)](#gr26o1o1o2) | 2 | 8 |

---

<span id="gr25o1"></span>
??? example "Gr(2,5) / O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Ambient Index:** $4$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $- 2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} + 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} - 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} - 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} + 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \cdot 2^{\frac{3}{4}} i \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $2 \cdot 2^{\frac{3}{4}} i \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \cdot 2^{\frac{3}{4}} \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $2 \cdot 2^{\frac{3}{4}} \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{8} - 2816 z^{4} - 65536\) | 8 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-45035996273704960000\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{8} - 2816 \lambda^{4} - 65536=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#1584955327b7). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 0 & 4 & 4 & 0 & 0\\4 & 0 & 0 & 0 & 0 & 0 & 4 & 0\\0 & 4 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 4 & 0 & 0 & 0 & 0 & 0 & 4\\0 & 0 & 4 & 4 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 4 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 8 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 4 & 0\end{bmatrix}
        $$


---

<span id="gr35o1"></span>
??? example "Gr(3,5) / O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Ambient Index:** $4$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $- 2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} + 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} - 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} - 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} + 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \cdot 2^{\frac{3}{4}} i \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $2 \cdot 2^{\frac{3}{4}} i \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \cdot 2^{\frac{3}{4}} \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $2 \cdot 2^{\frac{3}{4}} \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{8} - 2816 z^{4} - 65536\) | 8 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-45035996273704960000\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{8} - 2816 \lambda^{4} - 65536=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#1e7394ef8632). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 0 & 4 & 4 & 0 & 0\\4 & 0 & 0 & 0 & 0 & 0 & 4 & 0\\0 & 4 & 0 & 0 & 0 & 0 & 0 & 4\\0 & 4 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 4 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 4 & 4 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 4 & 8 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 4 & 0\end{bmatrix}
        $$


---

<span id="gr25o2"></span>
??? example "Gr(2,5) / O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Ambient Index:** $3$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $- 3 \sqrt[3]{-22 + 10 \sqrt{5}}$ (mult: 1), $\frac{3 \sqrt[3]{-22 + 10 \sqrt{5}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{-22 + 10 \sqrt{5}}}{2}$ (mult: 1), $\frac{3 \sqrt[3]{-22 + 10 \sqrt{5}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{-22 + 10 \sqrt{5}}}{2}$ (mult: 1), $3 \sqrt[3]{22 + 10 \sqrt{5}}$ (mult: 1), $- \frac{3 \sqrt[3]{22 + 10 \sqrt{5}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{22 + 10 \sqrt{5}}}{2}$ (mult: 1), $- \frac{3 \sqrt[3]{22 + 10 \sqrt{5}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{22 + 10 \sqrt{5}}}{2}$ (mult: 1), $0$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 2 |
        | \(z^{6} - 1188 z^{3} - 11664\) | 6 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0,0\}\!\}\) |
        | \(\lambda^{6} - 1188 \lambda^{3} - 11664=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#1cd0a9ffb74e). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 6 & 12 & 0 & 0 & 0 & 24\\3 & 0 & 0 & 0 & 18 & 12 & 0 & 0\\0 & 3 & 0 & 0 & 0 & 0 & 6 & 0\\0 & 3 & 0 & 0 & 0 & 0 & 12 & 0\\0 & 0 & 3 & 3 & 0 & 0 & 0 & 6\\0 & 0 & 0 & 3 & 0 & 0 & 0 & 6\\0 & 0 & 0 & 0 & 6 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 3 & 0\end{bmatrix}
        $$


---

<span id="gr35o2"></span>
??? example "Gr(3,5) / O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Ambient Index:** $3$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $- 3 \sqrt[3]{-22 + 10 \sqrt{5}}$ (mult: 1), $\frac{3 \sqrt[3]{-22 + 10 \sqrt{5}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{-22 + 10 \sqrt{5}}}{2}$ (mult: 1), $\frac{3 \sqrt[3]{-22 + 10 \sqrt{5}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{-22 + 10 \sqrt{5}}}{2}$ (mult: 1), $3 \sqrt[3]{22 + 10 \sqrt{5}}$ (mult: 1), $- \frac{3 \sqrt[3]{22 + 10 \sqrt{5}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{22 + 10 \sqrt{5}}}{2}$ (mult: 1), $- \frac{3 \sqrt[3]{22 + 10 \sqrt{5}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{22 + 10 \sqrt{5}}}{2}$ (mult: 1), $0$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 2 |
        | \(z^{6} - 1188 z^{3} - 11664\) | 6 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0,0\}\!\}\) |
        | \(\lambda^{6} - 1188 \lambda^{3} - 11664=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#d7857b18eb8e). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 12 & 6 & 0 & 0 & 0 & 24\\3 & 0 & 0 & 0 & 12 & 18 & 0 & 0\\0 & 3 & 0 & 0 & 0 & 0 & 12 & 0\\0 & 3 & 0 & 0 & 0 & 0 & 6 & 0\\0 & 0 & 3 & 0 & 0 & 0 & 0 & 6\\0 & 0 & 3 & 3 & 0 & 0 & 0 & 6\\0 & 0 & 0 & 0 & 3 & 6 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 3 & 0\end{bmatrix}
        $$


---

<span id="gr26o1o1o1"></span>
??? example "Gr(2,6) / O(1)+O(1)+O(1)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $5$
    - **Ambient Index:** $3$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $9$ (mult: 1), $-3$ (mult: 1), $\frac{3}{2} - \frac{3 \sqrt{3} i}{2}$ (mult: 1), $\frac{3}{2} + \frac{3 \sqrt{3} i}{2}$ (mult: 1), $- \frac{9}{2} - \frac{9 \sqrt{3} i}{2}$ (mult: 1), $- \frac{9}{2} + \frac{9 \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 3\) | 1 | 1 |
        | \(z - 9\) | 1 | 1 |
        | \(z\) | 1 | 2 |
        | \(z^{2} + 9 z + 81\) | 2 | 1 |
        | \(z^{2} - 3 z + 9\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 3=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 9=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |
        | \(\lambda^{2} + 9 \lambda + 81=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{2} - 3 \lambda + 9=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#51706ac77ff7). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 3 & 9 & 0 & 0 & 0 & 6\\3 & 0 & 0 & 0 & 9 & 9 & 0 & 0\\0 & 3 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 3 & 0 & 0 & 0 & 0 & 9 & 0\\0 & 0 & 3 & 3 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 3 & 0 & 0 & 0 & 3\\0 & 0 & 0 & 0 & 5 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 9 & 0\end{bmatrix}
        $$



---

<span id="gr25o3"></span>
??? example "Gr(2,5) / O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Ambient Index:** $2$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $- 6 i \sqrt{- \frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $6 i \sqrt{- \frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $- 6 \sqrt{\frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $6 \sqrt{\frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $0$ (mult: 4)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 4 |
        | \(z^{4} - 1188 z^{2} - 11664\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{\frac{1}{6},\frac{1}{6},\frac{5}{6},\frac{5}{6}\}\!\}\) |
        | \(\lambda^{4} - 1188 \lambda^{2} - 11664=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#dd16e36a8997). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 36 & 0 & 0 & 2232 & 1224 & 0 & 26568\\2 & 0 & 54 & 96 & 0 & 0 & 2988 & 0\\0 & 2 & 0 & 0 & 72 & 42 & 0 & 1008\\0 & 2 & 0 & 0 & 96 & 54 & 0 & 1224\\0 & 0 & 2 & 2 & 0 & 0 & 54 & 0\\0 & 0 & 0 & 2 & 0 & 0 & 42 & 0\\0 & 0 & 0 & 0 & 4 & 2 & 0 & 36\\0 & 0 & 0 & 0 & 0 & 0 & 2 & 0\end{bmatrix}
        $$


---

<span id="gr35o3"></span>
??? example "Gr(3,5) / O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Ambient Index:** $2$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $- 6 i \sqrt{- \frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $6 i \sqrt{- \frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $- 6 \sqrt{\frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $6 \sqrt{\frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $0$ (mult: 4)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 4 |
        | \(z^{4} - 1188 z^{2} - 11664\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{\frac{1}{6},\frac{1}{6},\frac{5}{6},\frac{5}{6}\}\!\}\) |
        | \(\lambda^{4} - 1188 \lambda^{2} - 11664=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#ffb644472d2c). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 36 & 0 & 0 & 1224 & 2232 & 0 & 26568\\2 & 0 & 96 & 54 & 0 & 0 & 2988 & 0\\0 & 2 & 0 & 0 & 54 & 96 & 0 & 1224\\0 & 2 & 0 & 0 & 42 & 72 & 0 & 1008\\0 & 0 & 2 & 0 & 0 & 0 & 42 & 0\\0 & 0 & 2 & 2 & 0 & 0 & 54 & 0\\0 & 0 & 0 & 0 & 2 & 4 & 0 & 36\\0 & 0 & 0 & 0 & 0 & 0 & 2 & 0\end{bmatrix}
        $$



    

    ***
    *Note: This catalog is automatically generated.*

---

<span id="gr26o1o1o2"></span>
??? example "Gr(2,6) / O(1)+O(1)+O(2)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $5$
    - **Ambient Index:** $2$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $- 12 \sqrt{3}$ (mult: 1), $12 \sqrt{3}$ (mult: 1), $- 4 i$ (mult: 1), $4 i$ (mult: 1), $0$ (mult: 4)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 4 |
        | \(z^{2} - 432\) | 2 | 1 |
        | \(z^{2} + 16\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{\frac{1}{6},\frac{1}{2},\frac{1}{2},\frac{5}{6}\}\!\}\) |
        | \(\lambda^{2} - 432=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{2} + 16=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fivefolds.md#c7da579d09a1). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 16 & 0 & 0 & 336 & 288 & 0 & 768\\2 & 0 & 16 & 36 & 0 & 0 & 480 & 0\\0 & 2 & 0 & 0 & 12 & 12 & 0 & 48\\0 & 2 & 0 & 0 & 32 & 28 & 0 & 80\\0 & 0 & 2 & 2 & 0 & 0 & 12 & 0\\0 & 0 & 0 & 2 & 0 & 0 & 24 & 0\\0 & 0 & 0 & 0 & \frac{10}{3} & \frac{8}{3} & 0 & \frac{16}{3}\\0 & 0 & 0 & 0 & 0 & 0 & 6 & 0\end{bmatrix}
        $$



---

## 4-folds

| Geometry | Ambient Index | Basis Rank |
|---|---|---|
| [Gr(4,5)](#gr45) | 5 | 5 |
| [Gr(2,4)](#gr24) | 4 | 6 |
| [Gr(2,5) / O(1)+O(1)](#gr25o1o1) | 3 | 6 |
| [Gr(3,5) / O(1)+O(1)](#gr35o1o1) | 3 | 6 |
| [Gr(2,5) / O(1)+O(2)](#gr25o1o2) | 2 | 6 |
| [Gr(3,5) / O(1)+O(2)](#gr35o1o2) | 2 | 6 |
| [Gr(2,5) / O(1)+O(3)](#gr25o1o3) | 1 | 6 |
| [Gr(2,5) / O(2)+O(2)](#gr25o2o2) | 1 | 6 |
| [Gr(3,5) / O(1)+O(3)](#gr35o1o3) | 1 | 6 |
| [Gr(3,5) / O(2)+O(2)](#gr35o2o2) | 1 | 6 |

---

<span id="gr45"></span>
??? example "Gr(4,5)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Ambient Index:** $5$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $5$ (mult: 1), $- \frac{5 \sqrt{5}}{4} - \frac{5}{4} - 5 i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \sqrt{5}}{4} - \frac{5}{4} + 5 i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5}{4} + \frac{5 \sqrt{5}}{4} - 5 i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5}{4} + \frac{5 \sqrt{5}}{4} + 5 i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y4=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z - 5\) | 1 | 1 |
        | \(z^{4} + 5 z^{3} + 25 z^{2} + 125 z + 625\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=9765625\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda - 5=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{4} + 5 \lambda^{3} + 25 \lambda^{2} + 125 \lambda + 625=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#139781d9fb14). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 0 & 5\\5 & 0 & 0 & 0 & 0\\0 & 5 & 0 & 0 & 0\\0 & 0 & 5 & 0 & 0\\0 & 0 & 0 & 5 & 0\end{bmatrix}
        $$



---

<span id="gr24"></span>
??? example "Gr(2,4)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $4$
    - **Ambient Index:** $4$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $- 4 \sqrt{2}$ (mult: 1), $4 \sqrt{2}$ (mult: 1), $- 4 \sqrt{2} i$ (mult: 1), $4 \sqrt{2} i$ (mult: 1), $0$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 2 |
        | \(z^{2} - 32\) | 2 | 1 |
        | \(z^{2} + 32\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0,0\}\!\}\) |
        | \(\lambda^{2} - 32=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{2} + 32=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#51615a7643a1). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 0 & 4 & 0\\4 & 0 & 0 & 0 & 0 & 4\\0 & 4 & 0 & 0 & 0 & 0\\0 & 4 & 0 & 0 & 0 & 0\\0 & 0 & 4 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 4 & 0\end{bmatrix}
        $$


---

<span id="gr25o1o1"></span>
??? example "Gr(2,5) / O(1)+O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Ambient Index:** $3$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $- 3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $\frac{3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $\frac{3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- \frac{3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $- \frac{3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{6} - 297 z^{3} - 729\) | 6 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=\frac{1793613375}{2}\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{6} - 297 \lambda^{3} - 729=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#3c0ee725b9d8). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 3 & 6 & 0 & 0\\3 & 0 & 0 & 0 & 6 & 0\\0 & 3 & 0 & 0 & 0 & 0\\0 & 3 & 0 & 0 & 0 & 3\\0 & 0 & 3 & \frac{9}{2} & 0 & 0\\0 & 0 & 0 & 0 & 6 & 0\end{bmatrix}
        $$


---

<span id="gr35o1o1"></span>
??? example "Gr(3,5) / O(1)+O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Ambient Index:** $3$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $- 3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $\frac{3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $\frac{3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- \frac{3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $- \frac{3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{6} - 297 z^{3} - 729\) | 6 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-1793613375\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{6} - 297 \lambda^{3} - 729=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#fbeb5f79765b). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 6 & 3 & 0 & 0\\3 & 0 & 0 & 0 & 3 & 0\\0 & 3 & 0 & 0 & 0 & 3\\0 & 3 & 0 & 0 & 0 & 0\\0 & 0 & 9 & 6 & 0 & 0\\0 & 0 & 0 & 0 & 3 & 0\end{bmatrix}
        $$


---

<span id="gr25o1o2"></span>
??? example "Gr(2,5) / O(1)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Ambient Index:** $2$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $- 4 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $4 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- 4 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $4 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $0$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 2 |
        | \(z^{4} - 176 z^{2} - 256\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0,0\}\!\}\) |
        | \(\lambda^{4} - 176 \lambda^{2} - 256=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#5a3a05721152). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 12 & 0 & 0 & 96 & 0\\2 & 0 & 12 & 20 & 0 & 48\\0 & 2 & 0 & 0 & 8 & 0\\0 & 2 & 0 & 0 & 16 & 0\\0 & 0 & 2 & 3 & 0 & 6\\0 & 0 & 0 & 0 & 4 & 0\end{bmatrix}
        $$


---

<span id="gr35o1o2"></span>
??? example "Gr(3,5) / O(1)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Ambient Index:** $2$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $- 4 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $4 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- 4 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $4 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $0$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 2 |
        | \(z^{4} - 176 z^{2} - 256\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0,0\}\!\}\) |
        | \(\lambda^{4} - 176 \lambda^{2} - 256=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#0c8674c9ad6f). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 12 & 0 & 0 & 48 & 0\\2 & 0 & 20 & 12 & 0 & 48\\0 & 2 & 0 & 0 & 8 & 0\\0 & 2 & 0 & 0 & 4 & 0\\0 & 0 & 6 & 4 & 0 & 12\\0 & 0 & 0 & 0 & 2 & 0\end{bmatrix}
        $$


---

<span id="gr25o1o3"></span>
??? example "Gr(2,5) / O(1)+O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Ambient Index:** $1$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-18$ (mult: 4), $\frac{261}{2} - \frac{135 \sqrt{5}}{2}$ (mult: 1), $\frac{261}{2} + \frac{135 \sqrt{5}}{2}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 18\) | 1 | 4 |
        | \(z^{2} - 261 z - 5751\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 18=0\) | \(\{\!\{\frac{1}{3},\frac{1}{3},\frac{2}{3},\frac{2}{3}\}\!\}\) |
        | \(\lambda^{2} - 261 \lambda - 5751=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#d2a92bddd407). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 2772 & 200988 & 310284 & 23784192 & 430673760\\1 & 57 & 5328 & 8244 & 644490 & 11892096\\0 & 1 & 18 & 57 & 4824 & 91692\\0 & 1 & 48 & 57 & 5832 & 109296\\0 & 0 & 1 & \frac{3}{2} & 57 & 1386\\0 & 0 & 0 & 0 & 2 & 0\end{bmatrix}
        $$


---

<span id="gr25o2o2"></span>
??? example "Gr(2,5) / O(2)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Ambient Index:** $1$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-12$ (mult: 4), $76 - 40 \sqrt{5}$ (mult: 1), $76 + 40 \sqrt{5}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 12\) | 1 | 4 |
        | \(z^{2} - 152 z - 2224\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 12=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2}\}\!\}\) |
        | \(\lambda^{2} - 152 \lambda - 2224=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#71c4061dbdf2). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 1080 & 46080 & 71424 & 3301632 & 39398400\\1 & 32 & 1848 & 2872 & 135552 & 1650816\\0 & 1 & 8 & 32 & 1648 & 20736\\0 & 1 & 28 & 32 & 2048 & 25344\\0 & 0 & 1 & \frac{3}{2} & 32 & 540\\0 & 0 & 0 & 0 & 2 & 0\end{bmatrix}
        $$


---

<span id="gr35o1o3"></span>
??? example "Gr(3,5) / O(1)+O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Ambient Index:** $1$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-18$ (mult: 4), $\frac{261}{2} - \frac{135 \sqrt{5}}{2}$ (mult: 1), $\frac{261}{2} + \frac{135 \sqrt{5}}{2}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 18\) | 1 | 4 |
        | \(z^{2} - 261 z - 5751\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 18=0\) | \(\{\!\{\frac{1}{3},\frac{1}{3},\frac{2}{3},\frac{2}{3}\}\!\}\) |
        | \(\lambda^{2} - 261 \lambda - 5751=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#f418dda622c4). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 2772 & 310284 & 200988 & 11892096 & 430673760\\1 & 57 & 8244 & 5328 & 322245 & 11892096\\0 & 1 & 57 & 48 & 2916 & 109296\\0 & 1 & 57 & 18 & 2412 & 91692\\0 & 0 & 3 & 2 & 57 & 2772\\0 & 0 & 0 & 0 & 1 & 0\end{bmatrix}
        $$


---

<span id="gr35o2o2"></span>
??? example "Gr(3,5) / O(2)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Ambient Index:** $1$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-12$ (mult: 4), $76 - 40 \sqrt{5}$ (mult: 1), $76 + 40 \sqrt{5}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 12\) | 1 | 4 |
        | \(z^{2} - 152 z - 2224\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=0\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 12=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2},\frac{1}{2},\frac{1}{2}\}\!\}\) |
        | \(\lambda^{2} - 152 \lambda - 2224=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-fourfolds.md#a6bf73eeb7fb). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 1080 & 71424 & 46080 & 1650816 & 39398400\\1 & 32 & 2872 & 1848 & 67776 & 1650816\\0 & 1 & 32 & 28 & 1024 & 25344\\0 & 1 & 32 & 8 & 824 & 20736\\0 & 0 & 3 & 2 & 32 & 1080\\0 & 0 & 0 & 0 & 1 & 0\end{bmatrix}
        $$



---

## 3-folds

| Geometry | Ambient Index | Basis Rank |
|---|---|---|
| [Gr(3,4)](#gr34) | 4 | 4 |
| [Gr(4,5) / O(1)](#gr45o1) | 4 | 4 |
| [Gr(2,4) / O(1)](#gr24o1) | 3 | 4 |
| [Gr(4,5) / O(2)](#gr45o2) | 3 | 4 |
| [Gr(2,4) / O(2)](#gr24o2) | 2 | 4 |
| [Gr(2,5) / O(1)+O(1)+O(1)](#gr25o1o1o1) | 2 | 4 |
| [Gr(3,5) / O(1)+O(1)+O(1)](#gr35o1o1o1) | 2 | 4 |
| [Gr(4,5) / O(3)](#gr45o3) | 2 | 4 |
| [Gr(2,4) / O(3)](#gr24o3) | 1 | 4 |
| [Gr(2,5) / O(1)+O(1)+O(2)](#gr25o1o1o2) | 1 | 4 |
| [Gr(3,5) / O(1)+O(1)+O(2)](#gr35o1o1o2) | 1 | 4 |
| [Gr(4,5) / O(4)](#gr45o4) | 1 | 4 |

---

<span id="gr34"></span>
??? example "Gr(3,4)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $3$
    - **Ambient Index:** $4$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $- 4 i$ (mult: 1), $4 i$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

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

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#92f8f69bd1f8). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 4\\4 & 0 & 0 & 0\\0 & 4 & 0 & 0\\0 & 0 & 4 & 0\end{bmatrix}
        $$


---

<span id="gr45o1"></span>
??? example "Gr(4,5) / O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Ambient Index:** $4$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $- 4 i$ (mult: 1), $4 i$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y4=1`.

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

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#005416420233). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 0 & 4\\4 & 0 & 0 & 0\\0 & 4 & 0 & 0\\0 & 0 & 4 & 0\end{bmatrix}
        $$



---

<span id="gr24o1"></span>
??? example "Gr(2,4) / O(1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $3$
    - **Ambient Index:** $3$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $3 \cdot 2^{\frac{2}{3}}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} - \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} + \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 1 |
        | \(z^{3} - 108\) | 3 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=2916\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{3} - 108=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#1841f3a70f74). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 3 & 0\\3 & 0 & 0 & 3\\0 & 6 & 0 & 0\\0 & 0 & 3 & 0\end{bmatrix}
        $$


---

<span id="gr45o2"></span>
??? example "Gr(4,5) / O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Ambient Index:** $3$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $3 \cdot 2^{\frac{2}{3}}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} - \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} + \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y4=1`.

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

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#6ce465296672). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 6 & 0\\3 & 0 & 0 & 6\\0 & 3 & 0 & 0\\0 & 0 & 3 & 0\end{bmatrix}
        $$



---

<span id="gr24o2"></span>
??? example "Gr(2,4) / O(2)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $3$
    - **Ambient Index:** $2$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $-8$ (mult: 1), $8$ (mult: 1), $0$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 8\) | 1 | 1 |
        | \(z - 8\) | 1 | 1 |
        | \(z\) | 1 | 2 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=256\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 8=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 8=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#0156965bbcb0). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 8 & 0 & 16\\2 & 0 & 8 & 0\\0 & 4 & 0 & 8\\0 & 0 & 2 & 0\end{bmatrix}
        $$


---

<span id="gr25o1o1o1"></span>
??? example "Gr(2,5) / O(1)+O(1)+O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Ambient Index:** $2$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $- 2 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $2 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- 2 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $2 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1)

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


---

<span id="gr35o1o1o1"></span>
??? example "Gr(3,5) / O(1)+O(1)+O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Ambient Index:** $2$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $- 2 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $2 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- 2 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $2 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z^{4} - 44 z^{2} - 16\) | 4 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=\frac{1600}{3}\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda^{4} - 44 \lambda^{2} - 16=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#70aac1aaa08e). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 6 & 0 & 4\\2 & 0 & 6 & 0\\0 & \frac{10}{3} & 0 & 2\\0 & 0 & 6 & 0\end{bmatrix}
        $$


---

<span id="gr45o3"></span>
??? example "Gr(4,5) / O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Ambient Index:** $2$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $- 6 \sqrt{3}$ (mult: 1), $6 \sqrt{3}$ (mult: 1), $0$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y4=1`.

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

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#a408b7769859). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 12 & 0 & 72\\2 & 0 & 30 & 0\\0 & 2 & 0 & 12\\0 & 0 & 2 & 0\end{bmatrix}
        $$



---

<span id="gr24o3"></span>
??? example "Gr(2,4) / O(3)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $3$
    - **Ambient Index:** $1$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $96$ (mult: 1), $-12$ (mult: 3)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z - 96\) | 1 | 1 |
        | \(z + 12\) | 1 | 3 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=4\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda - 96=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda + 12=0\) | \(\{\!\{0,\frac{1}{6},\frac{5}{6}\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#83c013d9bdf4). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 792 & 21816 & 396576\\1 & 30 & 1170 & 21816\\0 & 2 & 30 & 792\\0 & 0 & 1 & 0\end{bmatrix}
        $$


---

<span id="gr25o1o1o2"></span>
??? example "Gr(2,5) / O(1)+O(1)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Ambient Index:** $1$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $-6$ (mult: 2), $16 - 10 \sqrt{5}$ (mult: 1), $16 + 10 \sqrt{5}$ (mult: 1)

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
        \begin{bmatrix}0 & 156 & 1440 & 13248\\1 & 10 & 152 & 1440\\0 & \frac{5}{2} & 10 & 156\\0 & 0 & 1 & 0\end{bmatrix}
        $$


---

<span id="gr35o1o1o2"></span>
??? example "Gr(3,5) / O(1)+O(1)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Ambient Index:** $1$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $-6$ (mult: 2), $16 - 10 \sqrt{5}$ (mult: 1), $16 + 10 \sqrt{5}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 6\) | 1 | 2 |
        | \(z^{2} - 32 z - 244\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=\frac{25}{3}\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 6=0\) | \(\{\!\{0,0\}\!\}\) |
        | \(\lambda^{2} - 32 \lambda - 244=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#d1339713ede4). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 156 & 2160 & 6624\\1 & 10 & 228 & 720\\0 & \frac{5}{3} & 10 & 52\\0 & 0 & 3 & 0\end{bmatrix}
        $$


---

<span id="gr45o4"></span>
??? example "Gr(4,5) / O(4)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Ambient Index:** $1$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $232$ (mult: 1), $-24$ (mult: 3)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y4=1`.

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

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-threefolds.md#490a4dc43960). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 3888 & 504576 & 18323712\\1 & 80 & 13600 & 504576\\0 & 1 & 80 & 3888\\0 & 0 & 1 & 0\end{bmatrix}
        $$



---

## Surfaces (2-folds)

| Geometry | Ambient Index | Basis Rank |
|---|---|---|
| [Gr(3,4) / O(1)](#gr34o1) | 3 | 3 |
| [Gr(4,5) / O(1)+O(1)](#gr45o1o1) | 3 | 3 |
| [Gr(2,4) / O(1)+O(1)](#gr24o1o1) | 2 | 3 |
| [Gr(3,4) / O(2)](#gr34o2) | 2 | 3 |
| [Gr(4,5) / O(1)+O(2)](#gr45o1o2) | 2 | 3 |
| [Gr(2,4) / O(1)+O(2)](#gr24o1o2) | 1 | 3 |
| [Gr(3,4) / O(3)](#gr34o3) | 1 | 3 |
| [Gr(4,5) / O(1)+O(3)](#gr45o1o3) | 1 | 3 |
| [Gr(4,5) / O(2)+O(2)](#gr45o2o2) | 1 | 3 |

---

<span id="gr34o1"></span>
??? example "Gr(3,4) / O(1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Ambient Index:** $3$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $3$ (mult: 1), $- \frac{3}{2} - \frac{3 \sqrt{3} i}{2}$ (mult: 1), $- \frac{3}{2} + \frac{3 \sqrt{3} i}{2}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z - 3\) | 1 | 1 |
        | \(z^{2} + 3 z + 9\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=27\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda - 3=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{2} + 3 \lambda + 9=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-surfaces.md#892655959f06). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 3\\3 & 0 & 0\\0 & 3 & 0\end{bmatrix}
        $$


---

<span id="gr45o1o1"></span>
??? example "Gr(4,5) / O(1)+O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $2$
    - **Ambient Index:** $3$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $3$ (mult: 1), $- \frac{3}{2} - \frac{3 \sqrt{3} i}{2}$ (mult: 1), $- \frac{3}{2} + \frac{3 \sqrt{3} i}{2}$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y4=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z - 3\) | 1 | 1 |
        | \(z^{2} + 3 z + 9\) | 2 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=27\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda - 3=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda^{2} + 3 \lambda + 9=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-surfaces.md#5bdf83aa585a). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 0 & 3\\3 & 0 & 0\\0 & 3 & 0\end{bmatrix}
        $$



---

<span id="gr24o1o1"></span>
??? example "Gr(2,4) / O(1)+O(1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Ambient Index:** $2$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $0$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 4\) | 1 | 1 |
        | \(z\) | 1 | 1 |
        | \(z - 4\) | 1 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=16\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 4=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 4=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-surfaces.md#1d67c54eac18). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 4 & 0\\2 & 0 & 2\\0 & 4 & 0\end{bmatrix}
        $$


---

<span id="gr34o2"></span>
??? example "Gr(3,4) / O(2)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Ambient Index:** $2$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $0$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 4\) | 1 | 1 |
        | \(z\) | 1 | 1 |
        | \(z - 4\) | 1 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=8\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 4=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 4=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-surfaces.md#53ee7c8af21e). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 4 & 0\\2 & 0 & 4\\0 & 2 & 0\end{bmatrix}
        $$


---

<span id="gr45o1o2"></span>
??? example "Gr(4,5) / O(1)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $2$
    - **Ambient Index:** $2$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $0$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y4=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 4\) | 1 | 1 |
        | \(z\) | 1 | 1 |
        | \(z - 4\) | 1 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=8\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 4=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 4=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-surfaces.md#04f8ea67b0d4). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 4 & 0\\2 & 0 & 4\\0 & 2 & 0\end{bmatrix}
        $$



---

<span id="gr24o1o2"></span>
??? example "Gr(2,4) / O(1)+O(2)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Ambient Index:** $1$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $12$ (mult: 1), $-4$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z - 12\) | 1 | 1 |
        | \(z + 4\) | 1 | 2 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=2\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda - 12=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda + 4=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-surfaces.md#c5377008d724). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 40 & 96\\1 & 4 & 20\\0 & 2 & 0\end{bmatrix}
        $$


---

<span id="gr34o3"></span>
??? example "Gr(3,4) / O(3)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Ambient Index:** $1$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $21$ (mult: 1), $-6$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z - 21\) | 1 | 1 |
        | \(z + 6\) | 1 | 2 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda - 21=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda + 6=0\) | \(\{\!\{\frac{1}{3},\frac{2}{3}\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-surfaces.md#1fe2cc704593). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 108 & 756\\1 & 9 & 108\\0 & 1 & 0\end{bmatrix}
        $$


---

<span id="gr45o1o3"></span>
??? example "Gr(4,5) / O(1)+O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $2$
    - **Ambient Index:** $1$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $21$ (mult: 1), $-6$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y4=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z - 21\) | 1 | 1 |
        | \(z + 6\) | 1 | 2 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda - 21=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda + 6=0\) | \(\{\!\{\frac{1}{3},\frac{2}{3}\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-surfaces.md#b1aa6f89ec3e). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 108 & 756\\1 & 9 & 108\\0 & 1 & 0\end{bmatrix}
        $$



---

<span id="gr45o2o2"></span>
??? example "Gr(4,5) / O(2)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $2$
    - **Ambient Index:** $1$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $12$ (mult: 1), $-4$ (mult: 2)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y4=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z - 12\) | 1 | 1 |
        | \(z + 4\) | 1 | 2 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda - 12=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda + 4=0\) | \(\{\!\{\frac{1}{2},\frac{1}{2}\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-surfaces.md#2dd604001dc5). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 40 & 192\\1 & 4 & 40\\0 & 1 & 0\end{bmatrix}
        $$



---

## Curves (1-folds)

| Geometry | Ambient Index | Basis Rank |
|---|---|---|
| [Gr(3,4) / O(1)+O(1)](#gr34o1o1) | 2 | 2 |
| [Gr(4,5) / O(1)+O(1)+O(1)](#gr45o1o1o1) | 2 | 2 |
| [Gr(2,4) / O(1)+O(1)+O(1)](#gr24o1o1o1) | 1 | 2 |
| [Gr(3,4) / O(1)+O(2)](#gr34o1o2) | 1 | 2 |
| [Gr(4,5) / O(1)+O(1)+O(2)](#gr45o1o1o2) | 1 | 2 |

---

<span id="gr34o1o1"></span>
??? example "Gr(3,4) / O(1)+O(1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $1$
    - **Ambient Index:** $2$
    - **Basis Rank:** $2$
    - **Eigenvalues:** $-2$ (mult: 1), $2$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 2\) | 1 | 1 |
        | \(z - 2\) | 1 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=2\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 2=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 2=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-points-curves.md#375785af1f22). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 2\\2 & 0\end{bmatrix}
        $$


---

<span id="gr45o1o1o1"></span>
??? example "Gr(4,5) / O(1)+O(1)+O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $1$
    - **Ambient Index:** $2$
    - **Basis Rank:** $2$
    - **Eigenvalues:** $-2$ (mult: 1), $2$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y4=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 2\) | 1 | 1 |
        | \(z - 2\) | 1 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=2\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 2=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 2=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-points-curves.md#8156468b738f). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 2\\2 & 0\end{bmatrix}
        $$



---

<span id="gr24o1o1o1"></span>
??? example "Gr(2,4) / O(1)+O(1)+O(1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $1$
    - **Ambient Index:** $1$
    - **Basis Rank:** $2$
    - **Eigenvalues:** $-2$ (mult: 1), $2$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y2=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 2\) | 1 | 1 |
        | \(z - 2\) | 1 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 2=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 2=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-points-curves.md#8b39618f3aed). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 4\\1 & 0\end{bmatrix}
        $$


---

<span id="gr34o1o2"></span>
??? example "Gr(3,4) / O(1)+O(2)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $1$
    - **Ambient Index:** $1$
    - **Basis Rank:** $2$
    - **Eigenvalues:** $-2$ (mult: 1), $2$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y3=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 2\) | 1 | 1 |
        | \(z - 2\) | 1 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 2=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 2=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-points-curves.md#79dd3601d09b). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 4\\1 & 0\end{bmatrix}
        $$


---

<span id="gr45o1o1o2"></span>
??? example "Gr(4,5) / O(1)+O(1)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $1$
    - **Ambient Index:** $1$
    - **Basis Rank:** $2$
    - **Eigenvalues:** $-2$ (mult: 1), $2$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** `y4=1`.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z + 2\) | 1 | 1 |
        | \(z - 2\) | 1 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda + 2=0\) | \(\{\!\{0\}\!\}\) |
        | \(\lambda - 2=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-points-curves.md#af3a5033ba7a). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0 & 4\\1 & 0\end{bmatrix}
        $$



---

## 0-folds

| Geometry | Ambient Index | Basis Rank |
|---|---|---|
| [Gr(3,4) / O(1)+O(1)+O(1)](#gr34o1o1o1) | 1 | 1 |

---

<span id="gr34o1o1o1"></span>
??? example "Gr(3,4) / O(1)+O(1)+O(1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $0$
    - **Ambient Index:** $1$
    - **Basis Rank:** $1$
    - **Eigenvalues:** $0$ (mult: 1)

    ??? note "Spectrum and connection exponents"

        **Parameter point:** ``.

        Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](notation.md).

        \(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

        | Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
        |---|---:|---:|
        | \(z\) | 1 | 1 |

        **Unit cyclic determinant:** \(\Delta_A(\mathbf a)=1\), in this basis.

        **Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

        | Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
        |---|---|
        | \(\lambda=0\) | \(\{\!\{0\}\!\}\) |

        Repeated entries retain their multiplicity.

        [Exact matrix, ordered basis and grading](../data/localization-results.json) · [Hodge data and atomic invariants](invariants-points-curves.md#c427c3fda1be). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

    ??? note "Quantum Matrix ($y=1$)"
        $$
        \begin{bmatrix}0\end{bmatrix}
        $$


---

