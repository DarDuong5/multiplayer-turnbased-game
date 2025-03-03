from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Characters.character import Character

class StatusEffect(ABC):
    def __init__(self, damage: int, duration: int):
        self._damage = damage
        self._duration = duration

    @abstractmethod
    def apply(self, target: 'Character') -> None:
        pass

    @abstractmethod
    def update(self, target: 'Character') -> None:
        pass

    def remove_effect(self, target: 'Character') -> None:
        if self in target.status_effect_type:
            target.status_effect_type.remove(self)
        if not target.status_effect_type:
            target.has_status_effect = False
    
    @property
    def damage(self) -> int:
        return self._damage
    
    @damage.setter
    def damage(self, new_damage: int) -> None:
        if new_damage < 0:
            raise Exception('New damage cannot be below 0')
        self._damage = new_damage
    
    @property
    def duration(self) -> int:
        return self._duration
    
    @duration.setter
    def duration(self, new_duration) -> None:
        if new_duration < 0:
            raise Exception('New duration cannot be below 0')
        self._duration = new_duration
    
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

