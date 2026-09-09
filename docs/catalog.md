# The Computed Catalog

This section houses an expanding catalog of explicit geometric examples computed by `gwflags`. Each entry acts as a "flash card" displaying the fundamental invariants.

## Glossary of Terms

<div class="grid cards" markdown>

-   __[Fano Index](methodology.md#2-fano-index-for-complete-intersections-in-flag-varieties)__

    ---
    
    The Fano index $I_X$ is the greatest integer dividing the anticanonical class $-K_X$. It dictates the powers of the Novikov parameters in quantum multiplication. 
    **Computation:** For a complete intersection of multidegrees $d_i$ in a flag variety $F$, the index is $I_F - \sum d_i$.

-   __[Dimension](methodology.md#4-dimension-and-basis-rank)__

    ---

    The complex dimension of the resulting geometric space. 
    **Computation:** If the ambient flag variety $F$ has dimension $N$, and we intersect $k$ line bundles (or a rank-$k$ vector bundle), the complete intersection dimension is $N - k$.

-   __[Basis Rank](methodology.md#4-dimension-and-basis-rank)__

    ---

    The number of dimensions in the projected flag-ambient cohomology ring $H_{amb}^*(X)$. This equals the size of the square quantum multiplication matrix.

-   __[Eigenvalues & Multiplicities](methodology.md#3-eigenvalues-and-multiplicities)__

    ---

    The eigenvalues of the small quantum multiplication matrix $c_1(TX)\star$ evaluated at $y=1$, along with their algebraic multiplicities. These values govern the spectrum of the quantum connection.

</div>

## Geometry Catalog

<div class="grid cards" markdown>

-   __[Fano Index](methodology.md#2-fano-index-for-complete-intersections-in-flag-varieties)__

    ---
    
    The Fano index $I_X$ is the greatest integer dividing the anticanonical class $-K_X$. It dictates the powers of the Novikov parameters in quantum multiplication. 
    **Computation:** For a complete intersection of multidegrees $d_i$ in a flag variety $F$, the index is $I_F - \sum d_i$.

-   __[Dimension](methodology.md#4-dimension-and-basis-rank)__

    ---

    The complex dimension of the resulting geometric space. 
    **Computation:** If the ambient flag variety $F$ has dimension $N$, and we intersect $k$ line bundles (or a rank-$k$ vector bundle), the complete intersection dimension is $N - k$.

-   __[Basis Rank](methodology.md#4-dimension-and-basis-rank)__

    ---

    The number of dimensions in the projected flag-ambient cohomology ring $H_{amb}^*(X)$. This equals the size of the square quantum multiplication matrix.

-   __[Eigenvalues & Multiplicities](methodology.md#3-eigenvalues-and-multiplicities)__

    ---

    The eigenvalues of the small quantum multiplication matrix $c_1(TX)\star$ evaluated at $y=1$, along with their algebraic multiplicities. These values govern the spectrum of the quantum connection.

-   __Case #10: P5 / O(4)  quartic 4-fold__

    ---
    
    - **Ambient Space:** `A5`
    - **Dimension:** 4
    - **Fano Index:** 2
    - **Basis Rank:** 6
    - **Eigenvalues:** -32.0 (mult: 1), 32.0 (mult: 1), 0.0 (mult: 3)
    - **Hodge Diamond ($h^{p,q}$):**
        $$
        \begin{pmatrix}
        1 & 0 & 0 & 0 & 0 \\
        0 & 1 & 0 & 21 & 0 \\
        0 & 0 & 142 & 0 & 0 \\
        0 & 21 & 0 & 1 & 0 \\
        0 & 0 & 0 & 0 & 1 \\
        \end{pmatrix}
        $$


</div>

***

*Note: This catalog is automatically generated.*