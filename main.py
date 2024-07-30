import numpy as np
from game_functions import TicTacToe
from ascii_art import logo


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


def reset_board(game_board):
    for row in range(0, 3):
        for n in range(0, 3):
            game_board[row, n] = 0


def print_sample_board(sample):
    for digit in sample:
        print(digit[0], digit[1], '|', digit[2], '|', digit[3])


tic_tac_toe = TicTacToe()

# Setup
ttt_sample = np.array([['1:     ', 1, 2, 3],
                       ['2:     ', 1, 2, 3],
                       ['3:     ', 1, 2, 3]])

board = np.array([[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]])

choosing = True
single_player = False
game_over = False
player_move = True
mode = ''
current_input = ''
players = ''
winner = ''
player_score = 0
computer_score = 0
player_1_score = 0
player_2_score = 0

print(logo)
print('Welcome to Noughts and Crosses, the British version of Tic Tac Toe!\n')
print('The rules are very simple, there will be a 3x3 grid of empty spaces and you will either play')
print('against the computer or another player. Whoever gets 3 in a row first wins!')
# Choose # of players
while choosing:
    num_players = input("\nType 'one' if you are playing against the computer or 'two' for two player mode: ")
    if num_players == 'one':
        single_player = True
        choosing = False
    elif num_players == 'two':
        choosing = False
        mode = 1
    else:
        print("Input not recognised, please type 'one' or 'two' to continue.")

# Rules of game
print('\n')
print('Sample board:\nrow     column')
print_sample_board(ttt_sample)
print('To play a move type two digits one being the column and row where your digit resides.\nUse the sample '
      'board above to check the values. Rows go vertically, whereas the column goes horizontally.\n')

print_board(board)
print('^ Current game ^')

# Single Player Game
while not game_over and single_player:
    mode = 'one'
    # Player Move
    if player_move:
        current_input = tic_tac_toe.player_turn(board, mode)
        if current_input == 'break':
            break
    else:
        current_input = tic_tac_toe.computer_turn(board)

    # Play move and change player
    if mode == 'one' and player_move:
        board[current_input[0], current_input[1]] = 1
        player_move = False
    else:
        board[current_input[0], current_input[1]] = 2
        player_move = True

    # Check score
    end_state = tic_tac_toe.check_score(board)
    print_board(board)
    if end_state == 'winner' and not player_move:
        print('\nPlayer wins! Congrats m8.')
        winner = 'player'
        player_score += 1
    elif end_state == 'winner' and player_move:
        print('\nYou lose, disgraceful...')
        winner = 'computer'
        computer_score += 1
    elif end_state == 'draw':
        print('\nDraw, no winners this time.')

    # Reset board and play again or end game.
    while end_state == 'winner' or end_state == 'draw':
        print('\nRunning Score:')
        print(f'Player has {player_score} points.')
        print(f'Computer has {computer_score} points.')
        play_again = input('Would you like to play again? Y/N: ').lower()
        if play_again == 'y' or play_again == 'yes':
            print('Restarting game')
            reset_board(board)
            print_board(board)
            end_state = 'play_again'
            if winner == 'player':
                player_move = True
        elif play_again == 'n' or play_again == 'no':
            print('Thanks for playing!')
            end_state = 'game_over'
            game_over = True
        else:
            print('Input not recognised, please try again.')

# Two Player Game
while not game_over and not single_player:
    # Player Move
    if player_move:
        current_input = tic_tac_toe.player_turn(board, mode)
        if current_input == 'break':
            break

    # Play Move and change player if two player.
    if mode == 1:
        board[current_input[0], current_input[1]] = 1
        mode = 2
    elif mode == 2:
        board[current_input[0], current_input[1]] = 2
        mode = 1

    # Check score
    end_state = tic_tac_toe.check_score(board)
    print('current score:')
    print_board(board)
    if end_state == 'winner' and mode == 2:
        print('\nPlayer 1 wins! Congratulations.')
        play_again = input('Would you like to play again?')
        winner = 1
        player_1_score += 1
    elif end_state == 'winner' and mode == 1:
        print('\nPlayer 2 wins! Congratulations.')
        winner = 2
        player_2_score += 1
    elif end_state == 'draw':
        print('\nDraw, no winners this time.')

    # Reset board and play again or end game.
    while end_state == 'winner' or end_state == 'draw':
        print('\nRunning Score:')
        print(f'Player 1 has {player_1_score} points.')
        print(f'Player 2 has {player_2_score} points.')
        play_again = input('Would you like to play again? Y/N: ').lower()
        if play_again == 'y' or play_again == 'yes':
            print('Restarting game')
            reset_board(board)
            print_board(board)
            if winner == 1:
                mode = 1
        elif play_again == 'n' or play_again == 'no':
            print('Thanks for playing!')
            game_over = True
        else:
            print('Input not recognised, please try again.')
