# Erdős #811: the original two-triangle question

Selected 11 September 2026 from fresh public sources, not local archives.

## Frozen original part

Is there an integer T such that, for every integer t>=T and every coloring
c:E(K_(6t+1))-> {0,1,2,3,4,5} in which every vertex has exactly t neighbors
of each color, there are six distinct vertices a,b,c,d,e,f such that the
six edges ab,bc,ca,de,ef,fd have six distinct colors?

Equivalently: does every sufficiently large balanced six-coloring contain
a rainbow copy of 2K3? The copy is not induced: cross edges are unrestricted.
Odd t permits no such coloring, by the handshake lemma, but even t is not
an added hypothesis. A negative answer requires arbitrarily large t, not
one finite base unless a valid amplification is proved.

This is an independently posed original part, not the entire classification
asked in #811 and not the already-disproved K4 part. Clemen--Wagner's primary
paper explicitly quotes Erdős--Tuza 1993 naming K4, C6, and 2K3 separately:
https://arxiv.org/html/2303.15476v1 (Introduction, paragraph before Theorem1.2).
Original bibliographic record and abstract:
https://doi.org/10.1016/S0167-5060(08)70377-7
P. Erdős and Z. Tuza, Rainbow Subgraphs in Edge-Colorings of Complete Graphs,
Annals of Discrete Mathematics55(1993),81--88.
The original full PDF has not yet been located/read; its precise historical
quotation is verified in the primary2023 paper, not inferred from a forum.

## Current claim gate

- https://www.erdosproblems.com/811 and its ordinary thread and proof-claims
  pages fetched today: OPEN, one ordinary comment identifying the known K4
  disproof, zero proof claims. No full two-triangle claim visible.
- https://arxiv.org/html/2303.15476v1 is a full primary K4 disproof; it does
  not settle 2K3 or C6. The full short mathematical text was read.
- https://www.erdosproblemaday.com/report/811 (27July2026), read completely,
  labels its work PARTIAL. It has a triangle-count identity, forest/triangle
  positive cases, proof lexicographic squares always contain rainbowC6,
  and a valid sufficient finite 2K3 construction target: no complementary
  rainbow-triangle palettes. Its K13 searches do not give a construction.
  We will not repeat those searches or claim its reductions as new.
- Targeted GitHub searches returned community tracking and unrelated
  formalization-metadata issues, not a complete proof of this part.
- Jig search found OpenE811 for the C6 question on its index; no indexed
  2K3 resolution found. Direct homepage text did not expose the card link.
  This is limited absence evidence, not an exhaustive Jig audit.

Earlier freshly inspected choices were rejected: #1040 capacity-one has
September full claims; #1041 has September degree7 disproof endorsed in its
ordinary thread; #1120 has arXiv2606.19178 divergence claim; #906 has April
and July full transcendental-function claims; #1045 regular-polygon part is
already false for even orders; #1038 has current full claims and intensive
existing analysis. No work on those was promoted as new.

## First new mathematical check

Test the exact triangle-color probability constraints implied by balance,
against all complement-free subsets of the twenty rainbow palettes. For
each unordered three-color multiset, use a nonnegative triangle density.
Each equal-color wedge has asymptotic probability1/36; each unordered
distinct-color wedge1/18. Can these identities alone force two complementary
palettes with positive density? If yes, finite-dimensional separation may
give a full large-order theorem, since positive-density complementary
triangles contain a disjoint pair. If feasible, exhibit an exact rational
abstract triangle law and retire this counting mechanism. Such a law is NOT
a graph construction and does not disprove the original question.

No resolution or new theorem is claimed here. No external publication made.
