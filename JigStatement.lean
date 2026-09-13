import Mathlib

namespace Statements.E811ClassAReduction

def Balanced {t : ℕ}
    (c : Fin (6 * t + 1) → Fin (6 * t + 1) → Fin 6) : Prop :=
  ∀ v k, ((Finset.univ.erase v).filter fun w => c v w = k).card = t

def RainbowTriangle {N : ℕ} (c : Fin N → Fin N → Fin 6)
    (x y z : Fin N) : Prop :=
  x ≠ y ∧ x ≠ z ∧ y ≠ z ∧
  c x y ≠ c x z ∧ c x y ≠ c y z ∧ c x z ≠ c y z

def TwoDisjointRainbowTriangles {N : ℕ}
    (c : Fin N → Fin N → Fin 6) : Prop :=
  ∃ a b d e f g : Fin N,
    ({a, b, d, e, f, g} : Finset (Fin N)).card = 6 ∧
    ({c a b, c a d, c b d, c e f, c e g, c f g} :
      Finset (Fin 6)) = Finset.univ

def ClassA (a b d : Fin 6) : Prop :=
  ({a, b, d} : Finset (Fin 6)) ∈
    ([{0,1,2}, {0,1,3}, {0,1,5}, {0,2,4}, {0,3,4},
      {0,3,5}, {1,2,3}, {1,3,4}, {1,4,5}, {2,3,5}] :
      List (Finset (Fin 6)))

def ClassASupportedUpToRelabeling {N : ℕ}
    (c : Fin N → Fin N → Fin 6) : Prop :=
  ∃ σ : Equiv.Perm (Fin 6), ∀ x y z,
    RainbowTriangle c x y z → ClassA (σ (c x y)) (σ (c x z)) (σ (c y z))

abbrev statement : Prop :=
  ∀ t : ℕ, 629137 ≤ t →
  ∀ c : Fin (6 * t + 1) → Fin (6 * t + 1) → Fin 6,
    (∀ x y, c x y = c y x) → Balanced c →
    ¬ TwoDisjointRainbowTriangles c → ClassASupportedUpToRelabeling c

theorem target : statement := sorry

end Statements.E811ClassAReduction
