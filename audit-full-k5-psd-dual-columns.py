"""Exact dual replay using independently reconstructed/audited census columns.

No optimizer, numerical matrix routines or discovery imports.
"""
from fractions import Fraction as Q
from itertools import combinations,permutations
from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent
d=json.loads((root/'full-k5-242467-census.json').read_text())
path=root/'full-k5-242467-psd-dual.json'
cert=json.loads(path.read_text())
S={t for i,t in enumerate(combinations(range(6),3)) if 242467>>i&1}
CP=[p for p in permutations(range(6)) if {tuple(sorted(p[c] for c in t)) for t in S}==S]
E=list(combinations(range(4),2))
G=[]
for row in d['k4_orbits']:
    rep=row['pattern']
    orb={tuple(cp[rep[E.index(tuple(sorted((v[a],v[b]))))]] for a,b in E)
         for cp in CP for v in permutations(range(4))}
    assert len(orb)==row['orbit_size']
    G.append(orb)
a={r['index']:Q(r['coefficient']) for r in cert['flag_coefficients']}
assert len(a)==len(cert['flag_coefficients'])
cuts=[]
for r in cert['PSD_cuts']:
    b=Q(r['coefficient']);v=r['vector'];e=r['color']
    assert b>=0 and len(v)==36 and all(isinstance(x,int) for x in v)
    q4=[sum(v[6*k[1]+k[3]]*v[6*k[2]+k[4]] for k in orb if k[0]==e) for orb in G]
    cuts.append((b,q4,max(abs(x) for x in v)**2))
minimum=None
for row in d['k5_orbits']:
    f=dict(row['rooted_balance_coefficients'])
    numerator=sum(x*f.get(i,0) for i,x in a.items())
    numerator-=sum(b*sum(x*y for x,y in zip(q4,row['k4_per_pattern_marginals']))
                   for b,q4,_ in cuts)
    average=numerator/row['orbit_size']
    assert average>=1
    minimum=average if minimum is None else min(minimum,average)
A=sum(abs(x) for x in a.values());B=sum(b*norm for b,_,norm in cuts)
bound=18*A+B+4
first_integer=bound.numerator//bound.denominator+1
out={'verified':True,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
     'K5_orbits':len(d['k5_orbits']),'minimum_averaged_gap':str(minimum),
     'flag_classes':len(a),'PSD_cuts':len(cuts),'A':str(A),'B':str(B),
     'sufficient_n_strict_bound':str(bound),'sufficient_integer_n':str(first_integer)}
(root/'full-k5-psd-dual-column-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
