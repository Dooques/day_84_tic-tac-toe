import numpy as np
from game_functions import TicTacToe


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
    for digit in sample:
        print(digit[0], digit[1], '|', digit[2], '|', digit[3])


tic_tac_toe = TicTacToe()

# Setup
ttt_sample = np.array([['1:', 1, 2, 3],
                       ['2:', 1, 2, 3],
                       ['3:', 1, 2, 3]])

ttt_setup = np.array([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]])

single_player = False
game_over = False
player_move = True
current_input = ''
board = ttt_setup
players = ''

# Choose # of players
num_players = input("Type 'one' if you are playing against the computer or 'two' for two player mode: ")
if num_players == 'one':
    single_player = True

# Rules of game
print('\n')
print_sample_board(ttt_sample)
print('To play a move type two digits one being the column and row where your digit resides. Use the sample '
      'board above to check the values. Rows go vertically, whereas the column goes horizontally.\n')

print_board(ttt_setup)
print('Current game ^\n')

# Play game
while single_player and not game_over:
    if player_move:
        current_input = tic_tac_toe.player_turn(board)
        if current_input == 'break':
            break
        player_move = False
    else:
        current_input = tic_tac_toe.computer_turn(board)
        player_move = True
    print(current_input)
    if player_move:
        board[current_input[0], current_input[1]] = 1
    else:
        board[current_input[0], current_input[1]] = 2
    game_over = tic_tac_toe.check_score(board)
    print_board(board)
    if game_over and not player_move:
        print('\nPlayer wins! Congrats m8.')
    elif game_over and player_move:
        print('\nYou lose, disgraceful...')


