from Actions.action import Action
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Characters.character import Character

'''
The subclass 'DefendAction' is inherited by the parent class 'Action'.
Although there are no new attributes for 'DefendAction', it still has its own purpose.
The attribute 'user' is the 'Character' defending
The method allows the user to use the move defend, therefore making it a defend action.

'''

# To represent a defend action
class DefendAction(Action): 
    def __init__(self, user: 'Character'):
        super().__init__(user)
    
    # Signature: None -> None
    # Purpose: Applies defense to the user and sets the duration for defending
    def defend(self) -> None:
        if not self.user.defense_active:
            self.user.defense += 10
            self.user.defense_active_turns = 3 # Technically 2 active turns due to how the turn mechanics work
            self.user.defense_active = True

# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

def test_defend() -> None:
    from Characters.dummy_character import DummyCharacter
    user = DummyCharacter()
    defend_action = DefendAction(user)
    assert user.defense == 0
    assert user.defense_active == False
    assert user.defense_active_turns == 0
    defend_action.defend()
    assert user.defense == 10
    assert user.defense_active == True
    assert user.defense_active_turns == 3




