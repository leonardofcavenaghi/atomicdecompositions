"""Small quantum multiplication by c1(TX) for a smooth projective toric
variety, assembled from the GW numbers of ToricVariety (same conventions
as gwflags.quantum: matrix of c1*, grading operator, Novikov variables).

Effective classes with a nonzero localization sum are nonnegative integer
combinations of the wall-curve classes (a fixed stable map covers
invariant curves).  A class beta contributes to c1* only if
3 - dim <= c1 . beta <= dim + 1  and  c1 . beta != 0  (dimension, unit and
divisor axioms).  When c1 is positive on every wall curve these classes
are finitely many.  Otherwise a complete intersection (assumed Fano) gets
the exact list of gwtoric.mori, and a toric variety that is not Fano a
cutoff at a bound on the degree of an ample divisor; see
curve_class_report.  The classes are independent of each other: they can
be spread over worker processes, and slow ones are cached on disk.
"""

import hashlib
import json
import os
import time
from fractions import Fraction
from math import gcd

import sympy

from gwflags.rootsystem import mat_inverse


def nonpositive_curves(X, K=None):
    """Wall-curve classes on which c1 (of X, or of the complete
    intersection Z) has degree <= 0.  When there are any, the list of
    betas_and_fano_index is a truncation."""
    rows = X.check_K(K)
    return [w for w in X.fan.wall_classes if X.c1_degree(w, rows) <= 0]


def default_max_degree(X, K=None):
    """Default ample-degree cutoff of betas_and_fano_index: None when c1
    is positive on every wall curve (the list is finite and exact),
    otherwise dim + 3 times the smallest ample degree of a wall curve,
    i.e. fixed loci whose trees have at most dim + 3 edges (the cost of a
    class grows roughly 5-fold per edge)."""
    rows = X.check_K(K)
    if not nonpositive_curves(X, rows):
        return None
    amp = X.fan.ample_divisor()
    return (X.n - len(rows) + 3) * min(
        X.fan.wall_degree(amp, w) for w in X.fan.wall_classes)


def _wall_sum_betas(X, rows, max_degree):
    """0 and the sums beta of wall curves with 3 - dim <= c1 . beta <=
    dim + 1, c1 . beta != 0, and omega . beta <= max_degree when given."""
    walls = X.fan.wall_classes
    degs = [X.c1_degree(w, rows) for w in walls]
    dim = X.n - len(rows)
    positive = all(d > 0 for d in degs)
    amp = X.fan.ample_divisor()
    adegs = [X.fan.wall_degree(amp, w) for w in walls]
    found = set()

    def rec(idx, current, cdeg, adeg):
        found.add(tuple(current))
        for j in range(idx, len(walls)):
            if max_degree is not None and adeg + adegs[j] > max_degree:
                continue
            if positive and cdeg + degs[j] > dim + 1:
                continue
            rec(j, [c + w for c, w in zip(current, walls[j])],
                cdeg + degs[j], adeg + adegs[j])

    rec(0, [0] * X.k, 0, 0)

    def contributes(v):
        d = X.c1_degree(v, rows)
        return not any(v) or (d != 0 and 3 - dim <= d <= dim + 1)

    return sorted((v for v in found if contributes(v)),
                  key=lambda v: (X.c1_degree(v, rows), v))


def curve_class_report(X, K=None, max_degree=None, mori=None, progress=None,
                       auto_mori=True, verify=3):
    """The curve classes that can contribute to c1* and how they were
    found, as a dict with keys

      mode    'positive': c1 is positive on every wall curve, the list
                  (sums of wall curves with c1 . beta <= dim + 1; for a
                  complete intersection only those that pass the
                  connectedness and point-insertion rules of gwtoric.mori)
                  is finite and exact;
              'mori': a complete intersection Z, assumed Fano, inside an
                  X with wall curves of c1(Z)-degree <= 0: exact list from
                  the cone of curves of Z (gwtoric.mori), no cutoff;
              'mori-auto': same, with inequalities derived by
                  gwtoric.mori.suggest_inequalities and checked by sampling
                  (a guess supported by evidence, not a proof);
              'cutoff': classes with omega . beta <= max_degree, omega =
                  X.fan.ample_divisor() (a toric X that is not Fano, an
                  explicit max_degree, or a stuck 'mori');
      fano, betas, nonpositive, max_degree (cutoff mode), stats (mori
      mode), not_fano: the reason when Z was found not to be Fano (a
      curve Z cap V(sigma) of c1(Z)-degree <= 0; cutoff mode is used),
      stuck: [(stratum rays, class with c1(Z)-degree <= 0)] when
      the cone of curves of Z could not be bounded and an inequality
      mori=[N, ...] (N . beta >= 0 on the curves of Z) is needed,
      suggested: [(stratum, divisor)] derived automatically, verify:
      the sample check of the inequalities (see mori.verify_mori).

    auto_mori: when a stratum is stuck, try to derive the missing
    inequalities and use the ones that survive the sample check.
    verify: how many excluded classes to test (0 switches the check off,
    and then nothing is derived automatically either)."""
    rows = X.check_K(K)
    fano = X.fano_index(rows)
    nonpos = nonpositive_curves(X, rows)
    out = {'fano': fano, 'nonpositive': nonpos, 'max_degree': None,
           'stuck': [], 'stats': None, 'not_fano': None, 'suggested': [],
           'verify': None}
    if rows and max_degree is None:
        # also when c1(Z) is positive on the wall curves: the list of
        # gwtoric.mori is contained in the sums of wall curves and drops
        # the classes whose invariants vanish for geometric reasons
        from .mori import (fano_ci_classes, MoriStuck, suggest_inequalities,
                           verify_mori)
        try:
            out['betas'], out['stats'] = fano_ci_classes(X, rows, mori,
                                                         progress)
            out['mode'] = 'mori' if nonpos else 'positive'
            if mori and verify:
                out['verify'] = verify_mori(X, rows, mori, verify, progress)
            return out
        except MoriStuck as exc:
            out['stuck'] = exc.stuck
            if auto_mori and verify:
                sug = suggest_inequalities(X, rows, progress, verify)
                if sug:
                    extra = [list(N) for _, N, _ in sug]
                    try:
                        out['betas'], out['stats'] = fano_ci_classes(
                            X, rows, list(mori or []) + extra, progress)
                        out['mode'] = 'mori-auto'
                        out['suggested'] = [(s, list(N)) for s, N, _ in sug]
                        out['verify'] = {
                            'checked': [b for _, _, r in sug
                                        for b in r['checked']],
                            'failures': []}
                        return out
                    except (MoriStuck, ValueError):
                        pass
        except ValueError as exc:
            out['not_fano'] = str(exc)
    if nonpos and max_degree is None:
        max_degree = default_max_degree(X, rows)
    out['mode'] = 'cutoff' if nonpos or max_degree is not None else 'positive'
    out['max_degree'] = max_degree
    out['betas'] = _wall_sum_betas(X, rows, max_degree)
    return out


def betas_and_fano_index(X, K=None, max_degree=None, mori=None):
    """(Fano index, curve classes that can contribute to c1*), the latter
    as vectors in Z^k.  With K the complete intersection Z is used:
    c1(Z) = c1(X) - sum D_m and dim Z = dim X - rank.

    The classes are 0 and the sums beta of wall curves (these generate
    the Mori cone of X) with  3 - dim <= c1 . beta <= dim + 1  and
    c1 . beta != 0:  <c1, a, b>_beta = (c1 . beta) <a, b>_beta, the
    dimension axiom needs deg a + deg b = dim - 1 + c1 . beta <= 2 dim,
    and an invariant with a degree-0 insertion vanishes.  The condition
    is on beta, not on its summands: a contributing class may contain
    wall curves of c1-degree <= 0 (E + f on F_2 has <pt> = 1).

    When c1 is positive on every wall curve the list is finite and exact.
    Otherwise it is infinite.  For a complete intersection Z (assumed
    Fano) it is replaced by the exact finite list of gwtoric.mori, built
    from the cone of curves of Z; mori = extra divisors N with
    N . beta >= 0 on the curves of Z, needed when that cone cannot be
    bounded from the fan alone (curve_class_report names the strata).
    For a toric X that is not Fano, with an explicit max_degree, or when
    the cone is not bounded, only the classes with omega . beta <=
    max_degree are listed, omega = X.fan.ample_divisor() (default:
    default_max_degree): c1* is then exact modulo the Novikov monomials
    of larger omega-degree."""
    rep = curve_class_report(X, K, max_degree, mori)
    return rep['fano'], rep['betas']


def c1_grading(X, K=None):
    """Degrees c_j of the Novikov variables: c1(Z) = sum_j c_j A_j in
    Pic X, where A_j = X.novikov_divisors.  With deg y_j = c_j the
    monomial q^beta has degree c1 . beta, so the matrix of c1* is
    homogeneous: entry (i, j) has degree deg sigma_j + 1 - deg sigma_i.
    Integers when the A_j are a Z-basis of Pic X (they are whenever a nef
    basis was found), Fractions otherwise."""
    rows = X.check_K(K)
    basis = X.fan.h2_basis
    mat = tuple(tuple(Fraction(v) for v in X.novikov_exponents(b))
                for b in basis)
    inv = mat_inverse(mat)
    out = []
    for j in range(len(basis)):
        v = sum(inv[j][a] * Fraction(X.c1_degree(b, rows))
                for a, b in enumerate(basis))
        out.append(int(v) if v.denominator == 1 else v)
    return out


def specialize_c1(X, M, K=None, var='t'):
    """The matrix with every Novikov variable replaced by t^{c_j}, i.e.
    q^beta -> t^{c1 . beta}: the single-variable, c1-graded form of the
    quantum product (the grading used for quantum periods).  This is a
    ring homomorphism, so the specialized matrix is still the matrix of a
    product, but it identifies all the curve classes of one c1-degree: it
    is a faithful record only when finitely many of them contribute,
    which needs c1 positive on the Mori cone (see curve_class_report)."""
    import sympy
    t = sympy.Symbol(var)
    subs = {sympy.Symbol(f'y{j + 1}'): t ** c
            for j, c in enumerate(c1_grading(X, K))}
    return [[sympy.expand(sympy.sympify(v).subs(subs)) for v in row]
            for row in M]


def _charpoly(A):
    """Coefficients of det(x I - A), highest power first, in exact
    arithmetic (Faddeev-LeVerrier).  A is a list of rows of Fractions."""
    n = len(A)
    coeffs = [Fraction(1)]
    Mk = [[Fraction(0)] * n for _ in range(n)]
    for k in range(1, n + 1):
        if k > 1:
            Mk = [[sum(A[i][t] * Mk[t][j] for t in range(n))
                   for j in range(n)] for i in range(n)]
        else:
            Mk = [row[:] for row in A]
        c = -Fraction(sum(Mk[i][i] for i in range(n)), k)
        coeffs.append(c)
        for i in range(n):
            Mk[i][i] += c
    return coeffs


def spectrum_at_one(M):
    """Eigenvalues of a quantum matrix with every Novikov variable set to
    1, sorted by descending modulus, so the first entry is the
    Conjecture-O eigenvalue.

    mpmath's QR iteration is tried first, at increasing precision: it
    fails to converge on some badly scaled matrices (entries spanning
    several orders of magnitude, which is what a Fano of small index
    gives).  The fallback is the exact characteristic polynomial, whose
    roots mpmath finds reliably; it costs O(n^4) exact operations, so it
    is only used when the iteration gives up."""
    from mpmath import mp, matrix as mpmatrix, eig, polyroots

    subs = {}
    for row in M:
        for v in row:
            if hasattr(v, 'free_symbols'):
                subs.update({s: 1 for s in v.free_symbols})
    n = len(M)
    exact = [[Fraction(str(sympy.Rational(sympy.sympify(v).subs(subs))))
              for v in row] for row in M]

    def sort(vals):
        # descending modulus, and on a tie the largest real part first, so
        # that the Conjecture-O eigenvalue heads the list even when the
        # index of the variety puts other eigenvalues on the same circle
        return sorted((complex(v) for v in vals),
                      key=lambda z: (-abs(z), -round(z.real, 6),
                                     round(z.imag, 6)))

    for dps in (25, 60, 150):
        mp.dps = dps
        A = mpmatrix(n, n)
        for i in range(n):
            for j in range(n):
                A[i, j] = mp.mpf(exact[i][j].numerator) / \
                    mp.mpf(exact[i][j].denominator)
        try:
            return sort(eig(A, left=False, right=False))
        except RuntimeError:                  # qr: failed to converge
            continue
    mp.dps = 60
    coeffs = _charpoly(exact)
    return sort(polyroots([mp.mpf(c.numerator) / mp.mpf(c.denominator)
                           for c in coeffs], maxsteps=200, extraprec=400))


def metric_matrix(X, K=None, progress=None, cancel=None):
    """g[i][j] = int_Z sigma_i sigma_j = int_X sigma_i sigma_j e(E) on the
    graded basis of H^*(X) (exact Fractions)."""
    rows = X.check_K(K)
    euler = [X.divisor(a) for a in rows]
    dim = X.n - len(rows)
    basis = X.classes
    N = len(basis)
    g = [[Fraction(0)] * N for _ in range(N)]
    degs = [b.degree() for b in basis]
    for i in range(N):
        for j in range(i, N):
            if degs[i] + degs[j] == dim:
                g[i][j] = g[j][i] = X.integral(basis[i], basis[j], *euler)
        if progress:
            progress(f'metric row {i + 1}/{N}')
        if cancel is not None and cancel():
            from .engine import Cancelled
            raise Cancelled()
    return g


def ambient_basis_indices(g):
    """Indices of an incrementally independent set of rows of the metric:
    a basis of H^*(X) modulo the classes pairing to zero with everything
    on Z (for K = [] the metric is nondegenerate and all rows are kept)."""
    from gwflags.quantum import _independent_rows
    return _independent_rows(g)


def _rat(fr):
    return sympy.Rational(fr.numerator, fr.denominator)


# ------------------------------------------- parallel evaluation and cache
CACHE_VERSION = 1
CACHE_SECONDS = 2.0        # only classes slower than this are stored
_WORKER_X = {}


def cache_dir():
    """Folder of the on-disk cache of GW numbers (GWTORIC_CACHE, default
    ~/.gwtoric_cache); None when GWTORIC_NO_CACHE is set."""
    if os.environ.get('GWTORIC_NO_CACHE'):
        return None
    return os.environ.get('GWTORIC_CACHE') or os.path.join(
        os.path.expanduser('~'), '.gwtoric_cache')


class _Cache:
    """Two-point numbers <a, b>_beta of one (X, K), keyed by beta and the
    names of the classes; one JSON file, rewritten atomically."""

    def __init__(self, X, rows, enabled=True):
        folder = cache_dir() if enabled else None
        self.path = None
        self.data = {}
        if folder is None:
            return
        key = json.dumps([CACHE_VERSION, X.fan.rays, X.fan.max_cones, rows])
        self.path = os.path.join(
            folder, hashlib.sha1(key.encode()).hexdigest()[:20] + '.json')
        try:
            with open(self.path, encoding='utf-8') as fh:
                self.data = json.load(fh)['values']
        except (OSError, ValueError, KeyError):
            self.data = {}

    def get(self, b, keys):
        hit = self.data.get(','.join(map(str, b)))
        if hit is None or any(k not in hit for k in keys):
            return None
        return [Fraction(hit[k]) for k in keys]

    def put(self, b, keys, vals):
        if self.path is None:
            return
        self.data.setdefault(','.join(map(str, b)), {}).update(
            {k: str(v) for k, v in zip(keys, vals)})
        try:
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            tmp = self.path + '.tmp'
            with open(tmp, 'w', encoding='utf-8') as fh:
                json.dump({'version': CACHE_VERSION, 'values': self.data}, fh)
            os.replace(tmp, self.path)
        except OSError:
            pass


def _worker_gw(args):
    """One curve class in a worker process (the variety is rebuilt once
    per process from its fan)."""
    rays, cones, rows, idx, b, pairs = args
    key = (rays, cones)
    X = _WORKER_X.get(key)
    if X is None:
        from .variety import ToricVariety
        X = _WORKER_X[key] = ToricVariety(rays, cones)
    t0 = time.time()
    classes = X.classes
    basis = [classes[i] for i in idx]
    vals = X.gw_multi([(basis[i], basis[j]) for i, j in pairs], b,
                      [tuple(a) for a in rows])
    return b, vals, time.time() - t0


def auto_workers(X, betas):
    """Worker processes for small_quantum_multiplication(workers='auto'):
    a pool only pays off (start-up ~1 s per process) when several classes
    have fixed loci with >= 4 edges."""
    amp = X.fan.ample_divisor()
    unit = min(X.fan.wall_degree(amp, w) for w in X.fan.wall_classes)
    heavy = sum(1 for b in betas if X.fan.wall_degree(amp, b) >= 4 * unit)
    if heavy < 2:
        return 1
    return max(1, min(heavy, (os.cpu_count() or 2) - 1))


def small_quantum_multiplication(X, betas, K=None, progress=None,
                                 workers=None, cache=True, cancel=None):
    """(matrix of c1*, grading, basis names).  With K the operator is
    c1(TZ)* on the ambient part of H^*(Z) in the sub-basis of X.classes
    returned; see ToricVariety.small_quantum_multiplication.

    workers: number of processes over which the curve classes are spread
    (None or 1: in this process; 'auto': auto_workers).  cache: classes
    that took more than CACHE_SECONDS are stored in cache_dir() and read
    back on later runs with the same fan and K.  cancel: a callable
    checked between classes (and inside the graph sum through
    X.cancel); when it returns True the worker processes are terminated
    and engine.Cancelled is raised."""
    from .engine import Cancelled
    rows = X.check_K(K)
    euler = [X.divisor(a) for a in rows]
    dim = X.n - len(rows)
    g_full = metric_matrix(X, rows, progress, cancel)
    idx = ambient_basis_indices(g_full) if rows else list(range(len(g_full)))
    basis = [X.classes[i] for i in idx]
    names = [X.class_names[i] for i in idx]
    degs = [b.degree() for b in basis]
    N = len(basis)
    g = [[g_full[i][j] for j in idx] for i in idx]
    ginv = mat_inverse(tuple(tuple(v for v in row) for row in g))
    r = X.k - X.n
    ys = sympy.symbols(f'y1:{r + 1}') if r else ()
    sqm = [[sympy.Integer(0)] * N for _ in range(N)]
    c1 = X.c1_ci(rows)
    log = progress or (lambda s: None)

    # classical part, and the two-point numbers needed for each class
    jobs = []                                  # (beta, c1 . beta, pairs)
    for beta in betas:
        b = X.beta(beta)
        if not any(b):
            for i in range(N):
                for j in range(i, N):
                    if degs[i] + degs[j] == dim - 1:
                        val = X.integral(c1, basis[i], basis[j], *euler)
                        if val:
                            sqm[i][j] += _rat(val)
                            if i != j:
                                sqm[j][i] += _rat(val)
            log(f'beta {b} done')
            continue
        cb = X.c1_degree(b, rows)
        pairs = [(i, j) for i in range(N) for j in range(i, N)
                 if degs[i] + degs[j] == dim - 1 + cb]
        if pairs:
            jobs.append((b, cb, pairs))

    store = _Cache(X, [list(a) for a in rows], cache)
    keyof = lambda pairs: [f'{names[i]}|{names[j]}' for i, j in pairs]
    results = {}
    todo = []
    for b, cb, pairs in jobs:
        hit = store.get(b, keyof(pairs))
        if hit is None:
            todo.append((b, cb, pairs))
        else:
            results[b] = hit
            log(f'beta {b} read from the cache')
    if workers == 'auto':
        workers = auto_workers(X, [b for b, _, _ in todo])
    workers = min(int(workers or 1), max(1, len(todo)))

    def finished(b, pairs, vals, seconds, count):
        results[b] = vals
        if seconds >= CACHE_SECONDS:
            store.put(b, keyof(pairs), vals)
        log(f'beta {b} done ({seconds:.1f}s, {count}/{len(todo)})')

    if workers > 1:
        from concurrent.futures import ProcessPoolExecutor, as_completed
        amp = X.fan.ample_divisor()
        # slowest classes first, so that they do not end up queued last
        order = sorted(todo, key=lambda job: -X.fan.wall_degree(amp, job[0]))
        log(f'{len(todo)} curve classes on {workers} processes')
        rays = tuple(tuple(v) for v in X.fan.rays)
        cones = tuple(tuple(c) for c in X.fan.max_cones)
        krows = tuple(tuple(a) for a in rows)
        pairs_of = {b: pairs for b, _, pairs in todo}
        pool = ProcessPoolExecutor(max_workers=workers)
        futs = []            # bound before the try: the handler below reads it
        try:
            futs = [pool.submit(_worker_gw, (rays, cones, krows, tuple(idx),
                                             b, tuple(pairs)))
                    for b, _, pairs in order]
            for count, fut in enumerate(as_completed(futs), 1):
                if cancel is not None and cancel():
                    raise Cancelled()
                b, vals, seconds = fut.result()
                finished(b, pairs_of[b], vals, seconds, count)
        except BaseException:
            for f in futs:
                f.cancel()
            # running tasks ignore cancel(), so end them the hard way
            for p in list(getattr(pool, '_processes', {}).values()):
                try:
                    p.terminate()
                except Exception:           # noqa: BLE001
                    pass
            pool.shutdown(wait=False)
            raise
        else:
            pool.shutdown(wait=True)
    else:
        for count, (b, cb, pairs) in enumerate(todo, 1):
            if cancel is not None and cancel():
                raise Cancelled()
            t0 = time.time()
            vals = X.gw_multi([(basis[i], basis[j]) for i, j in pairs], b,
                              rows, progress=progress)
            finished(b, pairs, vals, time.time() - t0, count)

    for b, cb, pairs in jobs:
        qmon = sympy.Integer(1)
        for y, e in zip(ys, X.novikov_exponents(b)):
            if e:
                qmon *= y ** e
        for (i, j), v in zip(pairs, results[b]):
            if v:
                term = cb * _rat(v) * qmon
                sqm[i][j] += term
                if i != j:
                    sqm[j][i] += term
    prod = [[sum(sqm[i][k] * _rat(ginv[k][j]) for k in range(N))
             for j in range(N)] for i in range(N)]
    mat_c1 = [[sympy.expand(prod[j][i]) for j in range(N)] for i in range(N)]
    grading = [[sympy.Rational(2 * degs[a] - dim, 2) if a == b else 0
                for b in range(N)] for a in range(N)]
    return mat_c1, grading, names
