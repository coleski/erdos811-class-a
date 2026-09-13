# Large original counterexamples have globally complement-free support

Root synthesis, 11 September 2026. A theorem about the ORIGINAL #811 model,
but NOT a proof that such counterexamples do not exist.

The new certificate/deletion-six/threshold bridge passed independent audit
in NINE-FAMILY-PSD-INDEPENDENT-AUDIT.md; its earlier robust and residual
dependencies have separate audits cited below. Root reran both independently
written full-pattern certificate checkers and the exact threshold checker.

## Statement

For t>=629137, every exactly balanced six-coloring of K_(6t+1) with no two
vertex-disjoint triangles whose six edges have different colors has its
ENTIRE rainbow-triangle palette support contained, after a color relabeling,
in either family88663 (Class A) or family242467. In particular no two
complementary rainbow palettes occur anywhere in such a coloring.

This implication explicitly assumes the global absence of every rainbow
2K3. It does NOT assert the false statement that any two complementary
palettes occurring in an arbitrary balanced graph have disjoint realizers.

## 1. The eleven-palette envelope

TWO-RESIDUAL-PALETTE-REDUCTION.md supplies an exceptional set of size at
most30, with residual palettes in one of these two families. Its complete
independent audit, including the exact original-graph finite errors and
threshold, is TWO-RESIDUAL-REDUCTION-INDEPENDENT-AUDIT.md.

MANDATORY-PALETTE-COARSENINGS.md upgrades this to a GLOBAL envelope. In
Class A, nine palettes are unique witnesses of individual coarsenings; a
triangle of any of their complements would contradict robust coarsening
after deleting itself and the exceptional set (at most33 vertices). In
family242467 every pair of palettes is exactly the witness set of a
coarsening. Two distinct globally occurring outside palettes would similarly
contradict robustness after deleting their chosen triangles and the
exceptional set (at most36 vertices). All required thresholds are at most
6845, below the present629137.

Thus after relabeling all global palettes lie in

    E={012,013,015,024,034,035,123,134,145,235,245}.

This envelope has exactly one complementary pair, 013 and245. Removing013
from E gives family242467; removing245 gives Class A. These identifications
are finite relabeling identities, not assumptions about the graph.

## 2. If both central palettes occur, a nine-palette deletion remains

Suppose triangles of both013 and245 occur. Choose one of each and delete
their vertices, obtaining a set Z of size at most6. Every013 triangle meets
the chosen245 triangle, and conversely: otherwise there would be a rainbow
2K3. Hence outside Z all rainbow palettes lie in

    E\{013,245}={012,015,024,034,035,123,134,145,235}.

This is a relabeling of mask242466, obtained by deleting one palette from
242467. The exact certificate uses242466; its canonical mask is88662.

## 3. Exact positive-gap certificate excludes that deletion

`k4-242466-psd-dual.json` supplies rational coefficients for

    g(K) = sum a*averaged_rooted_balance_flag(K)
           - sum b*averaged_root_pair_quadratic(K),    b>=0.

The averages are explicitly uniform over all24 vertex permutations and
all6 automorphisms of the nine-palette family. The definitions and original
finite sampling bounds are FINITE-FLAG-BRIDGE.md, Sections2--4. All66 flag
coefficients and8 integer-vector PSD cuts are part of the certificate.

Root read the standalone verifier and independently ran it. It checked
EVERY one of46656 labeled K4 patterns with rational/integer arithmetic:
there are11358 allowed patterns and g>=1 on every one. Globally g>=-B.
The exact coefficient norms are

    A = 99105232761143253014623713 / 870045109056532003460,
    D = 408188186312417039449377 / 87004510905653200346,
    B = 165935746784616540459756 / 217511277264133000865.

Here A=sum|a| and D=sum b*(max|v|)^2. On a uniformly sampled ordered set
of four DISTINCT vertices of the ORIGINAL balanced graph, the exact degree
identities and finite variance inequality give

    E g <= (10A+D)/(n-3),      n=6t+1.

The sample hits Z with probability at most4|Z|/n<=24/n. Otherwise all its
rainbow palettes belong to the nine-family and g>=1. Therefore

    E g >= 1-24(1+B)/n.

No exact balance of the graph after deletion is assumed. Sufficient strict
contradiction thresholds are

    n > 48(1+B),       n > 2(10A+D)+3.

Both hold for every n>=3774823, the order at t=629137. These comparisons
are recorded as exact rational assertions in verify-global-reduction-bounds.py.
The lower expectation is greater than1/2 and the upper less than1/2.

Thus both central palettes cannot occur. The entire support is globally
contained in Class A or242467, and is complement-free, as asserted.

## Remaining obligation — unchanged original target

We have NOT excluded exactly balanced colorings with globally complement-free
Class A or242467 support, nor constructed one. Those are now the remaining
counterexample possibilities. An admissible finite example would amplify;
a universal exclusion would prove the original eventual assertion. Neither
exists in this work yet. The exact rational full242467 K4+PSD law is only
an abstract relaxation, not a graph.

The finite pattern certificate and the human bridge are not a Lean proof.
Formalization of Gallai, the graph/certificate bridge, the final theorem,
and the final independent correspondence audit remain unfinished.
