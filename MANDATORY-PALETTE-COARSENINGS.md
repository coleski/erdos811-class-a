# Mandatory palette witnesses in the two surviving families

11 September 2026. Exact finite combinatorics and conditional global consequences.
No full original-problem resolution is asserted.

## Conventions and exhaustive finite certificate

Colors are 0 through 5. A palette is an unordered three-element color set.
For a surjection `f:{0,...,5}->{0,1,2}`, define its witness set inside a
palette family `F` to be those `P in F` on which `f` is injective. There are
exactly 540 such surjections. Thus if all rainbow palettes on a vertex set
lie in `F`, a coarsened rainbow triangle has a palette in this witness set.

The standard-library checker `verify-mandatory-palette-coarsenings.py`
enumerates all 540 coarsenings, all 1024 subfamilies of each ten-palette
family, and all 720 color relabelings for each reported orbit computation.
Its `--certificates` option prints an explicit surjection for each minimal
witness set. No SAT or graph-realizability assumption is involved.

## Class A: nine singleton witnesses

Use the normalized Class A family

```
F_A = {012,013,015,024,034,035,123,134,145,235}.
```

Its raw bit mask in lexicographic triple order is 173483, and its canonical
color-permutation representative is 88663. Exactly nine palettes are unique
witnesses of some coarsening: every palette other than `013`. Explicit
surjections, displayed as `(f(0),...,f(5))`, are:

```
012 : (0,1,2,1,0,1)
015 : (0,1,0,0,1,2)
024 : (0,0,1,0,2,0)
034 : (0,1,0,1,2,1)
035 : (0,0,1,1,0,2)
123 : (0,0,1,2,0,2)
134 : (0,1,0,0,2,1)
145 : (0,0,0,0,1,2)
235 : (0,0,1,0,0,2).
```

These nine singleton sets are exactly the inclusion-minimal witness sets.
Consequently a subfamily of `F_A` meeting every coarsening witness is either
the nine-set `F_A\{013}` or all ten palettes. Replacing `013` by its complement
`245` gives orbit 242467, not one of the previously dual-excluded orbits.

In particular, the previously constructed twelve-part near-balanced model,
when relabeled into Class A, has support
`{013,015,024,035,123,145,235}`. It misses the newly mandatory `012,034,134`.
Thus it does not refute a structural theorem whose hypotheses additionally
include robust existence of all coarsening witnesses. This observation does
not prove such a structural theorem.

## Orbit 242467: every pair, no singleton

Use the canonical family

```
F_B = {012,013,024,035,045,125,134,145,234,235}.
```

There is no singleton coarsening witness. The inclusion-minimal witness
sets are exactly all 45 unordered pairs of distinct palettes in `F_B`.
Therefore its subfamilies meeting every witness are all ten palettes or any
nine of them. Flipping any one palette to its complement gives Class A,
orbit 88663.

The failure of individual mandatory palettes in this family is substantive;
one must not transfer the Class A nine-singleton argument unchanged.

## A short structural proof of all the forcing witnesses

The pair-witness property does not require exhaustive coarsening enumeration.
For each color `v`, make its link graph on the other five colors: `ab` is an
edge exactly when `vab` belongs to `F_B`. These six link graphs are cycles
of length five, with cyclic orders

```
v=0: 1,2,4,5,3       v=1: 0,2,5,4,3
v=2: 0,1,5,3,4       v=3: 0,1,4,2,5
v=4: 0,2,3,1,5       v=5: 0,3,2,1,4.
```

Let `P,Q` be any two distinct faces of `F_B`. They intersect, because two
disjoint three-subsets of six colors would be complementary, whereas `F_B`
is complement-free. Choose `v` in their intersection. They correspond to
two distinct edges of the link cycle at `v`. Deleting these two cycle edges
leaves two nonempty paths, one possibly a single vertex. Partition the six
colors into `{v}` and the vertex sets of these two paths. The only link
edges across the latter two groups are exactly the two removed edges.
Thus the only transversal palettes in `F_B` are `P,Q`.

When `|P intersect Q|=2`, this partition has group sizes 1,1,4; when their
intersection has size one, the sizes are 1,2,3. This is an explicit
construction of all 45 pair-witness coarsenings.

The same argument proves the Class A singleton assertion uniformly. Write
that family as `F_B\{P} union {complement(P)}`, after the suitable relabeling.
For every `Q!=P`, use the preceding coarsening with singleton `v in P intersect Q`.
The added palette `complement(P)` avoids `v`, so is not transversal. The
removed palette `P` is gone. Hence `Q` is the unique transversal palette in
the flipped family. These elementary cycle-link facts are all that is needed;
identifying the face complex topologically as the six-vertex triangulation
of the projective plane is not an input to the argument.

## Global complement restrictions from robust coarsening

Assume a balanced six-coloring of `K_(6t+1)` has no rainbow `2K3`. Suppose
deleting a set `S` of at most 30 vertices leaves rainbow support contained
in a specified family `F`. Use the separately proved robustness theorem:
after deleting any set of at most `r` vertices, every three-way coarsening
still has a rainbow triangle when `t>=5(r+1)^2`.

### Class A case

Let `P` be one of its nine singleton-witness palettes. If a triangle of
palette `complement(P)` occurs anywhere in the full graph, delete its three
vertices as well as `S`. Robustness at deletion size 33 supplies the unique
coarsening witness `P` on the remaining graph. It is disjoint from the first
triangle, producing a rainbow `2K3`, a contradiction.

Thus for `t>=5780`, all nine complementary palettes are globally absent.
The only possible complementary pair anywhere in the graph is `013/245`.
Its two members cannot be eliminated by the singleton-witness argument.

### Orbit 242467 case

Suppose there are two distinct palettes `Q_i,Q_j` outside `F_B` occurring
anywhere in the full graph. Since `F_B` is maximal complement-free, their
complements `P_i,P_j` are distinct members of `F_B`. Choose triangles of
palettes `Q_i,Q_j`; they may intersect. Delete both triangles and `S`, at
most 36 vertices in total. Choose a coarsening whose witness set in `F_B`
is exactly `{P_i,P_j}`. Robustness gives a triangle of one of these two
palettes on the remaining vertices. It is disjoint from the corresponding
chosen complementary triangle, a contradiction.

Therefore for `t>=6845` at most one distinct rainbow palette outside `F_B`
can occur globally. The full support is contained in `F_B` plus at most one
complementary palette. Such an eleven-palette envelope has exactly one
complementary pair. This is a reduction, not an argument excluding that pair.

## Combined eleven-palette envelope theorem

Combine the preceding deductions with the separately established
`TWO-RESIDUAL-PALETTE-REDUCTION.md`: for `t>=629137`, a hypothetical original
counterexample has a deletion set of size at most 30 whose remaining support
lies in Class A or orbit 242467. This audit read that manuscript; its rational
dual constants and prior classification checks are dependencies, not repeated
independent computations in this file.

Since `629137>6845`, in either case the FULL graph has at most one unordered
complementary pair of rainbow palettes present. More specifically, after a
color relabeling its full support is contained in the eleven-palette envelope

```
{012,013,015,024,034,035,123,134,145,235,245}.
```

For residual Class A this was proved directly above. For residual 242467 with
one additional complement, flipping the corresponding original palette gives
Class A, by the exact orbit calculation. With no additional complement its
support is already globally complement-free; it is still a subset of a
corresponding eleven-palette envelope after choosing any face to flip.

If both central palettes `013,245` occur, choose a triangle of each and delete
their vertices, at most six. On the remainder neither central palette can
occur, because such a triangle would be disjoint from its complementary
chosen triangle. Therefore all remaining rainbow palettes lie in the common
nine-set

```
{012,015,024,034,035,123,134,145,235}.
```

Its raw mask is 173481, and canonical mask 88662, under the color permutation
`(0,1,4,2,5,3)`. This deletion statement does not itself exclude coexistence;
a separate obstruction for that nine-family residual is necessary.

Update: the necessary nine-family obstruction has now been supplied by an
exact PSD certificate and independently audited in
`NINE-FAMILY-PSD-INDEPENDENT-AUDIT.md`. It excludes such a deletion-six residual
for `t>=381259`, below the combined threshold 629137. Therefore at the same
combined threshold the full support is globally complement-free. The global
Class A / 242467 alternatives themselves remain unresolved.

## Remaining gap

These results do not show that the last complementary pair has disjoint
representatives, nor that the resulting ten- or eleven-palette restrictions
are incompatible with exact balance. The earlier local counterexample to
automatic disjointness prevents assuming that implication without proof.
All global conclusions above explicitly use the no-rainbow-`2K3` hypothesis
and robustness after deleting the chosen triangles.

The first of these gaps is now closed by the separate nine-family PSD audit
just cited, under the full no-`2K3` hypothesis. It is not closed by the
coarsening census alone. The exact balanced realizability of the final two
globally complement-free families is still open in this work.
