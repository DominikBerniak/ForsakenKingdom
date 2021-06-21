import os
import random
from util import clear_screen, get_input
from ui import print_error_message, print_message, display_menu

def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    pass


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
    weapons_description = ["Bloody","Blessed","Cursed","Doom","Big", "Metal" ,"War","Elvies","Small","Holy","Enchantend",""]
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

def load_module(option):
    if option == "q":
        return 0
    # elif option == 2:
    #     sales_controller.menu()
    # elif option == 3:
    #     hr_controller.menu()
    # elif option == 0:
    #      return 0
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
            print_error_message("There is no such option!")
        except ValueError:
            print_error_message("Please enter a number!")
    print_message("Good-bye!")
