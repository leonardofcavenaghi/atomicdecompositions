"""Install the published archives independently and check their real launchers.

Run on a machine with pip, venv, network access and local sockets available.
No source-tree imports or pre-existing package installation are used.
"""
from pathlib import Path
import hashlib,json,os,socket,subprocess,sys,tempfile,time,urllib.request,zipfile
ROOT=Path(__file__).resolve().parents[1]

def run(args,cwd):
 subprocess.run(args,cwd=cwd,check=True,timeout=240)

def server(python,module,cwd):
 with socket.socket() as sock:
  sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
 args=[str(python),'-m',module,'--no-browser','--port',str(port)]
 if module=='gwapp':args+=['--workspace',str(cwd/'workspace')]
 log=cwd/(module+'.log')
 with log.open('w') as out:
  process=subprocess.Popen(args,cwd=cwd,stdout=out,stderr=out)
  try:
   deadline=time.monotonic()+45
   while True:
    if process.poll() is not None:raise AssertionError(log.read_text())
    try:
     with urllib.request.urlopen(f'http://127.0.0.1:{port}/',timeout=2) as response:
      assert response.status==200
      assert '<html' in response.read().decode().lower()
     break
    except (OSError,TimeoutError):
     if time.monotonic()>deadline:raise AssertionError(log.read_text())
     time.sleep(0.2)
   if module=='gwapp':
    for path in ['flag/','toric/']:
     with urllib.request.urlopen(f'http://127.0.0.1:{port}/{path}',timeout=10) as response:
      assert response.status==200 and '<html' in response.read().decode().lower()
  finally:
   process.terminate()
   try:process.wait(timeout=10)
   except subprocess.TimeoutExpired:process.kill();process.wait()

manifest=json.loads((ROOT/'docs/downloads/manifest.json').read_text())
for item in manifest:
 archive=ROOT/'docs/downloads'/item['file']
 assert hashlib.sha256(archive.read_bytes()).hexdigest()==item['sha256']
 with tempfile.TemporaryDirectory(prefix='geoatoms-install-') as td:
  temporary=Path(td);extracted=temporary/'source';extracted.mkdir()
  with zipfile.ZipFile(archive) as z:
   assert z.testzip() is None
   for entry in z.namelist():
    assert not Path(entry).is_absolute() and '..' not in Path(entry).parts
   z.extractall(extracted)
  folders=list(extracted.iterdir());assert len(folders)==1
  source=folders[0]
  snapshot=source/'SOURCE-SNAPSHOT.json'
  if snapshot.exists():
   for path,sha in json.loads(snapshot.read_text())['files'].items():
    assert hashlib.sha256((source/path).read_bytes()).hexdigest()==sha,path
  env=temporary/'venv'
  run([sys.executable,'-m','venv',str(env)],temporary)
  python=env/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
  run([str(python),'-m','pip','install',str(source)],temporary)
  work=temporary/'outside-source';work.mkdir()
  code="from gwflags import FlagVariety; assert FlagVariety('A3',[1]).gw([], beta=(1,), K=[[3]])==27; print('unmarked flag cubic: 27')"
  run([str(python),'-c',code],work)
  run([str(python),'-m','gwflags.cli','--help'],work)
  server(python,'gwflags.gui',work)
  is_new='1.1.0.dev1' in item['file']
  if is_new:
   run([str(python),'-c',"from gwtoric import projective_space; assert projective_space(3).gw([], beta=(1,1,1,1), K=[[3]])==27; print('unmarked toric cubic: 27')"],work)
   run([str(python),'-m','gwtoric.cli','--help'],work)
   server(python,'gwtoric.gui',work)
  if item['file'].startswith('gw-combined'):
   run([str(python),'-c',"import importlib.resources as r; assert r.files('gwapp').joinpath('flag_extensions.js').is_file()"],work)
   server(python,'gwapp',work)
  print('Installed archive and launchers passed:',item['file'],flush=True)
print('All distribution installations passed')
