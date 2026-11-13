"""Command-line interface for gwtoric.

Examples
--------
    python -m gwtoric.cli --preset P2 info
    python -m gwtoric.cli --preset P2 gw --beta 1,1,1 --classes "pt|pt"
    python -m gwtoric.cli --rays "1,0;0,1;-1,2;0,-1" --cones "0,1;1,2;2,3;3,0" info
    python -m gwtoric.cli --preset F1 gw --beta 1,0 --classes "pt"
    python -m gwtoric.cli --preset P1xP1 sqm
    python -m gwtoric.cli --preset P4 --K 5 gw --beta 1 --classes ""   # quintic: 2875
    python -m gwtoric.cli --preset P4 --K 2 sqm                         # quadric 3-fold
    python -m gwtoric.cli --preset F2 sqm --max-degree 4                # non-Fano: cutoff
    python -m gwtoric.cli --preset P4 --K 3 exponents                   # cubic 3-fold: irrational
    python -m gwtoric.cli --preset P5 --K 4 exponents --very-general    # quartic 4-fold
    python -m gwtoric.cli --preset PB5:0,2 --K 0,0,0,0,0,0,0,2 info     # quartic double 5-fold
    python -m gwtoric.cli --rays ... --cones ... --K 0,0,1,0,0,2,0 sqm --mori 0,0,-1,0,0,2,0 --workers 8

Classes are expressions in x0, x1, ... (toric divisor classes), pt, c1,
one, with + - * ^ and rational coefficients, separated by "|".  Curve
classes are given as k integers (one per ray) or as k - n coordinates in
the printed H_2 basis.  --K cuts a complete intersection: one nef divisor
per row (k ray coefficients or H^2-basis coordinates), rows separated by
";"; invariants and c1* are then those of the zero locus with ambient
insertions (quantum Lefschetz).
"""

import argparse
import sys
from fractions import Fraction

from . import (ToricVariety, projective_space, hirzebruch,
               product_of_projective_spaces,
               projective_bundle_over_projective_space, del_pezzo_6)


def preset(name):
    key = name.upper().replace(' ', '')
    if key.startswith('P') and key[1:].isdigit():
        return projective_space(int(key[1:]))
    if key.startswith('F') and key[1:].isdigit():
        return hirzebruch(int(key[1:]))
    if 'X' in key and all(p.startswith('P') and p[1:].isdigit()
                          for p in key.split('X')):
        return product_of_projective_spaces(*(int(p[1:]) for p in key.split('X')))
    if key.startswith('PB') and ':' in key:
        base, twists = key[2:].split(':', 1)
        return projective_bundle_over_projective_space(
            int(base), [int(v) for v in twists.replace(':', ',').split(',')])
    if key in ('DP6', 'HEXAGON'):
        return del_pezzo_6()
    if key == 'BLP3':
        return projective_space(3).blowup((0, 1, 2))
    raise ValueError(f'unknown preset {name!r}; try P2, P3, P1xP1, P1xP2, '
                     f'F1, F2, dP6, BlP3, PB5:0,2')


def parse_int_list(spec):
    return [[int(v) for v in row.split(',')] for row in spec.split(';')]


def parse_classes(spec, X):
    env = {f'x{i}': X.x(i) for i in range(X.k)}
    env.update({'pt': X.pt, 'c1': X.c1, 'one': X.one, 'Fraction': Fraction})
    out = []
    if not spec.strip():
        return out
    for token in spec.split('|'):
        expr = token.strip().replace('^', '**')
        try:
            val = eval(expr, {'__builtins__': {}}, env)
        except Exception as exc:
            raise ValueError(f'cannot parse class {token!r}: {exc}')
        if isinstance(val, (int, Fraction)):
            val = X.one * val
        out.append(val)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog='gwtoric',
        description='GW invariants and quantum multiplication of smooth '
                    'projective toric varieties')
    ap.add_argument('--rays', help='rays, e.g. "1,0;0,1;-1,-1"')
    ap.add_argument('--cones', help='maximal cones (0-based ray indices), '
                                    'e.g. "0,1;1,2;0,2"')
    ap.add_argument('--preset', help='P2, P3, P1xP1, P1xP2, F1, F2, dP6, BlP3')
    ap.add_argument('--K', help='complete intersection: one nef divisor per '
                                'row (k ray coefficients, or coordinates on '
                                'the H^2 basis rays), rows separated by ";" '
                                '- e.g. --K 5 for the quintic in P4')
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('info', help='fan, cohomology basis, Hodge diamond, curves')
    gwp = sub.add_parser('gw', help='one GW invariant')
    gwp.add_argument('--beta', required=True)
    gwp.add_argument('--classes', required=True)
    sqmp = sub.add_parser('sqm', help='small quantum multiplication by c1')
    sqmp.add_argument('--betas', help='optional list of curve classes, '
                                      'rows separated by ";"')
    sqmp.add_argument('--max-degree', type=int,
                      help='cutoff omega.beta <= N on the curve classes, '
                           'omega the ample divisor printed by info (only '
                           'needed when c1 has degree <= 0 on some '
                           'invariant curve; default dim + 3 times the '
                           'smallest omega-degree of an invariant curve)')
    sqmp.add_argument('--mori', help='complete intersections (assumed Fano) '
                                     'in an X with invariant curves of '
                                     'c1(Z)-degree <= 0: divisors N with '
                                     'N.beta >= 0 on every curve of Z, one '
                                     'per row like --K; needed when the '
                                     'cone of curves of Z cannot be bounded '
                                     'from the fan (a warning says so)')
    sqmp.add_argument('--workers', default='auto',
                      help="processes for the curve classes (default 'auto')")
    sqmp.add_argument('--verify', type=int, default=3,
                      help='how many of the curve classes excluded by --mori '
                           'to check by computing their invariants (0 turns '
                           'the check off and stops --mori being guessed)')
    sqmp.add_argument('--no-auto-mori', action='store_true',
                      help='do not try to derive the missing inequalities')
    expp = sub.add_parser('exponents',
                          help='rank and regularized exponents of the '
                               'generic Hodge factors of the quantum '
                               'connection, and the rationality obstruction')
    expp.add_argument('--very-general', action='store_true',
                      help='for an even-dimensional complete intersection, '
                           'assert that the primitive middle cohomology has '
                           'no rational (n/2, n/2) class (the hypothesis '
                           '(18) of the paper); without it no verdict is '
                           'issued in even dimension')
    expp.add_argument('--var', default='q',
                      help='name of the small-locus parameter (default q)')
    args = ap.parse_args(argv)

    try:
        if args.preset:
            X = preset(args.preset)
        elif args.rays and args.cones:
            X = ToricVariety(parse_int_list(args.rays), parse_int_list(args.cones))
        else:
            ap.error('give --preset or both --rays and --cones')
        K = X.check_K(parse_int_list(args.K)) if args.K else []
    except ValueError as exc:
        ap.error(str(exc))

    if args.cmd == 'info':
        print(X)
        print('rays:', X.fan.rays)
        print('maximal cones:', X.fan.max_cones)
        print('Betti numbers b_0, b_2, ...:', X.betti)
        print('Ambient Hodge diamond:' if K else 'Hodge diamond:')
        print(X.hodge_diamond_str())
        if K:
            from .hodge import HodgeNotSupported
            print('Complete-intersection Hodge diamond:')
            try:
                hodge = X.hodge_report(K)
            except HodgeNotSupported as exc:
                print('Not computed:', exc)
            else:
                print(hodge['diamond'])
                print(f'Betti numbers b_0, ..., b_{2*hodge["dimension"]}:', hodge['betti'])
                print('Euler characteristic:', hodge['euler'])
                print('Chern numbers:', hodge['chern_numbers'])
                print('Method:', hodge['method'])
                print('Assumptions:', hodge['assumptions'])
        print('H^2 basis rays:', X.h2_generators)
        print('Novikov variables: ' + ', '.join(
            f'y{j + 1} <-> {X.reduce(X.divisor(a))}'
            for j, a in enumerate(X.novikov_divisors))
            + ('  (nef basis of Pic X: the exponents are >= 0)'
               if X.fan.nef_basis() else
               '  (no nef lattice basis: exponents can be negative)'))
        print('cohomology basis:')
        for i, name in enumerate(X.class_names):
            print(f'  sigma_{i}: {name}')
        print('c1 =', X.reduce(X.c1))
        print('H_2 basis (vectors a_rho):', X.h2_basis)
        print('invariant curves (wall, class, c1-degree):')
        for tau, cls in X.wall_curves:
            print(f'  {tau}: {cls}  c1.C = {sum(cls)}')
        print('Fano:', X.is_fano, ' ample divisor used:', X.fan.ample_divisor())
        if X.is_fano:
            r, A = X.anticanonical_generator()
            print(f'Fano index of X = {r}:  -K_X = {r} * {X.reduce(X.divisor(A))}')
        if K:
            print('complete intersection Z of the divisors', [list(a) for a in K])
            print(f'  dim Z = {X.n - len(K)},  c1(Z) = {X.reduce(X.c1_ci(K))}')
            r, A = X.anticanonical_generator(K)
            print(f'  Fano index of Z = {r}:  -K_Z = {r} * ({X.reduce(X.divisor(A))})|_Z, '
                  f'coindex {X.n - len(K) + 1 - r}'
                  + ('' if X.n - len(K) >= 3 else '  (index in Pic X; Pic Z can be '
                     'larger for a curve or a surface)'))
            print('  degrees on invariant curves (wall: [D_m.C], c1(Z).C):')
            for tau, cls in X.wall_curves:
                print(f'    {tau}: {[X.fan.wall_degree(a, cls) for a in K]}'
                      f'  {X.c1_degree(cls, K)}')
        return

    if args.cmd == 'exponents':
        from .connection import invariants, report
        print(report(invariants(X, K, var=args.var,
                                very_general=args.very_general)))
        return 0

    if args.cmd == 'gw':
        beta = X.beta([int(v) for v in args.beta.split(',')])
        classes = parse_classes(args.classes, X)
        val = X.gw(classes, beta, K)
        print(f'beta = {list(beta)}  (c1.beta = {X.c1_degree(beta, K)}'
              + (' on Z' if K else '') + ')')
        print(f'GW invariant = {val}')
        return

    if args.cmd == 'sqm':
        if args.betas:
            betas = [X.beta(b) for b in parse_int_list(args.betas)]
            fano = None
        else:
            rep = X.curve_class_report(
                K, args.max_degree,
                parse_int_list(args.mori) if args.mori else None,
                progress=lambda s: print('  ', s, file=sys.stderr),
                auto_mori=not args.no_auto_mori, verify=args.verify)
            fano, betas = rep['fano'], rep['betas']
            for s, b in rep['stuck']:
                stratum = ','.join(map(str, s))
                print(f'WARNING: c1(Z) has degree <= 0 on the class {list(b)} '
                      f'of the stratum V({stratum}); give --mori N with '
                      f'N.beta >= 0 on the curves of Z for an exact list',
                      file=sys.stderr)
            if rep['not_fano']:
                print('WARNING:', rep['not_fano'], file=sys.stderr)
            for s, N in rep.get('suggested', []):
                print(f'inequality {list(N)} derived automatically for the '
                      f'stratum V{tuple(s)} (checked by sampling, not proved)',
                      file=sys.stderr)
            ver = rep.get('verify')
            if ver and ver['failures']:
                b, p, v = ver['failures'][0]
                print(f'WARNING: the inequalities are WRONG: they exclude the '
                      f'class {b} with <{p[0]}, {p[1]}> = {v} != 0',
                      file=sys.stderr)
            elif ver:
                print(f'sample check: all invariants of the '
                      f'{len(ver["checked"])} cheapest excluded classes vanish',
                      file=sys.stderr)
            if rep['mode'] in ('mori', 'mori-auto'):
                print('exact list from the cone of curves of Z (Z is assumed '
                      'to be Fano)', file=sys.stderr)
            if rep['mode'] == 'cutoff':
                print(f'WARNING: c1 has degree <= 0 on the invariant curve(s) '
                      f'{[list(z) for z in rep["nonpositive"]]}; the curve '
                      f'classes are truncated at omega.beta <= '
                      f'{rep["max_degree"]}, omega = '
                      f'{list(X.fan.ample_divisor())} (raise --max-degree to '
                      f'go further)', file=sys.stderr)
        print('Fano index =', fano)
        print('betas =', [list(b) for b in betas])
        workers = args.workers if args.workers == 'auto' else int(args.workers)
        M, Gr, names = X.small_quantum_multiplication(
            betas, K, progress=lambda s: print('  ', s, file=sys.stderr),
            workers=workers)
        print('basis =', names, '(ambient part of H*(Z))' if K else '')
        print('c1(TZ)* =' if K else 'c1(TX)* =')
        for row in M:
            print('  ', row)
        print('grading =', [Gr[i][i] for i in range(len(Gr))])
        cg = X.c1_grading(K)
        print('Novikov degrees: ' + ', '.join(
            f'deg y{j + 1} = {c}' for j, c in enumerate(cg))
            + '  (q^beta has degree c1.beta; the matrix is homogeneous)')
        print('c1* with y_j -> t^(c_j)  [one variable, graded by c1.beta; '
              'identifies all classes of the same c1-degree]:')
        for row in X.specialize_c1(M, K):
            print('  ', row)
        from .quantum import spectrum_at_one
        ev = spectrum_at_one(M)
        chop = lambda x: 0.0 if abs(x) < 1e-10 else x
        print('eigenvalues at y=1 =',
              ['%+.6g%+.6gi' % (chop(z.real), chop(z.imag)) for z in ev])
        try:
            print('eigenvalues (symbolic) =', X.eigenvalues(M))
        except Exception:
            print('eigenvalues (symbolic): no closed form for generic y')


if __name__ == '__main__':
    main()
