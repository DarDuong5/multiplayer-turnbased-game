from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Status_Effects.status_effect import StatusEffect
    
class Character(ABC):
    def __init__(self, health: int, defense: int, base_attack: int, special_attack: int, base_attack_name: str, special_attack_name: str):
        self._health = health
        self._defense = defense
        self._base_attack = base_attack
        self._special_attack = special_attack
        self._base_attack_name = base_attack_name
        self._special_attack_name = special_attack_name
        self._special_attack_cooldown = 3
        self._defense_active = False
        self._defense_active_turns = 0
        self._has_status_effect: bool = False
        self._status_effect_type: set[StatusEffect] = set()
        self._can_attack = True

    @abstractmethod
    def attack(self, target: 'Character') -> None:
        pass
    
    @abstractmethod
    def special_move(self, target: 'Character') -> None:
        pass

    @property
    def health(self) -> int:
        return self._health
    
    @health.setter
    def health(self, new_health: int) -> None:
        self._health = new_health

    @property
    def defense(self) -> int:
        return self._defense
    
    @defense.setter
    def defense(self, new_defense: int) -> None:
        self._defense = new_defense

    @property
    def base_attack(self) -> int:
        return self._base_attack 

    @base_attack.setter
    def base_attack(self, new_base_attack: int) -> None:
        self._base_attack = new_base_attack

    @property
    def special_attack(self) -> int:
        return self._special_attack
    
    @special_attack.setter
    def special_attack(self, new_special_attack: int) -> None:
        self._special_attack = new_special_attack
    
    @property
    def defense_active(self) -> bool:
        return self._defense_active
    
    @defense_active.setter
    def defense_active(self, new_defense_active: bool) -> None:
        self._defense_active = new_defense_active

    @property 
    def has_status_effect(self) -> bool:
        return self._has_status_effect 
    
    @has_status_effect.setter
    def has_status_effect(self, new_has_status_effect: bool) -> None:
        self._has_status_effect = new_has_status_effect
    
    @property
    def status_effect_type(self) -> list['StatusEffect']:
        return self._status_effect_type
    
    @status_effect_type.setter
    def status_effect_type(self, new_status_effect_type: list['StatusEffect']) -> None:
        self._status_effect_type = new_status_effect_type
    
    @property
    def can_attack(self) -> bool:
        return self._can_attack
    
    @can_attack.setter
    def can_attack(self, new_can_attack: bool) -> None:
        self._can_attack = new_can_attack

    @property
    def base_attack_name(self) -> str:
        return self._base_attack_name
    
    @base_attack_name.setter
    def base_attack_name(self, new_name: str) -> None:
        self._base_attack_name = new_name

    @property
    def special_attack_name(self) -> str:
        return self._special_attack_name
    
    @special_attack_name.setter
    def special_attack_name(self, new_name: str) -> None:
        self._special_attack_name = new_name

    @property
    def special_attack_cooldown(self) -> int:
        return self._special_attack_cooldown
    
    @special_attack_cooldown.setter
    def special_attack_cooldown(self, value: int) -> None:
        self._special_attack_cooldown = value

    @property
    def defense_active_turns(self) -> int:
        return self._defense_active_turns
    
    @defense_active_turns.setter
    def defense_active_turns(self, value: int) -> int:
        self._defense_active_turns = value

    def defend(self) -> None:
        from Actions.defend_action import DefendAction
        defense_action = DefendAction(user=self) 
        defense_action.defend()

    def update_defense(self) -> None:
        if self.defense_active_turns > 0:
            self.defense_active_turns -= 1
        if self.defense_active_turns == 0 and self.defense_active:
            self.defense -= 10
            self.defense_active = False
            print(f'{self}\' defense has worn out!\n')

# PYTESTS

def test_get_health() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    assert user.health == 100

def test_set_health() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    assert user.health == 100
    user.health = 0
    assert user.health == 0

def test_get_defense() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    assert user.defense == 0

def test_set_defense() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    assert user.defense == 0
    user.defense = 100
    assert user.defense == 100

def test_get_base_attack() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    assert user.base_attack == 25

def test_set_base_attack() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    assert user.base_attack == 25
    user.base_attack = 0
    assert user.base_attack == 0

def test_get_special_attack() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    assert user.special_attack == 50

def test_set_special_attack() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    assert user.special_attack == 50
    user.special_attack = 100
    assert user.special_attack == 100

def test_get_defense_active() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    assert user.defense_active == False

def test_set_defense_active() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    assert user.defense_active == False
    user.defense_active = True
    assert user.defense_active == True

def test_get_status_effect_type() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    assert user.status_effect_type == set()

def test_set_status_effect_type() -> None:
    from Characters.dummy_character import DummyCharacter
    from Status_Effects.poison import Poison
    user = DummyCharacter()
    assert user.status_effect_type == set()
    user.status_effect_type = [Poison]
    assert user.status_effect_type == [Poison]

def test_get_can_attack() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    assert user.can_attack == True

def test_set_can_attack() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    assert user.can_attack == True
    user.can_attack = False
    assert user.can_attack == False
    