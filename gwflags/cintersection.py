"""Complete-intersection sector: localization twisted by the Euler class
of a bundle E.

Historically this implemented V3.nb's split-line-bundle formulas
(mu, EulerCompleteIntersection, hCompleteIntersection,
OmegaCompleteIntersection, GWCOMPLETEINTERSECTION).  It now operates on
arbitrary fiber-weight multisets (gwflags.bundles.HomogeneousBundle);
a legacy K = [[a, b], ...] list of rows is converted on entry, each row
becoming the single weight -sum_m a_m omega_{i_m}, which reproduces the
original formulas exactly.

Twisted ingredients per fixed point w and weight mu:
    vertex:  value(w.mu)                       (product over mu = e(E_w))
    edge (root beta, degree d), with b = -<mu, beta^vee> >= 0 (convexity):
             prod_{i=0}^{b d} ( value(w.mu) + (i/d) P(w.beta) )
Concave summands (b < 0) are not supported: the genus-0 twisted theory
requires curve-wise global generation, which FlagVariety validates.
"""

from fractions import Fraction

from .rootsystem import dot, matvec
from .bundles import HomogeneousBundle, WeightEvaluator, _omega_ort


# ----------------------------------------------------------- normalization
def as_weights(gw, K):
    """Normalize a bundle spec to a tuple of fiber-weight ort vectors.
    Accepts a HomogeneousBundle or the legacy list of integer rows."""
    if isinstance(K, HomogeneousBundle):
        return K.weights
    cache = gw.__dict__.setdefault('_legacy_weight_cache', {})
    kkey = tuple(tuple(r) for r in K)
    hit = cache.get(kkey)
    if hit is None:
        rs, kept = gw.rs, gw.wd.roots_that_stay
        ws = []
        for row in K:
            v = tuple(Fraction(0) for _ in range(rs.dim_ort))
            for am, r in zip(row, kept):
                if am:
                    om = _omega_ort(rs, r)
                    v = tuple(x - am * y for x, y in zip(v, om))
            ws.append(v)
        hit = cache[kkey] = tuple(ws)
    return hit


def ci_rank(K):
    """Rank of the twisting bundle (codimension of the intersection)."""
    if isinstance(K, HomogeneousBundle):
        return K.rank
    return len(K)


def _evaluator(gw):
    ev = gw.__dict__.get('_weight_evaluator')
    if ev is None:
        ev = gw._weight_evaluator = WeightEvaluator(gw.rs, gw.bk)
    return ev


def _wvalue(gw, w, mu):
    """value(w.mu), cached."""
    cache = gw.__dict__.setdefault('_wvalue_cache', {})
    key = (w, mu)
    hit = cache.get(key)
    if hit is None:
        hit = cache[key] = _evaluator(gw).value(matvec(w, mu))
    return hit


# ------------------------------------------------------------- ingredients
def euler_complete_intersection(gw, K, w):
    """e(E) at the fixed point w (cached)."""
    weights = as_weights(gw, K)
    cache = gw.__dict__.setdefault('_euler_cache', {})
    hit = cache.get((w, weights))
    if hit is not None:
        return hit
    e = 1
    for mu in weights:
        e = e * _wvalue(gw, w, mu)
    e = gw.bk.cancel(e)
    cache[(w, weights)] = e
    return e


def _splitting_degree(gw, mu, root_idx):
    rs = gw.rs
    b_ort = rs.positive_roots_ort[root_idx]
    v = -Fraction(2 * dot(mu, b_ort), dot(b_ort, b_ort))
    assert v.denominator == 1, 'non-integral splitting degree'
    return int(v)


def h_complete_intersection(gw, K, w, root_idx, d):
    """Edge factor e(H^0(f^*E)) for an edge leaving w with root beta and
    degree d (cached by content)."""
    weights = as_weights(gw, K)
    cache = gw.__dict__.setdefault('_hci_cache', {})
    ckey = (w, root_idx, d, weights)
    hit = cache.get(ckey)
    if hit is not None:
        return hit
    bk = gw.bk
    pw = gw.poly_w(w, gw.rs.positive_roots_ort[root_idx])
    result = 1
    for mu in weights:
        b = _splitting_degree(gw, mu, root_idx)
        if b < 0:
            raise NotImplementedError(
                f'concave summand (splitting degree {b} < 0) — the '
                f'twisted genus-0 theory needs curve-wise global '
                f'generation')
        mval = _wvalue(gw, w, mu)
        prod = 1
        for i in range(0, b * d + 1):
            prod = prod * (mval + bk.rational(Fraction(i, d)) * pw)
        result = result * prod
    cache[ckey] = result
    return result


def omega_complete_intersection(gw, K, dt):
    """Twist factor of a decorated tree (vertex^{1-valence} x edges)."""
    first = second = 1
    for v, (w, parent_label, children, marks) in enumerate(dt.table(), 1):
        n_incident = (1 if parent_label else 0) + len(children)
        second = second * euler_complete_intersection(gw, K, w) ** (1 - n_incident)
        for (ridx, d) in children:
            first = first * h_complete_intersection(gw, K, w, ridx, d)
    return first * second


def gw_complete_intersection(gw, coh_classes, beta, K, progress=None):
    """The twisted localization sum, via GWCalculator.gw_invariant's
    `extra` hook so all class-independent caching applies."""
    weights = as_weights(gw, K)
    if sum(beta) == 0:
        return gw.gw_invariant(coh_classes, beta, progress,
                               extra=lambda s: euler_complete_intersection(gw, K, s))
    cache = gw.__dict__.setdefault('_ci_twist_cache', {})

    def extra(dt):
        hit = cache.get((id(dt), weights))
        if hit is None:
            hit = omega_complete_intersection(gw, K, dt)
            cache[(id(dt), weights)] = hit
        return hit

    return gw.gw_invariant(coh_classes, beta, progress, extra=extra)
