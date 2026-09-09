"""gwflags — Python/SageMath translation of V3.nb.

Gromov–Witten invariants of flag varieties G/P (including semisimple
products like 'A3xA3' for P^3 x P^3) via Bott localization, complete
intersections therein, and the small quantum multiplication matrix
c1(TX)* with its eigenvalues.

Fast path: every GW number is gated by the dimension axiom and then the
localization sum is evaluated exactly (fractions.Fraction) at two
independent random points of the equivariant torus — the gated sum is a
constant, so the evaluation IS the invariant, and agreement of the two
points guards against accidental poles.  No CAS in the hot loops; sympy
(or Sage) only assembles the final quantum matrices and eigenvalues.

Quick start::

    from gwflags import FlagVariety

    X = FlagVariety('A2', [1])          # P^2
    X.gw([X.pt, X.pt], beta=(1, 0))     # Fraction(1, 1)

    M, Gr, idx = X.small_quantum_multiplication()
    X.eigenvalues(M)
"""

from fractions import Fraction

from .rootsystem import RootSystemData, matmul, mat_inverse
from .weyl import WeylData
from .localization import GWCalculator
from .cintersection import gw_complete_intersection
from .symbolic import get_backend, NumericBackend
from .quantum import (metric_matrix, reduce_matrix, betas_and_fano_index,
                      small_quantum_multiplication, chern_class_vector,
                      chern_class_ci)
from .bundles import (HomogeneousBundle, O, taut_sub, taut_quot, dual,
                      osum, tensor, sym, wedge)


class FlagVariety:
    """High-level interface: fast numeric evaluation by default, symbolic
    calculators on demand (`.sym` / `.gw_raw`)."""

    def __init__(self, algebra, roots_that_stay, backend=None, seed=0):
        self.rs = RootSystemData(algebra)
        keep = list(roots_that_stay)
        if not keep or len(set(keep)) != len(keep) or \
                any(not isinstance(r, int) or r < 1 or r > self.rs.rank
                    for r in keep):
            raise ValueError(
                f'roots_that_stay must be distinct 1-based simple-root '
                f'indices within 1..{self.rs.rank}; got {roots_that_stay!r}')
        self.wd = WeylData(self.rs, keep)
        self._backend_pref = backend
        self._seed = seed
        self._sym = None
        self._numeric = None

    # ------------------------------------------------------- input checks
    def _check_K(self, K):
        """Validate the twisting bundle.  Legacy K = list of integer rows
        (one entry per kept simple root, in roots_that_stay order, all
        >= 0); alternatively a bundles.HomogeneousBundle, which must be
        curve-wise convex (globally generated on every invariant curve).
        Guards against silently reinterpreted input (e.g. a single row
        [2,2,2] on a Picard-rank-1 space is NOT three quadrics)."""
        if not K:
            return []
        from .bundles import HomogeneousBundle
        if isinstance(K, HomogeneousBundle):
            if K.X.wd is not self.wd:
                raise ValueError('bundle was built on a different flag')
            if not K.is_curvewise_convex():
                raise ValueError(
                    f'bundle {K.name} is not globally generated on every '
                    f'invariant curve (a splitting degree is negative); '
                    f'the genus-0 twisted theory requires convexity — for '
                    f'tautological subbundles use the dual S* instead of S')
            return K
        npic = len(self.wd.roots_that_stay)
        for row in K:
            if len(row) != npic:
                hint = ''
                if npic == 1 and len(row) > 1:
                    sep = ';'.join(str(v) for v in row)
                    hint = (f'  For {len(row)} separate line-bundle summands '
                            f'write them as separate rows, e.g. -K "{sep}" '
                            f'on the command line.')
                raise ValueError(
                    f'bundle row {list(row)} has {len(row)} '
                    f'{"entry" if len(row) == 1 else "entries"} but the '
                    f'flag has {npic} kept simple '
                    f'{"root" if npic == 1 else "roots"} (Picard '
                    f'generators); each row needs exactly {npic} '
                    f'{"entry" if npic == 1 else "entries"}, in '
                    f'roots_that_stay order.{hint}')
            if any(not isinstance(v, int) or v < 0 for v in row):
                raise ValueError(
                    f'bundle row {list(row)} has a negative or non-integer '
                    f'entry; only nef summands (entries >= 0) are supported '
                    f'(convexity of the twisted theory requires it).')
        return [list(r) for r in K]

    def _check_beta(self, beta):
        beta = tuple(beta)
        if len(beta) != self.rs.rank or \
                any(not isinstance(v, int) or v < 0 for v in beta):
            raise ValueError(
                f'beta must have one nonnegative integer per simple root '
                f'({self.rs.rank} entries for this algebra); got {beta!r}')
        return beta

    def __getstate__(self):
        """Pickle without calculators: workers rebuild them fresh (empty
        caches, own random points) — avoids unpicklable backend state and
        id-keyed cache aliasing across processes.  The shared decoration
        cache on WeylData travels along, which is safe (content-keyed) and
        saves regeneration."""
        state = dict(self.__dict__)
        state['_sym'] = None
        state['_numeric'] = None
        return state

    # ------------------------------------------------------- calculators
    @property
    def sym(self):
        """Symbolic calculator (sympy, or Sage inside SageMath)."""
        if self._sym is None:
            self._sym = GWCalculator(self.rs, None,
                                     get_backend(self._backend_pref),
                                     wd=self.wd)
        return self._sym

    @property
    def bk(self):
        return self.sym.bk

    def _numeric_pair(self, fresh=False):
        if self._numeric is None or fresh:
            if fresh:
                self._seed += 2
            self._numeric = tuple(
                GWCalculator(self.rs, None, NumericBackend(self._seed + k),
                             wd=self.wd)
                for k in (0, 1))
        return self._numeric

    # ------------------------------------------------------------ classes
    @property
    def classes(self):
        """Schubert basis: minimal coset representatives (Weyl matrices)."""
        return list(self.wd.reduced_group)

    @property
    def pt(self):
        return max(self.wd.reduced_group, key=self.wd.length)

    def class_of_word(self, word):
        m = self.wd.group[0]
        for i in word:
            m = matmul(m, self.rs.reflection_matrices[i - 1])
        return m

    def schubert(self, word):
        """Schubert class from a word of 1-based simple reflections,
        projected to its minimal coset representative."""
        return self.wd.project(self.class_of_word(word))

    def class_words(self):
        return [self.wd.word_of[m] for m in self.wd.reduced_group]

    @property
    def dimension(self):
        return len(self.wd.reduced_roots)

    # ------------------------------------------------------- degree gate
    def expected_degree(self, beta, n_classes, K=None):
        """Codimension sum the dimension axiom requires; invariants whose
        insertions don't match it vanish (this replaces the notebook's
        x -> prime*t, Limit[t -> 0] step)."""
        from .cintersection import ci_rank
        K = K or []
        dim = len(self.wd.reduced_roots) - ci_rank(K)
        if sum(beta) == 0:
            return dim
        cvec = chern_class_ci(self, K) if K else chern_class_vector(self)
        cb = sum(a * b for a, b in zip(cvec, beta))
        return dim + cb + n_classes - 3

    # --------------------------------------------------------------- GW
    def gw(self, coh_classes, beta, K=None, progress=None):
        """GW invariant as an exact Fraction.  coh_classes: Weyl matrices
        (see .classes / .pt / .schubert); beta: tuple over simple roots;
        K: complete-intersection multidegrees (list of rows) or None."""
        K = self._check_K(K or [])
        beta = self._check_beta(beta)
        deg = sum(self.wd.length(c) for c in coh_classes)
        if deg != self.expected_degree(beta, len(coh_classes), K):
            return Fraction(0)
        for attempt in range(3):
            try:
                vals = []
                for calc in self._numeric_pair(fresh=attempt > 0):
                    if K:
                        vals.append(gw_complete_intersection(
                            calc, coh_classes, beta, K, progress))
                    else:
                        vals.append(calc.gw_invariant(
                            coh_classes, beta, progress))
                if vals[0] == vals[1]:
                    return vals[0]
            except ZeroDivisionError:
                pass
        raise ArithmeticError(
            'numeric evaluations disagree — please report (classes of '
            f'lengths {[self.wd.length(c) for c in coh_classes]}, '
            f'beta={beta}, K={K})')

    # alias used by the quantum module
    gw_number = gw

    def gw_raw(self, coh_classes, beta, K=None, progress=None):
        """Raw symbolic localization sum (sympy/Sage expression)."""
        K = self._check_K(K or [])
        beta = self._check_beta(beta)
        if K:
            return gw_complete_intersection(self.sym, coh_classes,
                                            tuple(beta), K, progress)
        return self.sym.gw_invariant(coh_classes, tuple(beta), progress)

    # ----------------------------------------------------------- quantum
    def fano_index_and_betas(self, K=None):
        return betas_and_fano_index(self, self._check_K(K or []))

    def small_quantum_multiplication(self, K=None, betas=None, progress=None,
                                     workers=0):
        K = self._check_K(K or [])
        if betas is None:
            _, betas = betas_and_fano_index(self, K)
        return small_quantum_multiplication(self, K, betas, progress, workers)

    def eigenvalues(self, mat, at_one=False):
        """Eigenvalues of a quantum-multiplication matrix; with at_one=True
        the quantum variables y_i are set to 1 first (Conjecture O)."""
        if at_one:
            subs = {}
            for row in mat:
                for v in row:
                    if hasattr(v, 'free_symbols'):
                        subs.update({s: 1 for s in v.free_symbols})
            mat = [[self.bk.subs(v, subs) if hasattr(v, 'free_symbols')
                    else v for v in row] for row in mat]
        return self.bk.eigenvalues(mat)


def projective_space(n, backend=None):
    """P^n = A_n / P_1."""
    return FlagVariety(('A', n), [1], backend)


def grassmannian(k, n, backend=None):
    """Gr(k, n) (k-dim subspaces of C^n) = A_{n-1} / P_k."""
    return FlagVariety(('A', n - 1), [k], backend)


def full_flag(algebra, backend=None):
    """G/B for the given algebra."""
    rs = RootSystemData(algebra)
    return FlagVariety(algebra, list(range(1, rs.rank + 1)), backend)
