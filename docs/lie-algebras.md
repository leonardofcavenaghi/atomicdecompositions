# Defining Flag Varieties $G/P$ in Our Software

This guide explains how to construct complex flag varieties $G/P$ using our software by specifying a **Cartan Type** (to define the complex semisimple Lie group $G$) and **Keep Nodes** (to define the parabolic subgroup $P$).

## 1. The Lie-Theoretic Setup

Let $G$ be a complex semisimple Lie group. We use its simply connected form
to label line bundles by fundamental weights: $SL(n)$, $Spin(n)$, or
$Sp(2n)$ in the classical cases. The orthogonal descriptions below can also
be written with $SO(n)$, which has the same flag varieties. Its Lie algebra
$\mathfrak{g}$ is classified by a **Cartan Type** and a Dynkin diagram;
simple roots are indexed by Bourbaki node numbers.

A standard parabolic subgroup $P \subset G$ is determined by a subset of the simple roots. In our software, you specify $P$ by providing the **Keep Nodes** (using the `--keep` argument in the CLI or "Keep Nodes" in the GUI). Geometrically, specifying a node $k$ in "Keep Nodes" corresponds to **crossing out** that node $k$ from the Dynkin diagram. This omits the $k$-th simple root from the Levi factor of $P$ (which is equivalent to keeping the $k$-th fundamental weight). Thus, if you specify a single node $k$ in Keep Nodes, node $k$ is crossed out, making $P$ a maximal parabolic subgroup, and $G/P$ is a generalized Grassmannian.

## 2. Dictionary of Standard Geometric Spaces

Below is the explicit mapping from classical geometric spaces to their corresponding (Cartan Type, Keep Nodes) inputs.

### Projective Spaces $\mathbb{P}^n$
The complex projective space $\mathbb{P}^n$ is the space of 1-dimensional subspaces in $\mathbb{C}^{n+1}$.
- **Group:** $G = SL(n+1)$
- **Cartan Type:** `$A_n$`
- **Keep Nodes:** `1` (or `n` for the dual projective space $\mathbb{P}^{n\ast}$)
- **Example:** To construct $\mathbb{P}^4$, use `Algebra = A4, Keep Nodes = 1`.

### Grassmannians $Gr(k, n)$
The Grassmannian $Gr(k, n)$ is the space of $k$-dimensional subspaces in $\mathbb{C}^n$.
- **Group:** $G = SL(n)$
- **Cartan Type:** `$A_{n-1}$`
- **Keep Nodes:** `k`
- **Example:** To construct $Gr(2, 5)$, use `Algebra = A4, Keep Nodes = 2`.

### Lagrangian Grassmannians $LG(n, 2n)$
The Lagrangian Grassmannian $LG(n, 2n)$ parameterizes $n$-dimensional isotropic subspaces of a $2n$-dimensional symplectic vector space.
- **Group:** $G = Sp(2n)$
- **Cartan Type:** `$C_n$`
- **Keep Nodes:** `n`
- **Example:** To construct $LG(3, 6)$, use `Algebra = C3, Keep Nodes = 3`.

### Odd Orthogonal Grassmannians $OG(n, 2n+1)$
This space parameterizes $n$-dimensional isotropic subspaces of a $(2n+1)$-dimensional orthogonal vector space.
- **Group:** $G = SO(2n+1)$
- **Cartan Type:** `$B_n$`
- **Keep Nodes:** `n`
- **Example:** To construct $OG(3, 7)$, use `Algebra = B3, Keep Nodes = 3`.

### Even Orthogonal Grassmannians $OG(n, 2n)$ (Spinor Varieties)
This space has two connected components, each parameterizing one family of $n$-dimensional isotropic subspaces in a $2n$-dimensional orthogonal vector space.
- **Group:** $G = SO(2n)$
- **Cartan Type:** `D_n`
- **Keep Nodes:** `n` (or `n-1` for the other connected component)
- **Example:** To construct $OG(4, 8)$, use `Algebra = D4, Keep Nodes = 4`.

## 3. References

On the maximal orthogonal Grassmannians above, `O(1)` denotes the primitive
spinor generator. The Plücker determinant line bundle is `O(2)`. This matters
when translating section degrees into Bundle K; the two conventions must not
be interchanged.

For rigorous foundations of Lie algebras, root systems, Dynkin diagrams, and the construction of homogeneous spaces, please refer to the following standard texts:

1. Fulton, W., & Harris, J. (1991). *Representation Theory: A First Course*. Springer.
2. Humphreys, J. E. (1972). *Introduction to Lie Algebras and Representation Theory*. Springer.

