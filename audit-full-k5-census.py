"""Independent full K5 census reconstruction; no generator imports.

Completeness: independently enumerate every allowed K4, then all extensions
of one representative of each orbit. Expand and check the complete S5/color
orbits, disjointness, every marginal coefficient and every rooted flag row.
"""
from array import array
from collections import Counter
from itertools import combinations,permutations,product
from pathlib import Path
import json,time
root=Path(__file__).resolve().parent
d=json.loads((root/'full-k5-242467-census.json').read_text())
S={t for i,t in enumerate(combinations(range(6),3)) if 242467>>i&1}
CP=[p for p in permutations(range(6)) if {tuple(sorted(p[c] for c in t)) for t in S}==S]
E4=list(combinations(range(4),2));E5=list(combinations(range(5),2))
V4=list(permutations(range(4)));V5=list(permutations(range(5)))
map4=[tuple(E4.index(tuple(sorted((v[a],v[b])))) for a,b in E4) for v in V4]
map5=[tuple(E5.index(tuple(sorted((v[a],v[b])))) for a,b in E5) for v in V5]
tris4=[tuple(E4.index(e) for e in combinations(vs,2)) for vs in combinations(range(4),3)]
tris5=[tuple(E5.index(e) for e in combinations(vs,2)) for vs in combinations(range(5),3)]
def allowed(p,tris):return all(len(set(q:=tuple(p[i] for i in t)))<3 or tuple(sorted(q)) in S for t in tris)
def encode(p):
    v=0
    for c in p:v=6*v+c
    return v
index4={}
for oi,row in enumerate(d['k4_orbits']):
    rep=row['pattern'];orb={tuple(cp[rep[j]] for j in m) for cp in CP for m in map4}
    assert len(orb)==row['orbit_size'] and tuple(rep)==min(orb)
    for p in orb:assert p not in index4;index4[p]=oi
direct4={p for p in product(range(6),repeat=6) if allowed(p,tris4)}
assert direct4==set(index4)
indexflag={}
tails=[m for v,m in zip(V4,map4) if v[0]==0]
for fi,row in enumerate(d['rooted_flag_orbits']):
    f=row['representative']
    orb={tuple(cp[f[j]] for j in m)+(cp[f[6]],) for cp in CP for m in tails}
    assert len(orb)==row['orbit_size'] and tuple(f)==min(orb)
    for p in orb:assert p not in indexflag;indexflag[p]=fi
assert set(indexflag)=={k+(c,) for k in direct4 for c in range(6)}
lookup=array('h',[-1])*(6**10)
base=[E5.index(e) for e in E4];extension=E5.index((0,4))
count=0;started=time.monotonic()
for oi,row in enumerate(d['k5_orbits']):
    rep=row['pattern'];assert allowed(rep,tris5)
    orb={tuple(cp[rep[j]] for j in m) for cp in CP for m in map5}
    assert tuple(rep)==min(orb) and len(orb)==row['orbit_size']
    marg=Counter();fc=Counter()
    for p in orb:
        code=encode(p);assert lookup[code]==-1;lookup[code]=oi
        k=tuple(p[i] for i in base);marg[index4[k]]+=1
        # Check complete rooted classes, not a reduced independent row basis.
        for c in range(6):fc[indexflag[k+(c,)]]+=5 if p[extension]==c else -1
    expected=[marg[i]//r['orbit_size'] for i,r in enumerate(d['k4_orbits'])]
    assert all(marg[i]%r['orbit_size']==0 for i,r in enumerate(d['k4_orbits']))
    assert expected==row['k4_per_pattern_marginals']
    assert {i:v for i,v in fc.items() if v}==dict(row['rooted_balance_coefficients'])
    count+=len(orb)
seeds=0;covered=Counter()
for row in d['k4_orbits']:
    old=dict(zip(E4,row['pattern']))
    for colors in product(range(6),repeat=4):
        ed=old|{(i,4):colors[i] for i in range(4)}
        p=tuple(ed[e] for e in E5)
        if allowed(p,tris5):
            oi=lookup[encode(p)];assert oi>=0;covered[oi]+=1;seeds+=1
assert seeds==5306 and len(covered)==551 and count==2607696
assert all(covered[i]==r['seed_count'] for i,r in enumerate(d['k5_orbits']))
out={'verified':True,'independent_K4_coverage':len(direct4),
     'labeled_rooted_flags':len(indexflag),'rooted_classes':len(d['rooted_flag_orbits']),
     'K5_orbits':len(covered),'K5_labeled_patterns':count,'all_seed_extensions':25*6**4,
     'allowed_seeds':seeds,'all_marginals_and_all_flag_coefficients':True,
     'seconds':time.monotonic()-started}
(root/'full-k5-census-independent-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
