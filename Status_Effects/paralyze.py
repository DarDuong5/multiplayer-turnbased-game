from typing import TYPE_CHECKING
from Status_Effects.status_effect import StatusEffect
import random

if TYPE_CHECKING:
    from Characters.character import Character

class Paralyze(StatusEffect):
    def __init__(self):
        super().__init__(damage=0, duration=2)

    def __str__(self) -> str:
        return 'Paralyze'
    
    def apply(self, target: 'Character') -> None:
        chance = random.randint(1, 4)
        if chance == 1 and self not in target.status_effect_type:
            target.has_status_effect = True
            target.status_effect_type.append(self)
            target.can_attack = False
            self.duration = 2

    def update(self, target: 'Character') -> None:
        self.duration -= 1
        if self.duration == 0:
            target.can_attack = True
            self.remove_effect(target)

# PYTESTS

# Signature: Character -> None
# Purpose: Helper method used for testing that guarantees the status effect instead of random chance
def guaranteed_apply_helper(target: 'Character') -> None:
    paralyze = Paralyze()
    if paralyze not in target._status_effect_type:
        target.has_status_effect = True
        target.status_effect_type.append(paralyze)
        target.can_attack = False
        paralyze.duration = 2

def test_apply() -> None:
    from Characters.dummy_character import DummyCharacter
    opponent = DummyCharacter()
    assert opponent.has_status_effect == False
    assert opponent.status_effect_type == []
    guaranteed_apply_helper(opponent)
    assert opponent.has_status_effect == True
    assert isinstance(opponent.status_effect_type[0], Paralyze)

def test_update() -> None:
    from Characters.dummy_character import DummyCharacter
    opponent = DummyCharacter()
    paralyze = Paralyze()
    assert opponent.health == 100
    assert paralyze.duration == 2
    guaranteed_apply_helper(opponent)
    paralyze.update(opponent)
    assert opponent.health == 100
    assert paralyze.duration == 1
    paralyze.update(opponent)
    assert opponent.health == 100
    assert paralyze.duration == 0