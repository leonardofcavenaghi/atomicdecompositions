"""Independent Gromov-Witten engine implementing Holmes-Muratore,
"Computations in equivariant Gromov-Witten theory of GKM spaces"
(arXiv:2509.07562), Theorem 3.4, specialized to genus 0.

This module deliberately re-derives the localization sum from the GKM
formulation rather than reusing gwflags.localization: fixed loci are
decorated trees mapping *into the GKM graph* (intrinsic edges — no
representative-dependent root labels), the edge factor h(e, d) uses the
compatible connection, and the vertex factor is the uniform

    alpha(v)^{val-1} * prod_i gamma_i|_v * prod_e alpha_{(e,v)}^{-1}
        * (sum_e alpha_{(e,v)}^{-1})^{n_v + val - 3}

(negative exponents allowed), which subsumes the KappaGamma/IVertex case
split of the classical engine.  Agreement of the two engines is a
formula-independent certification of both.

The GKM graph of a flag variety G/P is generated from gwflags root data
via the dictionary of the collaborators' draft (flagpart.pdf §2.5):
vertices = minimal coset representatives, flags at w = reduced roots
beta with axial weight -w(beta), edges w -> proj(w s_beta), connection
integers a_gamma = <gamma, beta^vee>, curve class of an edge = the
coroot of its root modulo the parabolic coroot lattice.
"""

from fractions import Fraction
from math import factorial

from .rootsystem import dot, matvec
from .trees import all_trees, all_possible_marks, ahu_canon

_FACT = [factorial(i) for i in range(64)]


class GKMGraph:
    """vertices 0..N-1; flags[v] = list of dicts with keys
    edge (edge id), weight (backend value), a (connection integers,
    parallel to flags[v] minus this flag), cls (curve-class tuple on the
    kept coordinates); edges[eid] = (v1, v2)."""

    def __init__(self, n_vertices):
        self.n = n_vertices
        self.flags = [[] for _ in range(n_vertices)]
        self.edges = []
        self.euler = [None] * n_vertices
        self.parallel_edges = []      # diagnostic: [(v, u, count)]

    def finalize(self):
        for v in range(self.n):
            e = 1
            for fl in self.flags[v]:
                e = e * fl['weight']
            self.euler[v] = e
        # diagnostic: parallel edges (several T-curves joining one pair)
        from collections import Counter
        for v in range(self.n):
            c = Counter(self.edges[fl['edge']][0] + self.edges[fl['edge']][1]
                        - v for fl in self.flags[v])
            for u, k in c.items():
                if k > 1 and v < u:
                    self.parallel_edges.append((v, u, k))


def gkm_graph_of_flag(rs, wd, bk):
    """Build the GKM graph of G/P from gwflags root data, with axial
    weights evaluated in the given backend (numeric or symbolic)."""
    reps = wd.reduced_group
    n = len(reps)
    step = wd.step_table()
    red = wd.reduced_root_indices
    kept = wd.roots_that_stay

    # linear form of an ort vector that is +- a positive root
    poly = {}
    for r, r_ort in zip(rs.positive_roots, rs.positive_roots_ort):
        p = bk.linear([Fraction(c) for c in r])
        poly[r_ort] = p
        poly[tuple(-x for x in r_ort)] = -p

    def weight(vi, q):
        """Axial weight of the flag (vertex vi, reduced root index q):
        -w(beta_q)."""
        return -poly[matvec(reps[vi], rs.positive_roots_ort[q])]

    g = GKMGraph(n)
    # curve class of the edge with root q: coroot restricted to kept coords
    cls_of = {q: tuple(rs.coroots[q][r - 1] for r in kept) for q in red}
    # pair flags into edges: (v, q) <-> (u, q') with matching data
    edge_id = {}
    for vi in range(n):
        for q in red:
            u = step[(vi, q)]
            if (vi, q) in edge_id:
                continue
            w_here = weight(vi, q)
            # find the unique flag at u pointing back with opposite weight
            partners = [q2 for q2 in red
                        if step[(u, q2)] == vi and weight(u, q2) == -w_here]
            assert partners, f'GKM pairing failed at ({vi},{q})'
            q2 = partners[0]
            assert cls_of[q] == cls_of[q2], \
                'edge class differs between endpoints'
            eid = len(g.edges)
            g.edges.append((vi, u))
            edge_id[(vi, q)] = eid
            edge_id[(u, q2)] = eid

    # flags with connection integers
    for vi in range(n):
        flist = []
        for q in red:
            b_ort = rs.positive_roots_ort[q]
            bb = dot(b_ort, b_ort)
            a = []
            for q2 in red:
                if q2 == q:
                    continue
                g_ort = rs.positive_roots_ort[q2]
                aval = Fraction(2 * dot(g_ort, b_ort), bb)
                assert aval.denominator == 1
                a.append(int(aval))
            flist.append({'edge': edge_id[(vi, q)], 'root': q,
                          'weight': weight(vi, q), 'a': a,
                          'cls': cls_of[q]})
        g.flags[vi] = flist
    g.finalize()
    return g


class GKMEngine:
    """Genus-0 Gromov-Witten invariants of a GKM space by the
    Holmes-Muratore Theorem 3.4 graph sum."""

    def __init__(self, graph, bk):
        self.g = graph
        self.bk = bk
        self._h_cache = {}

    # ------------------------------------------------------- edge factor
    def _b(self, u, w, a):
        """b(u, w, a): 1/e(H^0) for a >= 0, e(H^1) for a < 0."""
        if a >= 0:
            r = 1
            for j in range(0, a + 1):
                r = r / (w - j * u)
            return r
        r = 1
        for j in range(1, -a):
            r = r * (w + j * u)
        return r

    def h(self, flag_v, flag_idx, d):
        """h(e, d) computed from the flag (vertex flag_v, index flag_idx
        into flags[flag_v]).  Theorem 3.6: independent of which of the
        two flags of e is chosen (asserted in the test-suite)."""
        key = (flag_v, flag_idx, d)
        hit = self._h_cache.get(key)
        if hit is not None:
            return hit
        fl = self.g.flags[flag_v][flag_idx]
        aeps = fl['weight']
        pref = self.bk.rational(
            Fraction((-1) ** d * d ** (2 * d), _FACT[d] ** 2)) / aeps ** (2 * d)
        others = [f2 for i2, f2 in enumerate(self.g.flags[flag_v])
                  if i2 != flag_idx]
        u = aeps / d
        val = pref
        for f2, a in zip(others, fl['a']):
            val = val * self._b(u, f2['weight'], d * a)
        self._h_cache[key] = val
        return val

    # --------------------------------------------------------- the sum
    def gw(self, insertions, beta):
        """insertions: list over marks of vectors [restriction at vertex v
        for v in 0..N-1] (e.g. Billey values for Schubert classes);
        beta: tuple of the curve class on the kept coordinates.
        Returns the localization sum in the engine's backend."""
        bk, g = self.bk, self.g
        n_marks = len(insertions)
        total = 0
        deg_total = sum(beta)
        if deg_total == 0:
            raise ValueError('use the classical pairing for beta = 0')
        for edges, k in all_trees(deg_total + 1):
            total = total + self._tree_sum(edges, k, insertions, beta)
        return total

    def _tree_sum(self, edges, k, insertions, beta):
        g = self.g
        n_marks = len(insertions)
        # tree structure keyed by edge tuples (matches trees.ahu_canon)
        adj = {v: [] for v in range(1, k + 1)}
        for e in edges:
            adj[e[0]].append((e[1], e))
            adj[e[1]].append((e[0], e))
        order, seen, bfs = [1], {1}, []
        for v in order:
            for w, e in adj[v]:
                if w not in seen:
                    seen.add(w)
                    bfs.append((w, v, e))
                    order.append(w)

        marks_options = all_possible_marks(n_marks, k)
        seen_canon = set()
        acc = [0]
        vimg = {v: None for v in range(1, k + 1)}
        eimg = {}          # edge tuple -> (edge_id, d, parent_vertex, flag_idx)

        def emit():
            edeg = {e: (eimg[e][0], eimg[e][1]) for e in edges}
            for marks in marks_options:
                key, aut = ahu_canon(
                    k, adj, edeg, lambda v: (vimg[v], marks[v - 1]))
                if key in seen_canon:
                    continue
                seen_canon.add(key)
                acc[0] = acc[0] + self._one(edges, k, adj, vimg, eimg,
                                            marks, insertions, aut)

        def assign(idx, remaining):
            if idx == len(bfs):
                if not any(remaining):
                    emit()
                return
            child, parent, e = bfs[idx]
            pv = vimg[parent]
            for fi, fl in enumerate(g.flags[pv]):
                cls = fl['cls']
                dmax = min(r // c for r, c in zip(remaining, cls) if c)
                for d in range(1, dmax + 1):
                    new_rem = tuple(r - d * c
                                    for r, c in zip(remaining, cls))
                    far = g.edges[fl['edge']]
                    vimg[child] = far[0] + far[1] - pv
                    eimg[e] = (fl['edge'], d, pv, fi)
                    assign(idx + 1, new_rem)
            vimg[child] = None
            eimg.pop(e, None)

        for v0 in range(g.n):
            vimg[1] = v0
            assign(0, tuple(beta))
        return acc[0]

    def _one(self, edges, k, adj, vimg, eimg, marks, insertions, aut):
        bk, g = self.bk, self.g
        contrib = bk.rational(Fraction(1, aut))
        # edge factors h(e, d)/d
        for e in edges:
            eid, d, pv, fi = eimg[e]
            contrib = contrib * self.h(pv, fi, d) / d
        # vertex factors
        for v in range(1, k + 1):
            fv = vimg[v]
            val = len(adj[v])
            nmk = len(marks[v - 1])
            contrib = contrib * g.euler[fv] ** (val - 1)
            for m in marks[v - 1]:
                contrib = contrib * insertions[m - 1][fv]
            inv_alphas = []
            for w, e in adj[v]:
                eid, d, pv, fi = eimg[e]
                wt = g.flags[pv][fi]['weight']
                if pv != fv:                     # far end: opposite weight
                    wt = -wt
                inv_alphas.append(d / wt)
            s = 0
            for ia in inv_alphas:
                contrib = contrib * ia
                s = s + ia
            expo = nmk + val - 3
            if expo:
                contrib = contrib * s ** expo
        return contrib


# ----------------------------------------------------------- convenience
def gkm_gw(X, coh_classes, beta, backend=None):
    """GW invariant of the flag variety X (a FlagVariety) for Schubert
    classes (Weyl matrices) and curve class beta over the simple roots,
    computed by the Holmes-Muratore engine.  Returns the raw sum in the
    chosen backend (defaults to a fresh numeric backend)."""
    from .symbolic import NumericBackend
    from .localization import GWCalculator
    bk = backend or NumericBackend(seed=71)
    calc = GWCalculator(X.rs, None, bk, wd=X.wd)   # for Billey values only
    graph = gkm_graph_of_flag(X.rs, X.wd, bk)
    eng = GKMEngine(graph, bk)
    reps = X.wd.reduced_group
    insertions = [[calc.billey(c, w) for w in reps] for c in coh_classes]
    kept_beta = tuple(beta[r - 1] for r in X.wd.roots_that_stay)
    # beta must be supported on kept nodes for the GKM class bookkeeping
    assert all(b == 0 or (i + 1) in X.wd.roots_that_stay
               for i, b in enumerate(beta)), \
        'gkm_gw needs beta supported on the kept simple roots'
    return eng.gw(insertions, kept_beta)
