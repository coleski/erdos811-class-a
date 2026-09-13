# Independent exact audit of the nine-family PSD certificate

11 September 2026. PASS. This verifies a finite certificate and its finite-graph
consequence, not a complete solution of Erdős #811. No Lean kernel verification
of these new certificate inequalities has been performed by this audit.

## Artifact and independently authored check

Certificate: `k4-242466-psd-dual.json`.

SHA256:
`ea730873c62e423a4195a3b334f74cd6d5660be14e1ffe87aba35e97ca1c6322`.

The auditor read the entire producer `k4-psd.py`, its setup module `k4-law.py`,
and the separately written `verify-psd-dual-independent.py`. Then the auditor
wrote and ran a NEW checker, `audit-nineface-psd.py`, importing none of those
modules. It evaluates the unsymmetrized functional on every labeled pattern,
then averages the VALUES over all six color automorphisms and all 24 vertex
permutations. It does not trust the producer's 147-orbit inequalities or a
floating optimization result.

The exact integer/rational expansion checked all 46656 edge colorings of a
labeled four-vertex complete graph. Of these, 11358 have all rainbow triangle
palettes in mask 242466. All satisfy the certified inequality. The certificate
contains 66 flag coefficients and eight PSD cuts; all eight PSD coefficients
are nonnegative. The integer cut vectors each have 36 entries.

## Functional and normalization

For an ordered quadruple of distinct vertices `1,2,3,4`, a flag indexed by
`f=(a,b,c,d)` is

```
F_f = 6 1_(col12=a,col13=b,col23=c,col14=d)
        - 1_(col12=a,col13=b,col23=c).
```

A cut with root color `e` and vector `v` indexed by ordered color pairs is

```
Q_(e,v) = 1_(col12=e) v(col13,col23) v(col14,col24).
```

Bars denote UNIFORM averages over `Aut(family) x S4`, of size `6*24=144`.
Stabilizers are retained: this is not a sum over distinct images. The
certificate means

```
g = sum_f a_f bar(F_f) - sum_j b_j bar(Q_j),    b_j >= 0.
```

The independent checker found

```
min(g on allowed patterns) = 1,
min(g on ALL patterns) = -B,

B = 165935746784616540459756 / 217511277264133000865,
A := sum_f |a_f|
  = 99105232761143253014623713 / 870045109056532003460,
K := sum_j b_j ||v_j||_infinity^2
  = 408188186312417039449377 / 87004510905653200346.
```

The edge-order mapping was checked explicitly. In lexicographic order
`01,02,03,12,13,23`, a pattern `(a,b,c,d,e,f)` contributes flag coordinates
`(a,b,d,c)` and root-extension coordinates `(a; (b,d),(c,e))`. Thus neither
the ordered triangle colors nor the two extension vertices are interchanged
accidentally.

## Finite balance error: no limiting substitution

Let the FULL graph have `n=6t+1` vertices and degree exactly `t` in every
color. Sample an ordered quadruple of distinct vertices uniformly.

Condition on the first three vertices having the specified flag triangle.
Let `k_d` be the number, zero through two, of the two edges from vertex 1
inside that triangle having color `d`. Exactly `t-k_d` choices for vertex 4
have the required extension color, among `n-3` possible vertices. Therefore

```
E F_f = (2-6k_d)/(n-3) * P(specified triangle),
|E F_f| <= 10/(n-3).
```

Every relabeled flag has the same bound, so uniform symmetrization preserves it.

For the PSD term, condition on the first two vertices. Write `N=n-2` and
`u_z=v(col1z,col2z)` for the `N` remaining vertices. Sampling distinct
vertices 3 and 4 gives

```
E[u_3 u_4 | vertices 1,2]
  = ((sum_z u_z)^2 - sum_z u_z^2)/(N(N-1))
  >= -||v||_infinity^2/(N-1)
   = -||v||_infinity^2/(n-3).
```

Multiplying by the root-color indicator cannot worsen this uniform lower
bound. Color and vertex averaging again preserves it. Consequently

```
E g <= (10A+K)/(n-3).                                  (1)
```

This is a finite sampling-without-replacement estimate. It does NOT assume
that the finite extension matrix is positive semidefinite without correction.

## Excluding a nine-family after at most six deletions

Suppose there is a set `R` of at most six vertices such that every rainbow
triangle outside `R` belongs to the certificate family, up to color relabeling.
A random ordered quadruple meets `R` with probability at most `24/n`. If
it avoids `R`, its pattern is allowed and has `g>=1`; otherwise `g>=-B`.
Thus

```
E g >= 1 - 24(1+B)/n.                                  (2)
```

The bounds (1),(2) contradict one another whenever

```
n > 48(1+B),
n > 2(10A+K)+3.
```

The larger exact right-hand side is

```
99513551454222028533873609 / 43502255452826600173.
```

Therefore the integer threshold `n>=2287550` suffices; for `n=6t+1`, the
sufficient integer threshold is `t>=381259`. These calculations use exact
rational comparisons, not rounded floating bounds.

## Connection to the exceptional complementary pair

The eleven-envelope reduction gives, after relabeling, the full support inside

```
{012,013,015,024,034,035,123,134,145,235,245}.
```

If both central palettes `013,245` occur, choose one triangle of each and
delete their union, at most six vertices. No remaining triangle can have
either central palette: it would be disjoint from the chosen complementary
triangle, contrary to the original no-rainbow-`2K3` assumption. All remaining
palettes therefore lie in

```
{012,015,024,034,035,123,134,145,235}.
```

The explicit color permutation `(3,4,1,5,0,2)` sends this nine-set to the
certificate family, mask 242466. This equality was independently checked.
Deleting triangles that intersect is harmless; their union is still at most
six vertices, and every remaining triangle is disjoint from EACH chosen one.

The previously established envelope threshold is `t>=629137`. It is larger
than `381259`, so no new increase is needed. At that same threshold,
the only possible complementary pair cannot have both members present.
Thus a hypothetical original counterexample has globally complement-free
rainbow-palette support. Applying the existing global palette restrictions
leaves only global Class A or orbit 242467.

## Audit boundary

The last paragraph depends on the prior envelope theorem and its separately
audited robust coarsening and rational-dual ingredients. The NEW certificate,
normalization, finite expectation inequalities, deletion-six step, mask
relabeling, and threshold comparison were all independently checked here.

Global Class A and global 242467 colorings remain to be excluded or realized.
This is not a proof of the full original two-triangle problem, and no
publication or external-acceptance claim is made.
