from Characters.character import Character

# To represent a Nightstalker character
class Nightstalker(Character):
    def __init__(self):
        super().__init__(health=100, defense=5, base_attack=80, special_attack=80, base_attack_name='Dagger Stab', special_attack_name='Silent Kill')

    # Signature: None -> str
    # Purpose: Returns the name of the this character 
    def __str__(self) -> str:
        return 'Nightstalker'

    # Signature: Character -> None
    # Purpose: Allows the character to attack the target  
    def attack(self, target: 'Character') -> None:
        from Actions.attack_action import AttackAction
        attack_action = AttackAction(damage=self.base_attack, user=self)
        attack_action.dagger_stab(target)

    # Signature: Character -> None
    # Purpose: Allows the character to perform a special move at the target
    def special_move(self, target: 'Character') -> None:
        from Actions.special_move_action import SpecialMoveAction
        special_move_action = SpecialMoveAction(damage=self.special_attack, user=self)
        special_move_action.silent_kill(target)
    
# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

def test_attack() -> None:
    user = Nightstalker()
    opponent = Nightstalker()
    assert opponent.health == 100
    user.attack(opponent)
    assert opponent.health == 25

def test_defend() -> None:
    user = Nightstalker()
    assert user.defense == 5
    assert user.defense_active == False
    user.defend()
    assert user.defense == 15
    assert user.defense_active == True

def test_special_move_without_defense() -> None:
    from Characters.dummy_character import DummyCharacter
    user = Nightstalker()
    opponent = DummyCharacter()
    assert opponent.health == 100
    assert opponent.defense_active == False
    user.special_attack_cooldown = 0
    assert user.special_attack_cooldown == 0
    user.special_move(opponent)
    assert opponent.health == -60
    assert user.special_attack_cooldown == 3

def test_special_move_with_defense() -> None:
    from Characters.dummy_character import DummyCharacter
    user = Nightstalker()
    opponent = DummyCharacter()
    assert opponent.health == 100
    assert opponent.defense_active == False
    user.special_attack_cooldown = 0
    assert user.special_attack_cooldown == 0
    opponent.defend()
    assert opponent.defense_active == True
    user.special_move(opponent)
    assert opponent.health == 20
    assert user.special_attack_cooldown == 3



