# Independent final synthesis audit: only Class A remains

September 11, 2026. Read `SINGLE-RESIDUAL-FAMILY.md` in full, together with
its frozen `TARGET.md`, `GLOBAL-COMPLEMENT-FREE-REDUCTION.md`, and the cited
Class A finite-relaxation scope statement. The new B certificate and its
finite bridge were independently audited separately in
`FULL-K5-PSD-DUAL-INDEPENDENT-AUDIT.md`. No new solver was used here.

## Large-original-model implication: PASS

The synthesis states an implication about **every original graph** satisfying
the hypotheses, not a six-part template assumption: if t>=629137, every
vertex of K_(6t+1) has exactly t incident edges of each of six colors, and
there is no rainbow pair of vertex-disjoint triangles, then its entire
rainbow palette support can be color-relabelled into Class A.

The previous global-support reduction uses the same hypotheses and supplies
Class A or family242467 at t>=629137. The new independently checked B
certificate excludes global family242467 at t>=7589. Since the first
threshold is larger, the synthesis follows. No balance condition is imposed
on a vertex-deleted graph, no exceptional set remains in the conclusion,
and no classification of all graphons or block decompositions is assumed.

A direct enumeration of all 720 color permutations additionally verifies
that the displayed ten palettes

    012 013 015 024 034 035 123 134 145 235

have mask173483 and canonical mask88663; they are complement-free. Thus the
displayed labeling and canonical name are consistent.

## All-orders B corollary: PASS

Assume a finite exactly balanced coloring with globally B support exists for
an integer t>0, on q=6t+1 vertices. Then q>=7, so q>1. The trivial t=0,
one-vertex case is correctly excluded from the corollary.

For an integer k>=1, use vertex set V^k. Color the edge between two distinct
tuples by the base color at their first differing coordinate. This defines
a unique color on every edge of a finite simple complete graph: distinct
tuples always have such a coordinate, and symmetry follows from symmetry
of the base edge-coloring.

For a fixed tuple and color c, the neighbors whose first differing
coordinate is j have t choices in that coordinate, q^(k-j) arbitrary
suffixes, and a forced common prefix. These cases are disjoint, so the
color degree is

    t * sum_{j=1}^k q^(k-j)
      = t*(q^k-1)/(q-1)
      = (q^k-1)/6.

This is an integer, as is also clear from the sum. All six colors have
the same exact degree at every tuple. The number of vertices is exactly
six times that new parameter plus one. No limiting approximation is involved.

For three distinct tuples, take the first coordinate where they are not
all equal. If all three coordinates differ there, their triangle colors
are exactly those of a base triangle. If exactly two coordinate values
occur there, the two cross edges have the same color, making the triangle
nonrainbow regardless of the third edge. Equivalently one may recursively
pass through common outer blocks. Hence every rainbow palette in the power
already occurs in the base. In particular the powers remain globally B.

Since q>1, the new parameter eventually exceeds7589, contradicting the B
case exclusion. An optional entirely finite simplification is available:
the **sixth power always suffices**, because

    (q^6-1)/6 >= (7^6-1)/6 =19608 >=7589.

The proof does not require t even as an extra hypothesis. If t is odd no
original balanced coloring exists by the handshake lemma; the conditional
amplification argument remains valid without splitting that vacuous case.

Thus the all-orders corollary really excludes every **nontrivial** finite
exactly balanced graph with globally family242467 support, not only those
above the computed threshold.

## Credit, outstanding scope, and final status: PASS

`TARGET.md` credits the public working report's sufficient finite
complement-free construction target and lexicographic amplification work.
The synthesis expressly retains that prior-work credit and identifies the
new ingredient as the full K5 B-family exclusion, not the standard product
observation. Nothing in this audit upgrades the historical original-source
gate: TARGET still transparently records that the original 1993 PDF was not
read, with the independently posed question quoted in a later primary paper.

A finite exactly balanced Class A example would be a genuine whole-target
counterexample mechanism: its complement-free palette support is preserved
by lexicographic powers, so arbitrarily large parameters would avoid rainbow
2K3. No such example has been constructed. Conversely a sufficiently-large
Class A exclusion, combined with this reduction, would prove the original
eventual assertion. No such exclusion is supplied by this synthesis.

The mentioned positive Class A K4 laws are consistently identified as
relaxations, not graphs or higher-order compatible laws. The synthesis does
not claim a full original solution, complete Lean formalization, remote
publication, or external verification. Its final list of outstanding human,
Lean, semantic, and novelty obligations correctly remains open.
