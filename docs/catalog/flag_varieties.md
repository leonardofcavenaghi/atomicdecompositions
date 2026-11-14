---
description: Small quantum multiplication for flag varieties, with exact matrices and reproducible localization inputs.
---

# Full flag example

The full flag variety `Fl(1,2;3)` illustrates the untwisted calculation.
See [Flag varieties and sections](additional.md) for the other computed flag examples.

For the kept-root beta convention and copyable browser/CLI syntax, see [How to Use](../how-to-use.md).

The displayed matrices are \(A(\mathbf 1)\), first-Chern quantum multiplication on the returned ambient space, with columns as images of the ordered basis. The returned grading is \(G=\operatorname{diag}(\operatorname{codim} e_i-\dim X/2)\). Spectral tables state their own parameter point. See [notation and scope](notation.md).

## Reproduce an entry in the software

The full flag card is `A2` with kept roots `1,2` and an empty Bundle K field.
Use the **Space Info** action first; it prints the reduced Schubert words that
can be copied into a GW-invariant request.

## 3-folds

| Geometry | Ambient Index | Basis Rank |
|---|---|---|
| [(a)  Fl(1,2,3)](#afl123) | 2 | 6 |

---

<span id="afl123"></span>
### (a)  Fl(1,2,3)
- **Ambient Space:** `$A2$`
- **Dimension:** $3$
- **Ambient Index:** $2$
- **Basis Rank:** $6$
- **Eigenvalues:** $- 4 \sqrt{2}$ (mult: 1), $4 \sqrt{2}$ (mult: 1), $- 2 i$ (mult: 2), $2 i$ (mult: 2)

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

??? note "Quantum Matrix ($y=1$)"
    $$
        \begin{bmatrix}0 & 2 & 2 & 0 & 0 & 4\\2 & 0 & 0 & 2 & 0 & 0\\2 & 0 & 0 & 0 & 2 & 0\\0 & 2 & 4 & 0 & 0 & 2\\0 & 4 & 2 & 0 & 0 & 2\\0 & 0 & 0 & 2 & 2 & 0\end{bmatrix}
    $$


---

