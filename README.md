# A Class A reduction for the two-triangle question in Erdős #811

This package proves a structural reduction for the independently posed
two-disjoint-rainbow-triangles part of
[Erdős problem #811](https://www.erdosproblems.com/811).

It does **not** solve the original question.

## The result

Let `t >= 629137`. Color the edges of `K_(6t+1)` with six colors so that
every vertex has exactly `t` neighbors in each color. If there are no two
vertex-disjoint triangles whose six edges have six different colors, then,
after permuting the color names, every rainbow triangle has one of the ten
palettes

```text
012, 013, 015, 024, 034, 035, 123, 134, 145, 235.
```

This remaining palette family is called Class A in the working notes. The
conclusion applies to the original graph; it is not based on assuming a block
model or symmetry. The unresolved task is to exclude all sufficiently large
Class A colorings or construct one exact finite example, which would amplify
to arbitrarily large examples.

## Read and verify

- `SINGLE-RESIDUAL-FAMILY.md`: theorem and synthesis.
- `GLOBAL-COMPLEMENT-FREE-REDUCTION.md`: reduction to two palette families.
- `FULL-K5-242467-PSD-GAP.md`: exact exclusion of the other family.
- `SINGLE-RESIDUAL-FAMILY-INDEPENDENT-AUDIT.md`: independent scope audit.
- `TARGET.md`: original statement, conventions, and prior-work boundaries.

The certificate layer uses exact integer and rational arithmetic. To replay
the two principal independent checks:

```sh
python3 audit-full-k5-census.py
python3 audit-full-k5-psd-dual-independent.py
python3 root-check-full-k5-dual.py
python3 verify-global-reduction-bounds.py
```

The full five-vertex census has 551 symmetry orbits containing **2,607,696**
labeled allowed patterns. The independent checker reconstructs the group
actions, census coverage, rooted flag classes, certificate values, and finite
threshold. Numerical optimizer output is not trusted as proof.

## Scope and provenance

This is AI-assisted research produced with Codex and independently audited by
separate Codex agents. That is adversarial internal review, not external human
peer review. The package is a partial-progress result and makes no claim that
Erdős #811 is resolved. See `SOURCE-RECHECK-20260911.md` and `TARGET.md` for
the bounded source audit and credited prior ingredients.

