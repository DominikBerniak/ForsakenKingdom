from util import clear_screen
from engine import get_boss_location

def display_message(message, new_lines=0,filler = 4):
    new_lines = "\n"*new_lines
    print(f"{new_lines}{filler*' '}{message}")

def display_error_message(message,new_lines=2,filler=4):
    new_lines = "\n"*new_lines
    print(f"{new_lines}{filler*' '}{message}")

def display_title(title,new_lines=2,filler=4):
    new_lines = "\n"*new_lines
    print(f"{new_lines}{filler*' '}{title}")

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

def display_dark_board(board,player):
    torch_range = 4
    print("\n")
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j > player["player_location"][1]-torch_range and j <player["player_location"][1]+ torch_range and i > player["player_location"][0] - torch_range and i < player["player_location"][0] + torch_range:
                if board[i][j] != " ":
                    print(board[i][j],end="")
                else:
                    print(".",end="")
            else:
                print(" ",end="")
        print()

def display_boss_board(board):
    boss_range = 1
    boss_location = get_boss_location(board)
    print("\n")
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j == boss_location[1]-boss_range and j == boss_location["boss_location"][1]+ boss_range and i == boss_location["boss_location"][0] - boss_range and i == boss_location["boss_location"][0] + boss_range:
                print("*",end="")
            elif j > boss_location[1]-boss_range and j <boss_location["boss_location"][1]+ boss_range and i > boss_location["boss_location"][0] - boss_range and i < boss_location["boss_location"][0] + boss_range:
                print(".",end="")
            else:
                print(board[i][j],end="")
        print()



def display_equipment(player):
    display_title("Your Equipment",4)
    equipment = player["equipment"]
    equipment_headers = ["Head","Chest","Legs","Shoes","Weapons"]
    for i in range(len(equipment_headers)):
        print(f"\n\n    {equipment_headers[i]} : {equipment[i]['name']}   {equipment[i]['type']}= {equipment[i]['value']}")

def display_stats(player_stats,board,new_lines=0, divider = ", the ", cut = 7):
    """
    player_stats.keys() = {"name", "race", "health", "lvl", "exp", 
                        "attack", "armor", "player_location", "player_icon", "inventory"}
    """

    stats = list(player_stats.items())
    #removing "player_location" and "player_icon" and "inventory"
    stats = [stats[i] for i in range(len(stats)) if i <cut]

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
    
    first_row = f"{stats_to_display[0][0]}{divider}{stats_to_display[0][1]} "
    # name_race_width = len(first_row)
    # for i in range(2,len(stats_to_display[0])):
    #     word_lenght = len(stats_to_display[0][i])
    #     filler = (cell_width - word_lenght) // 2 * " "
    #     filler_2 = (cell_width - word_lenght - len(filler)) * " "
    #     first_row += "|" + filler + stats_to_display[0][i] +  filler_2

    for i in range(2,len(stats_to_display[0])):
        first_row += "| " + stats_to_display[0][i] + " "

    # second_row = " "
    # for i in range(len(stats_to_display[1])):
    #     word_lenght = len(stats_to_display[1][i])
    #     filler = (cell_width - word_lenght) // 2 * " "
    #     filler_2 = (cell_width - word_lenght - len(filler)) * " "
    #     second_row += filler + stats_to_display[1][i] +  filler_2 + "|"
    
    second_row = ""
    for i in range(len(stats_to_display[1])):
        second_row += stats_to_display[1][i] + " | "

    # board_width = len(board[0])
    # left_indent = "\n" + ' '*((board_width//2) - (len(first_row)//2)+4)
    # first_row = left_indent + first_row
    # second_row = left_indent + ' ' *name_race_width + second_row
    new_lines = "\n" * new_lines
    print(new_lines)
    print(f"{first_row}".center(len(board[0])+3))
    print()
    print(f"{second_row[:-2]}".center(len(board[0])+6))





# def display_menu(title, list_options):
#     display_title(f"   {title}\n")
#     for i in range(1,len(list_options)):
#         print(f"    ({i}) {list_options[i]}")
#     print(f"\n    (0) {list_options[0]}\n")


            #testing centered menu

def display_menu(title, list_options):
    longest_option_lenght = len(max(list_options, key=len))
    display_title(f"{title}\n\n".center(119),4,0)
    list_of_indieces = list(range(1,len(list_options)))
    list_of_indieces.append(0)
    for i in list_of_indieces:
        option_lenght = len(list_options[i])
        filler = (longest_option_lenght - option_lenght) * " "
        print(f"({i}) {list_options[i]}{filler}\n".center(119))

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
            
def display_inventory(inventory, lable = "Inventory:\n"):
    # inventory = [{'type': str, 'name': str, 'value': int}, ...]
    inventory = sorted(inventory, key=lambda x: x["type"])
    longest_name = len(inventory[0]["name"])
    longest_type = len(inventory[0]["type"])
    longest_value = len(str(inventory[0]["value"]))
    is_gold_in_inventory = False
    if len(inventory) > 1:
        for i in range(len(inventory)):
            if len(inventory[i]["name"]) > longest_name:
                longest_name = len(inventory[i]["name"])
            elif len(inventory[i]["type"]) > longest_type:
                longest_type = len(inventory[i]["type"])
            elif len(str(inventory[i]["value"])) > longest_value:
                longest_value = len(str(inventory[i]["value"]))
    else:
        longest_name = len(inventory[0]["name"])
        longest_type = len(inventory[0]["type"])
        longest_value = len(str(inventory[0]["value"]))

    clear_screen()
    display_title(f"{lable}".center(119),3,filler=0)
    for i in range(len(inventory)):
        name_lenght = len(inventory[i]["name"])
        type_lenght = len(inventory[i]["type"])
        value_lenght = len(str(inventory[i]["value"]))
        filler_name = (longest_name - name_lenght + 2)*" "
        filler_type = (longest_type - type_lenght + 2)*" "
        filler_value = (longest_value - value_lenght + 2)*" "
        if inventory[i]["name"] != "Gold":
            display_message(f"{inventory[i]['name']}{filler_name}:  {inventory[i]['type']}{filler_type}=  {inventory[i]['value']}{filler_value}".center(119),1,filler=0)
        else:
            is_gold_in_inventory = True
            gold = inventory[i]
    if is_gold_in_inventory:
        gold_filler_name = (longest_name + 2)*" "
        gold_filler_type = (longest_type - len(gold["type"]) + 2)*" "
        gold_filler_value = (longest_value - len(str(gold["value"])) + 2)*" "
        print()
        display_message(f"{gold_filler_name}   {gold['type']}{gold_filler_type}=  {gold['value']}{gold_filler_value}".center(119),1,filler=0)


"""ASCI ART"""

def display_fight_art(board):
    art = """   |\                     /)
 /\_\\\__               (_//
|   `>\-`     _._       //`)
 \ /` \\\  _.-`:::`-._  //
  `    \|`    :::    `|/
        |     :::     |
        |.....:::.....|
        |:::::::::::::|
        |     :::     |
        \     :::     /
         \    :::    /
          `-. ::: .-'
           //`:::`\\\\
          //   '   \\\\
         //         \\\\"""
    art = art.split("\n")
    longest_row_length = len(max(art))
    for i in range(len(art)):
        row_lenght = len(art[i])
        filler = (longest_row_length - row_lenght) * " "
        print(f"{art[i]}{filler}".center(len(board[0])-4))