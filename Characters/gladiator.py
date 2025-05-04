from Characters.character import Character

'''
'Gladiator' is a subclass of 'Character' where it has its own built-in attributes. A player is able to select this character and play as it.
'''

# To represent a Gladiator character
class Gladiator(Character):
    def __init__(self):
        super().__init__(health=250, defense=10, base_attack=30, special_attack=50, base_attack_name='Sword Slash', special_attack_name='Titan Smash')

    # Signature: None -> str
    # Purpose: Returns the name of the this character
    def __str__(self) -> str:
        return 'Gladiator'
    
    # Signature: Character -> None
    # Purpose: Allows the character to attack the target
    def attack(self, target: 'Character') -> None:
        from Actions.attack_action import AttackAction
        attack_action = AttackAction(damage=self.base_attack, user=self)
        attack_action.sword_slash(target)

    # Signature: Character -> None
    # Purpose: Allows the character to perform a special move at the target
    def special_move(self, target: 'Character') -> None:
        from Actions.special_move_action import SpecialMoveAction
        special_move_action = SpecialMoveAction(damage=self.special_attack, user=self)
        special_move_action.titan_smash(target)

# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

def test_attack() -> None:
    from Characters.dummy_character import DummyCharacter
    user = Gladiator()
    opponent = DummyCharacter()
    assert opponent.health == 100
    user.attack(opponent)
    assert opponent.health == 70

def test_defend() -> None:
    user = Gladiator()
    assert user.defense == 10
    assert user.defense_active == False
    user.defend()
    assert user.defense == 20
    assert user.defense_active == True

def test_special_move() -> None:
    from Characters.dummy_character import DummyCharacter
    user = Gladiator()
    opponent = DummyCharacter()
    assert opponent.health == 100
    user.special_attack_cooldown = 0
    assert user.special_attack_cooldown == 0
    user.special_move(opponent)
    assert opponent.health == 50
    assert user.special_attack_cooldown == 3

    