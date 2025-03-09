from typing import TYPE_CHECKING
from Status_Effects.status_effect import StatusEffect
import random
import math
import time

if TYPE_CHECKING:
    from Characters.character import Character

# To represent a confusion status effect
class Confusion(StatusEffect):
    def __init__(self):
        super().__init__(damage=15, duration=2, effect_type='Confusion')

    # Signature: None -> str
    # Purpose: Returns the name of the this status effect
    def __str__(self) -> str:
        return 'Confusion'

    # Signature: Character -> None
    # Purpose: A chance to apply confusion on the target after using a special attack move
    def apply(self, target: 'Character') -> None:
        chance = random.randint(1, 4)
        if chance == 1 and self not in target.status_effect_type:
            target.has_status_effect = True
            target.status_effect_type.add(self)
            self.duration = 3 # Technically 2 turns based on how the turn mechanics work
            print(f'{target} has been confused!\n')
            time.sleep(1.0)

    # Signature: Character -> None
    # Purpose: Updates the status effect on the target as well as the duration. The target will not be able to attack and will hurt itself while attacking for the duration.
    def update(self, target: 'Character') -> None:
        confusion_damage = math.floor(target.base_attack * 0.25)
        target.health -= confusion_damage
        self.duration -= 1
        print(f'{target} is confused and dealt {confusion_damage} to itself while attacking!\n'
              f'{target} now has {target.health}!\n')
        time.sleep(1.0)
        if self.duration <= 0:
            self.remove_effect(target)
            print(f'The confusion has worn off of {target}.\n')
            time.sleep(1.0)

# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

# Signature: Character -> None
# Purpose: Helper method used for testing that guarantees the status effect instead of random chance
def guaranteed_apply_helper(target: 'Character') -> None:
    confusion = Confusion()  # Create an instance of Confusion
    if confusion not in target.status_effect_type:
        target.has_status_effect = True
        target.status_effect_type.add(confusion)  # Append the instance, not the class
        confusion.duration = 2

def test_apply() -> None:
    from Characters.dummy_character import DummyCharacter
    opponent = DummyCharacter()
    assert opponent.has_status_effect == False
    assert opponent.status_effect_type == set()
    guaranteed_apply_helper(opponent)
    assert opponent.has_status_effect == True
    assert any(isinstance(effect, Confusion) for effect in opponent.status_effect_type)

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

