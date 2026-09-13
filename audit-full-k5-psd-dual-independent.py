"""Exact raw-pattern audit of the full K5 B dual; no producer imports.

The census JSON supplies representatives only; coverage, orbit action, rooted
flag classes, and every raw function value are independently reconstructed.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import lcm
from pathlib import Path
import hashlib
import json
import time

HERE = Path(__file__).parent
cert_path = HERE / 'full-k5-242467-psd-dual.json'
census_path = HERE / 'full-k5-242467-census.json'
cert_bytes = cert_path.read_bytes()
census_bytes = census_path.read_bytes()
cert = json.loads(cert_bytes)
census = json.loads(census_bytes)
assert cert['mask'] == census['mask'] == 242467
F = {tuple(map(int, x)) for x in
     '012 013 024 035 045 125 134 145 234 235'.split()}
autos = [p for p in permutations(range(6))
         if {tuple(sorted(p[x] for x in t)) for t in F} == F]
assert len(autos) == 60
E4 = list(combinations(range(4), 2))
E5 = list(combinations(range(5), 2))
T4 = [[E4.index(e) for e in combinations(t, 2)] for t in combinations(range(4), 3)]
T5 = [[E5.index(e) for e in combinations(t, 2)] for t in combinations(range(5), 3)]


def ok(p, triangles):
    return all(len(s := {p[i] for i in inds}) < 3 or tuple(sorted(s)) in F
               for inds in triangles)


def actions(edges, perms):
    return [tuple(edges.index(tuple(sorted((p[i], p[j])))) for i, j in edges)
            for p in perms]


A4 = actions(E4, permutations(range(4)))
A5 = actions(E5, permutations(range(5)))
AR = actions(E4, [(0,) + p for p in permutations((1, 2, 3))])
all4 = {p for p in product(range(6), repeat=6) if ok(p, T4)}
assert len(all4) == 12936
todo4 = all4.copy()
reps4 = []
while todo4:
    p = min(todo4)
    orb = {tuple(cp[p[j]] for j in a) for cp in autos for a in A4}
    assert orb <= todo4
    reps4.append((p, len(orb)))
    todo4.difference_update(orb)
assert reps4 == [(tuple(r['pattern']), r['orbit_size']) for r in census['k4_orbits']]

# Independent complete seed coverage, justified by canonicalizing face0123.
base = [E5.index(e) for e in E4]
ext = [E5.index((v, 4)) for v in range(4)]
seeds = set()
for p, _ in reps4:
    for tail in product(range(6), repeat=4):
        q = [-1] * 10
        for i, c in zip(base, p): q[i] = c
        for i, c in zip(ext, tail): q[i] = c
        if ok(q, T5): seeds.add(tuple(q))
assert len(seeds) == 5306

unseen = {q + (d,) for q in all4 for d in range(6)}
flag_index = {}
flag_sizes = []
for i, recorded in enumerate(census['rooted_flag_orbits']):
    p = min(unseen)
    assert p == tuple(recorded['representative'])
    orb = {tuple(cp[p[j]] for j in a) + (cp[p[6]],)
           for cp in autos for a in AR}
    assert orb <= unseen and len(orb) == recorded['orbit_size']
    flag_sizes.append(len(orb))
    for q in orb: flag_index[q] = i
    unseen.difference_update(orb)
assert not unseen and len(flag_sizes) == 282 and len(flag_index) == 77616

coef = [Fraction(0)] * 282
used = set()
for r in cert['flag_coefficients']:
    i = r['index']
    assert i not in used and 0 <= i < 282
    used.add(i)
    coef[i] = Fraction(r['coefficient'])
cuts = [(r['color'], r['vector'], Fraction(r['coefficient'])) for r in cert['PSD_cuts']]
assert len(used) == 185 and len(cuts) == 1
for e, v, b in cuts:
    assert 0 <= e < 6 and len(v) == 36 and all(type(x) is int for x in v) and b >= 0
assert Fraction(cert['gap']) == 1
LCD = lcm(*(a.denominator for a in coef), *(b.denominator for _, _, b in cuts))
ci = [int(a * LCD) for a in coef]
cut_ints = [(e, v, int(b * LCD)) for e, v, b in cuts]
raw_flags = {}
for p in all4:
    local = [ci[flag_index[p + (d,)]] for d in range(6)]
    total = sum(local)
    raw_flags[p] = [6 * x - total for x in local]

# The integer code checks disjoint orbits without retaining millions of tuples.
def encode(p):
    a = 0
    for x in p: a = 6 * a + x
    return a


seen_codes = set()
todo_seeds = seeds.copy()
results = []
start = time.monotonic()
for j, row in enumerate(census['k5_orbits']):
    p = tuple(row['pattern'])
    assert len(p) == 10 and ok(p, T5)
    orb = {tuple(cp[p[i]] for i in a) for cp in autos for a in A5}
    assert len(orb) == row['orbit_size'] and min(orb) == p
    codes = {encode(q) for q in orb}
    assert not seen_codes.intersection(codes)
    seen_codes.update(codes)
    covered = seeds.intersection(orb)
    assert covered and len(covered) == row['seed_count']
    assert covered <= todo_seeds
    todo_seeds.difference_update(covered)
    value = 0
    for q in orb:
        k = tuple(q[i] for i in base)
        # Every labeled orbit outcome is evaluated, not just representatives.
        raw = raw_flags[k][q[3]]
        for e, v, b in cut_ints:
            if q[0] == e:
                raw -= b * v[6 * q[1] + q[4]] * v[6 * q[2] + q[5]]
        value += raw
    assert value >= len(orb) * LCD, (j, p, Fraction(value, len(orb) * LCD))
    results.append(Fraction(value, len(orb) * LCD))
    if (j + 1) % 100 == 0:
        print(json.dumps({'orbits_checked': j + 1, 'labeled': len(seen_codes),
                          'seconds': time.monotonic() - start}), flush=True)
assert not todo_seeds
assert len(results) == 551 and len(seen_codes) == 2607696
A = sum(abs(a) for a in coef)
D = sum(b * max(abs(x) for x in v) ** 2 for _, v, b in cuts)
threshold = (18 * A + D + 3) / 6
t_min = threshold.numerator // threshold.denominator + 1
assert 6 * t_min + 1 > 18 * A + D + 4
out = {'certificate': 'independent-full-K5-dual-audit',
       'input_sha256': hashlib.sha256(cert_bytes).hexdigest(),
       'census_sha256': hashlib.sha256(census_bytes).hexdigest(),
       'k4_patterns': 12936, 'k4_orbits': 25, 'seeds': 5306,
       'rooted_flags': 77616, 'rooted_flag_orbits': 282,
       'k5_orbits': 551, 'raw_labeled_patterns_checked': len(seen_codes),
       'minimum_group_average': str(min(results)), 'maximum_group_average': str(max(results)),
       'A': str(A), 'D': str(D), 'global_B_t_sufficient': t_min,
       'scope': 'global family242467 only; not ClassA or full original811'}
path = HERE / 'full-k5-psd-dual-independent-audit.json'
path.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out), flush=True)
