
def print_message(message):
    print(message)

def print_error_message(message):
    print("\n" + message)
    pass

def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    pass

def print_menu(title, list_options):
    print(f"\n{title}:\n")
    for i in range(1,len(list_options)):
        print(f"({i}) {list_options[i]}")
    print(f"\n(0) {list_options[0]}\n")

def display_menu():
    options = ["Exit program",  # zamkniecie pod "q"
               "New Game",
               "Hall of Fame",  # optional
               "Authors"]
    print_menu("Main menu", options)