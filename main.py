import numpy as np
import random


def print_board(game_board):
    blank = '_'
    x = 'x'
    o = 'o'
    row_index = 0
    row_1 = []
    row_2 = []
    row_3 = []
    rows = [row_1, row_2, row_3]
    for row in range(3):
        index = 0
        for char in range(3):
            if game_board[row_index, index] == 0:
                rows[row_index].append(f'{blank}')
                index += 1
            elif game_board[row_index, index] == 1:
                rows[row_index].append(f'{x}')
                index += 1
            else:
                rows[row_index].append(f'{o}')
                index += 1
        row_index += 1
    for row in rows:
        for char in row:
            if row.index(char) == 0 or row.index(char) == 1:
                char_index = row.index(char)
                row[char_index] = f'{char} |'
    for row in rows:
        print(row[0], row[1], row[2])


def print_sample_board(sample):
    for item in sample:
        print(item[0], item[1], '|', item[2], '|', item[3])


def player_turn():
    plyr_input = input('Please type a row and a column number separated by a comma.\nType here: ')
    if plyr_input == 'exit':
        return 'break'
    split_input = plyr_input.split(',')
    clean_input = int(split_input[0]) - 1, int(split_input[1]) - 1
    return clean_input


def computer_turn(game_board):
    row_num = 0
    spaces_used = []
    for row in game_board:
        col_num = 0
        for item in row:
            if item == 1 or item == 2:
                spaces_used.append((row_num, col_num))
            col_num += 1
        row_num += 1
    print(spaces_used)
    digit_1 = random.randint(0, 2)
    digit_2 = random.randint(0, 2)
    if digit_1 not in spaces_used and digit_2 not in spaces_used:
        return digit_1, digit_2


ttt_sample = np.array([['1:', 1, 2, 3],
                       ['2:', 1, 2, 3],
                       ['3:', 1, 2, 3]])
ttt_setup = np.array([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]])

print_board(ttt_setup)

single_player = False
player_move = True
current_input = ''
board = ttt_setup
players = ''

# Choose # of players
num_players = input("Type 'one' if you are playing against the computer or 'two' for two player mode: ")
if num_players == 'one':
    single_player = True

# Rules of game
print_sample_board(ttt_sample)
print('To play a move type two digits one being the column and row where your digit resides. Use the sample '
      'board above to check the values. Rows go vertically, whereas the column goes horizontally.')
print_board(ttt_setup)
print('Current game ^')

# Play game
while single_player:
    if player_move:
        current_input = player_turn()
        if current_input == 'break':
            break
        player_move = False
    else:
        current_input = computer_turn(board)
        player_move = True
    print(current_input)
    if player_move:
        board[current_input[0], current_input[1]] = 1
    else:
        board[current_input[0], current_input[1]] = 2
    print_board(board)



