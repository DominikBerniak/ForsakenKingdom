from util import clear_screen

def display_message(message, new_lines=0):
    new_lines = "\n"*new_lines
    print(f"{new_lines}    {message}")

def display_error_message(message):
    print("\n\n    " + message)

def display_title(title):
    print(f"\n\n    {title}")

def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    print("\n")
    for i in range(len(board)):
        row = "    " + "".join(board[i])
        row = row.replace("O", " ")
        print(row)

def display_stats(player_stats,board):
    """
    player_stats.keys() = {"name", "race", "health", "lvl", "exp", 
                        "attack", "armor", "player_location", "player_icon"}
    """

    stats = list(player_stats.items())
    #removing "player_location" and "player_icon" and "inventory"
    stats = [stats[i] for i in range(len(stats)) if i <7]

    for i in range(len(stats)):
        if i <2:
            stats[i] = stats[i][1]
        else:
            stats[i] = (stats[i][0] + ": " + str(stats[i][1])).title()
    longest_word = 0
    for i in range(2,len(stats)):
        if len(str(stats[i])) > longest_word:
            longest_word = len(str(stats[i]))
    stats_to_display = [[],[]]
    stats_to_display[0] = [stats[x] for x in range(len(stats)) if x <5]
    stats_to_display[1] = [stats[x] for x in range(len(stats)) if x >4]
    cell_width = longest_word + 2
    
    first_row = f"{stats_to_display[0][0]}, the {stats_to_display[0][1]} "
    name_race_width = len(first_row)
    for i in range(2,len(stats_to_display[0])):
        word_lenght = len(stats_to_display[0][i])
        filler = (cell_width - word_lenght) // 2 * " "
        filler_2 = (cell_width - word_lenght - len(filler)) * " "
        first_row += "|" + filler + stats_to_display[0][i] +  filler_2

    second_row = " "
    for i in range(len(stats_to_display[1])):
        word_lenght = len(stats_to_display[1][i])
        filler = (cell_width - word_lenght) // 2 * " "
        filler_2 = (cell_width - word_lenght - len(filler)) * " "
        second_row += filler + stats_to_display[1][i] +  filler_2 + "|"
    
    board_width = len(board[0])
    left_indent = "\n" + ' '*((board_width//2) - (len(first_row)//2)+4)
    first_row = left_indent + first_row
    second_row = left_indent + ' ' *name_race_width + second_row
    print(first_row)
    print(second_row[:-1])

def display_menu(title, list_options):
    display_title(f"   {title}\n")
    for i in range(1,len(list_options)):
        print(f"    ({i}) {list_options[i]}")
    print(f"\n    (0) {list_options[0]}\n")

def display_race_choices(races):
    clear_screen()
    longest_race = 0
    for i in range(len(races)):
        if len(races[i]["race"]) > longest_race:
            longest_race = len(races[i]["race"])
    print("\n\n    Choose your characters race:")
    for i in range(len(races)):
        race_length = len(races[i]["race"])
        filler = " "*(longest_race-race_length+4)
        print(f'\n\n      {(race_length+1)*" "}{filler}Health  =  {races[i]["health"]}')
        print(f'      {races[i]["race"]}:{filler}Attack  =  {races[i]["attack"]}')
        print(f'      {(race_length+1)*" "}{filler}Armor   =  {races[i]["armor"]}')
        if i < len(races)-1:
            print("\n    ============================")
            
def display_inventory(inventory):
    # inventory = [{'type': str, 'name': str, 'value': int}, ...]
    inventory = sorted(inventory, key=lambda x: x["type"])
    longest_name = 0
    longest_type = 0 
    for i in range(len(inventory)):
        if len(inventory[i]["name"]) > longest_name:
            longest_name = len(inventory[i]["name"])
        elif len(inventory[i]["type"]) > longest_type:
            longest_type = len(inventory[i]["type"])
    clear_screen()
    display_title("Inventory:\n")
    for i in range(len(inventory)):
        name_lenght = len(inventory[i]["name"])
        type_lenght = len(inventory[i]["type"])
        filler_name = (longest_name - name_lenght + 2)*" "
        filler_type = (longest_type - type_lenght + 2)*" "
        display_message(f"{inventory[i]['name']}{filler_name}:  {inventory[i]['type']}{filler_type}=  {inventory[i]['value']}",1)


"""ASCI ART"""

