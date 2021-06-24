import util
import engine
import ui
from time import sleep
import winsound
from boards import level_1, level_2

PLAYER_ICON = '@'
CLOSED_DOOR_ICON = 'X'
OPEN_EXIT_DOOR_ICON = 'O'
NPC_SHOP_ICON = '$'
NPC_QUEST_ICON = "?"
ENEMY_ICON = 'T'
ITEM_ICON = '&'
TREASURE_ICON = "+"

PLAYER_START_ROW = 30
PLAYER_START_COL = 57

# PLAYER_ICON = '='
# PLAYER_START_ROW = 5
# PLAYER_START_COL = 10

BOARD_WIDTH = 115
BOARD_HEIGHT = 30


def player_dead(player):
    util.clear_screen()
    ui.display_title("You are dead")
    ui.display_message(f"You have achieved {player['lvl']} level.",2)
    util.press_any_button(4)
    return main()


def quit():
    ui.clear_screen()
    ui.display_message("Thank you for playing. Goodbye!".center(119),2,0)
    sleep(2)
    ui.clear_screen()

def main():
    util.clear_screen()
    option = engine.menu()
    if option == "start_game" or option == "load_game":
        if option == "start_game":
            util.clear_screen()
            player = engine.create_player(PLAYER_START_ROW,PLAYER_START_COL,PLAYER_ICON)
        boards = [level_1 ,level_2,engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)]
        board_level = [2]
        engine.put_door_on_board(boards,CLOSED_DOOR_ICON)
        engine.put_npc_shop_on_board(boards,NPC_SHOP_ICON)
        engine.put_npc_quest_on_board(boards,board_level[0],NPC_QUEST_ICON)
        engine.put_treasure_on_board(boards,board_level[0],TREASURE_ICON)
        engine.put_enemy_on_board(boards,ENEMY_ICON)
        engine.put_item_on_board(boards,ITEM_ICON)

        if option == "load_game":
            player = {}
            engine.load_game(player, boards, board_level)
        while True:
            util.clear_screen()
            engine.put_player_on_board(boards[board_level[0]], player, PLAYER_ICON)
            ui.display_board(boards[board_level[0]])
            ui.display_stats(player,boards[board_level[0]],2)
            player_location_row, player_location_col = player["player_location"]

            key = util.key_pressed()
            if key == "`":
                ui.clear_screen()
                pause_option = engine.pause_menu(player, boards, board_level)
                if pause_option == "exit_game":
                    util.clear_screen()
                    if util.get_confirmation("Do you really want to quit the game? (yes/no)"):
                        return quit()
                elif pause_option == "back_to_menu":
                    return main()

            elif key == "w" and engine.is_not_wall(boards[board_level[0]], player_location_row-1, player_location_col):
                if engine.is_unoccupied(boards[board_level[0]],player_location_row-1,player_location_col):
                    player["player_location"][0] -= 1
                    # winsound.Beep(150,100)
                    engine.move_enemies_randomly(boards[board_level[0]],ENEMY_ICON,player)
                else:
                    player_encounter = engine.encounter(boards[board_level[0]], player,player_location_row-1,player_location_col,NPC_QUEST_ICON,NPC_SHOP_ICON,ENEMY_ICON,ITEM_ICON,board_level[0],CLOSED_DOOR_ICON,TREASURE_ICON)
                    player["player_location"][0] -= player_encounter[0]
                    if len(player_encounter) > 1 and player_encounter[1] == "defeat":
                        return player_dead(player)

            elif key == "s" and engine.is_not_wall(boards[board_level[0]], player_location_row+1, player_location_col):
                if engine.is_unoccupied(boards[board_level[0]],player_location_row+1,player_location_col):
                    player["player_location"][0] += 1
                    # winsound.Beep(150,100)
                    engine.move_enemies_randomly(boards[board_level[0]],ENEMY_ICON,player)
                else:
                    player_encounter = engine.encounter(boards[board_level[0]], player,player_location_row+1, player_location_col,NPC_QUEST_ICON,NPC_SHOP_ICON,ENEMY_ICON,ITEM_ICON,board_level[0],CLOSED_DOOR_ICON,TREASURE_ICON)
                    player["player_location"][0] += player_encounter[0]
                    if len(player_encounter) > 1 and player_encounter[1] == "defeat":
                        return player_dead(player)

            elif key == "a" and engine.is_not_wall(boards[board_level[0]], player_location_row, player_location_col-1):
                if engine.is_unoccupied(boards[board_level[0]],player_location_row,player_location_col-1):
                    player["player_location"][1] -= 1 
                    # winsound.Beep(150,100)
                    engine.move_enemies_randomly(boards[board_level[0]],ENEMY_ICON,player)
                else:
                    player_encounter = engine.encounter(boards[board_level[0]], player,player_location_row,player_location_col-1,NPC_QUEST_ICON,NPC_SHOP_ICON,ENEMY_ICON,ITEM_ICON,board_level[0],CLOSED_DOOR_ICON,TREASURE_ICON) 
                    player["player_location"][1] -= player_encounter[0]
                    if len(player_encounter) > 1 and player_encounter[1] == "defeat":
                        return player_dead(player)

            elif key == "d" and engine.is_not_wall(boards[board_level[0]], player_location_row, player_location_col+1):
                if engine.is_unoccupied(boards[board_level[0]],player_location_row,player_location_col+1):
                    player["player_location"][1] += 1 
                    # winsound.Beep(150,100)
                    engine.move_enemies_randomly(boards[board_level[0]],ENEMY_ICON,player)
                else:
                    player_encounter = engine.encounter(boards[board_level[0]], player,player_location_row,player_location_col+1,NPC_QUEST_ICON,NPC_SHOP_ICON,ENEMY_ICON,ITEM_ICON,board_level[0],CLOSED_DOOR_ICON,TREASURE_ICON) 
                    player["player_location"][1] += player_encounter[0]
                    if len(player_encounter) > 1 and player_encounter[1] == "defeat":
                        return player_dead(player)

            elif key == "i":
                if len(player["inventory"])>0:
                    ui.display_inventory(player["inventory"])
                else:
                    util.clear_screen()
                    ui.display_message("Your inventory is empty.".center(119),3,0)
                util.press_any_button(4,0,True)

            elif key =="b":
                engine.wear_equipment(player)
                util.press_any_button(3 ,0,True)

            #Changing board level
            player_location_row, player_location_col = player["player_location"]
            board_walls = {"rows": [0, len(boards[board_level[0]])-1], "cols": [0, len(boards[board_level[0]][0])-1]}
            if player_location_row in board_walls["rows"] or player_location_col in board_walls["cols"]:
                if board_level[0] == 0:
                    player["player_location"] = engine.player_location_after_door(boards[board_level[0]],player_location_row,player_location_col)
                    board_level[0] = 1
                else:
                    if boards[board_level[0]][player_location_row][player_location_col] == OPEN_EXIT_DOOR_ICON:
                        player["player_location"] = engine.player_location_after_door(boards[board_level[0]],player_location_row,player_location_col)
                        board_level[0] -= 1
                    else:
                        player["player_location"] = engine.player_location_after_door(boards[board_level[0]],player_location_row,player_location_col)
                        board_level[0] += 1
            
    elif option == "quit":
        quit()

if __name__ == '__main__':
    main()