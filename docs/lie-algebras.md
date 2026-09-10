# Defining Flag Varieties $G/P$ in Our Software

This guide explains how to construct complex flag varieties $G/P$ using our software by specifying a **Cartan Type** (to define the complex semisimple Lie group $G$) and **Keep Nodes** (to define the parabolic subgroup $P$).

## 1. The Lie-Theoretic Setup

Let $G$ be a simply connected complex semisimple Lie group (e.g., $SL(n)$, $SO(n)$, $Sp(2n)$). Its Lie algebra $\mathfrak{g}$ is classified by a **Cartan Type**, which corresponds to a specific Dynkin diagram. The simple roots of $\mathfrak{g}$ correspond to the nodes of this diagram, typically indexed $1, 2, \dots, n$.

A standard parabolic subgroup $P \subset G$ is determined by a subset of the simple roots. In our software, you specify $P$ by providing the **Keep Nodes** (using the `--keep` argument in the CLI or "Keep Nodes" in the GUI). Geometrically, specifying a node $k$ in "Keep Nodes" corresponds to **crossing out** that node $k$ from the Dynkin diagram. This omits the $k$-th simple root from the Levi factor of $P$ (which is equivalent to keeping the $k$-th fundamental weight). Thus, if you specify a single node $k$ in Keep Nodes, node $k$ is crossed out, making $P$ a maximal parabolic subgroup, and $G/P$ is a generalized Grassmannian.

## 2. Dictionary of Standard Geometric Spaces

Below is the explicit mapping from classical geometric spaces to their corresponding (Cartan Type, Keep Nodes) inputs.

### Projective Spaces $\mathbb{P}^n$
The complex projective space $\mathbb{P}^n$ is the space of 1-dimensional subspaces in $\mathbb{C}^{n+1}$.
- **Group:** $G = SL(n+1)$
- **Cartan Type:** `A_n`
- **Keep Nodes:** `1` (or `n` for the dual projective space $\mathbb{P}^{n\ast}$)
- **Example:** To construct $\mathbb{P}^4$, use `Algebra = A4, Keep Nodes = 1`.

### Grassmannians $Gr(k, n)$
The Grassmannian $Gr(k, n)$ is the space of $k$-dimensional subspaces in $\mathbb{C}^n$.
- **Group:** $G = SL(n)$
- **Cartan Type:** `A_{n-1}`
- **Keep Nodes:** `k`
- **Example:** To construct $Gr(2, 5)$, use `Algebra = A4, Keep Nodes = 2`.

### Lagrangian Grassmannians $LG(n, 2n)$
The Lagrangian Grassmannian $LG(n, 2n)$ parameterizes $n$-dimensional isotropic subspaces of a $2n$-dimensional symplectic vector space.
- **Group:** $G = Sp(2n)$
- **Cartan Type:** `C_n`
- **Keep Nodes:** `n`
- **Example:** To construct $LG(3, 6)$, use `Algebra = C3, Keep Nodes = 3`.

### Odd Orthogonal Grassmannians $OG(n, 2n+1)$
This space parameterizes $n$-dimensional isotropic subspaces of a $(2n+1)$-dimensional orthogonal vector space.
- **Group:** $G = SO(2n+1)$
- **Cartan Type:** `B_n`
- **Keep Nodes:** `n`
- **Example:** To construct $OG(3, 7)$, use `Algebra = B3, Keep Nodes = 3`.

### Even Orthogonal Grassmannians $OG(n, 2n)$ (Spinor Varieties)
This space has two connected components, each parameterizing one family of $n$-dimensional isotropic subspaces in a $2n$-dimensional orthogonal vector space.
- **Group:** $G = SO(2n)$
- **Cartan Type:** `D_n`
- **Keep Nodes:** `n` (or `n-1` for the other connected component)
- **Example:** To construct $OG(4, 8)$, use `Algebra = D4, Keep Nodes = 4`.

## 3. References

For rigorous foundations of Lie algebras, root systems, Dynkin diagrams, and the construction of homogeneous spaces, please refer to the following standard texts:

1. Fulton, W., & Harris, J. (1991). *Representation Theory: A First Course*. Springer. (Specifically, Part III and IV for Lie algebras and their representations).
2. Humphreys, J. E. (1972). *Introduction to Lie Algebras and Representation Theory*. Springer. (Specifically, Chapter III on root systems and Chapter VI on Chevalley groups).

