from Characters.character import Character
from Characters.gladiator import Gladiator
from Characters.voidcaster import Voidcaster 
from Characters.nightstalker import Nightstalker
from Characters.stormstriker import Stormstriker
from Characters.stoneguard import Stoneguard
from Actions.action import Action
from Actions.defend_action import DefendAction
from Status_Effects.confusion import Confusion
from Status_Effects.paralyze import Paralyze
from Status_Effects.poison import Poison

class SpecialMoveAction(Action):
    def __init__(self, damage: int, cooldown: int, user: 'Character'):
        super().__init__(user)
        self._damage = damage
        self._cooldown = cooldown
        
    @property
    def damage(self) -> int:
        return self._damage
    
    @damage.setter
    def damage(self, new_damage: int) -> None:
        self._damage = new_damage

    @property
    def cooldown(self) -> int:
        return self._cooldown
    
    @cooldown.setter
    def cooldown(self, new_cooldown: int) -> None:
        self._cooldown = new_cooldown
    
    def titan_smash(self, target: 'Character') -> None:
        if self.cooldown == 0:
            target.health -= self.damage - target.defense
            self.cooldown = 2
        else:
            return f'The ability Titan Smash is still on cooldown!'
    
    # Does damage to every opponent, can apply confusion
    def arcane_blast(self, target: 'Character') -> None:
        if self.cooldown == 0:
            target._health -= self.damage - target.defense
            self.cooldown = 2
            Confusion().apply(target)
        else:
            return f'The ability Arcane Blast is still on cooldown!'

    # Bypasses defenses, can apply stun
    def piercing_arrow(self, target: 'Character') -> None:
        if self.cooldown == 0:
            target.health -= self.damage
            self.cooldown = 2
            Paralyze().apply(target)
        else:
            return f'The ability Piecing Arrow is still on cooldown!'

    def silent_kill(self, target: 'Character') -> None:
        if self.cooldown == 0:
            if not target.defense_active:
                target.health -= self.damage * 2
            else:
                target.health -= self.damage
            self.cooldown = 2
            Poison().apply(target)

        else:
            return f'The ability Silent Kill is still on cooldown!'

    def iron_fortress(self) -> None:
        if self.cooldown == 0:
            self.user.defense += 15
            self.cooldown = 2
        else:
            return f'The ability Iron Fortress is still on cooldown!'
        
# PYTEST

def test_get_damage() -> None:
    user = Gladiator()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, cooldown=0, user=user)
    assert user_special_move_action.damage == 50

def test_set_damage() -> None:
    user = Stoneguard()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, cooldown=0, user=user)
    assert user_special_move_action.damage == 0
    user_special_move_action.damage = 10000
    assert user_special_move_action.damage == 10000

def test_get_cooldown() -> None:
    user = Voidcaster()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, cooldown=2, user=user)
    assert user_special_move_action.cooldown == 2

def test_set_cooldown() -> None:
    user = Nightstalker()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, cooldown=2, user=user)
    assert user_special_move_action.cooldown == 2
    user_special_move_action.cooldown = 1
    assert user_special_move_action.cooldown == 1

def test_iron_smash() -> None:
    user = Gladiator() 
    opponent = Stormstriker()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, cooldown=0, user=user)
    assert opponent.health == 150
    assert user_special_move_action.cooldown == 0
    user_special_move_action.titan_smash(opponent)
    assert opponent.health == 100
    assert user_special_move_action.cooldown == 2

def test_arcane_blast() -> None:
    user = Voidcaster()
    opponent = Nightstalker()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, cooldown=0, user=user)
    assert opponent.health == 100
    assert user_special_move_action.cooldown == 0
    user_special_move_action.arcane_blast(opponent)
    assert opponent.health == 45
    assert user_special_move_action.cooldown == 2

def test_piercing_arrow() -> None: 
    user = Stormstriker()
    opponent = Gladiator()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, cooldown=0, user=user)
    assert opponent.health == 250
    assert user_special_move_action.cooldown == 0
    user_special_move_action.piercing_arrow(opponent)
    assert opponent.health == 190
    assert user_special_move_action.cooldown == 2

def test_silent_kill_with_defense_off() -> None:
    user = Nightstalker()
    opponent = Stormstriker()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, cooldown=0, user=user)
    assert opponent.health == 150
    assert user_special_move_action.cooldown == 0
    user_special_move_action.silent_kill(opponent)
    assert opponent.health == -10
    assert user_special_move_action.cooldown == 2

def test_silent_kill_with_defense_on() -> None:
    user = Nightstalker()
    opponent = Stormstriker()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, cooldown=0, user=user)
    opponent_defend_action = DefendAction(0, opponent)
    assert opponent.health == 150
    assert user_special_move_action.cooldown == 0
    opponent_defend_action.defend()
    user_special_move_action.silent_kill(opponent)
    assert opponent.health == 70
    assert user_special_move_action.cooldown == 2

def test_iron_fortress() -> None:
    user = Stoneguard()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, cooldown=0, user=user)
    assert user.defense == 25
    user_special_move_action.iron_fortress()
    assert user.defense == 40
    assert user_special_move_action.cooldown == 2


