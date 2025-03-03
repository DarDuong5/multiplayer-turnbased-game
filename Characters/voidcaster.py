from typing import TYPE_CHECKING
from Characters.character import Character

if TYPE_CHECKING:
    from Characters.character import Character

class Voidcaster(Character):
    def __init__(self):
        super().__init__(health=125, defense=0, base_attack=50, special_attack=60)
    
    def attack(self, target: 'Character') -> None:
        from Actions.attack_action import AttackAction
        attack_action = AttackAction(damage=self.base_attack, user=self)
        attack_action.dark_pulse(target)

    def defend(self) -> None:
        from Actions.defend_action import DefendAction
        defense_action = DefendAction(active_turns=0, user=self)
        defense_action.defend()

    def special_move(self, target: 'Character') -> None:
        from Actions.special_move_action import SpecialMoveAction
        special_move_action = SpecialMoveAction(damage=self.special_attack, cooldown=2, user=self)
        special_move_action.arcane_blast(target)
    
# PYTESTS

def test_attack() -> None:
    from Characters.dummy_character import DummyCharacter
    user = Voidcaster()
    opponent = DummyCharacter()
    assert opponent.health == 100
    user.attack(opponent)
    assert opponent.health == 50

def test_defend() -> None:
    user = Voidcaster()
    assert user.defense == 0
    assert user.defense_active == False
    user.defend()
    assert user.defense == 10
    assert user.defense_active == True

def test_special_move() -> None:
    from Characters.dummy_character import DummyCharacter
    from Actions.special_move_action import SpecialMoveAction
    user = Voidcaster()
    opponent = DummyCharacter()
    assert opponent.health == 100
    special_move_action = SpecialMoveAction(damage=user.special_attack, cooldown=0, user=user)
    special_move_action.arcane_blast(opponent)
    assert opponent.health == 40
    assert special_move_action.cooldown == 2
