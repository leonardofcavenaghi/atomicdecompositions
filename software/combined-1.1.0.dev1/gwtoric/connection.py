"""Rank and regularized exponents of the generic Hodge factors of the
quantum connection, and the resulting obstruction to rationality.

This implements the procedure of Section 5 of

    L. Carazolli, L. F. Cavenaghi, L. Katzarkov, M. Kontsevich and
    P. A. M. Martins, "A quantum connection approach to rationality",

for the targets gwtoric handles: a smooth projective toric variety, or the
ambient part of a smooth complete intersection in one.

The input is the pair of matrices of the formal disk connection

    nabla_u = d/du + K^F / u^2 + G / u                                  (14)

at a point of the one-parameter small locus along the primitive
anticanonical ray (the paper's (8)).  Here K^F = -c1(TX)* is minus the
small quantum multiplication by c1 and G = diag((2 deg - dim)/2) is the
grading operator -- exactly what ToricVariety.small_quantum_multiplication
already returns, so disk_connection is a thin wrapper around it.

The steps, following the paper:

  Step 1 (genericity and cyclicity).  Evaluate the Krylov determinant
      Delta(q) = det(1, K^F 1, ..., (K^F)^{N-1} 1)
  on the unit class.  Delta != 0 certifies that the chosen point lies in
  the generic locus U^gen_X and that K^F is cyclic, so every eigenvalue
  carries a single Jordan block (Lemma 3.9 and the discussion of Step 1).

  Step 2 (rank).  Factor det(x id - K^F).  An eigenvalue of algebraic
  multiplicity m gives a generic Hodge factor of rank m (Lemma 3.3,
  Corollary 3.4).

  Step 3 (exponents).  Write a horizontal section of E^{lambda/u} tensor
  M_lambda as phi = u^s sum_{k>=0} u^k v_k, v_0 != 0.  Then (16) reads

      (lambda id - K^F) v_0 = 0,
      (lambda id - K^F) v_k = (G + (s + k - 1) id) v_{k-1},   k >= 1,

  and pairing with a left kernel vector w gives the solvability conditions
  (17)

      w (G + (s + k - 1) id) v_{k-1} = 0.

  Cyclicity makes both kernels one-dimensional, so v_k = v_k^part + c_k v_0
  with a free kernel parameter.  The conditions vanish identically until
  some order, where they become a polynomial in s whose roots are the
  admissible leading powers; by Lemma 5.1 every exponent class of R_lambda
  is represented modulo Z by one of them, and F = Exp(R_lambda) is their
  multiset of classes in Q/Z.

  For a *simple* eigenvalue the rank is 1 and (17) at k = 1 already gives
  s = -w G v_0 / (w v_0) = -tr(P_lambda G), the spectral projector trace.
  That is a residue, so it is computed here without ever leaving Q(q):
  with chi = det(x id - K^F) and N = tr(adj(x id - K^F) G),
      s = -N(lambda) / chi'(lambda),
  evaluated modulo the irreducible factor of chi that lambda satisfies.
  This covers the whole spectrum of a target whose c1* is regular
  semisimple, P^n included, with no algebraic number arithmetic.

  Verdict (Theorem 4.5).  For 2 <= dim X <= 4, if X is rational then every
  cyclic generic Hodge factor of unramified exponential type with rational
  residues has (m, F) equal to (1, {{0}}) ("point"), (2, {{1/2, 1/2}})
  ("curve", dim >= 3) or (3, {{0, 0, 0}}) ("surface", dim = 4).  One
  factor off that list proves X irrational.  Proposition 5.5 adds: a
  threefold with a cyclic rank-two factor whose F is not {{1/2, 1/2}} has
  X x P^1 irrational too.

Two things the software cannot check for you.

  * The criterion lives on the Hodge-invariant space
    H^Hdg(X) = sum_p (H^{2p}(X, Q) cap H^{p,p}), and what gwtoric computes
    for a complete intersection is the *ambient* part i^* H^*(Y).  These
    agree for a toric X (all of H^* is of Hodge-Tate type) and for a
    complete intersection of ample divisors of odd dimension (the middle
    cohomology then carries no (p,p) class, and Lefschetz plus hard
    Lefschetz make every other degree ambient).  In even dimension they
    agree only if the primitive middle cohomology carries no rational
    (n/2, n/2) class -- the paper's hypothesis (18), true for a very
    general member when h^{n/2-1,n/2+1} > 0, and false for instance for
    the cubic surface, whose Picard rank is 7.  hodge_invariant_status
    reports which case you are in and the verdict is withheld unless the
    hypothesis holds or you assert it with very_general=True.

  * The paper's Step 3 finishes by turning the recursion into a scalar ODE
    and checking that each admissible leading power really occurs without
    logarithmic terms.  Here the admissible powers are reported together
    with whether their number matches the rank; when it does, the count
    forces one log-free solution per power, which is the situation in all
    of the paper's examples.  When it does not, the result is flagged and
    the scalar-ODE step has to be done by hand.
"""

from fractions import Fraction
from math import gcd

import sympy


# ---------------------------------------------------------------- the pair
def _det(M):
    """Determinant of a sympy matrix over Q(q).

    sympy's default fraction-free elimination is quadratic in the entry
    degrees and becomes the whole cost of the characteristic polynomial and
    the Krylov test for the matrices that come up here; the polynomial
    domain does the same determinant about two orders of magnitude faster
    (0.04 s against 4 s on a nine-class four-fold).  Falls back to the
    dense method on anything the domain cannot hold.
    """
    try:
        from sympy.polys.matrices import DomainMatrix
        d = DomainMatrix.from_Matrix(M).det()
        return sympy.expand(d.as_expr() if hasattr(d, 'as_expr')
                            else sympy.sympify(d))
    except Exception:                                          # noqa: BLE001
        return sympy.expand(M.det())


def disk_connection(X, K=None, var='q', primitive=True, M=None, Gr=None):
    """(K^F, G, names) of the formal disk connection (14) at a point of the
    one-parameter small locus (8).

    K^F = -c1* and G = diag((2 deg - dim)/2) come from
    X.small_quantum_multiplication(K=K); every Novikov variable y_j is
    replaced by var ** c_j with c_j the c1-degrees (quantum.c1_grading),
    which is the paper's (8).  With primitive=True the degrees are divided
    by their gcd first, so var runs along the *primitive* anticanonical
    ray; for a Picard-rank-one target this sends y1 -> q, the
    normalization of the matrices printed in the paper.

    Pass M, Gr to reuse an already computed pair.
    """
    from .quantum import c1_grading
    if M is None or Gr is None:
        M, Gr, names = X.small_quantum_multiplication(K=K)
    else:
        names = [f'sigma{i}' for i in range(len(M))]
    degs = [Fraction(c) for c in c1_grading(X, K)]
    if primitive:
        num, den = 0, 1
        for c in degs:
            num = gcd(num, c.numerator)
            den = den * c.denominator // gcd(den, c.denominator)
        g = Fraction(num, den) if num else Fraction(1)
        degs = [c / g for c in degs]
    q = sympy.Symbol(var)
    subs = {sympy.Symbol(f'y{j + 1}'):
            q ** sympy.Rational(c.numerator, c.denominator)
            for j, c in enumerate(degs)}
    KF = -sympy.Matrix([[sympy.expand(sympy.sympify(v).subs(subs))
                         for v in row] for row in M])
    return KF, sympy.Matrix(Gr), names


# ------------------------------------------------- is the criterion usable?
def hodge_invariant_status(X, K=None, very_general=False):
    """(status, message): whether the space gwtoric computes on is the
    Hodge-invariant space H^Hdg the criterion needs.

    'full'      X is toric and no complete intersection is cut: H^*(X, Q)
                is of Hodge-Tate type, so H^Hdg(X) is all of it.
    'odd'       a complete intersection of ample divisors of odd dimension:
                the middle cohomology is of odd degree and carries no
                (p,p) class, and every other degree is ambient, so
                H^Hdg(Z) = i^* H^*(X) is exactly what is computed.
    'assumed'   even dimension, and you asserted very_general=True.
    'needs-very-general'  even dimension: the ambient part is H^Hdg only if
                the primitive middle cohomology has no rational
                (n/2, n/2) class.
    'not-ample' some hypersurface is nef but not ample, so the Lefschetz
                comparison that makes the non-middle degrees ambient is
                not available here.
    """
    rows = X.check_K(K)
    dim = X.n - len(rows)
    if not rows:
        return 'full', ('X is toric, so H^*(X, Q) is of Hodge-Tate type and '
                        'H^Hdg(X) = H^*(X, Q): the whole basis is used')
    walls = X.fan.wall_classes
    bad = [list(a) for a in rows
           if not all(X.fan.wall_degree(a, w) > 0 for w in walls)]
    if bad:
        return 'not-ample', (
            f'the hypersurface {bad[0]} is nef but not ample, so the '
            f'Lefschetz hyperplane theorem is not available and the ambient '
            f'part need not be all of H^Hdg(Z); no verdict is issued')
    if dim % 2:
        return 'odd', (
            f'dim Z = {dim} is odd: the middle cohomology has odd degree and '
            f'carries no (p,p) class, and Lefschetz and hard Lefschetz make '
            f'every other degree ambient, so H^Hdg(Z) = i^* H^*(X) is '
            f'exactly the space computed here')
    half = dim // 2
    if very_general:
        return 'assumed', (
            f'dim Z = {dim} is even and you asserted very_general=True, i.e. '
            f'H^{dim}(Z, Q)_prim cap H^{{{half},{half}}}(Z) = 0 (the paper\'s '
            f'hypothesis (18)); H^Hdg(Z) = i^* H^*(X) is then the space used')
    return 'needs-very-general', (
        f'dim Z = {dim} is even, so the ambient part is all of H^Hdg(Z) only '
        f'when H^{dim}(Z, Q)_prim cap H^{{{half},{half}}}(Z) = 0.  That holds '
        f'for a very general member as soon as h^{{{half - 1},{half + 1}}}(Z) '
        f'> 0, and fails when the primitive middle cohomology is all of type '
        f'({half},{half}) -- as for the cubic surface in P^3, whose Picard '
        f'rank is 7 while the ambient part has rank 1.  Pass '
        f'very_general=True to assert it; until then no verdict is issued')


# --------------------------------------------------- Step 1: the Krylov test
def exponential_type_status(X, K=None):
    """(ok, message): whether Theorem 3.6 guarantees that the disk
    connection at a point of the small locus is of unramified exponential
    type with rational residues -- which it does for a Fano target, and
    (explicitly, in the theorem's own words) for a graded ambient subspace
    closed under the small quantum product, which is what is used here.

    Proposition 3.8 covers a nef canonical class instead, but its exponents
    are read at a point of the Hodge-fixed base that the one-parameter
    small locus does not reach when c1 = 0 (there K^F vanishes
    identically), so that branch is not implemented.
    """
    rows = X.check_K(K)
    fano = X.is_fano_ci(rows) if rows else X.fan.is_fano()
    if fano:
        return True, ('c1 is positive on every invariant curve, so '
                      'Theorem 3.6 applies' + (' (on the ambient subspace, '
                      'as the theorem allows)' if rows else ''))
    return False, (
        'c1 is not positive on every invariant curve, so Theorem 3.6 does '
        'not guarantee unramified exponential type here; Proposition 3.8 '
        'treats a nef canonical class but needs a point of the Hodge-fixed '
        'base beyond the one-parameter small locus, and is not implemented')


def cyclic_determinant(KF, unit=0):
    """Delta = det(1, K^F 1, ..., (K^F)^{N-1} 1), the determinant of the
    Krylov matrix of K^F on the unit class (basis vector `unit`, index 0 in
    gwtoric's graded basis).

    Delta != 0 certifies both halves of Step 1 at once: the Euler powers
    span the Hodge-fixed tangent space, so the point lies in U^gen_X, and
    K^F is cyclic, i.e. every eigenvalue has a single Jordan block.
    Rescaling a basis vector rescales Delta, but not its vanishing.
    """
    N = KF.shape[0]
    v = sympy.zeros(N, 1)
    v[unit] = 1
    cols = [v]
    for _ in range(N - 1):
        cols.append(sympy.expand(KF * cols[-1]))
    return sympy.factor(_det(sympy.Matrix.hstack(*cols)))


def chi_and_N(KF, G, x=None):
    """(chi, N) with chi = det(x id - K^F) and N = tr(adj(x id - K^F) G),
    from a *single* determinant.

    By Jacobi's formula det(M + t G) = det M + t tr(adj(M) G) + O(t^2), so
    the two are the first two coefficients in t of det(x id - K^F + t G).
    Forming N as an adjugate instead costs N^2 cofactor determinants: 52 s
    against 0.24 s on a nine-class four-fold.
    """
    x = x or sympy.Symbol('x')
    t = sympy.Dummy('t')
    n = KF.shape[0]
    co = sympy.Poly(_det(x * sympy.eye(n) - KF + t * G), t).all_coeffs()[::-1]
    co = list(co) + [sympy.Integer(0)] * max(0, 2 - len(co))
    return sympy.expand(co[0]), sympy.expand(co[1])


# ------------------------------------------------------- Step 2: the ranks
class NotCyclic(ValueError):
    """The eigenvalue does not carry a single Jordan block, so the factor is
    not cyclic and Theorem 4.5 does not apply to it."""


def characteristic_factors(KF, x=None, chi=None):
    """[(p, m)] -- the irreducible factors of det(x id - K^F) over Q(q)
    with their multiplicities.  A factor of degree d and multiplicity m
    carries d eigenvalues of algebraic multiplicity m, i.e. d generic Hodge
    factors of rank m.  Pass chi to reuse a determinant already computed.
    """
    x = x or sympy.Symbol('x')
    if chi is None:
        chi = _det(x * sympy.eye(KF.shape[0]) - KF)
    out = [(sympy.Poly(p, x), int(m))
           for p, m in sympy.factor_list(chi, x)[1]]
    out.sort(key=lambda t: (-t[1], t[0].degree(),
                            sympy.default_sort_key(t[0].as_expr())))
    return out


def _linear_root(p):
    """The root of a degree-one factor, or None."""
    if p.degree() != 1:
        return None
    a, b = p.all_coeffs()
    return sympy.simplify(-b / a)


# --------------------------------------------------- Step 3: the exponents
def simple_exponent(KF, G, p, x=None, chi=None, N=None):
    """The exponent of the rank-one factors at the roots of the *simple*
    irreducible factor p of det(x id - K^F), as -N/chi' reduced modulo p
    (see the module docstring).  Returns a Fraction when the reduction is a
    rational constant -- so one class shared by every root of p -- and the
    unreduced expression otherwise.  Pass chi, N from chi_and_N to reuse
    them across the factors.
    """
    x = x or sympy.Symbol('x')
    if chi is None or N is None:
        chi, N = chi_and_N(KF, G, x)
    chi = sympy.Poly(chi, x)
    inv = sympy.invert(sympy.Poly(chi.diff(x).as_expr(), x), p)
    r = sympy.simplify(sympy.rem(sympy.expand(-N * inv.as_expr()),
                                 p.as_expr(), x))
    rr = sympy.nsimplify(r)
    if rr.is_rational:
        return Fraction(int(sympy.Rational(rr).p), int(sympy.Rational(rr).q))
    return r


def exponents(KF, G, lam, m=None, max_order=None):
    """Regularized exponents of the generic Hodge factor at the eigenvalue
    lam, by the recursion (16) and the solvability conditions (17).

    Returns a dict with

      rank         m, the algebraic multiplicity of lam,
      order        the order k at which (17) first failed to vanish,
      obstruction  that condition, as a polynomial in s,
      powers       its roots s with multiplicity: the admissible leading
                   powers,
      F            the multiset Exp(R_lam) of their classes in Q/Z, as
                   Fractions in [0, 1), sorted,
      complete     whether len(powers) == m, i.e. whether the admissible
                   powers already account for the whole rank,
      v            v_0, ..., v_{order-1}, the v_k carrying their free
                   kernel parameters c1, c2, ... as symbols,
      free_params  the free parameters the obstruction still depends on
                   (it must not; in the paper's examples they all cancel).

    Raises NotCyclic when ker(lam id - K^F) is not one-dimensional.
    """
    N = KF.shape[0]
    s = sympy.Symbol('s')
    A = sympy.expand(lam * sympy.eye(N) - KF)
    right = A.nullspace()
    if len(right) != 1:
        raise NotCyclic(
            f'the eigenvalue {lam} has a {len(right)}-dimensional kernel, so '
            f'its generalized eigenspace is not a single Jordan block and '
            f'the factor is not cyclic (check cyclic_determinant first)')
    v0 = sympy.simplify(right[0])
    w = sympy.simplify(A.T.nullspace()[0]).T
    if m is None:
        m = _multiplicity(KF, lam)
    if max_order is None:
        max_order = m + 2

    v, vs, params = v0, [v0], []
    for k in range(1, max_order + 1):
        rhs = sympy.expand((G + (s + k - 1) * sympy.eye(N)) * v)
        obs = sympy.expand((w * rhs)[0, 0])
        if sympy.simplify(obs) != 0:
            powers = _roots(obs, s)
            return {'eigenvalue': sympy.simplify(lam), 'rank': m, 'order': k,
                    'obstruction': sympy.factor(obs), 'powers': powers,
                    'F': _classes(powers), 'complete': len(powers) == m,
                    'v': vs, 'method': 'recursion',
                    'free_params': sorted(obs.free_symbols & set(params),
                                          key=sympy.default_sort_key)}
        xs = sympy.symbols(f'z0:{N}')
        sol = sympy.linsolve((A, rhs), xs)
        if not sol:
            raise ValueError(
                f'the linear system at order {k} is inconsistent although '
                f'its solvability condition vanishes; this cannot happen')
        part = sympy.Matrix(list(sol)[0])
        part = part.subs({z: 0 for z in xs})       # kill whatever stays free
        c = sympy.Symbol(f'c{k}')
        params.append(c)
        v = sympy.expand(part + c * v0)
        vs.append(v)
    raise ValueError(
        f'the solvability condition still vanishes identically at order '
        f'{max_order}; raise max_order (or the factor is not of unramified '
        f'exponential type with rational residues)')


def _multiplicity(KF, lam, chi=None):
    x = sympy.Symbol('x')
    chi = sympy.Poly(_det(x * sympy.eye(KF.shape[0]) - KF)
                     if chi is None else chi, x)
    lin, m = sympy.Poly(x - lam, x), 0
    while True:
        quo, rem = sympy.div(chi, lin)
        if sympy.simplify(rem.as_expr()) != 0:
            return m
        chi, m = quo, m + 1


def _roots(obs, s):
    """Roots in s with multiplicity, as Fractions (rational by Thm. 3.6)."""
    poly = sympy.Poly(sympy.numer(sympy.together(obs)), s)
    out = []
    for r, mult in sorted(sympy.roots(poly).items(),
                          key=sympy.default_sort_key):
        rr = sympy.nsimplify(r)
        if not rr.is_rational:
            raise ValueError(
                f'the obstruction has the non-rational root {r}, so the '
                f'factor does not have rational residues')
        out.extend([Fraction(int(sympy.Rational(rr).p),
                             int(sympy.Rational(rr).q))] * mult)
    if len(out) != poly.degree():
        raise ValueError(f'only {len(out)} of {poly.degree()} roots of the '
                         f'obstruction were found')
    return out


def _classes(powers):
    """The multiset of classes mod Z, as representatives in [0, 1)."""
    return sorted(p - (p.numerator // p.denominator) for p in powers)


# ------------------------------------------------------ Theorem 4.5 verdict
#  (rank, exponents) forced on a *rational* X of dimension n
RATIONAL_TYPES = {
    2: [(1, (Fraction(0),))],
    3: [(1, (Fraction(0),)), (2, (Fraction(1, 2), Fraction(1, 2)))],
    4: [(1, (Fraction(0),)), (2, (Fraction(1, 2), Fraction(1, 2))),
        (3, (Fraction(0), Fraction(0), Fraction(0)))],
}
TYPE_NAMES = {(1, (Fraction(0),)): 'point',
              (2, (Fraction(1, 2), Fraction(1, 2))): 'curve',
              (3, (Fraction(0), Fraction(0), Fraction(0))): 'surface'}


def allowed_type(dim, m, F):
    """(ok, name): whether (m, F) is one of the types Theorem 4.5 allows on
    a rational variety of this dimension, and the name of that type.  ok is
    None when the theorem says nothing (dim outside 2..4)."""
    if dim not in RATIONAL_TYPES:
        return None, None
    key = (m, tuple(F))
    return key in RATIONAL_TYPES[dim], TYPE_NAMES.get(key)


# ---------------------------------------------------------------- pipeline
def invariants(X, K=None, var='q', primitive=True, M=None, Gr=None,
               very_general=False, max_order=None):
    """The whole Section 5 procedure: the disk connection, the Krylov test,
    and for every generic Hodge factor its rank and exponent multiset, with
    the Theorem 4.5 verdict.

    Simple eigenvalues are handled by the residue formula (so the whole
    spectrum is covered when c1* is regular semisimple); an eigenvalue of
    multiplicity > 1 that is rational in q goes through the recursion.  A
    multiple eigenvalue that is not rational in q is reported with its rank
    and no exponents.

    Returns a dict; report() renders it.
    """
    KF, G, names = disk_connection(X, K, var=var, primitive=primitive,
                                   M=M, Gr=Gr)
    rows = X.check_K(K)
    dim = X.n - len(rows)
    status, note = hodge_invariant_status(X, K, very_general)
    fano, fano_note = exponential_type_status(X, K)
    delta = cyclic_determinant(KF)
    out = {'dim': dim, 'K': [list(a) for a in rows], 'KF': KF, 'G': G,
           'names': names, 'delta': delta, 'cyclic': delta != 0,
           'hodge_status': status, 'hodge_note': note, 'fano': fano,
           'fano_note': fano_note, 'factors': []}
    x = sympy.Symbol('x')
    chi, Nad = chi_and_N(KF, G, x)
    for p, m in characteristic_factors(KF, x, chi):
        lam = _linear_root(p)
        rec = {'poly': p.as_expr(), 'eigenvalue': lam, 'rank': m,
               'n_eigenvalues': p.degree()}
        try:
            if m == 1:
                e = simple_exponent(KF, G, p, x, chi, Nad)
                if isinstance(e, Fraction):
                    rec.update(powers=[e], F=_classes([e]), complete=True,
                               method='residue', order=1,
                               obstruction=None, free_params=[])
                else:
                    rec['error'] = (f'the residue reduction {e} is not a '
                                    f'rational constant')
            elif lam is not None:
                rec.update(exponents(KF, G, lam, m, max_order))
            else:
                rec['error'] = (f'multiplicity {m} at an eigenvalue that is '
                                f'not rational in {var}: pass the eigenvalue '
                                f'to exponents() explicitly to follow it')
        except (NotCyclic, ValueError) as err:
            rec['error'] = str(err)
        if 'F' in rec:
            rec['allowed'], rec['type'] = allowed_type(dim, rec['rank'],
                                                       rec['F'])
        out['factors'].append(rec)

    usable = (status in ('full', 'odd', 'assumed') and out['cyclic']
              and fano)
    off = [f for f in out['factors'] if f.get('allowed') is False]
    graded = [f for f in out['factors'] if f.get('allowed') is not None]
    out['usable'] = usable
    if not usable:
        why = ('the Krylov determinant vanishes, so Step 1 does not '
               'certify a generic cyclic point' if not out['cyclic']
               else fano_note if not fano else note)
        out['irrational'], out['verdict'] = None, f'no verdict: {why}'
    elif dim not in RATIONAL_TYPES:
        out['irrational'], out['verdict'] = None, (
            f'no verdict: Theorem 4.5 covers dimensions 2 to 4 only, and '
            f'dim = {dim}; the ranks and exponents above are still the '
            f'invariants of the factors')
    elif off:
        f = off[0]
        out['irrational'], out['verdict'] = True, (
            f'the factor at lambda = {f["eigenvalue"]} has (m, F) = '
            f'({f["rank"]}, {{{{{_fmt(f["F"])}}}}}), which Theorem 4.5 does '
            f'not allow on a rational {dim}-fold, so X is irrational')
    elif graded:
        kinds = sorted({f['type'] for f in graded if f.get('type')})
        out['irrational'], out['verdict'] = False, (
            f'every computed factor is of allowed type ({", ".join(kinds)}), '
            f'so Theorem 4.5 gives no obstruction')
    else:
        out['irrational'], out['verdict'] = None, (
            'no verdict: no factor\'s exponents could be computed')
    # Proposition 5.5
    out['times_p1'] = bool(dim == 3 and usable and any(
        f.get('rank') == 2 and tuple(f.get('F', ())) !=
        (Fraction(1, 2), Fraction(1, 2)) for f in out['factors']
        if 'F' in f))
    return out


def _fmt(F):
    return ', '.join(str(f) for f in F)


def report(res):
    """The dict of invariants() as text."""
    L = []
    kk = res['K']
    L.append(f'dim {res["dim"]}'
             + (f', complete intersection {kk}' if kk else '')
             + f', basis {res["names"]}')
    L.append('K^F = -c1* :')
    L.append(sympy.pretty(res['KF']))
    G = res['G']
    L.append('G = diag(' + ', '.join(str(G[i, i])
                                     for i in range(G.shape[0])) + ')')
    L.append(f'Krylov determinant Delta = {res["delta"]}'
             + ('  (nonzero: the point is generic and K^F is cyclic)'
                if res['cyclic'] else '  (ZERO: Step 1 fails)'))
    L.append(f'H^Hdg [{res["hodge_status"]}]: {res["hodge_note"]}')
    L.append(f'Thm 3.6 [{"ok" if res["fano"] else "no"}]: {res["fano_note"]}')
    L.append('generic Hodge factors:')
    for f in res['factors']:
        head = (f'  lambda = {f["eigenvalue"]}' if f['eigenvalue'] is not None
                else f'  the {f["n_eigenvalues"]} roots of {f["poly"]}')
        L.append(f'{head}, rank m = {f["rank"]}')
        if 'error' in f:
            L.append(f'      no exponents: {f["error"]}')
            continue
        if f.get('obstruction') is not None:
            L.append(f'      (17) first nonzero at order k = {f["order"]}: '
                     f'{f["obstruction"]} = 0')
            if f['free_params']:
                L.append(f'      WARNING: it still depends on the free '
                         f'kernel parameters {f["free_params"]}')
        else:
            L.append('      simple eigenvalue: s = -N/chi\' modulo the factor')
        L.append(f'      s = {_fmt(f["powers"])}   '
                 f'F = {{{{{_fmt(f["F"])}}}}}'
                 + ('' if f['complete'] else
                    f'   (only {len(f["powers"])} powers for rank '
                    f'{f["rank"]}: the paper\'s scalar-ODE step is needed)')
                 + (f'   [{f["type"]} type]' if f.get('type') else
                    '   [not an allowed type]' if f.get('allowed') is False
                    else ''))
    L.append(res['verdict'])
    if res.get('times_p1'):
        L.append('Proposition 5.5: X x P^1 is irrational as well')
    return '\n'.join(L)
