# Only Class A remains for the original two-triangle question

11 September2026. This is a theorem about the ORIGINAL model, not a
restriction imposed on that model. It is still a reduction, not a solution
of Erdős #811's independently posed rainbow-two-triangle question.

## Theorem

Let t>=629137, and let the edges of K_(6t+1) be colored in six colors,
with every vertex having exactly t neighbors in each color. If there are
no two vertex-disjoint triangles whose six edges have six different colors,
then, after a permutation of the color names, EVERY rainbow triangle has
one of the following ten palettes:

    012,013,015,024,034,035,123,134,145,235.

This is Class A (canonical mask88663; the displayed labeling has
mask173483). The conclusion concerns the entire graph, without an
exceptional vertex set and without an assumed block decomposition.

## Proof

GLOBAL-COMPLEMENT-FREE-REDUCTION.md, with its cited independent audits,
proves that every graph under these assumptions has its entire rainbow
support in Class A or in family242467, after relabeling. Its threshold is
t>=629137 and includes the exact finite errors in every earlier reduction.

FULL-K5-242467-PSD-GAP.md excludes the latter family for every t>=7589.
The exact certificate has185 rooted-flag-class coefficients and one
nonnegative quadratic coefficient. Its gap is at least1 on every allowed
K5 after uniform group averaging. The independent raw-pattern check
reconstructs all551 orbits and evaluates all2607696 labeled patterns;
the minimum average is exactly1. The separate finite bridge bounds the
expectation by18A/(n-4)+D/(n-3)<1 at the stated threshold, a contradiction.

Since629137>=7589, only Class A remains. This establishes the theorem.

## Verification evidence

- Certificate: full-k5-242467-psd-dual.json, SHA256
  d04310f203fe5b4ae7503265104a31bc62cb61951fef3023604af98418971c35.
- Independent raw-pattern check: audit-full-k5-psd-dual-independent.py;
  result full-k5-psd-dual-independent-audit.json.
- Independent normalization/sampling audit:
  FULL-K5-FINITE-BRIDGE-INDEPENDENT-AUDIT.md.
- Root independently reconstructed the K4 quadratic columns and checked
  all551 rational orbit inequalities and exact thresholds:
  root-check-full-k5-dual.py / root-full-k5-dual-check.json.
- Root also read and replayed the separately implemented full census
  verifier, including all32400 canonical-face extensions and every
  marginal/flag column (owner39408 terminal exit0 PASS).

These are human proofs and reproducible exact computer checks. They are
not a complete Lean formalization. No remote publication or verifier
acceptance is asserted.

## Stronger corollary for the excluded family

In fact no nontrivial finite exactly balanced six-coloring can have all
rainbow palettes in family242467, at ANY t>0. Suppose such a coloring
exists on q=6t+1>1 vertices. Its k-fold lexicographic power has q^k
vertices and color degree (q^k-1)/6 at every vertex. An edge is colored
by the first coordinate at which its endpoints differ.

For a triangle in a lexicographic product, either all three vertices are
in one outer block, all are in distinct outer blocks, or exactly two are
in one block. In the third case two edges have the same color; in the
other cases any rainbow palette is a palette of one factor. Thus every
power still has all rainbow palettes in242467. In fact the sixth power
already suffices: q>=7 gives (q^6-1)/6>=19608>7589, contradicting the
family exclusion. The standard lexicographic amplification observation
is prior public work, already credited in TARGET.md; the newly verified
ingredient is the full K5 family exclusion.

## Exact unresolved obligation

Neither a finite exactly balanced Class A example nor a universal
exclusion of Class A has been proved. An admissible Class A example would
amplify and disprove the original eventual assertion. Excluding every
sufficiently large Class A coloring would prove it. Neither is supplied
by this reduction.

CLASS-A-FINITE-K4-PSD-LIFT.md now shows that exact finite four-vertex
balance and all root-edge variance constraints are insufficient: those
relaxations have strictly positive feasible laws for every sufficiently
large parameter. This does not construct a graph. Work on Class A must
use additional compatibility, higher-order information, or structure.

The original task remains UNSOLVED. The final human solution, exact final
Lean theorem/bridge, clean pinned build, independent final meaning audit,
and final novelty gate are still outstanding.
