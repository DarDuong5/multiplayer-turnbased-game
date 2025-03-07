from typing import TYPE_CHECKING
from Status_Effects.status_effect import StatusEffect
import random
import time

if TYPE_CHECKING:
    from Characters.character import Character

class Poison(StatusEffect):
    def __init__(self):
        super().__init__(damage=5, duration=4, effect_type='Poison')

    def __str__(self) -> str:
        return 'Poison'
    
    def apply(self, target: 'Character') -> None:
        chance = random.randint(1, 3)
        if chance == 1 and self not in target.status_effect_type:
            target.has_status_effect = True
            target.status_effect_type.add(self)
            self.duration = 5 # Technically 4 turns based on how the turn mechanics work
            print(f'{target} has been poisoned!\n')
            time.sleep(1.0)

    def update(self, target: 'Character') -> None:
        target.health -= self.damage
        self.duration -= 1
        print(f'{target} is poisoned and the poison dealt {self.damage}!\n'
              f'{target} now has {target.health}!\n')
        time.sleep(1.0)
        if self.duration <= 0:
            self.remove_effect(target)
            print(f'The poison has worn off of {target}.\n')

# PYTESTS

# Signature: Character -> None
# Purpose: Helper method used for testing that guarantees the status effect instead of random chance
def guaranteed_apply_helper(target: 'Character') -> None:
    poison = Poison()
    if poison not in target.status_effect_type:
        target.has_status_effect = True
        target.status_effect_type.append(poison)
        poison.duration = 4

def test_apply() -> None:
    from Characters.dummy_character import DummyCharacter
    opponent = DummyCharacter()
    assert opponent.has_status_effect == False
    assert opponent.status_effect_type == []
    guaranteed_apply_helper(opponent)
    assert opponent.has_status_effect == True
    assert isinstance(opponent.status_effect_type[0], Poison)

def test_update() -> None:
    from Characters.dummy_character import DummyCharacter
    opponent = DummyCharacter()
    poison = Poison()
    assert opponent.health == 100
    assert poison.duration == 4
    poison.update(opponent)
    assert opponent.health == 95
    assert poison.duration == 3
    poison.update(opponent)
    assert opponent.health == 90
    assert poison.duration == 2
    poison.update(opponent)
    assert opponent.health == 85
    assert poison.duration == 1
    poison.update(opponent)
    assert opponent.health == 80
    assert poison.duration == 0
