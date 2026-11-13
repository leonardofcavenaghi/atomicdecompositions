"""Curve classes of a Fano complete intersection Z in a toric variety X
when c1(Z) is not positive on every invariant curve of X.

L = -K_X - sum_m D_m restricts to -K_Z.  The classes that can contribute
to c1(TZ)* have 1 <= L . beta <= dim Z + 1, but when L has degree <= 0 on
some invariant curve of X infinitely many classes of the Mori cone of X
satisfy this.  The ones that matter are effective on Z, so the list is
bounded here by a polyhedral description of the curves of Z instead of an
ample-degree cutoff.  Everything below assumes that Z is a generic member
and that **Z is Fano** (not checked: it cannot be read off the fan).

Pieces.  An irreducible curve B of Z lies in a smallest orbit closure
V(sigma) and meets its open orbit, so with beta = (a_rho) = (D_rho . B):

  * a_rho = 0   for rho outside sigma and its link (D_rho misses V(sigma));
  * a_rho >= 0  for rho in the link of sigma (B is not inside D_rho);
  * a_rho = 0   for rho in the link with Z cap V(sigma + rho) empty;
  * N . beta >= 0 for every user inequality N (the `mori` argument: a
    divisor that is nonnegative on every curve of Z);
  * L . beta >= 1  (Z is Fano).

Z cap V(sigma) is cut out by generic sections of globally generated line
bundles, so it has the expected dimension or is empty, and it is empty
iff the class prod_m D_m . [V(sigma)] vanishes.  Only strata with
dim V(sigma) - r >= 1 carry curves; when that number is 1, Z cap V(sigma)
is a curve of known class c and its components B satisfy in addition
c - [B] in the same cone (for r = 1 and D^2 . V > 0 it is irreducible by
Bertini, so B = c).  A pair (sigma, beta) satisfying these conditions is a
*piece*.  If L is positive on each of these cones the pieces with
L <= dim Z + 1 are finitely many; otherwise MoriStuck names the strata and
the rays with L <= 0, and a `mori` inequality is needed there.

Configurations.  The image of a stable map is a connected union of
irreducible curves, so its class is a sum of pieces whose incidence graph
is connected.  Two curves with smallest strata sigma_i, sigma_j can meet
only if sigma_i + sigma_j is a cone, a^i_rho >= 1 for rho in
sigma_j - sigma_i and a^j_rho >= 1 for rho in sigma_i - sigma_j (a common
point lies in every D_rho, rho in sigma_i + sigma_j).

Insertions.  <c1, a, b>_beta needs deg a + deg b = dim - 1 + L . beta, so
for L . beta >= dim every such invariant has a point insertion.  A
component through a general point of Z lies in no toric divisor
(sigma = empty) and has L >= 2; through two general points it has
L >= dim + 1.  Hence beta is kept only if some connected configuration
has a free piece (L . beta = dim), resp. two free pieces or one with
L >= dim + 1 (L . beta = dim + 1); in the last case beta is also dropped
when H . beta = 0 for a nef H that is nontrivial on Z (the curves of
class beta lie in the fibres of the contraction of H, and two general
points of Z do not).  Every rule is a necessary condition, so no
contributing class is lost.
"""

from fractions import Fraction
from itertools import combinations, product
from math import ceil, floor, gcd

from .fan import integer_kernel

CONFIG_LIMIT = 400000      # above this the connectedness test is skipped
BOX_LIMIT = 3000000


class MoriStuck(Exception):
    """L is not positive on the cone of some stratum.  .stuck is a list of
    (sigma, ray) with ray a class (vector in Z^k) of L-degree <= 0."""

    def __init__(self, stuck):
        self.stuck = stuck
        super().__init__(
            'c1(Z) is not positive on the cone of curves of the strata '
            + ', '.join(f'V{tuple(s)} (class {list(b)})' for s, b in stuck))


# ---------------------------------------------------------- linear algebra
def _primitive(v):
    den = 1
    for x in v:
        den = den * Fraction(x).denominator // gcd(den, Fraction(x).denominator)
    ints = [int(Fraction(x) * den) for x in v]
    g = 0
    for x in ints:
        g = gcd(g, abs(x))
    return tuple(x // g for x in ints) if g else tuple(ints)


def _nullspace(rows, d):
    """Basis of { v in Q^d : row . v = 0 for all rows }."""
    M = [[Fraction(x) for x in r] for r in rows]
    pivots = []
    rk = 0
    for c in range(d):
        p = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[rk], M[p] = M[p], M[rk]
        inv = 1 / M[rk][c]
        M[rk] = [x * inv for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[rk])]
        pivots.append(c)
        rk += 1
    free = [c for c in range(d) if c not in pivots]
    basis = []
    for fcol in free:
        v = [Fraction(0)] * d
        v[fcol] = Fraction(1)
        for i, pc in enumerate(pivots):
            v[pc] = -M[i][fcol]
        basis.append(v)
    return basis


def extreme_rays(A, d):
    """Primitive generators of the extreme rays of the pointed cone
    { v in Q^d : A v >= 0 } (A: integer rows)."""
    rows = sorted({_primitive(r) for r in A if any(r)})
    if d == 0:
        return []
    if len(_nullspace(rows, d)) != 0:
        raise ValueError('the cone is not pointed')
    rays = set()
    for sub in combinations(rows, d - 1):
        ns = _nullspace(sub, d)
        if len(ns) != 1:
            continue
        for sign in (1, -1):
            v = [sign * x for x in ns[0]]
            if all(sum(a * b for a, b in zip(r, v)) >= 0 for r in rows):
                rays.add(_primitive(v))
    return sorted(rays)


def lattice_points(G, h, d):
    """Integer points of { u in Q^d : G u + h >= 0 }.  Returns
    (points, recession rays); points is None when the polyhedron is
    unbounded (recession rays nonempty)."""
    if d == 0:
        return ([()] if all(x >= 0 for x in h) else []), []
    rows = [tuple(g) + (hh,) for g, hh in zip(G, h)] + [(0,) * d + (1,)]
    rays = extreme_rays(rows, d + 1)
    recession = [r[:d] for r in rays if r[d] == 0]
    if recession:
        return None, recession
    verts = [[Fraction(x, r[d]) for x in r[:d]] for r in rays]
    if not verts:
        return [], []
    lo = [ceil(min(v[i] for v in verts)) for i in range(d)]
    hi = [floor(max(v[i] for v in verts)) for i in range(d)]
    size = 1
    for a, b in zip(lo, hi):
        size *= max(0, b - a + 1)
    if size > BOX_LIMIT:
        raise ValueError(f'{size} lattice points to scan: too many')
    pts = [u for u in product(*(range(a, b + 1) for a, b in zip(lo, hi)))
           if all(sum(x * y for x, y in zip(g, u)) + hh >= 0
                  for g, hh in zip(G, h))]
    return pts, []


# ------------------------------------------------------------------ strata
class _Geometry:
    """Fan data in coordinates t on H_2 (beta = sum_j t_j h2_basis[j])."""

    def __init__(self, X, rows, mori):
        self.X = X
        self.fan = fan = X.fan
        self.rows = rows
        self.r = len(rows)
        self.dimZ = X.n - len(rows)
        self.rank = fan.k - fan.n
        basis = fan.h2_basis
        # a_rho as a functional of t
        self.coord = [tuple(v[i] for v in basis) for i in range(fan.k)]
        L = [1 - sum(a[i] for a in rows) for i in range(fan.k)]
        self.L = self.functional(L)
        self.mori = [self.functional(N) for N in mori]
        self.euler = [X.divisor(a) for a in rows]
        amp = fan.ample_divisor()
        self.omega = X.one * 0
        for i, c in enumerate(amp):
            if c:
                self.omega = self.omega + c * X.x(i)
        self._alive = {}

    def functional(self, divisor):
        return tuple(sum(divisor[i] * self.coord[i][j]
                         for i in range(self.fan.k))
                     for j in range(self.rank))

    def beta(self, t):
        basis = self.fan.h2_basis
        return tuple(sum(t[j] * basis[j][i] for j in range(self.rank))
                     for i in range(self.fan.k))

    def tcoords(self, beta):
        """Inverse of .beta (h2_basis is a Z-basis of H_2)."""
        rows = [list(self.coord[i]) + [beta[i]] for i in range(self.fan.k)]
        ns = _nullspace(rows, self.rank + 1)
        assert len(ns) == 1 and ns[0][-1] != 0
        t = [-x / ns[0][-1] for x in ns[0][:-1]]
        assert all(x.denominator == 1 for x in t)
        return tuple(int(x) for x in t)

    def stratum_class(self, sigma):
        cls = self.X.one
        for i in sorted(sigma):
            cls = cls * self.X.x(i)
        return cls

    def alive(self, sigma):
        """Z cap V(sigma) is nonempty."""
        hit = self._alive.get(sigma)
        if hit is None:
            e = self.X.n - len(sigma) - self.r
            if e < 0:
                hit = False
            else:
                hit = self.X.integral(self.stratum_class(sigma), *self.euler,
                                      *([self.omega] * e)) != 0
            self._alive[sigma] = hit
        return hit

    def link(self, sigma):
        return [i for i in range(self.fan.k)
                if i not in sigma and sigma | {i} in self.fan.faces]


def _stratum_pieces(geo, sigma, stuck):
    """t-coordinates of the pieces of the stratum sigma (see module doc)."""
    fan, X = geo.fan, geo.X
    link = geo.link(sigma)
    eqs = [geo.coord[i] for i in range(fan.k)
           if i not in sigma and i not in link]
    ineqs = list(geo.mori)
    for i in link:
        if geo.alive(sigma | {i}):
            ineqs.append(geo.coord[i])
        else:
            eqs.append(geo.coord[i])
    # lattice of the solutions of the equalities
    if eqs:
        W = integer_kernel([list(e) for e in eqs])
    else:
        W = [tuple(1 if i == j else 0 for i in range(geo.rank))
             for j in range(geo.rank)]
    d = len(W)
    red = lambda f: tuple(sum(f[i] * w[i] for i in range(geo.rank)) for w in W)
    lift = lambda u: tuple(sum(u[j] * W[j][i] for j in range(d))
                           for i in range(geo.rank))
    A = [red(f) for f in ineqs]
    Lr = red(geo.L)
    top = geo.dimZ + 1
    curve = fan.n - len(sigma) - geo.r == 1
    if curve:
        base = geo.stratum_class(sigma)
        c = tuple(int(X.integral(X.x(i), base, *geo.euler))
                  for i in range(fan.k))
        tc = geo.tcoords(c)
        Lc = sum(a * b for a, b in zip(geo.L, tc))
        if Lc <= 0:
            raise ValueError(
                f'Z is not Fano: the curve Z cap V{tuple(sorted(sigma))} of '
                f'class {list(c)} has anticanonical degree {Lc}')
        if geo.r == 1 and X.integral(base, geo.euler[0], geo.euler[0]) > 0:
            return [tc] if Lc <= top else []       # irreducible (Bertini)
        # components: u and c - u in the cone
        ns = _nullspace([[w[i] for w in W] + [-tc[i]]
                         for i in range(geo.rank)], d + 1)
        sol = next((v for v in ns if v[-1] != 0), None)
        assert sol is not None, 'class of Z cap V outside its stratum'
        uc = [x / sol[-1] for x in sol[:-1]]
        G = A + [tuple(-x for x in a) for a in A]
        h = [0] * len(A) + [sum(a * b for a, b in zip(row, uc)) for row in A]
    else:
        G = list(A)
        h = [0] * len(A)
    G = G + [tuple(-x for x in Lr), Lr]
    h = h + [top, -1]
    # the L >= 1 row would hide the recession directions with L <= 0 of
    # the cone, so test positivity of L on the cone first
    if not curve:
        bad = [ray for ray in extreme_rays(A, d)
               if sum(a * b for a, b in zip(Lr, ray)) <= 0] if d else []
        if bad:
            stuck.extend((tuple(sorted(sigma)), geo.beta(lift(ray)))
                         for ray in bad)
            return []
    pts, rec = lattice_points(G, h, d)
    assert pts is not None, rec
    return [lift(u) for u in pts]


def _is_wall_sum(fan, beta, memo):
    """beta is a nonnegative integer combination of wall classes (only
    these have fixed loci in the localization sum)."""
    if not any(beta):
        return True
    hit = memo.get(beta)
    if hit is None:
        amp = fan.ample_divisor()
        hit = False
        if fan.wall_degree(amp, beta) > 0:
            for w in fan.wall_classes:
                rest = tuple(x - y for x, y in zip(beta, w))
                if fan.wall_degree(amp, rest) >= 0 and \
                        _is_wall_sum(fan, rest, memo):
                    hit = True
                    break
        memo[beta] = hit
    return hit


# -------------------------------------------------------------------- main
def _collect_pieces(geo):
    """(pieces, stuck, strata): the irreducible pieces of every stratum that
    meets Z in curves, the strata whose cone is unbounded in a direction
    where c1(Z) <= 0, and the strata themselves."""
    fan = geo.fan
    stuck, pieces = [], []
    strata = sorted((s for s in fan.faces
                     if fan.n - len(s) - geo.r >= 1 and geo.alive(s)),
                    key=lambda s: (len(s), sorted(s)))
    for sigma in strata:
        for t in _stratum_pieces(geo, sigma, stuck):
            pieces.append((sigma, geo.beta(t),
                           sum(a * b for a, b in zip(geo.L, t))))
    pieces = sorted(set(pieces), key=lambda p: (p[2], sorted(p[0]), p[1]))
    return pieces, stuck, strata


# ------------------------------------------- checking and guessing "mori"
def excluded_classes(X, K, mori, limit=6, max_omega=None):
    """Curve classes that pass the axioms of quantum.curve_class_report but
    are excluded by the inequalities, cheapest (smallest omega-degree)
    first.  These are exactly the classes whose invariants the inequalities
    claim to be zero."""
    from .ci import normalize_divisor
    from .quantum import _wall_sum_betas
    rows = X.check_K(K)
    N = [normalize_divisor(X, v) for v in mori]
    amp = X.fan.ample_divisor()
    unit = min(X.fan.wall_degree(amp, w) for w in X.fan.wall_classes)
    cut = max_omega if max_omega is not None else 2 * unit
    top = (X.n - len(rows) + 4) * unit if max_omega is None else max_omega
    out = []
    while cut <= top:
        found = []
        for b in _wall_sum_betas(X, rows, cut):
            if any(b) and any(X.fan.wall_degree(v, b) < 0 for v in N):
                found.append((X.fan.wall_degree(amp, b), b))
        out = [b for _, b in sorted(found)]
        if len(out) >= limit:
            break
        cut += unit
    return out[:limit]


def verify_mori(X, K, mori, limit=4, progress=None):
    """Sample check of the inequalities: compute the invariants of the
    cheapest curve classes they exclude and require them to vanish.  A
    failure means the inequalities are wrong (they remove a class that
    really contributes); passing is evidence, not a proof.  Returns
    {'checked': [...], 'failures': [(beta, pair, value), ...]}."""
    rows = X.check_K(K)
    dim = X.n - len(rows)
    log = progress or (lambda s: None)
    classes = X.classes
    degs = [c.degree() for c in classes]
    checked, failures = [], []
    for b in excluded_classes(X, K, mori, limit):
        cb = X.c1_degree(b, rows)
        pairs = [(i, j) for i in range(len(classes))
                 for j in range(i, len(classes))
                 if degs[i] + degs[j] == dim - 1 + cb]
        if not pairs:
            continue
        vals = X.gw_multi([(classes[i], classes[j]) for i, j in pairs], b, rows)
        bad = [(pairs[s], v) for s, v in enumerate(vals) if v]
        checked.append(list(b))
        for (i, j), v in bad:
            failures.append((list(b), (X.class_names[i], X.class_names[j]), v))
        log(f'excluded class {list(b)}: {len(pairs)} invariants, '
            + ('all zero' if not bad else f'{len(bad)} NONZERO'))
    return {'checked': checked, 'failures': failures}


def suggest_inequalities(X, K, progress=None, verify=3):
    """Try to derive the inequalities the stuck strata need.  For each
    unbounded direction B0 an LP looks for a divisor N with N . B0 <= -1
    and N . p >= 0 on every piece found in the strata that are not stuck
    (those are classes of curves that Z really contains, so a valid N must
    be nonnegative on them).  Each candidate is then checked by
    verify_mori; only the ones that survive are returned.

    The result is a guess supported by sampling, never a proof: use it to
    save work, not to certify an answer."""
    from .ci import normalize_divisor
    import sympy
    from sympy.solvers.simplex import lpmin
    rows = X.check_K(K)
    geo = _Geometry(X, rows, [])
    log = progress or (lambda s: None)
    pieces, stuck, _ = _collect_pieces(geo)
    if not stuck:
        return []
    good = sorted({geo.tcoords(b) for _, b, _ in pieces})
    out = []
    for sigma, b0 in stuck:
        t0 = geo.tcoords(b0)
        cs = sympy.symbols(f'c0:{2 * geo.rank}')       # N = c+ - c-
        coef = [cs[2 * j] - cs[2 * j + 1] for j in range(geo.rank)]
        cons = [sum(c * p for c, p in zip(coef, t)) >= 0 for t in good]
        cons.append(sum(c * p for c, p in zip(coef, t0)) <= -1)
        cons += [c >= 0 for c in cs]
        try:
            _, sol = lpmin(sum(cs), cons)
        except Exception as exc:                        # noqa: BLE001
            log(f'no inequality found for the stratum V{tuple(sorted(sigma))}'
                f' ({exc})')
            continue
        vals = [sympy.Rational(sol[c]) for c in cs]
        den = 1
        for v in vals:
            den = den * v.q // gcd(den, v.q)
        degs = [int((vals[2 * j] - vals[2 * j + 1]) * den)
                for j in range(geo.rank)]
        N = X.fan.divisor_with_degrees(degs)
        rep = verify_mori(X, K, [list(N)], verify, progress) if verify else \
            {'checked': [], 'failures': []}
        ok = not rep['failures']
        log(f'candidate inequality {list(N)} for V{tuple(sorted(sigma))}: '
            + ('verified on ' + str(len(rep['checked'])) + ' excluded classes'
               if ok else 'REJECTED, it excludes a class with a nonzero '
               'invariant'))
        if ok:
            out.append((tuple(sorted(sigma)), tuple(N), rep))
    return out


def fano_ci_classes(X, K, mori=None, progress=None):
    """Curve classes of X that can contribute to c1(TZ)* for the Fano
    complete intersection Z cut out by K (see the module doc).  mori: list
    of divisors that are nonnegative on every curve of Z.  Returns
    (betas, stats) with betas sorted by (L . beta, beta), 0 first; raises
    MoriStuck when L is not positive on the cone of some stratum."""
    from .ci import normalize_divisor
    rows = X.check_K(K)
    if not rows:
        raise ValueError('a toric variety itself is Fano only if c1 is '
                         'positive on every invariant curve')
    mori = [normalize_divisor(X, N) for N in (mori or [])]
    geo = _Geometry(X, rows, mori)
    fan = X.fan
    dim = geo.dimZ
    top = dim + 1
    log = progress or (lambda s: None)

    # pieces
    pieces, stuck, strata = _collect_pieces(geo)
    if stuck:
        raise MoriStuck(stuck)
    log(f'{len(strata)} strata of X meet Z in curves; {len(pieces)} '
        f'irreducible pieces with c1-degree <= {top}')

    # connected configurations
    P = len(pieces)

    # Incidence depends only on the stratum and which coordinates are >= 1,
    # not on the full curve class. Reuse identical rows instead of repeating
    # this test and allocating a separate length-P row for every piece.
    signatures=[(s,frozenset(rho for rho,v in enumerate(beta) if v>=1))
                for s,beta,_ in pieces]
    types=list(dict.fromkeys(signatures))
    type_index={signature:i for i,signature in enumerate(types)}
    indices=[type_index[sig] for sig in signatures]
    type_meet=[]
    for si,positive_i in types:
        type_meet.append([(si|sj in fan.faces and sj-si<=positive_i and si-sj<=positive_j)
                          for sj,positive_j in types])
    rows=[[row[j] for j in indices] for row in type_meet]
    meet=[rows[i] for i in indices]
    free = [not s and deg >= 2 for s, _, deg in pieces]
    flags = {}                                 # beta -> [any, one, two]

    def record(beta, nfree, big):
        f = flags.setdefault(beta, [False, False, False])
        f[0] = True
        f[1] = f[1] or nfree >= 1
        f[2] = f[2] or nfree >= 2 or big

    configs = {(i,) for i in range(P)}
    connected = True
    frontier = configs
    while frontier and connected:
        new = set()
        for cfg in frontier:
            deg = sum(pieces[i][2] for i in cfg)
            for j in range(P):
                if deg + pieces[j][2] > top:
                    break                      # pieces are sorted by degree
                if any(meet[i][j] for i in cfg):
                    nxt = tuple(sorted(cfg + (j,)))
                    if nxt not in configs:
                        new.add(nxt)
                        # Once the existing fallback threshold is exceeded,
                        # finishing this entire level only wastes memory/time.
                        if len(configs)+len(new)>CONFIG_LIMIT:
                            connected=False
                            break
            if not connected:
                break
        if not connected:
            break
        configs |= new
        frontier = new
        if len(configs) > CONFIG_LIMIT:
            connected = False
    if connected:
        for cfg in configs:
            beta = tuple(sum(pieces[i][1][rho] for i in cfg)
                         for rho in range(fan.k))
            record(beta, sum(free[i] for i in cfg),
                   any(not pieces[i][0] and pieces[i][2] >= top for i in cfg))
    else:
        log(f'more than {CONFIG_LIMIT} configurations: connectedness test '
            f'skipped')
        level = {0: {(0,) * fan.k: (0, False)}}
        for deg in range(1, top + 1):
            cur = {}
            for s, b, pd in pieces:
                for rest, (nf, big) in level.get(deg - pd, {}).items():
                    beta = tuple(x + y for x, y in zip(rest, b))
                    onf, obig = cur.get(beta, (0, False))
                    cur[beta] = (max(onf, nf + (not s and pd >= 2)),
                                 obig or big or (not s and pd >= top))
            level[deg] = cur
            for beta, (nf, big) in cur.items():
                record(beta, nf, big)

    # nef classes H, nontrivial on Z, for the two-point rule
    walls_t = [geo.tcoords(w) for w in fan.wall_classes]
    nef = []
    for s in extreme_rays(walls_t, geo.rank):
        # a divisor with H . h2_basis[j] = s_j
        ns = _nullspace([[fan.h2_basis[j][i] for i in range(fan.k)] + [-s[j]]
                         for j in range(geo.rank)], fan.k + 1)
        sol = next(v for v in ns if v[-1] != 0)
        H = X.one * 0
        for i in range(fan.k):
            if sol[i]:
                H = H + (sol[i] / sol[-1]) * X.x(i)
        if X.integral(H, *geo.euler, *([geo.omega] * (dim - 1))) != 0:
            nef.append(s)

    memo = {}
    betas = []
    dropped = 0
    for beta, (ok_any, ok_one, ok_two) in flags.items():
        t = geo.tcoords(beta)
        deg = sum(a * b for a, b in zip(geo.L, t))
        keep = ok_any and _is_wall_sum(fan, beta, memo)
        if keep and deg == dim:
            keep = ok_one
        elif keep and deg == top:
            keep = ok_two and all(sum(a * b for a, b in zip(s, t)) > 0
                                  for s in nef)
        if keep:
            betas.append((deg, beta))
        else:
            dropped += 1
    betas = [(0,) * fan.k] + [b for _, b in sorted(betas)]
    stats = {'strata': len(strata), 'pieces': len(pieces),
             'configurations': len(configs) if connected else None,
             'candidates': len(flags), 'dropped': dropped}
    log(f'{len(flags)} connected effective classes, {dropped} dropped by '
        f'the point-insertion rules: {len(betas) - 1} classes left')
    return betas, stats
