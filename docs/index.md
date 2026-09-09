# Theory of Atoms

<div align="center">
  <img src="assets/logo.jpg" alt="Theory of Atoms Logo" width="200"/>
</div>

Welcome to the documentation and software repository for **"On the Atomic Decomposition of Complete Intersection in Flag Varieties."** 

This project is an effort of the **Theory of Atoms** mathematical research group, led by **Dr. Ludmil Katzarkov**.

## Authors & Contributors

**Lead Investigator:**
- Dr. Ludmil Katzarkov

**Authors:**
- Leonardo F. Cavenaghi
- Giovane Galindo
- Bogdan Georgiev
- Maxim Kontsevich
- Pedro Antonio Muniz Martins

**Other Contributors:**
- Boris Alexeev

---

## About the Project

This project lies at the intersection of algebraic geometry, representation theory, and enumerative geometry. It provides:

1. **Root-Theoretic Localization Formalism**: For genus-zero Gromov-Witten invariants of flag varieties and smooth zero loci of globally generated homogeneous vector bundles.
2. **Software Implementation**: An algorithmic implementation in Python / SageMath that computes these invariants explicitly over decorated trees, utilizing the roots of the ambient flag variety.
3. **Connections to the Theory of Hodge Atoms**: Bridging explicit combinatorial geometry with theoretical criteria (spectral and numerical) for the rationality of Fano fourfolds (e.g., cubic fourfolds, ordinary Gushel-Mukai fourfolds, and Küchle fourfolds).

## The Software: `gwflags`

The accompanying software, `gwflags`, computes:
- Genus-0 Gromov-Witten invariants by Bott localization via **Billey's formula**.
- Twisted invariants for complete intersections with the Euler class.
- The small quantum multiplication matrix \( c_1(TX)\star \), grading operators, and eigenvalues (to test Conjecture \(\mathcal{O}\) / Gamma-conjecture asymptotics).

## Navigate the Documentation

- [**Installation**](installation.md): Clean, step-by-step instructions for getting Python, SageMath, and `gwflags` running on Windows, macOS, and Linux.
- [**Methodology**](methodology.md): An explanation of how the software implements the localization formalism described in the paper.
- [**Theoretical Basis**](theory.md): A summary of the main theorems (Theorems A, B, C, and D) and how the software relates to the spectral irrationality criteria.

## Download

The code is hosted directly on this repository. You can explore the source code here:
- [GitHub Repository](https://github.com/leonardofcavenaghi/atomicdecompositions)
