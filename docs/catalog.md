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

??? example "Case #2: P2  Fano index 3"
    - **Ambient Space:** `$A2$`
    - **Dimension:** $2$
    - **Fano Index:** $3$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $3$ (mult: 1), $- \frac{3}{2} - \frac{3 \sqrt{3} i}{2}$ (mult: 1), $- \frac{3}{2} + \frac{3 \sqrt{3} i}{2}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 3\\3 & 0 & 0\\0 & 3 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #4: P3  Fano index 4"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $3$
    - **Fano Index:** $4$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $- 4 i$ (mult: 1), $4 i$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 4\\4 & 0 & 0 & 0\\0 & 4 & 0 & 0\\0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #1: P2 Fano index 3"
    - **Ambient Space:** `$A2$`
    - **Dimension:** $2$
    - **Fano Index:** $3$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $3$ (mult: 1), $- \frac{3}{2} - \frac{3 \sqrt{3} i}{2}$ (mult: 1), $- \frac{3}{2} + \frac{3 \sqrt{3} i}{2}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 3\\3 & 0 & 0\\0 & 3 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #7: P4  Fano index 5"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $5$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $5$ (mult: 1), $- \frac{5 \sqrt{5}}{4} - \frac{5}{4} - 5 i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \sqrt{5}}{4} - \frac{5}{4} + 5 i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5}{4} + \frac{5 \sqrt{5}}{4} - 5 i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5}{4} + \frac{5 \sqrt{5}}{4} + 5 i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 5\\5 & 0 & 0 & 0 & 0\\0 & 5 & 0 & 0 & 0\\0 & 0 & 5 & 0 & 0\\0 & 0 & 0 & 5 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #5: P3 / O(2)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Fano Index:** $2$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $0$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 4 & 0\\2 & 0 & 4\\0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  & 1 &  &  \\
         & 0 &  & 0 &  \\
        0 &  & 2 &  & 0 \\
         & 0 &  & 0 &  \\
         &  & 1 &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #3: P2 / O(2)"
    - **Ambient Space:** `$A2$`
    - **Dimension:** $1$
    - **Fano Index:** $1$
    - **Basis Rank:** $3$
    - **Eigenvalues:** $-2$ (mult: 1), $2$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 4\\1 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         & 1 &  \\
        0 &  & 0 \\
         & 1 &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #8: P4 / O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $3$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $3 \cdot 2^{\frac{2}{3}}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} - \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} + \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 6 & 0\\3 & 0 & 0 & 6\\0 & 3 & 0 & 0\\0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #10: P4 / O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $2$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $- 6 \sqrt{3}$ (mult: 1), $6 \sqrt{3}$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 12 & 0 & 72\\2 & 0 & 30 & 0\\0 & 2 & 0 & 12\\0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #12: P5  Fano index 6"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $5$
    - **Fano Index:** $6$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-6$ (mult: 1), $6$ (mult: 1), $-3 - 3 \sqrt{3} i$ (mult: 1), $-3 + 3 \sqrt{3} i$ (mult: 1), $3 - 3 \sqrt{3} i$ (mult: 1), $3 + 3 \sqrt{3} i$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 0 & 6\\6 & 0 & 0 & 0 & 0 & 0\\0 & 6 & 0 & 0 & 0 & 0\\0 & 0 & 6 & 0 & 0 & 0\\0 & 0 & 0 & 6 & 0 & 0\\0 & 0 & 0 & 0 & 6 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #16: P5 / O(3)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $4$
    - **Fano Index:** $3$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $9$ (mult: 1), $- \frac{9}{2} - \frac{9 \sqrt{3} i}{2}$ (mult: 1), $- \frac{9}{2} + \frac{9 \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 18 & 0 & 0\\3 & 0 & 0 & 45 & 0\\0 & 3 & 0 & 0 & 18\\0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #6: P3 / O(3)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Fano Index:** $1$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $21$ (mult: 1), $-6$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 108 & 756\\1 & 9 & 108\\0 & 1 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  & 1 &  &  \\
         & 0 &  & 0 &  \\
        0 &  & 7 &  & 0 \\
         & 0 &  & 0 &  \\
         &  & 1 &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #13: P5 / O(2)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $4$
    - **Fano Index:** $4$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $- 4 \sqrt{2}$ (mult: 1), $4 \sqrt{2}$ (mult: 1), $- 4 \sqrt{2} i$ (mult: 1), $4 \sqrt{2} i$ (mult: 1), $0$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 8 & 0\\4 & 0 & 0 & 0 & 8\\0 & 4 & 0 & 0 & 0\\0 & 0 & 4 & 0 & 0\\0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #17: P5 / O(4)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-32$ (mult: 1), $32$ (mult: 1), $0$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 48 & 0 & 5568 & 0\\2 & 0 & 208 & 0 & 5568\\0 & 2 & 0 & 208 & 0\\0 & 0 & 2 & 0 & 48\\0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #9: P4 / O(2)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $2$
    - **Fano Index:** $1$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $12$ (mult: 1), $-4$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 40 & 192\\1 & 4 & 40\\0 & 1 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  & 1 &  &  \\
         & 0 &  & 0 &  \\
        0 &  & 6 &  & 0 \\
         & 0 &  & 0 &  \\
         &  & 1 &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #14: P5 / O(2)+O(2)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $3$
    - **Fano Index:** $2$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-8$ (mult: 1), $8$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 8 & 0 & 32\\2 & 0 & 16 & 0\\0 & 2 & 0 & 8\\0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #20: P6 / O(2)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $5$
    - **Fano Index:** $5$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $5 \cdot 2^{\frac{2}{5}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{2}{5}} \sqrt{5}}{4} - \frac{5 \cdot 2^{\frac{2}{5}}}{4} - 5 \cdot 2^{\frac{2}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{2}{5}} \sqrt{5}}{4} - \frac{5 \cdot 2^{\frac{2}{5}}}{4} + 5 \cdot 2^{\frac{2}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{2}{5}}}{4} + \frac{5 \cdot 2^{\frac{2}{5}} \sqrt{5}}{4} - 5 \cdot 2^{\frac{2}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{2}{5}}}{4} + \frac{5 \cdot 2^{\frac{2}{5}} \sqrt{5}}{4} + 5 \cdot 2^{\frac{2}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $0$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 10 & 0\\5 & 0 & 0 & 0 & 0 & 10\\0 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 5 & 0 & 0 & 0\\0 & 0 & 0 & 5 & 0 & 0\\0 & 0 & 0 & 0 & 5 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #19: P6  Fano index 7"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $6$
    - **Fano Index:** $7$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $7$ (mult: 1), $- 7 \cos{\left(\frac{\pi}{7} \right)} - 7 i \sin{\left(\frac{\pi}{7} \right)}$ (mult: 1), $- 7 \cos{\left(\frac{\pi}{7} \right)} + 7 i \sin{\left(\frac{\pi}{7} \right)}$ (mult: 1), $- 7 \cos{\left(\frac{3 \pi}{7} \right)} - 7 i \sin{\left(\frac{3 \pi}{7} \right)}$ (mult: 1), $- 7 \cos{\left(\frac{3 \pi}{7} \right)} + 7 i \sin{\left(\frac{3 \pi}{7} \right)}$ (mult: 1), $7 \cos{\left(\frac{2 \pi}{7} \right)} - 7 i \sin{\left(\frac{2 \pi}{7} \right)}$ (mult: 1), $7 \cos{\left(\frac{2 \pi}{7} \right)} + 7 i \sin{\left(\frac{2 \pi}{7} \right)}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 0 & 0 & 7\\7 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 7 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 7 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 7 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 7 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 7 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #27: P6 / O(4)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $12 \cdot 2^{\frac{2}{3}}$ (mult: 1), $- 6 \cdot 2^{\frac{2}{3}} - 6 \cdot 2^{\frac{2}{3}} \sqrt{3} i$ (mult: 1), $- 6 \cdot 2^{\frac{2}{3}} + 6 \cdot 2^{\frac{2}{3}} \sqrt{3} i$ (mult: 1), $0$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 72 & 0 & 0 & 1728\\3 & 0 & 0 & 312 & 0 & 0\\0 & 3 & 0 & 0 & 312 & 0\\0 & 0 & 3 & 0 & 0 & 72\\0 & 0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #23: P6 / O(2)+O(3)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $- 12 \sqrt{3}$ (mult: 1), $12 \sqrt{3}$ (mult: 1), $0$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 24 & 0 & 1152 & 0\\2 & 0 & 84 & 0 & 1152\\0 & 2 & 0 & 84 & 0\\0 & 0 & 2 & 0 & 24\\0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #21: P6 / O(2)+O(2)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $4$
    - **Fano Index:** $3$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $6 \sqrt[3]{2}$ (mult: 1), $- 3 \sqrt[3]{2} - 3 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $- 3 \sqrt[3]{2} + 3 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 12 & 0 & 0\\3 & 0 & 0 & 24 & 0\\0 & 3 & 0 & 0 & 12\\0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #25: P6 / O(3)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $5$
    - **Fano Index:** $4$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $- 4 \cdot 3^{\frac{3}{4}}$ (mult: 1), $4 \cdot 3^{\frac{3}{4}}$ (mult: 1), $- 4 \cdot 3^{\frac{3}{4}} i$ (mult: 1), $4 \cdot 3^{\frac{3}{4}} i$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 24 & 0 & 0\\4 & 0 & 0 & 0 & 60 & 0\\0 & 4 & 0 & 0 & 0 & 24\\0 & 0 & 4 & 0 & 0 & 0\\0 & 0 & 0 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #28: P6 / O(5)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $- 50 \sqrt{5}$ (mult: 1), $50 \sqrt{5}$ (mult: 1), $0$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 240 & 0 & 422400 & 0 & 62640000\\2 & 0 & 1540 & 0 & 1385000 & 0\\0 & 2 & 0 & 2690 & 0 & 422400\\0 & 0 & 2 & 0 & 1540 & 0\\0 & 0 & 0 & 2 & 0 & 240\\0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #11: P4 / O(4)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $232$ (mult: 1), $-24$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 3888 & 504576 & 18323712\\1 & 80 & 13600 & 504576\\0 & 1 & 80 & 3888\\0 & 0 & 1 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #15: P5 / O(2)+O(3)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $96$ (mult: 1), $-12$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 792 & 43632 & 793152\\1 & 30 & 2340 & 43632\\0 & 1 & 30 & 792\\0 & 0 & 1 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #30: P7  Fano index 8"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $7$
    - **Fano Index:** $8$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-8$ (mult: 1), $8$ (mult: 1), $- 4 \sqrt{2} - 4 \sqrt{2} i$ (mult: 1), $- 4 \sqrt{2} + 4 \sqrt{2} i$ (mult: 1), $- 8 i$ (mult: 1), $8 i$ (mult: 1), $4 \sqrt{2} - 4 \sqrt{2} i$ (mult: 1), $4 \sqrt{2} + 4 \sqrt{2} i$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 0 & 0 & 0 & 8\\8 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 8 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 8 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 8 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 8 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 8 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 8 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #31: P7 / O(2)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $6$
    - **Fano Index:** $6$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $- 6 \sqrt[3]{2}$ (mult: 1), $6 \sqrt[3]{2}$ (mult: 1), $- 3 \sqrt[3]{2} - 3 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $- 3 \sqrt[3]{2} + 3 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $3 \sqrt[3]{2} - 3 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $3 \sqrt[3]{2} + 3 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $0$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 0 & 12 & 0\\6 & 0 & 0 & 0 & 0 & 0 & 12\\0 & 6 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 6 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 6 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 6 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 6 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #32: P7 / O(2)+O(2)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $5$
    - **Fano Index:** $4$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-8$ (mult: 1), $8$ (mult: 1), $- 8 i$ (mult: 1), $8 i$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 16 & 0 & 0\\4 & 0 & 0 & 0 & 32 & 0\\0 & 4 & 0 & 0 & 0 & 16\\0 & 0 & 4 & 0 & 0 & 0\\0 & 0 & 0 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #33: P7 / O(2)+O(2)+O(2)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-16$ (mult: 1), $16$ (mult: 1), $0$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 16 & 0 & 448 & 0\\2 & 0 & 48 & 0 & 448\\0 & 2 & 0 & 48 & 0\\0 & 0 & 2 & 0 & 16\\0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #35: P7 / O(2)+O(3)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $9 \cdot 2^{\frac{2}{3}}$ (mult: 1), $- \frac{9 \cdot 2^{\frac{2}{3}}}{2} - \frac{9 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $- \frac{9 \cdot 2^{\frac{2}{3}}}{2} + \frac{9 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 36 & 0 & 0 & 432\\3 & 0 & 0 & 126 & 0 & 0\\0 & 3 & 0 & 0 & 126 & 0\\0 & 0 & 3 & 0 & 0 & 36\\0 & 0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #36: P7 / O(2)+O(4)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-64$ (mult: 1), $64$ (mult: 1), $0$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 96 & 0 & 53376 & 0 & 3207168\\2 & 0 & 512 & 0 & 157952 & 0\\0 & 2 & 0 & 832 & 0 & 53376\\0 & 0 & 2 & 0 & 512 & 0\\0 & 0 & 0 & 2 & 0 & 96\\0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #38: P7 / O(3)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $6$
    - **Fano Index:** $5$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $5 \cdot 3^{\frac{3}{5}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} - \frac{5 \cdot 3^{\frac{3}{5}}}{4} - 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} - \frac{5 \cdot 3^{\frac{3}{5}}}{4} + 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}}}{4} + \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} - 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}}}{4} + \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} + 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 30 & 0 & 0\\5 & 0 & 0 & 0 & 0 & 75 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 30\\0 & 0 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 5 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 5 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 5 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #39: P7 / O(3)+O(3)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-54$ (mult: 1), $54$ (mult: 1), $0$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 72 & 0 & 28512 & 0 & 1283040\\2 & 0 & 360 & 0 & 79056 & 0\\0 & 2 & 0 & 594 & 0 & 28512\\0 & 0 & 2 & 0 & 360 & 0\\0 & 0 & 0 & 2 & 0 & 72\\0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  & 1 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
        0 &  & 16 &  & 410 &  & 410 &  & 16 &  & 0 \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 1 &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #41: P7 / O(4)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $6$
    - **Fano Index:** $4$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-16$ (mult: 1), $16$ (mult: 1), $- 16 i$ (mult: 1), $16 i$ (mult: 1), $0$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 96 & 0 & 0 & 0\\4 & 0 & 0 & 0 & 416 & 0 & 0\\0 & 4 & 0 & 0 & 0 & 416 & 0\\0 & 0 & 4 & 0 & 0 & 0 & 96\\0 & 0 & 0 & 4 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 1 &  & 266 &  & 1108 &  & 266 &  & 1 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #42: P7 / O(5)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $6$
    - **Fano Index:** $3$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $15 \cdot 5^{\frac{2}{3}}$ (mult: 1), $- \frac{15 \cdot 5^{\frac{2}{3}}}{2} - \frac{15 \sqrt{3} \cdot 5^{\frac{2}{3}} i}{2}$ (mult: 1), $- \frac{15 \cdot 5^{\frac{2}{3}}}{2} + \frac{15 \sqrt{3} \cdot 5^{\frac{2}{3}} i}{2}$ (mult: 1), $0$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 360 & 0 & 0 & 298800 & 0\\3 & 0 & 0 & 2310 & 0 & 0 & 298800\\0 & 3 & 0 & 0 & 4035 & 0 & 0\\0 & 0 & 3 & 0 & 0 & 2310 & 0\\0 & 0 & 0 & 3 & 0 & 0 & 360\\0 & 0 & 0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

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

    </details>


??? example "Case #43: P7 / O(6)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $6$
    - **Fano Index:** $2$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $-432$ (mult: 1), $432$ (mult: 1), $0$ (mult: 5)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 1440 & 0 & 37687680 & 0 & 288139991040 & 0\\2 & 0 & 12528 & 0 & 262916928 & 0 & 288139991040\\0 & 2 & 0 & 32688 & 0 & 262916928 & 0\\0 & 0 & 2 & 0 & 32688 & 0 & 37687680\\0 & 0 & 0 & 2 & 0 & 12528 & 0\\0 & 0 & 0 & 0 & 2 & 0 & 1440\\0 & 0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 330 &  & 13140 &  & 38166 &  & 13140 &  & 330 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #22: P6 / O(2)+O(2)+O(2)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $56$ (mult: 1), $-8$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 304 & 9984 & 121088\\1 & 16 & 800 & 9984\\0 & 1 & 16 & 304\\0 & 0 & 1 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  & 1 &  &  &  \\
         &  & 0 &  & 0 &  &  \\
         & 0 &  & 1 &  & 0 &  \\
        0 &  & 14 &  & 14 &  & 0 \\
         & 0 &  & 1 &  & 0 &  \\
         &  & 0 &  & 0 &  &  \\
         &  &  & 1 &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #18: P5 / O(5)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $4$
    - **Fano Index:** $1$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $3005$ (mult: 1), $-120$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 198000 & 395550000 & 423858600000 & 109236016800000\\1 & 650 & 1487500 & 1620307500 & 423858600000\\0 & 1 & 1225 & 1487500 & 395550000\\0 & 0 & 1 & 650 & 198000\\0 & 0 & 0 & 1 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  & 1 &  &  &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 120 &  & 581 &  & 120 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 1 &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #45: P8  Fano index 9"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $8$
    - **Fano Index:** $9$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $9$ (mult: 1), $- 9 \cos{\left(\frac{\pi}{9} \right)} - 9 i \sin{\left(\frac{\pi}{9} \right)}$ (mult: 1), $- 9 \cos{\left(\frac{\pi}{9} \right)} + 9 i \sin{\left(\frac{\pi}{9} \right)}$ (mult: 1), $- \frac{9}{2} - \frac{9 \sqrt{3} i}{2}$ (mult: 1), $- \frac{9}{2} + \frac{9 \sqrt{3} i}{2}$ (mult: 1), $9 \cos{\left(\frac{4 \pi}{9} \right)} - 9 i \sin{\left(\frac{4 \pi}{9} \right)}$ (mult: 1), $9 \cos{\left(\frac{4 \pi}{9} \right)} + 9 i \sin{\left(\frac{4 \pi}{9} \right)}$ (mult: 1), $9 \cos{\left(\frac{2 \pi}{9} \right)} - 9 i \sin{\left(\frac{2 \pi}{9} \right)}$ (mult: 1), $9 \cos{\left(\frac{2 \pi}{9} \right)} + 9 i \sin{\left(\frac{2 \pi}{9} \right)}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 9\\9 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 9 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 9 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 9 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 9 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 9 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 9 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 9 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #47: P8 / O(2)+O(2)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $6$
    - **Fano Index:** $5$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $5 \cdot 2^{\frac{4}{5}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{4}{5}} \sqrt{5}}{4} - \frac{5 \cdot 2^{\frac{4}{5}}}{4} - 5 \cdot 2^{\frac{4}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{4}{5}} \sqrt{5}}{4} - \frac{5 \cdot 2^{\frac{4}{5}}}{4} + 5 \cdot 2^{\frac{4}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{4}{5}}}{4} + \frac{5 \cdot 2^{\frac{4}{5}} \sqrt{5}}{4} - 5 \cdot 2^{\frac{4}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{4}{5}}}{4} + \frac{5 \cdot 2^{\frac{4}{5}} \sqrt{5}}{4} + 5 \cdot 2^{\frac{4}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 20 & 0 & 0\\5 & 0 & 0 & 0 & 0 & 40 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 20\\0 & 0 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 5 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 5 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 5 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 0 &  & 0 &  & 10 &  & 0 &  & 0 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #46: P8 / O(2)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $7$
    - **Fano Index:** $7$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $7 \cdot 2^{\frac{2}{7}}$ (mult: 1), $- 7 \cdot 2^{\frac{2}{7}} \cos{\left(\frac{\pi}{7} \right)} - 7 \cdot 2^{\frac{2}{7}} i \sin{\left(\frac{\pi}{7} \right)}$ (mult: 1), $- 7 \cdot 2^{\frac{2}{7}} \cos{\left(\frac{\pi}{7} \right)} + 7 \cdot 2^{\frac{2}{7}} i \sin{\left(\frac{\pi}{7} \right)}$ (mult: 1), $- 7 \cdot 2^{\frac{2}{7}} \cos{\left(\frac{3 \pi}{7} \right)} - 7 \cdot 2^{\frac{2}{7}} i \sin{\left(\frac{3 \pi}{7} \right)}$ (mult: 1), $- 7 \cdot 2^{\frac{2}{7}} \cos{\left(\frac{3 \pi}{7} \right)} + 7 \cdot 2^{\frac{2}{7}} i \sin{\left(\frac{3 \pi}{7} \right)}$ (mult: 1), $7 \cdot 2^{\frac{2}{7}} \cos{\left(\frac{2 \pi}{7} \right)} - 7 \cdot 2^{\frac{2}{7}} i \sin{\left(\frac{2 \pi}{7} \right)}$ (mult: 1), $7 \cdot 2^{\frac{2}{7}} \cos{\left(\frac{2 \pi}{7} \right)} + 7 \cdot 2^{\frac{2}{7}} i \sin{\left(\frac{2 \pi}{7} \right)}$ (mult: 1), $0$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 0 & 0 & 14 & 0\\7 & 0 & 0 & 0 & 0 & 0 & 0 & 14\\0 & 7 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 7 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 7 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 7 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 7 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 7 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  &  & 1 &  &  &  &  &  &  &  \\
         &  &  &  &  &  & 0 &  & 0 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 0 &  & 0 &  &  &  &  &  &  \\
         &  &  &  &  &  &  & 1 &  &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #48: P8 / O(2)+O(2)+O(2)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $12$ (mult: 1), $-6 - 6 \sqrt{3} i$ (mult: 1), $-6 + 6 \sqrt{3} i$ (mult: 1), $0$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 24 & 0 & 0 & 192\\3 & 0 & 0 & 72 & 0 & 0\\0 & 3 & 0 & 0 & 72 & 0\\0 & 0 & 3 & 0 & 0 & 24\\0 & 0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  & 1 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
        0 &  & 0 &  & 27 &  & 27 &  & 0 &  & 0 \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 1 &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #49: P8 / O(2)+O(2)+O(3)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $- 24 \sqrt{3}$ (mult: 1), $24 \sqrt{3}$ (mult: 1), $0$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 48 & 0 & 10944 & 0 & 331776\\2 & 0 & 216 & 0 & 29088 & 0\\0 & 2 & 0 & 336 & 0 & 10944\\0 & 0 & 2 & 0 & 216 & 0\\0 & 0 & 0 & 2 & 0 & 48\\0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  & 1 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
        0 &  & 11 &  & 316 &  & 316 &  & 11 &  & 0 \\
         & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 1 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 1 &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #51: P8 / O(2)+O(3)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $6$
    - **Fano Index:** $4$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $- 4 \sqrt{2} \cdot 3^{\frac{3}{4}}$ (mult: 1), $4 \sqrt{2} \cdot 3^{\frac{3}{4}}$ (mult: 1), $- 4 \sqrt{2} \cdot 3^{\frac{3}{4}} i$ (mult: 1), $4 \sqrt{2} \cdot 3^{\frac{3}{4}} i$ (mult: 1), $0$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 48 & 0 & 0 & 0\\4 & 0 & 0 & 0 & 168 & 0 & 0\\0 & 4 & 0 & 0 & 0 & 168 & 0\\0 & 0 & 4 & 0 & 0 & 0 & 48\\0 & 0 & 0 & 4 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 0 &  & 45 &  & 252 &  & 45 &  & 0 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #53: P8 / O(2)+O(4)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $6$
    - **Fano Index:** $3$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $24 \sqrt[3]{2}$ (mult: 1), $- 12 \sqrt[3]{2} - 12 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $- 12 \sqrt[3]{2} + 12 \sqrt[3]{2} \sqrt{3} i$ (mult: 1), $0$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 144 & 0 & 0 & 40320 & 0\\3 & 0 & 0 & 768 & 0 & 0 & 40320\\0 & 3 & 0 & 0 & 1248 & 0 & 0\\0 & 0 & 3 & 0 & 0 & 768 & 0\\0 & 0 & 0 & 3 & 0 & 0 & 144\\0 & 0 & 0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 9 &  & 882 &  & 3140 &  & 882 &  & 9 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #54: P8 / O(2)+O(5)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $6$
    - **Fano Index:** $2$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $- 100 \sqrt{5}$ (mult: 1), $100 \sqrt{5}$ (mult: 1), $0$ (mult: 5)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 480 & 0 & 3273600 & 0 & 7293600000 & 0\\2 & 0 & 3560 & 0 & 19926400 & 0 & 7293600000\\0 & 2 & 0 & 8460 & 0 & 19926400 & 0\\0 & 0 & 2 & 0 & 8460 & 0 & 3273600\\0 & 0 & 0 & 2 & 0 & 3560 & 0\\0 & 0 & 0 & 0 & 2 & 0 & 480\\0 & 0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 157 &  & 6938 &  & 20764 &  & 6938 &  & 157 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #24: P6 / O(2)+O(4)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $4$
    - **Fano Index:** $1$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $976$ (mult: 1), $-48$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 25632 & 16464384 & 6088232448 & 607435407360\\1 & 208 & 159328 & 60008448 & 6088232448\\0 & 1 & 368 & 159328 & 16464384\\0 & 0 & 1 & 208 & 25632\\0 & 0 & 0 & 1 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  & 1 &  &  &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 77 &  & 394 &  & 77 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 1 &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #26: P6 / O(3)+O(3)"
    - **Ambient Space:** `$A6$`
    - **Dimension:** $4$
    - **Fano Index:** $1$
    - **Basis Rank:** $7$
    - **Eigenvalues:** $693$ (mult: 1), $-36$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 13608 & 6244776 & 1637648928 & 122790427200\\1 & 144 & 80352 & 21464352 & 1637648928\\0 & 1 & 261 & 80352 & 6244776\\0 & 0 & 1 & 144 & 13608\\0 & 0 & 0 & 1 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  & 1 &  &  &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 49 &  & 267 &  & 49 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 1 &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #56: P8 / O(3)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $7$
    - **Fano Index:** $6$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $- 6 \sqrt{3}$ (mult: 1), $6 \sqrt{3}$ (mult: 1), $- 3 \sqrt{3} - 9 i$ (mult: 1), $- 3 \sqrt{3} + 9 i$ (mult: 1), $3 \sqrt{3} - 9 i$ (mult: 1), $3 \sqrt{3} + 9 i$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 0 & 36 & 0 & 0\\6 & 0 & 0 & 0 & 0 & 0 & 90 & 0\\0 & 6 & 0 & 0 & 0 & 0 & 0 & 36\\0 & 0 & 6 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 6 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 6 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 6 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 6 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  &  & 1 &  &  &  &  &  &  &  \\
         &  &  &  &  &  & 0 &  & 0 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 0 &  & 1 &  & 84 &  & 84 &  & 1 &  & 0 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 0 &  & 0 &  &  &  &  &  &  \\
         &  &  &  &  &  &  & 1 &  &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #57: P8 / O(3)+O(3)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $6$
    - **Fano Index:** $3$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $27$ (mult: 1), $- \frac{27}{2} - \frac{27 \sqrt{3} i}{2}$ (mult: 1), $- \frac{27}{2} + \frac{27 \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 108 & 0 & 0 & 21384 & 0\\3 & 0 & 0 & 540 & 0 & 0 & 21384\\0 & 3 & 0 & 0 & 891 & 0 & 0\\0 & 0 & 3 & 0 & 0 & 540 & 0\\0 & 0 & 0 & 3 & 0 & 0 & 108\\0 & 0 & 0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 2 &  & 329 &  & 1303 &  & 329 &  & 2 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #58: P8 / O(3)+O(4)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $6$
    - **Fano Index:** $2$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $- 96 \sqrt{3}$ (mult: 1), $96 \sqrt{3}$ (mult: 1), $0$ (mult: 5)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 288 & 0 & 1081728 & 0 & 1344190464 & 0\\2 & 0 & 1968 & 0 & 6113088 & 0 & 1344190464\\0 & 2 & 0 & 4656 & 0 & 6113088 & 0\\0 & 0 & 2 & 0 & 4656 & 0 & 1081728\\0 & 0 & 0 & 2 & 0 & 1968 & 0\\0 & 0 & 0 & 0 & 2 & 0 & 288\\0 & 0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 54 &  & 2720 &  & 8534 &  & 2720 &  & 54 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 1 &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #60: P8 / O(4)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $7$
    - **Fano Index:** $5$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $10 \cdot 2^{\frac{3}{5}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{3}{5}} \sqrt{5}}{2} - \frac{5 \cdot 2^{\frac{3}{5}}}{2} - 10 \cdot 2^{\frac{3}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{3}{5}} \sqrt{5}}{2} - \frac{5 \cdot 2^{\frac{3}{5}}}{2} + 10 \cdot 2^{\frac{3}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{3}{5}}}{2} + \frac{5 \cdot 2^{\frac{3}{5}} \sqrt{5}}{2} - 10 \cdot 2^{\frac{3}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5 \cdot 2^{\frac{3}{5}}}{2} + \frac{5 \cdot 2^{\frac{3}{5}} \sqrt{5}}{2} + 10 \cdot 2^{\frac{3}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $0$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 120 & 0 & 0 & 0\\5 & 0 & 0 & 0 & 0 & 520 & 0 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 520 & 0\\0 & 0 & 5 & 0 & 0 & 0 & 0 & 120\\0 & 0 & 0 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 5 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 5 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 5 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  &  & 1 &  &  &  &  &  &  &  \\
         &  &  &  &  &  & 0 &  & 0 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 0 &  & 156 &  & 2304 &  & 2304 &  & 156 &  & 0 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 0 &  & 0 &  &  &  &  &  &  \\
         &  &  &  &  &  &  & 1 &  &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #62: P8 / O(5)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $7$
    - **Fano Index:** $4$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $- 20 \sqrt[4]{5}$ (mult: 1), $20 \sqrt[4]{5}$ (mult: 1), $- 20 \sqrt[4]{5} i$ (mult: 1), $20 \sqrt[4]{5} i$ (mult: 1), $0$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 480 & 0 & 0 & 0 & 57600\\4 & 0 & 0 & 0 & 3080 & 0 & 0 & 0\\0 & 4 & 0 & 0 & 0 & 5380 & 0 & 0\\0 & 0 & 4 & 0 & 0 & 0 & 3080 & 0\\0 & 0 & 0 & 4 & 0 & 0 & 0 & 480\\0 & 0 & 0 & 0 & 4 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  &  & 1 &  &  &  &  &  &  &  \\
         &  &  &  &  &  & 0 &  & 0 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 9 &  & 2598 &  & 23607 &  & 23607 &  & 2598 &  & 9 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 0 &  & 0 &  &  &  &  &  &  \\
         &  &  &  &  &  &  & 1 &  &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #63: P8 / O(6)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $7$
    - **Fano Index:** $3$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $108$ (mult: 1), $-54 - 54 \sqrt{3} i$ (mult: 1), $-54 + 54 \sqrt{3} i$ (mult: 1), $0$ (mult: 5)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 2160 & 0 & 0 & 42456960 & 0 & 0\\3 & 0 & 0 & 18792 & 0 & 0 & 132020928 & 0\\0 & 3 & 0 & 0 & 49032 & 0 & 0 & 42456960\\0 & 0 & 3 & 0 & 0 & 49032 & 0 & 0\\0 & 0 & 0 & 3 & 0 & 0 & 18792 & 0\\0 & 0 & 0 & 0 & 3 & 0 & 0 & 2160\\0 & 0 & 0 & 0 & 0 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  &  & 1 &  &  &  &  &  &  &  \\
         &  &  &  &  &  & 0 &  & 0 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 165 &  & 19855 &  & 142740 &  & 142740 &  & 19855 &  & 165 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 0 &  & 0 &  &  &  &  &  &  \\
         &  &  &  &  &  &  & 1 &  &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #66: Gr(2,4)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $4$
    - **Fano Index:** $4$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $- 4 \sqrt{2}$ (mult: 1), $4 \sqrt{2}$ (mult: 1), $- 4 \sqrt{2} i$ (mult: 1), $4 \sqrt{2} i$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 4 & 0\\4 & 0 & 0 & 0 & 0 & 4\\0 & 4 & 0 & 0 & 0 & 0\\0 & 4 & 0 & 0 & 0 & 0\\0 & 0 & 4 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #67: Gr(2,4) / O(1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $3$
    - **Fano Index:** $3$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $3 \cdot 2^{\frac{2}{3}}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} - \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} + \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 3 & 0\\3 & 0 & 0 & 3\\0 & 6 & 0 & 0\\0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #68: Gr(2,4) / O(1)+O(1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Fano Index:** $2$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $0$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 4 & 0\\2 & 0 & 2\\0 & 4 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #69: Gr(2,4) / O(1)+O(1)+O(1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $1$
    - **Fano Index:** $1$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-2$ (mult: 1), $2$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 4\\1 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #70: Gr(2,4) / O(1)+O(2)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Fano Index:** $1$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $12$ (mult: 1), $-4$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 40 & 96\\1 & 4 & 20\\0 & 2 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #71: Gr(2,4) / O(2)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $3$
    - **Fano Index:** $2$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $-8$ (mult: 1), $8$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 8 & 0 & 16\\2 & 0 & 8 & 0\\0 & 4 & 0 & 8\\0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #72: Gr(2,4) / O(3)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $6$
    - **Eigenvalues:** $96$ (mult: 1), $-12$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 792 & 21816 & 396576\\1 & 30 & 1170 & 21816\\0 & 2 & 30 & 792\\0 & 0 & 1 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #73: Gr(3,4)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $3$
    - **Fano Index:** $4$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $- 4 i$ (mult: 1), $4 i$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 4\\4 & 0 & 0 & 0\\0 & 4 & 0 & 0\\0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #74: Gr(3,4) / O(1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Fano Index:** $3$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $3$ (mult: 1), $- \frac{3}{2} - \frac{3 \sqrt{3} i}{2}$ (mult: 1), $- \frac{3}{2} + \frac{3 \sqrt{3} i}{2}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 3\\3 & 0 & 0\\0 & 3 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #75: Gr(3,4) / O(1)+O(1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $1$
    - **Fano Index:** $2$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $-2$ (mult: 1), $2$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 2\\2 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #76: Gr(3,4) / O(1)+O(1)+O(1)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $0$
    - **Fano Index:** $1$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $0$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0\end{matrix}\right]
        $$

    </details>


??? example "Case #77: Gr(3,4) / O(1)+O(2)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $1$
    - **Fano Index:** $1$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $-2$ (mult: 1), $2$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 4\\1 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #78: Gr(3,4) / O(2)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Fano Index:** $2$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $0$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 4 & 0\\2 & 0 & 4\\0 & 2 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #79: Gr(3,4) / O(3)"
    - **Ambient Space:** `$A3$`
    - **Dimension:** $2$
    - **Fano Index:** $1$
    - **Basis Rank:** $4$
    - **Eigenvalues:** $21$ (mult: 1), $-6$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 108 & 756\\1 & 9 & 108\\0 & 1 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #80: Gr(2,5)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $6$
    - **Fano Index:** $5$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $\frac{5}{2} - \frac{5 \sqrt{5}}{2}$ (mult: 1), $\frac{5}{2} + \frac{5 \sqrt{5}}{2}$ (mult: 1), $\frac{5}{2} - 5 \sqrt{- \frac{5}{4} - \frac{\sqrt{5}}{2}}$ (mult: 1), $\frac{5}{2} - 5 \sqrt{- \frac{5}{4} + \frac{\sqrt{5}}{2}}$ (mult: 1), $\frac{5}{2} + 5 \sqrt{- \frac{5}{4} - \frac{\sqrt{5}}{2}}$ (mult: 1), $\frac{5}{2} + 5 \sqrt{- \frac{5}{4} + \frac{\sqrt{5}}{2}}$ (mult: 1), $- \frac{15}{4} + \frac{5 \sqrt{5}}{4} - 5 \sqrt{- \frac{5}{8} + \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{15}{4} - \frac{5 \sqrt{5}}{4} - 5 \sqrt{- \frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{15}{4} - \frac{5 \sqrt{5}}{4} + 5 \sqrt{- \frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{15}{4} + \frac{5 \sqrt{5}}{4} + 5 \sqrt{- \frac{5}{8} + \frac{\sqrt{5}}{8}}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 0 & 0 & 5 & 0 & 0 & 0\\5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5\\0 & 0 & 5 & 5 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 5 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 5 & 5 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #81: Gr(2,5) / O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Fano Index:** $4$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} + 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} - 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} - 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} + 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \cdot 2^{\frac{3}{4}} i \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $2 \cdot 2^{\frac{3}{4}} i \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \cdot 2^{\frac{3}{4}} \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $2 \cdot 2^{\frac{3}{4}} \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 4 & 4 & 0 & 0\\4 & 0 & 0 & 0 & 0 & 0 & 4 & 0\\0 & 4 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 4 & 0 & 0 & 0 & 0 & 0 & 4\\0 & 0 & 4 & 4 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 4 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 8 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #82: Gr(2,5) / O(1)+O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $3$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $\frac{3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $\frac{3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- \frac{3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $- \frac{3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 3 & 6 & 0 & 0\\3 & 0 & 0 & 0 & 6 & 0\\0 & 3 & 0 & 0 & 0 & 0\\0 & 3 & 0 & 0 & 0 & 3\\0 & 0 & 3 & \frac{9}{2} & 0 & 0\\0 & 0 & 0 & 0 & 6 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #83: Gr(2,5) / O(1)+O(1)+O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $2$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 2 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $2 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- 2 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $2 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 6 & 0 & 8\\2 & 0 & 4 & 0\\0 & 5 & 0 & 6\\0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #84: Gr(2,5) / O(1)+O(1)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $-6$ (mult: 2), $16 - 10 \sqrt{5}$ (mult: 1), $16 + 10 \sqrt{5}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 156 & 1440 & 13248\\1 & 10 & 152 & 1440\\0 & \frac{5}{2} & 10 & 156\\0 & 0 & 1 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #85: Gr(2,5) / O(1)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 4 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $4 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- 4 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $4 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 12 & 0 & 0 & 96 & 0\\2 & 0 & 12 & 20 & 0 & 48\\0 & 2 & 0 & 0 & 8 & 0\\0 & 2 & 0 & 0 & 16 & 0\\0 & 0 & 2 & 3 & 0 & 6\\0 & 0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #64: P8 / O(7)"
    - **Ambient Space:** `$A8$`
    - **Dimension:** $7$
    - **Fano Index:** $2$
    - **Basis Rank:** $9$
    - **Eigenvalues:** $- 686 \sqrt{7}$ (mult: 1), $686 \sqrt{7}$ (mult: 1), $0$ (mult: 6)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 10080 & 0 & 4112519040 & 0 & 1068310404604800 & 0 & 10225965588972134400\\2 & 0 & 112392 & 0 & 49399013664 & 0 & 3840731271980064 & 0\\0 & 2 & 0 & 400904 & 0 & 107503371248 & 0 & 1068310404604800\\0 & 0 & 2 & 0 & 600334 & 0 & 49399013664 & 0\\0 & 0 & 0 & 2 & 0 & 400904 & 0 & 4112519040\\0 & 0 & 0 & 0 & 2 & 0 & 112392 & 0\\0 & 0 & 0 & 0 & 0 & 2 & 0 & 10080\\0 & 0 & 0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  &  &  &  & 1 &  &  &  &  &  &  &  \\
         &  &  &  &  &  & 0 &  & 0 &  &  &  &  &  &  \\
         &  &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  &  \\
         &  &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  &  \\
         &  &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 1287 &  & 98979 &  & 619569 &  & 619569 &  & 98979 &  & 1287 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  & 1 &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 0 &  & 0 &  & 0 &  & 0 &  &  &  &  \\
         &  &  &  &  & 0 &  & 1 &  & 0 &  &  &  &  &  \\
         &  &  &  &  &  & 0 &  & 0 &  &  &  &  &  &  \\
         &  &  &  &  &  &  & 1 &  &  &  &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #87: Gr(2,5) / O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 3 \sqrt[3]{-22 + 10 \sqrt{5}}$ (mult: 1), $\frac{3 \sqrt[3]{-22 + 10 \sqrt{5}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{-22 + 10 \sqrt{5}}}{2}$ (mult: 1), $\frac{3 \sqrt[3]{-22 + 10 \sqrt{5}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{-22 + 10 \sqrt{5}}}{2}$ (mult: 1), $3 \sqrt[3]{22 + 10 \sqrt{5}}$ (mult: 1), $- \frac{3 \sqrt[3]{22 + 10 \sqrt{5}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{22 + 10 \sqrt{5}}}{2}$ (mult: 1), $- \frac{3 \sqrt[3]{22 + 10 \sqrt{5}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{22 + 10 \sqrt{5}}}{2}$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 6 & 12 & 0 & 0 & 0 & 24\\3 & 0 & 0 & 0 & 18 & 12 & 0 & 0\\0 & 3 & 0 & 0 & 0 & 0 & 6 & 0\\0 & 3 & 0 & 0 & 0 & 0 & 12 & 0\\0 & 0 & 3 & 3 & 0 & 0 & 0 & 6\\0 & 0 & 0 & 3 & 0 & 0 & 0 & 6\\0 & 0 & 0 & 0 & 6 & 3 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #86: Gr(2,5) / O(1)+O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $1$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $-18$ (mult: 4), $\frac{261}{2} - \frac{135 \sqrt{5}}{2}$ (mult: 1), $\frac{261}{2} + \frac{135 \sqrt{5}}{2}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 2772 & 200988 & 310284 & 23784192 & 430673760\\1 & 57 & 5328 & 8244 & 644490 & 11892096\\0 & 1 & 18 & 57 & 4824 & 91692\\0 & 1 & 48 & 57 & 5832 & 109296\\0 & 0 & 1 & \frac{3}{2} & 57 & 1386\\0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #89: Gr(2,5) / O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 6 i \sqrt{- \frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $6 i \sqrt{- \frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $- 6 \sqrt{\frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $6 \sqrt{\frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $0$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 36 & 0 & 0 & 2232 & 1224 & 0 & 26568\\2 & 0 & 54 & 96 & 0 & 0 & 2988 & 0\\0 & 2 & 0 & 0 & 72 & 42 & 0 & 1008\\0 & 2 & 0 & 0 & 96 & 54 & 0 & 1224\\0 & 0 & 2 & 2 & 0 & 0 & 54 & 0\\0 & 0 & 0 & 2 & 0 & 0 & 42 & 0\\0 & 0 & 0 & 0 & 4 & 2 & 0 & 36\\0 & 0 & 0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #88: Gr(2,5) / O(2)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $1$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $-12$ (mult: 4), $76 - 40 \sqrt{5}$ (mult: 1), $76 + 40 \sqrt{5}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 1080 & 46080 & 71424 & 3301632 & 39398400\\1 & 32 & 1848 & 2872 & 135552 & 1650816\\0 & 1 & 8 & 32 & 1648 & 20736\\0 & 1 & 28 & 32 & 2048 & 25344\\0 & 0 & 1 & \frac{3}{2} & 32 & 540\\0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #91: Gr(3,5)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $6$
    - **Fano Index:** $5$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $\frac{5}{2} - \frac{5 \sqrt{5}}{2}$ (mult: 1), $\frac{5}{2} + \frac{5 \sqrt{5}}{2}$ (mult: 1), $\frac{5}{2} - 5 \sqrt{- \frac{5}{4} - \frac{\sqrt{5}}{2}}$ (mult: 1), $\frac{5}{2} - 5 \sqrt{- \frac{5}{4} + \frac{\sqrt{5}}{2}}$ (mult: 1), $\frac{5}{2} + 5 \sqrt{- \frac{5}{4} - \frac{\sqrt{5}}{2}}$ (mult: 1), $\frac{5}{2} + 5 \sqrt{- \frac{5}{4} + \frac{\sqrt{5}}{2}}$ (mult: 1), $- \frac{15}{4} + \frac{5 \sqrt{5}}{4} - 5 \sqrt{- \frac{5}{8} + \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{15}{4} - \frac{5 \sqrt{5}}{4} - 5 \sqrt{- \frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{15}{4} - \frac{5 \sqrt{5}}{4} + 5 \sqrt{- \frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{15}{4} + \frac{5 \sqrt{5}}{4} + 5 \sqrt{- \frac{5}{8} + \frac{\sqrt{5}}{8}}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 0 & 0 & 5 & 0 & 0 & 0\\5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5\\0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 5 & 5 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 5 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 5 & 5 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #92: Gr(3,5) / O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Fano Index:** $4$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} + 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} - 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} - 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $2 \sqrt[4]{2} \sqrt[4]{-11 + 5 \sqrt{5}} + 2 \sqrt[4]{2} i \sqrt[4]{-11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \cdot 2^{\frac{3}{4}} i \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $2 \cdot 2^{\frac{3}{4}} i \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $- 2 \cdot 2^{\frac{3}{4}} \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1), $2 \cdot 2^{\frac{3}{4}} \sqrt[4]{11 + 5 \sqrt{5}}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 4 & 4 & 0 & 0\\4 & 0 & 0 & 0 & 0 & 0 & 4 & 0\\0 & 4 & 0 & 0 & 0 & 0 & 0 & 4\\0 & 4 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 4 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 4 & 4 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 4 & 8 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #93: Gr(3,5) / O(1)+O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $3$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $\frac{3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $\frac{3 \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- \frac{3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1), $- \frac{3 \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}}{2}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 6 & 3 & 0 & 0\\3 & 0 & 0 & 0 & 3 & 0\\0 & 3 & 0 & 0 & 0 & 3\\0 & 3 & 0 & 0 & 0 & 0\\0 & 0 & 9 & 6 & 0 & 0\\0 & 0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #94: Gr(3,5) / O(1)+O(1)+O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $2$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 2 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $2 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- 2 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $2 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 6 & 0 & 4\\2 & 0 & 6 & 0\\0 & \frac{10}{3} & 0 & 2\\0 & 0 & 6 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #95: Gr(3,5) / O(1)+O(1)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $-6$ (mult: 2), $16 - 10 \sqrt{5}$ (mult: 1), $16 + 10 \sqrt{5}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 156 & 2160 & 6624\\1 & 10 & 228 & 720\\0 & \frac{5}{3} & 10 & 52\\0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #96: Gr(3,5) / O(1)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $2$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 4 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $4 i \sqrt{- \frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $- 4 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $4 \sqrt{\frac{11}{2} + \frac{5 \sqrt{5}}{2}}$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 12 & 0 & 0 & 48 & 0\\2 & 0 & 20 & 12 & 0 & 48\\0 & 2 & 0 & 0 & 8 & 0\\0 & 2 & 0 & 0 & 4 & 0\\0 & 0 & 6 & 4 & 0 & 12\\0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #34: P7 / O(2)+O(2)+O(3)"
    - **Ambient Space:** `$A7$`
    - **Dimension:** $4$
    - **Fano Index:** $1$
    - **Basis Rank:** $8$
    - **Eigenvalues:** $408$ (mult: 1), $-24$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 5328 & 1427328 & 230750208 & 11257159680\\1 & 84 & 28152 & 4643136 & 230750208\\0 & 1 & 144 & 28152 & 1427328\\0 & 0 & 1 & 84 & 5328\\0 & 0 & 0 & 1 & 0\end{matrix}\right]
        $$

    </details>
    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>

        $$
        \begin{matrix}
         &  &  &  & 1 &  &  &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
        0 &  & 42 &  & 236 &  & 42 &  & 0 \\
         & 0 &  & 0 &  & 0 &  & 0 &  \\
         &  & 0 &  & 1 &  & 0 &  &  \\
         &  &  & 0 &  & 0 &  &  &  \\
         &  &  &  & 1 &  &  &  &  \\
        \end{matrix}
        $$

    </details>


??? example "Case #98: Gr(3,5) / O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 3 \sqrt[3]{-22 + 10 \sqrt{5}}$ (mult: 1), $\frac{3 \sqrt[3]{-22 + 10 \sqrt{5}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{-22 + 10 \sqrt{5}}}{2}$ (mult: 1), $\frac{3 \sqrt[3]{-22 + 10 \sqrt{5}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{-22 + 10 \sqrt{5}}}{2}$ (mult: 1), $3 \sqrt[3]{22 + 10 \sqrt{5}}$ (mult: 1), $- \frac{3 \sqrt[3]{22 + 10 \sqrt{5}}}{2} - \frac{3 \sqrt{3} i \sqrt[3]{22 + 10 \sqrt{5}}}{2}$ (mult: 1), $- \frac{3 \sqrt[3]{22 + 10 \sqrt{5}}}{2} + \frac{3 \sqrt{3} i \sqrt[3]{22 + 10 \sqrt{5}}}{2}$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 12 & 6 & 0 & 0 & 0 & 24\\3 & 0 & 0 & 0 & 12 & 18 & 0 & 0\\0 & 3 & 0 & 0 & 0 & 0 & 12 & 0\\0 & 3 & 0 & 0 & 0 & 0 & 6 & 0\\0 & 0 & 3 & 0 & 0 & 0 & 0 & 6\\0 & 0 & 3 & 3 & 0 & 0 & 0 & 6\\0 & 0 & 0 & 0 & 3 & 6 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #97: Gr(3,5) / O(1)+O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $1$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $-18$ (mult: 4), $\frac{261}{2} - \frac{135 \sqrt{5}}{2}$ (mult: 1), $\frac{261}{2} + \frac{135 \sqrt{5}}{2}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 2772 & 310284 & 200988 & 11892096 & 430673760\\1 & 57 & 8244 & 5328 & 322245 & 11892096\\0 & 1 & 57 & 48 & 2916 & 109296\\0 & 1 & 57 & 18 & 2412 & 91692\\0 & 0 & 3 & 2 & 57 & 2772\\0 & 0 & 0 & 0 & 1 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #100: Gr(3,5) / O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $- 6 i \sqrt{- \frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $6 i \sqrt{- \frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $- 6 \sqrt{\frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $6 \sqrt{\frac{33}{2} + \frac{15 \sqrt{5}}{2}}$ (mult: 1), $0$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 36 & 0 & 0 & 1224 & 2232 & 0 & 26568\\2 & 0 & 96 & 54 & 0 & 0 & 2988 & 0\\0 & 2 & 0 & 0 & 54 & 96 & 0 & 1224\\0 & 2 & 0 & 0 & 42 & 72 & 0 & 1008\\0 & 0 & 2 & 0 & 0 & 0 & 42 & 0\\0 & 0 & 2 & 2 & 0 & 0 & 54 & 0\\0 & 0 & 0 & 0 & 2 & 4 & 0 & 36\\0 & 0 & 0 & 0 & 0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #99: Gr(3,5) / O(2)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $1$
    - **Basis Rank:** $10$
    - **Eigenvalues:** $-12$ (mult: 4), $76 - 40 \sqrt{5}$ (mult: 1), $76 + 40 \sqrt{5}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 1080 & 71424 & 46080 & 1650816 & 39398400\\1 & 32 & 2872 & 1848 & 67776 & 1650816\\0 & 1 & 32 & 28 & 1024 & 25344\\0 & 1 & 32 & 8 & 824 & 20736\\0 & 0 & 3 & 2 & 32 & 1080\\0 & 0 & 0 & 0 & 1 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #102: Gr(4,5)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $4$
    - **Fano Index:** $5$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $5$ (mult: 1), $- \frac{5 \sqrt{5}}{4} - \frac{5}{4} - 5 i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \sqrt{5}}{4} - \frac{5}{4} + 5 i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5}{4} + \frac{5 \sqrt{5}}{4} - 5 i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5}{4} + \frac{5 \sqrt{5}}{4} + 5 i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 5\\5 & 0 & 0 & 0 & 0\\0 & 5 & 0 & 0 & 0\\0 & 0 & 5 & 0 & 0\\0 & 0 & 0 & 5 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #103: Gr(4,5) / O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $4$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $- 4 i$ (mult: 1), $4 i$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 4\\4 & 0 & 0 & 0\\0 & 4 & 0 & 0\\0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #104: Gr(4,5) / O(1)+O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $2$
    - **Fano Index:** $3$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $3$ (mult: 1), $- \frac{3}{2} - \frac{3 \sqrt{3} i}{2}$ (mult: 1), $- \frac{3}{2} + \frac{3 \sqrt{3} i}{2}$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 3\\3 & 0 & 0\\0 & 3 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #105: Gr(4,5) / O(1)+O(1)+O(1)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $1$
    - **Fano Index:** $2$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $-2$ (mult: 1), $2$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 2\\2 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #106: Gr(4,5) / O(1)+O(1)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $1$
    - **Fano Index:** $1$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $-2$ (mult: 1), $2$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 4\\1 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #107: Gr(4,5) / O(1)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $2$
    - **Fano Index:** $2$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $-4$ (mult: 1), $4$ (mult: 1), $0$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 4 & 0\\2 & 0 & 4\\0 & 2 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #108: Gr(4,5) / O(1)+O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $2$
    - **Fano Index:** $1$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $21$ (mult: 1), $-6$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 108 & 756\\1 & 9 & 108\\0 & 1 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #109: Gr(4,5) / O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $3$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $3 \cdot 2^{\frac{2}{3}}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} - \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $- \frac{3 \cdot 2^{\frac{2}{3}}}{2} + \frac{3 \cdot 2^{\frac{2}{3}} \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 1)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 6 & 0\\3 & 0 & 0 & 6\\0 & 3 & 0 & 0\\0 & 0 & 3 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #110: Gr(4,5) / O(2)+O(2)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $2$
    - **Fano Index:** $1$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $12$ (mult: 1), $-4$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 40 & 192\\1 & 4 & 40\\0 & 1 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #111: Gr(4,5) / O(3)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $2$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $- 6 \sqrt{3}$ (mult: 1), $6 \sqrt{3}$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 12 & 0 & 72\\2 & 0 & 30 & 0\\0 & 2 & 0 & 12\\0 & 0 & 2 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #112: Gr(4,5) / O(4)"
    - **Ambient Space:** `$A4$`
    - **Dimension:** $3$
    - **Fano Index:** $1$
    - **Basis Rank:** $5$
    - **Eigenvalues:** $232$ (mult: 1), $-24$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 3888 & 504576 & 18323712\\1 & 80 & 13600 & 504576\\0 & 1 & 80 & 3888\\0 & 0 & 1 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #113: Gr(2,6)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $8$
    - **Fano Index:** $6$
    - **Basis Rank:** $15$
    - **Eigenvalues:** $- 6 \sqrt{3}$ (mult: 1), $6 \sqrt{3}$ (mult: 1), $- 6 i$ (mult: 1), $6 i$ (mult: 1), $- 3 \sqrt{3} - 3 i$ (mult: 1), $- 3 \sqrt{3} + 3 i$ (mult: 1), $3 \sqrt{3} - 3 i$ (mult: 1), $3 \sqrt{3} + 3 i$ (mult: 1), $- 6 \sqrt{- \frac{3}{2} - \frac{3 \sqrt{3} i}{2}}$ (mult: 1), $- 6 \sqrt{- \frac{3}{2} + \frac{3 \sqrt{3} i}{2}}$ (mult: 1), $6 \sqrt{- \frac{3}{2} - \frac{3 \sqrt{3} i}{2}}$ (mult: 1), $6 \sqrt{- \frac{3}{2} + \frac{3 \sqrt{3} i}{2}}$ (mult: 1), $0$ (mult: 3)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{array}{ccccccccccccccc}0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 0 & 0 & 0 & 0 & 0\\6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 0 & 0 & 0\\0 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 0\\0 & 0 & 6 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6\\0 & 0 & 0 & 0 & 6 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 6 & 0 & 6 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 6 & 6 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 6 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 6 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 6 & 0\end{array}\right]
        $$

    </details>


??? example "Case #114: Gr(2,6) / O(1)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $7$
    - **Fano Index:** $5$
    - **Basis Rank:** $15$
    - **Eigenvalues:** $-5$ (mult: 1), $- \frac{5 \sqrt{5}}{4} + \frac{5}{4} - 5 i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5 \sqrt{5}}{4} + \frac{5}{4} + 5 i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $\frac{5}{4} + \frac{5 \sqrt{5}}{4} - 5 i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $\frac{5}{4} + \frac{5 \sqrt{5}}{4} + 5 i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $5 \cdot 3^{\frac{3}{5}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} - \frac{5 \cdot 3^{\frac{3}{5}}}{4} - 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} - \frac{5 \cdot 3^{\frac{3}{5}}}{4} + 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{5}{8} - \frac{\sqrt{5}}{8}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}}}{4} + \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} - 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $- \frac{5 \cdot 3^{\frac{3}{5}}}{4} + \frac{5 \cdot 3^{\frac{3}{5}} \sqrt{5}}{4} + 5 \cdot 3^{\frac{3}{5}} i \sqrt{\frac{\sqrt{5}}{8} + \frac{5}{8}}$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{array}{cccccccccccc}0 & 0 & 0 & 0 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & 0\\5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 5 & 0 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 0\\0 & 0 & 5 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5\\0 & 0 & 0 & 0 & 5 & 10 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 5 & -5 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 5 & 5 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 10 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 5 & 0\end{array}\right]
        $$

    </details>


??? example "Case #115: Gr(2,6) / O(1)+O(1)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $6$
    - **Fano Index:** $4$
    - **Basis Rank:** $15$
    - **Eigenvalues:** $- 4 \cdot 3^{\frac{3}{4}}$ (mult: 1), $4 \cdot 3^{\frac{3}{4}}$ (mult: 1), $- 4 \cdot 3^{\frac{3}{4}} i$ (mult: 1), $4 \cdot 3^{\frac{3}{4}} i$ (mult: 1), $- 2 \sqrt{2} - 2 \sqrt{2} i$ (mult: 1), $- 2 \sqrt{2} + 2 \sqrt{2} i$ (mult: 1), $2 \sqrt{2} - 2 \sqrt{2} i$ (mult: 1), $2 \sqrt{2} + 2 \sqrt{2} i$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 0 & 0 & 4 & 8 & 0 & 0 & 0 & 0\\4 & 0 & 0 & 0 & 0 & 0 & 8 & 4 & 0 & 0\\0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 4 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0\\0 & 0 & 4 & 4 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 4 & 0 & 0 & 0 & 0 & 0 & 4\\0 & 0 & 0 & 0 & 4 & 8 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 4 & -4 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 12 & 8 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 4 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #116: Gr(2,6) / O(1)+O(1)+O(1)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $5$
    - **Fano Index:** $3$
    - **Basis Rank:** $15$
    - **Eigenvalues:** $9$ (mult: 1), $-3$ (mult: 1), $\frac{3}{2} - \frac{3 \sqrt{3} i}{2}$ (mult: 1), $\frac{3}{2} + \frac{3 \sqrt{3} i}{2}$ (mult: 1), $- \frac{9}{2} - \frac{9 \sqrt{3} i}{2}$ (mult: 1), $- \frac{9}{2} + \frac{9 \sqrt{3} i}{2}$ (mult: 1), $0$ (mult: 2)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 0 & 3 & 9 & 0 & 0 & 0 & 6\\3 & 0 & 0 & 0 & 9 & 9 & 0 & 0\\0 & 3 & 0 & 0 & 0 & 0 & 0 & 0\\0 & 3 & 0 & 0 & 0 & 0 & 9 & 0\\0 & 0 & 3 & 3 & 0 & 0 & 0 & 0\\0 & 0 & 0 & 3 & 0 & 0 & 0 & 3\\0 & 0 & 0 & 0 & 5 & 4 & 0 & 0\\0 & 0 & 0 & 0 & 0 & 0 & 9 & 0\end{matrix}\right]
        $$

    </details>


??? example "Case #117: Gr(2,6) / O(1)+O(1)+O(2)"
    - **Ambient Space:** `$A5$`
    - **Dimension:** $5$
    - **Fano Index:** $2$
    - **Basis Rank:** $15$
    - **Eigenvalues:** $- 12 \sqrt{3}$ (mult: 1), $12 \sqrt{3}$ (mult: 1), $- 4 i$ (mult: 1), $4 i$ (mult: 1), $0$ (mult: 4)
    <details><summary>Quantum Matrix ($y=1$)</summary>
        $$
        \left[\begin{matrix}0 & 16 & 0 & 0 & 336 & 288 & 0 & 768\\2 & 0 & 16 & 36 & 0 & 0 & 480 & 0\\0 & 2 & 0 & 0 & 12 & 12 & 0 & 48\\0 & 2 & 0 & 0 & 32 & 28 & 0 & 80\\0 & 0 & 2 & 2 & 0 & 0 & 12 & 0\\0 & 0 & 0 & 2 & 0 & 0 & 24 & 0\\0 & 0 & 0 & 0 & \frac{10}{3} & \frac{8}{3} & 0 & \frac{16}{3}\\0 & 0 & 0 & 0 & 0 & 0 & 6 & 0\end{matrix}\right]
        $$

    </details>


</div>

***
*Note: This catalog is automatically generated.*
