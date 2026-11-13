"""Validate fresh fourfold outputs and their exact connection/Hodge identities."""
from pathlib import Path
import importlib.util,json,sys
import sympy as s
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R))
from gwflags import FlagVariety
spec=importlib.util.spec_from_file_location('flag_connection_validation',R/'software/flag-1.1.0.dev1/gwflags/connection_spectra.py')
analysis=importlib.util.module_from_spec(spec);spec.loader.exec_module(analysis)
hspec=importlib.util.spec_from_file_location('gwflags._hodge_validation',R/'software/flag-1.1.0.dev1/gwflags/hodge.py')
hmodule=importlib.util.module_from_spec(hspec);hspec.loader.exec_module(hmodule)
data=json.loads((R/'docs/data/flag-fourfolds.json').read_text())['records']
expected={'LG3-1-2':(128,-8,80,448),'G2-QUADRIC':(324,-6,60,828)}
assert {r['id'] for r in data}==set(expected)
for r in data:
 ident=r['id'];delta,root,a,b=expected[ident]
 X=FlagVariety(r['input']['algebra'],r['input']['keep']);K=r['input']['bundle']
 index,betas=X.fano_index_and_betas(K)
 assert X.dimension-len(K)==r['dimension']==4 and index==r['fano_index']==1
 assert [list(beta) for beta in betas]==r['curve_classes']
 assert [list(X.class_words()[i]) for i in r['basis_indices']]==r['basis_words']
 assert [len(w) for w in r['basis_words']]==r['basis_degrees']
 M=s.Matrix(r['matrix_symbolic']);A=M.subs({v:1 for v in M.free_symbols});G=s.Matrix(r['grading']);n=M.rows
 assert n==5 and A==s.Matrix(r['matrix_at_one'])
 assert G==s.diag(*[d-2 for d in r['basis_degrees']])
 y=s.Symbol('y1');assert M.free_symbols=={y}
 for i in range(n):
  for j in range(n):
   if M[i,j]:assert s.Poly(M[i,j],y).monoms()==[(1-r['basis_degrees'][i]+r['basis_degrees'][j],)]
 unit=s.eye(n)[:,r['basis_indices'].index(0)];C=s.Matrix.hstack(*[A**k*unit for k in range(n)])
 assert C.det()==delta==s.Rational(r['cyclic_determinant_at_one'])
 z=s.Symbol('z');assert s.expand(A.charpoly(z).as_expr()-(z-root)**3*(z**2-a*z-b))==0
 c=analysis.connection_report(M,G);assert c==r['connection'] and c['status']=='computed'
 triple=next(f for f in c['sectors'] if f['multiplicity_per_root']==3)
 assert triple['classes_mod_Z']=={'0':1,'1/2':2}
 h=hmodule.hodge_report(r['input']['algebra'],r['input']['keep'],K)
 assert h['hodge_complete']
 assert {f'{p},{q}':value for p,row in enumerate(h['hodge_matrix']) for q,value in enumerate(row) if value}==r['hodge_numbers']
 assert r['genericity']=='Very general smooth member'
 factors=r['coarse_factors'];assert sum(f['conjugate_count']*f['rho'] for f in factors)==5
 poly={}
 for f in factors:
  assert sum(f['hodge_polynomial'].values())==f['full_rank']
  for k,v in f['hodge_polynomial'].items():poly[k]=poly.get(k,0)+f['conjugate_count']*v
 full={}
 for pair,value in r['hodge_numbers'].items():
  p,q=map(int,pair.split(','));k=str(p-q);full[k]=full.get(k,0)+value
 assert poly==full=={'0':104,'2':14,'-2':14}
 assert sum(f['conjugate_count']*f['full_rank'] for f in factors)==132
print('Validated fresh fourfold matrices, full curve lists, exact exponent multisets and Hodge polynomial identities:',len(data))
