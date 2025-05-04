from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from Characters.character import Character

'''
ABC abstraction is implemented on the parent class 'StatusEffect' where the methods 'apply' and 'update' are abstract.
'apply' has the chance to apply the effect onto the target after being attacked by a special move.
'update' decreases the character's health and/or skips the target's turn depending on the specific status effect.
This is followed by polymorphism since these methods will have their own different functions. 
Encapsulation is also being used, making the attributes protected. 
The method that will universally be used on is 'remove_effect' which removes the effect after the status duration runs out. 

If there is anything I can do to improve upon this, it would be to make the parent class 'StatusEffect' a factory class since there could be a high possibiliy
that if there are new characters, then there could be new status effects as well. 
'''

# To represent a status effect
class StatusEffect(ABC):
    def __init__(self, damage: int, duration: int, effect_type: str):
        self._damage = damage
        self._duration = duration
        self._effect_type = effect_type

    # Signature: Character -> None
    # Purpose: A chance to apply status effect on the target after using a special attack move
    @abstractmethod
    def apply(self, target: 'Character') -> None:
        pass

    # Signature: Character -> None
    # Purpose: Updates the status effect on the target as well as the duration.
    @abstractmethod
    def update(self, target: 'Character') -> None:
        pass

    # Signature: Character -> None
    # Purpose: Removes the status effect from the target after the duration runs out
    def remove_effect(self, target: 'Character') -> None:
        # This ensures that the effect can be identified and removed based on its type
        to_remove = [effect for effect in target.status_effect_type if effect.effect_type == self.effect_type]
        for effect in to_remove:
            target.status_effect_type.remove(effect)
        
        if not target.status_effect_type:
            target.has_status_effect = False

    # Signature: None -> int
    # Purpose: Gets and returns the damage of the status effect
    @property
    def damage(self) -> int:
        return self._damage
    
    # Signature: int -> None
    # Purpose: Sets and updates the damage of the status effect
    @damage.setter
    def damage(self, new_damage: int) -> None:
        self._damage = new_damage
    
    # Signature: None -> int
    # Purpose: Gets and returns the duration of the status effect
    @property
    def duration(self) -> int:
        return self._duration
    
    # Signature: int -> None
    # Purpose: Sets and updates the duration of the status effect
    @duration.setter
    def duration(self, new_duration: int) -> None:
        self._duration = new_duration

    # Signature: None -> str
    # Purpose: Gets and returns the effect type applied onto the character
    @property
    def effect_type(self) -> str:
        return self._effect_type
    
    # Signature: str -> None
    # Purpose: Sets and updates the effect type applied onto the character
    @effect_type.setter
    def effect_type(self, value: str) -> None:
        self._effect_type = value

    # Signature: Optional -> None
    # Purpose: Compares based on effect type and other attributes (optional)
    def __eq__(self, other: Optional['StatusEffect']) -> bool:
        return isinstance(other, StatusEffect) and self.effect_type == other.effect_type

    # Signature: None -> int
    # Purpose: Hashes based on the effect type that uniquely identifies an object based on its attributes
    def __hash__(self) -> int:
        return hash(self.effect_type)
    
# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

# Signature: Character -> None
# Purpose: Helper method used for testing that guarantees the status effect instead of random chance
def guaranteed_apply(target: 'Character') -> None:
    from Status_Effects.poison import Poison
    poison = Poison()
    if poison not in target.status_effect_type:
        target.has_status_effect = True
        target.status_effect_type.add(poison)
        poison.duration = 4

def test_remove_effect() -> None:
    from Status_Effects.poison import Poison
    from Characters.dummy_character import DummyCharacter
    opponent = DummyCharacter()
    poison = Poison()
    assert opponent.has_status_effect == False
    assert opponent.status_effect_type == set()
    guaranteed_apply(opponent)
    assert opponent.has_status_effect == True
    assert any(isinstance(effect, Poison) for effect in opponent.status_effect_type)
    poison.remove_effect(opponent)
    assert opponent.has_status_effect == False
    assert opponent.status_effect_type == set()

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

def test_get_effect_type() -> None:
    from Status_Effects.poison import Poison
    poison = Poison()
    assert poison.effect_type == 'Poison'

def test_set_effect_type() -> None:
    from Status_Effects.poison import Poison
    poison = Poison()
    assert poison.effect_type == 'Poison'
    poison.effect_type = 'Poisoned'
    assert poison.effect_type == 'Poisoned'
