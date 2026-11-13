"""Check projective and split-bundle identifications directly from the saved fans."""
from pathlib import Path
import json,itertools
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'docs/data'

def primitive_sets(rays,cones):
 k=len(rays);cs=[set(c) for c in cones];out=[]
 for size in range(2,len(rays[0])+2):
  for seq in itertools.combinations(range(k),size):
   q=set(seq)
   if any(p<=q for p in out):continue
   if not any(q<=c for c in cs):out.append(q)
 return out

def identify(r):
 rays=r['rays'];k=len(rays);n=len(rays[0]);rho=k-n
 pcs=primitive_sets(rays,r['cones']);V=s.Matrix(rays)
 if len(pcs)!=rho or set().union(*pcs)!=set(range(k)) or sum(map(len,pcs))!=k:return dict(status='fan presentation retained',picard_rank=rho)
 expected={tuple(sorted(set(range(k))-set(omit))) for omit in itertools.product(*(sorted(b) for b in pcs))}
 assert expected=={tuple(sorted(c)) for c in r['cones']},r['id']
 sums=[sum((s.Matrix(rays[i]) for i in b),s.zeros(n,1)) for b in pcs]
 if all(v==s.zeros(n,1) for v in sums):
  dims=[len(b)-1 for b in pcs];degrees=[[sum(row[i] for i in b) for b in pcs] for row in r['K']]
  return dict(status='verified',kind='projective space' if rho==1 else 'product of projective spaces',dimensions=dims,defining_degrees=degrees,primitive_blocks=[sorted(b) for b in pcs],certificate='Disjoint primitive collections; each ray-block sum is zero; all product maximal cones match.')
 if rho>2:
  for fidx,F0 in enumerate(pcs):
   if sums[fidx]!=s.zeros(n,1):continue
   F=sorted(F0);Bs=[sorted(b) for j,b in enumerate(pcs) if j!=fidx]
   columns=[];valid=True
   for j,b in enumerate(pcs):
    if j==fidx:continue
    solution=list(s.linsolve((s.Matrix([rays[v] for v in F[1:]]).T,sums[j])))
    if not solution or not all(v.is_Integer for v in solution[0]):valid=False;break
    col=[0]+list(map(int,solution[0]));columns.append([v-min(col) for v in col])
   if not valid:continue
   a=[list(v) for v in zip(*columns)]
   basis=V[[j for b in Bs for j in b[1:]]+F[1:],:].T
   assert abs(basis.det())==1,r['id']
   Q=s.zeros(k,rho)
   for j,b in enumerate(Bs):
    for v in b:Q[v,j]=1
   for j,v in enumerate(F):
    for z in range(rho-1):Q[v,z]=-a[j][z]
    Q[v,rho-1]=1
   assert V.T*Q==s.zeros(n,rho),(r['id'],'bundle divisor relations')
   defining=[list(map(int,(s.Matrix([row])*Q).tolist()[0])) for row in r['K']]
   return dict(status='verified',kind='split projective bundle over product',base_dimensions=[len(b)-1 for b in Bs],twists_vectors=sorted(a),defining_divisor_coordinates=defining,base_rays=Bs,fibre_rays=F,certificate='Primitive collections and all product maximal cones match; a cone gives a unimodular lattice basis; fibre ray sum vanishes and the exact divisor-class matrix satisfies every lattice linear relation.')
  return dict(status='fan presentation retained',picard_rank=rho)
 zeros=[i for i,v in enumerate(sums) if v==s.zeros(n,1)]
 assert rho==2 and len(zeros)==1,(r['id'],'no unique fibre collection',pcs,sums)
 F=sorted(pcs[zeros[0]]);B=sorted(pcs[1-zeros[0]])
 coeff=list(s.linsolve((s.Matrix([rays[j] for j in F[1:]]).T,sums[1-zeros[0]])))[0]
 assert all(v.is_Integer for v in coeff),r['id'];a=[0]+list(map(int,coeff));a=[v-min(a) for v in a]
 # The integral basis from a maximal cone proves the lattice model, not just an equal period.
 basis=V[B[1:]+F[1:],:].T;assert abs(basis.det())==1,r['id']
 jzero=F[a.index(0)]
 def principal(vec):
  m=list(s.linsolve((V,s.Matrix(vec))))
  return bool(m) and all(x.is_Integer for x in m[0])
 for j,twist in zip(F,a):
  v=[0]*k;v[j]+=1;v[jzero]-=1;v[B[0]]+=twist;assert principal(v),(r['id'],j,'divisor convention')
 for j in B:
  v=[0]*k;v[j]+=1;v[B[0]]-=1;assert principal(v),(r['id'],j,'base divisor')
 degrees=[]
 for row in r['K']:
  d=sum(row[j] for j in F);h=sum(row[j] for j in B)-sum(row[j]*tw for j,tw in zip(F,a));degrees.append(dict(xi=d,H=h))
 return dict(status='verified',kind='split projective bundle',base_dimension=len(B)-1,fibre_dimension=len(F)-1,twists=sorted(a),defining_divisors=degrees,base_rays=B,fibre_rays=F,ray_twists=a,certificate='Disjoint primitive collections and all maximal cones verified; a cone gives a unimodular lattice basis; fibre ray sum vanishes; normalized twisting relation and divisor linear equivalences checked exactly.')


if __name__=='__main__':
 results=[]
 for slug in ['fourfolds','fivefolds']:
  for record in json.loads((D/('toric-'+slug+'.json')).read_text())['records']:
   result=identify(record);result['id']=record['id'];results.append(result)
 expected=json.loads((D/'geometric-presentations.json').read_text())['records']
 assert results==expected,'Geometric certificates disagree with the saved fan and divisor inputs'
 print('Verified geometric presentations:',sum(r['status']=='verified' for r in results),'of',len(results))
