from typing import TYPE_CHECKING
from Status_Effects.status_effect import StatusEffect
import random
import time 

if TYPE_CHECKING:
    from Characters.character import Character

# To represent a paralyze status effect
class Paralyze(StatusEffect):
    def __init__(self):
        super().__init__(damage=0, duration=2, effect_type='Paralyze')

    # Signature: None -> str
    # Purpose: Returns the name of the this status effect
    def __str__(self) -> str:
        return 'Paralyze'
    
    # Signature: Character -> None
    # Purpose: A chance to apply paralysis on the target after using a special attack move
    def apply(self, target: 'Character') -> None:
        chance = random.randint(1, 4)
        if chance == 1 and self not in target.status_effect_type:
            target.has_status_effect = True
            target.status_effect_type.add(self)
            target.can_attack = False
            self.duration = 3 # Technically 2 turns based on how the turn mechanics work
            print(f'{target} has been paralyzed!\n')
            time.sleep(1.0)

    # Signature: Character -> None
    # Purpose: Updates the status effect on the target as well as the duration. The target will not be able to attack for the duration.
    def update(self, target: 'Character') -> None:
        self.duration -= 1
        print(f'{target} has been paralyzed and cannot move!\n')
        time.sleep(1.0)
        if self.duration <= 0:
            target.can_attack = True
            self.remove_effect(target)
            print(f'The paralysis has worn off of {target}.\n')
            time.sleep(1.0)

# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

# Signature: Character -> None
# Purpose: Helper method used for testing that guarantees the status effect instead of random chance
def guaranteed_apply_helper(target: 'Character') -> None:
    paralyze = Paralyze()
    if paralyze not in target._status_effect_type:
        target.has_status_effect = True
        target.status_effect_type.add(paralyze)
        target.can_attack = False
        paralyze.duration = 2

def test_apply() -> None:
    from Characters.dummy_character import DummyCharacter
    opponent = DummyCharacter()
    assert opponent.has_status_effect == False
    assert opponent.status_effect_type == set()
    guaranteed_apply_helper(opponent)
    assert opponent.has_status_effect == True
    assert any(isinstance(effect, Paralyze) for effect in opponent.status_effect_type)

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