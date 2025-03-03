from Characters.character import Character
from Characters.gladiator import Gladiator
from Characters.voidcaster import Voidcaster
from Characters.nightstalker import Nightstalker
from Characters.stormstriker import Stormstriker
from Characters.stoneguard import Stoneguard
from Actions.action import Action

class AttackAction(Action):
    def __init__(self, damage: int, user: 'Character'):
        super().__init__(user)
        self._damage = damage
    
    @property
    def damage(self) -> int:
        return self._damage
    
    @damage.setter
    def damage(self, new_damage: int) -> None:
        self._damage = new_damage

    def _apply_damage(self, target: 'Character') -> None:
        target._health -= max(0, self._damage - target._defense)

    def sword_slash(self, target: 'Character') -> None:
        self._apply_damage(target)
    
    def dark_pulse(self, target: 'Character') -> None:
        self._apply_damage(target)

    def electric_arrow(self, target: 'Character') -> None:
        self._apply_damage(target)

    def dagger_stab(self, target: 'Character') -> None:
        self._apply_damage(target)
     
    def rocky_punch(self, target: 'Character') -> None:
        self._apply_damage(target)

# PYTESTS 

def test_get_damage() -> None:
    gladiator: 'Character' = Gladiator()
    attack_action: AttackAction = AttackAction(gladiator.base_attack, gladiator)
    assert attack_action.damage == gladiator.base_attack

def test_set_damage() -> None:
    gladiator: 'Character' = Gladiator()
    voidcaster: 'Character' = Voidcaster()
    attack_action: AttackAction = AttackAction(gladiator.base_attack, gladiator)
    assert attack_action.damage == gladiator.base_attack
    attack_action.damage = voidcaster.base_attack
    assert attack_action.damage == voidcaster.base_attack

def test_apply_damage() -> None:
    user = Stoneguard()
    opponent = Nightstalker()
    user_attack_action = AttackAction(user.base_attack, user)
    assert opponent.health == 100
    user_attack_action._apply_damage(opponent)
    assert opponent.health == 90

def test_sword_slash() -> None:
    user = Gladiator()
    opponent = Nightstalker()
    user_attack_action = AttackAction(user.base_attack, user)
    assert opponent.health == 100
    user_attack_action.sword_slash(opponent)
    assert opponent.health == 75

def test_dark_pulse() -> None:
    user = Voidcaster()
    opponent = Gladiator()
    user_attack_action = AttackAction(user.base_attack, user)
    assert opponent.health == 250
    user_attack_action.dark_pulse(opponent)
    assert opponent.health == 210

def test_electric_arrow() -> None:
    user = Stormstriker()
    opponent = Voidcaster()
    user_attack_action = AttackAction(user.base_attack, user)
    assert opponent.health == 125
    user_attack_action.electric_arrow(opponent)
    assert opponent.health == 85

def test_dagger_stab() -> None:
    user = Nightstalker()
    opponent = Stoneguard()
    user_attack_action = AttackAction(user.base_attack, user)
    assert opponent.health == 350
    user_attack_action.dagger_stab(opponent)
    assert opponent.health == 295

def test_rocky_punch() -> None:
    user = Stoneguard()
    opponent = Nightstalker()
    user_attack_action = AttackAction(user.base_attack, user)
    assert opponent.health == 100
    user_attack_action.rocky_punch(opponent)
    assert opponent.health == 90





    