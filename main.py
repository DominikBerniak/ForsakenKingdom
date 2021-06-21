import util
import engine
import ui
import os
from time import sleep

PLAYER_ICON = '@'
PLAYER_START_ROW = 3
PLAYER_START_COL = 3

BOARD_WIDTH = 115
BOARD_HEIGHT = 30

def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_player():
    ui.display_title("Create your hero")
    player_stats = {"name":util.get_input("Your hero's name",1).title()}
    while True:        
        orc = {"race":"Orc" ,"health":125,"lvl":1,"exp":0,"attack":7,"armor":20}
        human = {"race":"Human","health":100,"lvl":1,"exp":0,"attack":10,"armor":10}
        dwarf = {"race":"Dwarf","health":75,"lvl":1,"exp":0,"attack":10,"armor":20} 
        elf = {"race":"Elf","health":75,"lvl":1,"exp":0,"attack":13,"armor":10}
        ui.display_race_choices([orc,human,dwarf,elf])

        player_race = util.get_input(" Race",3).lower()
        if player_race == "human":
            player_stats.update(human)
            break
        elif player_race == "dwarf":
            player_stats.update(dwarf)
            break
        elif player_race == "elf":
            player_stats.update(elf)
            break
        elif player_race == "orc":
            player_stats.update(orc)
            break
        else:
            console_clear()
            ui.print_error_message("    Wrong race name!")
            sleep(2)
    player_stats.update({"player_location": (PLAYER_START_ROW,PLAYER_START_COL),
                         "player_icon":PLAYER_ICON})
    return player_stats

def get_player_placement(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "@":
                return i,j

def main():
    util.clear_screen()
    # option = engine.menu()
    #if option == "start_game":
    util.clear_screen()
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        ui.display_stats(player,board)

        key = util.key_pressed()
        if key == "q":
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()