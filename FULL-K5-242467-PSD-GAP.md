# Full K5 consistency excludes palette family 242467 asymptotically

2026-09-11. This is a complete family-specific exclusion, **not a complete
solution of original Erdős #811**. Other palette families must still be
handled by the parent proof. No graph or graphon realization is claimed.

## Exact theorem furnished by the certificate

Let G be a complete graph on n=6t+1 vertices, with its edges colored in
six colors and every vertex incident with exactly t edges of each color.
If every rainbow triangle's unordered palette belongs to

    S = {012,013,024,035,045,125,134,145,234,235},

then n < 45535. In particular no such globally supported coloring exists
for integer t>=7589. The stated threshold is deliberately conservative.

The finite argument uses only five-vertex sampling, the exact color
degrees, and a root-pair variance inequality. It does not assume a
graph-limit compactness theorem or triangle removal.

## Full finite census and completeness

`full-k5-242467-census.py` was authored by the parent. It finds551
Aut(S)×S5 orbits containing2,607,696 labeled allowed K5 patterns. The
25 K4 orbits contain12,936 labeled allowed patterns. The complete set
of77,616 labeled K4-rooted-extension flags splits into282 classes under
Aut(S) and permutations of the three non-root K4 vertices.

The independent `audit-full-k5-census.py` imports no generator code. It
directly checks all46,656 labeled K4 patterns, reconstructs the full
flag partition, expands all551 K5 orbits and verifies their disjointness,
all25 marginal columns and all282 flag columns. It also checks all
25*6^4=32,400 extensions of the K4 representatives: exactly5,306 are
allowed and every one belongs to an enumerated K5 orbit.

This last test is a completeness proof, not a heuristic search. Any
allowed K5 has a K4 face; an S4 vertex permutation and color automorphism
send that face to one of the25 representatives. Extend that permutation
by fixing the fifth vertex. The resulting K5 is among the checked
extensions. Hence the full K5 orbit containing the original pattern is
present. All sampled triangles, including those through the fifth
vertex, are checked.

Independent census owner73363, terminal exit0, PASS. Durable result:
`full-k5-census-independent-audit.json`.

## The exact positive-gap identity

Certificate: `full-k5-242467-psd-dual.json`.
SHA-256:

    d04310f203fe5b4ae7503265104a31bc62cb61951fef3023604af98418971c35

It has185 rational rooted-flag-class coefficients a_j and one nonnegative
rational PSD coefficient b with an integer36-vector v. Rooted classes
are indexed by `rooted_flag_orbits` in the census JSON.

For a labeled K5 p, edge order is12,13,14,15,23,24,25,34,35,45. Write k
for its induced ordered K4 on1234. For a rooted flag class C_j define

    F_j(p) = 6*1[(k,color15) in C_j]
             - number of d in {0,...,5} with (k,d) in C_j.

Thus a coefficient multiplies the **SUM over distinct flags in its
class**, not their average. The quadratic expression is

    Q(p) = 1[color12=0]
           *v[6*color13+color23]*v[6*color14+color24].

Let g be the uniform average of sum_j a_j F_j - bQ under all60 color
automorphisms and all120 vertex permutations of K5. The exact certificate
asserts

    g(p) >= 1

for every palette-allowed K5. Orbit averaging is correctly normalized:
each labeled element of a group orbit occurs equally often, regardless
of stabilizer size. Consequently the stored column inequality has
right side equal to the K5 orbit size, not1.

`audit-full-k5-psd-dual-columns.py` independently reconstructs the K4
quadratic coefficients and checks this inequality in rational arithmetic
on all551 columns. The minimum orbit average is exactly1. The census
columns themselves were independently reconstructed as explained above.
No numerical solver status is used in this verification.

## Finite expectation upper bound

Average the original coloring uniformly over Aut(S), then sample five
ordered distinct vertices. Vertex exchangeability makes the expectation
of the fully averaged g equal to that of its unaveraged expression.

For a fixed ordered K4 k and color d, let s_d(k) count the three edges
from its root whose colors are d. Exact balance gives

    P(k,color15=d) = (t-s_d(k))/(n-4) * P(k).

For a flag class put D_j(k)={d:(k,d) in C_j}. Summing the last equation,

    E F_j = sum_k [3|D_j(k)|-6 sum_(d in D_j(k)) s_d(k)]
                     *P(k)/(n-4).

Since |D_j(k)|<=6 and the sum of the three root incidences is at most3,
the bracket has absolute value at most18. The events k are disjoint;
no additional factor equal to the size of a flag class is introduced.
Therefore |E F_j|<=18/(n-4).

For Q, condition on the ordered root pair12. The values
v[color1z,color2z] over the remaining n-2 vertices have square of their
sum nonnegative. Sampling two distinct remaining vertices gives

    E Q >= -||v||_infinity^2/(n-3).

The color12 indicator does not worsen this bound. Let

    A = sum_j |a_j|,
    B = b*||v||_infinity^2.

The exact certificate norms are stored in
`full-k5-psd-dual-column-audit.json`. They imply

    E g <= 18A/(n-4)+B/(n-3)
         <= (18A+B)/(n-4).

But all sampled K5s are palette-allowed, so E g>=1. This is impossible
if n>18A+B+4. Exact rational evaluation gives45535 as a sufficient
integer n, proving the theorem stated above.

## Discovery versus proof

The earlier84-type projection cone is genuinely feasible together with
K4 PSD, as independently certified in `PROJECTION-SDP-ONE-SHOT-STATUS.md`.
The full K5 gate is strictly stronger because it preserves every rooted
extension balance class rather than only an active-event projection.

One bounded SCS call on the full551-orbit law and the exact16-dimensional
Gram image returned a numerical maximum margin near-0.0037257992.
Owner2352 reached terminal exit0. That output was only discovery.

The two positive eigen-directions of the numerical PSD dual were lifted
to integer36-vectors. One exact Farkas recovery with a subset of valid
rooted rows yielded the certificate above; only one quadratic direction
was required in the final certificate. Selecting rows numerically does
not assume the numerical rank is exact: the recovered rational identity
was checked against all551 columns. Owner73354, terminal exit0,
approximately72.77 seconds for rational recovery.

The complete scripts and logs are
`full-k5-242467-psd-gate.py`, `full-k5-242467-psd-gate.log`, and
`recover-full-k5-242467-psd-dual.py`. Every process is terminal.

## Reproduction of exact checks

    python3 audit-full-k5-census.py
    python3 audit-full-k5-psd-dual-columns.py

These are certificate checks. Running a discovery solver is unnecessary.
The number-theory agent's additional independent raw-pattern replay is
now complete: `audit-full-k5-psd-dual-independent.py` checks all2,607,696
labeled patterns and obtains minimum group average1, matching norms and
the threshold t>=7589. Its result is
`full-k5-psd-dual-independent-audit.json`. The parent also independently
passed its separate column replay, `root-full-k5-dual-check.json`.
