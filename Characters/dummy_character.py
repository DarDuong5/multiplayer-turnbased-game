from Characters.character import Character

class DummyCharacter(Character):
    def __init__(self):
        super().__init__(health=100, defense=0, base_attack=25, special_attack=50)

    def attack(self, target: 'Character') -> None:
        pass  

    def defend(self) -> None:
        from Actions.defend_action import DefendAction
        defense_action = DefendAction(active_turns=0, user=self)
        defense_action.defend()

    def special_move(self, target: 'Character') -> None:
        pass


