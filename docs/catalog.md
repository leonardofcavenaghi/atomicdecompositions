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

-   __Case #5: Gr(2,4)  flag itself__

    ---
    
    - **Ambient Space:** `A3`
    - **Dimension:** 4
    - **Fano Index:** 4
    - **Basis Rank:** 6
    - **Eigenvalues:** -5.657 (mult: 1), 5.657 (mult: 1), -4*sqrt(2)*I (mult: 1), 4*sqrt(2)*I (mult: 1), 0.0 (mult: 2)


-   __Case #6: Gr(2,4) / O(2)  del Pezzo__

    ---
    
    - **Ambient Space:** `A3`
    - **Dimension:** 3
    - **Fano Index:** 2
    - **Basis Rank:** 6
    - **Eigenvalues:** -8.0 (mult: 1), 8.0 (mult: 1), 0.0 (mult: 2)


-   __Case #13: Gr(2,5) / O(1)  del Pezzo 5-fold V5__

    ---
    
    - **Ambient Space:** `A4`
    - **Dimension:** 5
    - **Fano Index:** 4
    - **Basis Rank:** 10
    - **Eigenvalues:** -2*2**(1/4)*(-11 + 5*sqrt(5))**(1/4) + 2*2**(1/4)*I*(-11 + 5*sqrt(5))**(1/4) (mult: 1), 2*2**(1/4)*(-11 + 5*sqrt(5))**(1/4) - 2*2**(1/4)*I*(-11 + 5*sqrt(5))**(1/4) (mult: 1), -2*2**(1/4)*(-11 + 5*sqrt(5))**(1/4) - 2*2**(1/4)*I*(-11 + 5*sqrt(5))**(1/4) (mult: 1), 2*2**(1/4)*(-11 + 5*sqrt(5))**(1/4) + 2*2**(1/4)*I*(-11 + 5*sqrt(5))**(1/4) (mult: 1), -2*2**(3/4)*I*(11 + 5*sqrt(5))**(1/4) (mult: 1), 2*2**(3/4)*I*(11 + 5*sqrt(5))**(1/4) (mult: 1), -7.3 (mult: 1), 7.3 (mult: 1)


-   __Case #3: P4 / O(3)  cubic 3-fold__

    ---
    
    - **Ambient Space:** `A4`
    - **Dimension:** 3
    - **Fano Index:** 2
    - **Basis Rank:** 5
    - **Eigenvalues:** -10.392 (mult: 1), 10.392 (mult: 1), 0.0 (mult: 2)
    - **Hodge Diamond ($h^{p,q}$):**
        $$
        \begin{pmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 5 & 0 \\
        0 & 5 & 1 & 0 \\
        0 & 0 & 0 & 1 \\
        \end{pmatrix}
        $$


-   __Case #2: P4 / O(2)  quadric 3-fold__

    ---
    
    - **Ambient Space:** `A4`
    - **Dimension:** 3
    - **Fano Index:** 3
    - **Basis Rank:** 5
    - **Eigenvalues:** 4.762 (mult: 1), -3*2**(2/3)/2 - 3*2**(2/3)*sqrt(3)*I/2 (mult: 1), -3*2**(2/3)/2 + 3*2**(2/3)*sqrt(3)*I/2 (mult: 1), 0.0 (mult: 1)
    - **Hodge Diamond ($h^{p,q}$):**
        $$
        \begin{pmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 1 & 0 \\
        0 & 0 & 0 & 1 \\
        \end{pmatrix}
        $$


</div>

***

*Note: This catalog is automatically generated.*