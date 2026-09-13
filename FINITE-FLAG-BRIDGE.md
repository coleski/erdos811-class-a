# Finite counting bridge from a four-vertex certificate to the original #811 part

11 September2026. This is a precise CONDITIONAL route to the full target.
The required certificates have NOT been found. No solution is claimed.

Let n=6t+1>=4 and let every vertex of K_n have exactlyt neighbors in each
of six colors. Suppose there is no rainbow copy of two vertex-disjoint
triangles using all six colors. A rainbow triangle palette is its three
edge colors, an unordered3subset of {0,...,5}.

## 1. At most360/n of the four-vertex sets violate one palette family

The twenty palettes form ten complementary pairs {P,P^c}. For each pair
choose one rare palette as follows. If one palette has no triangle, choose
it. Otherwise fix one triangle of paletteP. Every triangle of paletteP^c
meets its three vertices, since a disjoint one would be a forbidden rainbow
2K3. Thus P^c has at most3*binom(n-1,2) triangles; choose P^c as rare.

Choose the other palette in each pair as allowed. This gives a ten-element
complement-free family S. There are at most

    30*binom(n-1,2) =15(n-1)(n-2)

triangles with rare rainbow palettes. A four-vertex set is bad if at least
one of its four triangles has a rare palette. Counting its contained rare
triangles gives at most15(n-1)(n-2)(n-3) bad four-vertex sets. Therefore the
bad fraction delta obeys

    delta <=360/n.

Nonrainbow triangles are unrestricted. Every good four-vertex set has all
its rainbow triangle palettes in S. `palette-orbits.py` enumerates all1024
maximal complement-free families and verifies that they form13 color-
permutation orbits. It is enough to supply one certificate for each orbit.
This is an exact finite reduction; no removal lemma or limit interchange.

## 2. Exact rooted balance identities, with controlled finite-order error

Sample four distinct ordered vertices(v1,v2,v3,v4) uniformly. Let tau be a
specified ordered triple of colors on edges12,13,23, and let d be a color.
Write P(tau,d) for the probability of this triangle pattern and color14=d;
write P(tau) for the triangle-pattern probability. Put

    s_d(tau)=1_(tau12=d)+1_(tau13=d), in {0,1,2}.

For every fixed ordered triangle of patterntau, there are exactly
t-s_d(tau) choices of v4 outside its three vertices with color14=d. Hence

    (n-3) P(tau,d) = (t-s_d(tau)) P(tau),
    6P(tau,d)-P(tau)
      = (2-6s_d(tau))/(n-3) * P(tau).

In particular the absolute value of each identity's left side is at most
10/(n-3). This follows from exact per-VERTEX color balance, not merely global
edge counts. The triangle law on an arbitrary probability space need not
satisfy the corresponding four-vertex consistency conditions.

## 3. What exact certificate would finish the full positive answer

For each one of the thirteen S representatives, seek rational coefficients
a_(tau,d). For an ordered six-edge coloringK of four vertices first define

    F_(tau,d)(K)=6*1_(K123=tau and K14=d)-1_(K123=tau),
    barF_(tau,d)(K)=(1/24) sum_(pi in S4) F_(tau,d)(K relabeled by pi),
    g(K)=sum_(tau,d) a_(tau,d)*barF_(tau,d)(K).

This EXPLICIT normalized vertex average matches an LP on exchangeable
four-vertex orbit masses. One may additionally average over a specified
color-automorphism group of S, again with normalization by its order. Each
averaged flag must be defined by its exact finite sum in the certificate.

Require g(K)>=1 for EVERY K all of whose rainbow triangle palettes belong
toS. There are at most6^6 patterns, so these inequalities can be verified
exactly. The graph's sampling is vertex-exchangeable, so the expectation
bound from Section2 applies to each normalized averaged flag as well. Let

    A=sum_(tau,d)|a_(tau,d)|,
    B=max(0, max_(all K)(-g(K))).

For the actual graph coloring, the exact identities above give

    |E g| <=10A/(n-3).

The good/bad partition independently gives

    E g >=1-(1+B)delta >=1-360(1+B)/n.

Thus no counterexample can exist when both n>720(1+B) and n>20A+3.
Taking the maximum threshold over the thirteen finite certificates would
prove the original assertion for all sufficiently larget. Color relabeling
does not change balance or the forbidden configuration.

The as-yet-unproved obligation is EXISTENCE of these coefficients for all
thirteen families (or another argument handling surviving families). A
floating-point infeasibility report is insufficient; coefficients and every
inequality need exact verification, then formal proof of this bridge. A
feasible four-vertex distribution would refute this particular certificate
mechanism for its family, not construct a balanced graph counterexample.

## 4. Stronger four-vertex constraints: rooted-pair variance

The balance-only test has a feasible family11455, so Section3 alone does
NOT finish the question. A genuinely stronger test remains on four vertices.

Fix a root-edge color e and a rational function v on the36 ordered color
pairs. Define

    Q_(e,v)(K)=1_(color12=e)
      *v(color13,color23)*v(color14,color24).

Let M=max|v|. For any fixed ordered root pair(x,y), put
f(z)=v(color(x,z),color(y,z)) for the N=n-2 other vertices. Then

    sum_(z != w) f(z)f(w) = (sum_z f(z))^2 - sum_z f(z)^2 >= -N M^2.

Divide by N(N-1), multiply by the root-edge indicator, and average over
root pairs. This proves the exact finite bound

    E Q_(e,v) >= -M^2/(n-3).

Normalized vertex and permitted color-group averages preserve this bound.
In the limiting relaxation the36-by36 type-pair matrix for each root-edge
color must consequently be positive semidefinite. A proposed local law
with a negative rational quadratic form violates a necessary graph condition.
Even tests v=unit_r-unit_s give useful linear inequalities for an LP.

To extend the certificate, take explicitly normalized averaged flags and
variance functions, and seek

    g(K)=sum a*barF(K) - sum b*barQ(K) >=1

on every allowed pattern, with rational b>=0. If A=sum|a| and
D=sum b*(max|v|)^2, then

    E g <=(10A+D)/(n-3).

The same good/bad lower bound applies. The contradiction thresholds become
n>720(1+B) and n>2(10A+D)+3. The signs matter: nonnegative variance
coefficients are SUBTRACTED in g. No PSD solver's numerical acceptance is
a proof; every stencil vector, coefficient, and pattern inequality must be
rational and independently checked.

This section is a new proposed mechanism, not a claim that certificates
including these constraints exist for every family. The finite sum-of-
squares identity supplies its full error bound without any graph-limit
assumption or unproved extension of a local distribution.
