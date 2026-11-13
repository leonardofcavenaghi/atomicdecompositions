"""Combinatorics of a smooth complete fan.

Input: rays rho_1..rho_k in Z^n and the maximal cones as sets of ray
indices (0-based).  Everything the localization pipeline needs is derived
here:

  * all cones (the fan is simplicial, so every subset of a maximal cone
    is a cone), minimal non-faces (Stanley-Reisner generators);
  * the dual basis {m_i} of every maximal cone sigma = {rho_1..rho_n},
    m_i(rho_j) = delta_ij -- these are the torus weights of the tangent
    space at the fixed point p_sigma, the tangent weights of the invariant
    curves through it, and the restrictions [D_{rho_i}]^T|_sigma of the
    equivariant divisor classes;
  * the walls tau = sigma cap sigma' (cones with n-1 rays) with their
    wall relation  v + v' + sum_i a_i rho_i = 0  and the resulting class
    [C_tau] = (b_rho) in H_2(X,Z) = { (a_rho) : sum a_rho rho = 0 },
    with  D_rho . C_tau = b_rho;
  * a Z-basis of H_2(X,Z) and an ample divisor (needed to bound the
    degrees in the tree enumeration).

Validation: |det sigma| = 1 for every maximal cone (smoothness), every
wall lies in exactly two maximal cones and v' lies strictly on the other
side of the wall (completeness / convexity), a random-point covering test,
and existence of an ample divisor (projectivity, via a small LP).
"""

from fractions import Fraction
from itertools import combinations
from math import gcd
import random

from gwflags.rootsystem import mat_inverse, mat_rank


# ------------------------------------------------------------ integer kernel
def integer_kernel(A):
    """Z-basis of { a in Z^k : A a = 0 } for an integer matrix A (list of
    rows), by unimodular column reduction."""
    n = len(A)
    k = len(A[0]) if A else 0
    cols = [[A[r][j] for r in range(n)] for j in range(k)]
    ucols = [[1 if i == j else 0 for i in range(k)] for j in range(k)]
    p = 0
    for r in range(n):
        if p >= k:
            break
        while True:
            piv = None
            for j in range(p, k):
                if cols[j][r] != 0 and (piv is None or
                                        abs(cols[j][r]) < abs(cols[piv][r])):
                    piv = j
            if piv is None:
                break
            cols[p], cols[piv] = cols[piv], cols[p]
            ucols[p], ucols[piv] = ucols[piv], ucols[p]
            done = True
            for j in range(p + 1, k):
                q = cols[j][r] // cols[p][r]
                if q:
                    cols[j] = [a - q * b for a, b in zip(cols[j], cols[p])]
                    ucols[j] = [a - q * b for a, b in zip(ucols[j], ucols[p])]
                if cols[j][r] != 0:
                    done = False
            if done:
                break
        if any(cols[j][r] != 0 for j in range(p, k)):
            p += 1
    basis = [tuple(u) for j, u in enumerate(ucols) if j >= p]
    for u in basis:
        assert all(sum(A[r][i] * u[i] for i in range(k)) == 0 for r in range(n))
    return basis


def _lcm(a, b):
    return a * b // gcd(a, b) if a and b else a or b


class Fan:
    def __init__(self, rays, max_cones, check=True, seed=0):
        rays = [tuple(int(x) for x in r) for r in rays]
        if not rays:
            raise ValueError('no rays given')
        n = len(rays[0])
        if any(len(r) != n for r in rays):
            raise ValueError('all rays must have the same dimension')
        if len(set(rays)) != len(rays):
            raise ValueError('rays must be distinct')
        self.n = n
        self.k = len(rays)
        self.rays = rays
        cones = []
        for c in max_cones:
            c = tuple(sorted(int(i) for i in c))
            if len(c) != n or len(set(c)) != n:
                raise ValueError(
                    f'maximal cone {c} must consist of {n} distinct rays')
            if any(i < 0 or i >= self.k for i in c):
                raise ValueError(f'maximal cone {c}: ray index out of range')
            cones.append(c)
        if len(set(cones)) != len(cones):
            raise ValueError('maximal cones must be distinct')
        if not cones:
            raise ValueError('no maximal cones given')
        self.max_cones = cones
        self._rng = random.Random(seed)

        # dual bases (also the smoothness check)
        self.dual = []
        for c in cones:
            R = tuple(tuple(Fraction(x) for x in rays[i]) for i in c)
            if mat_rank(R) < n:
                raise ValueError(f'maximal cone {c} is degenerate')
            Rinv = mat_inverse(R)
            d = {}
            for j, i in enumerate(c):
                m = tuple(Rinv[r][j] for r in range(n))
                if any(x.denominator != 1 for x in m):
                    raise ValueError(
                        f'maximal cone {c} is not smooth (|det| != 1); '
                        f'only smooth fans are supported')
                d[i] = tuple(int(x) for x in m)
            self.dual.append(d)
        self.cone_index = {c: i for i, c in enumerate(cones)}

        # all faces
        faces = set()
        for c in cones:
            for s in range(n + 1):
                for sub in combinations(c, s):
                    faces.add(frozenset(sub))
        self.faces = faces
        used = set(i for c in cones for i in c)
        if len(used) != self.k:
            raise ValueError('every ray must belong to some maximal cone')

        # walls
        self.walls = []                    # list of dicts
        self.wall_index = {}
        facets = {}
        for ci, c in enumerate(cones):
            for i in c:
                tau = tuple(j for j in c if j != i)
                facets.setdefault(tau, []).append((ci, i))
        for tau, lst in sorted(facets.items()):
            if len(lst) != 2:
                raise ValueError(
                    f'wall {tau} lies in {len(lst)} maximal cone(s), '
                    f'expected 2: the fan is not complete (or not a fan)')
            (ca, v), (cb, vp) = lst
            coords = {i: sum(self.dual[ca][i][r] * rays[vp][r]
                             for r in range(n)) for i in cones[ca]}
            if coords[v] != -1:
                raise ValueError(
                    f'cones {cones[ca]} and {cones[cb]} do not lie on '
                    f'opposite sides of their common wall {tau} '
                    f'(coefficient {coords[v]}); not a smooth complete fan')
            b = [0] * self.k
            b[v] = 1
            b[vp] = 1
            for i in tau:
                b[i] = -coords[i]
            w = {'tau': tau, 'cones': (ca, cb), 'v': v, 'vp': vp,
                 'cls': tuple(b)}
            self.wall_index[tau] = len(self.walls)
            self.walls.append(w)
        self.wall_classes = sorted(set(w['cls'] for w in self.walls))

        # H_2 lattice: kernel of the ray matrix
        A = [[rays[i][r] for i in range(self.k)] for r in range(n)]
        self.ray_matrix = A
        self.h2_basis = integer_kernel(A)
        assert len(self.h2_basis) == self.k - n, 'unexpected H_2 rank'

        if check:
            self._covering_check()
        self.ample = None
        self._ample_computed = False
        # Pic X = Hom(H_2(X, Z), Z): the divisors D_rho with rho outside a
        # maximal cone are a Z-basis, so the pairing between them and
        # h2_basis is unimodular and converts degrees <-> coefficients
        self._pic_free = [i for i in range(self.k) if i not in set(cones[0])]
        self._pic_inv = None
        self._nef_basis = ()                       # () = not computed yet

    # ---------------------------------------------------------- helpers
    def is_cone(self, rays_subset):
        return frozenset(rays_subset) in self.faces

    def cones_by_dim(self):
        out = [0] * (self.n + 1)
        for f in self.faces:
            out[len(f)] += 1
        return out

    def minimal_nonfaces(self):
        """Minimal subsets of rays that are not cones (Stanley-Reisner
        generators).  Their size is at most n + 1."""
        out = []
        for s in range(2, self.n + 2):
            for sub in combinations(range(self.k), s):
                fs = frozenset(sub)
                if fs in self.faces:
                    continue
                if any(nf <= fs for nf in out):
                    continue
                out.append(fs)
        return [tuple(sorted(f)) for f in out]

    def in_h2(self, a):
        return all(sum(self.rays[i][r] * a[i] for i in range(self.k)) == 0
                   for r in range(self.n))

    def _covering_check(self, trials=25):
        """A generic point must lie in exactly one maximal cone."""
        n = self.n
        for _ in range(trials):
            pt = [Fraction(self._rng.randint(-10 ** 6, 10 ** 6),
                           self._rng.randint(1, 1000)) for _ in range(n)]
            count = 0
            for ci, c in enumerate(self.max_cones):
                coords = [sum(self.dual[ci][i][r] * pt[r] for r in range(n))
                          for i in c]
                if all(x > 0 for x in coords):
                    count += 1
            if count != 1:
                raise ValueError(
                    f'a generic point lies in {count} maximal cones; the '
                    f'cones do not form a complete fan')

    # ------------------------------------------- Picard group coordinates
    def _pic_matrix(self):
        """Inverse of the pairing matrix (h2_basis[j] . D_i)_{i in
        _pic_free, j} (unimodular, see __init__)."""
        if self._pic_inv is None:
            r = self.k - self.n
            mat = tuple(tuple(Fraction(self.h2_basis[j][i]) for j in range(r))
                        for i in self._pic_free)
            self._pic_inv = mat_inverse(mat)
        return self._pic_inv

    def curve_coordinates(self, cls):
        """Coordinates of a curve class in h2_basis (integers)."""
        inv = self._pic_matrix()
        r = self.k - self.n
        out = []
        for j in range(r):
            v = sum(inv[j][a] * Fraction(cls[i])
                    for a, i in enumerate(self._pic_free))
            assert v.denominator == 1, 'class outside the H_2 lattice'
            out.append(int(v))
        return tuple(out)

    def divisor_with_degrees(self, degs):
        """Ray coefficients of the divisor D with D . h2_basis[j] = degs[j],
        supported outside the first maximal cone."""
        inv = self._pic_matrix()
        r = self.k - self.n
        out = [0] * self.k
        for a, i in enumerate(self._pic_free):
            v = sum(inv[j][a] * Fraction(degs[j]) for j in range(r))
            assert v.denominator == 1, 'degrees outside the Picard lattice'
            out[i] = int(v)
        return tuple(out)

    def _det(self, rows):
        mat = [[Fraction(x) for x in row] for row in rows]
        n = len(mat)
        det = Fraction(1)
        for c in range(n):
            p = next((i for i in range(c, n) if mat[i][c] != 0), None)
            if p is None:
                return Fraction(0)
            if p != c:
                mat[c], mat[p] = mat[p], mat[c]
                det = -det
            det *= mat[c][c]
            inv = 1 / mat[c][c]
            mat[c] = [x * inv for x in mat[c]]
            for i in range(c + 1, n):
                if mat[i][c]:
                    f = mat[i][c]
                    mat[i] = [x - f * y for x, y in zip(mat[i], mat[c])]
        return det

    def nef_basis(self, limit=40000):
        """Ray coefficients of r = k - n nef divisors forming a Z-basis of
        Pic X, or None when the nef cone contains no lattice basis.  Their
        degrees on an effective class are >= 0, which is what makes the
        Novikov exponents nonnegative."""
        if self._nef_basis != ():
            return self._nef_basis
        from itertools import combinations
        from .mori import extreme_rays
        r = self.k - self.n
        self._nef_basis = None
        if r == 0:
            self._nef_basis = []
            return self._nef_basis
        walls_t = sorted({self.curve_coordinates(w) for w in self.wall_classes})
        try:
            rays = extreme_rays(walls_t, r)
        except ValueError:                       # nef cone not pointed
            return None
        # a prime divisor is preferred to an arbitrary representative
        prime = {}
        for i in range(self.k):
            coeffs = [1 if j == i else 0 for j in range(self.k)]
            degs = tuple(self.wall_degree(coeffs, b) for b in self.h2_basis)
            prime.setdefault(degs, i)
        # prime divisors first: they give the shortest Novikov monomials
        nefprime = sorted(degs for degs, i in prime.items()
                          if all(self.wall_degree(
                              [1 if j == i else 0 for j in range(self.k)], w) >= 0
                              for w in self.wall_classes) and any(degs))
        extra = sorted(set(rays) - set(nefprime),
                       key=lambda v: (sum(abs(x) for x in v), v))
        sums = sorted({tuple(a + b for a, b in zip(u, v))
                       for u, v in combinations(rays, 2)}
                      - set(nefprime) - set(extra),
                      key=lambda v: (sum(abs(x) for x in v), v))
        cands = nefprime + extra + sums
        tried = 0
        for sub in combinations(cands[:12], r):
            tried += 1
            if tried > limit:
                break
            if abs(self._det(sub)) != 1:
                continue
            out = []
            for degs in sub:
                i = prime.get(degs)
                out.append(tuple(1 if j == i else 0 for j in range(self.k))
                           if i is not None else self.divisor_with_degrees(degs))
            self._nef_basis = out
            return out
        return None

    # ------------------------------------------------------ ample divisor
    def wall_degree(self, coeffs, cls):
        return sum(c * b for c, b in zip(coeffs, cls))

    def ample_divisor(self):
        """Integer coefficients c_rho >= 0 of an ample divisor
        sum c_rho D_rho (all wall curves have positive degree).  The
        anticanonical divisor (all ones) is used when the variety is Fano;
        otherwise a small LP is solved.  Raises if none exists (the fan is
        not projective)."""
        if self._ample_computed:
            return self.ample
        ones = [1] * self.k
        if all(self.wall_degree(ones, w) > 0 for w in self.wall_classes):
            self.ample = ones
        else:
            self.ample = self._ample_lp()
        self._ample_computed = True
        return self.ample

    def is_fano(self):
        return all(sum(w) > 0 for w in self.wall_classes)

    def _ample_lp(self):
        try:
            import sympy
            from sympy.solvers.simplex import lpmin
        except ImportError as exc:      # pragma: no cover
            raise ValueError('the variety is not Fano and sympy\'s simplex '
                             'solver is unavailable to find an ample divisor'
                             ) from exc
        cs = sympy.symbols(f'c0:{self.k}')
        constraints = [sum(c * b for c, b in zip(cs, w)) >= 1
                       for w in self.wall_classes]
        constraints += [c >= 0 for c in cs]
        try:
            _, sol = lpmin(sum(cs), constraints)
        except Exception as exc:
            raise ValueError('no ample divisor found: the fan is not '
                             'projective (or the LP failed: %s)' % exc)
        vals = [Fraction(int(sympy.Rational(sol[c]).p),
                         int(sympy.Rational(sol[c]).q)) for c in cs]
        den = 1
        for v in vals:
            den = _lcm(den, v.denominator)
        coeffs = [int(v * den) for v in vals]
        assert all(self.wall_degree(coeffs, w) > 0 for w in self.wall_classes)
        return coeffs

    # ------------------------------------------------------ constructions
    def product(self, other):
        n1, n2 = self.n, other.n
        rays = [r + (0,) * n2 for r in self.rays] + \
               [(0,) * n1 + r for r in other.rays]
        cones = [c1 + tuple(i + self.k for i in c2)
                 for c1 in self.max_cones for c2 in other.max_cones]
        return Fan(rays, cones)

    def star_subdivision(self, cone_rays):
        """Blow-up along the orbit closure V(tau): insert the ray
        sum_{rho in tau} rho and subdivide every maximal cone containing
        tau.  Stays smooth."""
        tau = tuple(sorted(cone_rays))
        if not self.is_cone(tau) or len(tau) < 2:
            raise ValueError(f'{tau} is not a cone of dimension >= 2')
        new_ray = tuple(sum(self.rays[i][r] for i in tau)
                        for r in range(self.n))
        rays = self.rays + [new_ray]
        v = self.k
        cones = []
        for c in self.max_cones:
            if set(tau) <= set(c):
                for i in tau:
                    cones.append(tuple(j for j in c if j != i) + (v,))
            else:
                cones.append(c)
        return Fan(rays, cones)

    def projective_bundle(self, divisors):
        """Fan of the projective bundle P(E) -> X of a split bundle
        E = O(D_0) + ... + O(D_r), r >= 1, by Cox-Little-Schenck
        Prop. 7.3.3 in the normalized form (7.3.2)-(7.3.3).

        Each summand is given by the k ray coefficients of
        D_i = sum_rho a_{i,rho} D_rho; every divisor on a smooth toric
        variety is Cartier, so any integers will do.  The fan lives in
        N x Z^r and its rays are, in this order,

          * the lifted base rays, one per ray of X and with the same index,
                v_rho = u_rho + sum_{i=1..r} (a_{i,rho} - a_{0,rho}) e_i,
          * the fiber rays e_1, ..., e_r, e_0 = -(e_1 + ... + e_r), i.e.
            indices k..k+r in the ray order of projective_space(r).

        The maximal cones are Cone(v_rho | rho in sigma(1)) + F_i for every
        maximal sigma of X and every facet F_i = Cone(e_0,..,^e_i,..,e_r) of
        the first orthant, (r + 1) |Sigma(n)| in all.

        Only the differences D_i - D_0 enter, as they must: P(E) = P(E ox L).
        Replacing some D_i by a linearly equivalent divisor shears N x Z^r by
        a lattice automorphism, so the variety depends only on the classes.
        D_{v_rho} = pi^* D_rho, and the fiber ray e_i cuts out the
        sub-bundle P(sum_{j != i} O(D_j)); with all D_i equal the
        construction returns the product fan of X and projective_space(r).
        """
        rows = [tuple(int(v) for v in a) for a in divisors]
        if len(rows) < 2:
            raise ValueError('a projective bundle needs at least two summands '
                             'O(D_0), ..., O(D_r)')
        if any(len(a) != self.k for a in rows):
            raise ValueError(f'every summand needs {self.k} ray coefficients, '
                             f'got {[len(a) for a in rows]}')
        r = len(rows) - 1
        rays = [self.rays[i] + tuple(rows[m][i] - rows[0][i]
                                     for m in range(1, r + 1))
                for i in range(self.k)]
        fiber = [tuple(1 if j == m else 0 for j in range(r)) for m in range(r)]
        fiber.append(tuple([-1] * r))                      # e_0 = -sum e_i
        rays += [(0,) * self.n + f for f in fiber]
        facets = list(combinations(range(self.k, self.k + r + 1), r))
        cones = [c + f for c in self.max_cones for f in facets]
        return Fan(rays, cones)
