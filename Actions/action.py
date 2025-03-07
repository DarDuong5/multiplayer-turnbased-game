from Characters.character import Character
from Characters.gladiator import Gladiator
from Characters.voidcaster import Voidcaster
from Characters.nightstalker import Nightstalker
from Characters.stormstriker import Stormstriker
from Characters.stoneguard import Stoneguard

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




