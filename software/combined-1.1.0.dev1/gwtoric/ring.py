"""Cohomology ring of a smooth complete toric variety,

    H^*(X, Q) = Q[x_1..x_k] / (I + J),

I = linear relations sum_i <m, rho_i> x_i, J = Stanley-Reisner ideal
(Cox-Little-Schenck, Theorem 12.4.1).

A graded basis is chosen by linear algebra, not by inspection: a Q-basis
of H^2 is picked greedily among the x_i (x_i is dropped when it is a
combination of the earlier ones modulo I); every x_i is then expressed in
those r = k - n variables, so the ring becomes Q[y_1..y_r]/J' with J' the
substituted Stanley-Reisner generators, and in each degree d the space
J'_d is spanned by (monomials of degree d - |S|) * g_S.  Row reduction of
that span gives the basis (the non-pivot monomials) and a normal-form map.
Dimensions are checked against the h-vector of the fan.

CohClass is a polynomial in the divisor classes x_i (dict monomial ->
coefficient, monomial = sorted tuple of ray indices with repetition); it
is what the user manipulates and what the localization engine restricts
to the fixed points.
"""

from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb

from gwflags.rootsystem import mat_inverse


class CohClass:
    """Polynomial in the toric divisor classes x_i of a ToricVariety."""

    __slots__ = ('X', 'terms')

    def __init__(self, X, terms):
        self.X = X
        self.terms = {m: Fraction(c) for m, c in terms.items() if c != 0}

    # ------------------------------------------------------ arithmetic
    def _coerce(self, other):
        if isinstance(other, CohClass):
            if other.X is not self.X:
                raise ValueError('classes live on different varieties')
            return other
        if isinstance(other, (int, Fraction)):
            return CohClass(self.X, {(): Fraction(other)})
        return NotImplemented

    def __add__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return other
        t = dict(self.terms)
        for m, c in other.terms.items():
            t[m] = t.get(m, 0) + c
        return CohClass(self.X, t)

    __radd__ = __add__

    def __neg__(self):
        return CohClass(self.X, {m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return other
        return self + (-other)

    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return other
        t = {}
        for m1, c1 in self.terms.items():
            for m2, c2 in other.terms.items():
                m = tuple(sorted(m1 + m2))
                t[m] = t.get(m, 0) + c1 * c2
        return CohClass(self.X, t)

    __rmul__ = __mul__

    def __pow__(self, e):
        if not isinstance(e, int) or e < 0:
            raise ValueError('exponent must be a nonnegative integer')
        out = CohClass(self.X, {(): Fraction(1)})
        for _ in range(e):
            out = out * self
        return out

    def __eq__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return False
        return self.X.ring.is_zero(self - other)

    __hash__ = None

    # --------------------------------------------------------- queries
    def is_zero(self):
        return not self.terms

    def degree(self):
        """Complex degree; raises for inhomogeneous classes."""
        degs = {len(m) for m in self.terms}
        if not degs:
            return 0
        if len(degs) > 1:
            raise ValueError(f'inhomogeneous class {self}')
        return degs.pop()

    def homogeneous_parts(self):
        parts = {}
        for m, c in self.terms.items():
            parts.setdefault(len(m), {})[m] = c
        return {d: CohClass(self.X, t) for d, t in sorted(parts.items())}

    def __repr__(self):
        if not self.terms:
            return '0'
        out = []
        for m, c in sorted(self.terms.items(), key=lambda mc: (len(mc[0]), mc[0])):
            mono = '*'.join(_mono_str(m))
            if not mono:
                out.append(str(c))
            elif c == 1:
                out.append(mono)
            elif c == -1:
                out.append('-' + mono)
            else:
                out.append(f'{c}*{mono}')
        s = ' + '.join(out)
        return s.replace('+ -', '- ')


def _mono_str(m):
    out, i = [], 0
    while i < len(m):
        j = i
        while j < len(m) and m[j] == m[i]:
            j += 1
        out.append(f'x{m[i]}' + (f'^{j - i}' if j - i > 1 else ''))
        i = j
    return out


# --------------------------------------------------------- polynomials in y
def _padd(a, b, scale=1):
    out = dict(a)
    for e, c in b.items():
        v = out.get(e, 0) + scale * c
        if v:
            out[e] = v
        elif e in out:
            del out[e]
    return out


def _pmul(a, b):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = tuple(x + y for x, y in zip(e1, e2))
            v = out.get(e, 0) + c1 * c2
            if v:
                out[e] = v
            elif e in out:
                del out[e]
    return out


class CohomologyRing:
    def __init__(self, fan):
        self.fan = fan
        k, n = fan.k, fan.n
        self.k, self.n = k, n
        r = k - n
        self.r = r

        # greedy H^2 basis among the x_i
        rows = [[Fraction(x) for x in row] for row in fan.ray_matrix]
        from gwflags.rootsystem import mat_rank
        chosen = []
        rank = mat_rank(rows) if rows else 0
        for i in range(k):
            e = [Fraction(1 if j == i else 0) for j in range(k)]
            nr = mat_rank(rows + [e])
            if nr > rank:
                chosen.append(i)
                rows.append(e)
                rank = nr
        assert len(chosen) == r, 'H^2 basis has the wrong size'
        self.basis_vars = chosen                 # ray indices j_1..j_r

        # express x_i in the basis: solve  e_i = sum c_j e_{b_j} + A^T lam
        M = tuple(tuple(
            (Fraction(1) if i == chosen[j] else Fraction(0)) if j < r
            else Fraction(fan.rays[i][j - r])
            for j in range(k)) for i in range(k))
        Minv = mat_inverse(M)
        self.subst = []          # subst[i] = {unit exponent tuple: coeff}
        for i in range(k):
            lin = {}
            for j in range(r):
                c = Minv[j][i]
                if c:
                    lin[tuple(1 if t == j else 0 for t in range(r))] = c
            self.subst.append(lin)

        # Stanley-Reisner generators in the y variables
        self.nonfaces = fan.minimal_nonfaces()
        self.sr_gens = []
        for S in self.nonfaces:
            p = {tuple([0] * r): Fraction(1)}
            for i in S:
                p = _pmul(p, self.subst[i])
            self.sr_gens.append((len(S), p))

        # graded pieces
        self.monos = {}
        self.mono_index = {}
        self.echelon = {}       # d -> {pivot col: row dict}
        self.basis = {}         # d -> list of exponent tuples
        for d in range(n + 1):
            self._build_degree(d)
        dims = [len(self.basis[d]) for d in range(n + 1)]
        hv = self._h_vector()
        if dims != hv:
            raise ValueError(
                f'cohomology dimensions {dims} disagree with the h-vector '
                f'{hv} of the fan; the fan is not a smooth complete fan')
        self.betti = dims
        # flat list of basis classes (as (degree, exponent tuple))
        self.graded_basis = [(d, e) for d in range(n + 1)
                             for e in self.basis[d]]

    # ------------------------------------------------------ construction
    def _h_vector(self):
        f = self.fan.cones_by_dim()          # f[i] = #cones with i rays
        n = self.n
        return [sum((-1) ** (i - d) * comb(i, d) * f[n - i] for i in range(d, n + 1))
                for d in range(n + 1)]

    def _monomials(self, d):
        r = self.r
        out = []
        for combo in combinations_with_replacement(range(r), d):
            e = [0] * r
            for j in combo:
                e[j] += 1
            out.append(tuple(e))
        # pure powers first (they are eliminated preferentially)
        out.sort(key=lambda e: (-max(e) if e else 0, e))
        return out

    def _build_degree(self, d):
        monos = self._monomials(d)
        idx = {e: i for i, e in enumerate(monos)}
        self.monos[d] = monos
        self.mono_index[d] = idx
        ech = {}
        for size, g in self.sr_gens:
            if size > d:
                continue
            for m in self._monomials(d - size):
                prod = _pmul({m: Fraction(1)}, g)
                vec = {idx[e]: c for e, c in prod.items()}
                self._insert(ech, vec)
        self.echelon[d] = ech
        self.basis[d] = [e for i, e in enumerate(monos) if i not in ech]

    @staticmethod
    def _reduce_vec(ech, vec):
        vec = dict(vec)
        for p in sorted(ech):
            c = vec.get(p)
            if c:
                row = ech[p]
                for col, rc in row.items():
                    v = vec.get(col, 0) - c * rc
                    if v:
                        vec[col] = v
                    elif col in vec:
                        del vec[col]
        return vec

    def _insert(self, ech, vec):
        vec = self._reduce_vec(ech, vec)
        if not vec:
            return
        p = min(vec)
        inv = 1 / vec[p]
        ech[p] = {col: c * inv for col, c in vec.items()}

    # ------------------------------------------------------- conversions
    def to_y(self, cls):
        """CohClass -> dict {degree: {exponent tuple: coeff}} in the basis
        variables (substituting the linear relations)."""
        out = {}
        r = self.r
        for m, c in cls.terms.items():
            p = {tuple([0] * r): c}
            for i in m:
                p = _pmul(p, self.subst[i])
            d = len(m)
            out[d] = _padd(out.get(d, {}), p)
        return {d: p for d, p in out.items() if p}

    def normal_form_y(self, d, p):
        """Reduce a degree-d polynomial in y to the basis monomials."""
        if d > self.n:
            return {}
        idx = self.mono_index[d]
        vec = {idx[e]: c for e, c in p.items()}
        vec = self._reduce_vec(self.echelon[d], vec)
        monos = self.monos[d]
        return {monos[i]: c for i, c in vec.items()}

    def coordinates(self, cls):
        """Coordinates of a CohClass in the graded basis: dict
        basis index -> Fraction."""
        out = {}
        pos = {b: i for i, b in enumerate(self.graded_basis)}
        for d, p in self.to_y(cls).items():
            for e, c in self.normal_form_y(d, p).items():
                out[pos[(d, e)]] = c
        return out

    def is_zero(self, cls):
        return not self.coordinates(cls)

    def y_to_class(self, X, d, e):
        """Basis monomial (degree d, exponents e) as a CohClass in the x's."""
        rays = []
        for j, ex in enumerate(e):
            rays.extend([self.basis_vars[j]] * ex)
        return CohClass(X, {tuple(sorted(rays)): Fraction(1)})

    def hodge_diamond(self):
        """h^{p,q}: only h^{p,p} = b_{2p} is nonzero."""
        n = self.n
        return [[self.betti[p] if (p == q) else 0 for q in range(n + 1)]
                for p in range(n + 1)]
