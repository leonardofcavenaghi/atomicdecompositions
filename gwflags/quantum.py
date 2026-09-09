"""Quantum-cohomology assembly of V3.nb: MetricCompletInter, ReduceMatrix,
SmallQuantumMultiplication, BetasAndFanoIndex.

All GW numbers are obtained through FlagVariety.gw_number (degree gate +
exact two-point numeric evaluation), so the metric and the pair sums are
exact Fractions; sympy/Sage only enters when the quantum variables y_i are
attached to the final matrix.  The per-beta pair sums can be distributed
over processes with workers=N.
"""

from fractions import Fraction
from math import gcd

from .rootsystem import mat_rank, mat_inverse
from .trees import nonneg_compositions


def spectrum_at_one(M):
    """Numeric eigenvalues of a quantum matrix with all y_i -> 1, via
    mpmath's QR-based eig (robust where symbolic eigenvalues fail, e.g.
    multivariate characteristic polynomials).  Sorted by descending
    modulus, so the first entry is the Conjecture-O eigenvalue."""
    import sympy
    from mpmath import mp, matrix as mpmatrix, eig
    subs = {}
    for row in M:
        for v in row:
            if hasattr(v, 'free_symbols'):
                subs.update({s: 1 for s in v.free_symbols})
    n = len(M)
    mp.dps = 25
    A = mpmatrix(n, n)
    for i in range(n):
        for j in range(n):
            q = sympy.Rational(sympy.sympify(M[i][j]).subs(subs))
            A[i, j] = mp.mpf(q.p) / mp.mpf(q.q)
    vals = eig(A, left=False, right=False)
    return sorted((complex(v) for v in vals),
                  key=lambda z: (-abs(z), round(z.real, 6), round(z.imag, 6)))


# ------------------------------------------------------------------- metric
def metric_matrix(X, K, indices, progress=None):
    """MetricCompletInter: g[k][j] = <sigma_k, sigma_j, 1>_0 (twisted by
    e(E) when K is nonempty).  Exact Fractions; the notebook's x -> 0
    limits are subsumed by the degree gate."""
    reps = X.wd.reduced_group
    zero = tuple([0] * X.rs.rank)
    mat = []
    for a, k in enumerate(indices):
        row = [X.gw_number([reps[k], reps[j], reps[0]], zero, K or None)
               for j in indices]
        mat.append(row)
        if progress:
            progress(f'metric row {a + 1}/{len(indices)}')
    return mat


def _independent_rows(rows):
    """LinesLI: indices of an incrementally independent set of rows."""
    chosen, idx, rank = [], [], 0
    for i, row in enumerate(rows):
        r = mat_rank(chosen + [[Fraction(v) for v in row]])
        if r > rank:
            chosen.append([Fraction(v) for v in row])
            idx.append(i)
            rank = r
    return idx


def reduce_matrix(X, mat):
    """ReduceMatrix: (independent column indices, invertible submatrix)."""
    rows = _independent_rows(mat)
    cols = _independent_rows([list(c) for c in zip(*mat)])
    sub = [[mat[i][j] for j in cols] for i in rows]
    return cols, sub


# ------------------------------------------------------- betas / Fano index
def chern_class_vector(X):
    """c1(TX) = sum of the reduced roots in the omega basis."""
    v = [0] * X.rs.rank
    for r in X.wd.reduced_roots:
        for j, c in enumerate(X.rs.omega_basis(r)):
            v[j] += int(c)
    return v


def chern_class_ci(X, K):
    """c1 of the complete intersection: c1(TX) - c1(E).

    K is either a HomogeneousBundle or the legacy list of rows, whose
    columns are paired with the kept simple roots in roots_that_stay
    order — the same convention the localization twist uses.  (The
    notebook instead used the ascending positions of the positive c1
    entries, which silently disagrees with its own mu when RootsThatStay
    is not sorted.)"""
    from .bundles import HomogeneousBundle
    c = chern_class_vector(X)
    bundle = [0] * len(c)
    if isinstance(K, HomogeneousBundle):
        for r, val in zip(X.wd.roots_that_stay, K.c1_coordinates()):
            bundle[r - 1] += val
    else:
        for row in K:
            for r, val in zip(X.wd.roots_that_stay, row):
                bundle[r - 1] += val
    return [a - b for a, b in zip(c, bundle)]


def vectors_with_support(n, positions, emax):
    """All nonnegative integer vectors of length n supported on `positions`
    (1-based) with total <= emax."""
    out = []
    for s in range(emax + 1):
        for comp in nonneg_compositions(s, len(positions)):
            v = [0] * n
            for p, c in zip(positions, comp):
                v[p - 1] = c
            out.append(tuple(v))
    return out


def betas_and_fano_index(X, K):
    """BetasAndFanoIndex: (Fano index, list of curve classes to sum over)."""
    from .cintersection import ci_rank
    c = chern_class_ci(X, K) if K else chern_class_vector(X)
    fano = 0
    for v in c:
        fano = gcd(fano, abs(v))
    if all(v == 0 for v in c):
        # Calabi-Yau complete intersection: c1 = 0, so c1(TX)* is the zero
        # operator; only the (vanishing) classical cup term remains
        return 0, [tuple([0] * X.rs.rank)]
    dim = len(X.wd.reduced_roots) - (ci_rank(K) if K else 0)
    # Enumerate supported beta with <c1, beta> <= dim + 1: the dimension
    # condition l_i + l_j = dim - 1 + <c1, beta> (with l <= dim) makes any
    # larger class vanish, so this is exhaustive.  Components where c1
    # vanishes are capped at dim + 1 each (their invariants carry a factor
    # <c1, beta> from other components; the notebook's total-degree bound
    # missed such classes entirely, e.g. a (1,2)-curve in P1xP1).
    cap = dim + 1
    kept = X.wd.roots_that_stay
    coeffs = [c[r - 1] for r in kept]
    betas = []
    def build(pos, remaining, current):
        if pos == len(kept):
            v = [0] * X.rs.rank
            for r, b in zip(kept, current):
                v[r - 1] = b
            betas.append(tuple(v))
            return
        ci = coeffs[pos]
        bmax = remaining // ci if ci > 0 else cap
        for b in range(bmax + 1):
            build(pos + 1, remaining - b * ci, current + [b])
    build(0, cap, [])
    betas.sort(key=lambda v: (sum(v), v))
    return fano, betas


# ------------------------------------------------- small quantum mult matrix
def _beta_block(X, K, cvec, dim, indices, beta):
    """All pair contributions of one curve class: {(i, j): Fraction}.
    For beta == 0 this is the classical cup product with c1; otherwise the
    divisor-axiom term (without its y-monomial, attached by the caller)."""
    reps = X.wd.reduced_group
    zero = tuple([0] * X.rs.rank)
    n = len(indices)
    out = {}
    if tuple(beta) == zero:
        divisors = [(e, ce) for e, ce in enumerate(cvec, start=1) if ce]
        for i in range(n):
            for j in range(i, n):
                cup = Fraction(0)
                for e, ce in divisors:
                    div = X.wd.project(X.rs.reflection_matrices[e - 1])
                    cup += ce * X.gw_number(
                        [div, reps[indices[i]], reps[indices[j]]], zero,
                        K or None)
                if cup:
                    out[(i, j)] = cup
        return out
    cb = sum(a * b for a, b in zip(cvec, beta))
    lens = [X.wd.length(reps[indices[i]]) for i in range(n)]
    pairs = [(i, j) for i in range(n) for j in range(i, n)
             if lens[i] + lens[j] == dim - 1 + cb]
    if not pairs:
        return {}
    # Decoration-outer streaming: each marked decoration class is generated
    # lazily and its class-independent factor computed ONCE, then
    # accumulated into every admissible pair.  Equivalent Fraction
    # arithmetic to the per-pair gw() calls (same decorations, same
    # factors), but O(1) memory in the number of decorations — the per-pair
    # formulation materialized the full marked-decoration list (tens of GB
    # at degree 5) purely to re-walk it once per pair.
    from .trees import all_trees, iter_decorated_trees
    from .cintersection import omega_complete_intersection
    K = X._check_K(K or [])
    sig = [reps[indices[i]] for i in range(n)]
    used_i = sorted({i for i, _ in pairs})
    used_j = sorted({j for _, j in pairs})
    for attempt in range(3):
        try:
            accs = []
            for calc in X._numeric_pair(fresh=attempt > 0):
                bk = calc.bk
                acc = {p: Fraction(0) for p in pairs}
                for tree in all_trees(sum(beta) + 1):
                    for dt in iter_decorated_trees(tree, beta, 2, X.wd):
                        w1, w2 = calc.mark_carriers(dt)
                        b1 = {i: calc.billey(sig[i], w1) for i in used_i}
                        b2 = {j: calc.billey(sig[j], w2) for j in used_j}
                        if all(bk.is_zero(v) for v in b1.values()) or \
                           all(bk.is_zero(v) for v in b2.values()):
                            continue
                        base = calc.dec_base_nocache(dt)
                        if K:
                            base = base * omega_complete_intersection(
                                calc, K, dt)
                        for (i, j) in pairs:
                            t = b1[i] * b2[j]
                            if not bk.is_zero(t):
                                acc[(i, j)] += bk.cancel(base * t)
                accs.append(acc)
            if accs[0] == accs[1]:
                return {p: cb * v for p, v in accs[0].items() if v}
        except ZeroDivisionError:
            pass
    raise ArithmeticError(
        'numeric evaluations disagree in beta block '
        f'{tuple(beta)} — please report')


def _beta_block_star(args):
    return _beta_block(*args)


# fork-context worker state: children inherit this copy-on-write, so the
# FlagVariety (with its warm decoration caches) is never pickled
_FORK_ARGS = []


def _beta_block_fork(beta):
    X, K, cvec, dim, indices = _FORK_ARGS[0]
    return _beta_block(X, K, cvec, dim, indices, beta)


def small_quantum_multiplication(X, K, betas, progress=None, workers=0):
    """SmallQuantumMultiplication: (matrix of c1(TX)*, grading matrix,
    0-based basis indices into X.classes).  Entries carry the quantum
    variables y_i.  workers > 0 distributes the per-beta blocks over
    processes."""
    bk, wd, rs = X.bk, X.wd, X.rs
    reps = wd.reduced_group

    if not K:
        indices = list(range(len(reps)))
        cvec = chern_class_vector(X)
        dim = len(wd.reduced_roots)
        g = metric_matrix(X, [], indices, progress)
    else:
        cvec = chern_class_ci(X, K)
        from .cintersection import ci_rank
        dim = len(wd.reduced_roots) - ci_rank(K)
        pre = metric_matrix(X, K, list(range(len(reps))), progress)
        indices, g = reduce_matrix(X, pre)
    ginv = mat_inverse(tuple(tuple(v for v in row) for row in g))

    n = len(indices)
    if workers and len(betas) > 1:
        import multiprocessing as mp
        from concurrent.futures import ProcessPoolExecutor
        if 'fork' in mp.get_all_start_methods():
            ctx = mp.get_context('fork')
            _FORK_ARGS[:] = [(X, K, cvec, dim, indices)]
            try:
                with ProcessPoolExecutor(max_workers=workers,
                                         mp_context=ctx) as pool:
                    blocks = list(pool.map(
                        _beta_block_fork, [tuple(b) for b in betas]))
            finally:
                _FORK_ARGS.clear()
        else:
            tasks = [(X, K, cvec, dim, indices, tuple(beta))
                     for beta in betas]
            with ProcessPoolExecutor(max_workers=workers) as pool:
                blocks = list(pool.map(_beta_block_star, tasks))
    else:
        blocks = []
        for beta in betas:
            blocks.append(_beta_block(X, K, cvec, dim, indices, tuple(beta)))
            if progress:
                progress(f'beta {tuple(beta)} done')

    sqm = [[0] * n for _ in range(n)]
    for beta, block in zip(betas, blocks):
        if tuple(beta) == tuple([0] * rs.rank):
            qmon = 1
        else:
            qmon = 1
            for u, bu in enumerate(beta, start=1):
                if bu:
                    qmon = qmon * bk.y(u) ** bu
        for (i, j), val in block.items():
            term = bk.rational(val) * qmon if qmon != 1 else val
            sqm[i][j] = sqm[i][j] + term
            if i != j:
                sqm[j][i] = sqm[j][i] + term

    # Transpose[SQM.g] with g the inverse metric
    prod = [[sum(sqm[i][k] * bk.rational(ginv[k][j]) for k in range(n))
             for j in range(n)] for i in range(n)]
    mat_c1 = [[prod[j][i] for j in range(n)] for i in range(n)]
    grading = [[bk.rational(Fraction(2 * wd.length(reps[indices[a]]) - dim, 2))
                if a == b else 0 for b in range(n)] for a in range(n)]
    return mat_c1, grading, indices
