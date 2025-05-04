from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Status_Effects.status_effect import StatusEffect

'''
Since the parent class 'Character' has so many attributes that all of the characters will inherit such as health, defense, attack etc., I used inheritance
as it would be cleaner to implement the subclasses associated as a specific character in the game. These specific characters include 'Gladiator', 
'Nightstalker', 'Stoneguard', 'Stormstriker', and 'Voidcaster'. The methods that all of these subclasses will have are 'defend' and 'update_defense'.
'defend allows the character to defend as defined in the 'DefendAction' subclass of 'Action. 'update_defense' basically just updates the turns if the defense is active.

All of the attributed are protected with the getter and setter methods, therefore they're encapsulated. 
'health' is the amount of health the character has.
'defense' is the amount of defense the character has.
'base_attack' is the amount of damage the user does.
'special_attack' is the amount of damage the user does.
'base_attack_name' displays the base attack name.
'special_attack_name' displays the special attack name.
'special_attack_cooldown' is the cooldown of the special attack before being used again.
'defense_active' tells whether the character's defense is active or not.
'defense_active_turns' is the number of turns that the defense is active.
'has_status_effect' tells whether the character has any status effect or not.
'status_effect_type' are the status effect(s) that the character has.
'can_attack' tells whether the character can attack or not; primarily used for Paralyze.

I also used ABC abstraction on the methods such as 'attack' and 'special_move' since every subclass will have these.
The method 'attack' is defined by the subclass 'AttackAction' of the parent class 'Action'.
The method 'special_move' is defined by the subclass 'SpecialMoveAction' of the parent class 'Action'.
This also followed by polymorphism since these subclasses' methods will have different functions. 

If there is anything that I could do to improve this design decision, it would be to implement a factory class within the parent class 'Character'
to help create multiple other characters easily in the future but I didn't have enough time for that. However, I will be implementing that in my own time.
'''
    
# To represent a character
class Character(ABC):
    def __init__(self, health: int, defense: int, base_attack: int, special_attack: int, base_attack_name: str, special_attack_name: str):
        self._health = health
        self._defense = defense
        self._base_attack = base_attack
        self._special_attack = special_attack
        self._base_attack_name = base_attack_name
        self._special_attack_name = special_attack_name
        self._special_attack_cooldown: int = 3
        self._defense_active: bool = False
        self._defense_active_turns: int = 0
        self._has_status_effect: bool = False
        self._status_effect_type: set[StatusEffect] = set()
        self._can_attack: bool = True

    # Signature: Character -> None
    # Purpose: Allows the character to attack the target
    @abstractmethod
    def attack(self, target: 'Character') -> None:
        pass
    
    # Signature: Character -> None
    # Purpose: Allows the character to perform a special move at the target
    @abstractmethod
    def special_move(self, target: 'Character') -> None:
        pass
    
    # Signature: None -> int
    # Purpose: Gets and returns the health of the character
    @property
    def health(self) -> int:
        return self._health
    
    # Signature: int -> None
    # Purpose: Sets and updates the health of the character
    @health.setter
    def health(self, new_health: int) -> None:
        self._health = new_health
    
    # Signature: None -> int
    # Purpose: Gets and returns the defense of the character
    @property
    def defense(self) -> int:
        return self._defense
    
    # Signature: int -> None
    # Purpose: Sets and updates the defense of the character
    @defense.setter
    def defense(self, new_defense: int) -> None:
        self._defense = new_defense

    # Signature: None -> int
    # Purpose: Gets and returns the base attack damage of the character
    @property
    def base_attack(self) -> int:
        return self._base_attack 

    # Signature: int -> None
    # Purpose: Sets and updates the base attack damage of the character
    @base_attack.setter
    def base_attack(self, new_base_attack: int) -> None:
        self._base_attack = new_base_attack

    # Signature: None -> int
    # Purpose: Gets and returns the special attack damage of the character
    @property
    def special_attack(self) -> int:
        return self._special_attack
    
    # Signature: int -> None
    # Purpose: Sets and updates the special attack damage of the character
    @special_attack.setter
    def special_attack(self, new_special_attack: int) -> None:
        self._special_attack = new_special_attack

    # Signature: None -> bool
    # Purpose: Gets and returns if the defense of the character is active or not
    @property
    def defense_active(self) -> bool:
        return self._defense_active

    # Signature: bool -> None
    # Purpose: Sets and updates if the defense of the character is active or not
    @defense_active.setter
    def defense_active(self, new_defense_active: bool) -> None:
        self._defense_active = new_defense_active

    # Signature: None -> bool
    # Purpose: Gets and returns if the character has a status effect or not
    @property 
    def has_status_effect(self) -> bool:
        return self._has_status_effect 

    # Signature: bool -> None
    # Purpose: Sets and updates if the defense of the character is active or not
    @has_status_effect.setter
    def has_status_effect(self, new_has_status_effect: bool) -> None:
        self._has_status_effect = new_has_status_effect
    
    # Signature: None -> list[StatusEffect]
    # Purpose: Gets and returns the status effect type
    @property
    def status_effect_type(self) -> list['StatusEffect']:
        return self._status_effect_type

    # Signature: list[StatusEffect] -> None
    # Purpose: Sets and updates the status effect type
    @status_effect_type.setter
    def status_effect_type(self, new_status_effect_type: list['StatusEffect']) -> None:
        self._status_effect_type = new_status_effect_type

    # Signature: None -> bool
    # Purpose: Gets and returns if the character can attack or not
    @property
    def can_attack(self) -> bool:
        return self._can_attack
    
    # Signature: bool -> None
    # Purpose: Sets and updates if the character can attack or not
    @can_attack.setter
    def can_attack(self, new_can_attack: bool) -> None:
        self._can_attack = new_can_attack

    # Signature: None -> str
    # Purpose: Gets and returns the base attack name of the character
    @property
    def base_attack_name(self) -> str:
        return self._base_attack_name
    
    # Signature: str -> None
    # Purpose: Sets and updates the base attack name of the character
    @base_attack_name.setter
    def base_attack_name(self, new_name: str) -> None:
        self._base_attack_name = new_name

    # Signature: None -> str
    # Purpose: Gets and returns the special attack name of the character
    @property
    def special_attack_name(self) -> str:
        return self._special_attack_name
    
    # Signature: str -> None
    # Purpose: Sets and updates the special attack name of the character
    @special_attack_name.setter
    def special_attack_name(self, new_name: str) -> None:
        self._special_attack_name = new_name

    # Signature: None -> int
    # Purpose: Gets and returns the special attack cooldown of the character
    @property
    def special_attack_cooldown(self) -> int:
        return self._special_attack_cooldown
    
    # Signature: int -> None
    # Purpose: Sets and updates the special attack cooldown of the character
    @special_attack_cooldown.setter
    def special_attack_cooldown(self, value: int) -> None:
        self._special_attack_cooldown = value

    # Signature: None -> int
    # Purpose: Gets and returns the duration of the defense
    @property
    def defense_active_turns(self) -> int:
        return self._defense_active_turns
    
    # Signature: int -> None
    # Purpose: Sets and updates the duration of the defense
    @defense_active_turns.setter
    def defense_active_turns(self, value: int) -> None:
        self._defense_active_turns = value

    # Signature: None -> None
    # Purpose: Allows the character to defend
    def defend(self) -> None:
        from Actions.defend_action import DefendAction
        defense_action = DefendAction(user=self) 
        defense_action.defend()

    # Signature: None -> None
    # Purpose: Updates character's defense and duration every turn
    def update_defense(self) -> None:
        if self.defense_active_turns > 0:
            self.defense_active_turns -= 1
        if self.defense_active_turns == 0 and self.defense_active:
            self.defense -= 10
            self.defense_active = False
            print(f'{self}\' defense has worn out!\n')

# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

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
    