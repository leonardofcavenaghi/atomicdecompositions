# GWFlags API Reference

This document provides a mathematical and technical overview of the core modules in the `gwflags` codebase, responsible for Gromov-Witten invariant computations via Bott localization.

## 1. Root Systems (`gwflags/rootsystem.py`)

The `rootsystem.py` module computes exact Lie-algebra data needed for the equivariant localization pipeline. It supports semisimple products (e.g., $A_3 \times A_3$).

### `RootSystemData`
A class that encapsulates all Lie-algebra data, computing exactly with rational fractions (`fractions.Fraction`):
- **Simple and Positive Roots**: Generates the orthogonal realizations (Bourbaki numbering) and computes positive roots in both the $\alpha$-basis and orthogonal coordinates.
- **Cartan Matrix & Reflection Matrices**: Computes the Cartan matrix $A_{ij} = 2 (\alpha_i, \alpha_j) / (\alpha_j, \alpha_j)$ and its inverse (used for fundamental weights), as well as reflection matrices for simple roots.
- **Coroots**: Calculates the integer coordinates of coroots $\beta^\vee$.

## 2. Bott Localization Core (`gwflags/localization.py`)

The localization module translates the `V3.nb` Mathematica notebook's localization algorithms (such as Billey's formula and the graph sum) into Python.

### `GWCalculator`
The main class orchestrating the computation of Gromov-Witten invariants for a given Lie algebra $G$ and parabolic subgroup $P$.
- **`rfactor(w)`**: Computes the local Euler factor $R(w) = \prod_{\beta \in R^+ \setminus R^+_P} (-x_{w.\beta})$.
- **`billey(shubert, vertex)`**: Computes the restriction of the equivariant Schubert class $\sigma_{\text{shubert}}$ to a fixed point `vertex` using Billey's formula.
- **`omega_lie(w, root_idx, d)`**: Computes the edge factor $h$-function of an edge leaving vertex $w$ with a specific root and degree.
- **`kappa_gamma(dt)` & `i_vertex(dt, v)`**: Compute the edge/vertex weights of a given decorated tree.
- **`gw_invariant(coh_classes, beta)`**: Computes the final equivariant localization sum by summing over all valid decorated trees.

## 3. Complete Intersection Sector (`gwflags/cintersection.py`)

This module implements localization twisted by the Euler class of a bundle $E$, representing the complete-intersection sector. 

- **`euler_complete_intersection(gw, K, w)`**: Computes the Euler class $e(E)$ at the fixed point $w$.
- **`h_complete_intersection(gw, K, w, root_idx, d)`**: Computes the edge factor $e(H^0(f^*E))$ for an edge leaving $w$. Concave summands (where the splitting degree $b < 0$) are rejected, as the twisted genus-0 theory requires curve-wise global generation.
- **`gw_complete_intersection(gw, coh_classes, beta, K)`**: Executes the twisted localization sum by injecting the appropriate multiplicative twists into `GWCalculator.gw_invariant`.


## 4. Main Interface (`gwflags/__init__.py`)

The main entrypoint for the library is the `FlagVariety` class, which wraps the underlying Lie algebra structures and localization calculators into a unified, high-level interface.

### `FlagVariety`
Represents a specific complex flag variety $G/P$ or a complete intersection inside it.

- **`__init__(self, algebra, roots_that_stay, backend=None)`**: Initializes the geometry. `algebra` is the Cartan type (e.g. `"A4"`), and `roots_that_stay` defines the parabolic subgroup $P$ by specifying which nodes of the Dynkin diagram are kept (1-indexed).
- **`gw(self, coh_classes, beta, K=None)`**: Computes the Gromov-Witten invariant $\langle \sigma_{u_1}, \dots, \sigma_{u_k} \rangle_{0, k, \beta}$ exactly as a rational fraction. If a vector bundle `K` is provided, computes the twisted invariant for the complete intersection.
- **`fano_index_and_betas(self, K=None)`**: Computes the Fano index $I_X$ of the geometry (or complete intersection) and returns a list of curve degrees $\beta$ required for the small quantum multiplication matrix.
- **`small_quantum_multiplication(self, K=None)`**: Computes the full $c_1(TX) \star (-)$ small quantum multiplication matrix projected onto the flag-ambient basis.
