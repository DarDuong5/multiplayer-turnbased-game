from Characters.character import Character

class DummyCharacter(Character):
    def __init__(self):
        super().__init__(health=100, defense=0, base_attack=25, special_attack=50, base_attack_name='Punch', special_attack_name='Double Punch')

    def attack(self, target: 'Character') -> None:
        pass  

    def defend(self) -> None:
        from Actions.defend_action import DefendAction
        defense_action = DefendAction(active_turns=0, user=self)
        defense_action.defend()

    def special_move(self, target: 'Character') -> None:
        pass


