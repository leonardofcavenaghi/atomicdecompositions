"""Local web GUI for gwtoric — explore smooth projective toric varieties,
Gromov–Witten invariants and quantum multiplication by c1 without the
command line.

    python -m gwtoric.gui             # serves http://127.0.0.1:8643 and
                                      # opens the browser
    python -m gwtoric.gui --port N --no-browser

Stdlib-only server (http.server), same design as gwflags.gui: jobs run on
worker threads with live progress and results render as tables.  Binds to
127.0.0.1 only.  Run from the folder containing both gwtoric and gwflags.
"""

import argparse
import json
import threading
import time
import traceback
import uuid
import webbrowser
from fractions import Fraction
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

def _fan_strings(X):
    rays = ';'.join(','.join(str(v) for v in r) for r in X.fan.rays)
    cones = ';'.join(','.join(str(v) for v in c) for c in X.fan.max_cones)
    return rays, cones


def _make_presets():
    from gwtoric import (projective_space, product_of_projective_spaces,
                         projective_bundle_over_projective_space)
    P4 = _fan_strings(projective_space(4))
    P6 = _fan_strings(projective_space(6))
    P2P2 = _fan_strings(product_of_projective_spaces(2, 2))
    # projective bundles by Cox-Little-Schenck Prop. 7.3.3 instead of fans
    # typed in by hand (ToricVariety.projective_bundle, Fan.projective_bundle)
    MM32 = _fan_strings(product_of_projective_spaces(1, 1).projective_bundle(
        [(0, 0, 0, 0), (0, 1, 0, 1), (0, 0, 0, 0)]))
    DC5 = _fan_strings(projective_bundle_over_projective_space(5, (0, 2)))
    # label, rays, cones, blowup, complete intersection K[, Mori cone
    # inequalities]
    return [
        ('P2', '1,0;0,1;-1,-1', '0,1;1,2;0,2', '', ''),
        ('P3', '1,0,0;0,1,0;0,0,1;-1,-1,-1',
         '0,1,2;0,1,3;0,2,3;1,2,3', '', ''),
        ('P4', *P4, '', ''),
        ('P1 x P1', '1,0;-1,0;0,1;0,-1', '0,2;2,1;1,3;3,0', '', ''),
        ('P1 x P2', '1,0,0;-1,0,0;0,1,0;0,0,1;0,-1,-1',
         '0,2,3;0,2,4;0,3,4;1,2,3;1,2,4;1,3,4', '', ''),
        ('F1 = Bl_pt P2', '1,0;0,1;-1,1;0,-1', '0,1;1,2;2,3;3,0', '', ''),
        ('F2  (non-Fano)', '1,0;0,1;-1,2;0,-1', '0,1;1,2;2,3;3,0', '', ''),
        ('dP6 = Bl_3pts P2  (hexagon)', '1,0;1,1;0,1;-1,0;-1,-1;0,-1',
         '0,1;1,2;2,3;3,4;4,5;5,0', '', ''),
        ('Bl_pt P3', '1,0,0;0,1,0;0,0,1;-1,-1,-1',
         '0,1,2;0,1,3;0,2,3;1,2,3', '0,1,2', ''),
        ('P1 x P1 x P1', '1,0,0;-1,0,0;0,1,0;0,-1,0;0,0,1;0,0,-1',
         '0,2,4;0,2,5;0,3,4;0,3,5;1,2,4;1,2,5;1,3,4;1,3,5', '', ''),
        ('quadric surface P1xP1 = (2) in P3', '1,0,0;0,1,0;0,0,1;-1,-1,-1',
         '0,1,2;0,1,3;0,2,3;1,2,3', '', '2'),
        ('cubic surface = (3) in P3', '1,0,0;0,1,0;0,0,1;-1,-1,-1',
         '0,1,2;0,1,3;0,2,3;1,2,3', '', '3'),
        ('Q3 = quadric 3-fold (2) in P4', *P4, '', '2'),
        ('cubic 3-fold (3) in P4', *P4, '', '3'),
        ('quartic 3-fold (4) in P4', *P4, '', '4'),
        ('quintic 3-fold (5) in P4  [Calabi-Yau: GW box only]', *P4, '', '5'),
        ('Fl(1,2,3) = (1,1) in P2 x P2', *P2P2, '', '1,1'),
        ('V8 = (2,2,2) in P6  [slow]', *P6, '', '2;2;2'),
        ('Mori-Mukai 3-2 = 2M+H2 in P(O+O+O(1,1)) over P1xP1  [slow]',
         *MM32, '', '0,0,1,0,0,2,0', '0,0,-1,0,0,2,0'),
        ('quartic double 5-fold w^2 = f_4 in P(O+O(2)) over P5',
         *DC5, '', '0,0,0,0,0,0,0,2'),
    ]


PRESETS = _make_presets()

JOBS = {}
JOBS_LOCK = threading.Lock()


# ------------------------------------------------------------- computations
def parse_int_list(spec):
    rows = [row for row in spec.replace('\n', ';').split(';') if row.strip()]
    return [[int(v) for v in row.replace(' ', '').split(',') if v != '']
            for row in rows]


def parse_factors(spec, what='the factors'):
    """[n_1, .., n_m] from "2,2" or "2;2" (the product P^n_1 x .. x P^n_m)."""
    ns = [n for row in parse_int_list(spec) for n in row]
    if not ns:
        raise ValueError(f'give {what}, e.g. 5 for P^5 or 1,1 for P^1 x P^1')
    if any(n < 1 for n in ns):
        raise ValueError(f'every factor needs dimension >= 1, got {ns}')
    return ns


def product_divisor(ns, row):
    """Ray coefficients of a divisor on P^n_1 x .. x P^n_m given either as
    one multidegree per factor -- O(a_1, .., a_m) = sum_j a_j D_j with D_j
    the last ray of the j-th factor, the normalization of Cox-Little-Schenck
    Example 7.3.5 -- or as all k ray coefficients."""
    k = sum(n + 1 for n in ns)
    if len(row) == k:
        return tuple(row)
    if len(row) != len(ns):
        raise ValueError(
            f'a divisor on a product of {len(ns)} projective spaces needs '
            f'one multidegree per factor ({len(ns)} entries) or all {k} ray '
            f'coefficients; got {len(row)} ({row})')
    out = [0] * k
    at = 0
    for n, a in zip(ns, row):
        at += n + 1
        out[at - 1] = a
    return tuple(out)


def typed_fan(params):
    from gwtoric import ToricVariety
    rays = parse_int_list(params.get('rays', ''))
    cones = parse_int_list(params.get('cones', ''))
    if not rays or not cones:
        raise ValueError('give the rays and the maximal cones (or pick a '
                         'preset)')
    return ToricVariety(rays, cones)


def build_variety(params):
    """The ambient variety from whichever input tab is in use: a product of
    projective spaces, a split projective bundle over one (or over the fan
    typed in by hand), or the fan itself.  Blow-ups are applied last."""
    from gwtoric import product_of_projective_spaces
    source = params.get('source', 'fan')
    if source == 'product':
        X = product_of_projective_spaces(*parse_factors(params.get('prod', '')))
    elif source == 'bundle':
        rows = parse_int_list(params.get('bundle_summands', ''))
        if len(rows) < 2:
            raise ValueError('a projective bundle P(O(D_0) + ... + O(D_r)) '
                             'needs at least two summands, one divisor per row')
        if params.get('bundle_base') == 'fan':
            X = typed_fan(params)
        else:
            ns = parse_factors(params.get('bundle_prod', ''), 'the base')
            X = product_of_projective_spaces(*ns)
            rows = [product_divisor(ns, r) for r in rows]
        X = X.projective_bundle(rows)
    else:
        X = typed_fan(params)
    blow = params.get('blowup', '').strip()
    if blow:
        for row in parse_int_list(blow):
            X = X.blowup(tuple(row))
    return X


def parse_classes(spec, X):
    from gwtoric.cli import parse_classes as _p
    spec = spec.strip()
    if not spec:
        return [], []                      # zero insertions are allowed
    classes = _p(spec, X)
    names = [t.strip() for t in spec.split('|')]
    return classes, names


def fmt_fraction(v):
    if isinstance(v, Fraction) and v.denominator == 1:
        return str(v.numerator)
    return str(v)


def class_report(X, K, params, log):
    """Curve classes for c1* (gwtoric.quantum.curve_class_report) with the
    log lines and the JSON summary shown by the page."""
    md = params.get('max_degree', '').strip()
    mspec = params.get('mori', '').strip()
    mori = parse_int_list(mspec) if mspec else None
    rep = X.curve_class_report(K, int(md) if md else None, mori, log)
    betas = rep['betas']
    ver = rep.get('verify')
    summary = {'mode': rep['mode'], 'n_betas': len(betas),
               'fano_index': rep['fano'], 'max_degree': rep['max_degree'],
               'stuck': [{'stratum': list(s), 'cls': list(b)}
                         for s, b in rep['stuck']],
               'nonpositive': [list(z) for z in rep['nonpositive']],
               'not_fano': rep['not_fano'],
               'suggested': [{'stratum': list(s), 'N': list(N)}
                             for s, N in rep.get('suggested', [])],
               'verify': {'checked': len(ver['checked']),
                          'failures': [[b, list(p), str(v)]
                                       for b, p, v in ver['failures']]}
               if ver else None}
    if rep['not_fano']:
        log(rep['not_fano'])
    if rep['mode'] in ('mori', 'mori-auto'):
        log(f'exact list of {len(betas)} curve classes from the cone of '
            f'curves of Z (Z is assumed to be Fano)')
    for s, N in rep.get('suggested', []):
        log(f'inequality {list(N)} derived automatically for the stratum '
            f'V({",".join(map(str, s))}) and checked on the cheapest classes '
            f'it excludes - evidence, not a proof')
    if ver:
        if ver['failures']:
            b, p, v = ver['failures'][0]
            log(f'WARNING: the inequalities are WRONG: they exclude the class '
                f'{b}, which has <{p[0]}, {p[1]}> = {v} != 0')
        else:
            log(f'sample check: every invariant of the {len(ver["checked"])} '
                f'cheapest excluded classes vanishes')
    for s, b in rep['stuck']:
        stratum = ','.join(map(str, s))
        log(f'c1(Z) has degree <= 0 on the class {list(b)} of the stratum '
            f'V({stratum}) and the fan does not tell whether Z contains such '
            f'curves: give a divisor N with N.beta >= 0 on the curves of Z '
            f'in "Mori cone inequalities" to get an exact list')
        if not rep.get('suggested'):
            log('  (no inequality could be derived automatically)')
    if rep['mode'] == 'cutoff':
        log(f'WARNING: c1 has degree <= 0 on the invariant curve'
            f'{"s" if len(rep["nonpositive"]) > 1 else ""} '
            f'{summary["nonpositive"]}; the curve classes are truncated at '
            f'omega.beta <= {rep["max_degree"]}, omega = '
            f'{list(X.fan.ample_divisor())} (c1* is exact modulo Novikov '
            f'monomials of larger omega-degree)')
    return rep, summary


def run_job(job, kind, params):
    from .engine import Cancelled

    def log(msg):
        job['log'].append(str(msg))

    try:
        t0 = time.time()
        if kind == 'spectrum':
            from .gui_spectrum import spectrum_report
            with JOBS_LOCK:
                original = JOBS.get(params.get('matrix_job'))
            if original is None or 'spectral_input' not in original:
                raise ValueError('compute a quantum matrix before updating its spectrum')
            M, Gr, count = original['spectral_input']
            result = spectrum_report(M, Gr, count, params, log, job['stop'].is_set)
            result['seconds'] = round(time.time() - t0, 2)
            job.update(result=result, state='done')
            log(f'done in {result["seconds"]}s (reused the computed matrix)')
            return
        X = build_variety(params)
        X.cancel = job['stop'].is_set
        kspec = params.get('K', '').strip()
        K = X.check_K(parse_int_list(kspec)) if kspec else []
        dim = X.n - len(K)
        log(f'{X!r}')
        log(f'rays {X.fan.rays}')
        if K:
            log(f'complete intersection Z of codimension {len(K)}: '
                f'divisors {[list(a) for a in K]}, dim Z = {dim}')
        result = {
            'dim': dim, 'k': X.k, 'picard': X.k - X.n, 'codim': len(K),
            'K': [list(a) for a in K],
            'fixed_points': len(X.fan.max_cones),
            # only for the toric variety itself: whether a complete
            # intersection is Fano cannot be read off the fan
            'fano': None if K else X.is_fano,
            'rays': [list(r) for r in X.fan.rays],
            'cones': [list(c) for c in X.fan.max_cones],
        }

        if kind == 'info':
            result['betti'] = X.betti
            result['hodge'] = X.hodge_diamond_str()
            if K:
                from .hodge import HodgeNotSupported
                try:
                    result['ci_hodge'] = X.hodge_report(K)
                except HodgeNotSupported as exc:
                    result['ci_hodge'] = {'unavailable': str(exc)}
                else:
                    result['fano'] = True
            result['h2_generators'] = X.h2_generators
            result['novikov'] = [repr(X.reduce(X.divisor(a)))
                                 for a in X.novikov_divisors]
            result['grading_y'] = [str(v) for v in X.c1_grading(K)]
            result['nef_novikov'] = X.fan.nef_basis() is not None
            result['basis'] = [
                {'index': i, 'name': name, 'degree': c.degree()}
                for i, (name, c) in enumerate(zip(X.class_names, X.classes))]
            result['c1'] = repr(X.reduce(X.c1_ci(K)))
            r, A = X.anticanonical_generator(K)
            result['index'] = {'r': r, 'A': repr(X.reduce(X.divisor(A))),
                               'coindex': dim + 1 - r}
            result['h2_basis'] = [list(b) for b in X.h2_basis]
            result['curves'] = [
                {'wall': list(tau), 'cls': list(cls),
                 'deg': X.c1_degree(cls, K),
                 'kdeg': [X.fan.wall_degree(a, cls) for a in K]}
                for tau, cls in X.wall_curves]
            result['ample'] = list(X.fan.ample_divisor())
            result['classes'] = class_report(X, K, params, log)[1]

        elif kind == 'gw':
            beta = X.beta([int(v) for v in params['beta'].replace(' ', '')
                           .split(',') if v != ''])
            classes, names = parse_classes(params['classes'], X)
            log(f'computing <{", ".join(names)}>_beta={list(beta)} '
                f'(c1.beta = {X.c1_degree(beta, K)}, expected codim '
                f'{X.expected_degree(beta, len(classes), K)}) ...')
            val = X.gw(classes, beta, K, progress=log)
            result['value'] = fmt_fraction(val)
            result['insertions'] = names
            result['beta'] = list(beta)
            result['c1_beta'] = X.c1_degree(beta, K)
            result['novikov'] = X.novikov_exponents(beta)

        elif kind == 'sqm':
            import sympy
            from .gui_spectrum import novikov_values, spectrum_report
            # Validate the point before spending time on localization.
            novikov_values(params.get('eval_y', ''), len(X.h2_generators))
            spec = params.get('betas', '').strip()
            if spec:
                betas = [X.beta(b) for b in parse_int_list(spec)]
                fano = None
                log(f'{len(betas)} user-given curve classes')
            else:
                rep, result['classes'] = class_report(X, K, params, log)
                fano, betas = rep['fano'], rep['betas']
                log(f'Fano index {fano}; {len(betas)} curve classes '
                    f'(max c1-degree {max(X.c1_degree(b, K) for b in betas)})')
            M, Gr, names = X.small_quantum_multiplication(
                betas, K, progress=log, workers='auto',
                cancel=job['stop'].is_set)
            log(f'matrix assembled in {time.time() - t0:.1f}s')
            # Keep the symbolic matrix so changing the point does not repeat GW sums.
            job['spectral_input'] = (M, Gr, len(X.h2_generators))

            log('computing characteristic polynomial ...')
            lam = sympy.Symbol('lambda')
            char_poly = sympy.Matrix(M).charpoly(lam).as_expr()

            result['fano_index'] = fano
            result['grading_y'] = [str(v) for v in X.c1_grading(K)]
            result['novikov'] = [repr(X.reduce(X.divisor(a)))
                                 for a in X.novikov_divisors]
            try:
                result['specialized'] = [[str(v) for v in row]
                                         for row in X.specialize_c1(M, K)]
            except Exception as exc:                        # noqa: BLE001
                log(f'could not specialize to one variable: {exc}')
            result['betas'] = [list(b) for b in betas]
            result['basis'] = names
            result['y_rays'] = X.h2_generators
            result['matrix'] = [[str(v) for v in row] for row in M]
            result['grading'] = [str(Gr[a][a]) for a in range(len(Gr))]
            result['char_poly'] = str(char_poly)
            result['spectrum'] = spectrum_report(
                M, Gr, len(X.h2_generators), params, log, job['stop'].is_set)
            if params.get('symbolic'):
                log('computing symbolic eigenvalues ...')
                try:
                    result['eigen_symbolic'] = [str(v)
                                                for v in X.eigenvalues(M)]
                except Exception as exc:                    # noqa: BLE001
                    log(f'no closed form for the eigenvalues: {exc}')
        else:
            raise ValueError(f'unknown action {kind!r}')

        result['seconds'] = round(time.time() - t0, 2)
        job['result'] = result
        job['state'] = 'done'
        log(f'done in {result["seconds"]}s')
    except Cancelled:
        job['state'] = 'stopped'
        job['error'] = 'stopped on request'
        log('stopped')
    except Exception as exc:                                # noqa: BLE001
        job['state'] = 'error'
        job['error'] = f'{type(exc).__name__}: {exc}'
        job['log'].append(traceback.format_exc(limit=3))


# --------------------------------------------------------------------- HTTP
class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):                           # silence stderr
        pass

    def _json(self, obj, code=200):
        data = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path in ('/', '/index.html'):
            data = PAGE.encode()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        elif self.path == '/api/presets':
            self._json([{'label': p[0], 'rays': p[1], 'cones': p[2],
                         'blowup': p[3], 'K': p[4],
                         'mori': p[5] if len(p) > 5 else ''}
                        for p in PRESETS])
        elif self.path.startswith('/api/stop'):
            jid = self.path.split('id=')[-1]
            with JOBS_LOCK:
                job = JOBS.get(jid)
            if job is None:
                self._json({'error': 'no such job'}, 404)
            else:
                job['stop'].set()
                job['log'].append('stop requested; finishing the current step')
                self._json({'ok': True})
        elif self.path.startswith('/api/status'):
            jid = self.path.split('id=')[-1]
            with JOBS_LOCK:
                job = JOBS.get(jid)
            if job is None:
                self._json({'error': 'no such job'}, 404)
            else:
                self._json({'state': job['state'], 'log': job['log'],
                            'result': job.get('result'),
                            'error': job.get('error')})
        else:
            self._json({'error': 'not found'}, 404)

    def do_POST(self):
        if self.path != '/api/run':
            self._json({'error': 'not found'}, 404)
            return
        try:
            length = int(self.headers.get('Content-Length', 0))
            params = json.loads(self.rfile.read(length) or b'{}')
            if not isinstance(params, dict):
                raise ValueError('body must be a JSON object')
        except Exception as exc:                            # noqa: BLE001
            self._json({'error': f'bad request: {exc}'}, 400)
            return
        kind = params.pop('action', 'info')
        jid = uuid.uuid4().hex[:12]
        job = {'state': 'running', 'log': [], 'result': None,
               'stop': threading.Event()}
        with JOBS_LOCK:
            JOBS[jid] = job
        threading.Thread(target=run_job, args=(job, kind, params),
                         daemon=True).start()
        self._json({'id': jid})


PAGE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>gwtoric — toric quantum multiplication lab</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&family=Inter:wght@400;500;600;700&display=swap');
:root {
  --bg: #09090b; --panel: #18181b; --edge: #27272a; --fg: #fafafa;
  --dim: #a1a1aa; --acc: #f59e0b; --acc-hover: #d97706;
  --ok: #34d399; --err: #f87171; --radius: 8px;
}
* { box-sizing:border-box; margin: 0; padding: 0; }
body {
  background:var(--bg); color:var(--fg);
  font-family: 'Inter', -apple-system, sans-serif;
  font-size: 14.5px; line-height: 1.6; -webkit-font-smoothing: antialiased;
}
header {
  padding: 16px 28px; background: var(--panel);
  border-bottom: 1px solid var(--edge);
  display: flex; align-items: baseline; gap: 16px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
header h1 { font-size: 20px; font-weight: 700; color: #fff; letter-spacing: -0.5px; }
header span { color: var(--dim); font-size: 13.5px; font-weight: 400; }
main { display: grid; grid-template-columns: 380px 1fr; gap: 0;
       min-height: calc(100vh - 61px); }
@media (max-width: 800px) { main { grid-template-columns: 1fr; } }
#controls { padding: 24px 28px; border-right: 1px solid var(--edge);
            background: rgba(24, 24, 27, 0.4); }
#results  { padding: 24px 32px; overflow-x: auto; }
.card-header { color: var(--fg); font-size: 13px; font-weight: 600;
               margin-top: 24px; padding-bottom: 6px;
               border-bottom: 1px solid var(--edge); }
.card-header:first-child { margin-top: 0; }
label { display: block; margin: 14px 0 6px; color: var(--dim);
        font-size: 12px; font-weight: 600; text-transform: uppercase;
        letter-spacing: 0.05em; }
input, select, textarea {
  width: 100%; padding: 10px 12px; border-radius: var(--radius);
  border: 1px solid var(--edge); background: var(--panel); color: var(--fg);
  font-family: 'Fira Code', monospace; font-size: 13px;
  transition: all 0.2s; outline: none;
}
textarea { resize: vertical; min-height: 58px; }
input:focus, select:focus, textarea:focus {
  border-color: var(--acc); box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.2); }
.tabs { display: flex; gap: 4px; margin: 14px 0 0; }
.tabs button {
  margin: 0; flex: 1; padding: 8px 4px; font-size: 11.5px; font-weight: 600;
  background: var(--panel); border: 1px solid var(--edge); color: var(--dim);
  box-shadow: none; transform: none; text-transform: uppercase;
  letter-spacing: 0.04em; border-radius: var(--radius) var(--radius) 0 0;
}
.tabs button:hover { background: #27272a; color: var(--fg); transform: none; }
.tabs button.on { background: rgba(245, 158, 11, 0.15); color: var(--acc);
                  border-color: rgba(245, 158, 11, 0.4); }
.pane { display: none; padding: 2px 14px 14px; background: rgba(9,9,11,0.5);
        border: 1px solid var(--edge); border-top: none;
        border-radius: 0 0 var(--radius) var(--radius); }
.pane.on { display: block; }
.row { display: flex; gap: 12px; }
.row > div { flex: 1; }
.check { display: flex; align-items: center; gap: 8px; margin-top: 12px;
         color: var(--dim); font-size: 13px; }
.check input { width: auto; }
button {
  margin-top: 16px; margin-right: 10px; padding: 10px 20px;
  border-radius: var(--radius); border: none; background: var(--acc);
  color: #111; font-weight: 600; font-size: 13.5px; cursor: pointer;
  transition: all 0.2s; outline: none; box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}
button:hover { background: var(--acc-hover); transform: translateY(-1px); }
button.secondary { background: var(--panel); border: 1px solid var(--edge);
                   color: var(--fg); box-shadow: none; }
button.secondary:hover { background: #27272a; }
button:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
#log {
  margin-top: 24px; padding: 12px 16px; background: #000;
  border: 1px solid var(--edge); border-radius: var(--radius);
  max-height: 250px; overflow-y: auto; font-family: 'Fira Code', monospace;
  font-size: 12px; color: var(--ok); white-space: pre-wrap;
  box-shadow: inset 0 2px 6px rgba(0,0,0,0.3);
}
h2 { font-size: 18px; font-weight: 600; margin: 24px 0 12px; color: #fff;
     letter-spacing: -0.3px; }
table { border-collapse: collapse; margin: 12px 0 24px;
        background: var(--panel); border-radius: var(--radius);
        overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
td, th { border: 1px solid var(--edge); padding: 8px 14px;
         font-family: 'Fira Code', monospace; font-size: 13px;
         text-align: center; }
th { color: var(--dim); font-weight: 600; background: rgba(255,255,255,0.02); }
tr:hover td { background: rgba(255,255,255,0.02); }
pre { font-family: 'Fira Code', monospace; font-size: 14px; line-height: 1.5;
      padding: 12px 16px; background: var(--panel);
      border: 1px solid var(--edge); border-radius: var(--radius);
      display: inline-block; margin-bottom: 16px; }
.badge {
  display: inline-block; margin: 4px 12px 4px 0; padding: 4px 12px;
  border-radius: 20px; background: rgba(245, 158, 11, 0.15);
  border: 1px solid rgba(245, 158, 11, 0.3); color: var(--acc);
  font-size: 12.5px; font-weight: 500;
}
.badge.no { background: rgba(248,113,113,0.12);
            border-color: rgba(248,113,113,0.3); color: var(--err); }
.dom { color: var(--ok); font-weight: 700;
       background: rgba(52, 211, 153, 0.1) !important; }
.err { color: var(--err); }
.note { color: var(--dim); font-size: 12px; }
sup { font-size: 10px; font-weight: 600; }
</style></head><body>
<header><h1>gwtoric</h1>
<span>Gromov&ndash;Witten invariants &amp; quantum multiplication for smooth
projective toric varieties — from a fan, a product of projective spaces or
a projective bundle</span></header>
<main>
<div id="controls">
  <div class="card-header">1. The variety</div>
  <label>Preset library</label>
  <select id="preset"><option value="">— choose a pre-configured example —</option></select>
  <div class="tabs">
    <button id="tab-product" class="tab">Product of P&#8319;</button>
    <button id="tab-bundle" class="tab">Projective bundle</button>
    <button id="tab-fan" class="tab">Fan</button>
  </div>

  <div class="pane" id="pane-product">
    <label>Factors of P<sup>n&#8321;</sup> &times; &hellip; &times; P<sup>n<sub>m</sub></sup></label>
    <input id="prod" value="2" placeholder="e.g. 2 for P&sup2;, or 1,1 for P&sup1;&times;P&sup1;">
    <div class="note" style="margin-top:6px">rays e&#8321;,&hellip;,e<sub>n</sub>,
    &minus;e&#8321;&minus;&hellip;&minus;e<sub>n</sub> per factor, in that order.</div>
  </div>

  <div class="pane" id="pane-bundle">
    <label>Base</label>
    <select id="bundle_base">
      <option value="product">a product of projective spaces</option>
      <option value="fan">the fan typed in the Fan tab</option>
    </select>
    <div id="bundle_prod_box">
      <label>Factors of the base</label>
      <input id="bundle_prod" value="5" placeholder="e.g. 5 for P&#8309;, or 1,1 for P&sup1;&times;P&sup1;">
    </div>
    <label>Summands D&#8320;, &hellip;, D<sub>r</sub> of E (one divisor per row)</label>
    <textarea id="bundle_summands" placeholder="over a product: one multidegree per factor, e.g. the rows 0 and 2 for P(O&oplus;O(2)); or all k ray coefficients">0
2</textarea>
    <div class="note" style="margin-top:6px">P(E) &rarr; X for
    E = O(D&#8320;) &oplus; &hellip; &oplus; O(D<sub>r</sub>), by the
    construction of Cox&ndash;Little&ndash;Schenck Prop.&nbsp;7.3.3: the rays of
    X keep their index and the fibre rays
    e&#8321;,&hellip;,e<sub>r</sub>, e&#8320;=&minus;&Sigma;e<sub>i</sub> are
    appended.  Only the differences D<sub>i</sub>&minus;D&#8320; matter, since
    P(E)=P(E&otimes;L).  Over a product, a row of one multidegree per factor
    means O(a&#8321;,&hellip;,a<sub>m</sub>); over the typed fan, a row is k ray
    coefficients or Picard-rank coordinates.</div>
  </div>

  <div class="pane" id="pane-fan">
    <label>Rays (one per row, or separated by ;)</label>
    <textarea id="rays">1,0;0,1;-1,-1</textarea>
    <label>Maximal cones (0-based ray indices)</label>
    <textarea id="cones">0,1;1,2;0,2</textarea>
  </div>

  <label>Blow up cones (optional, e.g. 0,1,2)</label>
  <input id="blowup" placeholder="star subdivisions applied in order, separated by ;">
  <label>Complete intersection (optional): one nef divisor per row</label>
  <textarea id="K" placeholder="k ray coefficients, or coordinates on the H&sup2; basis rays; e.g. 5 (quintic in P4), 1,1 ((1,1) in P2xP2), 2;2;2"></textarea>
  <button id="binfo" class="secondary" style="width:100%">Fan, cohomology &amp; curves</button>

  <div class="card-header">2. Quantum multiplication by c&#8321;(TX)</div>
  <label>Curve classes (optional; automatic list and completeness mode reported below)</label>
  <input id="betas" placeholder="rows of k integers separated by ;  e.g. 0,0,0,0;1,0,1,2">
  <label>Mori cone inequalities (optional, complete intersections): divisors N with N&middot;&beta; &ge; 0 on the curves of Z</label>
  <textarea id="mori" placeholder="one divisor per row, like the complete intersection; only needed when the log asks for it"></textarea>
  <div class="row">
    <div>
      <label>Novikov point for spectrum &amp; cyclic determinant</label>
      <input id="eval_y" placeholder="e.g. y1=2, y2=-1">
      <div class="note">Omitted variables equal 1. Exact fractions, decimals,
      sqrt(...) and I are supported.</div>
    </div>
    <div>
      <label>Max ample degree &omega;&middot;&beta; (cutoff, non-Fano)</label>
      <input id="max_degree" placeholder="default (dim+3)&middot;min &omega;&middot;C">
    </div>
  </div>
  <div class="check"><input type="checkbox" id="symbolic" checked>
    <span>eigenvalues of the symbolic matrix (may be slow for large H*)</span></div>
  <div class="check"><input type="checkbox" id="connection" checked>
    <span>connection exponents for selected eigenvalues</span></div>
  <label>Eigenvalues &lambda; of K<sup>F</sup> = &minus;c&#8321;&#8902; (optional)</label>
  <input id="eigen_selection" placeholder="all by default; or e.g. 0; -6*sqrt(3)">
  <div class="note">Separate exact eigenvalues by semicolons. The cyclic
  determinant tests the whole matrix at the chosen point, independently of
  this selection.</div>
  <button id="bsqm" style="width:100%">Compute c&#8321;(TX)&#8902; matrix</button>
  <button id="bspectrum" class="secondary" style="width:100%" disabled>Update spectrum &amp; cyclic determinant</button>
  <div class="note">Update reuses the last matrix. After changing the variety,
  complete intersection or curve classes, compute a new matrix first.</div>

  <div class="card-header">3. One GW invariant</div>
  <label>Curve class &beta;</label>
  <input id="beta" placeholder="k integers (one per ray) or Picard-rank coordinates">
  <label>Insertions (separated by |)</label>
  <input id="classes" placeholder="e.g. pt | pt | x0*x1 | 2*c1">
  <button id="bgw" class="secondary" style="width:100%">Compute invariant</button>
  <div class="card-header">Stop</div>
  <button id="bstop" class="secondary" style="width:100%;
    border-color:var(--err);color:var(--err)">Stop the running computation</button>
  <div class="note" style="margin-top:6px">the job ends at its next
  checkpoint (a tree of the graph sum, a metric row or a curve class) and its
  worker processes are killed; closing this tab does <b>not</b> stop it.</div>

  <div id="log">System ready. Waiting for input...</div>
</div>
<div id="results"><h2>Results</h2>
<div id="out" style="color:var(--dim)">Pick a preset, a product of
projective spaces, a projective bundle or a fan of your own, and press
<b>Fan, cohomology &amp; curves</b> to see the H<sub>2</sub> basis and the
invariant curves, then <b>c&#8321;(TX)&#8902; matrix</b>.  Progress streams
in the log.</div></div>
</main>
<script>
const $ = id => document.getElementById(id);
const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');
const pretty = s => esc(s).replace(/\*\*(\d+)/g,'<sup>$1</sup>')
                          .replace(/\*/g,'&middot;');
const BTN = ['bsqm','binfo','bgw'];
let current=null, matrixJob=null;
function busy(on){ BTN.forEach(b=>$(b).disabled=on);
  $('bspectrum').disabled = on || !matrixJob;
  $('bstop').disabled = !on;
  $('bstop').textContent = on ? 'Stop the running computation'
                              : 'Stop (nothing is running)'; }
$('bstop').onclick=()=>{ if(current){ $('bstop').disabled=true;
  $('bstop').textContent='stopping...';
  fetch('/api/stop?id='+current).then(()=>{}).catch(()=>{}); } };
busy(false);
const TABS=['product','bundle','fan'];
let source='product';
function tab(name){ source=name;
  TABS.forEach(t=>{ $('tab-'+t).classList.toggle('on', t===name);
                    $('pane-'+t).classList.toggle('on', t===name); }); }
TABS.forEach(t=>$('tab-'+t).onclick=()=>tab(t));
$('bundle_base').onchange = ()=>{ $('bundle_prod_box').style.display =
  $('bundle_base').value==='fan' ? 'none' : 'block'; };
tab('product');
fetch('/api/presets').then(r=>r.json()).then(ps=>{
  ps.forEach((p,i)=>{ const o=document.createElement('option');
    o.value=i; o.textContent=p.label; $('preset').appendChild(o); });
  window._presets=ps; });
$('preset').onchange = ()=>{ const p=window._presets[$('preset').value];
  if(p){ $('rays').value=p.rays.split(';').join('\n');
         $('cones').value=p.cones.split(';').join('\n');
         $('blowup').value=p.blowup;
         $('K').value=p.K.split(';').join('\n');
         $('mori').value=p.mori.split(';').join('\n');
         tab('fan'); } };
// hand the fan a product/bundle tab generated to the Fan tab for editing
function toFanTab(){ const r=window._lastFan; if(!r) return;
  $('rays').value=r.rays.map(v=>v.join(',')).join('\n');
  $('cones').value=r.cones.map(v=>v.join(',')).join('\n');
  $('blowup').value=''; tab('fan'); }
let timer=null;
function run(action){
  const params={action, source, rays:$('rays').value, cones:$('cones').value,
    prod:$('prod').value, bundle_base:$('bundle_base').value,
    bundle_prod:$('bundle_prod').value,
    bundle_summands:$('bundle_summands').value,
    blowup:$('blowup').value, K:$('K').value, betas:$('betas').value,
    eval_y:$('eval_y').value, max_degree:$('max_degree').value, mori:$('mori').value,
    symbolic:$('symbolic').checked,
    connection:$('connection').checked, eigen_selection:$('eigen_selection').value,
    matrix_job:matrixJob,
    beta:$('beta').value, classes:$('classes').value};
  if(action==='sqm') matrixJob=null;
  busy(true); $('bstop').disabled=false; current=null;
  $('log').textContent='starting...';
  const fail = msg => { clearInterval(timer); busy(false);
    const target=action==='spectrum' ? $('spectrum-results') : $('out');
    target.innerHTML='<span class="err">'+esc(msg)+'</span>'; };
  fetch('/api/run',{method:'POST',body:JSON.stringify(params)})
    .then(r=>r.json()).then(({id,error})=>{
      if(error){ fail(error); return; }
      current=id;
      timer=setInterval(()=>fetch('/api/status?id='+id)
        .then(r=>r.json()).then(st=>{
          $('log').textContent=st.log.join('\n');
          $('log').scrollTop=$('log').scrollHeight;
          if(st.state!=='running'){ clearInterval(timer); busy(false);
            current=null;
            if(st.state==='stopped') fail('stopped on request');
            else if(st.state==='error') fail(st.error);
            else {
              if(action==='sqm') matrixJob=id;
              render(action, st.result); busy(false);
            } }
        }).catch(()=>{}),700); })
    .catch(e=>fail('request failed: '+e));
}
function badges(res){
  return (res.codim?'<span class="badge">complete intersection, codim '+
      res.codim+': '+res.K.map(vec).join(' ')+'</span>':'')+
    '<span class="badge">dim '+res.dim+'</span>'+
    '<span class="badge">'+res.k+' rays</span>'+
    '<span class="badge">Picard rank '+res.picard+'</span>'+
    '<span class="badge">'+res.fixed_points+' fixed points</span>'+
    (res.fano===null?'':res.fano?'<span class="badge">Fano</span>':
              '<span class="badge no">not Fano</span>')+
    '<span class="badge">'+res.seconds+'s</span>';
}
const vec = v => '('+v.join(', ')+')';
function classBadges(c){
  if(!c) return '';
  let h='<span class="badge">Fano index '+c.fano_index+'</span>'+
        '<span class="badge">'+c.n_betas+' curve classes for c&#8321;&#8902;</span>';
  if(c.mode==='mori'||c.mode==='mori-auto')
    h+='<span class="badge">exact list from the cone of curves of Z '+
       '(Z assumed Fano)</span>';
  (c.suggested||[]).forEach(s=>h+='<span class="badge">inequality '+
       vec(s.N)+' derived automatically for V('+s.stratum.join(',')+
       ')</span>');
  if(c.verify)
    h+=(c.verify.failures.length
        ? '<span class="badge no">the inequalities are WRONG: they exclude '+
          vec(c.verify.failures[0][0])+', whose invariant is '+
          esc(c.verify.failures[0][2])+'</span>'
        : '<span class="badge">inequalities checked on '+c.verify.checked+
          ' excluded classes (evidence, not a proof)</span>');
  if(c.mode==='cutoff')
    h+='<span class="badge no">truncated at &omega;&middot;&beta; &le; '+
       c.max_degree+': c&#8321; has degree &le; 0 on '+
       c.nonpositive.map(vec).join(' ')+'</span>';
  if(c.not_fano) h+='<span class="badge no">'+esc(c.not_fano)+'</span>';
  c.stuck.forEach(s=>h+='<span class="badge no">Mori cone inequality needed: '+
       'c&#8321;(Z)&middot;'+vec(s.cls)+' &le; 0 on the stratum V('+
       s.stratum.join(',')+')</span>');
  return h;
}
function renderSpectrum(s){
  let h='<h2>Spectrum at '+esc(s.point)+'</h2>'+
    '<div class="note">This analysis uses the last computed matrix and its '+
    'curve classes, on the displayed basis (ambient cohomology for a complete intersection).</div>';
  h+='<h3>Specialized c&#8321;&#8902;</h3><table>';
  s.matrix.forEach(row=>{h+='<tr>'; row.forEach(v=>h+='<td>'+pretty(v)+'</td>'); h+='</tr>';});
  h+='</table>';
  h+='<h3>Cyclic determinant</h3><div>&Delta; = det(1, K<sup>F</sup>1, &hellip;, '+
    '(K<sup>F</sup>)<sup>N&minus;1</sup>1), K<sup>F</sup> = &minus;c&#8321;&#8902;</div>'+
    '<pre>'+pretty(s.delta)+'</pre><div class="note">'+
    (s.cyclic===true?'Nonzero: the unit is a cyclic vector on this basis.':
      s.cyclic===false?'Zero: the unit does not generate this basis under powers of K^F; the cyclicity test fails.':
      'Could not decide whether the determinant vanishes; cyclicity is not certified.')+
    ' This is a test of the whole matrix, not of an individual eigenvalue.</div>';
  const fmt=x=>Math.abs(x)<1e-12?'0':Number(x.toPrecision(8)).toString();
  const complex=(re,im)=>fmt(re)+(Math.abs(im)>1e-12?
    (im<0?' - ':' + ')+fmt(Math.abs(im))+'i':'');
  if(s.eigenvalues){
    h+='<h3>Eigenvalues</h3><table><tr><th>c&#8321;&#8902;</th><th>K<sup>F</sup> = &minus;c&#8321;&#8902;</th></tr>';
    s.eigenvalues.forEach(([re,im])=>h+='<tr><td>'+complex(re,im)+
      '</td><td>'+complex(-re,-im)+'</td></tr>');
    h+='</table><div class="note">Numerical values with multiplicity, ordered by modulus. Spectral radius: '+
      fmt(Math.max(...s.eigenvalues.map(([re,im])=>Math.hypot(re,im))))+'</div>';
  }
  if(s.spectrum_error) h+='<div class="err">Numerical spectrum unavailable: '+esc(s.spectrum_error)+'</div>';
  if(s.connection_error) h+='<div class="err">Connection exponents unavailable: '+esc(s.connection_error)+'</div>';
  if(s.connection_requested){
    h+='<h3>Connection spectrum for selected eigenvalues</h3><table><tr>'+
      '<th>&lambda; of K<sup>F</sup></th><th>Algebraic multiplicity</th><th>Leading powers s</th>'+
      '<th>Classes mod Z</th><th>Status</th></tr>';
    s.factors.forEach(f=>{
      const label=f.eigenvalue===null?'Roots of '+f.poly+' = 0':f.eigenvalue;
      const status=f.error || ((f.complete?'Complete power count':'Incomplete power count')+
        ' ('+f.method+')'+(f.note?'; '+f.note:''));
      h+='<tr><td>'+pretty(label)+'</td><td>'+f.multiplicity+'</td><td>'+
        (f.powers?f.powers.map(pretty).join(', '):'Unavailable')+'</td><td>'+
        (f.F?'{'+f.F.map(esc).join(', ')+'}':'Unavailable')+'</td><td>'+esc(status)+'</td></tr>';
    });
    h+='</table><div class="note">For d/du + K<sup>F</sup>/u&sup2; + G/u. '+
      'Rows labeled by a polynomial apply to each of its roots. Unsupported factors are reported explicitly; '+
      'this pointwise calculation does not issue a rationality verdict.</div>';
  }
  return h;
}
function render(action,res){
  if(action==='spectrum'){
    $('spectrum-results').innerHTML=renderSpectrum(res);
    return;
  }
  if(action!=='sqm') matrixJob=null;
  let h=badges(res);
  if(action==='info'){
    h+=classBadges(res.classes);
    h+='<h2>Fan</h2><table><tr><th>&rho;<sub>i</sub></th><th>ray</th></tr>';
    res.rays.forEach((r,i)=>h+='<tr><td>'+i+'</td><td>'+vec(r)+'</td></tr>');
    h+='</table><div class="note">maximal cones: '+
       res.cones.map(vec).join('  ')+'</div>';
    window._lastFan=res;
    if(source!=='fan') h+='<button class="secondary" onclick="toFanTab()">'+
       'Edit this fan by hand (copy it into the Fan tab)</button>';
    if(res.codim){
      const ci=res.ci_hodge;
      h+='<h2>Complete-intersection Hodge diamond</h2>';
      if(ci.unavailable) h+='<div class="note">Not computed: '+esc(ci.unavailable)+'</div>';
      else h+='<pre>'+esc(ci.diamond)+'</pre><div class="note">'+
        'Betti numbers b<sub>0</sub>, ..., b<sub>'+2*ci.dimension+'</sub> = ['+ci.betti.join(', ')+
        '] &nbsp; Euler characteristic = '+ci.euler+'<br>'+esc(ci.assumptions)+
        '<br>Method: '+esc(ci.method)+
        '<br>The quantum matrix still acts on ambient cohomology; primitive middle classes are not added.</div>';
    }
    h+='<h2>'+(res.codim?'Ambient Hodge diamond':'Hodge diamond')+'</h2><pre>'+esc(res.hodge)+'</pre>'+
       '<div class="note">Betti numbers b<sub>0</sub>, b<sub>2</sub>, … = ['+
       res.betti.join(', ')+']</div>';
    h+='<h2>'+(res.codim?'Ambient cohomology basis':'Cohomology basis')+'</h2><table><tr><th>&sigma;</th><th>class</th>'+
       '<th>degree</th></tr>';
    res.basis.forEach(b=>h+='<tr><td>&sigma;<sub>'+b.index+'</sub></td><td>'+
       pretty(b.name)+'</td><td>'+b.degree+'</td></tr>');
    const Z=res.codim?'Z':'X';
    h+='</table><div class="note">c&#8321;(T'+Z+') = '+pretty(res.c1)+
       (res.codim?' (restricted to Z; ambient classes)':'')+
       ' &nbsp;·&nbsp; H&sup2; basis rays ['+res.h2_generators.join(', ')+
       '] (the coordinates accepted in "Complete intersection")</div>';
    h+='<div class="note">Novikov variables: '+(res.novikov||[]).map((d,j)=>
       'y<sub>'+(j+1)+'</sub> = q<sup>'+pretty(d)+'</sup> (degree '+
       res.grading_y[j]+')').join(', ')+' &nbsp;&mdash;&nbsp; q<sup>&beta;</sup> '+
       '= &prod;<sub>j</sub> y<sub>j</sub><sup>A<sub>j</sub>&middot;&beta;</sup>'+
       (res.nef_novikov?', a nef basis of Pic X, so the exponents are &ge; 0'
                       :'; no nef lattice basis was found, so exponents can be '+
                        'negative')+'</div>';
    h+='<h2>Fano index</h2><div>&minus;K<sub>'+Z+'</sub> = '+res.index.r+
       ' &middot; ('+pretty(res.index.A)+')'+(res.codim?'|<sub>Z</sub>':'')+
       ' &nbsp;&rArr;&nbsp; index <b>'+res.index.r+'</b>, coindex '+
       res.index.coindex+'</div><div class="note">gcd of the degrees '+
       'c&#8321;&middot;&beta; over a basis of H<sub>2</sub>(X, Z), i.e. the '+
       'divisibility of &minus;K in Pic X'+(res.codim?' (equal to Pic Z for a '+
       'complete intersection of ample divisors of dimension &ge; 3; a '+
       'curve or a surface can have a larger Picard group)':'')+
       '; meaningful when '+Z+' is Fano.</div>';
    h+='<h2>Curve classes</h2><div class="note">H<sub>2</sub> basis '+
       '(vectors a<sub>&rho;</sub>, one entry per ray): '+
       res.h2_basis.map(vec).join('  ')+'</div>';
    h+='<table><tr><th>wall (rays)</th><th>class</th>'+
       (res.codim?'<th>D<sub>m</sub>·C</th>':'')+'<th>c&#8321;('+Z+')·C</th></tr>';
    res.curves.forEach(c=>h+='<tr><td>'+vec(c.wall)+'</td><td>'+vec(c.cls)+
       '</td>'+(res.codim?'<td>'+c.kdeg.join(', ')+'</td>':'')+
       '<td>'+c.deg+'</td></tr>');
    h+='</table><div class="note">ample divisor used: '+vec(res.ample)+'</div>';
  } else if(action==='gw'){
    h+='<h2>&lang;'+res.insertions.map(esc).join(', ')+'&rang;<sub>&beta;='+
       vec(res.beta)+'</sub> = <b style="font-size:22px">'+esc(res.value)+
       '</b></h2>';
    h+='<div class="note">c&#8321;·&beta; = '+res.c1_beta+
       ' &nbsp;·&nbsp; q<sup>&beta;</sup> = '+
       res.novikov.map((e,j)=>'y<sub>'+(j+1)+'</sub><sup>'+e+'</sup>').join('')+
       '</div>';
  } else {
    if(res.classes) h+=classBadges(res.classes);
    else h+='<span class="badge">'+res.betas.length+' curve classes (given)</span>';
    h+='<h2>c&#8321;(T'+(res.codim?'Z':'X')+')&#8902; in the '+
       (res.codim?'ambient ':'')+'basis ['+res.basis.map(pretty).join(', ')+
       ']</h2><table><tr><th></th>';
    res.basis.forEach(b=>h+='<th>'+pretty(b)+'</th>'); h+='</tr>';
    res.matrix.forEach((row,i)=>{ h+='<tr><th>'+pretty(res.basis[i])+'</th>';
      row.forEach(v=>h+='<td>'+pretty(v)+'</td>'); h+='</tr>'; });
    h+='</table>';
    h+='<div class="note">curve classes used: '+res.betas.map(vec).join('  ')+
       '<br>Novikov variables: '+(res.novikov||[]).map((d,j)=>
         'y<sub>'+(j+1)+'</sub> = q<sup>'+pretty(d)+'</sup>'+
         (res.grading_y?' (degree '+res.grading_y[j]+')':'')).join(', ')+
       ' &nbsp;&mdash;&nbsp; a nef basis of Pic X, so the exponents of '+
       'q<sup>&beta;</sup> are &ge; 0</div>';
    if(res.specialized){
      h+='<h2>One variable: y<sub>j</sub> &rarr; t<sup>c<sub>j</sub></sup>, '+
         'i.e. q<sup>&beta;</sup> &rarr; t<sup>c&#8321;&middot;&beta;</sup></h2>'+
         '<table><tr><th></th>';
      res.basis.forEach(b=>h+='<th>'+pretty(b)+'</th>'); h+='</tr>';
      res.specialized.forEach((row,i)=>{ h+='<tr><th>'+pretty(res.basis[i])+'</th>';
        row.forEach(v=>h+='<td>'+pretty(v)+'</td>'); h+='</tr>'; });
      h+='</table><div class="note">this identifies every curve class of the '+
         'same c&#8321;-degree; it is a faithful record only when finitely '+
         'many of them contribute.</div>';
    }
    h+='<h2>Grading</h2><div>diag('+res.grading.map(esc).join(', ')+')</div>';
    if(res.char_poly)
      h+='<h2>Characteristic polynomial</h2><pre>'+pretty(res.char_poly)+'</pre>';
    h+='<div id="spectrum-results">'+renderSpectrum(res.spectrum)+'</div>';
    if(res.eigen_symbolic){
      h+='<h2>Eigenvalues (symbolic)</h2><table>';
      res.eigen_symbolic.forEach(v=>h+='<tr><td>'+pretty(v)+'</td></tr>');
      h+='</table>';
    }
  }
  $('out').innerHTML=h;
}
$('bsqm').onclick=()=>run('sqm');
$('bspectrum').onclick=()=>run('spectrum');
$('binfo').onclick=()=>run('info');
$('bgw').onclick=()=>run('gw');
</script></body></html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--port', type=int, default=8643)
    ap.add_argument('--no-browser', action='store_true')
    args = ap.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    url = f'http://127.0.0.1:{args.port}'
    print(f'gwtoric GUI serving at {url}  (Ctrl-C to stop)')
    if not args.no_browser:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nbye')


if __name__ == '__main__':
    main()

