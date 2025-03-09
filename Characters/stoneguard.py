from Characters.character import Character
import time

# To represent a Stoneguard character
class Stoneguard(Character):
    def __init__(self):
        super().__init__(health=350, defense=25, base_attack=15, special_attack=0, base_attack_name='Rocky Punch', special_attack_name='Iron Fortress')
        self._iron_defense_duration = 0
        self._iron_defense_active = False

    # Signature: None -> str
    # Purpose: Returns the name of the this character
    def __str__(self) -> str:
        return 'Stoneguard'

    # Signature: Character -> int
    # Purpose: Gets and returns the duration of Iron Defense
    @property
    def iron_defense_duration(self) -> int:
        return self._iron_defense_duration
    
    # Signature: int -> None
    # Purpose: Sets and updates the duration of Iron Defense
    @iron_defense_duration.setter
    def iron_defense_duration(self, duration: int) -> None:
        self._iron_defense_duration = duration

    # Signature: None -> bool
    # Purpose: Gets and returns if the iron defense is active or not
    @property
    def iron_defense_active(self) -> bool:
        return self._iron_defense_active
    
    # Signature: bool -> None
    # Purpose: Sets and updates if the iron defense is active or not
    @iron_defense_active.setter
    def iron_defense_active(self, value: bool) -> None:
        self._iron_defense_active = value

    # Signature: Character -> None
    # Purpose: Allows the character to attack the target
    def attack(self, target: 'Character') -> None:
        from Actions.attack_action import AttackAction
        attack_action = AttackAction(damage=self.base_attack, user=self)
        attack_action.rocky_punch(target)

    # Signature: Character -> None
    # Purpose: Allows the character to perform a special move on itself
    def special_move(self) -> None:
        from Actions.special_move_action import SpecialMoveAction
        special_move_action = SpecialMoveAction(damage=self.special_attack, user=self)
        special_move_action.iron_fortress()

    # Signature: None -> None
    # Purpose: Updates the duration of the special move on this character
    def update_iron_defense(self) -> None:
        if self.iron_defense_duration > 0:
            self.iron_defense_duration -= 1
        if self.iron_defense_duration == 0 and self._iron_defense_active:
            self.defense -= 15
            self.iron_defense_active = False
            print(f'{self}\' Iron Defense has worn out!\n')
            time.sleep(1.0)

# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

def test_attack() -> None:
    from Characters.dummy_character import DummyCharacter
    user = Stoneguard()
    opponent = DummyCharacter()
    assert opponent.health == 100
    user.attack(opponent)
    assert opponent.health == 85

def test_defend() -> None:
    user = Stoneguard()
    assert user.defense == 25
    assert user.defense_active == False
    user.defend()
    assert user.defense == 35
    assert user.defense_active == True

def test_special_move() -> None:
    user = Stoneguard()
    assert user.health == 350
    assert user.defense == 25
    user.special_attack_cooldown = 0
    assert user.special_attack_cooldown == 0
    user.special_move()
    assert user.defense == 40
