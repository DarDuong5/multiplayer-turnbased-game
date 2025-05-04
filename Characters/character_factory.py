from Characters.gladiator import Gladiator
from Characters.nightstalker import Nightstalker
from Characters.stoneguard import Stoneguard
from Characters.stormstriker import Stormstriker
from Characters.voidcaster import Voidcaster
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Characters.character import Character

# To represent a character factory class for characters
class CharacterFactory:
    # Signature: str -> Character
    # Purpose: 
    def create_character(character_type: str) -> 'Character':
        character_type = character_type.lower()
        if character_type == '1':
            return Gladiator()
        elif character_type == '2':
            return Voidcaster()
        elif character_type == '3':
            return Stormstriker()
        elif character_type == '4':
            return Nightstalker()
        elif character_type == '5':
            return Stoneguard()
        else:
            raise ValueError(f'Unknown character type: {character_type}')
        
# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

def test_correct_instance() -> None:
    assert str(CharacterFactory.create_character('1')) == 'Gladiator'
    assert str(CharacterFactory.create_character('2')) == 'Voidcaster'
    assert str(CharacterFactory.create_character('3')) == 'Stormstriker'
    assert str(CharacterFactory.create_character('4')) == 'Nightstalker'
    assert str(CharacterFactory.create_character('5')) == 'Stoneguard'
