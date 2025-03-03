from Characters.character import Character
from Characters.gladiator import Gladiator
from Characters.voidcaster import Voidcaster
from Characters.nightstalker import Nightstalker
from Characters.stormstriker import Stormstriker
from Characters.stoneguard import Stoneguard
from Actions.action import Action

class DefendAction(Action): 
    def __init__(self, active_turns: int, user: 'Character'):
        super().__init__(user)
        self._active_turns = active_turns

    @property
    def active_turns(self) -> int:
        return self._active_turns
    
    @active_turns.setter
    def active_turns(self, new_active_turns: int) -> None:
        if new_active_turns < 0:
            print('Error: Active turns cannot be negative')
        else:
            self._active_turns = new_active_turns
    
    def defend(self) -> None:
        if self.active_turns == 0 and not self.user.defense_active:
            self.user.defense += 10
            self.active_turns = 2
            self.user.defense_active = True
        else:
            print('Your defense is still active!')

    def update(self) -> None:
        self.active_turns -= 1
        if self.active_turns == 0:
            self.user.defense -= 10
            self.user.defense_active = False

# PYTESTS

def test_get_active_turns() -> None:
    user = Gladiator()
    user_defend_action = DefendAction(0, user)
    assert user.defense_active == False
    assert user_defend_action.active_turns == 0

def test_set_active_turns() -> None:
    user = Stoneguard()
    user_defend_action = DefendAction(0, user)
    assert user_defend_action.active_turns == 0
    user_defend_action.active_turns = 2
    assert user_defend_action.active_turns == 2

def test_defend() -> None:
    user = Stormstriker()
    user_defend_action = DefendAction(0, user)
    assert user.defense == 0
    user_defend_action.defend()
    assert user.defense == 10
    assert user_defend_action.active_turns == 2
    user2 = Nightstalker()
    user2_defend_action = DefendAction(0, user2)
    assert user2.defense == 5
    user2_defend_action.defend()
    assert user2.defense == 15
    assert user_defend_action.active_turns == 2
    assert user2_defend_action.defend() == print('Your defense is still active!')

def test_update() -> None:
    user = Voidcaster()
    user_defend_action = DefendAction(2, user)
    assert user_defend_action.active_turns == 2
    user_defend_action.update()
    assert user_defend_action.active_turns == 1


