# Independent audit of the two-residual-palette reduction

11 September 2026. Auditor: original_number_theory. Verdict: PASS for the
human reduction in `TWO-RESIDUAL-PALETTE-REDUCTION.md`, with "rainbow pair"
interpreted as two vertex-disjoint triangles whose SIX edges use all six
colors. Spelling out that interpretation in the theorem avoids ambiguity.

This audit is not a full solution of original #811 and does not certify a
complete Lean proof or any unprovided certificate for the two survivors.

## Material inspected and rerun

Read the complete reduction, `FINITE-FLAG-BRIDGE.md`, the previous
`VARIANCE-AND-DUAL-INDEPENDENT-AUDIT.md`, and the full standalone checker
`check-expanded-duals.py`. The preceding robust-coarsening and bounded-cover
steps have separately passed `ROBUST-BRIDGE-INDEPENDENT-AUDIT.md`.

Reran exactly:

    python3 check-expanded-duals.py k4-all-dual.log --masks 1023 13119

The input SHA256 remains

    b3d96b0c57f0230db1ce498d5cdd09338c3da404ab7ee58c7117c55033108f8c.

Both certificates passed every one of the 46,656 labeled four-vertex
colorings with exact integer/Fraction arithmetic. The script independently
computes the color automorphism group and explicitly normalizes its average
and the 24 vertex permutations. The verified constants are:

| Mask | Allowed minimum | Global minimum | A | B |
| --- | --- | --- | --- | --- |
| 1023 | 1 | -361/32 | 9889/4 | 361/32 |
| 13119 | 1 | -10567/13 | 2453630/13 | 10567/13 |

There are no PSD terms in these two certificates. Therefore the absolute
expectation bound for balance flags alone applies exactly as stated.

## 1. Exact original-graph expectation bound

Sample four distinct ORDERED vertices uniformly from the original graph
of order n=6t+1. Fix an ordered triangle pattern tau and root-edge color d.
For a triangle realizing tau, put s_d=1_(tau12=d)+1_(tau13=d). Of the n-3
vertices outside the triangle, exactly t-s_d extend root vertex 1 by color
d. Thus, for the indicator flag F=6*1_(tau and color14=d)-1_tau,

    E F = ((2-6s_d)/(n-3)) Pr(tau).

Since s_d lies in {0,1,2}, its absolute value is at most 10/(n-3).
The same bound holds under any vertex relabeling and color permutation;
normalized finite averages preserve it. Taking the coefficient absolute
sum A yields

    |E g| <= 10A/(n-3).

Crucially, this sample and this identity concern the ORIGINAL graph, which
is exactly color-balanced. No exact balance is asserted on V minus S.
The residual graph is used only to identify good four-vertex patterns.

## 2. Good and bad four-vertex samples

Let S be the SINGLE deletion set supplied by the cover argument. For each
fixed vertex v, a uniform four-vertex set contains v with probability 4/n.
The union bound consequently gives

    Pr(the sample meets S) <= 4|S|/n <= 120/n.

The same event probability holds for ordered sampling; it depends only on
the underlying set. A sample disjoint from S has every rainbow triangle
palette in the chosen family F, so its verified certificate value is at
least 1. On ANY other sample, including all possible forbidden patterns,
the independently checked global bound is g>=-B. Hence

    E g >= 1 - (1+B) Pr(sample meets S)
        >= 1 - 120(1+B)/n.

The proof does not assume that each palette of F is realized, that bad
sets actually contain forbidden triangles, or that a bad pattern has any
particular form. Declaring every sample meeting S bad only weakens this
lower bound. In particular there is no density or graph-limit assumption.

If F is a color permutation of a canonical mask, globally rename the
colors before applying its certificate. This preserves exact balance and
the forbidden six-color configuration, so no extra constants are needed.

## 3. Threshold audit

The old sufficient hypotheses

    n > 720(1+B),       n > 20A+3

remain valid with the stronger 120/n bound. They make the lower expectation
bound greater than 1/2 (in fact greater than 5/6 under the first condition)
and the upper bound strictly less than 1/2.

For mask 1023 their maximum is 49448. For mask 13119 their maximum is

    20*(2453630/13)+3 = 49072639/13.

At the stated t=629137, the order is n=3774823, and

    13n = 49072699 > 49072639.

Both sufficient thresholds hold, as does t>=4805 for the robust bridge.
They continue to hold for every larger t. The exact expectation bounds at
this threshold were also checked directly:

| Mask | Lower bound for E g | Upper bound for E g |
| --- | --- | --- |
| 1023 | 15093397/15099292 | 9889/1509928 |
| 13119 | 47803099/49072699 | 1226815/2453633 |

In each row the lower bound is greater than 1/2 and the upper bound is
strictly less than 1/2. All calculations used rational arithmetic. No
rounding of the strict threshold or numerical solver tolerance is involved.

Although this t happens to be odd, the theorem need not add an evenness
assumption: odd t is already impossible for an exactly t-regular color
class on an odd-order complete graph. Proving the statement for all integer
t above the threshold is valid and includes the nonvacuous even cases.

## 4. Certified scope

The robust coarsening/census reduction leaves four possible maximal
residual families. The two checked K4 certificates exclude 1023 and 13119
for every original coloring at the displayed threshold, even with up to
30 exceptional vertices. Therefore a hypothetical original counterexample
must have all its residual rainbow palettes contained, after ONE global
color permutation, in 88663 or 242467.

The family need not equal the actual residual support, and neither a
template decomposition nor restrictions on triangles touching S follow
from this particular theorem. The reduction is correctly stated as a
necessary condition on a full original counterexample, not its resolution.
