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


-   __Case #8: P5 / O(2)  quadric 4-fold__

    ---
    
    - **Ambient Space:** `A5`
    - **Dimension:** 4
    - **Fano Index:** 4
    - **Basis Rank:** 6
    - **Eigenvalues:** -5.657 (mult: 1), 5.657 (mult: 1), -4*sqrt(2)*I (mult: 1), 4*sqrt(2)*I (mult: 1), 0.0 (mult: 1)
    - **Hodge Diamond ($h^{p,q}$):**
        $$
        \begin{pmatrix}
        1 & 0 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 & 0 \\
        0 & 0 & 2 & 0 & 0 \\
        0 & 0 & 0 & 1 & 0 \\
        0 & 0 & 0 & 0 & 1 \\
        \end{pmatrix}
        $$


-   __Case #16: Gr(2,5) / O(1)+O(1)  del Pezzo 4-fold__

    ---
    
    - **Ambient Space:** `A4`
    - **Dimension:** 4
    - **Fano Index:** 3
    - **Basis Rank:** 10
    - **Eigenvalues:** -1.345 (mult: 1), 3*(-11/2 + 5*sqrt(5)/2)**(1/3)/2 - 3*sqrt(3)*I*(-11/2 + 5*sqrt(5)/2)**(1/3)/2 (mult: 1), 3*(-11/2 + 5*sqrt(5)/2)**(1/3)/2 + 3*sqrt(3)*I*(-11/2 + 5*sqrt(5)/2)**(1/3)/2 (mult: 1), 6.69 (mult: 1), -3*(11/2 + 5*sqrt(5)/2)**(1/3)/2 - 3*sqrt(3)*I*(11/2 + 5*sqrt(5)/2)**(1/3)/2 (mult: 1), -3*(11/2 + 5*sqrt(5)/2)**(1/3)/2 + 3*sqrt(3)*I*(11/2 + 5*sqrt(5)/2)**(1/3)/2 (mult: 1)


-   __Case #14: Gr(2,5) / O(2)  Gushel-Mukai 5-fold__

    ---
    
    - **Ambient Space:** `A4`
    - **Dimension:** 5
    - **Fano Index:** 3
    - **Basis Rank:** 10
    - **Eigenvalues:** -2.135 (mult: 1), 3*(-22 + 10*sqrt(5))**(1/3)/2 - 3*sqrt(3)*I*(-22 + 10*sqrt(5))**(1/3)/2 (mult: 1), 3*(-22 + 10*sqrt(5))**(1/3)/2 + 3*sqrt(3)*I*(-22 + 10*sqrt(5))**(1/3)/2 (mult: 1), 10.62 (mult: 1), -3*(22 + 10*sqrt(5))**(1/3)/2 - 3*sqrt(3)*I*(22 + 10*sqrt(5))**(1/3)/2 (mult: 1), -3*(22 + 10*sqrt(5))**(1/3)/2 + 3*sqrt(3)*I*(22 + 10*sqrt(5))**(1/3)/2 (mult: 1), 0.0 (mult: 2)


-   __Case #11: P5 / O(2)+O(2)__

    ---
    
    - **Ambient Space:** `A5`
    - **Dimension:** 3
    - **Fano Index:** 2
    - **Basis Rank:** 6
    - **Eigenvalues:** -8.0 (mult: 1), 8.0 (mult: 1), 0.0 (mult: 2)
    - **Hodge Diamond ($h^{p,q}$):**
        $$
        \begin{pmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 2 & 0 \\
        0 & 2 & 1 & 0 \\
        0 & 0 & 0 & 1 \\
        \end{pmatrix}
        $$


-   __Case #22: G2/P1  quadric 5-fold__

    ---
    
    - **Ambient Space:** `G2`
    - **Dimension:** 5
    - **Fano Index:** 5
    - **Basis Rank:** 6
    - **Eigenvalues:** 6.598 (mult: 1), -5*2**(2/5)*sqrt(5)/4 - 5*2**(2/5)/4 - 5*2**(2/5)*I*sqrt(5/8 - sqrt(5)/8) (mult: 1), -5*2**(2/5)*sqrt(5)/4 - 5*2**(2/5)/4 + 5*2**(2/5)*I*sqrt(5/8 - sqrt(5)/8) (mult: 1), -5*2**(2/5)/4 + 5*2**(2/5)*sqrt(5)/4 - 5*2**(2/5)*I*sqrt(sqrt(5)/8 + 5/8) (mult: 1), -5*2**(2/5)/4 + 5*2**(2/5)*sqrt(5)/4 + 5*2**(2/5)*I*sqrt(sqrt(5)/8 + 5/8) (mult: 1), 0.0 (mult: 1)


-   __Case #9: P5 / O(3)  cubic 4-fold__

    ---
    
    - **Ambient Space:** `A5`
    - **Dimension:** 4
    - **Fano Index:** 3
    - **Basis Rank:** 6
    - **Eigenvalues:** 9.0 (mult: 1), -9/2 - 9*sqrt(3)*I/2 (mult: 1), -9/2 + 9*sqrt(3)*I/2 (mult: 1), 0.0 (mult: 2)
    - **Hodge Diamond ($h^{p,q}$):**
        $$
        \begin{pmatrix}
        1 & 0 & 0 & 0 & 0 \\
        0 & 1 & 0 & 1 & 0 \\
        0 & 0 & 21 & 0 & 0 \\
        0 & 1 & 0 & 1 & 0 \\
        0 & 0 & 0 & 0 & 1 \\
        \end{pmatrix}
        $$


-   __Case #23: G2/P2__

    ---
    
    - **Ambient Space:** `G2`
    - **Dimension:** 5
    - **Fano Index:** 3
    - **Basis Rank:** 6
    - **Eigenvalues:** -3.35 (mult: 1), 3*(-9 + 6*sqrt(3))**(1/3)/2 - 3*sqrt(3)*I*(-9 + 6*sqrt(3))**(1/3)/2 (mult: 1), 3*(-9 + 6*sqrt(3))**(1/3)/2 + 3*sqrt(3)*I*(-9 + 6*sqrt(3))**(1/3)/2 (mult: 1), 8.06 (mult: 1), -3*(9 + 6*sqrt(3))**(1/3)/2 - 3*sqrt(3)*I*(9 + 6*sqrt(3))**(1/3)/2 (mult: 1), -3*(9 + 6*sqrt(3))**(1/3)/2 + 3*sqrt(3)*I*(9 + 6*sqrt(3))**(1/3)/2 (mult: 1)


-   __Case #24: G2/P2 / O(1)__

    ---
    
    - **Ambient Space:** `G2`
    - **Dimension:** 4
    - **Fano Index:** 2
    - **Basis Rank:** 6
    - **Eigenvalues:** -2*I*sqrt(-9 + 6*sqrt(3)) (mult: 1), 2*I*sqrt(-9 + 6*sqrt(3)) (mult: 1), -8.807 (mult: 1), 8.807 (mult: 1), 0.0 (mult: 1)


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


-   __Case #18: Gr(2,5) / O(1)^3  del Pezzo 3-fold V5__

    ---
    
    - **Ambient Space:** `A4`
    - **Dimension:** 3
    - **Fano Index:** 2
    - **Basis Rank:** 10
    - **Eigenvalues:** -2*I*sqrt(-11/2 + 5*sqrt(5)/2) (mult: 1), 2*I*sqrt(-11/2 + 5*sqrt(5)/2) (mult: 1), -6.66 (mult: 1), 6.66 (mult: 1)


-   __Case #17: Gr(2,5) / O(1)+O(2)  Gushel-Mukai 4-fold__

    ---
    
    - **Ambient Space:** `A4`
    - **Dimension:** 4
    - **Fano Index:** 2
    - **Basis Rank:** 10
    - **Eigenvalues:** -4*I*sqrt(-11/2 + 5*sqrt(5)/2) (mult: 1), 4*I*sqrt(-11/2 + 5*sqrt(5)/2) (mult: 1), -13.321 (mult: 1), 13.321 (mult: 1), 0.0 (mult: 2)


-   __Case #25: Fl(1,3,4) / O(1,1)__

    ---
    
    - **Ambient Space:** `A3`
    - **Dimension:** 4
    - **Fano Index:** 2
    - **Basis Rank:** 12
    - **Eigenvalues:** 8.0 (mult: 1), -8.0 (mult: 1), -4*I (mult: 2), 4*I (mult: 2), 0.0 (mult: 3)


-   __Case #27: OG(3,7) / O(2)__

    ---
    
    - **Ambient Space:** `B3`
    - **Dimension:** 5
    - **Fano Index:** 4
    - **Basis Rank:** 8
    - **Eigenvalues:** -8.0 (mult: 1), 8.0 (mult: 1), -8*I (mult: 1), 8*I (mult: 1), 0.0 (mult: 2)


-   __Case #31: LG(3,6) / O(1)__

    ---
    
    - **Ambient Space:** `C3`
    - **Dimension:** 5
    - **Fano Index:** 3
    - **Basis Rank:** 8
    - **Eigenvalues:** 2.646 (mult: 1), -3*(12 - 8*sqrt(2))**(1/3)/2 - 3*sqrt(3)*I*(12 - 8*sqrt(2))**(1/3)/2 (mult: 1), -3*(12 - 8*sqrt(2))**(1/3)/2 + 3*sqrt(3)*I*(12 - 8*sqrt(2))**(1/3)/2 (mult: 1), 8.57 (mult: 1), -3*(8*sqrt(2) + 12)**(1/3)/2 - 3*sqrt(3)*I*(8*sqrt(2) + 12)**(1/3)/2 (mult: 1), -3*(8*sqrt(2) + 12)**(1/3)/2 + 3*sqrt(3)*I*(8*sqrt(2) + 12)**(1/3)/2 (mult: 1)


-   __Case #28: OG(3,7) / O(3)__

    ---
    
    - **Ambient Space:** `B3`
    - **Dimension:** 5
    - **Fano Index:** 3
    - **Basis Rank:** 8
    - **Eigenvalues:** 14.287 (mult: 1), -9*2**(2/3)/2 - 9*2**(2/3)*sqrt(3)*I/2 (mult: 1), -9*2**(2/3)/2 + 9*2**(2/3)*sqrt(3)*I/2 (mult: 1), 0.0 (mult: 3)


-   __Case #30: OG(3,7) / O(2)+O(2)__

    ---
    
    - **Ambient Space:** `B3`
    - **Dimension:** 4
    - **Fano Index:** 2
    - **Basis Rank:** 8
    - **Eigenvalues:** -16.0 (mult: 1), 16.0 (mult: 1), 0.0 (mult: 3)


-   __Case #32: LG(3,6) / O(1)+O(1)__

    ---
    
    - **Ambient Space:** `C3`
    - **Dimension:** 4
    - **Fano Index:** 2
    - **Basis Rank:** 8
    - **Eigenvalues:** -1.657 (mult: 1), 9.657 (mult: 1), -9.657 (mult: 1), 1.657 (mult: 1), 0.0 (mult: 1)


</div>

***

*Note: This catalog is automatically generated.*