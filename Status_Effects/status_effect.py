from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Characters.character import Character

class StatusEffect(ABC):
    def __init__(self, damage: int, duration: int, effect_type: str):
        self._damage = damage
        self._duration = duration
        self.effect_type = effect_type

    @abstractmethod
    def apply(self, target: 'Character') -> None:
        pass

    @abstractmethod
    def update(self, target: 'Character') -> None:
        pass

    def remove_effect(self, target: 'Character') -> None:
        # This ensures that the effect can be identified and removed based on its type
        to_remove = [effect for effect in target.status_effect_type if effect.effect_type == self.effect_type]
        for effect in to_remove:
            target.status_effect_type.remove(effect)
            print(f'Removed effect: {effect} from {target}')
        
        if not target.status_effect_type:
            target.has_status_effect = False
            print(f'{target} no longer has any status effects.')

    @property
    def damage(self) -> int:
        return self._damage
    
    @damage.setter
    def damage(self, new_damage: int) -> None:
        # if new_damage < 0:
        #     raise Exception('New damage cannot be below 0')
        self._damage = new_damage
    
    @property
    def duration(self) -> int:
        return self._duration
    
    @duration.setter
    def duration(self, new_duration) -> None:
        # if new_duration < 0:
        #     raise Exception('New duration cannot be below 0')
        self._duration = new_duration

    def __eq__(self, other):
        # Compare based on effect type and other attributes (optional)
        return isinstance(other, StatusEffect) and self.effect_type == other.effect_type

    def __hash__(self):
        # Hash based on the effect type
        return hash(self.effect_type)
    
# PYTESTS

# Signature: Character -> None
# Purpose: Helper method used for testing that guarantees the status effect instead of random chance
def guaranteed_apply(target: 'Character') -> None:
    from Status_Effects.poison import Poison
    poison = Poison()
    if poison not in target.status_effect_type:
        target.has_status_effect = True
        target.status_effect_type.append(poison)
        poison.duration = 4

def test_remove_effect() -> None:
    from Status_Effects.poison import Poison
    from Characters.dummy_character import DummyCharacter
    opponent = DummyCharacter()
    poison = Poison()
    assert opponent.has_status_effect == False
    assert opponent.status_effect_type == []
    guaranteed_apply(opponent)
    assert opponent.has_status_effect == True
    assert isinstance(opponent.status_effect_type[0], Poison)
    poison = opponent.status_effect_type[0]
    poison.remove_effect(opponent)
    assert opponent.has_status_effect == False
    assert opponent.status_effect_type == []

def test_get_damage() -> None:
    from Status_Effects.poison import Poison
    poison = Poison()
    assert poison.damage == 5

def test_set_damage() -> None:
    from Status_Effects.poison import Poison
    poison = Poison()
    assert poison.damage == 5
    poison.damage = 100
    assert poison.damage == 100

def test_get_duration() -> None:
    from Status_Effects.poison import Poison
    poison = Poison()
    assert poison.duration == 4

def test_set_duration() -> None:
    from Status_Effects.poison import Poison
    poison = Poison()
    assert poison.duration == 4
    poison.duration = 10
    assert poison.duration == 10

