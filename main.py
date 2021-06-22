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

def create_player():
    while True:
        ui.clear_screen()
        ui.display_title("Create your hero")
        player_stats = {"name":util.get_input("Your hero's name",1).title()}
        if player_stats["name"] == "Admin":
            player_stats.update({"race":"God" ,"health":1000000,"lvl":1000000,"exp":1000000,"attack":1000000,
                                "armor":1000000,"player_location": [PLAYER_START_ROW,PLAYER_START_COL],"player_icon":PLAYER_ICON, "inventory":{}})
            return player_stats
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
                util.clear_screen()
                ui.display_error_message("    Wrong race name!")
                sleep(2)      
        player_stats.update({"player_location": [PLAYER_START_ROW,PLAYER_START_COL],
                                "player_icon":PLAYER_ICON, "inventory": {}})

        if engine.get_confirmation(f"""You've created {player_stats["name"]}, the {player_stats["race"]}.
    
    Do you want to play as {player_stats["name"]}? (yes/no)"""):
            break
    return player_stats

def quit():
    ui.clear_screen()
    ui.display_message("Thank you for playing. Goodbye!",2)
    sleep(2)
    ui.clear_screen()

def main():
    util.clear_screen()
    option = engine.menu()
    if option == "start_game":
        util.clear_screen()
        player = create_player()
        board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
        player["inventory"].update({"sword":10, "helmet": 10, "torch": 1})
        util.clear_screen()
        while True:
            util.clear_screen()
            engine.put_player_on_board(board, player)
            ui.display_board(board)
            ui.display_stats(player,board)

            key = util.key_pressed()
            if key == "`":
                if engine.get_confirmation("Do you really want to quit the game? (yes/no)"):
                    return quit()
            elif key == "w":
                player["player_location"][0] -= 1 
            elif key == "s":
                player["player_location"][0] += 1 
            elif key == "a":
                player["player_location"][1] -= 1 
            elif key == "d":
                player["player_location"][1] += 1 
            elif key == "i":
                ui.display_inventory(player["inventory"])
                util.press_any_button(4)
            
            
    elif option == "quit":
        quit()


if __name__ == '__main__':
    main()