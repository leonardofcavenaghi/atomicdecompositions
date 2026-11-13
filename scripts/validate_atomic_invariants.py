"""Check every published atomic certificate against exact matrices and Hodge data."""
from pathlib import Path
import json,re,collections,importlib.util,sys
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application
R=Path(__file__).resolve().parents[1];D=R/'docs/data';sys.path.insert(0,str(R))
audit=json.loads((D/'atomic-invariants.json').read_text());records=audit['records'];catalog=json.loads((D/'catalog-records.json').read_text())['records']
assert {r['id'] for r in records}=={r['id'] for r in catalog}
sources={r['id']:r for r in json.loads((D/'localization-results.json').read_text())['examples']}
sources.update({r['id']:r for r in json.loads((D/'flag-fourfolds.json').read_text())['records']})
for name in ['fourfolds','fivefolds']:sources.update({r['id']:r for r in json.loads((D/('toric-'+name+'.json')).read_text())['records']})

def expr(value):
 value=re.sub(r'y_\{(\d+)\}',r'y\1',value);value=re.sub(r'\^\{(-?\d+)\}',r'**(\1)',value)
 value=re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}',r'((\1)/(\2))',value)
 return parse_expr(value,transformations=standard_transformations+(implicit_multiplication_application,),local_dict={f'y{i}':s.Symbol(f'y{i}') for i in range(1,25)})

def sparse_hodge(entries):return {(e['p'],e['q']):e['value'] for e in entries if e['value']}

def source_hodge(text,dim):
 for m in re.finditer(r'\\begin\{(?:array|matrix)\}(?:\{[c ]+\})?(.*?)\\end\{(?:array|matrix)\}',text,re.S):
  rows=[row for row in m[1].split('\\\\') if row.strip()]
  if len(rows)!=2*dim+1:continue
  h={};valid=True
  for rr,row in enumerate(rows):
   for cc,cell in enumerate(row.split('&')):
    cell=cell.strip()
    if not cell:continue
    if not cell.isdigit():valid=False;break
    pnum=rr+cc-dim;p=pnum//2;q=rr-p
    if pnum%2 or not 0<=p<=dim or not 0<=q<=dim:valid=False;break
    if int(cell):h[p,q]=int(cell)
  if valid and h.get((0,0))==1:return h
 raise AssertionError('No source Hodge diagram')

hspec=importlib.util.spec_from_file_location('gwflags._atomic_hodge_validation',R/'software/flag-1.1.0.dev1/gwflags/hodge.py')
hmodule=importlib.util.module_from_spec(hspec);hspec.loader.exec_module(hmodule)
lam=s.Symbol('lambda');full_count=0
for r in records:
 ident=r['id'];src=sources[ident];n=r['ambient_rank'];dim=r['dimension'];h=sparse_hodge(r['full_hodge_numbers'])
 assert all(0<=p<=dim and 0<=q<=dim and isinstance(v,int) and v>=0 for (p,q),v in h.items())
 assert all(h.get((q,p),0)==v and h.get((dim-p,dim-q),0)==v for (p,q),v in h.items()),ident
 poly={}
 for (p,q),v in h.items():k=str(p-q);poly[k]=poly.get(k,0)+v
 assert poly==r['full_hodge_polynomial'] and sum(h.values())==r['full_rank'],ident
 if 'matrix_symbolic' in src:
  M=s.Matrix(src['matrix_symbolic']);unit=src['basis_indices'].index(0)
  if not src['input']['bundle']:
   expected=collections.Counter(src['basis_degrees']);assert h=={(d,d):v for d,v in expected.items()}
  elif r['hodge_provenance'].startswith('Fresh'):
   a=src['input'];report=hmodule.hodge_report(a['algebra'],a['keep'],a['bundle']);assert report['hodge_complete']
   assert h=={(p,q):v for p,row in enumerate(report['hodge_matrix']) for q,v in enumerate(row) if v},ident
 else:
  M=s.zeros(n);unit=src['basis'].index('1')
  for i,j,v in src['matrix_sparse_latex']:M[i,j]=expr(v)
  text=(R/'docs/catalog/records'/(ident.lower()+'.md')).read_text();assert h==source_hodge(text,dim),ident
 assert M.shape==(n,n)
 for test in r['point_tests']:
  values={s.Symbol(k):s.Rational(v) for k,v in test['point'].items()};A=M.subs(values);assert not A.free_symbols
  v=s.eye(n)[:,unit];columns=[]
  for _ in range(n):columns.append(v);v=A*v
  delta=s.sympify(str(DomainMatrix.from_Matrix(s.Matrix.hstack(*columns)).det()))
  assert delta==s.Rational(test['determinant']) and bool(delta)==test['cyclic'],ident
 selected=M.subs({s.Symbol(k):s.Rational(v) for k,v in r['selected_point'].items()})
 assert r['unit_cyclic']==(s.Rational(r['unit_cyclic_determinant'])!=0)
 selected_test=next(t for t in r['point_tests'] if t['point']==r['selected_point']);assert selected_test['determinant']==r['unit_cyclic_determinant']
 expected=s.Integer(1)
 for f in r['factors']:
  p=s.Poly(s.sympify(f['polynomial_A'].replace('lambda','_lambda'),locals={'_lambda':lam}),lam)
  assert p.degree()==f['conjugate_eigenvalues'] and s.gcd(p,p.diff()).degree()==0
  expected*=p.as_expr()**f['multiplicity_per_root']
 assert s.expand(expected-selected.charpoly(lam).as_expr())==0,ident
 if r['classification']=='full_coarse_factors':
  assert r['unit_cyclic'] and r['full_hodge_invariant_rank']==n
  assert r['primitive_assignment_rule'] in {'full_tate','chern_index_zero','unique_rational_root','projective_index_one','odd_nilpotent_factor','cubic_threefold_projective_bundle'}
  if ident in ['LG3-1-2','G2-QUADRIC']:assert r['generality']=='Very general smooth member'
  assert r['curve_completeness']!='not established' and r['generality']
  assert sum(f['rho']*f['conjugate_eigenvalues'] for f in r['factors'])==n
  full={}
  for f in r['factors']:
   assert f['rho']==f['multiplicity_per_root'] and sum(f['hodge_polynomial'].values())==f['full_rank']
   for k,v in f['hodge_polynomial'].items():full[k]=full.get(k,0)+f['conjugate_eigenvalues']*v
  assert full==r['full_hodge_polynomial'],ident
  full_count+=1
 else:
  assert all('rho' not in f and 'hodge_polynomial' not in f for f in r['factors'])
  if r['classification']=='ambient_sector_incomplete':assert r['unit_cyclic'] and r['full_hodge_invariant_rank']>n
  else:assert not r['unit_cyclic'] and not any(t['cyclic'] for t in r['point_tests'])
assert dict(collections.Counter(r['classification'] for r in records))==audit['counts']
print('Validated exact point determinants, characteristic factors, full Hodge data and atomic polynomial sums:',len(records),'records;',full_count,'full certificates')
