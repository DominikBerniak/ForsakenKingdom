import random
import util
import ui
from time import sleep

def create_board(width, height):
  
    '''Creates a new game board based on input parameters.
    Args:
    int: The width of the board
    int: The height of the board
    Returns:
    list: Game board
    '''
    board = [[" " for x in range(width)]for y in range(height)]
    for i in range(len(board)):
        board[i].insert(0, "|")
        board[i].append("|")
    horizontal_top_board_line = ["=" for x in range(len(board[0]))]
    horizontal_bottom_board_line = ["=" for x in range(len(board[0]))]
    board.insert(0,horizontal_top_board_line)
    board.append(horizontal_bottom_board_line)
    return board

def is_unoccupied(board,row,col):
    return board[row][col] == " "

def get_player_placement(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "@":
                return i,j

def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    cords = get_player_placement(board)
    if cords:
        board[cords[0]][cords[1]] = " "
    player_row, player_col, player_icon = player["player_location"][0],player["player_location"][1], player["player_icon"]
    board[player_row][player_col] = player_icon

def get_confirmation(message):
    ui.clear_screen()
    confirmation = util.get_input(message,2).lower()
    return confirmation in ["yes", "y"]

def random_item_name(type,type_description):
    item = random.choice(type)
    description_item = random.choice(type_description)
    return description_item+" "+item

def create_item():
    MIN_ATTACK_VALUE = 1
    MAX_ATTACK_VALUE = 10
    MIN_ARMOR_VALUE = 1
    MAX_ARMOR_VALUE = 10
    MIN_GOLD_VALUE = 1
    MAX_GOLD_VALUE = 17
    MIN_CONSUMABLE_VALUE = 10
    MAX_CONSUMABLE_VALUE = 50

    item_stats = dict()
    weapons = ["Bow","Warglaive","Staff","Wand","Axe","Sword","Mace","Dagger","Fist","Crossbow"]
    weapons_description = ["Bloody","Blessed", "Cursed","Doom","Big", "Metal" ,"War","Elvies","Small","Holy","Enchantend",""]
    armor = ["Helmet", "Chest", "Trousers", "Shoes"]
    armor_description = ["Plate","Leather","Mail","Cloth"]
    consumable = ["Ham","Cheese","Elixir","Bread","Water"]
    consumable_description = ["Stinky","Tasty","Godlike"]
    type = ["Weapons","Weapons","Weapons","Armor","Armor","Health","Gold"]

    randomized_type = random.choice(type)
    item_stats["type"] = randomized_type
    if randomized_type == "Weapons":
        item_stats["name"] = random_item_name(weapons,weapons_description)
        item_stats["type"] = "Attack"
        item_stats["value"] = random.randint(MIN_ATTACK_VALUE,MAX_ATTACK_VALUE)
    elif randomized_type == "Armor":
        item_stats["name"] = random_item_name(armor,armor_description)
        item_stats["value"] = random.randint(MIN_ARMOR_VALUE,MAX_ARMOR_VALUE)
    elif randomized_type == "Health":
        item_stats["name"] = random_item_name(consumable,consumable_description)
        item_stats["value"] = random.randint(MIN_CONSUMABLE_VALUE,MAX_CONSUMABLE_VALUE)
    else:
        item_stats["name"] = "Gold"
        item_stats["value"] = random.randint(MIN_GOLD_VALUE,MAX_GOLD_VALUE)
    return item_stats

def authors():
    crew = ["Dawid Kuropka     : Full-Stack Developer",
            "Kewin Gregorczyk  : Full-Stack Developer",
            "Kordian Płusa     : Full-Stack Developer",
            "Jakub Młocek      : Full-Stack Developer",
            "Dominik Berniak   : Full-Stack Developer"]
    crew_display = ""
    i = 0
    x = 0
    while x in range(len(crew)*2):
        ui.clear_screen()
        ui.display_title("            Game authors:\n")
        if x == 0:
            crew_display = crew[i]
        elif x%2 != 0:
            crew_display = "\n    " + crew_display
            i+=1
        else:
            crew_display = crew[i] + "\n    " + crew_display
        ui.display_message(crew_display,1)
        sleep(0.2)
        x+=1
    util.press_any_button(3,8)
    util.clear_screen()

def instruction():
    ui.clear_screen()
    information = = """Preparation for the game:",
                "First you need to create a character. Choose the races responsibly! 
                "Each race has different stats. The character is moved by W/S/A/D. Also \"W\" is
                "to attacking. 
                "Objective:
                "The most important objective is defeating the final boss,
                "but before you get to this stage, you have to defeat a lot of enemies.
                "During your adventure you will meet \"npc\" with whom you can trade,
                "and they can give you a quests."""
    ui.display_message(information,2)
    util.press_any_button(2)
    util.clear_screen()

def hall_of_fame():
    ui.clear_screen()
    ui.display_message("Not implemented yet!",2)
    util.press_any_button(2)
    util.clear_screen()

def create_menu():
    options = ["Exit game", 
               "New Game",
               "Hall of Fame",  # optional
               "Authors",
               "Instruction"]
    ui.display_menu("Main menu", options)

def load_module(option):
    if option == 1:
        #start_game()
        return "start_game"
    elif option == 2:
        hall_of_fame()
    elif option == 3:
        authors()
    elif option == 4:
        instruction()
    elif option == 0:
        return "quit"
    else:
        raise KeyError()

def menu():
    while True:
        create_menu()
        try:
            option = util.get_input("Select option",2)
            # load_module(int(option))
            option = load_module(int(option))
            if option == "start_game" or option == "quit":
                return option

        except KeyError:
            util.clear_screen()
            ui.display_error_message("There is no such option!\n")
            util.press_any_button(1)
            util.clear_screen()
            
        except ValueError:
            util.clear_screen()
            ui.display_error_message("Please enter a number!\n")
            util.press_any_button(1)
            util.clear_screen()

def create_npc(name,cost_item,amount_items_in_shop):
    list_items_in_shop = []
    for i in range(amount_items_in_shop):
        list_items_in_shop.append(create_item())
    npc = {
        "icon": "$",
        "name": name,
        "cost_item": cost_item,
        "shop": list_items_in_shop
    }
    return npc

def create_torch():
    torch = {
        "type" : "Key",
        "name" : "Torch",
        "value": 1
    }
    return torch

def create_key():
    torch = {
        "type" : "Key",
        "name" : "Key",
        "value": 1
    }
    return torch

def create_peter():
    peter = {
        "icon": "?",
        "name":"Peter Iscoming",
        "quest_description":"You must correct answer to my question",
        "quest":"What is the name of command to add one or more files to the staging area?",
        "answer": "git add",
        "reward": create_torch()
    }
    return peter

def create_kate():
    kate = {
        "icon": "?",
        "name": "Kate Antlish",
        "quest_description": "You must correct answer to my question",
        "quest": "How reversed string where variable name word?",
        "answer":"word[::-1]",
        "reward":create_key()
    }
    return kate

def create_adalbert():
    adalbert = {
        "icon":"?",
        "name": "Adalbert Gribbs",
        "quest_description": "You must correct answer to my question",
        "quest": "What is a StackOverflow? ",
        "answer":"error",
        "reward":create_key()
    }
    return adalbert

def do_quest(npc,board,player):
    util.clear_screen()
    ui.display_message(npc["name"] + ": "+npc["quest_description"])
    ui.display_message("You: ")
    answer = input(npc["quest"])
    if answer == npc["answer"]:
        ui.display_message(npc["name"]+": "+"Correct, you got a key!!")
    else:
        ui.display_message(npc["name"]+": "+"uuh, sry you must still learn this")
    
    util.press_any_button()
    reward = npc["reward"]

    add_to_inventory(player,reward)
    util.clear_screen()
    ui.display_board(board)

def add_to_inventory(player, added_items):
    inventory = player["inventory"]
    is_in_inventory = False
    for items in inventory:
        if items["name"] == added_items["name"]:
            items["value"] += added_items["value"]
            is_in_inventory = True
    if not is_in_inventory:
        inventory.append(added_items)

def remove_from_inventory(inventory, removed_items):
    pass
