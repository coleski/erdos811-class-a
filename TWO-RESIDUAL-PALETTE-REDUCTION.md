# Full #811 counterexamples reduce to two residual palette types

11 September 2026. This is a reduction of the ORIGINAL target, not a
replacement target and not a complete solution. It applies to arbitrary
balanced colorings, with no circulant, template, or global-palette assumption.

## Theorem (human proof; independent audit passed)

Let t>=629137. Suppose a six-edge-coloring of K_(6t+1) has degree exactly t
in each color at every vertex and has no two disjoint triangles whose six
edges have all six different colors.
There exist a vertex set S with |S|<=30 and a permutation of the six colors
such that every rainbow triangle in the induced graph outside S has palette
in one of the two ten-element families with masks

    88663 (Class A), or 242467.

Masks use the lexicographic ordering of the twenty triples from {0,...,5}.
No monochromatic block structure of the residual graph is asserted.

## Proof

1. Apply BOUNDED-VERTEX-COVER.md. For each complementary pair of triangle
   palettes, either forbid one absent palette, or choose one realizing
   triangle and forbid its complement outside that triangle's three vertices.
   Their union S has at most 30 vertices. All residual rainbow palettes
   belong to a maximal complement-free family F, consisting of exactly one
   palette from each complementary pair.

2. By ROBUST-114-AND-222-COARSENING.md and ROBUST-123-COARSENING.md, for
   t>=4805 EVERY three-way partition of the original colors has a rainbow
   triangle avoiding S. This uses exact original balance before deletion,
   not a claim that the residual graph remains exactly balanced. Each such
   triangle has a palette in F and meets all three color groups. Consequently
   F passes the three-way coarsening test.

3. The exact finite census in check-circulant-schur-coarsenings.py exhausts
   all 1024 maximal complement-free families and all 540 surjective maps
   from six colors to three named groups. It leaves 228 labeled families
   in four color-permutation orbits: 1023,13119,88663,242467. The combinatorial
   test has no primality assumption; that word in the script's historical
   name does not restrict this application. Root reran its exact checks.

4. Exclude 1023 and 13119 with the previously independently checked rational
   four-vertex certificates. For either family, let g be the explicitly
   normalized S4/color-automorphism average defined in FINITE-FLAG-BRIDGE.md.
   Its minimum on allowed four-vertex patterns is 1, its global minimum
   is -B, and its coefficient absolute sum is A. Exact original balance gives

       |E g| <= 10A/(n-3),       n=6t+1.

   A uniformly sampled four-vertex set is disjoint from S except with
   probability at most 4|S|/n<=120/n. Disjoint sets have all their rainbow
   palettes in F. Thus

       E g >= 1-120(1+B)/n.

   The weaker previously recorded sufficient thresholds
   n>720(1+B) and n>20A+3 therefore apply as well. For mask 1023 the constants
   are A=9889/4, B=361/32, and n>49448 suffices. For mask 13119 they are
   A=2453630/13, B=10567/13, and n>49072639/13 suffices. These values and
   all 46656 labeled four-vertex inequalities were independently verified
   in VARIANCE-AND-DUAL-INDEPENDENT-AUDIT.md. Since t>=629137 implies
   13(6t+1)>=49072699>49072639, both cases are impossible.

Only 88663 and 242467 remain, proving the stated reduction.

## What this changes, and what remains missing

Previously nine palette exclusions held only for a GLOBAL complement-free
support (or a prime circulant). Rare triangles prevented their use on the
bounded-deletion core of an arbitrary original counterexample. The robust
coarsening lemmas remove precisely that obstacle. There is no passage to a
limit and no assumption that an existence lemma gives positive density.

This still does NOT solve #811. Both residual families require further work,
including compatibility with the exceptional vertices and exact original
degrees. Class A has a genuine twelve-part balanced limiting model, so
uniform positive-gap limiting inequalities cannot exclude it. No checked
final Lean theorem or independent final correspondence audit exists.

The proof depends on classical Gallai partition structure and exact finite
censuses/certificates. Their Lean formalization and the complete final target
bridge remain obligations. No novelty or external-acceptance claim is made.
