"""Exact spectrum and unit cyclicity data for the local quantum matrix UI."""

import sympy as sp


def matrix_analysis(matrix, unit_index=0, specialization=None, defaults=None, cyclic_determinant=None, symbolic_cyclicity=False):
    """Analyze the displayed matrix; unset variables specialize to one.

    Cyclicity is computed in the returned cohomology basis, starting with
    its unit vector, rather than inferred from numerical eigenvalues.
    By default the Krylov determinant uses the exactly specialized matrix.
    Set symbolic_cyclicity=True only to request the generic symbolic result.
    """
    matrix = sp.Matrix(matrix)
    n = matrix.rows
    if not n or matrix.cols != n:
        raise ValueError('Expected a nonempty square quantum matrix')
    if not 0 <= unit_index < n:
        raise ValueError('The quantum basis does not contain the unit')
    values = {symbol: sp.Integer(1) for symbol in matrix.free_symbols}
    values.update(defaults or {})
    values.update(specialization or {})
    evaluated = matrix.subs(values, simultaneous=True)
    if evaluated.free_symbols or any(v.is_finite is not True for v in evaluated):
        raise ValueError('Spectrum specialization must give finite numerical entries')
    result = {'specialization': {str(k): str(v) for k, v in
                                 sorted(values.items(), key=lambda item: str(item[0]))},
              'unit_index': unit_index, 'rank': n}
    lam = sp.Symbol('lambda')
    polynomial = evaluated.charpoly(lam).as_poly()
    result['characteristic_polynomial'] = str(sp.factor(polynomial.as_expr()))
    factors = sp.factor_list(polynomial.as_expr(), lam)[1]
    result['factors'] = [{'polynomial': str(factor), 'multiplicity': int(mult),
                          'degree': int(sp.degree(factor, lam))}
                         for factor, mult in factors]
    # Solve factors separately so repeated eigenvalues keep their exact
    # multiplicities and do not cause repeated-root numerical instability.
    try:
        eigenvalues = []
        for factor, mult in factors:
            roots = sp.Poly(factor, lam).nroots(n=25, maxsteps=200)
            for root in roots:
                value = complex(root)
                eigenvalues.append({'real': value.real, 'imag': value.imag,
                                    'multiplicity': int(mult)})
        result['eigenvalues'] = sorted(eigenvalues,
            key=lambda z: (-abs(complex(z['real'], z['imag'])), z['real'], z['imag']))
    except Exception as exc:
        result['eigenvalues'] = []
        result['spectrum_error'] = str(exc)
    try:
        if cyclic_determinant is None:
            from sympy.polys.matrices import DomainMatrix
            dm = DomainMatrix.from_Matrix(matrix if symbolic_cyclicity else evaluated)
            domain = dm.domain
            entries = dm.to_list()
            vector = [domain.one if i == unit_index else domain.zero for i in range(n)]
            columns = [vector]
            for _ in range(1, n):
                vector = [sum((entries[i][j]*vector[j] for j in range(n)),domain.zero) for i in range(n)]
                columns.append(vector)
            krylov = DomainMatrix([[columns[j][i] for j in range(n)] for i in range(n)],(n,n),domain)
            determinant = sp.factor(domain.to_sympy(krylov.det()))
        else:
            determinant = sp.sympify(cyclic_determinant)
            if not symbolic_cyclicity:
                determinant = sp.simplify(determinant.subs(values, simultaneous=True))
        specialized = sp.simplify(determinant.subs(values, simultaneous=True))
        result.update(cyclic_determinant=str(determinant),
                      cyclic_determinant_scope='symbolic' if symbolic_cyclicity else 'specialized',
                      cyclic_determinant_at_specialization=str(specialized),
                      cyclic_at_specialization=(None if specialized.is_zero is None
                                                else not specialized.is_zero))
    except Exception as exc:
        result['cyclic_error'] = str(exc)
    return result
