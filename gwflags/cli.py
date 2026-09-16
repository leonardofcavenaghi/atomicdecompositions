"""Command-line interface replacing the notebook's DialogInput screens.

Examples
--------
GW invariant (classes given as reduced words, comma-separated;
`pt` and `id` are accepted):

    python3 -m gwflags.cli A2 --keep 1 gw --beta 1 --classes pt,pt
    python3 -m gwflags.cli A3 --keep 2 gw --beta 1 --classes "1|3 2 1|pt"

Small quantum multiplication (c1(TX)*, its eigenvalues, grading):

    python3 -m gwflags.cli A2 --keep 1 sqm
    python3 -m gwflags.cli A3 --keep 1 -K 2 sqm        # quadric in P^3

Complete intersections: -K takes semicolon-separated rows, e.g. two
bundle summands O(1,2) + O(1,1) on a two-generator Picard group:
    -K "1,2;1,1"
"""

import argparse
import ast
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
            try:
                word = tuple(int(c) for c in token.replace(',', ' ').split())
            except ValueError as exc:
                raise ValueError(
                    f'invalid Schubert word {token!r}: use integer node labels '
                    'separated by spaces') from exc
            try:
                representative = X.wd.project(X.class_of_word(word))
                if len(word) != X.wd.length(representative):
                    raise ValueError(
                        'word must be reduced and minimal for the parabolic; '
                        'copy a word printed by the info command')
                out.append(representative)
            except (IndexError, KeyError, ValueError) as exc:
                raise ValueError(f'invalid Schubert word {word!r}: {exc}') from exc
    return out


def parse_k(spec, X=None):
    spec = spec.strip()
    if not spec:
        return []
    if any(c.isalpha() for c in spec):
        from gwflags.bundles import O, taut_sub, taut_quot, dual, osum, tensor, sym, wedge

        # Appendix C of the paper writes bundles without repeating the
        # ambient variety: O(1), S(3), and Q(3).  The Python API keeps the
        # explicit X argument, so the interface binds these paper aliases to
        # the current FlagVariety while retaining O(X, 1) and the explicit
        # taut_sub/taut_quot spellings for backwards compatibility.
        def paper_O(*args, **kwargs):
            if args and args[0] is X:
                return O(*args, **kwargs)
            return O(X, *args, **kwargs)

        def paper_S(*args, **kwargs):
            if args and args[0] is X:
                args = args[1:]
            return taut_sub(X, *args, **kwargs)

        def paper_Q(*args, **kwargs):
            if args and args[0] is X:
                args = args[1:]
            return taut_quot(X, *args, **kwargs)

        try:
            tree = ast.parse(spec, mode='eval')
            allowed = {"X": X, "O": paper_O, "S": paper_S, "Q": paper_Q,
                       "taut_sub": taut_sub, "taut_quot": taut_quot,
                       "dual": dual, "osum": osum, "tensor": tensor,
                       "sym": sym, "wedge": wedge}
            for node in ast.walk(tree):
                if isinstance(node, ast.Name) and node.id not in allowed:
                    raise ValueError(f'unknown name {node.id!r}')
                if isinstance(node, ast.Call) and not (isinstance(node.func, ast.Name) and node.func.id in allowed):
                    raise ValueError('only supported bundle constructors may be called')
                if isinstance(node, ast.Attribute):
                    raise ValueError('attribute access is not supported; use X only as a constructor argument')
            return eval(compile(tree, '<bundle>', 'eval'), {'__builtins__': {}}, allowed)
        except Exception as e:
            raise ValueError(f"Invalid bundle expression: {e}")
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
                     help='curve class in kept-root order (or a full ambient '
                          'vector with zeroes off kept roots), e.g. 1 or 1,0')
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
        K = X._check_K(parse_k(args.K, X))
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
        try:
            beta = X._check_beta(tuple(int(v.strip())
                                       for v in args.beta.split(',')))
            classes = parse_classes(args.classes, X)
        except ValueError as exc:
            ap.error(str(exc))
        val = X.gw(classes, beta, K or None,
                   progress=lambda s: print('  ', s, file=sys.stderr))
        print(f'beta = {list(beta)}  # ambient node order')
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
