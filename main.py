import util
import engine
import ui
import os
from time import sleep

PLAYER_ICON = '@'
CLOSED_DOOR_ICON = 'X'
OPEN_EXIT_DOOR_ICON = 'O'
NPC_SHOP_ICON = '$'

PLAYER_START_ROW = 5
PLAYER_START_COL = 100

BOARD_WIDTH = 115
BOARD_HEIGHT = 30




def create_player():
    while True:
        ui.clear_screen()
        ui.display_title("Create your hero")
        player_stats = {"name":util.get_input("Your hero's name",1).title()}
        if player_stats["name"] == "Admin":
            player_stats.update({"race":"God" ,"health":1000000,"lvl":1000000,"exp":1000000,"attack":1000000,
                                "armor":1000000,"player_location": [PLAYER_START_ROW,PLAYER_START_COL],"player_icon":PLAYER_ICON, "inventory":[]})
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
                                "player_icon":PLAYER_ICON, "inventory": []})
        ui.clear_screen()
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
        board = [engine.create_board(BOARD_WIDTH, BOARD_HEIGHT),engine.create_board(BOARD_WIDTH, BOARD_HEIGHT),engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)]
        engine.put_door_on_board(board,CLOSED_DOOR_ICON)
        board_level = 0


        player["inventory"].extend([{'type': 'armor', 'name': 'Mail Shoes', 'value': 1}, {'type': 'gold', 'name': 'Gold', 'value': 8},
        {'type': 'consumable', 'name': 'Godlike Cheese', 'value': 29},{'type': 'armor', 'name': 'Chain Chestplate', 'value': 2}])

        util.clear_screen()
        while True:
            util.clear_screen()
            engine.put_player_on_board(board[board_level], player)
            ui.display_board(board[board_level])
            ui.display_stats(player,board[board_level])
            player_location_row, player_location_col = player["player_location"]

            key = util.key_pressed()
            if key == "`":
                ui.clear_screen()
                if engine.get_confirmation("Do you really want to quit the game? (yes/no)"):
                    return quit()
            elif key == "w" and engine.is_not_wall(board[board_level], player_location_row-1, player_location_col,CLOSED_DOOR_ICON):
                player["player_location"][0] -= 1 
            elif key == "s" and engine.is_not_wall(board[board_level], player_location_row+1, player_location_col,CLOSED_DOOR_ICON):
                player["player_location"][0] += 1 
            elif key == "a" and engine.is_not_wall(board[board_level], player_location_row, player_location_col-1,CLOSED_DOOR_ICON):
                player["player_location"][1] -= 1 
            elif key == "d" and engine.is_not_wall(board[board_level], player_location_row, player_location_col+1,CLOSED_DOOR_ICON):
                player["player_location"][1] += 1 
            elif key == "i":
                ui.display_inventory(player["inventory"])
                util.press_any_button(4)
            elif key =="p":
                engine.sell_from_inventory(player,board[board_level])

            #Changing board level
            player_location_row, player_location_col = player["player_location"]
            board_walls = {"rows": [0, len(board[board_level])-1], "cols": [0, len(board[board_level][0])-1]}
            if player_location_row in board_walls["rows"] or player_location_col in board_walls["cols"]:
                if board_level == 0:
                    player["player_location"] = engine.player_location_after_door(board[board_level],player_location_row,player_location_col)
                    board_level = 1
                else:
                    if board[board_level][player_location_row][player_location_col] == OPEN_EXIT_DOOR_ICON:
                        player["player_location"] = engine.player_location_after_door(board[board_level],player_location_row,player_location_col)
                        board_level -= 1
                    else:
                        player["player_location"] = engine.player_location_after_door(board[board_level],player_location_row,player_location_col)
                        board_level += 1
            
    elif option == "quit":
        quit()


if __name__ == '__main__':
    main()