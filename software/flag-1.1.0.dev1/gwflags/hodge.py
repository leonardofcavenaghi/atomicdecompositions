"""Hodge diamonds only, extracted from the exact flag Hodge calculator."""
from collections import Counter, deque, OrderedDict


from fractions import Fraction as F


from functools import lru_cache, reduce


from itertools import combinations_with_replacement


from math import gcd, prod, factorial


import threading


from types import SimpleNamespace


import argparse


import ast


import json


from .rootsystem import RootSystemData, dot, parse_algebra


def _integer(value, label="value"):
    value = F(value)
    if value.denominator != 1:
        raise ArithmeticError(f"{label} must be integral, got {value}")
    return int(value)


def _chern(roots, degree):
    out = [F(1)] + [F(0)] * degree
    for root in roots:
        for k in range(degree, 0, -1):
            out[k] += root * out[k - 1]
    return out


def _quotient(numerator, denominator, degree):
    out = []
    for k in range(degree + 1):
        out.append(numerator[k] - sum(denominator[j] * out[k-j]
                                     for j in range(1, k+1)))
    return out


def _partitions(n, minimum=1):
    if n == 0:
        yield ()
    for k in range(minimum, n+1):
        for tail in _partitions(n-k, k):
            yield (k,) + tail


def _jsonable(value):
    if isinstance(value, F):
        return int(value) if value.denominator == 1 else str(value)
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(v) for v in value]
    return value


def _log_hirzebruch(degree, y):
    """log(Q_y(t)/(1+y)), exact coefficients through the requested degree."""
    # Todd(t) is the reciprocal of (1-exp(-t))/t.
    denominator = [F((-1)**k, factorial(k+1)) for k in range(degree+1)]
    todd = _quotient([F(1)]+[F(0)]*degree, denominator, degree)
    if degree:
        todd[1] -= F(y, 1+y)
    logarithm = [F(0)]
    for n in range(1, degree+1):
        logarithm.append(todd[n] - sum((k*logarithm[k]*todd[n-k]
                                      for k in range(1, n)), F(0))/n)
    return tuple(logarithm)


def _interpolate_integer_nodes(values):
    """Newton interpolation at 0,...,d, returned in the ordinary power basis."""
    degree = len(values)-1
    result = [F(0)]*(degree+1)
    basis = [F(1)]
    differences = list(values)
    for k in range(degree+1):
        for j, coefficient in enumerate(basis):
            result[j] += differences[0]*coefficient
        differences = [b-a for a, b in zip(differences, differences[1:])]
        following = [F(0)]*(len(basis)+1)
        for j, coefficient in enumerate(basis):
            following[j] -= F(k, k+1)*coefficient
            following[j+1] += coefficient/F(k+1)
        basis = following
    return [_integer(v, 'chi_y coefficient') for v in result]


def _validate_algebra(algebra):
    try:
        factors = parse_algebra(algebra)
    except (ValueError, IndexError, TypeError, AttributeError) as exc:
        raise ValueError('Use an algebra such as A2, G2 or A2xA2') from exc
    for family, rank in factors:
        valid = ((family in ('A', 'B', 'C') and rank >= 1)
                 or (family == 'D' and rank >= 4)
                 or (family == 'E' and rank in (6, 7, 8))
                 or (family == 'F' and rank == 4) or (family == 'G' and rank == 2))
        if not valid:
            raise ValueError(f'Unsupported finite root system {family}{rank}')
    if not factors:
        raise ValueError('Specify a nonempty semisimple algebra')
    return factors


def parse_bundle(spec, X):
    """Legacy rows, or a restricted AST of the GWflags bundle constructors.

    This deliberately does not use eval; attributes, indexing and arbitrary
    Python code are rejected. Existing HomogeneousBundle objects also work.
    """
    from . import bundles
    if not isinstance(spec, str):
        return [] if spec is None else spec
    if not spec.strip():
        return []
    if not any(c.isalpha() for c in spec):
        try:
            return [[int(v) for v in row.split(',')] for row in spec.split(';')]
        except ValueError as exc:
            raise ValueError('Use rows like "1,1;2,2" for line bundles') from exc
    allowed = {n: getattr(bundles, n) for n in
               ('O', 'taut_sub', 'taut_quot', 'dual', 'osum', 'tensor', 'sym', 'wedge')}

    def visit(node):
        if isinstance(node, ast.Name) and node.id == 'X':
            return X
        if isinstance(node, ast.Constant) and type(node.value) in (int, str):
            return node.value
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            val = visit(node.operand)
            if type(val) is int:
                return -val
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in allowed and all(k.arg == 'name' for k in node.keywords):
                args = [visit(a) for a in node.args]
                if node.func.id in ('taut_sub', 'taut_quot'):
                    if len(args) < 2 or args[1] not in X.keep:
                        raise ValueError('A tautological bundle node must be a kept root')
                if node.func.id in ('sym', 'wedge'):
                    if not args or type(args[0]) is not int or args[0] < 0:
                        raise ValueError('Symmetric/exterior powers must be nonnegative integers')
                return allowed[node.func.id](*args, **{k.arg: visit(k.value)
                                                       for k in node.keywords})
        raise ValueError('Only GWflags bundle constructors and integer arguments are allowed')
    try:
        return visit(ast.parse(spec, mode='eval').body)
    except (SyntaxError, TypeError, IndexError) as exc:
        raise ValueError(f'Invalid bundle expression: {exc}') from exc


class FlagHodge:
    def __init__(self, algebra, roots_that_stay, max_fixed_points=20000):
        _validate_algebra(algebra)
        self.rs = RootSystemData(algebra)
        self.keep = list(roots_that_stay)
        n = self.rs.rank
        if not self.keep or len(set(self.keep)) != len(self.keep) or any(
                type(i) is not int or not 1 <= i <= n for i in self.keep):
            raise ValueError(f'Kept roots must be distinct indices in 1..{n}')
        if type(max_fixed_points) is not int or max_fixed_points < 1:
            raise ValueError('max_fixed_points must be a positive integer')
        self.levi = [i for i in range(1, n+1) if i not in self.keep]
        self.root_indices = [q for q, r in enumerate(self.rs.positive_roots)
                             if any(r[i-1] for i in self.keep)]
        self.dimension = len(self.root_indices)
        self.tangent_roots = [self.rs.omega_basis(self.rs.positive_roots[q])
                              for q in self.root_indices]
        self.delta = tuple(sum(r[i] for r in self.tangent_roots) for i in range(n))
        self.polarization = tuple(int(i+1 in self.keep) for i in range(n))
        # Compatibility with existing O/taut_sub/taut_quot constructors.
        self.wd = SimpleNamespace(roots_that_stay=self.keep,
                                 reduced_root_indices=self.root_indices)
        self.words = []
        self.orbit = {}
        queue = deque([(self.polarization, ())])
        self.orbit[self.polarization] = 0
        while queue:
            weight, word = queue.popleft()
            self.words.append(word)
            for i in range(1, n+1):
                reflected = self.reflect(weight, i)
                if reflected not in self.orbit:
                    if len(self.orbit) >= max_fixed_points:
                        raise ValueError(f'Flag exceeds {max_fixed_points} fixed points; '
                                         'increase max_fixed_points explicitly')
                    self.orbit[reflected] = len(self.orbit)
                    queue.append((reflected, (i,) + word))
        self.identity = tuple(tuple(int(i == j) for j in range(n)) for i in range(n))
        self.matrices = [self._matrix(w) for w in self.words]
        self.matrix_index = {m: i for i, m in enumerate(self.matrices)}
        self._ambient_evaluations = {}
        # Per-instance bounded memoization: evicting a flag also releases its BWB cache.
        self.bwb = lru_cache(maxsize=8192)(self.bwb)


    def reflect(self, weight, node):
        a = self.rs.cartan_matrix[node-1]
        return tuple(x - weight[node-1] * y for x, y in zip(weight, a))


    def act(self, word, weight):
        for i in reversed(word):
            weight = self.reflect(weight, i)
        return tuple(weight)


    def _append(self, matrix, node):
        """Root-basis columns of w*s_node, without ambient orthogonal matrices."""
        a = matrix[node-1]
        return tuple(tuple(x-self.rs.cartan_matrix[j][node-1]*y
                           for x, y in zip(col, a)) for j, col in enumerate(matrix))


    def _matrix(self, word):
        m = self.identity
        for node in word:
            m = self._append(m, node)
        return m


    def _point(self, seed=0):
        # Positive values for every simple root => no root denominator vanishes.
        alpha = [i+1 if seed == 0 else (i+2)**2 + 1 for i in range(self.rs.rank)]
        omega = [sum(F(self.rs.cart_matrix[j][i])*alpha[j]
                     for j in range(self.rs.rank)) for i in range(self.rs.rank)]
        return alpha, omega


    def bwb(self, weight):
        """Line-bundle BWB; weight is in full fundamental-weight coordinates."""
        weight = tuple(weight)
        if len(weight) != self.rs.rank or any(type(x) is not int for x in weight):
            raise ValueError('BWB needs integral full-rank fundamental-weight coordinates')
        if any(weight[i-1] for i in self.levi):
            raise ValueError('This weight does not define a line bundle on G/P')
        shifted = tuple(v+1 for v in weight)
        if any(dot(shifted, co) == 0 for co in self.rs.coroots):
            return {'degree': None, 'dimension': 0, 'highest_weight': None,
                    'singular': True, 'euler_characteristic': 0}
        degree = 0
        while any(x < 0 for x in shifted):
            node = next(i+1 for i, x in enumerate(shifted) if x < 0)
            shifted = self.reflect(shifted, node)
            degree += 1
        dimension = prod(F(dot(shifted, co), sum(co)) for co in self.rs.coroots)
        dimension = _integer(dimension, 'Weyl dimension')
        return {'degree': degree, 'dimension': dimension,
                'highest_weight': tuple(x-1 for x in shifted), 'singular': False,
                'euler_characteristic': (-1)**degree * dimension}


    def _bundle(self, spec):
        from .bundles import HomogeneousBundle
        bundle = parse_bundle(spec, self)
        n = self.rs.rank
        if isinstance(bundle, HomogeneousBundle):
            if bundle.X.rs.name != self.rs.name or list(bundle.X.wd.roots_that_stay) != self.keep:
                raise ValueError('Bundle belongs to a different flag or kept-root ordering')
            weights = []
            for fiber in bundle.weights:
                if len(fiber) != self.rs.dim_ort:
                    raise ValueError('Bundle weight has the wrong orthogonal dimension')
                weights.append(tuple(_integer(-F(2*dot(fiber, a), dot(a, a)),
                                               'Bundle weight')
                                     for a in self.rs.simple_roots_ort))
            multiset = Counter(weights)
            for node in self.levi:
                if Counter(self.reflect(w, node) for w in weights) != multiset:
                    raise ValueError('Bundle weights are not invariant under the Levi Weyl group')
            split = all(all(w[i-1] == 0 for i in self.levi) for w in weights)
            rows = [[w[i-1] for i in self.keep] for w in weights] if split else None
            name = bundle.name
        else:
            if not isinstance(bundle, (list, tuple)):
                raise ValueError('Bundle must be multidegree rows or a HomogeneousBundle')
            rows = []
            weights = []
            for row in bundle:
                if not isinstance(row, (list, tuple)) or len(row) != len(self.keep):
                    raise ValueError(f'Each bundle row needs {len(self.keep)} entries; '
                                     'separate summands with semicolons')
                if any(type(v) is not int or v < 0 for v in row):
                    raise ValueError('Line-bundle rows must contain nonnegative integers')
                rows.append(list(row))
                w = [0]*n
                for i, v in zip(self.keep, row):
                    w[i-1] = v
                weights.append(tuple(w))
            name = ' + '.join('O('+','.join(map(str, r))+')' for r in rows) or '0'
        if rows is not None and any(v < 0 for row in rows for v in row):
            raise ValueError('Negative line-bundle degrees have no regular nonempty section')
        return weights, rows, name


    def _local_data(self, weights, degree, seed=0):
        _, point = self._point(seed)
        out = []
        divisors = [tuple(int(j == i-1) for j in range(self.rs.rank)) for i in self.keep]
        if seed not in self._ambient_evaluations:
            self._ambient_evaluations[seed] = [
                ([-dot(self.act(word, root), point) for root in self.tangent_roots],
                 [-dot(self.act(word, w), point) for w in divisors]) for word in self.words]
        for word, (tangent, divisor_values) in zip(self.words, self._ambient_evaluations[seed]):
            bundle = [-dot(self.act(word, weight), point) for weight in weights]
            c = _quotient(_chern(tangent, degree), _chern(bundle, degree), degree)
            out.append({'chern': c, 'factor': F(prod(bundle), prod(tangent)),
                        'divisors': divisor_values, 'tangent': tangent, 'bundle': bundle})
        return out


    def _chi_y(self, local, degree, *, only_zero=False, progress=None):
        """Exact HRR localization; no floating point or section invariance is used.

        Evaluate at y=0,...,d and interpolate the polynomial of degree <=d.
        Logarithmic series reduce products over tangent/bundle weights to power sums.
        """
        powers = [[sum(a**k for a in row['tangent'])-sum(b**k for b in row['bundle'])
                   for k in range(degree+1)] for row in local]
        values = []
        for y in range(1 if only_zero else degree+1):
            if progress:
                progress(f'Exact Hirzebruch genus: evaluation {y+1}/{1 if only_zero else degree+1}')
            logarithm = _log_hirzebruch(degree, y)
            total = F(0)
            for row, power in zip(local, powers):
                exponential = [F(1)]
                for n in range(1, degree+1):
                    exponential.append(sum(k*logarithm[k]*power[k]*exponential[n-k]
                                           for k in range(1, n+1))/n)
                total += row['factor']*exponential[degree]*(1+y)**degree
            values.append(_integer(total, 'Hirzebruch evaluation'))
        return values[0] if only_zero else _interpolate_integer_nodes(values)


    def _koszul(self, weights, dimension):
        zero = (0,)*self.rs.rank
        sums = Counter({(0, zero): 1})
        for weight in weights:
            extra = Counter()
            for (k, w), mult in sums.items():
                extra[k+1, tuple(x-y for x, y in zip(w, weight))] += mult
            sums.update(extra)
            if len(sums) > 100000:
                raise ValueError('Koszul complex exceeds 100000 distinct weight terms')
        groups = Counter()
        terms = []
        chi = 0
        for (k, weight), mult in sorted(sums.items()):
            cohom = self.bwb(weight)
            chi += (-1)**k * mult * cohom['euler_characteristic']
            if cohom['dimension']:
                q = cohom['degree']
                groups[-k, q] += mult * cohom['dimension']
                terms.append({'koszul_degree': -k, 'sheaf_cohomology_degree': q,
                              'weight': weight, 'multiplicity': mult, **cohom})
        uncertain_totals = set()
        for p, q in groups:
            for r in range(1, len(weights)+1):
                if (p+r, q-r+1) in groups:
                    uncertain_totals.update((p+q, p+q+1))
        upper = [sum(v for (p, q), v in groups.items() if p+q == j)
                 for j in range(dimension+1)]
        h = [None if j in uncertain_totals else upper[j] for j in range(dimension+1)]
        # For a known nonempty projective zero locus, constants survive.
        if upper[0] == 1:
            h[0] = 1
        return {'euler_characteristic': chi, 'h_q_O': h, 'e1_upper_bounds': upper,
                'unresolved_differential_totals': sorted(uncertain_totals), 'terms': terms}


    def analyze(self, K=None, *, verify=True, progress=None):
        log = progress or (lambda _: None)
        mode, want_hodge, h11 = "hodge", True, None
        weights, rows, bundle_name = self._bundle(K)
        if rows is None or any(v <= 0 for row in rows for v in row):
            raise ValueError("Hodge diamonds require a sum of ample line bundles (all multidegrees positive), or the ambient flag")
        N, r = self.dimension, len(weights)
        d = N-r
        if d < 0:
            raise ValueError('Bundle rank exceeds ambient dimension: no nonempty regular zero locus')
        if h11 is not None and (d != 3 or type(h11) is not int or h11 < 1):
            raise ValueError('An external h11 must be a positive integer for a threefold')
        ample = r > 0 and rows is not None and all(v > 0 for row in rows for v in row)
        antican = tuple(self.delta[i]-sum(w[i] for w in weights) for i in range(self.rs.rank))
        c1kept = [antican[i-1] for i in self.keep]
        log(f'{self.rs.name}/P: ambient dimension {N}, zero-locus dimension {d}, '
            f'{len(self.words)} fixed points')
        local = self._local_data(weights, d)

        def integrate(partition=(), divisors=(), data=local):
            if sum(partition)+len(divisors) != d:
                raise ValueError('Integration requires total complex degree dim(Y)')
            return _integer(sum(row['factor'] * prod(row['chern'][k] for k in partition)
                                * prod(row['divisors'][j] for j in divisors) for row in data),
                            'intersection number')

        partitions = list(_partitions(d)) if mode != 'hodge' else (
            [()] if d == 0 else [(1,)] if d == 1 else [(1, 1), (2,)] if d == 2
            else [(1, 2), (3,)] if d == 3 else [(d,)])
        numbers = {'*'.join('c'+str(k) for k in p) or '1': integrate(p) for p in partitions}
        euler = numbers['c'+str(d)] if d else numbers['1']
        intersections = {','.join(str(self.keep[j]) for j in inds) or '1': integrate(divisors=inds)
                         for inds in combinations_with_replacement(range(len(self.keep)), d)} if mode != 'hodge' else {}
        degree = _integer(sum(row['factor']*sum(row['divisors'])**d for row in local))
        if verify:
            log('Checking characteristic numbers at a second exact torus point')
            other = self._local_data(weights, d, seed=1)
            for p in partitions:
                if integrate(p) != integrate(p, data=other):
                    raise ArithmeticError('Localization checks disagree')
        chern = {}
        if mode == 'full':
            log('Expanding Chern classes in the ambient Schubert basis')
            chern = self._schubert_chern(local, d)
        chi = None
        if d == 0:
            chi = degree
        elif d == 1:
            chi = F(euler, 2)
        elif d == 2:
            chi = F(numbers['c1*c1']+euler, 12)
        elif d == 3:
            chi = F(numbers['c1*c2'], 24)
        if chi is not None:
            chi = _integer(chi, 'holomorphic Euler characteristic')
        chi_y = None
        chi_y_method = None
        hrr_checked = False
        if r and want_hodge:
            chi_y = self._chi_y(local, d, progress=log)
            chi_y_method = 'Hirzebruch-Riemann-Roch with exact torus localization'
            if verify and chi_y != self._chi_y(other, d):
                raise ArithmeticError('Hirzebruch genus disagrees at two torus points')
            hrr_checked = verify
            if chi is not None and chi != chi_y[0]:
                raise ArithmeticError('Todd formula and Hirzebruch genus disagree')
            chi = chi_y[0]
        elif r and chi is None:
            chi = self._chi_y(local, d, only_zero=True)
            if verify and chi != self._chi_y(other, d, only_zero=True):
                raise ArithmeticError('Todd genus disagrees at two torus points')
        empty = degree == 0
        if degree < 0:
            raise ValueError('Negative degree is incompatible with a smooth effective regular zero locus')
        koszul = None
        structure = [None]*(d+1)
        if rows is not None and not empty and want_hodge:
            log('Computing line-bundle cohomology by Borel-Weil-Bott and Koszul')
            koszul = self._koszul(weights, d)
            if chi is not None and chi != koszul['euler_characteristic']:
                raise ArithmeticError('BWB/Koszul and Todd-genus computations disagree')
            chi = koszul['euler_characteristic']
            structure = koszul['h_q_O'][:]
        if r == 0:
            structure = [1]+[0]*d
            chi = 1
        elif ample and d > 0 and not empty:
            structure = [1]+[0]*(d-1)+[(-1)**d*(chi-1)]
        elif d == 0:
            structure = [degree]
        # Euler characteristic can resolve one unknown, but not a differential.
        if chi is not None and structure.count(None) == 1:
            j = structure.index(None)
            structure[j] = (-1)**j*(chi-sum((-1)**k*x for k, x in enumerate(structure)
                                          if x is not None))
        if empty:
            structure = [0]*(d+1)
        h = [[None]*(d+1) for _ in range(d+1)]

        def assign(p, q, value):
            if value is not None:
                value = _integer(value, 'Hodge number')
                if value < 0:
                    raise ArithmeticError('Negative Hodge number; check the geometric hypotheses')
            for a, b in {(p, q), (q, p), (d-p, d-q), (d-q, d-p)}:
                if h[a][b] is not None and value is not None and h[a][b] != value:
                    raise ArithmeticError('Inconsistent Hodge symmetry or external h11')
                if value is not None:
                    h[a][b] = value

        for q, v in enumerate(structure if want_hodge else []):
            assign(0, q, v)
        if not want_hodge:
            pass
        elif r == 0 or empty:
            h = [[0]*(d+1) for _ in range(d+1)]
            if not empty:
                for word in self.words:
                    h[len(word)][len(word)] += 1
        elif ample:
            if h11 is not None and h11 != len(self.keep):
                raise ValueError('External h11 contradicts the Lefschetz theorem')
            ambient = Counter(map(len, self.words))
            for p in range(d+1):
                for q in range(d+1):
                    if p+q < d:
                        assign(p, q, ambient[p] if p == q else 0)
            for p in range(d+1):
                known = sum((-1)**q*h[p][q] for q in range(d+1) if q != d-p)
                assign(p, d-p, (-1)**(d-p)*(chi_y[p]-known))
        elif d == 1 and structure[0] is not None:
            assign(0, 1, F(2*structure[0]-euler, 2))
        elif d == 2 and all(v is not None for v in structure):
            c, q, pg = structure
            assign(1, 1, euler-2*c+4*q-2*pg)
        elif d == 3:
            if h11 is not None:
                assign(1, 1, h11)
            if h[1][1] is not None and all(v is not None for v in structure):
                c, q, h02, pg = structure
                assign(1, 2, c-2*q+2*h02-pg+h[1][1]-F(euler, 2))
        complete = all(v is not None for row in h for v in row)
        if h11 is not None and h[1][1] is not None and h[1][1] != h11:
            raise ValueError('External h11 contradicts the independently computed value')
        if r == 0 and want_hodge:
            chi_y = [(-1)**p*h[p][p] for p in range(d+1)]
            chi_y_method = 'Ambient Schubert-cell decomposition'
        if chi_y is not None:
            if sum((-1)**p*v for p, v in enumerate(chi_y)) != euler:
                raise ArithmeticError('chi_y(-1) disagrees with the top Chern number')
            if any(chi_y[d-p] != (-1)**d*chi_y[p] for p in range(d+1)):
                raise ArithmeticError('Hirzebruch genus fails Serre duality')
            if complete and any(sum((-1)**q*h[p][q] for q in range(d+1)) != chi_y[p]
                                for p in range(d+1)):
                raise ArithmeticError('Hodge diamond disagrees with chi(Omega^p)')
        betti = [None if any(h[p][k-p] is None for p in range(max(0, k-d), min(d, k)+1))
                 else sum(h[p][k-p] for p in range(max(0, k-d), min(d, k)+1))
                 for k in range(2*d+1)]
        if complete and sum((-1)**k*b for k, b in enumerate(betti)) != euler:
            raise ArithmeticError('Hodge diamond fails the Euler-characteristic check')
        return _jsonable(dict(dimension=d, ambient_dimension=N,
            hodge_certified=complete, hodge_complete=complete,
            hodge_matrix=h if complete else None,
            hodge_diamond=[[h[p][k-p] for p in range(max(0,k-d),min(d,k)+1)]
                           for k in range(2*d+1)] if complete else None,
            betti_numbers=betti, euler=euler, chi_y=chi_y,
            verification=dict(two_torus_points=verify, hodge_euler_check=complete,
                              bwb_todd_check=koszul is not None),
            assumptions=["Smooth regular zero locus of the expected codimension"],
            scope="Hodge dimensions; no primitive quantum multiplication is inferred"))


def hodge_report(algebra, keep, K=None, **options):
    return FlagHodge(algebra, keep).analyze(K, **options)
