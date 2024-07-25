import random


class TicTacToe:
    def __init__(self):
        pass

    def player_turn(self, game_board):
        plyr_input = input('\nPlease type a row and a column number separated by a comma.\nType here: ')
        row_num = 0
        spaces_used = []
        for row in game_board:
            col_num = 0
            for item in row:
                if item == 1 or item == 2:
                    spaces_used.append((row_num, col_num))
                col_num += 1
            row_num += 1
        if plyr_input == 'exit':
            return 'break'
        split_input = plyr_input.split(',')
        clean_input = int(split_input[0]) - 1, int(split_input[1]) - 1
        if clean_input in spaces_used:
            print('This space is already occupied, please try again.')
            self.player_turn(game_board)
        print(clean_input)
        return clean_input

    def computer_turn(self, game_board):
        print("\nComputer's Turn")
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
        print(f'spaces used: {spaces_used}')
        digit_1 = random.randint(0, 2)
        digit_2 = random.randint(0, 2)
        move = (digit_1, digit_2)
        print(f'computer move: {(digit_1, digit_2)}')
        while move in spaces_used:
            digit_1 = random.randint(0, 2)
            digit_2 = random.randint(0, 2)
            move = (digit_1, digit_2)
        else:
            return move

    def check_score(self, game_board):
        rows = [game_board[item, :] for item in range(0, 3)]
        cols = [game_board[:, item] for item in range(0, 3)]
        diag_tl_to_br = [game_board[0, 0], game_board[1, 1], game_board[2,2]]
        diag_bl_to_tr = [game_board[2, 0], game_board[1, 1], game_board[0, 2]]
        diags = [diag_tl_to_br, diag_bl_to_tr]
        for line in rows:
            print(f'row: {line}')
            if line[1] == line[0]:
                if line[2] == line[0]:
                    if line[0] == 1 or line[0] == 2:
                        return True
        for line in cols:
            print(f'col: {line}')
            if line[1] == line[0]:
                if line[2] == line[0] and line[0] == 1 or line[0] == 2:
                    if line[0] == 1 or line[0] == 2:
                        return True
        for line in diags:
            print(f'diag: {line}')
            if line[1] == line[0]:
                if line[2] == line[0] and line[0] == 1 or line[0] == 2:
                    if line[0] == 1 or line[0] == 2:
                        return True
