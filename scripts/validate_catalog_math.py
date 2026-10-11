"""Audit every displayed spectrum and projective Hodge diamond.

Spectra are checked numerically against characteristic-polynomial derivatives
with 60-digit evaluations and a relative residual tolerance of 1e-9. Hodge
numbers use exact rational Hirzebruch-Riemann-Roch: the coefficient of H^n in
[H(1+y exp(-H))/(1-exp(-H))]^(n+1)/(1+y), multiplied by
(1-exp(-d H))/(1+y exp(-d H)) for each defining degree d. Lefschetz determines
the off-middle cohomology, so the resulting chi_y determines the diamond.

Install requirements-test.txt before running. This does not repeat GW sums.
"""
import sys, re, json, math
from pathlib import Path
from fractions import Fraction as F
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import sympy as s
from sympy.parsing.latex import parse_latex
from scripts.validate_catalog import cards, FIELD_RE, MATRIX_RE
from scripts.validate_localization_results import parse_display

failures = []
eigen_count = hodge_count = 0

def chi_y(n, degrees, y):
    def mul(a,b):
        return [sum(a[j]*b[k-j] for j in range(k+1)) for k in range(n+1)]
    def div(a,b):
        c=[]
        for k in range(n+1):
            c.append((a[k]-sum(b[j]*c[k-j] for j in range(1,k+1)))/b[0])
        return c
    exp=[F((-1)**k,math.factorial(k)) for k in range(n+1)]
    a=div([F(1+y)]+[y*v for v in exp[1:]],
          [F((-1)**k,math.factorial(k+1)) for k in range(n+1)])
    result=[F(1)]+[F(0)]*n
    for _ in range(n+1): result=mul(result,a)
    for d in degrees:
        ex=[F((-d)**k,math.factorial(k)) for k in range(n+1)]
        result=mul(result,div([F(0)]+[-v for v in ex[1:]],
                             [F(1+y)]+[y*v for v in ex[1:]]))
    return result[n]/(1+y)

for filename in ['projective.md','grassmannians.md','flag_varieties.md']:
    path=ROOT/'docs/catalog'/filename
    entries=cards(path)
    if filename=='flag_varieties.md':
        from types import SimpleNamespace
        entries=[SimpleNamespace(title='Fl(1,2,3)',text=path.read_text())]
    for card in entries:
        try:
            m=MATRIX_RE.search(card.text)
            A=s.Matrix([[parse_display(c) for c in row.split('&')] for row in m.group(1).split('\\\\') if row.strip()])
            A=A.subs({v:1 for v in A.free_symbols})
            eigenline=re.search(r'\*\*Eigenvalues:\*\* (.*)',card.text)
            if eigenline:
                pairs=re.findall(r'\$([^$]+)\$ \(mult: (\d+)\)',eigenline.group(1))
                assert pairs, 'unparsed eigenvalue line'
                assert sum(int(mult) for _,mult in pairs)==A.rows, 'eigenvalue multiplicity total'
                poly=A.charpoly().as_poly(); x=poly.gen
                seen=[]
                for latex,mult in pairs:
                    value=parse_latex(latex).subs({s.Symbol('i'):s.I,s.Symbol('pi'):s.pi})
                    assert not value.free_symbols, ('unparsed eigenvalue',latex,value)
                    z=s.N(value,60)
                    assert all(abs(complex(z)-a)>1e-7*max(1,abs(complex(z))) for a in seen), 'duplicate eigenvalue'
                    seen.append(complex(z))
                    p=poly
                    for k in range(int(mult)):
                        residual=abs(complex(s.N(p.as_expr().subs(x,z),50)))
                        scale=sum(abs(complex(c))*max(1,abs(complex(z)))**power[0] for power,c in p.terms())
                        assert residual/max(1,scale)<1e-9, ('spectral residual',latex,k,residual/max(1,scale))
                        p=p.diff()
                eigen_count+=1
            diamond=re.search(r'\\begin\{matrix\}(.*?)\\end\{matrix\}',card.text,re.S)
            if filename=='projective.md' and diamond:
                n=int(re.match(r'P(\d+)',card.title).group(1))
                degrees=[int(d) for d in re.findall(r'O\((\d+)\)',card.title)]
                dim=n-len(degrees); y=s.Symbol('y')
                chi=s.Poly(s.interpolate([(j,s.Rational(chi_y(n,degrees,j))) for j in range(dim+1)],y),y)
                actual={}
                rows=[row for row in diamond.group(1).split('\\\\') if row.strip()]
                assert len(rows)==2*dim+1, 'diamond height'
                for r,row in enumerate(rows):
                    for c,token in enumerate(row.split('&')):
                        if token.strip():
                            p=(r+c-dim)//2; q=r-p
                            assert (r+c-dim)%2==0 and 0<=p<=dim and 0<=q<=dim, 'diamond position'
                            actual[p,q]=int(token)
                expected={}
                for p in range(dim+1):
                    for q in range(dim+1):
                        value=int(p==q)
                        if p+q==dim:
                            value+=(-1)**q*(chi.nth(p)-(-1)**p)
                        expected[p,q]=value
                assert actual==expected, ('Hodge mismatch',[(k,v,expected[k]) for k,v in actual.items() if v!=expected[k]])
                hodge_count+=1
        except Exception as e:
            failures.append({'page':filename,'title':card.title,'error':str(e)})
report={'eigenvalue_cards_checked':eigen_count,'projective_Hodge_diamonds_checked':hodge_count,'failures':failures}
print(json.dumps(report,indent=2))

if failures:
    raise SystemExit(1)
