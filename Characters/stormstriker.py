from Characters.character import Character

# To represent a stormstriker character
class Stormstriker(Character):
    def __init__(self):
        super().__init__(health=150, defense=0, base_attack=40, special_attack=60, base_attack_name='Electric Arrow', special_attack_name='Piercing Arrow')

    # Signature: None -> str
    # Purpose: Returns the name of the this character
    def __str__(self) -> str:
        return 'Stormstriker'

    # Signature: Character -> None
    # Purpose: Allows the character to attack the target
    def attack(self, target: 'Character') -> None:
        from Actions.attack_action import AttackAction
        attack_action = AttackAction(damage=self.base_attack, user=self)
        attack_action.electric_arrow(target)

    # Signature: Character -> None
    # Purpose: Allows the character to perform a special move at the target
    def special_move(self, target: 'Character') -> None:
        from Actions.special_move_action import SpecialMoveAction
        special_move_action = SpecialMoveAction(damage=self.special_attack, user=self)
        special_move_action.piercing_arrow(target)

# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

def test_attack() -> None:
    from Characters.dummy_character import DummyCharacter
    user = Stormstriker()
    opponent = DummyCharacter()
    assert opponent.health == 100
    user.attack(opponent)
    assert opponent.health == 60

def test_defend() -> None:
    user = Stormstriker()
    assert user.defense == 0
    assert user.defense_active == False
    user.defend()
    assert user.defense == 10
    assert user.defense_active == True

def test_special_move() -> None:
    from Characters.stoneguard import Stoneguard
    user = Stormstriker()
    opponent = Stoneguard()
    assert opponent.health == 350
    assert opponent.defense == 25
    user.special_attack_cooldown = 0
    assert user.special_attack_cooldown == 0
    user.special_move(opponent)
    assert opponent.health == 290
    assert user.special_attack_cooldown == 3
