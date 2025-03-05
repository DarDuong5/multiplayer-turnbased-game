from Characters.character import Character

class Nightstalker(Character):
    def __init__(self):
        super().__init__(health=100, defense=5, base_attack=80, special_attack=80, base_attack_name='Dagger Stab', special_attack_name='Silent Kill')
    
    def __str__(self) -> str:
        return f'Nightstalker'
    
    def attack(self, target: 'Character') -> None:
        from Actions.attack_action import AttackAction
        attack_action = AttackAction(damage=self.base_attack, user=self)
        attack_action.dagger_stab(target)

    def defend(self) -> None:
        from Actions.defend_action import DefendAction
        defense_action = DefendAction(active_turns=0, user=self)
        defense_action.defend()

    def special_move(self, target: 'Character') -> None:
        from Actions.special_move_action import SpecialMoveAction
        special_move_action = SpecialMoveAction(damage=self.special_attack, cooldown=2, user=self)
        special_move_action.silent_kill(target)
    
# PYTESTS

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
    from Actions.special_move_action import SpecialMoveAction
    user = Nightstalker()
    opponent = DummyCharacter()
    assert opponent.health == 100
    assert opponent.defense_active == False
    special_move_action = SpecialMoveAction(damage=user.special_attack, cooldown=0, user=user)
    special_move_action.silent_kill(opponent)
    assert opponent.health == -60
    assert special_move_action.cooldown == 2

def test_special_move_with_defense() -> None:
    from Characters.dummy_character import DummyCharacter
    from Actions.special_move_action import SpecialMoveAction
    user = Nightstalker()
    opponent = DummyCharacter()
    assert opponent.health == 100
    assert opponent.defense_active == False
    opponent.defend()
    assert opponent.defense_active == True
    special_move_action = SpecialMoveAction(damage=user.special_attack, cooldown=0, user=user)
    special_move_action.silent_kill(opponent)
    assert opponent.health == 20
    assert special_move_action.cooldown == 2



