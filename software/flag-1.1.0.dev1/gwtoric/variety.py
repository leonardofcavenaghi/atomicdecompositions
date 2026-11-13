"""High-level interface: a smooth projective toric variety from its fan,
its cohomology ring, and genus-0 Gromov-Witten invariants by torus
localization.

Conventions
-----------
* rays rho_0..rho_{k-1} in Z^n, maximal cones as 0-based index sets;
* x_i = class of the toric divisor D_{rho_i}; c_1(TX) = sum_i x_i;
* H_2(X, Z) = { a in Z^k : sum_i a_i rho_i = 0 }, with  int_beta x_i = a_i;
  a curve class is given either as such a vector of length k or by its
  coordinates in the Z-basis ToricVariety.h2_basis (length k - n);
* the quantum variable y_j is attached to the j-th element x_{b_j} of the
  chosen H^2 basis, q^beta = prod_j y_j^{int_beta x_{b_j}}.

Every GW number is gated by the dimension axiom and then evaluated exactly
(fractions.Fraction) at two independent random points of the equivariant
torus, as in gwflags: the gated localization sum is a constant, so one
evaluation is the invariant and the second guards against accidental
poles.  Non-convex targets are fine: the edge factor of the engine is the
virtual-localization one (H^1 terms enter for negative splitting degrees).
"""

from fractions import Fraction
from itertools import combinations
from math import gcd

from gwflags.symbolic import NumericBackend

from .fan import Fan
from .ring import CohClass, CohomologyRing
from .engine import ToricGKMEngine


class ToricVariety:
    def __init__(self, rays, max_cones, seed=0):
        self.fan = Fan(rays, max_cones)
        self.ring = CohomologyRing(self.fan)
        self.n = self.fan.n
        self.k = self.fan.k
        self._seed = seed
        self._engines = None
        # optional callable; while it returns True every graph sum stops
        # with engine.Cancelled (the GUI's Stop button)
        self.cancel = None

    def __repr__(self):
        return (f'<ToricVariety: dim {self.n}, {self.k} rays, '
                f'{len(self.fan.max_cones)} fixed points, '
                f'Picard rank {self.k - self.n}>')

    # ------------------------------------------------------------ classes
    def x(self, i):
        """Class of the toric divisor D_{rho_i}."""
        if not 0 <= i < self.k:
            raise ValueError(f'ray index {i} out of range 0..{self.k - 1}')
        return CohClass(self, {(i,): Fraction(1)})

    divisor = x

    @property
    def one(self):
        return CohClass(self, {(): Fraction(1)})

    @property
    def c1(self):
        """First Chern class sum_i x_i (anticanonical class)."""
        return CohClass(self, {(i,): Fraction(1) for i in range(self.k)})

    def point_class(self, cone=None):
        """Class of the fixed point of a maximal cone (default: the first)."""
        c = self.fan.max_cones[0] if cone is None else tuple(sorted(cone))
        if c not in self.fan.cone_index:
            raise ValueError(f'{c} is not a maximal cone')
        return CohClass(self, {tuple(c): Fraction(1)})

    @property
    def pt(self):
        return self.point_class()

    @property
    def classes(self):
        """Graded basis of H^*(X, Q): monomials in the H^2 basis."""
        return [self.ring.y_to_class(self, d, e)
                for d, e in self.ring.graded_basis]

    @property
    def class_names(self):
        return [repr(c) for c in self.classes]

    @property
    def h2_generators(self):
        """Ray indices of the chosen basis of H^2 (Picard generators)."""
        return list(self.ring.basis_vars)

    @property
    def betti(self):
        return list(self.ring.betti)

    def hodge_report(self, K=None):
        """Exact Hodge data, Betti numbers b_0,...,b_{2dim}, and Euler number.

        With K: smooth ample Fano complete intersections of dimension 3-5; requires
        every defining divisor and -K_Y-sum K ample on the ambient. Other
        CI cases raise HodgeNotSupported. With no K: the ambient toric variety.
        """
        from .hodge import hodge_report
        return hodge_report(self, K)

    def chern_numbers(self, K=None):
        """Exact Chern numbers of a smooth nef CI (or ambient) of dimension 3-5.

        These numbers alone need not determine the Hodge diamond when K is
        not ample. Smoothness of a particular defining equation is assumed.
        """
        from .hodge import chern_numbers
        return chern_numbers(self, K)

    def hodge_diamond(self, K=None):
        """Matrix h[p][q], for the ambient or a supported CI specified by K."""
        return self.hodge_report(K)['hodge']

    def hodge_diamond_str(self, K=None):
        """Printable diamond; accepts the same K and hypotheses as hodge_report."""
        return self.hodge_report(K)['diamond']

    def coordinates(self, cls):
        """Coordinates of a class in .classes (dict index -> Fraction)."""
        return self.ring.coordinates(cls)

    def reduce(self, cls):
        """Normal form of a class in the basis .classes."""
        basis = self.classes
        out = self.one * 0
        for i, c in self.coordinates(cls).items():
            out = out + c * basis[i]
        return out

    @property
    def dimension(self):
        return self.n

    # ------------------------------------------------------------- curves
    @property
    def h2_basis(self):
        """Z-basis of H_2(X, Z) as vectors in Z^k."""
        return list(self.fan.h2_basis)

    @property
    def wall_curves(self):
        """[(wall rays, class vector)] for all torus-invariant curves."""
        return [(w['tau'], w['cls']) for w in self.fan.walls]

    @property
    def is_fano(self):
        return self.fan.is_fano()

    def beta(self, b):
        """Normalize a curve class to a vector in Z^k (see module doc)."""
        b = tuple(int(v) for v in b)
        r = self.k - self.n
        if len(b) == self.k:
            if not self.fan.in_h2(b):
                raise ValueError(
                    f'{b} is not a curve class: sum a_i rho_i != 0')
            return b
        if len(b) == r:
            out = [0] * self.k
            for coef, vec in zip(b, self.fan.h2_basis):
                for i in range(self.k):
                    out[i] += coef * vec[i]
            return tuple(out)
        raise ValueError(
            f'a curve class needs {self.k} entries (one per ray) or {r} '
            f'coordinates in h2_basis; got {len(b)}')

    def c1_degree(self, beta, K=None):
        """c1 . beta, of X or (with K) of the complete intersection Z:
        c1(Z) = c1(X) - sum_m D_m restricted."""
        b = self.beta(beta)
        deg = sum(b)
        for a in self.check_K(K):
            deg -= self.fan.wall_degree(a, b)
        return deg

    @property
    def novikov_divisors(self):
        """Ray coefficients of the divisors A_1, ..., A_r whose degrees are
        the Novikov exponents:  q^beta = prod_j y_j^{A_j . beta}.  A nef
        Z-basis of Pic X when the nef cone contains one, so that the
        exponents are >= 0 on every effective class; otherwise (no lattice
        basis of nef classes) the H^2 basis rays x_{b_j}, and then negative
        exponents can occur."""
        nef = self.fan.nef_basis()
        if nef is None:
            return [tuple(1 if i == j else 0 for i in range(self.k))
                    for j in self.ring.basis_vars]
        return nef

    def novikov_exponents(self, beta):
        b = self.beta(beta)
        return [self.fan.wall_degree(a, b) for a in self.novikov_divisors]

    # ------------------------------------------------ complete intersections
    def divisor(self, a):
        """CohClass of the divisor sum a_i D_i (k entries, or coordinates
        on the H^2 basis rays)."""
        from .ci import normalize_divisor
        cls = self.one * 0
        for i, c in enumerate(normalize_divisor(self, a)):
            if c:
                cls = cls + c * self.x(i)
        return cls

    def check_K(self, K):
        """Normalize a complete-intersection spec (list of nef divisors)
        to ray-coefficient tuples; [] for no twist."""
        from .ci import check_K
        return check_K(self, K)

    def c1_ci(self, K=None):
        """c1 of X or, with K, of the complete intersection Z (as a class
        of X; restrict to Z)."""
        cls = self.c1
        for a in self.check_K(K):
            cls = cls - self.divisor(a)
        return cls

    def fano_index(self, K=None):
        """Fano index: the largest r with -K = r A for a divisor class A
        of X, i.e. the gcd of the degrees c1 . beta over a Z-basis of
        H_2(X, Z) (Pic X = Hom(H_2(X, Z), Z) for a smooth complete toric
        variety).  With K it is the divisibility of
        -K_Z = (-K_X - sum_m D_m)|_Z in the image of Pic X; this is the
        Fano index of Z when Pic Z = Pic X, which holds for a complete
        intersection of ample divisors of dimension >= 3 (Lefschetz).  A
        surface or a curve can have a larger Picard group, and then a
        different index.  Meaningful when the variety is Fano, which is
        not checked for a complete intersection."""
        rows = self.check_K(K)
        r = 0
        for v in self.fan.h2_basis:
            r = gcd(r, abs(self.c1_degree(v, rows)))
        return r

    def anticanonical_generator(self, K=None):
        """(r, A): the Fano index r = fano_index(K) and ray coefficients
        of a divisor A with -K = r A in Pic X (restricted to Z with K).
        A is the representative supported away from the first maximal
        cone; the rays outside a maximal cone give a Z-basis of Pic X."""
        rows = self.check_K(K)
        r = self.fano_index(rows)
        L = [1 - sum(a[i] for a in rows) for i in range(self.k)]
        if r == 0:
            return 0, tuple([0] * self.k)
        cone = self.fan.max_cones[0]
        dual = self.fan.dual[0]
        m = [sum(L[i] * dual[i][t] for i in cone) for t in range(self.n)]
        rep = [L[i] - sum(m[t] * self.fan.rays[i][t] for t in range(self.n))
               for i in range(self.k)]
        assert all(v % r == 0 for v in rep), 'anticanonical class not divisible'
        return r, tuple(v // r for v in rep)

    def is_fano_ci(self, K=None):
        """c1(Z) positive on every invariant curve of X.  Sufficient but
        not necessary for Z to be Fano (whether Z is Fano cannot be read
        off the fan), so this only decides how the curve classes of c1*
        are listed; see curve_class_report."""
        rows = self.check_K(K)
        return all(sum(w) - sum(self.fan.wall_degree(a, w) for a in rows) > 0
                   for w in self.fan.wall_classes)

    def expected_degree(self, beta, n_classes, K=None):
        """Codimension sum the dimension axiom requires (for the complete
        intersection cut out by K when given)."""
        b = self.beta(beta)
        rows = self.check_K(K)
        dim = self.n - len(rows)
        if not any(b):
            return dim
        return dim + self.c1_degree(b, rows) + n_classes - 3

    # ------------------------------------------------------------ engines
    def __getstate__(self):
        state = dict(self.__dict__)
        state['_engines'] = None
        return state

    def _engine_pair(self, fresh=False):
        if self._engines is None or fresh:
            if fresh:
                self._seed += 2
            self._engines = tuple(
                ToricGKMEngine(self.fan, NumericBackend(self._seed + t))
                for t in (0, 1))
        for eng in self._engines:
            eng.cancel = self.cancel
        return self._engines

    def _two_point(self, func):
        """Evaluate func(engine) on two independent random points, retry
        with fresh points on disagreement or accidental poles."""
        count=getattr(self,'evaluation_count',2)
        if count not in (1,2):raise ValueError('evaluation_count must be 1 or 2')
        for attempt in range(3):
            try:
                vals = []
                for evaluation, eng in enumerate(self._engine_pair(fresh=attempt > 0)[:count], 1):
                    eng.evaluation_attempt = attempt + 1
                    eng.evaluation_pass = evaluation
                    vals.append(func(eng))
                if count==1 or vals[0] == vals[1]:
                    return vals[0]
            except ZeroDivisionError:
                pass
        raise ArithmeticError('numeric evaluations disagree - please report')

    # ---------------------------------------------------------- integrals
    def integral(self, *classes):
        """int_X of the product of the given classes (exact Fraction)."""
        prod = self.one
        for c in classes:
            prod = prod * c
        parts = prod.homogeneous_parts()
        top = parts.get(self.n)
        if top is None:
            return Fraction(0)
        return self._two_point(
            lambda eng: eng.classical([eng.restrict(top)]))

    def gw(self, classes, beta, K=None, progress=None):
        """Genus-0 GW invariant <classes>_{0, beta} as an exact Fraction.
        classes: list of homogeneous CohClass; beta: curve class.
        K: optional complete intersection (list of nef divisors, each as
        ray coefficients); the invariant is then the one of the zero
        locus Z with the classes restricted to Z, summed over the curve
        classes of Z mapping to beta (quantum Lefschetz)."""
        return self.gw_multi([tuple(classes)], beta, K, progress)[0]

    def gw_multi(self, class_tuples, beta, K=None, progress=None):
        """Several invariants with the same number of insertions and the
        same beta, sharing one enumeration of the fixed loci."""
        b = self.beta(beta)
        rows = self.check_K(K)
        sizes = {len(t) for t in class_tuples}
        if len(sizes) != 1:
            raise ValueError('all tuples need the same number of classes')
        n_cl = sizes.pop()
        out = [Fraction(0)] * len(class_tuples)
        expected = self.expected_degree(b, n_cl, rows)
        active = []
        for s, t in enumerate(class_tuples):
            if sum(c.degree() for c in t) == expected:
                active.append(s)
        if not active:
            return out
        if not any(b):
            if n_cl != 3:
                return out
            euler = [self.divisor(a) for a in rows]
            for s in active:
                out[s] = self.integral(*class_tuples[s], *euler)
            return out

        from .progress import ClassProgress
        reporter = ClassProgress.create(b, progress)

        def run(eng):
            from .ci import twist_for
            sets = [tuple(eng.restrict(c) for c in class_tuples[s])
                    for s in active]
            twist = twist_for(eng, rows) if rows else None
            previous = getattr(eng, 'progress', None)
            eng.progress = reporter
            try:
                from .degree_bound import degree_bound, localization_divisor, reuse_degree_checkpoints
                divisor = localization_divisor(self, rows, b)
                with degree_bound(eng, divisor):
                    if getattr(self, 'tree_parallel', None):
                        from .tree_parallel import parallel_sum
                        if divisor is not None:
                            reuse_degree_checkpoints(eng, sets, b, twist, self.tree_parallel, parallel_sum)
                        return parallel_sum(eng, sets, b, twist, self.tree_parallel)
                    return eng.gw_multi(sets, b, twist)
            finally:
                eng.progress = previous

        try:
            vals = self._two_point(run)
        except Exception:
            if reporter:
                reporter.emit(force=True, stage='class_failed')
            raise
        if reporter:
            reporter.emit(force=True, stage='class_complete')
        for s, v in zip(active, vals):
            out[s] = v
        if progress:
            progress(f'beta {b}: {len(active)} invariants')
        return out

    # ----------------------------------------------------------- quantum
    def fano_index_and_betas(self, K=None, max_degree=None, mori=None):
        """See quantum.betas_and_fano_index: 0 and the sums of wall curves
        with 3 - dim <= c1 . beta <= dim + 1, c1 . beta != 0.  When some
        wall curve has c1-degree <= 0: the exact list of gwtoric.mori for
        a complete intersection (assumed Fano; mori = divisors that are
        >= 0 on the curves of Z), else a cutoff at ample degree
        max_degree."""
        from .quantum import betas_and_fano_index
        return betas_and_fano_index(self, K, max_degree, mori)

    def curve_class_report(self, K=None, max_degree=None, mori=None,
                           progress=None, auto_mori=True, verify=3):
        """The classes of fano_index_and_betas together with how they
        were found (mode 'positive', 'mori', 'mori-auto' or 'cutoff'), the
        strata where an inequality is still needed, the inequalities
        derived automatically, and the sample check of the inequalities
        used; see quantum.curve_class_report."""
        from .quantum import curve_class_report
        return curve_class_report(self, K, max_degree, mori, progress,
                                  auto_mori, verify)

    def verify_mori(self, K=None, mori=None, limit=4, progress=None):
        """Sample check of Mori cone inequalities: the invariants of the
        cheapest curve classes they exclude must all vanish; see
        gwtoric.mori.verify_mori."""
        from .mori import verify_mori
        return verify_mori(self, K, mori or [], limit, progress)

    def suggest_mori(self, K=None, progress=None, verify=3):
        """Inequalities derived for the stuck strata and checked by
        sampling; see gwtoric.mori.suggest_inequalities."""
        from .mori import suggest_inequalities
        return suggest_inequalities(self, K, progress, verify)

    def nonpositive_curves(self, K=None):
        """Wall-curve classes with c1-degree <= 0 (when there are any,
        fano_index_and_betas is a truncation)."""
        from .quantum import nonpositive_curves
        return nonpositive_curves(self, K)

    def default_max_degree(self, K=None):
        """Default ample-degree cutoff of fano_index_and_betas (None when
        no cutoff is needed)."""
        from .quantum import default_max_degree
        return default_max_degree(self, K)

    def small_quantum_multiplication(self, betas=None, K=None, progress=None,
                                     max_degree=None, mori=None,
                                     workers=None, cache=True, cancel=None):
        """Matrix of c1(TX)* on H^*(X) in the basis .classes, the grading
        operator and the basis names.  Entries carry the quantum variables
        y_j (Novikov exponents int_beta x_{b_j}).  betas defaults to
        fano_index_and_betas(K, max_degree)[1].

        With K (a complete intersection Z): the matrix of c1(TZ)* on the
        ambient part i^*H^*(X) of H^*(Z), in the sub-basis of .classes
        whose names are returned (classes vanishing on Z, or pairing to
        zero with every ambient class, are dropped).  Curve classes and
        Novikov variables are those of X.

        workers: processes over which the curve classes are spread (an
        int, or 'auto'); cache: keep slow classes on disk
        (quantum.cache_dir())."""
        from .quantum import small_quantum_multiplication, betas_and_fano_index
        if betas is None:
            _, betas = betas_and_fano_index(self, K, max_degree, mori)
        return small_quantum_multiplication(self, betas, K, progress,
                                            workers, cache, cancel)

    def c1_grading(self, K=None):
        """Degrees c_j of the Novikov variables (c1 = sum c_j A_j over
        A_j = novikov_divisors); with deg y_j = c_j the matrix of c1* is
        homogeneous and q^beta has degree c1 . beta.  See
        quantum.c1_grading."""
        from .quantum import c1_grading
        return c1_grading(self, K)

    def specialize_c1(self, M, K=None, var='t'):
        """The matrix with y_j -> t^{c_j}, i.e. q^beta -> t^{c1 . beta}:
        one variable, graded by the anticanonical degree.  Identifies all
        the curve classes of the same c1-degree, so it is faithful only
        when finitely many of them contribute.  See
        quantum.specialize_c1."""
        from .quantum import specialize_c1
        return specialize_c1(self, M, K, var)

    def eigenvalues(self, M, at_one=False):
        import sympy
        Ms = sympy.Matrix([[sympy.sympify(v) for v in row] for row in M])
        if at_one:
            Ms = Ms.subs({s: 1 for s in Ms.free_symbols})
        out = []
        for val, mult in Ms.eigenvals().items():
            out.extend([sympy.simplify(val)] * mult)
        return out

    # ------------------------------------- the quantum connection / exponents
    def quantum_connection(self, K=None, **kw):
        """(K^F, G, names): the formal disk connection
        d/du + K^F/u^2 + G/u at a point of the one-parameter small locus,
        with K^F = -c1* and G the grading operator.  See
        gwtoric.connection."""
        from .connection import disk_connection
        return disk_connection(self, K, **kw)

    def rationality_invariants(self, K=None, **kw):
        """Rank and regularized exponent multiset of every generic Hodge
        factor of the quantum connection, and the obstruction to
        rationality of Theorem 4.5 of Carazolli-Cavenaghi-Katzarkov-
        Kontsevich-Martins.  Pass very_general=True for an even-dimensional
        complete intersection (the paper's hypothesis (18));
        gwtoric.connection.report renders the result."""
        from .connection import invariants
        return invariants(self, K, **kw)

    # ------------------------------------------------------ constructions
    def product(self, other):
        f = self.fan.product(other.fan)
        return ToricVariety(f.rays, f.max_cones)

    def blowup(self, cone_rays):
        """Blow-up along the orbit closure of the cone spanned by the
        given rays (a maximal cone = a fixed point)."""
        f = self.fan.star_subdivision(cone_rays)
        return ToricVariety(f.rays, f.max_cones)

    def projective_bundle(self, summands):
        """The projective bundle P(E) -> X of the split bundle
        E = O(D_0) + ... + O(D_r) (Cox-Little-Schenck Prop. 7.3.3, see
        Fan.projective_bundle).  Each summand is a divisor given by its k
        ray coefficients, by k - n coordinates on the H^2 basis rays
        X.h2_generators, or -- when the Picard rank is 1 -- by a single
        integer; P(E) = P(E ox L), so only the differences D_i - D_0 and
        only their classes matter.

        The rays 0..k-1 of X keep their index, with D_i pulling back to
        D_i, and the r + 1 fiber rays e_1, ..., e_r, e_0 are appended.

            projective_space(1).projective_bundle([0, a])  # = hirzebruch(a)
            P2 = projective_space(2)
            P2.projective_bundle([0, 0, 0]) # = P2.product(projective_space(2))
        """
        from .ci import normalize_divisor
        rows = [normalize_divisor(self, (a,) if isinstance(a, int) else a)
                for a in summands]
        f = self.fan.projective_bundle(rows)
        return ToricVariety(f.rays, f.max_cones)


# ------------------------------------------------------------- constructors
def projective_space(n):
    rays = [tuple(1 if j == i else 0 for j in range(n)) for i in range(n)]
    rays.append(tuple([-1] * n))
    cones = list(combinations(range(n + 1), n))
    return ToricVariety(rays, cones)


def hirzebruch(a):
    """F_a = P(O + O(a)) over P^1."""
    rays = [(1, 0), (0, 1), (-1, a), (0, -1)]
    cones = [(0, 1), (1, 2), (2, 3), (3, 0)]
    return ToricVariety(rays, cones)


def product_of_projective_spaces(*ns):
    X = projective_space(ns[0])
    for m in ns[1:]:
        X = X.product(projective_space(m))
    return X


def projective_bundle_over_projective_space(s, twists):
    """P(O(a_0) + ... + O(a_r)) over P^s for twists = (a_0, ..., a_r), with
    O(a) = O(a D_0) and D_0 the divisor of the ray -e_1 - ... - e_s (the
    last ray of projective_space(s)).  This is Cox-Little-Schenck
    Example 7.3.5: the minimal generators come out as

        v_0 = u_0 + (a_1 - a_0) e_1 + ... + (a_r - a_0) e_r,
        v_j = u_j (j = 1..s),        e_1, ..., e_r, e_0 = -sum e_i,

    the maximal cones are Cone(v_0,..,^v_j,..,v_s) + Cone(e_0,..,^e_i,..,e_r),
    and P(E) is a smooth projective (s + r)-fold with Pic = Z^2.  Kleinschmidt
    classified the smooth projective toric varieties of Picard rank 2: they
    are exactly these.  Up to the twist P(E) = P(E ox L) one may take
    a_0 = 0; hirzebruch(a) is the case s = r = 1 (up to the order of the
    two fiber rays)."""
    X = projective_space(s)
    last = X.k - 1
    rows = [tuple(int(a) if i == last else 0 for i in range(X.k))
            for a in twists]
    return X.projective_bundle(rows)


def del_pezzo_6():
    """P^2 blown up at the three fixed points (hexagon fan)."""
    rays = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]
    cones = [(i, (i + 1) % 6) for i in range(6)]
    return ToricVariety(rays, cones)
