# Quantum Geometry Catalog

Welcome to the automated catalog. Below you will find geometric and quantum properties computed for various complete intersections.

## Glossary

- **Ambient Space**: The ambient flag variety $G/P$ in which the complete intersection $X$ is embedded.
- **Dimension**: The complex dimension of the resulting geometric space $X$. Computed by subtracting the rank of the intersecting bundle from the dimension of the ambient space.
- **Fano Index**: The greatest integer $I_X$ dividing the anticanonical class $-K_X$. It dictates the powers of the Novikov parameters in quantum multiplication.
- **Basis Rank**: The number of dimensions in the projected flag-ambient cohomology ring $H_{amb}^*(X)$. This equals the size of the square quantum multiplication matrix.
- **Eigenvalues**: The eigenvalues of the small quantum multiplication matrix $c_1(TX)\star$ evaluated at $y=1$, along with their algebraic multiplicities. These values govern the spectrum of the quantum connection.
- **Hodge Diamond**: The geometric $h^{p,q}$ Hodge numbers of the space.

***

<div class="grid cards" markdown>

??? example "Case #5: Gr(2,4)  flag itself"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $4$
    - **Fano Index:** $4$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $- 4 \sqrt{2}$ (mult: 1), $4 \sqrt{2}$ (mult: 1), $- 4 \sqrt{2} i$ (mult: 1), $4 \sqrt{2} i$ (mult: 1), $0$ (mult: 2)


??? example "Case #6: Gr(2,4) / O(2)  del Pezzo"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $3$
    - **Fano Index:** $2$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-8$ (mult: 1), $8$ (mult: 1), $0$ (mult: 2)


??? example "Case #2: P4 / O(2)  quadric 3-fold"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $3$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $3 \cdot 2^{\frac{2}{3}}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} - \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} + \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 1)
    - **Hodge Diamond ($h^{p,q}$):**
        $$
                \begin{matrix}
         &  &  & 1 &  &  &  \\
         &  & 0 &  & 0 &  &  \\
         & 0 &  & 1 &  & 0 &  \\
        0 &  & 0 &  & 0 &  & 0 \\
         & 0 &  & 1 &  & 0 &  \\
         &  & 0 &  & 0 &  &  \\
         &  &  & 1 &  &  &  \\
        \end{matrix}
        $$


??? example "Case #13: Gr(2,5) / O(1)  del Pezzo 5-fold V5"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Fano Index:** $4$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} + 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} - 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} - 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} + 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \cdot 2^{\frac{3}{4}} i \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $2 \cdot 2^{\frac{3}{4}} i \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \cdot 2^{\frac{3}{4}} \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $2 \cdot 2^{\frac{3}{4}} \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1)


??? example "Case #3: P4 / O(3)  cubic 3-fold"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $2$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $- 6 \sqrt{3}$ (mult: 1), $6 \sqrt{3}$ (mult: 1), $0$ (mult: 2)
    - **Hodge Diamond ($h^{p,q}$):**
        $$
                \begin{matrix}
         &  &  & 1 &  &  &  \\
         &  & 0 &  & 0 &  &  \\
         & 0 &  & 1 &  & 0 &  \\
        0 &  & 5 &  & 5 &  & 0 \\
         & 0 &  & 1 &  & 0 &  \\
         &  & 0 &  & 0 &  &  \\
         &  &  & 1 &  &  &  \\
        \end{matrix}
        $$


??? example "Case #16: Gr(2,5) / O(1)+O(1)  del Pezzo 4-fold"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $3$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $\frac{3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $\frac{3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- \frac{3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $- \frac{3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1)


??? example "Case #14: Gr(2,5) / O(2)  Gushel-Mukai 5-fold"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 3 \sqrt[3]{-22 + 10 \sqrt{5}}$ (mult: 1), $\frac{3 \sqrt[3]{-22 + 10 \sqrt{5}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{-22 + 10 \sqrt{5}}}{2}$ (mult: 1), $\frac{3 \sqrt[3]{-22 + 10 \sqrt{5}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{-22 + 10 \sqrt{5}}}{2}$ (mult: 1), $3 \sqrt[3]{22 + 10 \sqrt{5}}$ (mult: 1), $- \frac{3 \sqrt[3]{22 + 10 \sqrt{5}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{22 + 10 \sqrt{5}}}{2}$ (mult: 1), $- \frac{3 \sqrt[3]{22 + 10 \sqrt{5}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{22 + 10 \sqrt{5}}}{2}$ (mult: 1), $0$ (mult: 2)

    - **Hodge Diamond:**
        $$
        \begin{matrix}
        & & & & & 1 & & & & & \\
        & & & & 0 & & 0 & & & & \\
        & & & 0 & & 1 & & 0 & & & \\
        & & 0 & & 0 & & 0 & & 0 & & \\
        & 0 & & 0 & & 2 & & 0 & & 0 & \\
        0 & & 0 & & 10 & & 10 & & 0 & & 0 \\
        & 0 & & 0 & & 2 & & 0 & & 0 & \\
        & & 0 & & 0 & & 0 & & 0 & & \\
        & & & 0 & & 1 & & 0 & & & \\
        & & & & 0 & & 0 & & & & \\
        & & & & & 1 & & & & & \\
        \end{matrix}
        $$


??? example "Case #8: P5 / O(2)  quadric 4-fold"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $4$
    - **Fano Index:** $4$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $- 4 \sqrt{2}$ (mult: 1), $4 \sqrt{2}$ (mult: 1), $- 4 \sqrt{2} i$ (mult: 1), $4 \sqrt{2} i$ (mult: 1), $0$ (mult: 1)
    - **Hodge Diamond ($h^{p,q}$):**
        $$
                \begin{matrix}
         &  &  &  & 1 &  &  &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 0 &  & 2 &  & 0 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 1 &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #17: Gr(2,5) / O(1)+O(2)  Gushel-Mukai 4-fold"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 4 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $4 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- 4 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $4 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $0$ (mult: 2)

    - **Hodge Diamond:**
        $$
        \begin{matrix}
        & & & & 1 & & & & \\
        & & & 0 & & 0 & & & \\
        & & 0 & & 1 & & 0 & & \\
        & 0 & & 0 & & 0 & & 0 & \\
        0 & & 1 & & 22 & & 1 & & 0 \\
        & 0 & & 0 & & 0 & & 0 & \\
        & & 0 & & 1 & & 0 & & \\
        & & & 0 & & 0 & & & \\
        & & & & 1 & & & & \\
        \end{matrix}
        $$


??? example "Case #22: G2/P1  quadric 5-fold"
    - **Ambient Space:** `$G2$`
    - **Dimension:** $5$
    - **Fano Index:** $5$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $5 \cdot 2^{\frac{2}{5}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{2}{5}} \sqrt{5}}{4} - \frac{5 \cdot 2^{\frac{2}{5}}}{4} - 5 \cdot 2^{\frac{2}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{2}{5}} \sqrt{5}}{4} - \frac{5 \cdot 2^{\frac{2}{5}}}{4} + 5 \cdot 2^{\frac{2}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{2}{5}}}{4} + \frac{5 \cdot 2^{\frac{2}{5}} \sqrt{5}}{4} - 5 \cdot 2^{\frac{2}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{2}{5}}}{4} + \frac{5 \cdot 2^{\frac{2}{5}} \sqrt{5}}{4} + 5 \cdot 2^{\frac{2}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $0$ (mult: 1)


??? example "Case #18: Gr(2,5) / O(1)^3  del Pezzo 3-fold V5"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $2$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 2 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $2 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- 2 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $2 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1)


??? example "Case #10: P5 / O(4)  quartic 4-fold"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-32$ (mult: 1), $32$ (mult: 1), $0$ (mult: 3)
    - **Hodge Diamond ($h^{p,q}$):**
        $$
                \begin{matrix}
         &  &  &  & 1 &  &  &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 21 &  & 142 &  & 21 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 1 &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #23: G2/P2"
    - **Ambient Space:** `$G2$`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $- 3 \sqrt[3]{-9 + 6 \sqrt{3}}$ (mult: 1), $\frac{3 \sqrt[3]{-9 + 6 \sqrt{3}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{-9 + 6 \sqrt{3}}}{2}$ (mult: 1), $\frac{3 \sqrt[3]{-9 + 6 \sqrt{3}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{-9 + 6 \sqrt{3}}}{2}$ (mult: 1), $3 \sqrt[3]{9 + 6 \sqrt{3}}$ (mult: 1), $- \frac{3 \sqrt[3]{9 + 6 \sqrt{3}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{9 + 6 \sqrt{3}}}{2}$ (mult: 1), $- \frac{3 \sqrt[3]{9 + 6 \sqrt{3}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{9 + 6 \sqrt{3}}}{2}$ (mult: 1)


??? example "Case #24: G2/P2 / O(1)"
    - **Ambient Space:** `$G2$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $- 2 i \sqrt{-9 + 6 \sqrt{3}}$ (mult: 1), $2 i \sqrt{-9 + 6 \sqrt{3}}$ (mult: 1), $- 2 \sqrt{9 + 6 \sqrt{3}}$ (mult: 1), $2 \sqrt{9 + 6 \sqrt{3}}$ (mult: 1), $0$ (mult: 1)


??? example "Case #27: OG(3,7) / O(2)"
    - **Ambient Space:** `$B3$`
    - **Dimension:** $5$
    - **Fano Index:** $4$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-8$ (mult: 1), $8$ (mult: 1), $- 8 i$ (mult: 1), $8 i$ (mult: 1), $0$ (mult: 2)


??? example "Case #25: Fl(1,3,4) / O(1,1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $12$
    - **Eigenvalues:** $8$ (mult: 1), $-8$ (mult: 1), $- 4 i$ (mult: 2), $4 i$ (mult: 2), $0$ (mult: 3)


??? example "Case #9: P5 / O(3)  cubic 4-fold"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $4$
    - **Fano Index:** $3$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $9$ (mult: 1), $- \frac{9}{2} - \frac{9 \sqrt{3} i}{2}$ (mult: 1), $- \frac{9}{2} + \frac{9 \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 2)
    - **Hodge Diamond ($h^{p,q}$):**
        $$
                \begin{matrix}
         &  &  &  & 1 &  &  &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 1 &  & 21 &  & 1 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 1 &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #19: Fl(1,4,5)  flag itself (P4xP4 / O(1,1))"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $7$
    - **Fano Index:** $4$
    - **Basis Rank:** $20$
    - **Eigenvalues:** $- 8 \sqrt[4]{2}$ (mult: 1), $4 \operatorname{CRootOf} {\left(x^{8} + 11 x^{4} - 1, 0\right)}$ (mult: 2), $4 \operatorname{CRootOf} {\left(x^{8} + 11 x^{4} - 1, 1\right)}$ (mult: 2), $8 \sqrt[4]{2}$ (mult: 1), $- 8 \sqrt[4]{2} i$ (mult: 1), $8 \sqrt[4]{2} i$ (mult: 1), $4 \operatorname{CRootOf} {\left(x^{8} + 11 x^{4} - 1, 2\right)}$ (mult: 2), $4 \operatorname{CRootOf} {\left(x^{8} + 11 x^{4} - 1, 3\right)}$ (mult: 2), $4 \operatorname{CRootOf} {\left(x^{8} + 11 x^{4} - 1, 4\right)}$ (mult: 2), $4 \operatorname{CRootOf} {\left(x^{8} + 11 x^{4} - 1, 5\right)}$ (mult: 2), $4 \operatorname{CRootOf} {\left(x^{8} + 11 x^{4} - 1, 6\right)}$ (mult: 2), $4 \operatorname{CRootOf} {\left(x^{8} + 11 x^{4} - 1, 7\right)}$ (mult: 2)


??? example "Case #28: OG(3,7) / O(3)"
    - **Ambient Space:** `$B3$`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $9 \cdot 2^{\frac{2}{3}}$ (mult: 1), $- \frac{9 \cdot 2^{\frac{2}{3}}}{2} - \frac{9 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $- \frac{9 \cdot 2^{\frac{2}{3}}}{2} + \frac{9 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 3)


??? example "Case #11: P5 / O(2)+O(2)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $3$
    - **Fano Index:** $2$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-8$ (mult: 1), $8$ (mult: 1), $0$ (mult: 2)
    - **Hodge Diamond ($h^{p,q}$):**
        $$
                \begin{matrix}
         &  &  & 1 &  &  &  \\
         &  & 0 &  & 0 &  &  \\
         & 0 &  & 1 &  & 0 &  \\
        0 &  & 2 &  & 2 &  & 0 \\
         & 0 &  & 1 &  & 0 &  \\
         &  & 0 &  & 0 &  &  \\
         &  &  & 1 &  &  &  \\
        \end{matrix}
        $$


??? example "Case #31: LG(3,6) / O(1)"
    - **Ambient Space:** `$C3$`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $3 \sqrt[3]{12 - 8 \sqrt{2}}$ (mult: 1), $- \frac{3 \sqrt[3]{12 - 8 \sqrt{2}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{12 - 8 \sqrt{2}}}{2}$ (mult: 1), $- \frac{3 \sqrt[3]{12 - 8 \sqrt{2}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{12 - 8 \sqrt{2}}}{2}$ (mult: 1), $3 \sqrt[3]{8 \sqrt{2} + 12}$ (mult: 1), $- \frac{3 \sqrt[3]{8 \sqrt{2} + 12}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{8 \sqrt{2} + 12}}{2}$ (mult: 1), $- \frac{3 \sqrt[3]{8 \sqrt{2} + 12}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{8 \sqrt{2} + 12}}{2}$ (mult: 1)


??? example "Case #30: OG(3,7) / O(2)+O(2)"
    - **Ambient Space:** `$B3$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-16$ (mult: 1), $16$ (mult: 1), $0$ (mult: 3)


??? example "Case #32: LG(3,6) / O(1)+O(1)"
    - **Ambient Space:** `$C3$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $4 - 4 \sqrt{2}$ (mult: 1), $4 + 4 \sqrt{2}$ (mult: 1), $- 4 \sqrt{2} - 4$ (mult: 1), $-4 + 4 \sqrt{2}$ (mult: 1), $0$ (mult: 1)


??? example "Case #21: B2/B / O(1,1)"
    - **Ambient Space:** `$B2$`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-2$ (mult: 2), $- \frac{\sqrt{\frac{568}{3 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209}} + 2 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209} + 60}}{2} + \frac{\sqrt{- \frac{856}{\sqrt{\frac{568}{3 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209}} + 2 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209} + 60}} - 2 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209} - \frac{568}{3 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209}} + 120}}{2}$ (mult: 1), $- \frac{\sqrt{\frac{568}{3 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209}} + 2 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209} + 60}}{2} - \frac{\sqrt{- \frac{856}{\sqrt{\frac{568}{3 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209}} + 2 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209} + 60}} - 2 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209} - \frac{568}{3 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209}} + 120}}{2}$ (mult: 1), $\frac{\sqrt{\frac{568}{3 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209}} + 2 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209} + 60}}{2} + \frac{\sqrt{- 2 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209} - \frac{568}{3 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209}} + \frac{856}{\sqrt{\frac{568}{3 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209}} + 2 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209} + 60}} + 120}}{2}$ (mult: 1), $- \frac{\sqrt{- 2 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209} - \frac{568}{3 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209}} + \frac{856}{\sqrt{\frac{568}{3 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209}} + 2 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209} + 60}} + 120}}{2} + \frac{\sqrt{\frac{568}{3 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209}} + 2 \sqrt[3]{\frac{1591 \sqrt{129}}{9} + 2209} + 60}}{2}$ (mult: 1)


??? example "Case #15: Gr(2,5) / O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 6 i \sqrt{- \frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $6 i \sqrt{- \frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $- 6 \sqrt{\frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $6 \sqrt{\frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $0$ (mult: 4)


??? example "Case #29: OG(3,7) / O(4)"
    - **Ambient Space:** `$B3$`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-64$ (mult: 1), $64$ (mult: 1), $0$ (mult: 4)


??? example "Case #20: Fl(1,4,5) / O(1,1)+O(1,1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $20$
    - **Eigenvalues:** $- 8 \sqrt{2}$ (mult: 1), $8 \sqrt{2}$ (mult: 1), $- 2 \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 2), $- 2 \sqrt{- \frac{5 \sqrt{5}}{2} - \frac{11}{2}}$ (mult: 2), $2 \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 2), $2 \sqrt{- \frac{5 \sqrt{5}}{2} - \frac{11}{2}}$ (mult: 2), $0$ (mult: 2)


??? example "Case #7: Gr(2,4) / O(3)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $96$ (mult: 1), $-12$ (mult: 3)


??? example "Case #4: P4 / O(4)  quartic 3-fold"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $232$ (mult: 1), $-24$ (mult: 3)
    - **Hodge Diamond ($h^{p,q}$):**
        $$
                \begin{matrix}
         &  &  & 1 &  &  &  \\
         &  & 0 &  & 0 &  &  \\
         & 0 &  & 1 &  & 0 &  \\
        0 &  & 30 &  & 30 &  & 0 \\
         & 0 &  & 1 &  & 0 &  \\
         &  & 0 &  & 0 &  &  \\
         &  &  & 1 &  &  &  \\
        \end{matrix}
        $$


??? example "Case #12: Gr(2,6) / O(1)+O(1)+O(2)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $15$
    - **Eigenvalues:** $- 12 \sqrt{3}$ (mult: 1), $12 \sqrt{3}$ (mult: 1), $- 4 i$ (mult: 1), $4 i$ (mult: 1), $0$ (mult: 4)


??? example "Case #26: Fl(1,3,4) / O(1,1)+O(1,1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $12$
    - **Eigenvalues:** $14$ (mult: 1), $-6$ (mult: 2), $-2$ (mult: 3)


??? example "Case #1: Fl(1,2,5) / O(0,1)+O(0,2)+O(1,0)  [GM-20 4-fold]"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $1$
    - **Basis Rank:** $20$
    - **Eigenvalues:** $-3$ (mult: 2), $-2$ (mult: 2), $\operatorname{CRootOf} {\left(x^{5} - 5 x^{4} - 192 x^{3} - 3848 x^{2} - 17040 x - 22928, 0\right)}$ (mult: 1), $\operatorname{CRootOf} {\left(x^{5} - 5 x^{4} - 192 x^{3} - 3848 x^{2} - 17040 x - 22928, 1\right)}$ (mult: 1), $\operatorname{CRootOf} {\left(x^{5} - 5 x^{4} - 192 x^{3} - 3848 x^{2} - 17040 x - 22928, 2\right)}$ (mult: 1), $\operatorname{CRootOf} {\left(x^{5} - 5 x^{4} - 192 x^{3} - 3848 x^{2} - 17040 x - 22928, 3\right)}$ (mult: 1), $\operatorname{CRootOf} {\left(x^{5} - 5 x^{4} - 192 x^{3} - 3848 x^{2} - 17040 x - 22928, 4\right)}$ (mult: 1)


</div>

***
*Note: This catalog is automatically generated.*
