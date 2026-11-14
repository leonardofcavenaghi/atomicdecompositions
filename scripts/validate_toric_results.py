"""Validate saved toric matrix contracts without repeating localization sums."""
from pathlib import Path
import sys,json,re,math,collections
P=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(P))
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application

from scripts.validate_exponent_multisets import expression

checked=nonzero=0
polynomials_checked=0
for path in (P/'docs/data').glob('toric-*.json'):
 data=json.loads(path.read_text())
 for r in data['records']:
  ident=r['id'];v=sp.Matrix(r['rays']);n=len(r['basis']);dim=r['dimension'];N=sp.Matrix(r['novikov_divisors']);k=len(r['novikov_divisors'])
  for ray in r['rays']:assert math.gcd(*ray)==1,(ident,'nonprimitive ray')
  facets=collections.Counter()
  for cone in r['cones']:
   assert abs(v[list(cone),:].det())==1,(ident,'nonsmooth maximal cone')
   for j in range(len(cone)):facets[tuple(sorted(cone[:j]+cone[j+1:]))]+=1
  assert all(c==2 for c in facets.values()),(ident,'fan facet incidence')
  c1=sp.Matrix([1-sum(row[i] for row in r['K']) for i in range(len(r['rays']))])
  sol=sp.linsolve((N.T.row_join(v),c1));assert sol is not sp.EmptySet,(ident,'c1 coordinates')
  weights=list(next(iter(sol)))[:k];assert all(x.is_Rational for x in weights),(ident,'Novikov weights')
  basisdegrees=[]
  for name in r['basis']:
   d=0 if name=='1' else sum(int(e or 1) for e in re.findall(r'x\d+(?:\^(\d+))?',name))
   basisdegrees.append(d)
  grade=r['grading_latex'];grade=grade[grade.find('(')+1:grade.rfind(')')]
  actual=[expression(x.strip()) for x in grade.split(',')]
  assert actual==[sp.Rational(d)-sp.Rational(dim,2) for d in basisdegrees],(ident,'grading',actual,basisdegrees)
  variables=[sp.Symbol(f'y{i+1}') for i in range(k)]
  for a,b,latex in r['matrix_sparse_latex']:
   e=expression(latex)
   assert e.free_symbols<=set(variables),(ident,'unexpected symbols',e.free_symbols)
   for term in sp.Add.make_args(sp.expand(e)):
    powers=term.as_powers_dict();coefficient=term
    degree=0
    for y,w in zip(variables,weights):
     power=powers.get(y,0);assert sp.sympify(power).is_Integer,(ident,'nonintegral power')
     coefficient/=y**power;degree+=power*w
    assert coefficient.is_Rational,(ident,'coefficient')
    assert degree+basisdegrees[a]-basisdegrees[b]==1,(ident,'degree axiom',a,b,latex,weights,basisdegrees[a],basisdegrees[b])
   nonzero+=1
  connection=next(q for q in json.loads((P/'docs/data/connection-exponents.json').read_text())['records'] if q['id']==ident)
  factors={f['number']:expression(f['polynomial_latex']) for f in connection['factors']}
  multiplicities={f['number']:f['multiplicity'] for f in connection['factors']}
  assert factors and set(factors)==set(multiplicities),(ident,'factor multiplicities')
  x=sp.Symbol('x');expected=sp.prod(factors[i]**m for i,m in multiplicities.items()).expand()
  M=sp.zeros(n)
  values={sp.Symbol(name):sp.sympify(value) for name,value in r.get('eval_y',{}).items()}
  for a,b,latex in r['matrix_sparse_latex']:M[a,b]=expression(latex).subs(values)
  M=M.subs({y:1 for y in M.free_symbols})
  assert sp.expand((-M).charpoly(x).as_expr()-expected)==0,(ident,'characteristic polynomial at saved point')
  polynomials_checked+=1
  checked+=1
print(json.dumps(dict(records=checked,nonzero_entries=nonzero,characteristic_polynomials=polynomials_checked,checks=['primitive rays','smooth cone determinants','fan facet incidence','c1 Novikov coordinates','basis grading','exact rational Laurent expressions','entry degree axiom'],fresh_localization=False)))
