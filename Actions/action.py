from Characters.character import Character
from Characters.gladiator import Gladiator
from Characters.voidcaster import Voidcaster
from Characters.nightstalker import Nightstalker
from Characters.stormstriker import Stormstriker
from Characters.stoneguard import Stoneguard


'''
The design decisions on this part was to use inheritance and encapsulation. It was logical to to make the 'Action' class the parent class
since it was more general and could be split into specific subclasses such as 'AttackAction', 'DefendAction' and 'SpecialMoveAction' which
has similar things to the parent class 'Action' but has different logic. Encapsulation was also an important design decision I decided
to implement for this part, making the attributes protected. 

Inheritance is implemented on the parent class 'Action' and used on the subclasses 'AttackAction', 'DefendAction', and 'SpecialMoveAction'.
'Action' has the attributes 'user' which is the 'Character' who executes the action.
'AttackAction', 'DefendAction', and 'SpecialMoveAction' will inherit the parent class attribute 'user'.
Encapsulation is also applied in this class by protecting the attribute 'user', having the getter and setter methods.

'''


# To represent an action
class Action:
    def __init__(self, user: 'Character'):
        self._user = user

    # Signature: None -> Character
    # Purpose: Gets and returns the character
    @property
    def user(self) -> 'Character':
        return self._user
    
    # Signature: Character -> None
    # Purpose: Sets and updates the character
    @user.setter
    def user(self, new_user: 'Character') -> None:
        self._user = new_user

# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

def test_get_user() -> None:
    gladiator = Gladiator()
    gladiator_action = Action(gladiator)
    stoneguard = Stoneguard()
    stoneguard_action = Action(stoneguard)
    voidcaster = Voidcaster()
    voidcaster_action = Action(voidcaster)
    stormstriker = Stormstriker()
    stormstriker_action = Action(stormstriker)
    nightstalker = Nightstalker()
    nightstalker_action = Action(nightstalker)
    assert gladiator_action.user == gladiator
    assert stoneguard_action.user == stoneguard
    assert voidcaster_action.user == voidcaster
    assert stormstriker_action.user == stormstriker
    assert nightstalker_action.user == nightstalker

def test_set_user() -> None:
    player1 = Gladiator()
    player2 = Stoneguard()
    action = Action(player1)
    assert action.user == player1
    action.user = player2
    assert action.user == player2




