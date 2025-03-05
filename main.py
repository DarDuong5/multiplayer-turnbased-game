from Battle_Manager.battle_queue import BattleQueue

def main():
    game = BattleQueue()
    # game.begin_game()
    # game.show_character()
    game.start_character_selection()
    game.during_game()

if __name__ == '__main__':
    main()