from Characters.gladiator import Gladiator
from Characters.nightstalker import Nightstalker
from Characters.stoneguard import Stoneguard
from Characters.voidcaster import Voidcaster
from Characters.stormstriker import Stormstriker
from Characters.character import Character
from typing import Optional, TYPE_CHECKING
import time

if TYPE_CHECKING:
    from Characters.character import Character

# Consists of 3 players. Player 1 will choose, then Player 2, and then Player 3

class BattleQueue:
    def __init__(self):
        self._player_queue: list = []
        self._available_characters: dict['Character'] = {'1': Gladiator(), '2': Voidcaster(), '3': Stormstriker(), '4': Nightstalker(), '5': Stoneguard()}

    @property
    def player_queue(self):
        return self._player_queue

    @property
    def available_characters(self):
        return self._available_characters

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

    def choose_character(self, player_number: int) -> None:
        while True:
            player_choice = input(f'Player {player_number} choose your character: ')

            if player_choice in self.available_characters:
                if self.available_characters[player_choice] in self.player_queue:
                    print(f'Character {player_choice} has already been chosen. Please select another.')
                else:
                    self.player_queue.append(self.available_characters[player_choice])
                    print(f'Player {player_number} chose {self.available_characters[player_choice]}\n')
                    break
            else:
                print(f'Invalid Choice: {player_choice}. Please choose a valid character.')

    def start_character_selection(self) -> None:
        for i in range(1, 4):
            self.choose_character(i)

    def during_game(self):
        turn_number: int = 0
        while len(self.player_queue) > 1:
            for i, player in enumerate(self.player_queue):
                turn_number += 1
                attack_name = player.base_attack_name
                special_name = player.special_attack_name

                move = input(
                    f'Player {i + 1} ({player}) status: {player.status_effect_type}\n'
                    f'Health: {player.health} | Defense: {player.defense}\n'
                    f'Turn {turn_number} | Player {i + 1} ({player}): What move do you choose?\n'
                    f'1. Attack: {attack_name} | 2. Defend: +10 Defense | 3. Special Move: {special_name}\n'
                    'Available choices: 1 | 2 | 3\n'
                )    

                # Handle choices
                if move == '1':
                    available: list[str] = []       
                    print('\nAvailable opponents:')
                    for j, opponent in enumerate(self.player_queue):
                        if i != j:
                            print(f'Player {j + 1} ({opponent}) - Health: {opponent.health} | Defense: {opponent.defense}')
                            available.append(str(j + 1))
                    while True: 
                        target = input('\nWho do you want to attack? (Choose the player number)\n')

                        if target not in available:
                            print('Invalid target, try again.')
                        else:
                            target_index = int(target) - 1
                            target_player = self.player_queue[target_index]
                            player.attack(target_player)
                            print(
                                f'Player {i + 1} ({player}) used {attack_name} on Player {target} ({target_player})!\n'
                                f'Player {target}\'s ({target_player}) health now is at {target_player.health}!\n'
                                )
                            break

                elif move == '2':
                    player.defend()
                    print(f'{player} defended and gained +10 Defense!\n')

                elif move == '3':
                    print(f'{player} used {special_name}!')
                    
                else:
                    print('Invalid choice. Please enter 1, 2, or 3.')
        
# class Player:
#     def __init__(self):
#         self._character: 'Character' = None