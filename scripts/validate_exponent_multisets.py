"""Verify exact exponent multisets against saved factor notes, retaining repeats."""
from pathlib import Path
from fractions import Fraction
import re,json,sys,collections
R=Path(__file__).resolve().parents[1]
import sympy as s
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application
x=s.Symbol('x');lam=s.Symbol('lambda')

def rationals(tex):
 tex=tex.strip().strip('$').replace('\\ ','').replace(' ','')
 if tex in ('','unresolved'):return None
 out=[]
 for v in tex.split(','):
  m=re.fullmatch(r'(-?)\\frac\{(-?\d+)\}\{(\d+)\}',v)
  if m:out.append(Fraction((-1 if m[1] else 1)*int(m[2]),int(m[3])))
  else:out.append(Fraction(v))
 return [str(v) for v in out]

def polynomial(tex):
 tex=tex.strip().rstrip('.').replace('\\\\&','').replace('\\,','')
 tex=re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}',r'((\1)/(\2))',tex)
 tex=re.sub(r'\^\{(-?\d+)\}',r'**(\1)',tex).replace('^','**')
 return s.Poly(parse_expr(tex,local_dict={'x':x},transformations=standard_transformations+(implicit_multiplication_application,)),x).monic()

out=[]
for slug in ['fourfolds','fivefolds']:
 for row in json.loads((R/'docs/data'/('toric-'+slug+'.json')).read_text())['records']:
  path=R/'docs/catalog/records'/(row['id'].lower()+'.md');text=path.read_text();factors={}
  polys={int(m[1]):m[2] for m in re.finditer(r'\\begin\{aligned\}p_\{(\d+)\}\(x\)&=(.*?)\\end\{aligned\}',text,re.S)}
  for i,p in polys.items():
   poly=polynomial(p)
   assert s.gcd(poly,poly.diff()).degree()==0,(row['id'],i,'factor is not square-free')
   if slug=='fourfolds':
    match=re.search(r'Factor '+str(i)+r': multiplicity (\d+); (\d+) distinct root',text)
    assert match,(row['id'],i)
    multiplicity=int(match[1]);assert poly.degree()==int(match[2])
   else:
    det=re.search(r'\\det\(xI-K\^F\)=(.*?)(?:\\\]|\$\$)',text,re.S)
    assert det,row['id']
    ms={int(j):int(m or 1) for j,m in re.findall(r'p_\{(\d+)\}\(x\)(?:\^\{(\d+)\})?',det[1])}
    multiplicity=ms[i]
   factors[i]=dict(number=i,polynomial_latex=p.strip().rstrip('.'),multiplicity=multiplicity,distinct_eigenvalues=poly.degree(),powers=None,classes=None,status='unresolved')
  if slug=='fourfolds':
   for m in re.finditer(r'Factor (\d+): multiplicity (\d+); (\d+) distinct root\(s\)(.*?)(?=\nFactor \d+:|\Z)',text,re.S):
    i=int(m[1]);f=factors[i];assert (f['multiplicity'],f['distinct_eigenvalues'])==(int(m[2]),int(m[3]))
    powers=re.search(r'\\text\{Powers\}=\\\{(.*?)\\\}',m[4],re.S)
    classes=re.search(r'\\text\{Classes modulo \}\\mathbb Z=\\\{(.*?)\\\}',m[4],re.S)
    f['powers']=rationals(powers[1]) if powers else None;f['classes']=rationals(classes[1]) if classes else None
    f['status']='complete' if 'Complete exponent computation: True.' in m[4] else ('partial' if powers or classes else 'unresolved')
  else:
   for line in text.splitlines():
    m=re.match(r'\| \$p_\{(\d+)\}\$ \|',line)
    if not m:continue
    cells=line.split('|');f=factors[int(m[1])];f['powers']=rationals(cells[2]);f['classes']=rationals(cells[3]);f['status']='complete' if cells[4].strip().startswith('complete /') else ('partial' if f['powers'] or f['classes'] else 'unresolved');f['method']=cells[4].strip()
  assert len(factors)>0 and sum(f['multiplicity']*f['distinct_eigenvalues'] for f in factors.values())==len(row['basis']),row['id']
  for f in factors.values():
   if f['status']=='complete':assert len(f['powers'])==len(f['classes'])==f['multiplicity'],(row['id'],f)
   if f['powers'] is not None and f['classes'] is not None:
    assert collections.Counter(str(Fraction(v)%1) for v in f['powers'])==collections.Counter(f['classes']),(row['id'],f)
  out.append(dict(id=row['id'],point=row['eval_y'],sector='computed ambient connection',factors=list(factors.values()),source=str(path.relative_to(R/'docs'))))
result=dict(convention='A=c1 star; saved characteristic factors p_i are for K^F=-A. Each row gives the multiset separately at every lambda with p_i(-lambda)=0. Powers s=-theta; classes are s modulo Z. Repeated entries are retained; unresolved is not an empty multiset.',records=out)
saved=json.loads((R/'docs/data/connection-exponents.json').read_text())
assert result==saved,'Saved exponent multisets disagree with their source factor notes'
print(json.dumps(dict(records=len(out),factor_statuses=dict(collections.Counter(f['status'] for r in out for f in r['factors'])))))
