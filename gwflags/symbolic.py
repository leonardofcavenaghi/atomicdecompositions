"""Symbolic backend: sympy under plain Python, Sage's symbolic ring when the
package is imported inside SageMath.

The rest of the package only touches computer-algebra through this interface:

    x(i), y(i), t      -- equivariant / quantum / limit variables (1-based i)
    rational(fr)       -- exact coefficient from fractions.Fraction
    linear(coeffs)     -- sum_i coeffs[i] * x_{i+1}   (LinearMapToPolynomial)
    cancel(e)          -- Cancel[Together[e]]
    is_zero(e)         -- Simplify[e] === 0
    subs(e, mapping)   -- substitution
    limit0(e, v)       -- Limit[e, v -> 0]
    variables(e)       -- Variables[e]
    randprime()        -- RandomPrime[{10000, 999999}]
    eigenvalues(mat)   -- Eigenvalues (list of lists in)
    evaluate_gw(e)     -- the notebook's final step: substitute every variable
                          by (random prime) * t and take t -> 0
"""


class SympyBackend:
    name = 'sympy'

    def __init__(self):
        import sympy
        self.sp = sympy
        self._t = sympy.Symbol('t')
        self._cache = {}

    def _sym(self, base, i):
        key = (base, i)
        if key not in self._cache:
            self._cache[key] = self.sp.Symbol(f'{base}{i}')
        return self._cache[key]

    def x(self, i):
        return self._sym('x', i)

    def y(self, i):
        return self._sym('y', i)

    @property
    def t(self):
        return self._t

    def rational(self, fr):
        return self.sp.Rational(fr.numerator, fr.denominator)

    def linear(self, coeffs):
        return sum((self.rational(c) * self.x(i + 1)
                    for i, c in enumerate(coeffs)), self.sp.Integer(0))

    def cancel(self, e):
        return self.sp.cancel(self.sp.together(e))

    def is_zero(self, e):
        return self.sp.simplify(e) == 0

    def subs(self, e, mapping):
        return self.sp.sympify(e).subs(mapping, simultaneous=True)

    def limit0(self, e, v):
        return self.sp.limit(e, v, 0)

    def variables(self, e):
        return sorted(self.sp.sympify(e).free_symbols, key=str)

    def randprime(self):
        return self.sp.randprime(10000, 999999)

    def eigenvalues(self, mat):
        M = self.sp.Matrix([[self.sp.sympify(v) for v in row] for row in mat])
        out = []
        for val, mult in M.eigenvals().items():
            out.extend([self.sp.simplify(val)] * mult)
        return out

    def mat_inverse(self, mat):
        M = self.sp.Matrix([[self.sp.sympify(v) for v in row] for row in mat])
        inv = M.inv()
        n = inv.shape[0]
        return [[inv[i, j] for j in range(n)] for i in range(n)]

    def to_fraction(self, e):
        from fractions import Fraction
        r = self.sp.nsimplify(e, rational=True)
        return Fraction(int(r.p), int(r.q))

    def evaluate_gw(self, e):
        """Substitute every free variable by prime*t, then t -> 0."""
        e = self.cancel(e)
        vs = [v for v in self.variables(e) if v != self._t]
        if not vs:
            return e
        e = self.subs(e, {v: self.randprime() * self._t for v in vs})
        return self.limit0(e, self._t)


class SageBackend:
    name = 'sage'

    def __init__(self):
        from sage.all import SR, QQ, var, random_prime, limit, matrix
        self.SR, self.QQ = SR, QQ
        self._var, self._random_prime = var, random_prime
        self._limit, self._matrix = limit, matrix
        self._t = var('t')
        self._cache = {}

    def _sym(self, base, i):
        key = (base, i)
        if key not in self._cache:
            self._cache[key] = self._var(f'{base}{i}')
        return self._cache[key]

    def x(self, i):
        return self._sym('x', i)

    def y(self, i):
        return self._sym('y', i)

    @property
    def t(self):
        return self._t

    def rational(self, fr):
        return self.QQ(fr.numerator) / self.QQ(fr.denominator)

    def linear(self, coeffs):
        return sum((self.rational(c) * self.x(i + 1)
                    for i, c in enumerate(coeffs)), self.SR(0))

    def cancel(self, e):
        return self.SR(e).simplify_rational()

    def is_zero(self, e):
        return self.SR(e).simplify_rational().is_zero()

    def subs(self, e, mapping):
        return self.SR(e).subs(mapping)

    def limit0(self, e, v):
        return self._limit(self.SR(e), **{str(v): 0})

    def variables(self, e):
        return sorted(self.SR(e).variables(), key=str)

    def randprime(self):
        return self._random_prime(999999, lbound=10000)

    def eigenvalues(self, mat):
        M = self._matrix(self.SR, [[self.SR(v) for v in row] for row in mat])
        return M.eigenvalues()

    def mat_inverse(self, mat):
        M = self._matrix(self.SR, [[self.SR(v) for v in row] for row in mat])
        inv = M.inverse()
        n = inv.nrows()
        return [[inv[i, j] for j in range(n)] for i in range(n)]

    def to_fraction(self, e):
        from fractions import Fraction
        q = self.QQ(e)
        return Fraction(int(q.numerator()), int(q.denominator()))

    def evaluate_gw(self, e):
        e = self.cancel(e)
        vs = [v for v in self.variables(e) if v != self._t]
        if not vs:
            return e
        e = self.subs(e, {v: self.randprime() * self._t for v in vs})
        return self.limit0(e, self._t)


class NumericBackend:
    """Exact evaluation backend: the equivariant variables x_i carry fixed
    random rational values, so every localization quantity is a plain
    ``fractions.Fraction`` and no CAS is involved.  Valid because each raw
    localization sum is homogeneous: after the degree gate (see
    localization.expected_degree) the sum is a constant, and evaluating the
    constant at one generic point IS the invariant.  Callers evaluate at two
    independent points to guard against accidental pole/degeneracy."""

    name = 'numeric'

    def __init__(self, seed=None):
        import random
        from fractions import Fraction
        self._rng = random.Random(seed)
        self._point = {}
        self._F = Fraction

    def x(self, i):
        if i not in self._point:
            while True:
                v = self._rng.randrange(10 ** 5, 10 ** 7)
                if v not in self._point.values():
                    break
            self._point[i] = self._F(v)
        return self._point[i]

    def rational(self, fr):
        return fr          # already an exact Rational; no re-normalization

    def linear(self, coeffs):
        return sum((c * self.x(i + 1) for i, c in enumerate(coeffs)),
                   self._F(0))

    def cancel(self, e):
        return e

    def is_zero(self, e):
        # exact for the quantities tested (sums of positive terms at
        # positive points); a genuine accidental zero is caught by the
        # two-point comparison one level up
        return e == 0


def get_backend(prefer=None):
    """Sage when available (or requested), sympy otherwise."""
    if prefer in (None, 'sage'):
        try:
            import sage.all  # noqa: F401
            return SageBackend()
        except ImportError:
            if prefer == 'sage':
                raise
    return SympyBackend()
