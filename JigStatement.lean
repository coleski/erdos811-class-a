import Mathlib

namespace Statements.E811ClassAReduction

def classA (a b d : Fin 6) : Prop :=
  ({a,b,d} : Finset (Fin 6)) ∈
    ([{0,1,2},{0,1,3},{0,1,5},{0,2,4},{0,3,4},
      {0,3,5},{1,2,3},{1,3,4},{1,4,5},{2,3,5}] : List (Finset (Fin 6)))

abbrev statement : Prop := ∀ t : ℕ, 629137 ≤ t →
  ∀ c : Fin (6*t+1) → Fin (6*t+1) → Fin 6,
  (∀ x y, c x y = c y x) →
  (∀ v k, ((Finset.univ.erase v).filter fun w => c v w = k).card = t) →
  ¬ (∃ v : Fin 6 → Fin (6*t+1), Function.Injective v ∧
      Function.Injective ![c (v 0) (v 1), c (v 1) (v 2), c (v 2) (v 0),
        c (v 3) (v 4), c (v 4) (v 5), c (v 5) (v 3)]) →
  ∃ σ : Equiv.Perm (Fin 6), ∀ x y z,
    x ≠ y → x ≠ z → y ≠ z →
    c x y ≠ c x z → c x y ≠ c y z → c x z ≠ c y z →
    classA (σ (c x y)) (σ (c x z)) (σ (c y z))

theorem target : statement := sorry

end Statements.E811ClassAReduction
