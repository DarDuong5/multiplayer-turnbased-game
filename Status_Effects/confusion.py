from typing import TYPE_CHECKING
from Status_Effects.status_effect import StatusEffect
import random
import math

if TYPE_CHECKING:
    from Characters.character import Character

class Confusion(StatusEffect):
    def __init__(self):
        super().__init__(damage=15, duration=2)

    def apply(self, target: 'Character') -> None:
        chance = random.randint(1, 4)
        if chance == 1 and self not in target.status_effect_type:
            target.has_status_effect = True
            target.status_effect_type.append(self)
            self.duration = 2

    def update(self, target: 'Character') -> None:
        target.health -= math.floor(target.base_attack * 0.25)
        self.duration -= 1
        if self.duration == 0:
            self.remove_effect(target)

# PYTESTS

# Signature: Character -> None
# Purpose: Helper method used for testing that guarantees the status effect instead of random chance
def guaranteed_apply_helper(target: 'Character') -> None:
    confusion = Confusion()  # Create an instance of Confusion
    if confusion not in target.status_effect_type:
        target.has_status_effect = True
        target.status_effect_type.append(confusion)  # Append the instance, not the class
        confusion.duration = 2

def test_apply() -> None:
    from Characters.dummy_character import DummyCharacter
    opponent = DummyCharacter()
    assert opponent.has_status_effect == False
    assert opponent.status_effect_type == []
    guaranteed_apply_helper(opponent)
    assert opponent.has_status_effect == True
    assert isinstance(opponent.status_effect_type[0], Confusion)  # Check instance

def test_update() -> None:
    from Characters.dummy_character import DummyCharacter
    opponent = DummyCharacter()
    confusion = Confusion()
    guaranteed_apply_helper(opponent)
    assert opponent.health == 100  # Use correct attribute access
    assert confusion.duration == 2
    confusion.update(opponent)
    assert opponent.health == 94
    assert confusion.duration == 1
    confusion.update(opponent)
    assert opponent.health == 88
    assert confusion.duration == 0

