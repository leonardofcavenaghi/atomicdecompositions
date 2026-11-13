"""Local application router; each geometry retains its own interface and engine."""
import argparse
from http.server import ThreadingHTTPServer
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import threading
import uuid
import webbrowser

from gwflags import gui as flag
from gwtoric import gui as toric

ROOT=Path(__file__).resolve().parent.parent
DATA=ROOT/'workspace'
JOBS={}
LOCK=threading.Lock()

HOME='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>GW · Choose your geometry</title><style>
body{margin:0;background:#0b1220;color:#e6edf7;font:18px system-ui;min-height:100vh;display:grid;place-items:center}
main{max-width:900px;padding:36px}h1{font-size:48px;margin:12px 0}p{color:#adbbd1;line-height:1.6}
nav{display:flex;gap:24px;margin-top:40px}a{flex:1;border:1px solid #405575;padding:32px;border-radius:16px;text-decoration:none;color:inherit;background:#152239}a:hover{border-color:#7cbdff;background:#1b304d}h2{margin-top:0;font-size:26px}small{color:#9aacc8} @media(max-width:600px){nav{flex-direction:column}h1{font-size:36px}}
</style><main><small>GROMOV–WITTEN COMPUTATIONS</small><h1>Choose your geometry</h1>
<p>Exact invariants, quantum multiplication, and complete intersections.<br>Choose the workspace for your variety.</p>
<nav><a href="/flag/"><h2>Flag varieties →</h2><p>Root systems, parabolics, and homogeneous bundles.</p></a>
<a href="/toric/"><h2>Toric varieties →</h2><p>Fans, toric divisors, and projective bundles.</p></a></nav>
<p><small>Local development build · 1.1.0.dev1</small></p></main></html>'''


def flag_page():
    page=flag.PAGE
    controls='''<div class="control-card"><div class="card-header">Additional computations</div>
<button id="bhodge" type="button">Hodge diamond</button>
<button id="banalysis" type="button">Update spectrum &amp; exponents</button>
<button id="bstop" type="button">Stop calculation</button>
<label for="evaluations">Exact evaluations per curve class</label><select id="evaluations"><option value="2">Two (cross-check)</option><option value="1">One</option></select>
<p class="help">Unmarked decorations and exact marking sums are saved automatically. Repeat the same inputs to resume. Hodge diamonds require ample line-bundle summands and assume a smooth regular section.</p></div>'''
    page=page.replace('<div id="controls">','<div id="controls">'+controls)
    page=page.replace("['bsqm','binfo','bgw']","['bsqm','binfo','bgw','bhodge','banalysis']")
    page=page.replace('let timer=null;', 'let timer=null; let currentJob=null;')
    page=page.replace('const params={action,',"const params={evaluations:$('evaluations').value, action,")
    page=page.replace('return {action:chosen,',"return {evaluations:$('evaluations').value, action:chosen,")
    page=page.replace('if(error){ fail(error); return; }','if(error){ fail(error); return; } currentJob=id;')
    page=page.replace("if(st.state==='error')","if(st.state==='error' || st.state==='cancelled')")
    page=page.replace("if(res.input) h+=", "if(res.input && Array.isArray(res.input.keep)) h+=")
    extension=(Path(__file__).with_name('flag_extensions.js')).read_text(encoding='utf-8')
    page=page.replace('</script></body>',extension+'\n</script></body>')
    return page


def stop(job):
    process=job['process']
    if process.poll() is None:
        if os.name=='nt':
            subprocess.run(['taskkill','/PID',str(process.pid),'/T','/F'],capture_output=True,
                           creationflags=subprocess.CREATE_NO_WINDOW)
        else:
            os.killpg(process.pid,signal.SIGTERM)
        process.wait(timeout=15)
    job['cancelled']=True


class Handler(flag.Handler):
    def _page(self,page):
        data=page.encode('utf-8');self.send_response(200)
        self.send_header('Content-Type','text/html; charset=utf-8')
        self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)

    def do_GET(self):
        if self.path=='/':
            return self._page(HOME)
        for prefix,module in (('/flag',flag),('/toric',toric)):
            if self.path in (prefix,prefix+'/'):
                page=flag_page() if module is flag else module.PAGE
                page=page.replace('/api/',prefix+'/api/')
                page=page.replace('<header>','<header><a href="/" style="color:inherit;margin-right:20px">← Choose geometry</a>')
                return self._page(page)
        if self.path.startswith('/toric/api/'):
            self.path=self.path[len('/toric'):]
            return toric.Handler.do_GET(self)
        if self.path=='/flag/api/presets':
            self.path='/api/presets';return flag.Handler.do_GET(self)
        if self.path.startswith(('/flag/api/status?id=','/flag/api/stop?id=')):
            jid=self.path.split('id=')[-1]
            with LOCK:
                job=JOBS.get(jid)
            if not job:
                return self._json(dict(error='No such job'),404)
            if '/stop?' in self.path:
                stop(job)
            request=job['path'];resultpath=request.with_suffix('.result.json')
            logs=request.with_suffix('.log')
            state=json.loads(resultpath.read_text()) if resultpath.exists() else dict(state='running')
            if resultpath.exists() and job['process'].poll() is None:
                job['process'].wait(timeout=15)
            if job.get('cancelled'):
                state=dict(state='cancelled',error='Stopped. Repeat the same inputs to resume saved tree work.')
            elif job['process'].poll() is not None and not resultpath.exists():
                state=dict(state='error',error='Worker exited unexpectedly; saved checkpoints are retained')
            state['log']=logs.read_text(encoding='utf-8').splitlines()[-500:] if logs.exists() else []
            return self._json(state)
        return self._json(dict(error='Not found'),404)

    def do_POST(self):
        if self.path=='/toric/api/run':
            self.path='/api/run';return toric.Handler.do_POST(self)
        if self.path!='/flag/api/run':
            return self._json(dict(error='Not found'),404)
        try:
            params=json.loads(self.rfile.read(int(self.headers.get('Content-Length',0))))
            if not isinstance(params,dict):
                raise ValueError('Expected an input object')
            with LOCK:
                if any(j['process'].poll() is None for j in JOBS.values()):
                    return self._json(dict(error='A flag computation is running. Stop it or wait for completion.'),409)
                folder=DATA/'jobs';folder.mkdir(parents=True,exist_ok=True)
                jid=uuid.uuid4().hex;path=folder/(jid+'.json')
                path.write_text(json.dumps(params),encoding='utf-8')
                kwargs={'creationflags':subprocess.CREATE_NO_WINDOW} if os.name=='nt' else {'start_new_session':True}
                process=subprocess.Popen([sys.executable,'-m','gwapp.worker',str(path)],cwd=ROOT,
                                         stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,**kwargs)
                JOBS[jid]=dict(path=path,process=process)
            self._json(dict(id=jid))
        except Exception as exc:
            self._json(dict(error=str(exc)),400)


def main():
    global DATA
    parser=argparse.ArgumentParser(description='Flag and toric computation workspaces')
    parser.add_argument('--port',type=int,default=8650)
    parser.add_argument('--no-browser',action='store_true')
    parser.add_argument('--workspace',type=Path,default=DATA)
    args=parser.parse_args()
    DATA=args.workspace.resolve()
    server=ThreadingHTTPServer(('127.0.0.1',args.port),Handler)
    url=f'http://127.0.0.1:{args.port}/';print(url,flush=True)
    if not args.no_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        for job in JOBS.values():
            if job['process'].poll() is None:
                stop(job)
        server.server_close()

