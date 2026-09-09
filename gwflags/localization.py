"""The Bott-localization core of V3.nb: ChangeToPolynom, Billey's formula
(`Bylleys`), edge factor (`OmegaLie`), Euler factor (`RFactor`),
`KappaGamma`, `IVertex` and the graph sum `GWInvariant`.

Everything symbolic goes through the backend (sympy or Sage); Weyl/roots
data comes from WeylData/RootSystemData.
"""

from fractions import Fraction
from itertools import combinations
from math import factorial

from .rootsystem import matmul, matvec, dot
from .symbolic import get_backend
from .trees import all_trees, decorated_trees
from .weyl import WeylData


class GWCalculator:
    """GW invariants of G/P for `algebra` (e.g. 'A2') and the kept simple
    roots `roots_that_stay` (1-based; the notebook's m)."""

    def __init__(self, rs, roots_that_stay, backend=None, wd=None):
        self.rs = rs
        self.wd = wd if wd is not None else WeylData(rs, roots_that_stay)
        self.bk = backend or get_backend()
        self._base_cache = {}     # id(decorated tree) -> base factor
        self._polyw_cache = {}    # (w, v_ort) -> ChangeToPolynom[w.v]
        self._edge_cache = {}     # (w, root_idx, d) -> edge weight

        # ChangeToPolynom lookup: ort vector of +-(positive root) -> +-poly
        bk = self.bk
        self._poly = {}
        self._poly_byll = {}
        for r, r_ort in zip(rs.positive_roots, rs.positive_roots_ort):
            p = bk.linear([Fraction(c) for c in r])
            inv = bk.rational(Fraction(0))
            for i, c in enumerate(r):
                if c != 0:
                    inv = inv + bk.rational(Fraction(c)) / bk.x(i + 1)
            neg = tuple(-x for x in r_ort)
            self._poly[r_ort] = p
            self._poly[neg] = -p
            self._poly_byll[r_ort] = p
            self._poly_byll[neg] = inv    # InvertVariables branch
        self._rfactor_cache = {}
        self._billey_cache = {}

    def __getstate__(self):
        """Drop caches on pickling: id(dt)-keyed entries are meaningless in
        another process (address reuse would silently alias), and the rest
        is cheap to rebuild."""
        state = dict(self.__dict__)
        for key in ('_base_cache', '_polyw_cache', '_rfactor_cache',
                    '_billey_cache', '_ci_twist_cache', '_euler_cache',
                    '_mu_cache', '_omega_ort_cache', '_bdeg_cache',
                    '_edge_cache'):
            state.pop(key, None)
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self._base_cache = {}
        self._polyw_cache = {}
        self._rfactor_cache = {}
        self._billey_cache = {}
        self._edge_cache = {}

    # ------------------------------------------------------------ polynomials
    def poly(self, v_ort):
        """ChangeToPolynom of an ort vector (must be +-a positive root)."""
        return self._poly[v_ort]

    def poly_byll(self, v_ort):
        """ChangeToPolynomByll (negative roots get inverted variables)."""
        return self._poly_byll[v_ort]

    def poly_w(self, w, v_ort):
        """ChangeToPolynom[w . v], cached — the localization formulas hit
        the same (Weyl element, root) pairs relentlessly."""
        key = (w, v_ort)
        hit = self._polyw_cache.get(key)
        if hit is None:
            hit = self._polyw_cache[key] = self.poly(matvec(w, v_ort))
        return hit

    # ------------------------------------------------------------- R factor
    def rfactor(self, w):
        """Local Euler factor prod_{beta in R+ \\ R+_P} (-x_{w.beta})."""
        if w not in self._rfactor_cache:
            r = 1
            for b_ort in self.wd.reduced_roots_ort:
                r = r * (-self.poly_w(w, b_ort))
            self._rfactor_cache[w] = r
        return self._rfactor_cache[w]

    # ------------------------------------------------------ Billey's formula
    def billey(self, shubert, vertex):
        """Restriction of the equivariant Schubert class sigma_shubert to
        the fixed point `vertex` (both are Weyl matrices)."""
        key = (shubert, vertex)
        if key in self._billey_cache:
            return self._billey_cache[key]
        wd, rs = self.wd, self.rs
        if shubert == wd.group[0]:
            res = 1
        else:
            vword = wd.word_of[vertex]
            sword = wd.word_of[shubert]
            if len(vword) < len(sword):
                res = 0
            else:
                # beta_i = s_{w_1}...s_{w_{i-1}} . alpha_{w_i}
                betas = []
                si = wd.group[0]
                for idx in vword:
                    b_ort = matvec(si, rs.positive_roots_ort[
                        rs.positive_roots.index(
                            tuple(1 if j == idx - 1 else 0
                                  for j in range(rs.rank)))])
                    betas.append(self.poly_byll(b_ort))
                    si = matmul(si, rs.reflection_matrices[idx - 1])
                res = 0
                for sub in combinations(range(len(vword)), len(sword)):
                    prod_m = wd.group[0]
                    for i in sub:
                        prod_m = matmul(prod_m,
                                        rs.reflection_matrices[vword[i] - 1])
                    if prod_m == shubert:
                        term = 1
                        for i in sub:
                            term = term * betas[i]
                        res = res + term
        self._billey_cache[key] = res
        return res

    # ------------------------------------------------------------ edge factor
    def edge_factor(self, w, root_idx, d):
        """R(w) * R(proj(w.s_alpha)) * OmegaLie(w, alpha, d): the full
        class-independent weight of one child edge in KappaGamma.  Cached by
        content — the same (vertex, root, degree) triples recur across
        thousands of decorated trees."""
        key = (w, root_idx, d)
        hit = self._edge_cache.get(key)
        if hit is None:
            root = self.rs.positive_roots[root_idx]
            w2 = self.wd.project(matmul(w, self.wd.reflection_of_root[root]))
            hit = (self.rfactor(w) * self.rfactor(w2)
                   * self.omega_lie(w, root_idx, d))
            self._edge_cache[key] = hit
        return hit

    def omega_lie(self, w, root_idx, d):
        """OmegaLie: the h-function of an edge leaving vertex w with root
        alpha = positive_roots[root_idx] and degree d."""
        bk, rs, wd = self.bk, self.rs, self.wd
        alpha = rs.positive_roots[root_idx]
        a_ort = rs.positive_roots_ort[root_idx]
        aa = dot(a_ort, a_ort)
        posiproduct = 1
        for beta, b_ort in zip(wd.reduced_roots, wd.reduced_roots_ort):
            if beta == alpha:
                continue
            ip = Fraction(2 * dot(a_ort, b_ort), aa)  # <beta, alpha^vee>
            val = d * ip
            assert val.denominator == 1
            val = int(val)
            if val <= -2:
                for j in range(1, -val):
                    posiproduct = posiproduct * (
                        -(self.poly_w(w, b_ort)
                          + bk.rational(Fraction(j, d)) * self.poly_w(w, a_ort)))
            elif val >= 0:
                for k in range(0, val + 1):
                    posiproduct = posiproduct / (
                        -(self.poly_w(w, b_ort)
                          - bk.rational(Fraction(k, d)) * self.poly_w(w, a_ort)))
            # val == -1: factor 1
        const = bk.rational(
            Fraction((-1) ** d * d ** (2 * d), factorial(d) ** 2))
        return const * self.poly_w(w, a_ort) ** (-2 * d) * posiproduct

    # --------------------------------------------------------- KappaGamma
    def kappa_gamma(self, dt):
        """KappaGamma of a decorated tree (its table is derived here)."""
        bk, wd, rs = self.bk, self.wd, self.rs
        first = second = third = degree_term = 1
        table = dt.table()
        for v, (w, parent_label, children, marks) in enumerate(table, start=1):
            first = first / self.rfactor(w)
            for (ridx, d) in children:
                second = second * self.edge_factor(w, ridx, d)
                degree_term = degree_term * bk.rational(Fraction(1, d))
            edges_in = ([parent_label] if parent_label else []) + children
            if len(children) == 1 and parent_label is None and not marks:
                ridx, d = edges_in[0]
                third = third * (-bk.rational(Fraction(1, d))
                                 * self.poly_w(w, rs.positive_roots_ort[ridx]))
            elif parent_label is not None and not children and not marks:
                ridx, d = edges_in[0]
                wpar = dt.parent_w(v)
                third = third * (bk.rational(Fraction(1, d))
                                 * self.poly_w(wpar, rs.positive_roots_ort[ridx]))
            elif len(children) == 2 and parent_label is None and not marks:
                (r1, d1), (r2, d2) = edges_in
                third = third * (-1 / (
                    bk.rational(Fraction(1, d1))
                    * self.poly_w(w, rs.positive_roots_ort[r1])
                    + bk.rational(Fraction(1, d2))
                    * self.poly_w(w, rs.positive_roots_ort[r2])))
            elif (parent_label is not None and len(children) == 1
                  and not marks):
                (rp, dp), (rc, dc) = edges_in
                wpar = dt.parent_w(v)
                third = third * (-1 / (
                    -bk.rational(Fraction(1, dp))
                    * self.poly_w(wpar, rs.positive_roots_ort[rp])
                    + bk.rational(Fraction(1, dc))
                    * self.poly_w(w, rs.positive_roots_ort[rc])))
        return degree_term * first * second * third

    # ------------------------------------------------------------- IVertex
    def i_vertex(self, dt, v):
        """IVertex: moduli-integral factor of a vertex with
        valence + #marks >= 3."""
        bk, rs = self.bk, self.rs
        w, parent_label, children, marks = dt.table()[v - 1]
        incident = ([parent_label] if parent_label else []) + children
        terms = []
        for i, (ridx, d) in enumerate(incident):
            if parent_label is not None and i == 0:
                val = (bk.rational(Fraction(1, d))
                       * self.poly_w(dt.parent_w(v),
                                     rs.positive_roots_ort[ridx]))
            else:
                val = (bk.rational(Fraction(1, d))
                       * (-self.poly_w(w, rs.positive_roots_ort[ridx])))
            terms.append(1 / val)
        first = 1
        for u in terms:
            first = first * u
        second = 0
        for u in terms:
            second = second + u
        expo = len(incident) + len(marks) - 3
        return first * second ** expo

    # ------------------------------------------------- per-decoration base
    def dec_base(self, dt):
        """Class-independent part of a decorated tree's contribution:
        (1/Aut) * KappaGamma * prod IVertex, plus the Weyl element carrying
        each mark.  Cached by id(dt): only valid for decorations retained
        by wd.decoration_cache (which pins the objects); streamed transient
        decorations must use dec_base_nocache instead."""
        hit = self._base_cache.get(id(dt))
        if hit is not None:
            return hit
        base = self.dec_base_nocache(dt)
        self._base_cache[id(dt)] = base
        return base

    def dec_base_nocache(self, dt):
        """dec_base without the id-keyed cache — for transient decorations
        from iter_decorated_trees, where id() reuse after garbage
        collection would silently alias cache entries."""
        bk = self.bk
        table = dt.table()
        aut = dt.automorphism_group_size()
        third = 1
        for v, (w, pl, ch, marks) in enumerate(table, start=1):
            if (1 if pl else 0) + len(ch) + len(marks) >= 3:
                third = third * self.i_vertex(dt, v)
        return bk.cancel(bk.rational(Fraction(1, aut))
                         * self.kappa_gamma(dt) * third)

    @staticmethod
    def mark_carriers(dt):
        """Weyl element carrying each mark of a decorated tree."""
        cached = getattr(dt, '_mark_ws', None)
        if cached is None:
            nmarks = sum(len(m) for m in dt.vmarks.values())
            ws = [None] * nmarks
            for v in range(1, dt.n + 1):
                for k in dt.vmarks[v]:
                    ws[k - 1] = dt.vw[v]
            cached = dt._mark_ws = tuple(ws)
        return cached

    # --------------------------------------------------------- GW invariant
    def gw_invariant(self, coh_classes, beta, progress=None, extra=None):
        """GWInvariant: equivariant localization sum.  coh_classes is a list
        of Weyl matrices (Schubert classes), beta a tuple over simple roots.
        With the symbolic backend this returns the raw sum (use
        .bk.evaluate_gw for the number); with the numeric backend it returns
        an exact Fraction (see FlagVariety.gw for the degree gate).

        extra(dt) -> factor: optional class-independent multiplier per
        decorated tree (used for the complete-intersection twist)."""
        bk, wd = self.bk, self.wd
        if sum(beta) == 0:
            total = 0
            for s in wd.reduced_group:
                term = 1 / self.rfactor(s)
                for c in coh_classes:
                    term = term * self.billey(c, s)
                if extra is not None:
                    term = term * extra(s)
                total = total + term
            return total
        total = 0
        trees = all_trees(sum(beta) + 1)
        for ti, tree in enumerate(trees):
            decs = decorated_trees(tree, beta, len(coh_classes), wd)
            if progress:
                progress(f'tree {ti + 1}/{len(trees)}: {len(decs)} decorations')
            for dt in decs:
                byll = 1
                mark_ws = self.mark_carriers(dt)
                for k, c in enumerate(coh_classes):
                    byll = byll * self.billey(c, mark_ws[k])
                    if bk.is_zero(byll):
                        break
                if bk.is_zero(byll):
                    continue
                term = self.dec_base(dt) * byll
                if extra is not None:
                    term = term * extra(dt)
                total = total + bk.cancel(term)
        return total

    # ------------------------------------------------------------ shortcuts
    def class_of_word(self, word):
        """Weyl matrix for a word of 1-based simple-reflection indices."""
        m = self.wd.group[0]
        for i in word:
            m = matmul(m, self.rs.reflection_matrices[i - 1])
        return m

    def point_class(self):
        """The longest minimal coset representative (the point class)."""
        return max(self.wd.reduced_group, key=self.wd.length)
