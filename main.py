import util
import engine
import ui
import os
PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_player():
    while True:
        print("""
        You Can choose your breed:
        ----------------------------------
        |Orc=125HP   | Attack:0 | Armor:0|
        |Human=100HP | Attack:0 | Armor:0|
        |Dwarf=75HP  | Attack:0 | Armor:0|
        |Elf=50HP    | Attack:0 | Armor:0|
        ----------------------------------
        """)
        player_stats={"name":input("Give name for your hero: ")}

        orc={"race":"Orc" ,"HP":125,"lvl":1,"xp":0,"attack":5,"armor":50}
        human={"race":"Human","HP":100,"lvl":1,"xp":0,"attack":10,"armor":45}
        dwarf={"race":"Dwarf","HP":75,"lvl":1,"xp":0,"attack":10,"armor":55} 
        elf={"race":"Elf","HP":50,"lvl":3,"xp":0,"attack":7,"armor":5}
        player_breed=input("Choose race: ").upper()

        if player_breed == "HUMAN":
            player_stats.update(human)
            break
        elif player_breed == "DWARF":
            player_stats.update(dwarf)
            break
        elif player_breed == "ELF":
            player_stats.update(elf)
            break
        elif player_breed == "ORC":
            player_stats.update(orc)
            break
        else:
            console_clear()
            print("CHOOSE YOUR CHARACTER FROM LIST!")

    return player_stats


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
