"""Specialized matrix analysis shared by the GUI worker and its tests."""

import ast
import math

import sympy as sp

from .connection import (characteristic_factors, chi_and_N, cyclic_determinant,
                         exponents, simple_exponent, _linear_root, _multiplicity)


def exact_number(text):
    """Read arithmetic, sqrt and I without evaluating Python input.

    Decimal literals are rationalized before any matrix calculation.
    """
    source = text.strip().replace('^', '**')

    def read(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return sp.Rational(ast.get_source_segment(source, node))
        if isinstance(node, ast.Name) and node.id == 'I':
            return sp.I
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = read(node.operand)
            return -value if isinstance(node.op, ast.USub) else value
        if isinstance(node, ast.BinOp):
            a, b = read(node.left), read(node.right)
            if isinstance(node.op, ast.Add):
                return a + b
            if isinstance(node.op, ast.Sub):
                return a - b
            if isinstance(node.op, ast.Mult):
                return a * b
            if isinstance(node.op, ast.Div):
                return a / b
            if isinstance(node.op, ast.Pow):
                return a ** b
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == 'sqrt' and len(node.args) == 1
                and not node.keywords):
            return sp.sqrt(read(node.args[0]))
        raise ValueError('use numbers, + - * / **, sqrt(...) and I')

    try:
        value = sp.simplify(read(ast.parse(source, mode='eval').body))
        if value.is_number is not True or value.is_finite is not True:
            raise ValueError('the value must be a finite number')
        return value
    except (SyntaxError, TypeError, ZeroDivisionError) as exc:
        raise ValueError(f'invalid number {text!r}') from exc


def novikov_values(spec, count):
    values = {sp.Symbol(f'y{i + 1}'): sp.Integer(1) for i in range(count)}
    seen = set()
    for pair in spec.split(','):
        if not pair.strip():
            continue
        if pair.count('=') != 1:
            raise ValueError('use assignments such as y1=2, y2=-1')
        name, text = (s.strip() for s in pair.split('='))
        symbol = sp.Symbol(name)
        if symbol not in values:
            raise ValueError(f'unknown Novikov variable {name}; expected '
                             + ', '.join(map(str, values)))
        if symbol in seen:
            raise ValueError(f'duplicate Novikov value for {name}')
        seen.add(symbol)
        values[symbol] = exact_number(text)
    return values


def numerical_spectrum(M):
    """Preserve exact multiplicities when possible, including at collisions."""
    poly = M.charpoly().as_poly()
    try:
        roots = poly.all_roots()
        if len(roots) != M.rows:
            raise NotImplementedError('root isolation did not cover the full polynomial')
    except (NotImplementedError, sp.PolynomialError):
        exact = sp.roots(poly)
        if sum(exact.values()) == M.rows:
            roots = [r for r, m in exact.items() for _ in range(m)]
        else:
            # An isolated context avoids changing another GUI job's precision.
            from mpmath import mp
            ctx = mp.clone()
            for precision in (30, 70, 150):
                ctx.dps = precision
                A = ctx.matrix([[ctx.mpc(str(sp.re(v).evalf(precision)),
                                        str(sp.im(v).evalf(precision)))
                                 for v in row] for row in M.tolist()])
                try:
                    roots = ctx.eig(A, left=False, right=False)
                    break
                except RuntimeError:
                    if precision == 150:
                        raise
    vals = [complex(r.evalf(20) if hasattr(r, 'evalf') else r) for r in roots]
    if not all(math.isfinite(z.real) and math.isfinite(z.imag) for z in vals):
        raise ValueError('eigenvalues exceed numerical display range')
    return sorted(vals, key=lambda z: (-round(abs(z), 10), -z.real, z.imag))


def spectrum_report(M, Gr, count, params, log=lambda s: None,
                    cancelled=lambda: False):
    """Analyze K^F = -c1* at one explicit point, on the computed basis.

    A blank eigenvalue selection means every characteristic factor.  A
    semicolon-separated list selects exact eigenvalues of K^F, not c1*.
    No genericity or rationality verdict is inferred from this point alone.
    """
    from .engine import Cancelled

    def checkpoint():
        if cancelled():
            raise Cancelled()

    values = novikov_values(params.get('eval_y', ''), count)
    A = sp.Matrix(M).subs(values, simultaneous=True).applyfunc(sp.simplify)
    if A.free_symbols or any(v.is_finite is not True for v in A):
        raise ValueError('the specialized matrix must have finite numeric entries')
    KF, G = -A, sp.Matrix(Gr)
    out = {'point': ', '.join(f'{s}={v}' for s, v in values.items()),
           'matrix': [[str(v) for v in row] for row in A.tolist()],
           'factors': [], 'connection_requested': bool(params.get('connection', True))}
    checkpoint()
    log('computing cyclic determinant at ' + out['point'])
    delta = cyclic_determinant(KF)
    out.update(delta=str(delta), cyclic=None if delta.is_zero is None else not delta.is_zero)
    checkpoint()
    try:
        log('computing eigenvalues at ' + out['point'])
        vals = numerical_spectrum(A)
        out['eigenvalues'] = [[v.real, v.imag] for v in vals]
    except Exception as exc:
        out['spectrum_error'] = str(exc)
    checkpoint()
    if not out['connection_requested']:
        return out
    log('computing connection exponents for the selected eigenvalues')
    x = sp.Symbol('x')
    selection = params.get('eigen_selection', '').strip()
    requested = list(dict.fromkeys(exact_number(s) for s in selection.split(';')
                                   if s.strip()))
    if selection and not requested:
        raise ValueError('enter exact eigenvalues separated by semicolons, or leave the field blank')
    try:
        chi, numerator = chi_and_N(KF, G, x)
        if requested:
            factors = [(sp.Poly(x - lam, x), _multiplicity(KF, lam, chi))
                       for lam in requested]
        else:
            factors = characteristic_factors(KF, x, chi)
    except Exception as exc:
        out['connection_error'] = str(exc)
        return out
    for p, m in factors:
        checkpoint()
        lam = _linear_root(p)
        rec = {'eigenvalue': str(lam) if lam is not None else None,
               'poly': str(p.as_expr()), 'multiplicity': m,
               'n_eigenvalues': p.degree()}
        out['factors'].append(rec)
        try:
            if not m:
                raise ValueError(f'{lam} is not an eigenvalue of K^F at this point')
            if m == 1:
                power = simple_exponent(KF, G, p, x, chi, numerator)
                rec.update(powers=[str(power)], complete=True, method='residue')
                power = sp.sympify(power)
                if power.is_Rational:
                    rec['F'] = [str(power % 1)]
                else:
                    rec['note'] = ('The power is expressed in the root x modulo the '
                                   'factor; rational exponent classes are not certified.')
            elif lam is not None:
                e = exponents(KF, G, lam, m)
                rec.update(powers=list(map(str, e['powers'])), F=list(map(str, e['F'])),
                           complete=e['complete'], method=e['method'],
                           obstruction=str(e['obstruction']))
            else:
                rec['error'] = ('Select an exact root of this repeated factor '
                                'to compute its connection exponents.')
        except Exception as exc:
            rec['error'] = str(exc)
    checkpoint()
    return out
