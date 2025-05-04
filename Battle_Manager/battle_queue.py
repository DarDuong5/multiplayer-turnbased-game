from Characters.gladiator import Gladiator
from Characters.nightstalker import Nightstalker
from Characters.stoneguard import Stoneguard
from Characters.voidcaster import Voidcaster
from Characters.stormstriker import Stormstriker
from Characters.character import Character
from Characters.character_factory import CharacterFactory
from Status_Effects.poison import Poison
from Status_Effects.confusion import Confusion
from Status_Effects.paralyze import Paralyze
from typing import Optional, TYPE_CHECKING
import time

if TYPE_CHECKING:
    from Characters.character import Character
    from Status_Effects.status_effect import StatusEffect
    from Status_Effects.poison import Poison
    from Status_Effects.confusion import Confusion
    from Status_Effects.paralyze import Paralyze

'''
'BattleQueue' is a class that manages the game logic such as letting the players choose their characters and keeping track of the players and turns.
There aren't any design patterns or OOP principles being used here but if there's something I want to improve on,
it would be cleaning up the code and separating these methods into separate files within this package to keep everything
organized and clean. I would only do this if I had more time but surely I will be doing this on my own time.
'''

# To represent a battle queue
class BattleQueue:
    def __init__(self):
        self._player_queue: list['Character'] = []
        self._available_characters: dict[str, 'Character'] = {
            '1': CharacterFactory.create_character('1'),
            '2': CharacterFactory.create_character('2'),
            '3': CharacterFactory.create_character('3'),
            '4': CharacterFactory.create_character('4'),
            '5': CharacterFactory.create_character('5')
        }
        self._available_status_effects: dict[str, 'StatusEffect'] = {'Paralyze': Paralyze(), 'Poison': Poison(), 'Confusion': Confusion()}

    # Signature: None -> list[Character]
    # Purpose: Gets and returns the player queue
    @property
    def player_queue(self) -> list['Character']:
        return self._player_queue
    
    # Signature: list[Character] -> None
    # Purpose: Sets and updates the player queue
    @player_queue.setter
    def player_queue(self, new_queue: list['Character']) -> None:
        self._player_queue = new_queue

    # Signature: None -> dict[str, Character]
    # Purpose: Gets and returns the available characters
    @property
    def available_characters(self) -> dict[str, 'Character']:
        return self._available_characters
    
    # Signature: None -> dict[str, StatusEffect]
    # Purpose: Gets and return the available status effects
    @property
    def available_status_effects(self) -> dict[str, 'StatusEffect']:
        return self._available_status_effects

    # Signature: None -> None
    # Purpose: Prints the introduction to the game for the player(s)
    def begin_game(self) -> None:
        print('\nWelcome to Classical Strike Showdown!')
        time.sleep(2.0)

        print('The rules are as follows:')
        time.sleep(2.0)

        print('Three players will compete against each other.')
        time.sleep(2.0) 

        print('Each player will choose their own unique class and will battle until the last one remains.')
        time.sleep(2.0)

        print('Without further ADOOOO, let the games begin!\n')
        time.sleep(2.0)

    # Signature: None -> None
    # Purpose: Prints and shows the available characters along with their description for the player(s) to choose
    def show_character(self):
        print('The character available are as follows: \n')
        time.sleep(2.0)

        print('1. Gladiator')
        print('The Gladiator is a strong fighter who is best at close combat.\n'
              'This character has a lot of health and can deal big physical damage.\n'
              'Players who like to fight up close and take hits will enjoy playing as a Gladiator.\n'
              "Their special move, Titan Smash, is a powerful attack that deals extra damage but has a cooldown, meaning it can't be used on every turn.\n"
              'Health: 250, Defense: 10, Attack Damage: 30, Special Damage: 50\n')
        time.sleep(1.0)

        print('2. Voidcaster')
        print('The Voidcaster is a magic user who fights from a distance using spells.\n'
              "They can deal a lot of magical damage, but they don’t have much health and are weak if attacked up close.\n"
              'This character is good for players who like long-range attacks and strategy.\n'
              'Their special move, ArcaneBlast, is a strong spell that hits all opponents at once.\n'
              'Health: 125, Defense: 0, Attack Damage: 50, Special Damage: 60\n')
        time.sleep(1.0)

        print('3. Stormstriker')
        print('The Stormstriker is a fast, ranged attacker who uses a bow and arrows.\n'
              "They are very quick and can attack from far away, but they aren’t strong in close combat and don’t have much defense.\n"
              'Players who like speed and avoiding attacks will enjoy playing as the Stormstriker.\n'
              'Their special move, Piercing Arrow, is an attack that ignores defense and does critical damage.\n'
              'Health: 150, Defense: 0, Attack Damage: 40, Special Damage: 60\n')
        time.sleep(1.0)

        print('4. Nightstalker')
        print('The Nightstalker is a stealth-based assassin who does high damage in one attack but has very low health.\n'
              "They are good at quick, surprise attacks but can be taken down easily if they don’t act fast.\n"
              'This character is best for players who like aggressive attacks and critical strikes.\n'
              'Their special move, Silent Kill, does double damage if the target is not defending.\n'
              'Health: 100, Defense: 5, Attack Damage: 80, Special Damage: 80\n')
        
        time.sleep(1.0)

        print('5. Stoneguard')
        print('The Stoneguard is a defensive tank who is built to absorb a lot of damage.\n'
              "This character has high health and defense but is slow and doesn’t hit very hard.\n"
              'This character is best for players who like defensive strategies and long battles.\n'
              'Their special move, Iron Fortress, reduces all damage taken for two turns, making them hard to defeat.\n'
              f'Health: 350, Defense: 25, Attack Damage: 15, Special Defense: +15\n')
        time.sleep(1.0)

        print('To choose a character, simply type their number and press enter when prompted.\n'
              'Every player will only have their own unique characters; no duplicates.\n')
        time.sleep(1.5)

    # Signature: int -> None
    # Purpose: Makes the player input the character they want to choose and appends to the player queue
    def choose_character(self, player_number: int) -> None:
        while True:
            player_choice = input(f'Player {player_number} choose your character: ')

            if player_choice in self.available_characters:
                if self.available_characters[player_choice] in self.player_queue:
                    print(f'Character {player_choice} has already been chosen. Please select another.')
                else:
                    self.player_queue.append(self.available_characters[player_choice])
                    print(f'Player {player_number} chose {self.available_characters[player_choice]}\n')
                    time.sleep(1.0)
                    break
            else:
                print(f'Invalid Choice: {player_choice}. Please choose a valid character.')
                time.sleep(1.0)

    # Signature: None -> None
    # Purpose: Allows a number of players to select their characters
    def start_character_selection(self) -> None:
        for i in range(1, 4):
            self.choose_character(i)

    # Signature: int -> list[str]
    # Purpose: Shows the available opponents for the user after using an attack move
    def append_available_opponents(self, player_index: int) -> list[str]: 
        available: list[str] = []       
        print('\nAvailable opponents:')
        time.sleep(1.0)
        for j, opponent in enumerate(self.player_queue):
            if player_index != j:
                print(f'Player {j + 1} ({opponent}) - Health: {opponent.health} | Defense: {opponent.defense}')
                available.append(str(j + 1))
                time.sleep(1.0)
        return available
    
    # Signature: list[str] -> int
    # Purpose: Prompts and makes the user select an opponent to attack, returning the opponent
    def choose_target(self, available: list[str]) -> int:
        while True: 
            target = input('\nWho do you want to attack? (Choose the player number)\n')
            if target not in available:
                print('Invalid target, try again.')
                time.sleep(1.0)
            else:
                return int(target) - 1

    # Signature: None -> None
    # Purpose: Handles the turn mechanics of the game such as updating duration and cooldown
    def handle_turns(self) -> None:
        for player in self.player_queue:
            if player.special_attack_cooldown > 0:
                player.special_attack_cooldown -= 1
            if player.defense_active:
                player.update_defense()
            if isinstance(player, Stoneguard) and player.iron_defense_active:
                player.update_iron_defense()
            # THINKING ABOUT PUTTING STATUS EFFECTS HERE

    # Signature: Character -> bool
    # Purpose: Updates the status effect on the player and skips the players turn depending on the status effect
    def handle_status_effects(self, player: 'Character') -> bool:
        # Check for Paralyze effect
        if any(isinstance(effect, Paralyze) for effect in player.status_effect_type):
            self.available_status_effects['Paralyze'].update(player)
            return True  # Skip turn
    
        # Check for Confusion effect
        if any(isinstance(effect, Confusion) for effect in player.status_effect_type):
            self.available_status_effects['Confusion'].update(player)
            return True  # Skip turn or apply damage
    
        # Handle Poison effects (no turn skip, just damage)
        if any(isinstance(effect, Poison) for effect in player.status_effect_type):
            self.available_status_effects['Poison'].update(player)
           
    # Signature: Character, int -> None
    # Purpose: Allows the player to attack the selected opponent using the base attack of the player's character
    def handle_base_attack(self, player: 'Character', player_index: int) -> None:
        available_opponents = self.append_available_opponents(player_index)
        target_index = self.choose_target(available_opponents)
        target_player = self.player_queue[target_index]
        player.attack(target_player)
        time.sleep(1.0)

        print(f'Player {player_index + 1} ({player}) used {player.base_attack_name} on Player {target_index + 1} ({target_player})!\n')
        time.sleep(1.0)

        print(f'Player {target_index + 1}\'s ({target_player}) health now is at {max(0, target_player.health)}!\n')
        time.sleep(1.0)
    
    # Signature: Character, int -> None
    # Purpose: Allows the player to use the special attack on a single or multiple targets or on themselves depending on the player's character
    def handle_special_attack(self, player: 'Character', player_index: int) -> None:
        if isinstance(player, Voidcaster):
            print(f'Player {player_index + 1} ({player}) used {player.special_attack_name} and attacked ALL opponents!\n')
            time.sleep(1.5)
            targets = [opponent for i, opponent in enumerate(self.player_queue) if i != player_index]
            player.special_move(targets)
            time.sleep(1.0)
        elif isinstance(player, Stoneguard):
            player.special_move()
            time.sleep(1.0)
        else:
            available_opponents = self.append_available_opponents(player_index)
            target_index = self.choose_target(available_opponents)
            target_player = self.player_queue[target_index]
            player.special_move(target_player)
            time.sleep(1.0)

            print(f'Player {player_index + 1} ({player}) used {player.special_attack_name} on Player {target_index + 1} ({target_player})!\n')
            time.sleep(1.0)

            print(f'Player {target_index + 1}\'s ({target_player}) health now is at {max(0, target_player.health)}!\n')
            time.sleep(1.0)

    # Signature: Character, str, int -> None
    # Purpose: Handles and executes the move that the player chose
    def handle_move(self, player: 'Character', move: str, player_index: int) -> None:
        # Base Attack 
        if move == '1':
            self.handle_base_attack(player, player_index)
        # Defend
        elif move == '2':
            if not player.defense_active:
                player.defend()
                print(f'{player} defended and gained +10 Defense!\n')
                time.sleep(1.0)
            else:
                print('Your defense is still active!\n')
                time.sleep(1.0)
        # Special Attack
        elif move == '3':
            if player.special_attack_cooldown == 0:
                self.handle_special_attack(player, player_index)
            else:
                print(f'The ability {player.special_attack_name} is on cooldown!\n')   
                time.sleep(1.0)
        else:
            print('Invalid choice. Please enter 1, 2, or 3.\n')
            time.sleep(1.0)

    # Signature: None -> None
    # Purpose: Handles everything that goes in within the game
    def during_game(self):
        turn_number: int = 0
        while len(self.player_queue) > 1:
            for i, player in enumerate(self.player_queue):
                turn_number += 1
                move = input(f'Player {i + 1} ({player}) | Status: {','.join(str(effect) for effect in player.status_effect_type) if player.status_effect_type else 'None'} | Cooldown: {player.special_attack_cooldown}\n'
                             f'Health: {player.health} | Defense: {player.defense}\n'
                             f'Turn {turn_number} | Player {i + 1} ({player}): What move do you choose?\n'
                             f'1. Attack: {player.base_attack_name} | 2. Defend: +10 Defense | 3. Special Move: {player.special_attack_name}\n'
                             'Available choices: 1 | 2 | 3\n')
                
                if self.handle_status_effects(player):
                    continue

                self.handle_move(player, move, i)
                self.handle_turns()
                self.remove_player()

        self.end_game()
    
    # Signature: None -> None
    # Purpose: Removes the player from the game when they're defeated
    def remove_player(self) -> None:
        """Removes players with 0 health from the game."""
        defeated_players = [player for player in self.player_queue if player.health <= 0]

        for player in defeated_players:
            print(f'{player} has been wiped out from the battle!\n')
            self.player_queue.remove(player)
            time.sleep(1.0)

    # Signature: None -> str
    # Purpose: Ends the game when one player remain, declaring them the winner
    def end_game(self) -> str:
        time.sleep(1.5)
        if len(self.player_queue) == 1:
            print(f'{self.player_queue[0]} has won!\n')
        else:
            print('No players remain! This game ends in a draw.\n')

    # Signature: None -> None
    # Purpose: Runs the entire game
    def run_game(self) -> None:
        self.begin_game()
        self.show_character()
        self.start_character_selection()
        self.during_game()

# -----------------------------------------------------------------PYTESTS-----------------------------------------------------------------

            