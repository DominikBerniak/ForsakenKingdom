import os
import random
from util import clear_screen, get_input
import ui

def create_board(width, height):
  
    '''Creates a new game board based on input parameters.
    Args:
    int: The width of the board
    int: The height of the board
    Returns:
    list: Game board
    '''
    board = [[" " for x in range(height)]for y in range(width)]
    for i in range(len(board)):
        board[i].insert(0, "|")
        board[i].append("|")
    horizontal_top_board_line = ["=" for x in range(len(board[0]))]
    horizontal_bottom_board_line = ["=" for x in range(len(board[0]))]
    board.insert(0,horizontal_top_board_line)
    board.append(horizontal_bottom_board_line)
    return board


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass

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
    type = ["weapons","weapons","weapons","armor","armor","consumable","gold"]

    randomized_type = random.choice(type)
    item_stats["type"] = randomized_type
    if randomized_type == "weapons":
        item_stats["name"] = random_item_name(weapons,weapons_description)
        item_stats["value"] = random.randint(MIN_ATTACK_VALUE,MAX_ATTACK_VALUE)
    elif randomized_type == "armor":
        item_stats["name"] = random_item_name(armor,armor_description)
        item_stats["value"] = random.randint(MIN_ARMOR_VALUE,MAX_ARMOR_VALUE)
    elif randomized_type == "consumable":
        item_stats["name"] = random_item_name(consumable,consumable_description)
        item_stats["value"] = random.randint(MIN_CONSUMABLE_VALUE,MAX_CONSUMABLE_VALUE)
    else:
        item_stats["name"] = "Gold"
        item_stats["value"] = random.randint(MIN_GOLD_VALUE,MAX_GOLD_VALUE)
    return item_stats

def authors():
    crew = ["Dominik Berniak",
            "Jakub Młocek",
            "Kordian Płusa",
            "Dawid Kuropka",
            "Kewin Gregorczyk"]
    print(crew)

def instruction():
    information = ["Welcome to Roguelike Game ! La Speluna, a company from San Escobar presents.. "]
    print(information)

def display_menu():
    options = ["Exit program",  # zamkniecie pod "q"
               "New Game",
               "Hall of Fame",  # optional
               "Authors",
               "Instruction"]
    ui.print_menu("Main menu", options)

def load_module(option):
    if option == 1:
        #start_game()
        pass
    elif option == 2:
        #hall_of_fame()
        pass
    elif option == 3:
        authors()
        pass
    elif option == 4:
        #Instruction()
        pass
    elif option == 0:
        return 0
    else:
        raise KeyError()

def menu():
    option = None
    while option != '0':
        clear_screen()
        display_menu()
        try:
            option = get_input("Select module")
            load_module(int(option))
        except KeyError:
            ui.print_error_message("There is no such option!")
        except ValueError:
            ui.print_error_message("Please enter a number!")
    ui.print_message("Good-bye!")

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
        "type" : "key",
        "name" : "torch",
        "value": 1
    }
    return torch

def create_key():
    torch = {
        "type" : "key",
        "name" : "key",
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
        "name": "Adalbert Grip",
        "quest_description": "You must correct answer to my question",
        "quest": "What is a StackOverflow?",
        "answer":"error",
        "reward":create_key()
    }
    return adalbert







