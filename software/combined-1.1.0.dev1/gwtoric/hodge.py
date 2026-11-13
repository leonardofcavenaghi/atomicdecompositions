"""Hodge numbers of smooth ample Fano complete intersections in dimensions 3-5.

For threefolds Lefschetz gives h11=rho(Y), and Gauss--Bonnet gives
h12 = 1 + rho(Y) - int(c3)/2. Check chi(O_X)=int(c1*c2)/24=1.

Weak Lefschetz determines H^k for k < 4; Hodge/Serre duality determines
k > 4. Since X is Fano, h^{p,0}=0 for p>0. The remaining h^{1,3} and
h^{2,2} follow from Hirzebruch--Riemann--Roch and Gauss--Bonnet:

  chi(Omega_X^1) = 4 chi(O_X) - (int c1*c3 + 2 int c4)/12,
  chi(O_X) = 1,  chi(Omega_X^1) = -rho - h^{1,3}.

All products are evaluated in the ambient Chow ring against [X]=prod L_i.
This computes dimensions, not a basis for primitive middle cohomology.

For fivefolds, Lefschetz fixes h11=rho(Y) and h22=b4(Y). HRR gives
  chi(O_X) = int(-c1^3*c2 + 3*c1*c2^2 + c1^2*c3 - c1*c4)/1440,
  chi(Omega_X^1) = 3 chi(O_X) - int(c1*c4+c5)/24 = -rho+h14.
Then Gauss--Bonnet determines h23. These identities follow by expanding
ch(Omega_X^1) td(TX) to degree five (Newton identities for Chern roots).
"""

from fractions import Fraction


class HodgeNotSupported(ValueError):
    """The hypotheses of the implemented CI Hodge formula are not certified."""


def format_diamond(h):
    n = len(h) - 1
    width = max(len(str(v)) for row in h for v in row) + 2
    lines = []
    for s in range(2 * n + 1):
        entries = [str(h[p][s - p]) for p in range(max(0, s - n),
                                                  min(s, n) + 1)]
        lines.append(''.join(e.center(width) for e in entries)
                     .center((n + 1) * width).rstrip())
    return '\n'.join(lines)


def _integer(value, name, nonnegative=False):
    value = Fraction(value)
    if value.denominator != 1 or (nonnegative and value < 0):
        raise ArithmeticError(f'inconsistent {name}: {value}')
    return int(value)


def _report(h, method, **extra):
    n = len(h) - 1
    betti = [sum(h[p][s-p] for p in range(max(0, s-n), min(s, n)+1))
             for s in range(2*n+1)]
    return dict(dimension=n, hodge=h, diamond=format_diamond(h), betti=betti,
                euler=sum((-1)**i * b for i, b in enumerate(betti)),
                method=method, **extra)


def chern_numbers(Y, K=None):
    """Exact Chern numbers of a smooth nef CI of dimension three to five.

    No ampleness/Fano assumption is needed for this adjunction calculation.
    It does not determine Picard rank or a full Hodge diamond by itself.
    With empty K, compute the Chern numbers of the toric ambient.
    """
    rows = Y.check_K(K)
    dim = Y.n - len(rows)
    if dim not in (3, 4, 5):
        raise HodgeNotSupported('Chern-number computation requires dimension 3, 4 or 5')
    c = [Y.one] + [Y.one * 0 for _ in range(dim)]
    for i in range(Y.k):
        for j in range(dim, 0, -1):
            c[j] = Y.reduce(c[j] + Y.x(i) * c[j-1])
    divisors = [Y.divisor(row) for row in rows]
    for divisor in divisors:
        # (1+L) c_new = c_old; ascending order uses c_new[j-1].
        for j in range(1, dim+1):
            c[j] = Y.reduce(c[j] - divisor * c[j-1])
    fundamental = Y.one
    for divisor in divisors:
        fundamental = Y.reduce(fundamental * divisor)

    def integral(*classes):
        return Y.integral(*classes, fundamental)

    if dim == 3:
        result = dict(c1_3=integral(c[1], c[1], c[1]),
                      c1_c2=integral(c[1], c[2]), c3=integral(c[3]))
    elif dim == 4:
        result = dict(c1_4=integral(c[1], c[1], c[1], c[1]),
                      c1_2_c2=integral(c[1], c[1], c[2]),
                      c2_2=integral(c[2], c[2]),
                      c1_c3=integral(c[1], c[3]), c4=integral(c[4]))
    else:
        result = dict(c1_5=integral(c[1], c[1], c[1], c[1], c[1]),
                      c1_3_c2=integral(c[1], c[1], c[1], c[2]),
                      c1_c2_2=integral(c[1], c[2], c[2]),
                      c1_2_c3=integral(c[1], c[1], c[3]),
                      c2_c3=integral(c[2], c[3]),
                      c1_c4=integral(c[1], c[4]), c5=integral(c[5]))
    return {key: _integer(value, key) for key, value in result.items()}


def hodge_report(Y, K=None):
    """Return JSON-ready exact data; raise HodgeNotSupported outside scope.

    With no K this is the ambient toric diamond in any dimension. Otherwise
    require dimension three to five, every defining divisor ample, and the adjunction
    divisor -K_Y-sum L_i ample on Y (a sufficient certificate that X is Fano).
    The result is for a smooth member of the specified complete-intersection
    family. It does not check smoothness of any particular defining equations.
    """
    rows = Y.check_K(K)
    if not rows:
        return _report(Y.ring.hodge_diamond(), 'toric fan',
                       subject='ambient', codimension=0)
    dim = Y.n - len(rows)
    if dim not in (3, 4, 5):
        raise HodgeNotSupported(
            f'complete-intersection Hodge numbers currently require dimension '
            f'3, 4 or 5; this input has dimension {dim}')
    for i, row in enumerate(rows, 1):
        for wall in Y.fan.wall_classes:
            degree = Y.fan.wall_degree(row, wall)
            if degree <= 0:
                raise HodgeNotSupported(
                    f'defining divisor L_{i} is not ample: degree {degree} '
                    f'on invariant curve {list(wall)}; the implemented '
                    f'Lefschetz formula requires every defining divisor ample')
    anticanonical = tuple(1 - sum(row[i] for row in rows) for i in range(Y.k))
    for wall in Y.fan.wall_classes:
        degree = Y.fan.wall_degree(anticanonical, wall)
        if degree <= 0:
            raise HodgeNotSupported(
                f'Fano condition not certified: the adjunction divisor '
                f'-K_Y - sum L_i has degree {degree} on invariant curve '
                f'{list(wall)}; this method requires it to be ample on Y')

    chern = chern_numbers(Y, rows)
    rho = Y.k - Y.n
    assumptions = ('Smooth complete intersection; every defining divisor '
                   'and -K_Y - sum L_i are ample on the ambient.')
    if dim == 3:
        if chern['c1_c2'] != 24:
            raise ArithmeticError('Fano Riemann--Roch check failed: c1*c2 != 24')
        a = _integer(1 + rho - Fraction(chern['c3'], 2), 'h^{1,2}',
                     nonnegative=True)
        h = [[0]*4 for _ in range(4)]
        h[0][0] = h[3][3] = 1
        h[1][1] = h[2][2] = rho
        h[1][2] = h[2][1] = a
        result = _report(h, 'ample Lefschetz and Gauss-Bonnet',
                         subject='complete_intersection', codimension=len(rows),
                         chern_numbers=chern, chi_O=1, picard_rank=rho,
                         assumptions=assumptions)
        if result['euler'] != chern['c3']:
            raise ArithmeticError('Hodge/Gauss--Bonnet Euler check failed')
        return result
    if dim == 5:
        chi0 = Fraction(-chern['c1_3_c2'] + 3*chern['c1_c2_2']
                        + chern['c1_2_c3'] - chern['c1_c4'], 1440)
        if chi0 != 1:
            raise ArithmeticError(f'Fano Riemann--Roch check failed: chi(O_X)={chi0}')
        chi1 = 3*chi0 - Fraction(chern['c1_c4'] + chern['c5'], 24)
        a = _integer(rho + chi1, 'h^{1,4}', nonnegative=True)
        diagonal2 = Y.betti[2]  # ambient b4; toric betti uses even degrees
        b = _integer(1 + rho + diagonal2 - a - Fraction(chern['c5'], 2),
                     'h^{2,3}', nonnegative=True)
        h = [[0]*6 for _ in range(6)]
        h[0][0] = h[5][5] = 1
        h[1][1] = h[4][4] = rho
        h[2][2] = h[3][3] = diagonal2
        h[1][4] = h[4][1] = a
        h[2][3] = h[3][2] = b
        result = _report(h, 'ample Lefschetz and Hirzebruch-Riemann-Roch',
                         subject='complete_intersection', codimension=len(rows),
                         chern_numbers=chern, chi_O=1, chi_Omega1=_integer(chi1, 'chi(Omega1)'),
                         picard_rank=rho, assumptions=assumptions)
        if result['euler'] != chern['c5']:
            raise ArithmeticError('Hodge/Gauss--Bonnet Euler check failed')
        return result
    chi0 = Fraction(-chern['c1_4'] + 4*chern['c1_2_c2'] + 3*chern['c2_2']
                    + chern['c1_c3'] - chern['c4'], 720)
    if chi0 != 1:
        raise ArithmeticError(f'Fano Riemann--Roch check failed: chi(O_X)={chi0}')
    a = _integer(Fraction(chern['c1_c3'] + 2*chern['c4'], 12) - 4 - rho,
                 'h^{1,3}', nonnegative=True)
    b = _integer(chern['c4'] - 2 - 2*rho - 2*a, 'h^{2,2}', nonnegative=True)
    h = [[0]*5 for _ in range(5)]
    h[0][0] = h[4][4] = 1
    h[1][1] = h[3][3] = rho
    h[1][3] = h[3][1] = a
    h[2][2] = b
    result = _report(h, 'ample Lefschetz and Hirzebruch-Riemann-Roch',
                     subject='complete_intersection', codimension=len(rows),
                     chern_numbers=chern, chi_O=1, picard_rank=rho,
                     assumptions=assumptions)
    if result['euler'] != chern['c4']:
        raise ArithmeticError('Hodge/Gauss--Bonnet Euler check failed')
    return result
