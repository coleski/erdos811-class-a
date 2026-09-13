"""Root's independent rational column check and original finite threshold.

Uses the separately reconstructed census as a finite combinatorial input;
does not import any solver, producer, or certificate verifier.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
path = root / 'full-k5-242467-psd-dual.json'
cert = json.loads(path.read_text())
data = json.loads((root / 'full-k5-242467-census.json').read_text())
assert cert['mask'] == data['mask'] == 242467
a = {r['index']: Q(r['coefficient']) for r in cert['flag_coefficients']}
assert len(a) == len(cert['flag_coefficients'])
assert all(0 <= i < len(data['rooted_flag_orbits']) for i in a)
family = {t for i, t in enumerate(combinations(range(6), 3)) if 242467 >> i & 1}
autos = [p for p in permutations(range(6))
         if {tuple(sorted(p[c] for c in t)) for t in family} == family]
edges = list(combinations(range(4), 2))
maps = [tuple(edges.index(tuple(sorted((p[i], p[j])))) for i, j in edges)
        for p in permutations(range(4))]
orbits = []
for r in data['k4_orbits']:
    k = r['pattern']
    orb = {tuple(cp[k[i]] for i in m) for cp in autos for m in maps}
    assert len(orb) == r['orbit_size']
    orbits.append(orb)
cuts = []
for row in cert['PSD_cuts']:
    b, e, v = Q(row['coefficient']), row['color'], row['vector']
    assert b >= 0 and 0 <= e < 6 and len(v) == 36
    assert all(isinstance(x, int) for x in v)
    q4 = [sum(v[6*k[1]+k[3]] * v[6*k[2]+k[4]] for k in orb if k[0] == e)
          for orb in orbits]
    cuts.append((b, v, q4))
minimum = None
for row in data['k5_orbits']:
    score = sum(a.get(i, Q(0)) * c for i, c in row['rooted_balance_coefficients'])
    for b, v, q4 in cuts:
        score -= b * sum(c * q for c, q in zip(row['k4_per_pattern_marginals'], q4))
    score /= row['orbit_size']
    assert score >= 1
    minimum = score if minimum is None else min(minimum, score)
A = sum(map(abs, a.values()))
D = sum(b * max(map(abs, v))**2 for b, v, q4 in cuts)
bound = 18*A + D
min_n = (bound + 4).__floor__() + 1
min_t = ((bound + 3)/6).__floor__() + 1
assert 6*min_t - 3 > bound
assert 6*629137 - 3 > bound
out = {'verified': True, 'certificate_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
       'K5_orbits': len(data['k5_orbits']), 'minimum_group_average': str(minimum),
       'flag_norm_A': str(A), 'PSD_error_norm_D': str(D),
       'strict_finite_bound_18A_plus_D': str(bound),
       'sufficient_n': min_n, 'sufficient_t': min_t,
       'existing_global_threshold_629137_dominates': True,
       'scope': 'Global family242467 exclusion only; ClassA remains'}
(root / 'root-full-k5-dual-check.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
