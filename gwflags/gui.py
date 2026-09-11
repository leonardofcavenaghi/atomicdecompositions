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
import json
import threading
import time
import traceback
import uuid
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PRESETS = [
    # label, algebra, keep, K
    ('(a)  Fl(1,2,3)', 'A2', '1,2', ''),
    ('(b)  P2xP2 / O(1,1)', 'A2xA2', '1,3', '1,1'),
    ('(c)  P4 / O(4)  quartic 3-fold', 'A4', '1', '4'),
    ('(d1) P3xP3 / O(1,1)+O(1,1)', 'A3xA3', '1,4', '1,1;1,1'),
    ('(d2) Fl(1,3,4) / O(1,1)', 'A3', '1,3', '1,1'),
    ('(e)  SO(5)/B / O(1,1)', 'B2', '1,2', '1,1'),
    ('(f)  P3xP3 / O(1,1)^3', 'A3xA3', '1,4', '1,1;1,1;1,1'),
    ('(g)  Gr(2,5) / O(1)+O(1)+O(2)', 'A4', '2', '1;1;2'),
    ('(h)  P3xP3 / O(1,1)+O(2,2)  [slow]', 'A3xA3', '1,4', '1,1;2,2'),
    ('(i)  Fl(1,2,5) / O(0,1)+O(0,2)+O(1,0)  GM-20', 'A4', '1,2',
     '0,1;0,2;1,0'),
    ('(j)  P1xP5 / O(1,1)+O(0,3)', 'A1xA5', '1,2', '1,1;0,3'),
    ('(k)  P1xP1xP4 / O(1,1,1)+O(0,0,3)  [slow]', 'A1xA1xA4', '1,2,3',
     '1,1,1;0,0,3'),
    ('quadric 3-fold Q3 in P4', 'A4', '1', '2'),
    ('cubic 3-fold in P4', 'A4', '1', '3'),
    ('V8 = (2,2,2) in P6', 'A6', '1', '2;2;2'),
    ('Gr(2,4)', 'A3', '2', ''),
    ('Gr(2,5) / O(2)  Gushel-Mukai 5-fold', 'A4', '2', '2'),
    ('Fl(1,4,5) / O(1,1)+O(1,1)', 'A4', '1,4', '1,1;1,1'),
    ('G2/P1  quadric 5-fold', 'G2', '1', ''),
    ('G2/P2', 'G2', '2', ''),
    ('OG(3,7) / O(2)', 'B3', '3', '2'),
    ('LG(3,6) / O(1)', 'C3', '3', '1'),
]

JOBS = {}
JOBS_LOCK = threading.Lock()


# ------------------------------------------------------------- computations
def parse_k(spec, X=None):
    spec = spec.strip()
    if not spec:
        return []
    if any(c.isalpha() for c in spec):
        from gwflags.bundles import O, taut_sub, taut_quot, dual, osum, tensor, sym, wedge
        try:
            return eval(spec, {"X": X, "O": O, "taut_sub": taut_sub, "taut_quot": taut_quot, "dual": dual, "osum": osum, "tensor": tensor, "sym": sym, "wedge": wedge})
        except Exception as e:
            raise ValueError(f"Invalid bundle expression: {e}")
    return [[int(v) for v in row.split(',')] for row in spec.split(';')]


def parse_classes(spec, X):
    out, names = [], []
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
            word = tuple(int(c) for c in token.replace(',', ' ').split())
            out.append(X.schubert(word))
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
        keep = [int(v) for v in params['keep'].split(',') if v.strip()]
        X = FlagVariety(algebra, keep)
        K = X._check_K(parse_k(params.get('K', ''), X))
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
            result['dim'] = X.dimension - len(K)

        elif kind == 'gw':
            beta = tuple(int(v) for v in params['beta'].split(','))
            classes, names = parse_classes(params['classes'], X)
            log(f'computing <{", ".join(names)}>_beta={list(beta)} ...')
            val = X.gw(classes, beta, K or None, progress=log)
            result['value'] = str(val)
            result['insertions'] = names
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
                    if '=' in pair:
                        k, v = pair.split('=')
                        eval_dict[sympy.Symbol(k.strip())] = sympy.sympify(v.strip())
            
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
            self._json([{'label': l, 'algebra': a, 'keep': k, 'K': kk}
                        for l, a, k, kk in PRESETS])
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
#gwbox { 
  border-top: 1px solid var(--edge); margin-top: 24px; padding-top: 8px; 
}
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
</style></head><body>
<header><h1>gwflags</h1>
<span>Gromov&ndash;Witten invariants &amp; quantum multiplication for flag
varieties — G/P and complete intersections</span></header>
<main>
<div id="controls">
  <label>Preset</label>
  <select id="preset"><option value="">— choose an example —</option></select>
  <label>Algebra</label>
  <input id="algebra" value="A2" placeholder="A2, B3, A3xA3, G2 ...">
  <div class="row">
    <div><label>Kept simple roots</label>
      <input id="keep" value="1" placeholder="e.g. 1,2"></div>
    <div><label>Bundle K (rows ; entries ,)</label>
      <input id="K" placeholder="e.g. 1,1;2,2"></div>
  </div>
  <div class="row">
    <div><label>Evaluate y (e.g. y1=2)</label>
      <input id="eval_y" placeholder="y1=2, y2=-1"></div>
    <div><label>Workers</label>
      <input id="workers" value="8"></div><div></div>
  </div>
  <button id="bsqm">c&#8321;(TX)&#8902; matrix</button>
  <button id="binfo" class="secondary">Info</button>
  <div id="gwbox">
    <label>GW invariant — curve class &beta;</label>
    <input id="beta" placeholder="one integer per simple root, e.g. 1,0">
    <label>Insertions (words | pt | id, separated by |)</label>
    <input id="classes" placeholder="pt|pt   or   2|1 3 2|pt">
    <button id="bgw" class="secondary">Compute invariant</button>
  </div>
  <div id="log">ready.</div>
</div>
<div id="results"><h2>Results</h2>
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
  if(p){ $('algebra').value=p.algebra; $('keep').value=p.keep;
         $('K').value=p.K; } };
let timer=null;
function run(action){
  const params={action, algebra:$('algebra').value, keep:$('keep').value,
    K:$('K').value, eval_y:$('eval_y').value, workers:$('workers').value,
    beta:$('beta').value, classes:$('classes').value};
  ['bsqm','binfo','bgw'].forEach(b=>$(b).disabled=true);
  $('log').textContent='starting...';
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
            else render(action, st.result); }
        }).catch(()=>{}),700); })
    .catch(e=>fail('request failed: '+e));
}
function render(action,res){
  let h='';
  if(action==='info'){
    h+='<span class="badge">dim '+res.dim+'</span>'+
       '<span class="badge">Fano index '+res.fano+'</span>'+
       '<span class="badge">c&#8321; = ['+res.c1+']</span>'+
       '<span class="badge">'+res.n_betas+' curve classes</span>';
    h+='<h2>Schubert basis</h2><table><tr><th>&sigma;</th><th>word</th>'+
       '<th>degree</th></tr>';
    res.basis.forEach(b=>h+='<tr><td>&sigma;<sub>'+b.index+'</sub></td><td>'+
       b.word+'</td><td>'+b.degree+'</td></tr>');
    h+='</table>';
  } else if(action==='gw'){
    h+='<h2>&lang;'+res.insertions.join(', ')+'&rang;<sub>&beta;=['+
       res.beta+']</sub> = <b style="font-size:20px">'+res.value+'</b></h2>';
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
        h+='<h2>Eigenvalues</h2><table><tr>';
        res.eigenvalues.forEach(([re,im],i)=>{
          const fmt=x=>{ let t=x.toFixed(4).replace(/\.?0+$/,'');
            return (t===''||t==='-0')?'0':t; };
          const s=fmt(re)+(Math.abs(im)>1e-6?((im>0?' + ':' − ')+
            fmt(Math.abs(im))+'i'):'');
          h+='<td class="'+(i===0?'dom':'')+'">'+s+'</td>'; });
        h+='</tr></table><div style="color:var(--dim);font-size:12px">'+
           'first entry = spectral radius (Conjecture O: real &amp; simple).'+
           '</div>';
    }
  }
  $('out').innerHTML=h;
}
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
