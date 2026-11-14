"""Validate catalogue links, scientific search keywords and the exact distributable sources.

This checks source artifacts; it does not replace a MkDocs/browser build or
an installed-package smoke test.
"""
from pathlib import Path
import hashlib,json,posixpath,re,urllib.parse,zipfile
ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'

def links(text):
 text=re.sub(r'```.*?```','',text,flags=re.S)
 return re.findall(r'\]\(([^)]+)\)',text)

pages=list(DOCS.rglob('*.md'))
for page in pages:
 text=page.read_text()
 text=re.sub(r'^---\n.*?\n---\n','',text,flags=re.S)
 text=re.sub(r'```.*?```','',text,flags=re.S)
 text=re.sub(r'\]\([^)]*\)',']',text)
 text=re.sub(r'<span[^>]*>','',text)
 assert not re.search(r'\b(?:QD5|QC5|PB5|PROD5|PCI5)-[A-Z0-9-]+\b|GM-20',text),(page,'synthetic public label')
 for phrase in ('saved computation records','newly published fan-based matrices','prepared source bundle','our internal conversations','Saved record:','This page transcribes','fan and divisor certificate','Workbook source ID','Flag mathematics','Toric mathematics'):
  assert phrase.casefold() not in text.casefold(),(page,'internal public copy',phrase)
 if page.is_relative_to(DOCS/'catalog'):
  for phrase in ('Complete exponent computation:', 'Status / method', 'Matrix complete', 'Ambient matrix incomplete', 'saved-exponent-summary:', '**Unresolved:**'):
   assert phrase.casefold() not in text.casefold(),(page,'workflow label in catalogue',phrase)
  assert not re.search(r'\b(?=[0-9a-f]{0,11}[a-f])[0-9a-f]{12}\b',text),(page,'visible machine identifier')

for page in pages:
 for target in links(page.read_text()):
  address=target.split('#')[0].split('?')[0]
  if not address or urllib.parse.urlsplit(address).scheme or address.startswith('/'):continue
  assert (page.parent/urllib.parse.unquote(address)).exists(),(page,target)

catalog=json.loads((DOCS/'data/catalog-records.json').read_text())['records']
original=json.loads((DOCS/'data/localization-results.json').read_text())['examples']
fresh=json.loads((DOCS/'data/flag-fourfolds.json').read_text())['records']
new=[r for name in ['fourfolds','fivefolds'] for r in json.loads((DOCS/'data'/('toric-'+name+'.json')).read_text())['records']]
assert len(catalog)==len(original)+len(new)+len(fresh) and len({r['id'] for r in catalog})==len(catalog)
sources={r['id']:r for r in original+new+fresh}
atomic={r['id']:r for r in json.loads((DOCS/'data/atomic-invariants.json').read_text())['records']}
assert set(sources)=={r['id'] for r in catalog}
master=(DOCS/'catalog/index.md').read_text()
qd5=next(r for r in catalog if r['id']=='QD5-001')
assert 'Quartic double cover' in qd5['title']
assert 'weighted hypersurface' in qd5['keywords']
for row in catalog:
 source=sources[row['id']]
 assert row['h11']==next((v['value'] for v in atomic[row['id']]['full_hodge_numbers'] if (v['p'],v['q'])==(1,1)),0),(row['id'],'summary Hodge number')
 assert row['dimension']==source['dimension'],row['id']
 assert f']({row["link"]})' in master,row['id']
 if row['link'].startswith('records/'):
  text=(DOCS/'catalog'/row['link']).read_text()
  assert '**Search aliases:**' not in text
  assert all(keyword in text for keyword in row['keywords']),(row['id'],'scientific keywords')
 if 'basis' in source:
  assert row['matrix_rank']==len(source['basis'])
 else:
  assert row['index']==source['fano_index']
  assert row['matrix_rank']==len(source['basis_indices'])

mirrors={'gw-combined-1.1.0.dev1.zip':'combined-1.1.0.dev1','gw-flag-1.1.0.dev1.zip':'flag-1.1.0.dev1','gw-toric-1.1.0.dev1.zip':'toric-1.1.0.dev1','gwflags-1.0.5-preserved.zip':'flag-1.0.5'}
archives=json.loads((DOCS/'downloads/manifest.json').read_text())
assert len(archives)==5
for item in archives:
 archive=DOCS/'downloads'/item['file']
 assert hashlib.sha256(archive.read_bytes()).hexdigest()==item['sha256']
 with zipfile.ZipFile(archive) as z:
  assert z.testzip() is None
  names=set(z.namelist());prefix=next(iter(names)).split('/')[0]+'/'
  for name in names:
   assert not Path(name).is_absolute() and '..' not in Path(name).parts
   data=z.read(name)
   if item['file'] in mirrors:
    assert (ROOT/'software'/mirrors[item['file']]/name[len(prefix):]).read_bytes()==data,(item['file'],name,'source mirror differs')
   if name.endswith('.md'):
    for target in links(data.decode()):
     address=target.split('#')[0]
     if not address or urllib.parse.urlsplit(address).scheme or address.startswith('/'):continue
     path=posixpath.normpath(posixpath.join(posixpath.dirname(name),address))
     assert path in names or any(n.startswith(path.rstrip('/')+'/') for n in names),(item['file'],name,target)
  snapshot=prefix+'SOURCE-SNAPSHOT.json'
  if snapshot in names:
   for path,digest in json.loads(z.read(snapshot))['files'].items():
    assert hashlib.sha256(z.read(prefix+path)).hexdigest()==digest,(item['file'],path)
  metadata=z.read(prefix+'pyproject.toml').decode()
  scripts=metadata.split('[project.scripts]')[1].split('\n[')[0]
  for module in re.findall(r'= "([a-zA-Z0-9_.]+):[a-zA-Z0-9_]+"',scripts):
   assert prefix+module.replace('.','/')+'.py' in names,(item['file'],module)
print(json.dumps(dict(markdown_pages=len(pages),catalogue_records=len(catalog),new_searchable_records=len(new)+len(fresh),archives=len(archives),source_mirrors=len(mirrors),passed=True)))
