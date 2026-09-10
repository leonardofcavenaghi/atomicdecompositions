# Quantum Geometry Catalog

Welcome to the automated catalog. Below you will find geometric and quantum properties computed for various complete intersections.

## Glossary

- **Ambient Space**: The ambient flag variety $G/P$ in which the complete intersection $X$ is embedded.
- **Dimension**: The complex dimension of the resulting geometric space $X$. Computed by subtracting the rank of the intersecting bundle from the dimension of the ambient space.
- **Fano Index**: The greatest integer $I_X$ dividing the anticanonical class $-K_X$. It dictates the powers of the Novikov parameters in quantum multiplication.
- **Basis Rank**: The number of dimensions in the projected flag-ambient cohomology ring $H_{amb}^*(X)$. This equals the size of the square quantum multiplication matrix.
- **Quantum Matrix ($y=1$)**: The small quantum multiplication matrix $c_1(TX)\star$ projected onto the flag-ambient cohomology ring, evaluated at Novikov parameters $y=1$.
- **Eigenvalues**: The eigenvalues of the small quantum multiplication matrix $c_1(TX)\star$ evaluated at $y=1$, along with their algebraic multiplicities. These values govern the spectrum of the quantum connection.
- **Hodge Diamond**: The geometric $h^{p,q}$ Hodge numbers of the space.

***

<div class="grid cards" markdown>

??? example "Case #4: P3  Fano index 4"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $3$
    - **Fano Index:** $4$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $- 4 i$ (mult: 1), $4 i$ (mult: 1)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 0 & 4\\4 & 0 & 0 & 0\\0 & 4 & 0 & 0\\0 & 0 & 4 & 0\end{matrix}\right]
        $$


??? example "Case #1: P2 Fano index 3"
    - **Ambient Space:** `$A2$`
    - **Dimension:** $2$
    - **Fano Index:** $3$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $3$ (mult: 1), $- \frac{3}{2} - \frac{3 \sqrt{3} i}{2}$ (mult: 1), $- \frac{3}{2} + \frac{3 \sqrt{3} i}{2}$ (mult: 1)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 3\\3 & 0 & 0\\0 & 3 & 0\end{matrix}\right]
        $$


??? example "Case #2: P2  Fano index 3"
    - **Ambient Space:** `$A2$`
    - **Dimension:** $2$
    - **Fano Index:** $3$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $3$ (mult: 1), $- \frac{3}{2} - \frac{3 \sqrt{3} i}{2}$ (mult: 1), $- \frac{3}{2} + \frac{3 \sqrt{3} i}{2}$ (mult: 1)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 3\\3 & 0 & 0\\0 & 3 & 0\end{matrix}\right]
        $$


??? example "Case #3: P2 / O(2)"
    - **Ambient Space:** `$A2$`
    - **Dimension:** $1$
    - **Fano Index:** $1$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $-2$ (mult: 1), $2$ (mult: 1)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 4\\1 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         & 1 &  \\
        0 &  & 0 \\
         & 1 &  \\
        \end{matrix}
        $$


??? example "Case #7: P4  Fano index 5"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $5$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $5$ (mult: 1), $- \frac{5 \sqrt{5}}{4} - \frac{5}{4} - 5 i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \sqrt{5}}{4} - \frac{5}{4} + 5 i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5}{4} + \frac{5 \sqrt{5}}{4} - 5 i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5}{4} + \frac{5 \sqrt{5}}{4} + 5 i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 5\\5 & 0 & 0 & 0 & 0\\0 & 5 & 0 & 0 & 0\\0 & 0 & 5 & 0 & 0\\0 & 0 & 0 & 5 & 0\end{matrix}\right]
        $$


??? example "Case #5: P3 / O(2)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Fano Index:** $2$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $0$ (mult: 1)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 4 & 0\\2 & 0 & 4\\0 & 2 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  & 1 &  &  \\
         & 0 &  & 0 &  \\
        0 &  & 2 &  & 0 \\
         & 0 &  & 0 &  \\
         &  & 1 &  &  \\
        \end{matrix}
        $$


??? example "Case #8: P4 / O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $3$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $3 \cdot 2^{\frac{2}{3}}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} - \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} + \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 1)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 6 & 0\\3 & 0 & 0 & 6\\0 & 3 & 0 & 0\\0 & 0 & 3 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
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


??? example "Case #10: P4 / O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $2$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $- 6 \sqrt{3}$ (mult: 1), $6 \sqrt{3}$ (mult: 1), $0$ (mult: 2)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 12 & 0 & 72\\2 & 0 & 30 & 0\\0 & 2 & 0 & 12\\0 & 0 & 2 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
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


??? example "Case #12: P5  Fano index 6"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $5$
    - **Fano Index:** $6$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-6$ (mult: 1), $6$ (mult: 1), $-3 - 3 \sqrt{3} i$ (mult: 1), $-3 + 3 \sqrt{3} i$ (mult: 1), $3 - 3 \sqrt{3} i$ (mult: 1), $3 + 3 \sqrt{3} i$ (mult: 1)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 0 & 6\\6 & 0 & 0 & 0 & 0 & 0\\0 & 6 & 0 & 0 & 0 & 0\\0 & 0 & 6 & 0 & 0 & 0\\0 & 0 & 0 & 6 & 0 & 0\\0 & 0 & 0 & 0 & 6 & 0\end{matrix}\right]
        $$


??? example "Case #13: P5 / O(2)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $4$
    - **Fano Index:** $4$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $- 4 \sqrt{2}$ (mult: 1), $4 \sqrt{2}$ (mult: 1), $- 4 \sqrt{2} i$ (mult: 1), $4 \sqrt{2} i$ (mult: 1), $0$ (mult: 1)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 0 & 8 & 0\\4 & 0 & 0 & 0 & 8\\0 & 4 & 0 & 0 & 0\\0 & 0 & 4 & 0 & 0\\0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
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


??? example "Case #14: P5 / O(2)+O(2)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $3$
    - **Fano Index:** $2$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-8$ (mult: 1), $8$ (mult: 1), $0$ (mult: 2)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 8 & 0 & 32\\2 & 0 & 16 & 0\\0 & 2 & 0 & 8\\0 & 0 & 2 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
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


??? example "Case #6: P3 / O(3)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Fano Index:** $1$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $21$ (mult: 1), $-6$ (mult: 2)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 108 & 756\\1 & 9 & 108\\0 & 1 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  & 1 &  &  \\
         & 0 &  & 0 &  \\
        0 &  & 7 &  & 0 \\
         & 0 &  & 0 &  \\
         &  & 1 &  &  \\
        \end{matrix}
        $$


??? example "Case #16: P5 / O(3)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $4$
    - **Fano Index:** $3$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $9$ (mult: 1), $- \frac{9}{2} - \frac{9 \sqrt{3} i}{2}$ (mult: 1), $- \frac{9}{2} + \frac{9 \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 2)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 18 & 0 & 0\\3 & 0 & 0 & 45 & 0\\0 & 3 & 0 & 0 & 18\\0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
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


??? example "Case #17: P5 / O(4)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-32$ (mult: 1), $32$ (mult: 1), $0$ (mult: 3)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 48 & 0 & 5568 & 0\\2 & 0 & 208 & 0 & 5568\\0 & 2 & 0 & 208 & 0\\0 & 0 & 2 & 0 & 48\\0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
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


??? example "Case #9: P4 / O(2)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $2$
    - **Fano Index:** $1$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $12$ (mult: 1), $-4$ (mult: 2)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 40 & 192\\1 & 4 & 40\\0 & 1 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  & 1 &  &  \\
         & 0 &  & 0 &  \\
        0 &  & 6 &  & 0 \\
         & 0 &  & 0 &  \\
         &  & 1 &  &  \\
        \end{matrix}
        $$


??? example "Case #21: P6 / O(2)+O(2)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $4$
    - **Fano Index:** $3$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $6 \sqrt[3]{2}$ (mult: 1), $- 3 \sqrt[3]{2} - 3 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $- 3 \sqrt[3]{2} + 3 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $0$ (mult: 2)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 12 & 0 & 0\\3 & 0 & 0 & 24 & 0\\0 & 3 & 0 & 0 & 12\\0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  &  & 1 &  &  &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 0 &  & 8 &  & 0 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 1 &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #19: P6  Fano index 7"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $6$
    - **Fano Index:** $7$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $7$ (mult: 1), $- 7 \cos{\left(\frac{\pi}{7} \right)} - 7 i \sin{\left(\frac{\pi}{7} \right)}$ (mult: 1), $- 7 \cos{\left(\frac{\pi}{7} \right)} + 7 i \sin{\left(\frac{\pi}{7} \right)}$ (mult: 1), $- 7 \cos{\left(\frac{3 \pi}{7} \right)} - 7 i \sin{\left(\frac{3 \pi}{7} \right)}$ (mult: 1), $- 7 \cos{\left(\frac{3 \pi}{7} \right)} + 7 i \sin{\left(\frac{3 \pi}{7} \right)}$ (mult: 1), $7 \cos{\left(\frac{2 \pi}{7} \right)} - 7 i \sin{\left(\frac{2 \pi}{7} \right)}$ (mult: 1), $7 \cos{\left(\frac{2 \pi}{7} \right)} + 7 i \sin{\left(\frac{2 \pi}{7} \right)}$ (mult: 1)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 0 & 0 & 7\\7 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 7 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 7 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 7 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 7 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 7 & 0\end{matrix}\right]
        $$


??? example "Case #23: P6 / O(2)+O(3)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $- 12 \sqrt{3}$ (mult: 1), $12 \sqrt{3}$ (mult: 1), $0$ (mult: 3)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 24 & 0 & 1152 & 0\\2 & 0 & 84 & 0 & 1152\\0 & 2 & 0 & 84 & 0\\0 & 0 & 2 & 0 & 24\\0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  &  & 1 &  &  &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 8 &  & 70 &  & 8 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 1 &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #20: P6 / O(2)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $5$
    - **Fano Index:** $5$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $5 \cdot 2^{\frac{2}{5}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{2}{5}} \sqrt{5}}{4} - \frac{5 \cdot 2^{\frac{2}{5}}}{4} - 5 \cdot 2^{\frac{2}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{2}{5}} \sqrt{5}}{4} - \frac{5 \cdot 2^{\frac{2}{5}}}{4} + 5 \cdot 2^{\frac{2}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{2}{5}}}{4} + \frac{5 \cdot 2^{\frac{2}{5}} \sqrt{5}}{4} - 5 \cdot 2^{\frac{2}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{2}{5}}}{4} + \frac{5 \cdot 2^{\frac{2}{5}} \sqrt{5}}{4} + 5 \cdot 2^{\frac{2}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $0$ (mult: 1)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 10 & 0\\5 & 0 & 0 & 0 & 0 & 10\\0 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 5 & 0 & 0 & 0\\0 & 0 & 0 & 5 & 0 & 0\\0 & 0 & 0 & 0 & 5 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  &  &  & 1 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
        0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 1 &  &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #27: P6 / O(4)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $12 \cdot 2^{\frac{2}{3}}$ (mult: 1), $- 6 \cdot 2^{\frac{2}{3}} - 6 \cdot 2^{\frac{2}{3}} \sqrt{3} i$ (mult: 1), $- 6 \cdot 2^{\frac{2}{3}} + 6 \cdot 2^{\frac{2}{3}} \sqrt{3} i$ (mult: 1), $0$ (mult: 3)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 72 & 0 & 0 & 1728\\3 & 0 & 0 & 312 & 0 & 0\\0 & 3 & 0 & 0 & 312 & 0\\0 & 0 & 3 & 0 & 0 & 72\\0 & 0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  &  &  & 1 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
        0 &  & 7 &  & 266 &  & 266 &  & 7 &  & 0 \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 1 &  &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #25: P6 / O(3)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $5$
    - **Fano Index:** $4$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $- 4 \cdot 3^{\frac{3}{4}}$ (mult: 1), $4 \cdot 3^{\frac{3}{4}}$ (mult: 1), $- 4 \cdot 3^{\frac{3}{4}} i$ (mult: 1), $4 \cdot 3^{\frac{3}{4}} i$ (mult: 1), $0$ (mult: 2)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 0 & 24 & 0 & 0\\4 & 0 & 0 & 0 & 60 & 0\\0 & 4 & 0 & 0 & 0 & 24\\0 & 0 & 4 & 0 & 0 & 0\\0 & 0 & 0 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  &  &  & 1 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
        0 &  & 0 &  & 21 &  & 21 &  & 0 &  & 0 \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 1 &  &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #28: P6 / O(5)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $- 50 \sqrt{5}$ (mult: 1), $50 \sqrt{5}$ (mult: 1), $0$ (mult: 4)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 240 & 0 & 422400 & 0 & 62640000\\2 & 0 & 1540 & 0 & 1385000 & 0\\0 & 2 & 0 & 2690 & 0 & 422400\\0 & 0 & 2 & 0 & 1540 & 0\\0 & 0 & 0 & 2 & 0 & 240\\0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  &  &  & 1 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
        0 &  & 84 &  & 1554 &  & 1554 &  & 84 &  & 0 \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 1 &  &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #11: P4 / O(4)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $232$ (mult: 1), $-24$ (mult: 3)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 3888 & 504576 & 18323712\\1 & 80 & 13600 & 504576\\0 & 1 & 80 & 3888\\0 & 0 & 1 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
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


??? example "Case #15: P5 / O(2)+O(3)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $96$ (mult: 1), $-12$ (mult: 3)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 792 & 43632 & 793152\\1 & 30 & 2340 & 43632\\0 & 1 & 30 & 792\\0 & 0 & 1 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  & 1 &  &  &  \\
         &  & 0 &  & 0 &  &  \\
         & 0 &  & 1 &  & 0 &  \\
        0 &  & 20 &  & 20 &  & 0 \\
         & 0 &  & 1 &  & 0 &  \\
         &  & 0 &  & 0 &  &  \\
         &  &  & 1 &  &  &  \\
        \end{matrix}
        $$


??? example "Case #31: P7 / O(2)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $6$
    - **Fano Index:** $6$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $- 6 \sqrt[3]{2}$ (mult: 1), $6 \sqrt[3]{2}$ (mult: 1), $- 3 \sqrt[3]{2} - 3 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $- 3 \sqrt[3]{2} + 3 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $3 \sqrt[3]{2} - 3 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $3 \sqrt[3]{2} + 3 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $0$ (mult: 1)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 0 & 12 & 0\\6 & 0 & 0 & 0 & 0 & 0 & 12\\0 & 6 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 6 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 6 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 6 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 6 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 0 &  & 0 &  & 2 &  & 0 &  & 0 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #32: P7 / O(2)+O(2)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $5$
    - **Fano Index:** $4$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-8$ (mult: 1), $8$ (mult: 1), $- 8 i$ (mult: 1), $8 i$ (mult: 1), $0$ (mult: 2)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 0 & 16 & 0 & 0\\4 & 0 & 0 & 0 & 32 & 0\\0 & 4 & 0 & 0 & 0 & 16\\0 & 0 & 4 & 0 & 0 & 0\\0 & 0 & 0 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  &  &  & 1 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
        0 &  & 0 &  & 3 &  & 3 &  & 0 &  & 0 \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 1 &  &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #33: P7 / O(2)+O(2)+O(2)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-16$ (mult: 1), $16$ (mult: 1), $0$ (mult: 3)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 16 & 0 & 448 & 0\\2 & 0 & 48 & 0 & 448\\0 & 2 & 0 & 48 & 0\\0 & 0 & 2 & 0 & 16\\0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  &  & 1 &  &  &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 3 &  & 38 &  & 3 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 1 &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #35: P7 / O(2)+O(3)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $9 \cdot 2^{\frac{2}{3}}$ (mult: 1), $- \frac{9 \cdot 2^{\frac{2}{3}}}{2} - \frac{9 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $- \frac{9 \cdot 2^{\frac{2}{3}}}{2} + \frac{9 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 3)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 36 & 0 & 0 & 432\\3 & 0 & 0 & 126 & 0 & 0\\0 & 3 & 0 & 0 & 126 & 0\\0 & 0 & 3 & 0 & 0 & 36\\0 & 0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  &  &  & 1 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
        0 &  & 1 &  & 83 &  & 83 &  & 1 &  & 0 \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 1 &  &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #30: P7  Fano index 8"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $7$
    - **Fano Index:** $8$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-8$ (mult: 1), $8$ (mult: 1), $- 4 \sqrt{2} - 4 \sqrt{2} i$ (mult: 1), $- 4 \sqrt{2} + 4 \sqrt{2} i$ (mult: 1), $- 8 i$ (mult: 1), $8 i$ (mult: 1), $4 \sqrt{2} - 4 \sqrt{2} i$ (mult: 1), $4 \sqrt{2} + 4 \sqrt{2} i$ (mult: 1)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 0 & 0 & 0 & 8\\8 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 8 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 8 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 8 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 8 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 8 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 8 & 0\end{matrix}\right]
        $$


??? example "Case #36: P7 / O(2)+O(4)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-64$ (mult: 1), $64$ (mult: 1), $0$ (mult: 4)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 96 & 0 & 53376 & 0 & 3207168\\2 & 0 & 512 & 0 & 157952 & 0\\0 & 2 & 0 & 832 & 0 & 53376\\0 & 0 & 2 & 0 & 512 & 0\\0 & 0 & 0 & 2 & 0 & 96\\0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  &  &  & 1 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
        0 &  & 36 &  & 783 &  & 783 &  & 36 &  & 0 \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 1 &  &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #38: P7 / O(3)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $6$
    - **Fano Index:** $5$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $5 \cdot 3^{\frac{3}{5}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} - \frac{5 \cdot 3^{\frac{3}{5}}}{4} - 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} - \frac{5 \cdot 3^{\frac{3}{5}}}{4} + 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}}}{4} + \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} - 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}}}{4} + \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} + 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $0$ (mult: 2)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 30 & 0 & 0\\5 & 0 & 0 & 0 & 0 & 75 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 30\\0 & 0 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 5 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 5 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 5 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 0 &  & 8 &  & 71 &  & 8 &  & 0 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
        \end{matrix}
        $$


??? example "Case #42: P7 / O(5)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $6$
    - **Fano Index:** $3$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $15 \cdot 5^{\frac{2}{3}}$ (mult: 1), $- \frac{15 \cdot 5^{\frac{2}{3}}}{2} - \frac{15 \sqrt{3} \cdot 5^{\frac{2}{3}} i}{2}$ (mult: 1), $- \frac{15 \cdot 5^{\frac{2}{3}}}{2} + \frac{15 \sqrt{3} \cdot 5^{\frac{2}{3}} i}{2}$ (mult: 1), $0$ (mult: 4)
    ??? note "Quantum Matrix ($y=1$)"
        $$
        \left[\begin{matrix}0 & 0 & 360 & 0 & 0 & 298800 & 0\\3 & 0 & 0 & 2310 & 0 & 0 & 298800\\0 & 3 & 0 & 0 & 4035 & 0 & 0\\0 & 0 & 3 & 0 & 0 & 2310 & 0\\0 & 0 & 0 & 3 & 0 & 0 & 360\\0 & 0 & 0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$
    ??? note "Hodge Diamond ($h^{p,q}$)"
        $$
        \begin{matrix}
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 36 &  & 2472 &  & 8093 &  & 2472 &  & 36 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
        \end{matrix}
        $$


</div>

***
*Note: This catalog is automatically generated.*
