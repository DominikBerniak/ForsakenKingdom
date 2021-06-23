import random
import util
import ui
from time import sleep

def create_board(width, height):
    board = [[" " for x in range(width)]for y in range(height)]
    for i in range(len(board)):
        board[i].insert(0, "|")
        board[i].append("|")
    horizontal_top_board_line = ["=" for x in range(len(board[0]))]
    horizontal_bottom_board_line = ["=" for x in range(len(board[0]))]
    board.insert(0,horizontal_top_board_line)
    board.append(horizontal_bottom_board_line)
    return board

def create_player(player_start_row, player_start_col, player_icon):
    while True:
        ui.clear_screen()
        ui.display_title("Create your hero")
        player_stats = {"name":util.get_input("Your hero's name",1).title()}
        if player_stats["name"] == "Admin":
            player_stats.update({"race":"God" ,"health":1000000,"lvl":1000000,"exp":90,"attack":1000000,
                                "armor":1000000,"player_location": [player_start_row,player_start_col],"player_icon":player_icon, "inventory":[]})
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
        player_stats.update({"player_location": [player_start_row,player_start_col],
                                "player_icon":player_icon, "inventory": []})
        ui.clear_screen()
        if util.get_confirmation(f"""You've created {player_stats["name"]}, the {player_stats["race"]}.
    
    Do you want to play as {player_stats["name"]}? (yes/no)"""):
            break
    return player_stats

def is_unoccupied(board,row,col):
    return board[row][col] == " " or board[row][col] == "O"

def is_not_wall(board, row, col):
    return (board[row][col] != "=" and board[row][col] != "|")

def get_player_placement(board, player_icon):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == player_icon:
                return i,j

def put_player_on_board(board, player,player_icon):
    cords = get_player_placement(board, player_icon)
    if cords:
        board[cords[0]][cords[1]] = " "
    player_row, player_col, player_icon = player["player_location"][0],player["player_location"][1], player["player_icon"]
    board[player_row][player_col] = player_icon

def player_location_after_door(board,player_location_row,player_location_col):
    if player_location_row == 0:
        player_location_row = len(board)-2
    elif player_location_row == len(board)-1:
        player_location_row = 1
    elif player_location_col == 0:
        player_location_col = len(board[0])-2
    elif player_location_col == len(board[0])-1:
        player_location_col = 1
    return [player_location_row,player_location_col]
    
def get_next_level_old_door_location(board,row,col):
    if row == 0:
        row = len(board)-1
    elif row == len(board)-1:
        row = 0
    elif col == 0:
        col = len(board[0])-1
    elif col == len(board[0])-1:
        col = 0
    return [row,col]

def put_door_on_board(board,door_icon):
    for i in range(len(board)):
        enter_door_row = random.randint(0, len(board[i])-1)
        if enter_door_row in [0, len(board[i])-1]:
            enter_door_col = random.choice([1,len(board[i][0])-2])
        else:
            enter_door_col = random.choice([0, len(board[i][0])-1])
        if i < len(board)-1:
            board[i][enter_door_row][enter_door_col] = door_icon
        exit_door_row, exit_door_col = get_next_level_old_door_location(board[0], enter_door_row, enter_door_col)
        if i < len(board)-1:
            board[i+1][exit_door_row][exit_door_col] = "O" #open door

def find_the_door(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "X":
                return row,col

def open_the_door(board,player):
    enter_door_row,enter_door_col = find_the_door(board)
    print(enter_door_row,enter_door_col)
    util.press_any_button()
    if have_key_in_inventory(player["inventory"]) != False:
        util.clear_screen()
        board[enter_door_row][enter_door_col] =" "
        ui.display_board(board)
    else:
        util.clear_screen()
        ui.display_message("Not have a key!!! Go find it!!")
        util.press_any_button()
        ui.display_board(board)
        

def put_npc_quest_on_board(board,npc_quest_icon):
    for i in range(len(board)):
        npc_row = random.randint(1, len(board[i])-2)
        npc_col = random.randint(1, len(board[i][0])-2)
        while not is_unoccupied(board[i],npc_row,npc_col):
            npc_row = random.randint(1, len(board[i])-2)
            npc_col = random.randint(1, len(board[i][0])-2)
        board[i][npc_row][npc_col] = npc_quest_icon

def put_npc_shop_on_board(board,npc_shop_icon):
    for i in range(len(board)):
        npc_row = random.randint(1, len(board[i])-2)
        npc_col = random.randint(1, len(board[i][0])-2)
        while not is_unoccupied(board[i],npc_row,npc_col):
            npc_row = random.randint(1, len(board[i])-2)
            npc_col = random.randint(1, len(board[i][0])-2)
        board[i][npc_row][npc_col] = npc_shop_icon

def put_item_on_board(board,item_icon):
    for i in range(len(board)):
        item_row = random.randint(1, len(board[i])-2)
        item_col = random.randint(1, len(board[i][0])-2)
        for x in range (0,11):
            while not is_unoccupied(board[i],item_row,item_col):
                item_row = random.randint(1, len(board[i])-2)
                item_col = random.randint(1, len(board[i][0])-2)
                x-=1
            board[i][item_row][item_col] = item_icon

def put_enemy_on_board(board,enemy_icon):
    for i in range(len(board)):
        number_of_enemies = random.randint(10,15)
        while number_of_enemies > 0:
            npc_row = random.randint(1, len(board[i])-2)
            npc_col = random.randint(1, len(board[i][0])-2)
            while not is_unoccupied(board[i],npc_row,npc_col):
                npc_row = random.randint(1, len(board[i])-2)
                npc_col = random.randint(1, len(board[i][0])-2)
            board[i][npc_row][npc_col] = enemy_icon
            number_of_enemies -= 1

def random_item_name(type,type_description):
    item = random.choice(type)
    description_item = random.choice(type_description)
    return (description_item+" "+item).strip()

def create_item(is_shop=False):
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
    if not is_shop:
        type = ["Weapons","Weapons","Weapons","Armor","Armor","Health","Gold"]
    else:
        type = ["Weapons","Weapons","Weapons","Armor","Armor","Health","Health"]

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
    information = """Preparation for the game:
                First you need to create a character. Choose the races responsibly! 
                Each race has different stats. The character is moved by W/S/A/D. Also \"W\" is
                to attacking. 
                Objective:
                The most important objective is defeating the final boss,
                but before you get to this stage, you have to defeat a lot of enemies.
                During your adventure you will meet \"npc\" with whom you can trade,
                and they can give you a quests."""
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

def have_key_in_inventory(inventory):
    index =0
    for item in inventory:
        if item["type"] == "Key":
            return index
        index += 1
    return False

def do_quest(board,player,board_lvl):
    if board_lvl == 0:
        npc = create_kate()
    elif board_lvl == 1:
        npc = create_adalbert()
    else:
        npc = create_peter()
    if not have_key_in_inventory(player["inventory"]):
        util.clear_screen()
        ui.display_message(npc["name"] + ": "+npc["quest_description"])
        answer = util.get_input(npc["name"]+": "+npc["quest"])
        reward = npc["reward"]

        if answer == npc["answer"]:
            ui.display_message(npc["name"]+": "+"Correct, you got a key!!")
            add_to_inventory(player,reward)
        else:
            ui.display_message(npc["name"]+": "+"uuh, sry you must still learn this")
        util.press_any_button()
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

def update_gold_in_inventory(inventory,amount_of_gold):
    for index in range(len(inventory)):
        if inventory[index]["name"] == "Gold":
            if inventory[index]["value"] + amount_of_gold < 0:
                raise ValueError
            else:
                inventory[index]["value"] += amount_of_gold
                
def create_enemy(player):
    skeleton = {"adjective": "","name":"Skeleton","health":[5,50],"attack": 10,"armor":75, "exp": 10}
    ghoul = {"adjective": "","name":"Ghoul","health":[15,50],"attack": 20,"armor":5, "exp": 15}
    boar = {"adjective": "","name":"Boar","health":[50,200],"attack": 10,"armor":40, "exp": 25}
    spider = {"adjective": "","name":"Spider","health":[10,50],"attack": 15,"armor":20, "exp": 15}
    ghost = {"adjective": "","name":"Ghost","health":[1,5],"attack": 3,"armor":100, "exp": 5}
    ogre = {"adjective": "","name":"Ogre","health":[20,75],"attack": 25,"armor":100, "exp": 75}
    enemy = random.choice([skeleton, ghoul, boar, spider, ghost, ogre])

    enemy_adjectives = ["Mighty", "Fearless", "Powerful", "Deadly", "Ferocious", "Horrifying", "Frightening", "Spooky", "Ghostly"]
    enemy_adjective = random.choice(enemy_adjectives)
    if enemy["name"] == "Skeleton":
        enemy_adjective = random.choice([enemy_adjective, "Scary Spooky"])
    enemy["adjective"] = enemy_adjective
    
    player_level = player["lvl"]
    if player_level < 5: 
        enemy["health"][1] = enemy["health"][1]//2
        enemy["armor"] = enemy["armor"]//2
    enemy["health"] = random.randint(enemy["health"][0],enemy["health"][1])

    return enemy


def sell_from_inventory(player):
    unsold_items = ["gold","torch","key"]
    while True:
        ui.display_inventory(player["inventory"])
        name_item_to_sell = util.get_input("What you want sell").lower()
        index = 0
        if name_item_to_sell in unsold_items:
            continue
        for item in player["inventory"]:
            if name_item_to_sell == item["name"].lower():
                break
            index += 1
        try:
            del player["inventory"][index]
            update_gold_in_inventory(player["inventory"],10)
            util.clear_screen()
            ui.display_inventory(player["inventory"])
        except IndexError:
            ui.display_error_message(f"You don't have {name_item_to_sell.title()}")
        
        if util.get_confirmation("Wanna sell somthing else?"):
            util.clear_screen()
        else:
            break

def buy_from_shop(player,npc):
    shop = npc["shop"]
    while True:
        ui.display_inventory(shop)
        index = 0
        name_item_to_buy = util.get_input("Want you buy something?").lower()
        for item in shop:
                if name_item_to_buy == item["name"].lower():
                    break
                index += 1
        try:
            add_to_inventory(player,shop[index])
            del shop[index]
            gold = {
                "type" : "Gold",
                "name" : "Gold",
                "value": -(npc["cost_item"])
                }
            update_gold_in_inventory(player["inventory"],-(npc["cost_item"]))
            util.clear_screen()
            ui.display_inventory(player["inventory"])
        except IndexError:
            ui.display_error_message(f"I don't have {name_item_to_buy.title()}")
        except ValueError:
            ui.display_error_message(f"You don't have money to buy this")

        if util.get_confirmation("Wanna buy somthing else?"):
            util.clear_screen()
        else:
            break

def filter_items(inventory,type,part_of_armor=""):
    filtred_inventory = []
    if type == "Armor":
        for item in inventory:
            item_name = item["name"].split(" ")
            if part_of_armor in item_name:
                filtred_inventory.append(item)
    elif type == "Weapons":
        for item in inventory:
            if item["type"] == type:
                filtred_inventory.append(item)
    return filtred_inventory

def choose_item_to_wear(filtred_inventory,player,number_of_part_equipment):
    while True:
        util.clear_screen()
        ui.display_inventory(filtred_inventory)
        item_from_inventory = util.get_input("Choose item to wear").lower()
        for item in filtred_inventory:
            if item["name"].lower() == item_from_inventory:
                return item
        if item_from_inventory == "return":
            return player["equipment"][number_of_part_equipment]
        ui.display_error_message(f"You not have {item_from_inventory.title()} in item")
        util.press_any_button()

def wear_equipment(board,player):
    while True:
        util.clear_screen()
        ui.display_equipment(player)
        equipment = player["equipment"]
        part_of_equipment = util.get_input("Choose your part of equipment").title()
        if part_of_equipment == "Head":
            filtred_item = filter_items(player["inventory"],"Armor","Helmet")
            player["armor"] -= equipment[0]["value"]
            equipment[0] = choose_item_to_wear(filtred_item,player,0)
            player["armor"] += equipment[0]["value"]
        elif part_of_equipment == "Chest":
            filtred_item = filter_items(player["inventory"],"Armor","Chest")
            player["armor"] -= equipment[1]["value"]
            equipment[1] = choose_item_to_wear(filtred_item,player,1)
            player["armor"] += equipment[1]["value"]
        elif part_of_equipment == "Legs":
            filtred_item = filter_items(player["inventory"],"Armor","Trousers")
            player["armor"] -= equipment[2]["value"]
            equipment[2] = choose_item_to_wear(filtred_item,player,2)
            player["armor"] += equipment[2]["value"]
        elif part_of_equipment == "Shoes":
            filtred_item = filter_items(player["inventory"],"Armor","Shoes")
            player["armor"] -= equipment[3]["value"]
            equipment[3] = choose_item_to_wear(filtred_item,player,3)
            player["armor"] += equipment[3]["value"]
        elif part_of_equipment == "Weapon":
            filtred_item = filter_items(player["inventory"],"Weapons")
            player["attack"] -= equipment[4]["value"]
            equipment[4] = choose_item_to_wear(filtred_item,player,4)
            player["attack"] += equipment[4]["value"]
        else:
            break
    ui.display_board(board)
    
def fight_enemy(player):
    util.clear_screen()

def use_item(player):
    inventory = list(player["inventory"])
    inventory_to_display = [inventory[i] for i in range(len(inventory)) if inventory[i]["type"] == "Health"]
    if len(inventory_to_display)>0:
        while True:
            util.clear_screen()
            ui.display_inventory(inventory_to_display,"Consumables:\n")
            was_item_used = False
            ui.display_message("What do you want to use?".center(119),4,filler=0)
            ui.display_message("(name of item / return)\n".center(120),1,filler=0)
            player_input = input("".rjust(119//2)).title()
            if player_input == "Return":
                return False
            for i in range(len(inventory)):
                if inventory[i]["name"] == player_input:
                    player["health"] += inventory[i]["value"]
                    player["inventory"].pop(i)
                    was_item_used = True
                    break
            if was_item_used:
                return was_item_used
            else:
                ui.display_error_message("No such item in your inventory".center(119), 4,0)
                util.press_any_button(2,center=True)
    else:
        util.clear_screen()
        ui.display_error_message("There are no consumables in your inventory".center(119),4,0)
        util.press_any_button(2,center=True)
        return False


def fight_enemy(player,board):
    enemy = create_enemy(player)
    enemy["exp"] = 10
    enemy_turn = "Enemy"
    player_turn = "Player"
    # turn = random.choice([enemy_turn,player_turn])
    turn = player_turn

    util.clear_screen()
    ui.display_title(f'You have encountered the {enemy["adjective"]} {enemy["name"]}.')
    util.press_any_button(2)
    while True:
        util.clear_screen()
        ui.display_stats(enemy,board,1," ",5)
        ui.display_fight_art(board)
        ui.display_stats(player,board,1)

        #enemy turn
        if turn == enemy_turn:
            ui.display_message(f"It's {turn.lower()}'s turn to attack".center(len(board[0])),2,0)
            sleep(1.5)
            enemy_max_damage = (enemy["attack"] - player["armor"])
            if enemy_max_damage > 0:
                enemy_damage = random.randint(1,enemy_max_damage)
                player["health"] -= enemy_damage
            else:
                enemy_damage = 0
            ui.display_message(f"{enemy['name']} did {enemy_damage} damage".center(len(board[0])),2,filler=0)
            util.press_any_button(1,0,True)
            util.clear_screen()
            turn = player_turn

        #player turn
        else:
            ui.display_message(f"It's your turn to attack".center(len(board[0])),4,0)
            ui.display_message("Attack | Use Item\n".center(len(board[0])),2,0)
            player_input = input("".rjust(len(board[0])//2)).lower().replace(" ", "")
            if player_input in ["useitem", "u", "i"]:
                did_use_item = use_item(player)
                if did_use_item:
                    turn = enemy_turn
            else:
                player_max_damage = (player["attack"] - enemy["armor"])
                if player_max_damage > 0:
                    player_damage = random.randint(1,player_max_damage)
                    enemy["health"] -= player_damage
                else:
                    player_damage = 0
                if enemy["health"] > 0:
                    ui.display_message(f"You did {player_damage} damage".center(len(board[0])),2,filler=0)
                    util.press_any_button(1,0,True)
                    util.clear_screen()
                    turn = enemy_turn

        if enemy["health"]<=0 or player["health"]<=0:
            break

    if enemy["health"] <= 0:
        player["exp"] += enemy["exp"]
        if player["exp"] >= 100:
            while True:
                player["lvl"] += 1
                player["exp"] -= 100
                if player["exp"] < 100:
                    break
        util.clear_screen()
        ui.display_message(f"You have killed the {enemy['adjective']} {enemy['name']} and gained {enemy['exp']} experience".center(len(board[0])),4,0)
        util.press_any_button(1,0,True)
        return "victory"
    else:
        return "defeat"

def interaction_with_traders(player):
    ui.clear_screen()
    sell_or_buy = util.get_input("Do you want to buy or sell something?".center(119),2,0).lower()
    if sell_or_buy == "sell":
        sell_from_inventory(player)
    elif sell_or_buy == "buy":
        buy_from_shop(player)
    else:
        util.clear_screen()
        ui.display_error_message("I don't understand. See you later!".center(119),filler=0)
        util.press_any_button(1,0,True)


def encounter(board, player, player_row, player_col,quest_icon,shop_icon,enemy_icon,item_icon,board_level,door_icon):
    if board[player_row][player_col] == quest_icon:
        do_quest(board,player,board_level)
        return [0]
    elif board[player_row][player_col] == shop_icon:
        interaction_with_traders(player)
        return [0]
    elif board[player_row][player_col] == enemy_icon:
        result = fight_enemy(player,board)
        if result == "victory":
            return [1]
    elif board[player_row][player_col] == door_icon:
        open_the_door(board, player)
        return [0]
    elif board[player_row][player_col] == item_icon:
        #collect_item
        return [1]
