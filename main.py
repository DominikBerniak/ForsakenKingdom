import util
import engine
import ui
import os
from time import sleep

PLAYER_ICON = '@'
CLOSED_DOOR_ICON = 'X'
OPEN_EXIT_DOOR_ICON = 'O'
NPC_SHOP_ICON = '$'
NPC_QUEST_ICON = "?"
ENEMY_ICON = 'T'

PLAYER_START_ROW = 5
PLAYER_START_COL = 100

BOARD_WIDTH = 115
BOARD_HEIGHT = 30

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
        player = engine.create_player(PLAYER_START_ROW,PLAYER_START_COL,PLAYER_ICON)
        board = [engine.create_board(BOARD_WIDTH, BOARD_HEIGHT),engine.create_board(BOARD_WIDTH, BOARD_HEIGHT),engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)]
        engine.put_door_on_board(board,CLOSED_DOOR_ICON)
        engine.put_npc_shop_on_board(board,NPC_SHOP_ICON)
        engine.put_enemy_on_board(board,ENEMY_ICON)
        board_level = 0


        player["inventory"].extend([{'type': 'Armor', 'name': 'Mail Shoes', 'value': 1}, {'type': 'Armor', 'name': 'Cloth Helmet', 'value': 8},
        {'type': 'Armor', 'name': 'Plate Helmet', 'value': 29},{'type': 'Armor', 'name': 'Mail Chest', 'value': 2},{'type': 'Weapons', 'name': 'Wooden Sword', 'value': 2}])

        util.clear_screen()
        while True:
            util.clear_screen()
            engine.put_player_on_board(board[board_level], player, PLAYER_ICON)
            ui.display_board(board[board_level])
            ui.display_stats(player,board[board_level])
            player_location_row, player_location_col = player["player_location"]

            key = util.key_pressed()
            if key == "`":
                ui.clear_screen()
                if util.get_confirmation("Do you really want to quit the game? (yes/no)"):
                    return quit()
            elif key == "w" and engine.is_not_wall(board[board_level], player_location_row-1, player_location_col,CLOSED_DOOR_ICON):
                if engine.is_unoccupied(board[board_level],player_location_row-1,player_location_col):
                    player["player_location"][0] -= 1
                else:
                    player["player_location"][0] -= engine.encounter(board[board_level], player,player_location_row-1,player_location_col,NPC_QUEST_ICON,NPC_SHOP_ICON,ENEMY_ICON,board_level)

            elif key == "s" and engine.is_not_wall(board[board_level], player_location_row+1, player_location_col,CLOSED_DOOR_ICON):
                if engine.is_unoccupied(board[board_level],player_location_row+1,player_location_col):
                    player["player_location"][0] += 1
                else:
                    player["player_location"][0] += engine.encounter(board[board_level], player,player_location_row+1, player_location_col,NPC_QUEST_ICON,NPC_SHOP_ICON,ENEMY_ICON,board_level)

            elif key == "a" and engine.is_not_wall(board[board_level], player_location_row, player_location_col-1,CLOSED_DOOR_ICON):
                if engine.is_unoccupied(board[board_level],player_location_row,player_location_col-1):
                    player["player_location"][1] -= 1 
                else:
                    player["player_location"][1] -= engine.encounter(board[board_level], player,player_location_row,player_location_col-1,NPC_QUEST_ICON,NPC_SHOP_ICON,ENEMY_ICON,board_level) 

            elif key == "d" and engine.is_not_wall(board[board_level], player_location_row, player_location_col+1,CLOSED_DOOR_ICON):
                if engine.is_unoccupied(board[board_level],player_location_row,player_location_col+1):
                    player["player_location"][1] += 1 
                else:
                    player["player_location"][1] += engine.encounter(board[board_level], player,player_location_row,player_location_col+1,NPC_QUEST_ICON,NPC_SHOP_ICON,ENEMY_ICON,board_level) 

            elif key == "i":
                ui.display_inventory(player["inventory"])
                util.press_any_button(4)

            elif key =="b":
                engine.wear_equipment(board[board_level],player)

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