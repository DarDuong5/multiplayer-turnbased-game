from Characters.character import Character

class Stoneguard(Character):
    def __init__(self):
        super().__init__(health=350, defense=25, base_attack=15, special_attack=0, base_attack_name='Rocky Punch', special_attack_name='Iron Fortress')

    def __str__(self) -> str:
        return 'Stoneguard'

    def attack(self, target: 'Character') -> None:
        from Actions.attack_action import AttackAction
        attack_action = AttackAction(damage=self.base_attack, user=self)
        attack_action.rocky_punch(target)

    def special_move(self) -> None:
        from Actions.special_move_action import SpecialMoveAction
        special_move_action = SpecialMoveAction(damage=self.special_attack, user=self)
        special_move_action.iron_fortress(self)
    
# PYTESTS

def test_attack() -> None:
    from Characters.dummy_character import DummyCharacter
    user = Stoneguard()
    opponent = DummyCharacter()
    assert opponent.health == 100
    user.attack(opponent)
    assert opponent.health == 85

def test_defend() -> None:
    user = Stoneguard()
    assert user.defense == 25
    assert user.defense_active == False
    user.defend()
    assert user.defense == 35
    assert user.defense_active == True

def test_special_move() -> None:
    from Actions.special_move_action import SpecialMoveAction
    user = Stoneguard()
    assert user.health == 350
    special_move_action = SpecialMoveAction(damage=user.special_attack, user=user)
    special_move_action.iron_fortress()
    assert user.defense == 40
    
