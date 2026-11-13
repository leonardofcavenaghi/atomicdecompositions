"""Complete intersections in a toric variety: localization twisted by the
Euler class of E = O(D_1) + ... + O(D_r)  (quantum Lefschetz, the toric
counterpart of gwflags.cintersection).

Each hypersurface is a torus-invariant divisor D = sum_i a_i D_i, given by
its k ray coefficients (or by k - n coordinates on the H^2 basis rays).
Genus-0 quantum Lefschetz needs every O(D) convex, i.e. globally
generated, which on a toric variety means D nef: D . C >= 0 on every wall
curve C (checked on entry; concave summands are refused, as in gwflags).
A generic section of such a bundle is smooth by Bertini, and the
invariants of the zero locus Z with insertions pulled back from X are

    <i^* g_1, ..., i^* g_m>^Z_{beta'} summed over beta' -> beta
        = int_{[M(X, beta)]^vir} e(E_{0,m,beta}) prod ev_a^* g_a,

with E_{0,m,beta} = R^0 pi_* f^* E.  On a fixed locus (graph Gamma) its
equivariant Euler class factors as

    prod_edges e(H^0(C_e, f^* E)) * prod_vertices e(E_{p_v})^{1 - val(v)},

where val counts incident edges only.  Ingredients per line bundle O(D)
(section 5 of the toric notes):
  * fiber weight at the fixed point of sigma: w_sigma(D) = sum_{i in sigma}
    a_i m_i, the restriction of the equivariant divisor class (the engine's
    lift);
  * on the wall curve C between sigma and sigma' with tangent weight t at
    sigma the lifts satisfy  w_sigma'(D) = w_sigma(D) - (D . C) t,  so a
    degree-d cover of C has H^0(f^* O(D)) with weights
        w_sigma(D) - (j / d) t,   j = 0, ..., (D . C) d.
The linearization is shifted by a generic constant per summand (a change
of linearization does not affect the non-equivariant answer, but it keeps
all vertex weights away from zero so no 0/0 appears in the graph sum).
"""

from fractions import Fraction


# ----------------------------------------------------------- normalization
def normalize_divisor(X, a):
    """Ray coefficients (length k) of a divisor given by k entries or by
    k - n coordinates on the H^2 basis rays X.h2_generators."""
    a = [int(v) for v in a]
    r = X.k - X.n
    if len(a) == X.k:
        return tuple(a)
    if len(a) == r:
        out = [0] * X.k
        for coef, ray in zip(a, X.h2_generators):
            out[ray] += coef
        return tuple(out)
    raise ValueError(
        f'a divisor needs {X.k} ray coefficients or {r} coordinates on '
        f'the H^2 basis rays {X.h2_generators}; got {len(a)}')


def check_K(X, K):
    """Validate a complete-intersection spec: list of divisors, each nef and
    nontrivial.  Returns a list of ray-coefficient tuples (possibly empty)."""
    if K is None:
        return []
    if isinstance(K, (tuple, list)) and K and not isinstance(K[0], (tuple, list)):
        K = [K]                                        # a single divisor
    rows = [normalize_divisor(X, a) for a in K]
    walls = X.fan.wall_classes
    for a in rows:
        degs = [X.fan.wall_degree(a, w) for w in walls]
        bad = [(w, d) for w, d in zip(walls, degs) if d < 0]
        if bad:
            w, d = bad[0]
            raise ValueError(
                f'divisor {list(a)} is not nef: degree {d} on the invariant '
                f'curve of class {list(w)} - genus-0 quantum Lefschetz '
                f'needs every hypersurface globally generated (convex)')
        if not any(degs):
            raise ValueError(f'divisor {list(a)} is trivial (degree 0 on '
                             f'every invariant curve)')
    return rows


# ------------------------------------------------------------------ twist
class LineBundleTwist:
    """Per-engine cache of the Euler-class ingredients of a split bundle
    sum_m O(D_m) evaluated in the engine's numeric backend."""

    def __init__(self, engine, rows):
        self.eng = engine
        self.rows = [tuple(r) for r in rows]
        bk = engine.bk
        fan = engine.fan
        # generic linearization shift per summand (see module doc)
        self.shift = [bk.x(10 ** 6 + 7 * m + 1) for m in range(len(rows))]
        # fiber weights at every fixed point, one list per summand
        self.w = []
        for m, a in enumerate(self.rows):
            wm = []
            for vi, c in enumerate(fan.max_cones):
                val = self.shift[m]
                for i in c:
                    if a[i]:
                        val = val + bk.rational(Fraction(a[i])) * engine.lift[(vi, i)]
                wm.append(val)
            self.w.append(wm)
        self.deg = [{eid: fan.wall_degree(a, cls)
                     for eid, cls in engine.edge_cls.items()}
                    for a in self.rows]
        self._vertex = {}
        self._edge = {}

    def vertex(self, vi):
        """e(E) at the fixed point vi."""
        hit = self._vertex.get(vi)
        if hit is None:
            hit = 1
            for wm in self.w:
                hit = hit * wm[vi]
            self._vertex[vi] = hit
        return hit

    def edge(self, pv, fi, d):
        """e(H^0(C, f^* E)) for the degree-d cover of the edge of flag fi
        at the fixed point pv."""
        key = (pv, fi, d)
        hit = self._edge.get(key)
        if hit is None:
            fl = self.eng.g.flags[pv][fi]
            t = fl['weight']
            eid = fl['edge']
            bk = self.eng.bk
            hit = 1
            for m in range(len(self.rows)):
                b = self.deg[m][eid]
                w0 = self.w[m][pv]
                for j in range(b * d + 1):
                    hit = hit * (w0 - bk.rational(Fraction(j, d)) * t)
            self._edge[key] = hit
        return hit


def twist_for(engine, rows):
    """Cached LineBundleTwist of the given (normalized) rows on an engine."""
    cache = engine.__dict__.setdefault('_twists', {})
    key = tuple(tuple(r) for r in rows)
    hit = cache.get(key)
    if hit is None:
        hit = cache[key] = LineBundleTwist(engine, rows)
    return hit
