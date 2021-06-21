def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    print("\n")
    for i in range(len(board)):
        row = "    " + "".join(board[i])
        print(row)

def display_stats(player_stats,board):
    #player_stats.keys = {"name", "race", "health", "lvl", "exp", "attack", "armor"}
    stats = list(player_stats.items())
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