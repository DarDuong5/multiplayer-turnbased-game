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

# To represent a special move action
class SpecialMoveAction(Action):
    def __init__(self, damage: int, user: 'Character'):
        super().__init__(user)
        self._damage = damage

    # Signature: None -> int:
    # Purpose: Gets and returns the damage of the attack action
    @property
    def damage(self) -> int:
        return self._damage
    
    # Signature: int -> None:
    # Purpose: Sets and updates the damage of the attack action
    @damage.setter
    def damage(self, new_damage: int) -> None:
        self._damage = new_damage
    
    # Signature: Character -> None:
    # Purpose: Applies damage to the target minus the defense and sets the special attack cooldown after using the move Titan Smash for Gladiator
    def titan_smash(self, target: 'Character') -> None:
        if self.user.special_attack_cooldown == 0:
            target.health -= self.damage - target.defense
            self.user.special_attack_cooldown = 3
    
    # Signature: Character -> None:
    # Purpose: Applies damage to the target minus the defense and sets the special attack cooldown after using the move Arcane Blast for Voidcaster
    def arcane_blast(self, targets: list['Character']) -> None:
        if self.user.special_attack_cooldown == 0:
            for target in targets:
                target._health -= self.damage - target.defense
                Confusion().apply(target)
                print(f'{target} took {self.damage - target.defense} damage and is now at {max(0, target._health)} health!\n')
            self.user.special_attack_cooldown = 3

    # Signature: Character -> None:
    # Purpose: Applies damage to the target minus the defense and sets the special attack cooldown after using the move Piercing Arrow for Stormstriker
    def piercing_arrow(self, target: 'Character') -> None:
        if self.user.special_attack_cooldown == 0:
            target.health -= self.damage
            Paralyze().apply(target)
            self.user.special_attack_cooldown = 3

    # Signature: Character -> None:
    # Purpose: Applies damage to the target minus the defense and sets the special attack cooldown after using the move Silent Kill for Nightstalker
    def silent_kill(self, target: 'Character') -> None:
        if self.user.special_attack_cooldown == 0:
            if not target.defense_active:
                target.health -= self.damage * 2
            else:
                target.health -= self.damage
            Poison().apply(target)
            self.user.special_attack_cooldown = 3

    # Signature: Character -> None:
    # Purpose: Applies defense to the user and sets the duration and special attack cooldown after using the move Iron Fortress for Stoneguard
    def iron_fortress(self) -> None:
        if isinstance(self.user, Stoneguard):
            if self.user.special_attack_cooldown == 0:
                self.user.defense += 15
                self.user.iron_defense_duration = 3
                self.user.iron_defense_active = True
                self.user.special_attack_cooldown = 3
                print(f'{self.user} activated Iron Fortress! Defense increased to {self.user.defense} for {self.user.iron_defense_duration} turns.\n')
            else:
                print(f'{self.user}\'s Iron Fortress is still on cooldown for {self.user.special_attack_cooldown} more turns!\n')


# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

def test_get_damage() -> None:
    user = Gladiator()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, user=user)
    assert user_special_move_action.damage == 50

def test_set_damage() -> None:
    user = Stoneguard()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, user=user)
    assert user_special_move_action.damage == 0
    user_special_move_action.damage = 10000
    assert user_special_move_action.damage == 10000

def test_titan_smash() -> None:
    user = Gladiator() 
    opponent = Stormstriker()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, user=user)
    assert opponent.health == 150
    user.special_attack_cooldown = 0
    assert user.special_attack_cooldown == 0
    user_special_move_action.titan_smash(opponent)
    assert opponent.health == 100
    assert user.special_attack_cooldown == 3

def test_arcane_blast() -> None:
    user = Voidcaster()
    opponent_1 = Nightstalker()
    opponent_2 = Gladiator()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, user=user)
    assert opponent_1.health == 100
    assert opponent_2.health == 250
    user.special_attack_cooldown = 0
    assert user.special_attack_cooldown == 0
    user_special_move_action.arcane_blast([opponent_1, opponent_2])
    assert opponent_1.health == 45
    assert opponent_2.health == 200
    assert user.special_attack_cooldown == 3

def test_piercing_arrow() -> None: 
    user = Stormstriker()
    opponent = Gladiator()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, user=user)
    assert opponent.health == 250
    user.special_attack_cooldown = 0
    assert user.special_attack_cooldown == 0
    user_special_move_action.piercing_arrow(opponent)
    assert opponent.health == 190
    assert user.special_attack_cooldown == 3

def test_silent_kill_with_defense_off() -> None:
    user = Nightstalker()
    opponent = Stormstriker()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, user=user)
    assert opponent.health == 150
    user.special_attack_cooldown = 0
    assert user.special_attack_cooldown == 0
    user_special_move_action.silent_kill(opponent)
    assert opponent.health == -10
    assert user.special_attack_cooldown == 3

def test_silent_kill_with_defense_on() -> None:
    user = Nightstalker()
    opponent = Stormstriker()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, user=user)
    assert opponent.health == 150
    user.special_attack_cooldown = 0
    assert user.special_attack_cooldown == 0
    opponent.defend() 
    user_special_move_action.silent_kill(opponent)
    assert opponent.health == 70
    assert user.special_attack_cooldown == 3

def test_iron_fortress() -> None:
    user = Stoneguard()
    user_special_move_action = SpecialMoveAction(damage=user.special_attack, user=user)
    user.special_attack_cooldown = 0
    assert user.special_attack_cooldown == 0
    assert user.defense == 25
    user_special_move_action.iron_fortress()
    assert user.defense == 40
    assert user.special_attack_cooldown == 3


