# The Computed Catalog

This section houses an expanding catalog of explicit geometric examples computed by `gwflags`. Each entry acts as a "flash card" displaying the fundamental invariants.

## Glossary of Terms

<div class="grid cards" markdown>

-   __Fano Index__

    ---
    
    The Fano index $I_X$ is the greatest integer dividing the anticanonical class $-K_X$. It dictates the powers of the Novikov parameters in quantum multiplication. 
    **Computation:** For a complete intersection of multidegrees $d_i$ in a flag variety $F$, the index is $I_F - \sum d_i$.

-   __Dimension__

    ---

    The complex dimension of the resulting geometric space. 
    **Computation:** If the ambient flag variety $F$ has dimension $N$, and we intersect $k$ line bundles (or a rank-$k$ vector bundle), the complete intersection dimension is $N - k$.

-   __Basis Rank__

    ---

    The number of dimensions in the projected flag-ambient cohomology ring $H_{amb}^*(X)$. This equals the size of the square quantum multiplication matrix.

-   __Leading Eigenvalue__

    ---

    The eigenvalue of the small quantum multiplication matrix $c_1(TX)\star$ with the largest absolute value. According to **Conjecture $\mathcal{O}$**, this eigenvalue dictates the dominant asymptotic behavior of the quantum connection.

</div>

## Geometry Catalog

<div class="grid cards" markdown>

-   __Case #1: $\mathbb{P}^4$ with $\mathcal{O}(2)$__

    ---

    - **Ambient Space:** $\mathbb{P}^4$ (Algebra `A4`)
    - **Vector Bundle:** $\mathcal{O}(2)$
    - **Fano Index:** 3
    - **Dimension:** 3
    - **Basis Rank:** 4
    - **Leading Eigenvalue:** $4.762$

    ??? abstract "Maximize Full Matrix"
        $$
        c_1(TX)\star = \begin{pmatrix}
        0 & 0 & 6 & 0 \\
        3 & 0 & 0 & 6 \\
        0 & 3 & 0 & 0 \\
        0 & 0 & 3 & 0 
        \end{pmatrix}
        $$

-   __Case #2: $\mathbb{P}^4$ with $\mathcal{O}(3)$__

    ---

    - **Ambient Space:** $\mathbb{P}^4$
    - **Vector Bundle:** $\mathcal{O}(3)$
    - **Fano Index:** 2
    - **Dimension:** 3
    - **Basis Rank:** 4
    - **Leading Eigenvalue:** $10.39$
    - **Degenerate Sector:** $m=2$, dim $1.67$

-   __Case #4: $\text{Gr}(2,4)$ with $\mathcal{O}(1)$__

    ---

    - **Ambient Space:** $\text{Gr}(2,4)$
    - **Vector Bundle:** $\mathcal{O}(1)$
    - **Fano Index:** 3
    - **Dimension:** 3
    - **Basis Rank:** 4
    - **Leading Eigenvalue:** $4.762$

</div>

***

*Note: This catalog is currently being populated with all 123 test cases. We are also integrating automated Hodge diamond computations.*
