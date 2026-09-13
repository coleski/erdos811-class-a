# Independent finite-bridge audit of the full K5 family242467 certificate

11 September2026. **PASS of normalization, finite sampling argument, and exact
threshold arithmetic.** This audit does not duplicate the other agents' raw
2,607,696-pattern inequality check. Its conclusion uses that separately
verified pointwise inequality; existence of a JSON file alone is not a proof.

Inspected in full: `FULL-K5-FINITE-CERTIFICATE-BRIDGE.md`,
`FULL-K5-CENSUS-AND-BALANCE.md`, `full-k5-242467-census.py`,
`full-k5-242467-psd-gate.py`, `recover-full-k5-242467-psd-dual.py`, and the
actual coefficients/normalization in `full-k5-242467-psd-dual.json`.

## Actual normalization matches the stated inequality

The certificate has185 distinct rooted-flag-class coefficients and one
nonnegative root-edge PSD coefficient, with gap1. A flag class is an orbit
under the60 family color automorphisms and the six permutations of vertices
1,2,3 fixing root0; it is **not** quotiented by a root-moving permutation.

For a class r, define D_r(q)={d:(q,d) belongs to r}. Summing the individual
labeled balance flags in the class gives exactly

```
F_r(K)=6 1((q(K),c04(K)) belongs to r)-|D_r(q(K))|.
```

The census stores the SUM of this expression over each full K5 orbit, not
its mean. The recovered dual's right side is that K5 orbit's size. Thus
division by the orbit size gives the claimed gap1 for the averaged functional.
The flag coefficient does not multiply an extra flag-orbit size afterward.

For the PSD cut, the recovery computes its sum on each K4 orbit, then
multiplies by the K5 census's number of extensions of each individual K4
pattern. This is exactly the sum of Q over the full K5 orbit. Vertex4 is
ignored in Q. Dividing again by the K5 orbit size gives the required mean.

Uniform averaging over the7200 group elements (60 color automorphisms times
120 vertex permutations) equals this orbit mean, because all orbit points
have equal stabilizer multiplicity. The averaging is of the **whole
functional**, consistently for flags and PSD cut. There is no missing factor
of60,120, the number of distinct orbit points, or a rooted flag-orbit size.

## Exact finite flag error

Sample five ordered distinct vertices from an original exactly balanced
six-coloring of K_n, n=6t+1. Conditional on the whole rooted K4 pattern q,
the number of remaining root neighbors whose colors lie in D=D_r(q) is
|D|t-s_D(q), where s_D counts the three already exposed root incidences in D.
Consequently

```
E F_r = sum_q P(q) [3|D_r(q)|-6s_D(q)]/(n-4).
```

The q events are disjoint, and their probabilities sum to1. Since
0<=|D|<=6 and0<=s_D<=3, the absolute value is at most18/(n-4), regardless
of how many labeled flags lie in r. Averaging over any vertex and color
permutations preserves this bound: the original color degrees are all t.

No assumption that the finite coloring itself is invariant under those
permutations is required. Only the sampling distribution and balance are used.

## Exact finite PSD error

Conditional on the ordered root pair, define a_w=v(c0w,c1w) for each of the
N=n-2 other vertices. For two distinct uniform choices w,w',

```
E(a_w a_w') = [(sum a_w)^2-sum a_w^2]/[N(N-1)]
             >= -max_i |v_i|^2/(n-3).
```

Multiply by the indicator that the root edge has the specified color and
average. The same lower bound holds; discarding the indicator probability
makes it weaker, not invalid. The unused fifth sampled vertex leaves the
ordered four-vertex marginal unchanged. Group averaging preserves the bound.

## Exact norms and threshold

For A=sum|a_r| and D=sum b_j max|v_ji|^2, the actual certificate gives

```
A = 3361841089779744929808284322854361016202724011837172652
    /1337557910209654559642237748857853071455522271764065,

D = 8587793533057340475505796869036269613921125720944832
    /29723509115770101325383061085730068254567161594757.
```

The maximum absolute integer vector entry is3354. Thus

```
E g <=18A/(n-4)+D/(n-3)<=(18A+D)/(n-4).
```

When the **global** rainbow support lies in family242467, every sampled K5 is
allowed and the independently checked pointwise gap implies E g>=1. This is
impossible for

```
t > (18A+D+3)/6
  = 6767066999861513113513978375970189331498872159702990819
    /891705273473103039761491832571902047637014847842710.
```

Therefore **every integer t>=7589** is excluded for globally family242467
colorings. The strict inequality and the direct expectation upper bound at
t7589 are checked with exact rational arithmetic in
`audit-full-k5-finite-norms.py`; its output is
`full-k5-finite-norms-independent.json`.

Combining with the existing global-support reduction at t>=629137 leaves
**only Class A**, with no increase in that existing threshold. This does not
exclude Class A and does not prove original #811. This audit is human/exact
arithmetic verification, not a Lean kernel check or external peer review.
