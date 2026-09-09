"""Command-line interface replacing the notebook's DialogInput screens.

Examples
--------
GW invariant (classes given as reduced words, comma-separated;
`pt` and `id` are accepted):

    python3 -m gwflags.cli A2 --keep 1 gw --beta 1,0 --classes pt,pt
    python3 -m gwflags.cli A3 --keep 2 gw --beta 0,1,0 --classes "1|3 2 1|pt"

Small quantum multiplication (c1(TX)*, its eigenvalues, grading):

    python3 -m gwflags.cli A2 --keep 1 sqm
    python3 -m gwflags.cli A3 --keep 1 sqm -K 2        # quadric in P^3

Complete intersections: -K takes semicolon-separated rows, e.g. two
bundle summands O(1,2) + O(1,1) on a two-generator Picard group:
    -K "1,2;1,1"
"""

import argparse
import sys

from . import FlagVariety


def parse_classes(spec, X):
    out = []
    for token in spec.split('|') if '|' in spec else spec.split(','):
        token = token.strip()
        if token in ('pt', 'point'):
            out.append(X.pt)
        elif token in ('id', 'e', ''):
            out.append(X.wd.group[0])
        else:
            word = tuple(int(c) for c in token.replace(',', ' ').split())
            out.append(X.schubert(word))
    return out


def parse_k(spec):
    if not spec:
        return []
    return [[int(v) for v in row.split(',')] for row in spec.split(';')]


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog='gwflags',
        description='GW invariants and quantum multiplication of flag '
                    'varieties (translation of V3.nb)')
    ap.add_argument('algebra', help="simple Lie algebra, e.g. A2, B3")
    ap.add_argument('--keep', required=True,
                    help='comma-separated 1-based simple roots kept out of P '
                         '(the notebook\'s m); e.g. 1 for P^n, k for Gr(k,.)')
    ap.add_argument('-K', default='',
                    help='complete-intersection multidegrees, rows separated '
                         'by ";", entries by ","')
    sub = ap.add_subparsers(dest='cmd', required=True)

    gwp = sub.add_parser('gw', help='one GW invariant')
    gwp.add_argument('--beta', required=True,
                     help='curve class over the simple roots, e.g. 1,0')
    gwp.add_argument('--classes', required=True,
                     help='insertions: reduced words separated by "|" '
                          '(spaces between letters), or pt / id')

    sqmp = sub.add_parser('sqm', help='small quantum multiplication by c1(TX)')
    sqmp.add_argument('--workers', type=int, default=0,
                      help='distribute per-beta blocks over N processes')
    sub.add_parser('info', help='print Schubert basis and c1')

    args = ap.parse_args(argv)
    keep = [int(v) for v in args.keep.split(',')]
    try:
        X = FlagVariety(args.algebra, keep)
        K = X._check_K(parse_k(args.K))
    except ValueError as exc:
        ap.error(str(exc))

    if args.cmd == 'info':
        from .quantum import chern_class_vector, chern_class_ci
        print(f'{args.algebra}/P, kept roots {keep}: dimension {X.dimension},'
              f' {len(X.classes)} Schubert classes')
        for i, w in enumerate(X.class_words()):
            print(f'  sigma_{i}: word {list(w) or "e"}, degree {len(w)}')
        c = chern_class_ci(X, K) if K else chern_class_vector(X)
        print('c1 =', c)
        return

    if args.cmd == 'gw':
        beta = tuple(int(v) for v in args.beta.split(','))
        classes = parse_classes(args.classes, X)
        val = X.gw(classes, beta, K or None,
                   progress=lambda s: print('  ', s, file=sys.stderr))
        print(f'beta = {list(beta)}')
        print(f'GW invariant = {val}')
        return

    if args.cmd == 'sqm':
        fano, betas = X.fano_index_and_betas(K or None)
        print('Fano index =', fano)
        print('betas =', [list(b) for b in betas])
        M, Gr, idx = X.small_quantum_multiplication(
            K or None, betas,
            progress=lambda s: print('  ', s, file=sys.stderr),
            workers=args.workers)
        print('basis (indices into Schubert classes) =', idx)
        print('c1(TX)* =')
        for row in M:
            print('  ', row)
        print('grading =', [row[i] for i, row in enumerate(Gr)])
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
