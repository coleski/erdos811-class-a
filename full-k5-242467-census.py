"""Complete allowed K5 orbit census from canonical four-vertex faces.

Every allowed K5 has a face in one of the25 allowed K4 orbits. Therefore
25*6**4 extensions suffice as seeds; no support restriction is imposed.
"""
from collections import Counter
from itertools import combinations, permutations, product
from pathlib import Path
import json
import time

root = Path(__file__).resolve().parent
started = time.monotonic()
family = {q for i, q in enumerate(combinations(range(6), 3)) if 242467 >> i & 1}
autos = [p for p in permutations(range(6))
         if {tuple(sorted(p[c] for c in q)) for q in family} == family]
E4 = list(combinations(range(4), 2))
E5 = list(combinations(range(5), 2))
V4 = [tuple(E4.index(tuple(sorted((p[a], p[b])))) for a, b in E4)
      for p in permutations(range(4))]
V5 = [tuple(E5.index(tuple(sorted((p[a], p[b])))) for a, b in E5)
      for p in permutations(range(5))]
rows4 = json.loads((root / 'k5-242467-universal-cut.json').read_text())['orbits']
index4 = {}
for i, row in enumerate(rows4):
    k = row['pattern']
    orb = {tuple(cp[k[j]] for j in vi) for cp in autos for vi in V4}
    assert len(orb) == row['orbit_size']
    for q in orb:
        assert q not in index4
        index4[q] = i
assert len(index4) == 12936
tri4 = [tuple(E4.index(e) for e in combinations(vs, 2))
        for vs in combinations(range(4), 3)]
allowed4 = {p for p in product(range(6), repeat=6)
            if all(len(set(q := tuple(p[e] for e in inds))) < 3
                   or tuple(sorted(q)) in family for inds in tri4)}
assert set(index4) == allowed4
faces = [tuple(E5.index(e) for e in combinations(vs, 2))
         for vs in combinations(range(5), 4)]
base = tuple(E5.index(e) for e in E4)
extension_edge = E5.index((0, 4))

seeds = set()
for row in rows4:
    fixed = dict(zip(E4, row['pattern']))
    for colors in product(range(6), repeat=4):
        edges = fixed | {(v, 4): colors[v] for v in range(4)}
        p = tuple(edges[e] for e in E5)
        if all(tuple(p[e] for e in face) in index4 for face in faces):
            seeds.add(p)
print(json.dumps({'stage': 'seeds', 'count': len(seeds),
                  'tested_extensions': 25 * 6**4}), flush=True)

# Root-preserving symmetry classes of the full K4->K5 balance flags.
tail_actions = []
for tail in permutations((1, 2, 3)):
    vp = (0,) + tail
    tail_actions.append(tuple(E4.index(tuple(sorted((vp[a], vp[b])))) for a, b in E4))
unseen = {k + (c,) for k in index4 for c in range(6)}
flag_index = {}
flag_rows = []
while unseen:
    f = min(unseen)
    orb = {tuple(cp[f[j]] for j in vi) + (cp[f[6]],)
           for cp in autos for vi in tail_actions}
    assert orb <= unseen
    idx = len(flag_rows)
    flag_rows.append({'representative': f, 'orbit_size': len(orb)})
    for q in orb:
        flag_index[q] = idx
    unseen.difference_update(orb)
print(json.dumps({'stage': 'flags', 'classes': len(flag_rows),
                  'labeled_flags': len(flag_index)}), flush=True)

todo = seeds.copy()
rows5 = []
total = 0
while todo:
    seed = min(todo)
    orb = {tuple(cp[seed[j]] for j in vi) for cp in autos for vi in V5}
    removed = todo.intersection(orb)
    assert removed and removed == seeds.intersection(orb)
    todo.difference_update(orb)
    marginal = Counter()
    flag_coeff = Counter()
    for p in orb:
        k = tuple(p[e] for e in base)
        marginal[index4[k]] += 1
        flag_coeff[flag_index[k + (p[extension_edge],)]] += 6
        for c in range(6):
            flag_coeff[flag_index[k + (c,)]] -= 1
    counts = [marginal[i] for i in range(25)]
    assert sum(counts) == len(orb)
    assert all(n % r['orbit_size'] == 0 for n, r in zip(counts, rows4))
    rows5.append({'pattern': min(orb), 'orbit_size': len(orb),
                  'seed_count': len(removed),
                  'k4_per_pattern_marginals': [n // r['orbit_size'] for n, r in zip(counts, rows4)],
                  'rooted_balance_coefficients': sorted((i, c) for i, c in flag_coeff.items() if c)})
    total += len(orb)
    if len(rows5) % 100 == 0:
        print(json.dumps({'stage': 'orbits', 'completed': len(rows5),
                          'remaining_seeds': len(todo), 'seconds': time.monotonic()-started}), flush=True)
rows5.sort(key=lambda r: tuple(r['pattern']))
out = {'mask': 242467, 'scope': 'ALL palette-allowed K5 patterns',
       'color_automorphisms': len(autos), 'seed_count': len(seeds),
       'total_labeled_k5_patterns': total,
       'k4_orbits': [{'pattern': r['pattern'], 'orbit_size': r['orbit_size']} for r in rows4],
       'rooted_flag_orbits': flag_rows, 'k5_orbits': rows5}
path = root / 'full-k5-242467-census.json'
path.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({'stage': 'complete', 'k5_orbits': len(rows5),
                  'labeled_k5_patterns': total, 'rooted_flag_classes': len(flag_rows),
                  'seconds': time.monotonic()-started, 'path': str(path)}), flush=True)
