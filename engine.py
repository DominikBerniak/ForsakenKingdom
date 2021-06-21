import os
from util import clear_screen, get_input
from ui import print_error_message, print_message

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



def print_menu(title, list_options):
    print(f"\n{title}:\n")
    for i in range(1,len(list_options)):
        print(f"({i}) {list_options[i]}")
    print(f"\n(0) {list_options[0]}\n")

def load_module(option):
    if option == 1:
        crm_controller.menu()
    elif option == 2:
        sales_controller.menu()
    elif option == 3:
        hr_controller.menu()
    elif option == 0:
        return 0
    else:
        raise KeyError()


def display_menu():
    options = ["Exit program",  # zamkniecie pod "q"
               "New Game",
               "Hall of Fame",  # optional
               "Authors"]
    print_menu("Main menu", options)

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