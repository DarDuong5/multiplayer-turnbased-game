from Characters.character import Character

'''
'Voidcaster' is a subclass of 'Character' where it has its own built-in attributes. A player is able to select this character and play as it.
'''
# To represent a Voidcaster character
class Voidcaster(Character):
    def __init__(self):
        super().__init__(health=125, defense=0, base_attack=50, special_attack=60, base_attack_name='Dark Pulse', special_attack_name='Arcane Blast')

    # Signature: None -> str
    # Purpose: Returns the name of the this character
    def __str__(self) -> str:
        return 'Voidcaster'

    # Signature: Character -> None
    # Purpose: Allows the character to attack the target
    def attack(self, target: 'Character') -> None:
        from Actions.attack_action import AttackAction
        attack_action = AttackAction(damage=self.base_attack, user=self)
        attack_action.dark_pulse(target)

    # Signature: Character -> None
    # Purpose: Allows the character to perform a special move at the target
    def special_move(self, target: list['Character']) -> None:
        from Actions.special_move_action import SpecialMoveAction
        special_move_action = SpecialMoveAction(damage=self.special_attack, user=self)
        special_move_action.arcane_blast(target)
    
# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

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
    user = Voidcaster()
    opponent1 = DummyCharacter()
    opponent2 = DummyCharacter()
    opponent3 = DummyCharacter()
    targets = [opponent1, opponent2, opponent3]
    assert opponent1.health == 100
    assert opponent2.health == 100
    assert opponent3.health == 100
    user.special_attack_cooldown = 0
    assert user.special_attack_cooldown == 0
    user.special_move(targets)
    assert opponent1.health == 40
    assert opponent2.health == 40
    assert opponent3.health == 40
    assert user.special_attack_cooldown == 3
