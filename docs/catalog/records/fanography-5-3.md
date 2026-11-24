---
title: "Fanography 5-3"
description: "Exact inputs, ordered basis, quantum multiplication and connection exponents for Fanography 5-3."
keywords: ["Fanography 5-3", "Fano variety 5-3", "dimension 3", "threefold", "Fano threefold", "Fanography", "Smooth projective toric threefold", "Fano", "quantum cohomology", "Gromov-Witten", "Hodge diamond", "quantum multiplication", "connection exponents", "smooth toric ambient", "regularized exponent multiset"]
---

# Fanography 5-3 — smooth projective toric threefold

**Geometric presentation.** Smooth projective toric threefold given directly by its complete smooth fan of Picard rank 5.

**Fanography family:** [5-3](https://fanography.info/5-3/) — $\mathbb{P}^1\times\mathrm{Bl}_3\mathbb{P}^2$. [Fano variety 5-3 reference card](../fanography.md#fano-variety-5-3) · [Geometric identification](../sources.md#geometric-identification).

**Construction:** Smooth projective toric threefold. **Dimension:** 3. **Index:** 1. **h(1,1):** 5.

[Catalogue](../index.md) · [3-folds](../threefolds.md) · [Fanography reference](../fanography.md)

## Spectrum and connection exponents

**Parameter point:** `y1=2, y2=3, y3=5, y4=7, y5=11`.

Here \(A(\mathbf y)\) is first-Chern quantum multiplication on the returned ambient space, and \(G\) is its centered codimension grading. Columns are images of the ordered basis. [Notation and scope](../notation.md).

\(\chi_{A(\mathbf a)}(z)=\prod_i p_i(z)^{m_i}\), with the monic factors below. Each multiplicity and exponent multiset applies separately at every root \(\lambda\) of the indicated factor.

| Factor \(p_i(z)\) | Distinct roots | Multiplicity \(m_i\) per root |
|---|---:|---:|
| \(z^{12} + 360 z^{11} + 39006 z^{10} - 1701000 z^{9} - 786824655 z^{8} - 69699382560 z^{7} - 805798497888 z^{6} + 341073610686720 z^{5} + 33291344951089536 z^{4} + 1592361633032202240 z^{3} + 44019729610800924672 z^{2} + 673042469795634954240 z + 4418873783420338376704\) | 12 | 1 |

**Unit cyclic determinant:** \(\Delta_A(\mathbf a)=-25428463657204426522780874805050876713457815196189717728445540799098770120777844077363200\), in this basis.

**Regularized exponent multisets** \(F_{\mathbf a,\lambda}\), with classes in \(\mathbb Q/\mathbb Z\):

| Spectral condition | \(F_{\mathbf a,\lambda}\) per eigenvalue |
|---|---|
| \(\lambda^{12} + 360 \lambda^{11} + 39006 \lambda^{10} - 1701000 \lambda^{9} - 786824655 \lambda^{8} - 69699382560 \lambda^{7} - 805798497888 \lambda^{6} + 341073610686720 \lambda^{5} + 33291344951089536 \lambda^{4} + 1592361633032202240 \lambda^{3} + 44019729610800924672 \lambda^{2} + 673042469795634954240 \lambda + 4418873783420338376704=0\) | \(\{\!\{0\}\!\}\) |

Repeated entries retain their multiplicity.

[Exact matrix, ordered basis and grading](../../data/toric-threefolds.json) · [Hodge data and atomic invariants](../invariants-threefolds.md#fanography-5-3). The full atomic interpretation uses the Hodge-space and curve hypotheses stated there.

## Geometry and Hodge diamond

**Positivity:** smooth toric Fano ambient (no defining bundle twist).
$\dim X=3$, $\dim Y=3$, codimension $0$, recorded index $1$, $(-K_X)^3=36$, $e(X)=12$.

$$
\begin{array}{ccccccc}&&&1&&&\\&&0&&0&&\\&0&&5&&0&\\0&&0&&0&&0\\&0&&5&&0&\\&&0&&0&&\\&&&1&&&\end{array}
$$

Ambient rank: 12; full even rank: 12; full odd rank: 0 ($h^{1,2}=0$).

$$
\begin{aligned}\int_X c_1^3&=36,&\int_X c_1 c_2&=24,\\\int_X c_3&=12,&\chi(\mathcal O_X)&=1.\end{aligned}
$$

### Exact toric inputs

Cones use zero-based ray indices; K rows are full ray coefficients. Novikov rows specify the divisor basis.

```python
rays = [[-1, 0, 0], [-1, 0, 1], [0, -1, 0], [0, 0, -1], [0, 0, 1], [0, 1, 0], [1, 0, -1], [1, 0, 0]]
cones = [[0, 3, 5], [0, 1, 5], [3, 5, 6], [2, 4, 7], [1, 2, 4], [2, 3, 6], [0, 1, 2], [0, 2, 3], [1, 4, 5], [2, 6, 7], [5, 6, 7], [4, 5, 7]]
K = []
novikov_divisors = [[0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 1]]
eval_y = {'y1': 2, 'y2': 3, 'y3': 5, 'y4': 7, 'y5': 11}
```

**Ordered ambient basis:**

```python
['1', 'x4', 'x3', 'x2', 'x1', 'x0', 'x2*x4', 'x2*x3', 'x1*x2', 'x0*x2', 'x0*x1', 'x0*x1*x2']
```

Curve enumeration: positive; 166 classes including zero.

### Quantum multiplication by $c_1(X)$

Columns are images of basis vectors. All omitted matrix entries are zero; indices are zero based.

```python
basis = ['1', 'x4', 'x3', 'x2', 'x1', 'x0', 'x2*x4', 'x2*x3', 'x1*x2', 'x0*x2', 'x0*x1', 'x0*x1*x2']
```

$$
G=\operatorname{diag}\!\left(- \frac{3}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, - \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{3}{2}\right)
$$

| $i$ | $j$ | $A_{ij}(\mathbf y)$ |
|---|---|---|
| 0 | 1 | $2 y_{3} y_{4} y_{5}$ |
| 0 | 2 | $2 y_{3} y_{4} y_{5}$ |
| 0 | 3 | $2 y_{1}$ |
| 0 | 4 | $2 y_{2} y_{4} y_{5}$ |
| 0 | 5 | $2 y_{2} y_{3} y_{5}$ |
| 0 | 10 | $3 y_{2} y_{3} y_{4} y_{5}^{2} + 3 y_{2} y_{3} y_{4} y_{5}$ |
| 1 | 0 | $1$ |
| 1 | 1 | $- y_{2} - y_{4} y_{5}$ |
| 1 | 2 | $y_{3}$ |
| 1 | 4 | $y_{2}$ |
| 1 | 6 | $2 y_{1}$ |
| 1 | 10 | $2 y_{2} y_{3} y_{5}$ |
| 2 | 0 | $1$ |
| 2 | 1 | $y_{4} y_{5}$ |
| 2 | 2 | $- y_{2} y_{5} - y_{3}$ |
| 2 | 5 | $y_{2} y_{5}$ |
| 2 | 7 | $2 y_{1}$ |
| 2 | 10 | $2 y_{2} y_{4} y_{5}$ |
| 3 | 0 | $2$ |
| 3 | 6 | $2 y_{3} y_{4} y_{5}$ |
| 3 | 7 | $2 y_{3} y_{4} y_{5}$ |
| 3 | 8 | $2 y_{2} y_{4} y_{5}$ |
| 3 | 9 | $2 y_{2} y_{3} y_{5}$ |
| 3 | 11 | $3 y_{2} y_{3} y_{4} y_{5}^{2} + 3 y_{2} y_{3} y_{4} y_{5}$ |
| 4 | 0 | $2$ |
| 4 | 1 | $y_{3} y_{5}$ |
| 4 | 2 | $y_{3}$ |
| 4 | 4 | $- y_{3} y_{5}$ |
| 4 | 5 | $y_{3} y_{5}$ |
| 4 | 8 | $2 y_{1}$ |
| 4 | 10 | $2 y_{2} y_{3} y_{5} + 2 y_{3} y_{4} y_{5}$ |
| 5 | 0 | $2$ |
| 5 | 1 | $y_{4} y_{5}$ |
| 5 | 2 | $y_{4}$ |
| 5 | 4 | $y_{4}$ |
| 5 | 5 | $- y_{4}$ |
| 5 | 9 | $2 y_{1}$ |
| 5 | 10 | $2 y_{2} y_{4} y_{5} + 2 y_{3} y_{4} y_{5}$ |
| 6 | 1 | $2$ |
| 6 | 3 | $1$ |
| 6 | 6 | $- y_{2} - y_{4} y_{5}$ |
| 6 | 7 | $y_{3}$ |
| 6 | 8 | $y_{2}$ |
| 6 | 11 | $2 y_{2} y_{3} y_{5}$ |
| 7 | 2 | $2$ |
| 7 | 3 | $1$ |
| 7 | 6 | $y_{4} y_{5}$ |
| 7 | 7 | $- y_{2} y_{5} - y_{3}$ |
| 7 | 9 | $y_{2} y_{5}$ |
| 7 | 11 | $2 y_{2} y_{4} y_{5}$ |
| 8 | 3 | $2$ |
| 8 | 4 | $2$ |
| 8 | 6 | $y_{3} y_{5}$ |
| 8 | 7 | $y_{3}$ |
| 8 | 8 | $- y_{3} y_{5}$ |
| 8 | 9 | $y_{3} y_{5}$ |
| 8 | 11 | $2 y_{2} y_{3} y_{5} + 2 y_{3} y_{4} y_{5}$ |
| 9 | 3 | $2$ |
| 9 | 5 | $2$ |
| 9 | 6 | $y_{4} y_{5}$ |
| 9 | 7 | $y_{4}$ |
| 9 | 8 | $y_{4}$ |
| 9 | 9 | $- y_{4}$ |
| 9 | 11 | $2 y_{2} y_{4} y_{5} + 2 y_{3} y_{4} y_{5}$ |
| 10 | 1 | $1$ |
| 10 | 2 | $1$ |
| 10 | 4 | $1$ |
| 10 | 5 | $1$ |
| 10 | 11 | $2 y_{1}$ |
| 11 | 6 | $1$ |
| 11 | 7 | $1$ |
| 11 | 8 | $1$ |
| 11 | 9 | $1$ |
| 11 | 10 | $2$ |
