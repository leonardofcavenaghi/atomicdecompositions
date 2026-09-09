"""Formal asymptotics of the quantum connection at the irregular point.

Input: the pair (K, G) produced by the quantum-multiplication pipeline —
K = the matrix of c1(TX)* (quantum variables evaluated, y = 1 by
default) and G the grading operator.  The object of study is the
meromorphic connection of Kontsevich's "dimension theory" program:

    nabla = d/du + K/u^2 + G/u ,

whose formal solutions at u -> 0 are e^{z/u} u^s (log u)^k (...) with z
running over the eigenvalues of K.  Per spectral point z the module
computes the moderate exponents s and the *dimension candidate*

    dim(z) = -2 * min Re(s)          (Kontsevich's conjecture:
                                      = Serre dimension of the
                                      corresponding SOD component).

Method (exact, all in the delta = u^2 d/du frame, where everything is
polynomial):
  * solutions satisfy  delta psi = -(K + u G) psi, so the covector
    recursion r_{k+1} = u^2 r_k' - (K + u G)^T r_k stays in Q[u]^n with
    deg r_k <= k; a Q-linear solve finds the scalar operator
    sum a_k(u) delta^k annihilating c^T psi;
  * conjugation by e^{z/u} is the constant shift delta -> delta - z;
  * delta^k(u^s) = s(s+1)...(s+k-1) u^{s+k}, so the indicial polynomial
    of the slope-0 face is read off the minimal u-valuation of
    sum a_k(u) s^{(k)} u^k; its roots are the moderate exponents of the
    e^{z/u} sector (fractional roots and repeated/log structure appear
    naturally — this handles nilpotent blocks uniformly);
  * simple nonzero eigenvalues can bypass the scalar route via
    first-order perturbation: s = -(w^T G v)/(w^T v).
"""

from fractions import Fraction

import sympy

u = sympy.Symbol('u')
_s = sympy.Symbol('s')


# ------------------------------------------------- scalar delta-operator
def scalar_delta_operator(K, G, cvec=None, max_tries=4):
    """Coefficients [a_0(u), ..., a_m(u)] (sympy polynomials in u) of a
    minimal-order operator sum_k a_k(u) delta^k annihilating c^T psi for
    delta psi = -(K + u G) psi."""
    K = sympy.Matrix(K)
    G = sympy.Matrix(G)
    n = K.shape[0]
    B = (K + u * G).T
    tries = 0
    while True:
        if cvec is not None:
            c = sympy.Matrix(list(cvec))
        elif tries == 0:
            c = sympy.Matrix([1] * n)
        else:
            import random
            rng = random.Random(17 + tries)
            c = sympy.Matrix([rng.randint(1, 9) for _ in range(n)])
        # a cyclic covector gives a dependence of full order n, so the
        # scalar operator captures the FULL solution space; a lower-order
        # dependence means c is non-cyclic (annihilates a subspace and
        # silently loses exponents) — demand a nonzero leading
        # coefficient, else retry with another covector
        rows = [c.T]
        for k in range(n):
            prev = rows[-1]
            nxt = (u ** 2 * prev.diff(u) - prev * B.T).applyfunc(sympy.expand)
            rows.append(nxt)
        dep = _poly_dependence(rows, require_top=True)
        if dep is not None:
            return dep
        tries += 1
        cvec = None
        if tries >= max_tries:
            raise RuntimeError(
                'no cyclic covector found (all tried covectors give '
                'lower-order operators)')


def _poly_dependence(rows, require_top=False):
    """Find polynomials a_k(u), not all zero, with sum a_k row_k = 0.
    deg row_k <= k, so a_k of degree <= D with D = sum deg suffices when
    a dependence over Q(u) exists.  Pure Q-linear algebra.  With
    require_top, only accept dependences whose top coefficient a_m is
    nonzero (full-order scalar operator — cyclic covector)."""
    m = len(rows) - 1
    n = rows[0].shape[1]
    D = max(2, m * (m + 1) // 2 + 2)
    polys = [[sympy.Poly(rows[k][0, j], u) for j in range(n)]
             for k in range(m + 1)]
    maxdeg = max(p.degree() for row in polys for p in row if not p.is_zero)
    nrows_eq = n * (maxdeg + D + 2)
    ncols = (m + 1) * (D + 1)
    M = sympy.zeros(nrows_eq, ncols)
    for k in range(m + 1):
        for j in range(n):
            coeffs = polys[k][j].all_coeffs()[::-1]   # low to high
            for dcoef, cval in enumerate(coeffs):
                if cval == 0:
                    continue
                for e in range(D + 1):
                    # a_k coefficient of u^e multiplies u^{dcoef+e}
                    M[j * (maxdeg + D + 2) + dcoef + e,
                      k * (D + 1) + e] += cval
    null = M.nullspace()
    if not null:
        return None

    def extract(a):
        out = []
        for k in range(m + 1):
            poly = sum(a[k * (D + 1) + e] * u ** e for e in range(D + 1))
            out.append(sympy.expand(poly))
        while out and out[-1] == 0:
            out.pop()
        return out

    if not require_top:
        return extract(null[0])
    for a in null:
        out = extract(a)
        if len(out) == m + 1:
            return out
    return None


# ----------------------------------------------------------- indicial data
def shift_operator(coeffs, z):
    """Coefficients of the operator with delta replaced by delta + z
    (i.e. the e^{z/u}-conjugated operator: y = e^{z/u} w satisfies the
    original equation iff w satisfies the shifted one with delta ->
    delta - z; equivalently substitute and expand binomially)."""
    m = len(coeffs) - 1
    out = [sympy.Integer(0)] * (m + 1)
    for k, a in enumerate(coeffs):
        if a == 0:
            continue
        # (delta - z)^k = sum_j C(k,j) (-z)^{k-j} delta^j
        for j in range(k + 1):
            out[j] = out[j] + a * sympy.binomial(k, j) * (-z) ** (k - j)
    while out and sympy.simplify(out[-1]) == 0:
        out.pop()
    return [sympy.expand(o) for o in out]


def indicial_polynomial(coeffs):
    """P(s) from the slope-0 face: apply sum a_k(u) delta^k to u^s using
    delta^k(u^s) = s^{(k)} u^{s+k}; collect the minimal u-power."""
    terms = {}
    for k, a in enumerate(coeffs):
        if a == 0:
            continue
        rising = 1
        for i in range(k):
            rising = rising * (_s + i)
        p = sympy.Poly(sympy.expand(a), u)
        for (j,), c in p.terms():
            key = j + k
            terms[key] = terms.get(key, 0) + c * rising
    if not terms:
        return sympy.Integer(0)
    nu = min(terms)
    return sympy.expand(terms[nu])


def _roots_of(P):
    P = sympy.expand(P)
    if P == 0:
        return []
    rd = sympy.roots(P, _s)
    out = []
    if sum(rd.values()) == sympy.degree(P, _s):
        for r, m in rd.items():
            out.extend([r] * m)
    else:
        for r in sympy.Poly(P, _s).all_roots():
            out.append(r)
    return out


# ------------------------------------------------------ spectral analysis
def _simple_exponent(K, G, z):
    """s = -(w^T G v)/(w^T v) for a simple eigenvalue z (exact for
    rational z; numeric-with-recognition otherwise)."""
    n = K.shape[0]
    if getattr(z, 'is_rational', False):
        Mz = K - z * sympy.eye(n)
        v = Mz.nullspace()[0]
        w = Mz.T.nullspace()[0]
        num = (w.T * G * v)[0, 0]
        den = (w.T * v)[0, 0]
        return sympy.nsimplify(sympy.cancel(-num / den), rational=True)
    from mpmath import mp, matrix as mpmatrix, eig
    mp.dps = 40
    A = mpmatrix(n, n)
    for i in range(n):
        for j in range(n):
            A[i, j] = complex(sympy.N(K[i, j], 40))
    zc = complex(sympy.N(z, 40))
    E, VR = eig(A)
    idx = min(range(n), key=lambda i: abs(complex(E[i]) - zc))
    v = [complex(VR[i, idx]) for i in range(n)]
    El, VL = eig(A.T)
    idxl = min(range(n), key=lambda i: abs(complex(El[i]) - zc))
    w = [complex(VL[i, idxl]) for i in range(n)]
    g = [complex(sympy.N(G[i, i], 40)) for i in range(n)]
    num = sum(w[i] * g[i] * v[i] for i in range(n))
    den = sum(w[i] * v[i] for i in range(n))
    val = -num / den
    rat = sympy.nsimplify(sympy.Float(val.real, 25), rational=True,
                          tolerance=1e-12)
    if abs(val.imag) < 1e-12 and abs(float(rat) - val.real) < 1e-10:
        return sympy.Rational(rat)
    return sympy.Float(val.real, 15) + sympy.I * sympy.Float(val.imag, 15)


def _projected_g_exponents(K, G, z, mult):
    """For a SEMISIMPLE sector (geometric = algebraic multiplicity) the
    exponents are exactly the eigenvalues of -Pi_z G Pi_z restricted to
    the eigenspace (first-order block reduction; higher corrections only
    produce logs at resonances, never shift the exponents).  Returns None
    if the sector is not semisimple."""
    n = K.shape[0]
    Mz = K - z * sympy.eye(n)
    V = Mz.nullspace()
    if len(V) != mult:
        return None            # Jordan sector
    W = Mz.T.nullspace()
    Vm = sympy.Matrix.hstack(*V)
    Wm = sympy.Matrix.hstack(*W)
    pair = Wm.T * Vm
    Gp = pair.inv() * (Wm.T * G * Vm)
    exps = []
    for ev, m in Gp.eigenvals().items():
        exps.extend([sympy.nsimplify(-ev, rational=False)] * m)
    return exps


def _scalar_route_exponents(K, G, z, n_covectors=3):
    """Indicial exponents of the e^{z/u} sector via cyclic scalar
    reductions.  A covector can shift exponents UP by integers when it
    pairs degenerately with a solution, so several random covectors are
    used and the pattern with the smallest minimum is returned."""
    import random
    best = None
    for t in range(n_covectors):
        if t == 0:
            c = None
        else:
            rng = random.Random(1000 + 37 * t)
            c = [rng.randint(1, 19) for _ in range(sympy.Matrix(K).shape[0])]
        try:
            coeffs = scalar_delta_operator(K, G, cvec=c)
        except RuntimeError:
            continue
        op = coeffs if z == 0 else shift_operator(coeffs, z)
        P = indicial_polynomial(op)
        exps = _roots_of(P)
        if not exps:
            continue
        m = min(complex(sympy.N(e)).real for e in exps)
        if best is None or m < best[0] - 1e-12:
            best = (m, exps)
    return best[1] if best else []


def spectral_exponents(K, G):
    """Per eigenvalue z of K: moderate exponents of the e^{z/u} sector
    and the dimension candidate -2 min Re(s).

    Semisimple sectors (geometric = algebraic multiplicity) use the
    exact projector formula spec(-Pi_z G Pi_z) — no covector artifacts.
    Jordan sectors use cyclic scalar reductions with several covectors
    (exponents there are genuinely fractional; the covector-minimum is
    taken because scalar models can shift exponents up by integers)."""
    Ks = sympy.Matrix(K)
    Gs = sympy.Matrix(G)
    eig = Ks.eigenvals()
    out = {}
    for z, mult in eig.items():
        if mult == 1:
            exps = [_simple_exponent(Ks, Gs, z)] if z != 0 else \
                _projected_g_exponents(Ks, Gs, z, mult)
            if exps is None:
                exps = _scalar_route_exponents(K, G, z)
        else:
            exps = None
            if _is_exactable(z):
                exps = _projected_g_exponents(Ks, Gs, z, mult)
            if exps is None:
                exps = _scalar_route_exponents(K, G, z)
        dimension = None
        if exps:
            vals = [complex(sympy.N(e)).real for e in exps]
            dimension = -2 * min(vals)
        out[z] = {'multiplicity': mult, 'exponents': exps,
                  'dimension': dimension}
    return out


def _is_exactable(z):
    """Exact nullspace computations are practical when the eigenvalue
    expression is simple (rational, or a small algebraic expression like
    2*I, -6*sqrt(3)); huge nested radicals would make exact linear
    algebra crawl — those only occur for simple eigenvalues, which never
    reach the projector path anyway."""
    if getattr(z, 'is_rational', False):
        return True
    try:
        return sympy.count_ops(z) <= 24
    except Exception:
        return False


# --------------------------------------------------------------- frontend
def quantum_connection_report(M, Gr, y_values=None):
    """From the pipeline's symbolic (matrix, grading): evaluate the
    quantum variables (default all 1) and run the spectral analysis."""
    subs = {}
    rows = []
    for row in M:
        r = []
        for vexpr in row:
            e = sympy.sympify(vexpr)
            for sym in e.free_symbols:
                subs[sym] = (y_values or {}).get(str(sym), 1)
            r.append(e)
        rows.append(r)
    Keval = [[sympy.nsimplify(e.subs(subs)) for e in r] for r in rows]
    n = len(Keval)
    Gm = [[sympy.Rational(Fraction(str(Gr[i][j]))) if i == j else 0
           for j in range(n)] for i in range(n)]
    return spectral_exponents(Keval, Gm)
