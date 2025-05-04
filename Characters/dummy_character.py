from Characters.character import Character

'''
'DummyCharacter' serves as testing my characters on it. 
'''

# To represent a dummy character, used for Pytest
class DummyCharacter(Character):
    def __init__(self):
        super().__init__(health=100, defense=0, base_attack=25, special_attack=50, base_attack_name='Punch', special_attack_name='Double Punch')

    # Signature: Character -> None
    # Purpose: Allows the character to attack the target
    def attack(self, target: 'Character') -> None:
        pass  

    # Signature: Character -> None
    # Purpose: Allows the character to perform a special move at the target
    def special_move(self, target: 'Character') -> None:
        pass


