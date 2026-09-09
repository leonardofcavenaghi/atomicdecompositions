"""Homogeneous vector bundles on flag varieties by T-weight multisets.

A completely reducible homogeneous bundle E on X = G/P is described, for
all localization purposes, by the multiset of T-weights of its fiber at
the base point eP (each weight given as a vector in the orthogonal
realization of the ambient root/weight space; type-A epsilon vectors are
fine — characters of the semisimple torus are read modulo the
W-invariant complement of the root span, which the evaluation projects
out).  The Weyl action transports the multiset to every fixed point; the
pairing <mu, beta^vee> gives the Birkhoff-Grothendieck splitting degrees
on invariant curves.

Conventions are anchored to the existing split-line-bundle code:
O_X(a_1,...,a_k) has the single fiber weight  mu = -sum_m a_m omega_{i_m},
so its localized weight at w is P(w.mu) = the engine's mu().  With this,
    det S* = det Q = O(1)   on Gr(k, n),
and the classical identifications hold (verified in the test-suite via
Z(Gr(2,4), Q) = P^2, Z(Gr(2,5), Q) = P^3, Z(Gr(2,5), Sym^2 S*) = OG(2,5)).

Constructors: O(X, *a), taut_sub(X, node), taut_quot(X, node), dual(E),
osum(E1, E2, ...), tensor(E1, E2) (also box products across factors),
sym(p, E), wedge(p, E).
"""

from fractions import Fraction
from itertools import combinations, combinations_with_replacement

from .rootsystem import dot, mat_inverse, vadd, vscale


class HomogeneousBundle:
    """weights: tuple of ort-space vectors (tuples of Fractions/ints) —
    the fiber weights at the base point."""

    def __init__(self, X, weights, name='E'):
        self.X = X
        self.weights = tuple(tuple(w) for w in weights)
        self.name = name

    @property
    def rank(self):
        return len(self.weights)

    def key(self):
        """Hashable cache key."""
        return self.weights

    def __repr__(self):
        return f'<{self.name}: rank {self.rank} on {self.X.rs.name}>'

    # ------------------------------------------------------- derived data
    def c1_coordinates(self):
        """c1(E) in the Schubert-divisor basis over the kept nodes:
        c1(E)_m = -<sum weights, alpha_{i_m}^vee>."""
        rs, kept = self.X.rs, self.X.wd.roots_that_stay
        total = None
        for w in self.weights:
            total = w if total is None else vadd(total, w)
        out = []
        for r in kept:
            a = rs.simple_roots_ort[r - 1]
            v = -Fraction(2 * dot(total, a), dot(a, a))
            assert v.denominator == 1, 'c1(E) not integral on kept nodes'
            out.append(int(v))
        return out

    def splitting_degrees(self, root_idx):
        """Birkhoff-Grothendieck degrees b_mu = -<mu, beta^vee> of E on
        the primitive invariant curve with root beta = root[root_idx]."""
        rs = self.X.rs
        b_ort = rs.positive_roots_ort[root_idx]
        bb = dot(b_ort, b_ort)
        out = []
        for mu in self.weights:
            v = -Fraction(2 * dot(mu, b_ort), bb)
            assert v.denominator == 1, 'non-integral splitting degree'
            out.append(int(v))
        return out

    def reduced_weights(self):
        """Canonical form of the weight multiset: each weight projected
        onto the root span (the torus-trivial W-invariant complement —
        e.g. the trace direction in type A — carries no character data),
        sorted.  Two presentations of the same bundle agree here."""
        rs = self.X.rs
        n = rs.rank
        gram = tuple(tuple(dot(rs.simple_roots_ort[i], rs.simple_roots_ort[j])
                           for j in range(n)) for i in range(n))
        ginv = mat_inverse(gram)
        out = []
        for w in self.weights:
            b = [dot(w, rs.simple_roots_ort[i]) for i in range(n)]
            c = [sum(ginv[i][j] * b[j] for j in range(n)) for i in range(n)]
            v = tuple(Fraction(0) for _ in range(rs.dim_ort))
            for ci, a in zip(c, rs.simple_roots_ort):
                v = vadd(v, vscale(ci, a))
            out.append(tuple(Fraction(x) for x in v))
        return tuple(sorted(out))

    def is_curvewise_convex(self):
        """True iff f*E is globally generated on every invariant curve
        (all splitting degrees >= 0) — the hypothesis the genus-0
        twisted theory needs."""
        return all(b >= 0
                   for q in self.X.wd.reduced_root_indices
                   for b in self.splitting_degrees(q))


# ----------------------------------------------------------- constructors
def _omega_ort(rs, node):
    """Fundamental weight omega_node in ort coordinates (via the inverse
    Cartan matrix: omega_r = sum_j (A^-1)^T[j][r] alpha_j)."""
    v = tuple(Fraction(0) for _ in range(rs.dim_ort))
    for j in range(rs.rank):
        c = rs.cart_matrix[j][node - 1]
        if c:
            v = vadd(v, vscale(c, rs.simple_roots_ort[j]))
    return v


def O(X, *a, name=None):
    """O_X(a_1, ..., a_k) over the kept nodes (roots_that_stay order):
    single fiber weight -sum a_m omega_{i_m}."""
    kept = X.wd.roots_that_stay
    if len(a) != len(kept):
        raise ValueError(f'O() needs {len(kept)} entries, got {len(a)}')
    v = tuple(Fraction(0) for _ in range(X.rs.dim_ort))
    for am, r in zip(a, kept):
        if am:
            v = vadd(v, vscale(-am, _omega_ort(X.rs, r)))
    return HomogeneousBundle(X, [v], name or f'O{a}')


def _type_a_factor(X, node):
    """(factor_start_node, factor_rank+1, offset in ort space) of the
    type-A factor containing the given global node."""
    start_node, off = 1, 0
    for fam, rank in X.rs.factors:
        dim = rank + 1 if fam == 'A' else None
        if fam != 'A':
            if start_node <= node < start_node + rank:
                raise ValueError('tautological bundles: type A factors only')
            start_node += rank
            off += {'A': rank + 1, 'B': rank, 'C': rank, 'D': rank,
                    'G': 3, 'F': 4, 'E': 8}[fam]
            continue
        if start_node <= node < start_node + rank:
            return start_node, rank + 1, off
        start_node += rank
        off += dim
    raise ValueError(f'node {node} not found')


def _eps(X, off, i, n_amb):
    """epsilon_i (1-based within the factor) as an ort vector."""
    return tuple(Fraction(1) if j == off + i - 1 else Fraction(0)
                 for j in range(X.rs.dim_ort))


def taut_sub(X, node, name=None):
    """Tautological subbundle S_k at the kept node (k = node -
    factor_start + 1 steps): fiber weights eps_1..eps_k.  NOT globally
    generated — use dual(taut_sub(...)) = S* for twists."""
    start, n_amb, off = _type_a_factor(X, node)
    k = node - start + 1
    ws = [_eps(X, off, i, n_amb) for i in range(1, k + 1)]
    return HomogeneousBundle(X, ws, name or f'S({node})')


def taut_quot(X, node, name=None):
    """Tautological quotient Q_k at the kept node: fiber weights
    eps_{k+1}..eps_n.  Globally generated."""
    start, n_amb, off = _type_a_factor(X, node)
    k = node - start + 1
    ws = [_eps(X, off, i, n_amb) for i in range(k + 1, n_amb + 1)]
    return HomogeneousBundle(X, ws, name or f'Q({node})')


def dual(E, name=None):
    return HomogeneousBundle(
        E.X, [tuple(-x for x in w) for w in E.weights],
        name or f'({E.name})^*')


def osum(*Es, name=None):
    X = Es[0].X
    ws = [w for E in Es for w in E.weights]
    return HomogeneousBundle(X, ws,
                             name or '+'.join(E.name for E in Es))


def tensor(E1, E2, name=None):
    """Tensor product; for bundles pulled back from different factors of
    a product this is the box product."""
    ws = [vadd(w1, w2) for w1 in E1.weights for w2 in E2.weights]
    return HomogeneousBundle(E1.X, ws,
                             name or f'{E1.name}(x){E2.name}')


def sym(p, E, name=None):
    ws = []
    for comb in combinations_with_replacement(range(E.rank), p):
        v = tuple(Fraction(0) for _ in range(E.X.rs.dim_ort))
        for i in comb:
            v = vadd(v, E.weights[i])
        ws.append(v)
    return HomogeneousBundle(E.X, ws, name or f'Sym^{p}{E.name}')


def wedge(p, E, name=None):
    ws = []
    for comb in combinations(range(E.rank), p):
        v = tuple(Fraction(0) for _ in range(E.X.rs.dim_ort))
        for i in comb:
            v = vadd(v, E.weights[i])
        ws.append(v)
    return HomogeneousBundle(E.X, ws, name or f'L^{p}{E.name}')


# ------------------------------------------------ weight-value evaluation
class WeightEvaluator:
    """P(w . mu) for arbitrary weights mu: expands the projection of an
    ort vector onto the root span in the simple-root basis and evaluates
    against the backend's x-variables.  Agrees with the root-only poly
    table on roots; extends it to epsilon/omega vectors (the projection
    kills the torus-trivial W-invariant directions)."""

    def __init__(self, rs, bk):
        self.rs = rs
        self.bk = bk
        n = rs.rank
        gram = tuple(tuple(dot(rs.simple_roots_ort[i],
                               rs.simple_roots_ort[j])
                           for j in range(n)) for i in range(n))
        self._gram_inv = mat_inverse(gram)
        self._cache = {}

    def value(self, v_ort):
        v_ort = tuple(v_ort)
        hit = self._cache.get(v_ort)
        if hit is None:
            n = self.rs.rank
            b = [dot(v_ort, self.rs.simple_roots_ort[i]) for i in range(n)]
            coeffs = [sum(self._gram_inv[i][j] * b[j] for j in range(n))
                      for i in range(n)]
            hit = self.bk.linear([Fraction(c) for c in coeffs])
            self._cache[v_ort] = hit
        return hit
