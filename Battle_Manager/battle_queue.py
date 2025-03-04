from Characters.gladiator import Gladiator
from Characters.nightstalker import Nightstalker
from Characters.stoneguard import Stoneguard
from Characters.voidcaster import Voidcaster
from Characters.stormstriker import Stormstriker
from typing import Optional, TYPE_CHECKING
import time

if TYPE_CHECKING:
    from Characters.character import Character

# Consists of 3 players. Player 1 will choose, then Player 2, and then Player 3

class BattleQueue:
    def __init__(self):
        self._player_queue: list = []

    @property
    def player_queue(self):
        pass

    @player_queue.setter
    def player_queue(self):
        pass

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
              "Their special move, Titan Smash, is a powerful attack that deals extra damage but has a cooldown, meaning it can't be used on every turn.\n")
        time.sleep(1.0)

        print('2. Voidcaster')
        print('The Voidcaster is a magic user who fights from a distance using spells.\n'
              "They can deal a lot of magical damage, but they don’t have much health and are weak if attacked up close.\n"
              'This character is good for players who like long-range attacks and strategy.\n'
              'Their special move, ArcaneBlast, is a strong spell that hits all opponents at once.\n')
        time.sleep(1.0)

        print('3. Stormstriker')
        print('The Stormstriker is a fast, ranged attacker who uses a bow and arrows.\n'
              "They are very quick and can attack from far away, but they aren’t strong in close combat and don’t have much defense.\n"
              'Players who like speed and avoiding attacks will enjoy playing as the Stormstriker.\n'
              'Their special move, Piercing Arrow, is an attack that ignores defense and does critical damage.\n')
        time.sleep(1.0)

        print('4. Nightstalker')
        print('The Nightstalker is a stealth-based assassin who does high damage in one attack but has very low health.\n'
              "They are good at quick, surprise attacks but can be taken down easily if they don’t act fast.\n"
              'This character is best for players who like aggressive attacks and critical strikes.\n'
              'Their special move, Silent Kill, does double damage if the target is not defending.\n')
        time.sleep(1.0)

        print('5. Stoneguard')
        print('The Stoneguard is a defensive tank who is built to absorb a lot of damage.\n'
              "This character hashigh health and defense but is slow and doesn’t hit very hard.\n"
              'This character is best for players who like defensive strategies and long battles.\n'
              'Their special move, Iron Fortress, reduces all damage taken for two turns, making them hard to defeat.\n')
        time.sleep(1.0)

    def choose_character(self):
        pass

class Player:
    def __init__(self):
        self._character: 'Character' = None