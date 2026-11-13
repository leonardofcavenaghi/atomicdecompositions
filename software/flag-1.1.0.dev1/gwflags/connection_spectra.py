"""Exact exponent classes from the scalar-filtration implementation.

Convention: K=-M, nabla=d/du+K/u**2+G/u.
"""
import sympy as sp
from sympy.polys.matrices import DomainMatrix as DM
u, s, t = sp.symbols("u s t")

def eval_poly_matrix(f, K):
    out = sp.zeros(K.rows)
    for c in sp.Poly(f, t).all_coeffs():
        out = out*K+c*sp.eye(K.rows)
    return out


def exponents(poly):
    poly = sp.Poly(poly, s)
    roots = sp.roots(poly.as_expr(), s)
    if sum(roots.values()) != poly.degree():
        raise ValueError('Indicial polynomial does not split into the available exact roots')
    classes = {}
    for root, mult in roots.items():
        if root.is_rational is not True:
            raise ValueError('Non-rational exponent requires explicit treatment: '+str(root))
        key = str(sp.Mod(root, 1))
        classes[key] = classes.get(key, 0)+int(mult)
    return {'representatives': {str(x): int(m) for x, m in roots.items()}, 'classes_mod_Z': classes}


def semisimple_residue(K, G, factor, multiplicity):
    degree = sp.degree(factor, t)
    if degree == 1:
        field = sp.QQ
        z = field.from_sympy(sp.solve(factor, t)[0])
    else:
        field = sp.QQ.alg_field_from_poly(sp.Poly(factor, t), alias='a')
        z = field.unit
    kd, gd = [DM.from_Matrix(A).convert_to(field) for A in (K, G)]
    A = kd-DM.eye(K.rows, field).scalarmul(z)
    V = A.nullspace(divide_last=True).transpose()
    W = A.transpose().nullspace(divide_last=True)
    assert V.shape[1] == W.shape[0] == multiplicity
    pair = W*V
    R = -(pair.inv()*W*gd*V)
    assert (A*V).is_zero_matrix and (W*A).is_zero_matrix
    cp = R.charpoly()
    # Coefficients should be rational for the present spectra, uniformly for
    # every conjugate eigenvalue. Reject rather than recognize numerically.
    rational_coefficients = []
    for c in cp:
        if field == sp.QQ:
            rational_coefficients.append(field.to_sympy(c))
        else:
            parts = c.to_list()
            if len(parts) > 1:
                raise ValueError('Residue characteristic polynomial depends on the algebraic eigenvalue')
            rational_coefficients.append(sp.QQ.to_sympy(parts[0]) if parts else sp.Integer(0))
    polynomial = sp.Poly.from_list(rational_coefficients, s).as_expr()
    return {'method': 'exact_semisimple_residue', 'residue_charpoly': str(sp.factor(polynomial)),
            'geometric_multiplicity': multiplicity,
            'field_degree': int(degree),
            'checks': {'left_right_kernel_dimensions': True, 'pairing_invertible': True,
                       'kernel_identities': True, 'residue_charpoly_rational': True},
            **exponents(polynomial)}


def sampled_pivots(rows):
    B = sp.Matrix.vstack(*rows)
    for point in (1, 2, 3, 5, 7):
        pivots = B.subs(u, point).rref()[1]
        if len(pivots) == B.rows:
            return list(pivots), point
    return None, None


def relation_to_basis(rows, new):
    """Exact relation new=sum coeff_i rows_i, or None if independent.

    A sampled invertible minor only chooses pivots. The resulting relation
    is always checked as a polynomial identity in every column.
    """
    pivots, point = sampled_pivots(rows)
    if pivots is None:
        raise RuntimeError('Could not find a nonsingular sampling minor for the existing basis')
    B = sp.Matrix.vstack(*rows)
    if sp.Matrix.vstack(B, new).subs(u, point).rank() > B.rows:
        return None
    A = B.extract(range(B.rows), pivots).T
    domain = sp.QQ.poly_ring(u)
    rhs = DM.from_Matrix(new.extract([0], pivots).T).convert_to(domain)
    num, den = DM.from_Matrix(A).convert_to(domain).solve_den(rhs)
    residual = DM.from_Matrix(new).convert_to(domain).scalarmul(den)-num.transpose()*DM.from_Matrix(B).convert_to(domain)
    if not residual.is_zero_matrix:
        return None
    nums = list(num.to_Matrix())
    den = domain.to_sympy(den)
    return nums, den, {'sample_point': point, 'pivot_columns': pivots,
                       'minor_determinant_at_sample': str(A.subs(u, point).det()),
                       'relation_identity': True}


def scalar_filtration(K, G):
    """Triangular differential cyclic filtration over Q(u).

    Each covector chain is stable modulo the preceding chains. The scalar
    equations describe successive solution subquotients; their exponent
    multisets add, including when the full connection has no cyclic constant
    covector. All relations and independence witnesses are exact.
    """
    n = K.rows
    rows, blocks = [], []
    for seed in range(n):
        first = sp.eye(n)[seed, :]
        if rows and relation_to_basis(rows, first) is not None:
            continue
        offset = len(rows)
        current = first
        while True:
            rows.append(current)
            new = (u*u*current.diff(u)-current*(K+u*G)).applyfunc(sp.expand)
            relation = relation_to_basis(rows, new)
            if relation is not None:
                nums, den, witness = relation
                coeffs = [-sp.expand(x) for x in nums[offset:]]+[sp.expand(den)]
                common = sp.gcd_list(coeffs)
                coeffs = [sp.cancel(x/common) for x in coeffs]
                blocks.append({'seed_covector_index': seed, 'offset': offset,
                    'order': len(coeffs)-1, 'coefficients': [str(x) for x in coeffs],
                    'relation_numerators': [str(x) for x in nums],
                    'relation_denominator': str(den), 'witness': witness})
                break
            current = new
            if len(rows) >= n:
                raise AssertionError('A full row basis must span its next derivative')
        if len(rows) == n:
            break
    assert len(rows) == n and sum(b['order'] for b in blocks) == n
    pivots, point = sampled_pivots(rows)
    determinant = sp.Matrix.vstack(*rows).subs(u, point).det()
    assert determinant != 0
    return {'blocks': blocks, 'total_order': n,
            'full_basis_witness': {'u': point, 'determinant': str(determinant)},
            'all_relations_verified': True}


def shifted_indicial(coefficients, z):
    coefficients = list(map(sp.sympify, coefficients))
    terms = {}
    for j in range(len(coefficients)):
        a = sum(coefficients[k]*sp.binomial(k, j)*(-z)**(k-j) for k in range(j, len(coefficients)))
        for (d,), c in sp.Poly(sp.expand(a), u).terms():
            terms[d+j] = terms.get(d+j, 0)+c*sp.rf(s, j)
    for degree in sorted(terms):
        p = sp.expand(terms[degree])
        if p != 0:
            return sp.factor(p), degree
    raise ValueError('Zero scalar operator')


def connection_report(matrix, grading, specialization=None, progress=None):
    """Exact spectral factors and exponent multisets, with unresolved factors explicit."""
    M, G = sp.Matrix(matrix), sp.Matrix(grading)
    if not M.rows or M.rows != M.cols or G.shape != M.shape:
        raise ValueError('Multiplication and grading must be matching square matrices')
    values = {v: sp.Integer(1) for v in M.free_symbols | G.free_symbols}
    values.update(specialization or {})
    K, G = -M.subs(values, simultaneous=True), G.subs(values, simultaneous=True)
    if any(v.is_Rational is not True for v in list(K)+list(G)):
        raise ValueError('Exact exponent analysis currently requires rational specialization')
    sectors, filtration = [], None
    for factor, mult in sp.factor_list(K.charpoly(t).as_expr(), t)[1]:
        degree, mult = int(sp.degree(factor, t)), int(mult)
        item = dict(eigenvalue_factor_K=str(factor), factor_degree=degree,
                    multiplicity_per_root=mult, total_rank=degree*mult)
        if progress:
            progress(f'Connection factor {factor}, rank per root {mult}')
        try:
            geometric = (K.rows-DM.from_Matrix(eval_poly_matrix(factor, K)).convert_to(sp.QQ).rank())//degree
            item['geometric_multiplicity_per_root'] = geometric
            if geometric == mult:
                item.update(semisimple_residue(K, G, factor, mult))
            else:
                if degree != 1:
                    raise ValueError('Nonsemisimple nonlinear factor requires algebraic scalar reduction')
                if filtration is None:
                    filtration = scalar_filtration(K, G)
                z = sp.solve(factor, t)[0]
                classes, representatives, polynomials, total = {}, {}, [], 0
                for block in filtration['blocks']:
                    P, valuation = shifted_indicial(block['coefficients'], z)
                    data = exponents(P)
                    total += sp.degree(P, s)
                    polynomials.append(dict(polynomial=str(P), valuation=int(valuation)))
                    for target, entries in ((classes,data['classes_mod_Z']), (representatives,data['representatives'])):
                        for value, count in entries.items():
                            target[value] = target.get(value,0)+count
                if total != mult:
                    raise ValueError('Indicial rank does not exhaust the spectral sector; possible additional irregular slopes')
                item.update(method='exact_scalar_filtration', classes_mod_Z=classes,
                            representatives=representatives, indicial_polynomials=polynomials)
            if sum(item['classes_mod_Z'].values()) != mult:
                raise ArithmeticError('Exponent multiplicity mismatch')
            item['status'] = 'computed'
        except (ValueError, RuntimeError, NotImplementedError, AssertionError) as exc:
            item.update(status='unresolved', reason=str(exc))
        sectors.append(item)
    return dict(status='computed' if all(x['status']=='computed' for x in sectors) else 'partial',
                sectors=sectors, rank=M.rows,
                convention='K=-M; nabla=d/du+K/u^2+G/u; exponent classes modulo Z',
                specialization={str(k):str(v) for k,v in values.items()},
                logarithmic_jordan_structure='not computed',
                scope='Returned quantum cohomology sector; no rationality verdict')

