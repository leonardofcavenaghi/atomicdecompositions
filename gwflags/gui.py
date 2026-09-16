"""Local web GUI for gwflags — run quantum-multiplication experiments
without touching the command line.

    python3 -m gwflags.gui            # serves http://127.0.0.1:8642 and
                                      # opens the browser
    python3 -m gwflags.gui --port N --no-browser

Stdlib-only server (http.server); computations run on worker threads with
live progress; results render as tables (matrix, grading, eigenvalues at
y = 1).  Binds to 127.0.0.1 only.
"""

import argparse
import ast
import json
import threading
import time
import traceback
import uuid
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PRESETS = [
    # label, algebra, keep, K, action, beta, classes, eval_y, expected
    ('(a) Fl(1,2,3)', 'A2', '1,2', '', 'info', '', '', '', 'full flag variety'),
    ('(b) P2xP2 / O(1,1)', 'A2xA2', '1,3', '1,1', 'info', '', '', '', 'dimension 3'),
    ('(c) quartic threefold', 'A4', '1', '4', 'gw', '1', '', '', '2875-style setup'),
    ('(d) Gr(2,4)', 'A3', '2', '', 'gw', '1', '2 1 3 2|1 2|3 2', '', 'invariant 1'),
    ('(e) cubic surface', 'A3', '1', '3', 'gw', '1', '', '', '27'),
    ('(f) quintic threefold', 'A4', '1', '5', 'gw', '1', '', '', '2875'),
    ('(g) quotient bundle on Gr(2,5)', 'A4', '2', 'taut_quot(X, 2)', 'info', '', '', '', 'dimension 3'),
    ('(h) P3xP3 / O(1,1)+O(2,2) [slow]', 'A3xA3', '1,4', '1,1;2,2', 'info', '', '', '', 'dimension 4'),
    ('(i) quantum matrix for P2', 'A2', '1', '', 'sqm', '', '', '', '3x3 matrix'),
]


JOBS = {}
JOBS_LOCK = threading.Lock()


# ------------------------------------------------------------- computations
def _int_vector(raw, label, *, expected=None, nonnegative=True):
    """Parse a comma-separated integer vector for the web form."""
    text = str(raw or '').strip()
    if not text:
        raise ValueError(f'{label} is required; enter comma-separated integers')
    parts = [part.strip() for part in text.split(',')]
    if any(not part for part in parts):
        raise ValueError(f'{label} must be comma-separated integers (for example 1,0,0)')
    try:
        values = [int(part) for part in parts]
    except ValueError as exc:
        raise ValueError(f'{label} must contain integers only (for example 1,0,0)') from exc
    if nonnegative and any(value < 0 for value in values):
        raise ValueError(f'{label} must contain nonnegative integers')
    if expected is not None and len(values) != expected:
        raise ValueError(f'{label} needs exactly {expected} entries for this algebra; got {len(values)}')
    return values


def parse_k(spec, X=None):
    spec = str(spec or '').strip()
    if not spec:
        return []
    if any(c.isalpha() for c in spec):
        from gwflags.bundles import O, taut_sub, taut_quot, dual, osum, tensor, sym, wedge, quot, Quot

        # Compact bundle aliases omit the ambient variety.  The Python API
        # keeps the explicit X argument, so the interface binds aliases to
        # the current FlagVariety while retaining explicit constructors.
        def compact_O(*args, **kwargs):
            if args and args[0] is X:
                return O(*args, **kwargs)
            return O(X, *args, **kwargs)

        def compact_S(*args, **kwargs):
            if args and args[0] is X:
                args = args[1:]
            return taut_sub(X, *args, **kwargs)

        def compact_Q(*args, **kwargs):
            if args and args[0] is X:
                args = args[1:]
            return taut_quot(X, *args, **kwargs)

        try:
            tree = ast.parse(spec, mode='eval')
            allowed = {"X": X, "O": compact_O, "S": compact_S, "Q": compact_Q,
                       "taut_sub": taut_sub, "taut_quot": taut_quot,
                       "dual": dual, "osum": osum, "tensor": tensor,
                       "sym": sym, "wedge": wedge, "quot": quot, "Quot": Quot}
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
    try:
        rows = []
        for raw_row in spec.split(';'):
            if not raw_row.strip():
                raise ValueError('empty bundle row')
            values = _int_vector(raw_row, 'Bundle K')
            rows.append(values)
        return rows
    except ValueError as e:
        raise ValueError(f'Invalid Bundle K: {e}. Use 3 or 1,1;2,2.') from e


def parse_classes(spec, X):
    out, names = [], []
    if not spec.strip():
        return out, names
    tokens = spec.split('|') if '|' in spec else spec.split(',')
    for token in tokens:
        token = token.strip()
        if token in ('pt', 'point'):
            out.append(X.pt)
            names.append('pt')
        elif token in ('id', 'e', ''):
            out.append(X.wd.group[0])
            names.append('id')
        else:
            try:
                pieces = token.replace(',', ' ').split()
                if not pieces:
                    raise ValueError('empty reduced word')
                word = tuple(int(c) for c in pieces)
            except ValueError as e:
                raise ValueError(
                    f'Insertion {token!r} is not a valid reduced word; '
                    'use spaces, for example 2 1 3 2') from e
            try:
                representative = X.wd.project(X.class_of_word(word))
                if len(word) != X.wd.length(representative):
                    raise ValueError(
                        'word must be reduced and minimal for the parabolic; '
                        'copy a word from Space Info')
                out.append(representative)
            except Exception as e:
                raise ValueError(
                    f'Insertion {token!r} is not valid for this variety: {e}') from e
            names.append('s' + ''.join(map(str, word)))
    return out, names


def spectrum_at_one(M):
    from .quantum import spectrum_at_one as _s
    return _s(M)


def run_job(job, kind, params):
    from gwflags import FlagVariety

    def log(msg):
        job['log'].append(str(msg))

    try:
        t0 = time.time()
        algebra = params['algebra'].strip()
        try:
            keep = _int_vector(params.get('keep', ''), 'Kept simple roots')
        except ValueError as e:
            raise ValueError(f'Cannot describe the variety: {e}') from e
        try:
            X = FlagVariety(algebra, keep)
        except ValueError as e:
            raise ValueError(f'Cannot describe the variety: {e}') from e
        try:
            K = X._check_K(parse_k(params.get('K', ''), X))
        except ValueError as e:
            raise ValueError(f'Cannot use Bundle K: {e}') from e
        log(f'{algebra}, kept roots {keep}'
            + (f', bundle {K}' if K else '')
            + f': |W| = {len(X.wd.group)}, {len(X.classes)} Schubert classes,'
              f' ambient dim {X.dimension}')
        result = {}

        if kind == 'info':
            from gwflags.quantum import chern_class_vector, chern_class_ci
            c = chern_class_ci(X, K) if K else chern_class_vector(X)
            fano, betas = X.fano_index_and_betas(K or None)
            result['basis'] = [
                {'index': i, 'word': ' '.join(map(str, w)) or 'e',
                 'degree': len(w)}
                for i, w in enumerate(X.class_words())]
            result['c1'] = c
            result['fano'] = fano
            result['n_betas'] = len(betas)
            result['dim'] = X.dimension - (K.rank if hasattr(K, 'rank') else len(K))

        elif kind == 'gw':
            if not str(params.get('beta', '')).strip():
                raise ValueError('Curve class beta is required; enter kept-root coordinates or a zero-padded ambient vector')
            beta_input = _int_vector(
                params['beta'], 'Curve class beta', expected=None)
            beta = X._check_beta(beta_input)
            classes, names = parse_classes(params.get('classes', ''), X)
            log(f'computing <{", ".join(names)}>_beta={list(beta)} ...')
            try:
                val = X.gw(classes, beta, K or None, progress=log)
            except ValueError as e:
                raise ValueError(
                    f'Cannot compute this invariant: {e}. Check beta length, '
                    'insertion degrees, and bundle convexity.') from e
            result['value'] = str(val)
            result['insertions'] = names
            result['beta_input'] = beta_input
            result['beta'] = list(beta)

        elif kind == 'sqm':
            import sympy
            workers = int(params.get('workers') or 0)
            fano, betas = X.fano_index_and_betas(K or None)
            log(f'Fano index {fano}; {len(betas)} curve classes '
                f'(max degree {max(sum(b) for b in betas)})')
            M, Gr, idx = X.small_quantum_multiplication(
                K or None, betas, progress=log, workers=workers)
            
            eval_y = params.get('eval_y', '').strip()
            eval_dict = {}
            if eval_y:
                for pair in eval_y.split(','):
                    if '=' not in pair or pair.count('=') != 1:
                        raise ValueError('Evaluate y must contain assignments such as y1=2,y2=-1')
                    k, v = pair.split('=', 1)
                    k = k.strip()
                    if not k.startswith('y') or not k[1:].isdigit():
                        raise ValueError(f'invalid Novikov variable {k!r}')
                    if not v.strip():
                        raise ValueError(f'Novikov assignment {k}= is missing a value')
                    try:
                        eval_dict[sympy.Symbol(k)] = sympy.sympify(v.strip())
                    except Exception as e:
                        raise ValueError(f'Novikov value {v.strip()!r} is not a valid number or expression') from e
                symbols = set().union(*(sympy.sympify(v).free_symbols for row in M for v in row))
                unknown = set(eval_dict) - symbols
                if unknown:
                    raise ValueError(f'unknown Novikov variable(s): {", ".join(map(str, unknown))}')
            
            if eval_dict:
                log(f'matrix assembled in {time.time() - t0:.1f}s; evaluating at {eval_y} ...')
                M = [[sympy.sympify(val).subs(eval_dict) if hasattr(val, 'free_symbols') or isinstance(val, str) else val for val in row] for row in M]
            else:
                log(f'matrix assembled in {time.time() - t0:.1f}s; keeping symbolic variables ...')
            
            # Compute Characteristic Polynomial
            log('computing characteristic polynomial ...')
            lam = sympy.Symbol('lambda')
            sympy_M = sympy.Matrix(M)
            char_poly = sympy_M.charpoly(lam).as_expr()
            
            result['fano'] = fano
            result['n_betas'] = len(betas)
            result['basis_indices'] = idx
            result['matrix'] = [[str(v) for v in row] for row in M]
            result['grading'] = [str(Gr[a][a]) for a in range(len(Gr))]
            result['char_poly'] = str(char_poly)
            
            # Only compute eigenvalues if not evaluated custom (to avoid complex root finding hangups)
            try:
                ev = spectrum_at_one(M) if not eval_dict else []
            except Exception as e:
                log(f"could not compute eigenvalues: {e}")
                ev = []
            result['eigenvalues'] = [[z.real, z.imag] for z in ev] if ev else []
        else:
            raise ValueError(f'unknown action {kind!r}')

        result['input'] = {'algebra': algebra, 'keep': keep, 'K': params.get('K', '').strip(), 'action': kind}
        result['seconds'] = round(time.time() - t0, 2)
        job['result'] = result
        job['state'] = 'done'
        log(f'done in {result["seconds"]}s')
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
            self._json([{'label': l, 'algebra': a, 'keep': k, 'K': kk, 'action': action,
                         'beta': beta, 'classes': classes, 'eval_y': eval_y,
                         'expected': expected}
                        for l, a, k, kk, action, beta, classes, eval_y, expected in PRESETS])
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
        job = {'state': 'running', 'log': [], 'result': None}
        with JOBS_LOCK:
            JOBS[jid] = job
        threading.Thread(target=run_job, args=(job, kind, params),
                         daemon=True).start()
        self._json({'id': jid})


PAGE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>gwflags — quantum multiplication lab</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&family=Inter:wght@400;500;600;700&display=swap');
:root { 
  --bg: #09090b; 
  --panel: #18181b; 
  --edge: #27272a; 
  --fg: #fafafa;
  --dim: #a1a1aa; 
  --acc: #3b82f6; 
  --acc-hover: #2563eb;
  --ok: #34d399; 
  --err: #f87171; 
  --radius: 8px;
}
* { box-sizing:border-box; margin: 0; padding: 0; }
body { 
  background:var(--bg); color:var(--fg);
  font-family: 'Inter', -apple-system, sans-serif;
  font-size: 14.5px; line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}
header { 
  padding: 16px 28px; 
  background: var(--panel);
  border-bottom: 1px solid var(--edge);
  display: flex; align-items: baseline; gap: 16px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
header h1 { font-size: 20px; font-weight: 700; color: #fff; letter-spacing: -0.5px; }
header span { color: var(--dim); font-size: 13.5px; font-weight: 400; }
main { 
  display: grid; grid-template-columns: 360px 1fr; gap: 0;
  min-height: calc(100vh - 61px); 
}
#controls { 
  padding: 24px 28px; 
  border-right: 1px solid var(--edge); 
  background: rgba(24, 24, 27, 0.4);
}
#results  { padding: 24px 32px; overflow-x: auto; }
label { 
  display: block; margin: 16px 0 6px; 
  color: var(--dim); font-size: 12px; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.05em; 
}
input, select { 
  width: 100%; padding: 10px 12px; border-radius: var(--radius);
  border: 1px solid var(--edge); background: var(--panel); color: var(--fg);
  font-family: 'Fira Code', monospace; font-size: 13px;
  transition: all 0.2s; outline: none;
}
input:focus, select:focus { border-color: var(--acc); box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2); }
.row { display: flex; gap: 12px; }
.row > div { flex: 1; }
button { 
  margin-top: 20px; margin-right: 10px; padding: 10px 20px;
  border-radius: var(--radius); border: none; background: var(--acc);
  color: #fff; font-weight: 600; font-size: 13.5px; cursor: pointer;
  transition: all 0.2s; outline: none; box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}
button:hover { background: var(--acc-hover); transform: translateY(-1px); }
button.secondary { background: var(--panel); border: 1px solid var(--edge); color: var(--fg); box-shadow: none; }
button.secondary:hover { background: #27272a; }
button:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
#gwbox { margin-top: 0; padding-top: 20px; }
#log { 
  margin-top: 24px; padding: 12px 16px; background: #000;
  border: 1px solid var(--edge); border-radius: var(--radius); max-height: 250px;
  overflow-y: auto; font-family: 'Fira Code', monospace; font-size: 12px;
  color: var(--ok); white-space: pre-wrap; box-shadow: inset 0 2px 6px rgba(0,0,0,0.3);
}
h2 { 
  font-size: 18px; font-weight: 600; margin: 24px 0 12px; color: #fff;
  letter-spacing: -0.3px; 
}
table { 
  border-collapse: collapse; margin: 12px 0 24px; 
  background: var(--panel); border-radius: var(--radius); overflow: hidden;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
td, th { 
  border: 1px solid var(--edge); padding: 10px 14px;
  font-family: 'Fira Code', monospace; font-size: 13px; text-align: center; 
}
th { color: var(--dim); font-weight: 600; background: rgba(255,255,255,0.02); }
tr:hover td { background: rgba(255,255,255,0.02); }
.badge { 
  display: inline-block; margin: 4px 12px 4px 0; padding: 4px 12px;
  border-radius: 20px; background: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.3);
  color: var(--acc); font-size: 12.5px; font-weight: 500;
}
.dom { color: var(--ok); font-weight: 700; background: rgba(52, 211, 153, 0.1) !important; }
.err { color: var(--err); }
sup { font-size: 10px; font-weight: 600; }
.help { color:var(--dim); font-size:12px; margin-top:4px; }
fieldset { border:1px solid var(--edge); border-radius:var(--radius); padding:10px 12px; margin-top:14px; }
legend { color:var(--dim); font-size:12px; padding:0 5px; }
.invalid { border-color:var(--err) !important; }
#status { min-height:1.5em; color:var(--dim); }
.result-tools {
  display:flex; align-items:center; flex-wrap:wrap; gap:8px;
  margin:0 0 12px;
}
.result-tools button { margin:0; }
#copy-status { color:var(--dim); font-size:12px; }
@media (max-width: 850px) { main { display:block; } #controls { border-right:0; border-bottom:1px solid var(--edge); } #results { padding:20px; } }
</style></head><body>
<header><h1>gwflags</h1>
<span>Gromov&ndash;Witten invariants &amp; quantum multiplication for flag
varieties — G/P and complete intersections</span></header>
<main>
<div id="controls">
  <div class="control-card">
    <div class="card-header">1. Space Definition</div>
    <label>Preset Library</label>
    <select id="preset"><option value="">— choose a pre-configured example —</option></select>
    <label for="algebra">Lie algebra</label>
    <input id="algebra" value="A2" aria-describedby="algebra-help" placeholder="A3 or A3xA3">
    <div id="algebra-help" class="help">Use A, B, C, D, G2, or products such as A3xA3.</div>
    <div class="row">
      <div>
        <label for="keep">Kept simple roots</label>
        <input id="keep" value="1" aria-describedby="keep-help" placeholder="1 or 1,2">
        <div id="keep-help" class="help">Comma-separated Bourbaki node numbers; order matters.</div>
      </div>
      <div>
        <label for="K">Bundle K (optional)</label>
        <input id="K" aria-describedby="K-help" placeholder="3 or 1,1;2,2">
        <div id="K-help" class="help">Use 3 or O(3) for a one-generator line bundle. Use O(a,b,...) when several kept roots are present; S(node) and Q(node) name tautological bundles at a kept type-A node. Use quot(E,F) (or Quot(E,F)) to form a quotient after the parser verifies F is a subbundle of E. Use semicolons between summands and commas between degree entries; Python [[3]] syntax is not accepted here.</div>
      </div>
    </div>
  </div>

  <div class="control-card">
    <div class="card-header">2. Execution Options</div>
    <div class="row">
      <div>
        <label for="eval_y">Evaluate y (optional)</label>
        <input id="eval_y" aria-describedby="eval-help" placeholder="y1=1">
        <div id="eval-help" class="help">Leave blank for symbolic variables. Use y&lt;ambient node&gt; labels, for example y1=1,y3=1 when kept roots are 1,3.</div>
      </div>
      <div>
        <label for="workers">Parallel workers</label>
        <input id="workers" value="8" aria-describedby="workers-help">
        <div id="workers-help" class="help">Use 0 for automatic; 4–8 is a good default.</div>
      </div>
    </div>
    <button id="bsqm" class="primary-btn">Compute quantum matrix</button>
    <button id="binfo" class="secondary">Describe this space</button>
  </div>

  <div class="control-card" id="gwbox">
    <div class="card-header">3. GW Invariants (Advanced)</div>
    <label for="beta">Curve class &beta;</label>
    <input id="beta" aria-describedby="beta-help" placeholder="one integer per root, e.g. 1,0,0">
    <div id="beta-help" class="help">Enter beta in kept-root order, or use a zero-padded ambient vector; removed-root entries must be zero.</div>
    <label for="classes">Insertions (separated by |)</label>
    <input id="classes" aria-describedby="classes-help" placeholder="pt | id | 2 1 3 2">
    <div id="classes-help" class="help">Use pt, id, or a space-separated reduced word copied from Space Info.</div>
    <button id="bgw" class="secondary" style="width:100%; margin-top:12px;">Compute one GW invariant</button>
  </div>
  
  <div id="status" aria-live="polite">Ready. Choose an example or enter a variety.</div><div id="log" aria-live="polite">System ready. Waiting for input...</div>
</div>
<div id="results"><div class="result-tools" role="toolbar" aria-label="Result tools">
<button id="copy-input" class="secondary" type="button">Copy input JSON</button>
<button id="download-output" class="secondary" type="button" disabled>Download result JSON</button>
<span id="copy-status" aria-live="polite"></span>
</div><h2>Results</h2>
<div id="out" style="color:var(--dim)">Pick a preset (or describe a flag
variety) and press <b>c&#8321;(TX)&#8902; matrix</b>.  Heavy examples —
index-1 Fano with degree-4/5 curves — can take minutes; progress streams in
the log.</div></div>
</main>
<script>
const $ = id => document.getElementById(id);
const pretty = s => s.replace(/\*\*(\d+)/g,'<sup>$1</sup>')
                     .replace(/\*/g,'&middot;');
fetch('/api/presets').then(r=>r.json()).then(ps=>{
  ps.forEach((p,i)=>{ const o=document.createElement('option');
    o.value=i; o.textContent=p.label; $('preset').appendChild(o); });
  window._presets=ps; });
$('preset').onchange = ()=>{ const p=window._presets[$('preset').value];
  if(p){ $('algebra').value=p.algebra; $('keep').value=p.keep; $('K').value=p.K;
    $('beta').value=p.beta||''; $('classes').value=p.classes||''; $('eval_y').value=p.eval_y||'';
    $('status').textContent='Loaded '+p.label+'. Recommended action: '+p.action+'. Expected: '+p.expected+'.';
    window._recommended=p.action; } };
function validate(action){
  let ok=true; ['algebra','keep','K','beta','classes','eval_y'].forEach(id=>$(id).classList.remove('invalid'));
  if(!/^[A-Za-z0-9]+(?:x[A-Za-z0-9]+)*$/.test($('algebra').value.trim())) { $('algebra').classList.add('invalid'); ok=false; }
  if(!/^\d+(?:,\d+)*$/.test($('keep').value.trim())) { $('keep').classList.add('invalid'); ok=false; }
  if(action==='gw' && $('beta').value.trim() && !/^\d+(?:,\d+)*$/.test($('beta').value.trim())) { $('beta').classList.add('invalid'); ok=false; }
  if(!ok) $('status').textContent='Please correct the highlighted fields.';
  return ok;
}
let timer=null;
let lastRequest=null;
let lastResult=null;
function inputSnapshot(action){
  const chosen = action || (lastRequest && lastRequest.action) ||
    window._recommended || 'info';
  return {action:chosen, algebra: $('algebra').value.trim(),
    keep: $('keep').value.trim(), K: $('K').value.trim(),
    beta: $('beta').value.trim(), classes: $('classes').value.trim(),
    eval_y: $('eval_y').value.trim(), workers: $('workers').value.trim()};
}
async function copyText(value){
  if(navigator.clipboard && navigator.clipboard.writeText){
    try { await navigator.clipboard.writeText(value); return; } catch (_) {}
  }
  const area=document.createElement('textarea'); area.value=value;
  area.setAttribute('readonly',''); area.style.position='fixed';
  area.style.opacity='0'; document.body.appendChild(area); area.select();
  const copied=document.execCommand('copy'); area.remove();
  if(!copied) throw new Error('clipboard access was denied');
}
function toolMessage(message, error=false){
  $('copy-status').textContent=message;
  $('copy-status').style.color=error?'var(--err)':'var(--dim)';
}
$('copy-input').onclick=async()=>{
  try {
    await copyText(JSON.stringify(inputSnapshot(), null, 2)+'\n');
    toolMessage('Input copied.');
  } catch(e) { toolMessage('Could not copy input: '+e.message, true); }
};
$('download-output').onclick=()=>{
  if(!lastResult || !lastRequest) return;
  const payload=JSON.stringify({input:lastRequest, result:lastResult}, null, 2)+'\n';
  const blob=new Blob([payload], {type:'application/json'});
  const url=URL.createObjectURL(blob); const link=document.createElement('a');
  const action=(lastRequest.action||'result').toLowerCase();
  link.href=url; link.download='gwflags-'+action+'-result.json';
  document.body.appendChild(link); link.click(); link.remove();
  setTimeout(()=>URL.revokeObjectURL(url), 0);
  toolMessage('Result downloaded.');
};
function run(action){
  if(!validate(action)) return;
  const params={action, algebra:$('algebra').value, keep:$('keep').value,
    K:$('K').value, eval_y:$('eval_y').value, workers:$('workers').value,
    beta:$('beta').value, classes:$('classes').value};
  lastRequest=params; lastResult=null; $('download-output').disabled=true;
  toolMessage('');
  ['bsqm','binfo','bgw'].forEach(b=>$(b).disabled=true);
  $('log').textContent='starting...'; $('status').textContent='Computing '+action+'…';
  const fail = msg => { clearInterval(timer);
    ['bsqm','binfo','bgw'].forEach(b=>$(b).disabled=false);
    $('out').innerHTML='<span class="err">'+msg+'</span>'; };
  fetch('/api/run',{method:'POST',body:JSON.stringify(params)})
    .then(r=>r.json()).then(({id,error})=>{
      if(error){ fail(error); return; }
      timer=setInterval(()=>fetch('/api/status?id='+id)
        .then(r=>r.json()).then(st=>{
          $('log').textContent=st.log.join('\n');
          $('log').scrollTop=$('log').scrollHeight;
          if(st.state!=='running'){ clearInterval(timer);
            ['bsqm','binfo','bgw'].forEach(b=>$(b).disabled=false);
            if(st.state==='error')
              $('out').innerHTML='<span class="err">'+st.error+'</span>';
            else { lastResult=st.result; $('download-output').disabled=false;
              render(action, st.result); } }
        }).catch(()=>{}),700); })
    .catch(e=>fail('request failed: '+e));
}
function render(action,res){
  let h='';
  if(res.input) h+='<div class="help">Input used: '+res.input.algebra+'; kept roots '+res.input.keep.join(',')+'; K='+((res.input.K||'empty'))+'</div>';
  if(action==='info'){
    h+='<span class="badge">dim '+res.dim+'</span>'+
       '<span class="badge">Fano index '+res.fano+'</span>'+
       '<span class="badge">c&#8321; = ['+res.c1+']</span>'+
       '<span class="badge">'+res.n_betas+' curve classes</span>';
    h+='<h2>Schubert basis</h2><table><tr><th>&sigma;</th><th>word</th>'+
       '<th>degree</th><th>use</th></tr>';
    res.basis.forEach(b=>h+='<tr><td>&sigma;<sub>'+b.index+'</sub></td><td>'+
       b.word+'</td><td>'+b.degree+'</td><td><button class=\"secondary\" style=\"margin:0;padding:4px 8px\" data-word=\"'+b.word+'\" onclick=\"addInsertion(this.dataset.word)\">Add</button></td></tr>');
    h+='</table>';
  } else if(action==='gw'){
    const entered = res.beta_input ? ('['+res.beta_input+'] &rarr; ') : '';
    h+='<h2>&lang;'+res.insertions.join(', ')+'&rang;<sub>&beta;='+entered+
       '['+res.beta+']</sub> = <b style="font-size:20px">'+res.value+'</b></h2>';
  } else {
    h+='<span class="badge">Fano index '+res.fano+'</span>'+
       '<span class="badge">'+res.n_betas+' curve classes</span>'+
       '<span class="badge">'+res.seconds+'s</span>';
    h+='<h2>c&#8321;(TX)&#8902;</h2><table>';
    res.matrix.forEach(row=>{ h+='<tr>';
      row.forEach(v=>h+='<td>'+pretty(v)+'</td>'); h+='</tr>'; });
    h+='</table>';
    h+='<h2>Grading</h2><div>diag('+res.grading.join(', ')+')</div>';
    if (res.char_poly) {
        h+='<h2>Characteristic Polynomial</h2><div style="padding: 10px; background: var(--panel); border: 1px solid var(--edge); font:13px ui-monospace,Menlo,monospace;">'+pretty(res.char_poly)+'</div>';
    }
    if (res.eigenvalues && res.eigenvalues.length > 0) {
        h+='<h2>Eigenvalues at y = 1</h2><table><tr>';
        res.eigenvalues.forEach(([re,im],i)=>{
          const fmt=x=>{ let t=x.toFixed(4).replace(/\.?0+$/,'');
            return (t===''||t==='-0')?'0':t; };
          const s=fmt(re)+(Math.abs(im)>1e-6?((im>0?' + ':' − ')+
            fmt(Math.abs(im))+'i'):'');
          h+='<td>'+s+'</td>'; });
        h+='</tr></table><div style="color:var(--dim);font-size:12px">Numerical spectrum after setting all Novikov variables to 1.</div>';
    }
  }
  $('out').innerHTML=h;
}
function addInsertion(word){ const f=$('classes'); if(word==='e') word='id'; f.value=f.value?f.value+'|'+word:word; $('status').textContent='Added '+word+' to insertions.'; }
$('bsqm').onclick=()=>run('sqm');
$('binfo').onclick=()=>run('info');
$('bgw').onclick=()=>run('gw');
</script></body></html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--port', type=int, default=8642)
    ap.add_argument('--no-browser', action='store_true')
    args = ap.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    url = f'http://127.0.0.1:{args.port}'
    print(f'gwflags GUI serving at {url}  (Ctrl-C to stop)')
    if not args.no_browser:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nbye')


if __name__ == '__main__':
    main()
