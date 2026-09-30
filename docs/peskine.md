# Peskine sixfold

For a general trivector \(\sigma\in\Lambda^3V_{10}^*\), the Peskine variety is
the rank-degeneracy locus

\[
X_\sigma=\{[L]\in\mathbb P(V_{10}) :
\operatorname{rank}\sigma(L,-,-)\leq 6\}.
\]

It is a smooth Fano sixfold of degree \(15\) and index \(3\).  The incidence
description identifies it with a zero locus on
\(F(1,4;10)=A_9/P_{1,4}\).  If \(S_1\subset S_4\subset V_{10}\) are the
tautological bundles and \(Q_i=V_{10}/S_i\), the rank-21 bundle used by the
software is

\[
E=S_1^*\otimes\bigl(\Lambda^2Q_1^*/\Lambda^2Q_4^*\bigr).
\]

The flag has dimension \(27\), so a regular section of \(E\) has a
six-dimensional zero locus.  In the \((H_1,H_4)\) basis, `gwflags` obtains

\[
c_1(E)=(13,5),\qquad
c_1(TF(1,4;10))=(4,9),\qquad
c_1(TX_\sigma)=(-9,4).
\]

On the zero locus, \(H_4=3H_1\), hence
\(c_1(TX_\sigma)=3H_1\).  The corresponding ambient curve generator is
\((1,0,0,3,0,0,0,0,0)\).

## Software input

Use the named constructor in Python:

```python
from gwflags import FlagVariety, peskine_bundle

X = FlagVariety('A9', [1, 4])
K = peskine_bundle(X)
fano, betas = X.fano_index_and_betas(K)

assert K.rank == 21
assert fano == 3
```

The compact GUI/CLI spelling is `Peskine()` (lowercase `peskine()` is also
accepted).  For example, this command reports the construction without
starting the positive-degree localization sum:

```bash
python3 -m gwflags.cli A9 --keep 1,4 -K "Peskine()" info
```

The named constructor is essential.  The generic fiber-character expression

```python
tensor(quot(wedge(2, dual(taut_quot(X, 1))),
            wedge(2, dual(taut_quot(X, 4)))),
      dual(taut_sub(X, 1)))
```

has the correct fixed-point character, but it treats the quotient as split on
invariant curves.  The actual quotient is a non-split homogeneous bundle.  Its
extension data changes the curve restrictions and removes the negative
apparent summands produced by the split expression.  `peskine_bundle(X)` keeps
the same character and supplies those geometric edge restrictions to the
twisted localization formula.

## Verified classical sector

The direct \(A_9/P_{1,4}\) backend constructs all 840 Schubert classes without
materializing the 3,628,800 elements of \(S_{10}\).  The degree-zero twisted
metric reduces the classes of codimension at most six to a rank-10 ambient
sector.  In the returned basis

```text
(), (4), (5 4), (6 5 4), (7 6 5 4),
(8 7 6 5 4), (9 8 7 6 5 4), (3 4), (3 5 4), (3 6 5 4)
```

classical multiplication by \(c_1(TX_\sigma)\) is

\[
\begin{bmatrix}
0&0&0&0&0&0&0&0&0&0\\
1&0&0&0&0&0&0&0&0&0\\
0&1&0&0&0&0&0&0&0&0\\
0&0&1&0&0&0&0&-14/5&0&0\\
0&0&0&1&0&0&0&0&-5&0\\
0&0&0&0&9&0&0&0&0&153/4\\
0&0&0&0&0&9&0&0&0&0\\
0&1&0&0&0&0&0&0&0&0\\
0&0&1&0&0&0&0&13/5&0&0\\
0&0&0&1&0&0&0&0&4&0
\end{bmatrix}.
\]

This is the verified \(q=0\) ambient operator.  The positive-degree generic
stable-map localization sum is available as an experimental scalability path,
but it is not yet presented as a completed small quantum matrix for the
Peskine sixfold.

## References

- P. De Poi, D. Faenzi, E. Mezzetti, and K. Ranestad,
  [*Fano congruences of index 3 and alternating 3-forms*](https://arxiv.org/abs/1606.04715).
- J. Song, [*Geometry of hyperkähler manifolds*](https://www.mathematik.hu-berlin.de/~songjiea/docs/thesis_Jieao_Song.pdf),
  Sections 4.3 and 4.5 for the flag zero-locus model and the degree/index
  calculation.
