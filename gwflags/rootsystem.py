"""Root-system data (translation of the LieART calls in V3.nb).

Everything is exact: vectors/matrices are tuples of ``fractions.Fraction``.
Simple roots use the standard (Bourbaki) orthogonal realizations, so for
type A_n the orthogonal ("ort") coordinates live in R^{n+1}.

Replaces the LieART calls of the notebook:
    PositiveRoots / AlphaBasis      -> RootSystemData.positive_roots (alpha basis)
    OrthogonalBasis[PositiveRoots]  -> RootSystemData.positive_roots_ort
    OrthogonalSimpleRoots           -> RootSystemData.simple_roots_ort
    ReflectionMatrices              -> RootSystemData.reflection_matrices
    CartanMatrix                    -> RootSystemData.cartan_matrix
    Transpose[Inverse[CartanMatrix]]-> RootSystemData.cart_matrix  (CartMatrix in V3.nb)
    Coroots (integer coords)        -> RootSystemData.coroots
    OmegaBasis                      -> RootSystemData.omega_basis(root)
"""

from fractions import Fraction
from itertools import product as iproduct

F = Fraction


# ----------------------------------------------------------------- linear alg
def _n(x):
    """Normalize an integral Fraction to int (fast hashing/arithmetic);
    non-integral values stay Fractions."""
    return int(x) if isinstance(x, F) and x.denominator == 1 else x


def norm_vec(v):
    return tuple(_n(x) for x in v)


def norm_mat(m):
    return tuple(tuple(_n(x) for x in row) for row in m)


def vec(*xs):
    return tuple(F(x) for x in xs)


def vadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def vsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def vscale(c, a):
    return tuple(F(c) * x for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def matvec(m, v):
    return tuple(dot(row, v) for row in m)


def matmul(a, b):
    bt = tuple(zip(*b))
    return tuple(tuple(dot(row, col) for col in bt) for row in a)


def identity(n):
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))


def mat_inverse(m):
    n = len(m)
    a = [[F(x) for x in row] + [F(1) if i == j else F(0) for j in range(n)]
         for i, row in enumerate(m)]
    for col in range(n):
        piv = next(r for r in range(col, n) if a[r][col] != 0)
        a[col], a[piv] = a[piv], a[col]
        p = a[col][col]
        a[col] = [x / p for x in a[col]]
        for r in range(n):
            if r != col and a[r][col] != 0:
                f = a[r][col]
                a[r] = [x - f * y for x, y in zip(a[r], a[col])]
    return tuple(tuple(row[n:]) for row in a)


def transpose(m):
    return tuple(zip(*m))


def mat_rank(rows):
    a = [[F(x) for x in r] for r in rows]
    if not a:
        return 0
    ncols, rank = len(a[0]), 0
    for col in range(ncols):
        piv = next((r for r in range(rank, len(a)) if a[r][col] != 0), None)
        if piv is None:
            continue
        a[rank], a[piv] = a[piv], a[rank]
        p = a[rank][col]
        a[rank] = [x / p for x in a[rank]]
        for r in range(len(a)):
            if r != rank and a[r][col] != 0:
                f = a[r][col]
                a[r] = [x - f * y for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


# ----------------------------------------------------- simple roots per type
def _simple_roots_ort(family, rank):
    """Standard orthogonal realizations (Bourbaki numbering)."""
    def e(i, dim):
        return tuple(F(1) if j == i else F(0) for j in range(dim))

    if family == 'A':
        d = rank + 1
        return [vsub(e(i, d), e(i + 1, d)) for i in range(rank)]
    if family == 'B':
        d = rank
        return [vsub(e(i, d), e(i + 1, d)) for i in range(rank - 1)] + [e(rank - 1, d)]
    if family == 'C':
        d = rank
        return ([vsub(e(i, d), e(i + 1, d)) for i in range(rank - 1)]
                + [vscale(2, e(rank - 1, d))])
    if family == 'D':
        d = rank
        return ([vsub(e(i, d), e(i + 1, d)) for i in range(rank - 1)]
                + [vadd(e(rank - 2, d), e(rank - 1, d))])
    if family == 'G' and rank == 2:
        # alpha1 = e1 - e2 (short), alpha2 = -2 e1 + e2 + e3 (long)
        return [vec(1, -1, 0), vec(-2, 1, 1)]
    if family == 'F' and rank == 4:
        return [vec(0, 1, -1, 0), vec(0, 0, 1, -1), vec(0, 0, 0, 1),
                vec(F(1, 2), F(-1, 2), F(-1, 2), F(-1, 2))]
    if family == 'E' and rank in (6, 7, 8):
        a1 = vec(F(1, 2), *([F(-1, 2)] * 6), F(1, 2))
        roots8 = [a1, vec(1, 1, 0, 0, 0, 0, 0, 0)]
        for i in range(6):
            roots8.append(vsub(
                tuple(F(1) if j == i + 1 else F(0) for j in range(8)),
                tuple(F(1) if j == i else F(0) for j in range(8))))
        return roots8[:rank]
    raise ValueError(f'unsupported algebra {family}{rank}')


def parse_algebra(name):
    """Parse a (possibly semisimple) algebra spec into a list of factors.

    Accepts 'A2', 'A2xA2', 'A1xA1xA4', ('A', 2), ['A2', 'A2'],
    [('A', 2), ('A', 2)].  Returns [(family, rank), ...].
    """
    if isinstance(name, (tuple, list)):
        if len(name) == 2 and isinstance(name[1], int):
            return [(name[0].upper(), int(name[1]))]
        out = []
        for part in name:
            out.extend(parse_algebra(part))
        return out
    out = []
    for part in name.replace('*', 'x').replace('X', 'x').split('x'):
        part = part.strip()
        out.append((part[0].upper(), int(part[1:])))
    return out


class RootSystemData:
    """All Lie-algebra data the V3.nb pipeline needs, computed exactly.
    Supports semisimple products (e.g. 'A3xA3' for P^3 x P^3 flags): simple
    roots of the factors are placed in orthogonal direct sum, nodes numbered
    consecutively across factors."""

    def __init__(self, algebra):
        self.factors = parse_algebra(algebra)
        self.name = 'x'.join(f'{f}{r}' for f, r in self.factors)
        self.rank = sum(r for _, r in self.factors)
        blocks = [_simple_roots_ort(f, r) for f, r in self.factors]
        dims = [len(b[0]) for b in blocks]
        self.dim_ort = sum(dims)
        self.simple_roots_ort = []
        off = 0
        for b, d in zip(blocks, dims):
            for root in b:
                self.simple_roots_ort.append(
                    tuple([F(0)] * off) + root + tuple([F(0)] * (self.dim_ort - off - d)))
            off += d

        self.simple_roots_ort = [norm_vec(a) for a in self.simple_roots_ort]
        n = self.rank
        sr = self.simple_roots_ort
        # Cartan matrix A_ij = 2 (a_i, a_j) / (a_j, a_j)
        self.cartan_matrix = tuple(
            tuple(F(2 * dot(sr[i], sr[j]), dot(sr[j], sr[j]))
                  for j in range(n))
            for i in range(n))
        assert all(x.denominator == 1 for row in self.cartan_matrix
                   for x in row)
        self.cartan_matrix = norm_mat(self.cartan_matrix)
        # CartMatrix of V3.nb: Transpose[Inverse[CartanMatrix]];
        # row j, column r gives the coefficient of alpha_j in omega_r.
        self.cart_matrix = transpose(mat_inverse(self.cartan_matrix))

        # positive roots in the alpha basis (integer tuples), via reflection
        # closure of the simple roots using only the Cartan matrix
        A = self.cartan_matrix
        seen = set()
        frontier = [tuple(1 if j == i else 0 for j in range(n)) for i in range(n)]
        allroots = set(frontier)
        while frontier:
            new = []
            for v in frontier:
                for j in range(n):
                    c = sum(v[i] * A[i][j] for i in range(n))
                    w = tuple(v[k] - (c if k == j else 0) for k in range(n))
                    if w not in allroots:
                        allroots.add(w)
                        new.append(w)
            frontier = new
        pos = sorted((tuple(int(c) for c in r) for r in allroots
                      if all(c >= 0 for c in r)),
                     key=lambda r: (sum(r), r))
        self.positive_roots = pos                      # alpha basis
        self.positive_roots_ort = [self.alpha_to_ort(r) for r in pos]

        # reflection matrices of the simple roots, acting on ort coordinates
        self.reflection_matrices = [self.reflection_matrix_of(a) for a in sr]

        # coroots: integer coordinates of beta^vee in the simple-coroot basis
        # (the Coroots[] script of V3.nb)
        self.coroots = []
        for r, r_ort in zip(pos, self.positive_roots_ort):
            bb = dot(r_ort, r_ort)
            co = tuple(F(c * dot(sr[i], sr[i]), bb) for i, c in enumerate(r))
            assert all(x.denominator == 1 for x in co), 'coroot not integral'
            self.coroots.append(tuple(int(x) for x in co))

    # ------------------------------------------------------------- helpers
    def alpha_to_ort(self, r):
        v = tuple(0 for _ in range(self.dim_ort))
        for c, a in zip(r, self.simple_roots_ort):
            v = vadd(v, vscale(c, a))
        return norm_vec(v)

    def reflection_matrix_of(self, root_ort):
        """s_beta acting on ort coordinates: x -> x - 2 (x,b)/(b,b) b."""
        d = self.dim_ort
        bb = dot(root_ort, root_ort)
        cols = []
        for i in range(d):
            ei = tuple(1 if j == i else 0 for j in range(d))
            cols.append(vsub(ei, vscale(F(2 * root_ort[i], bb), root_ort)))
        # columns are images of basis vectors
        return norm_mat(transpose(tuple(cols)))

    def omega_basis(self, root_alpha):
        """OmegaBasis: alpha-basis root -> fundamental-weight coordinates,
        i.e. component j is <root, alpha_j^vee>."""
        A = self.cartan_matrix
        n = self.rank
        return tuple(sum(root_alpha[i] * A[i][j] for i in range(n))
                     for j in range(n))

    def root_index_ort(self, v_ort):
        """Index and sign of an ort vector among the positive roots."""
        for i, r in enumerate(self.positive_roots_ort):
            if v_ort == r:
                return i, 1
            if v_ort == tuple(-x for x in r):
                return i, -1
        raise KeyError(f'not (minus) a positive root: {v_ort}')
