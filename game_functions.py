import random


class TicTacToe:
    def __init__(self):
        self.row_index = [[], [], []]
        for row in range(0, 3):
            for item in range(0, 3):
                self.row_index[row].append((row, item))
        self.col_index = [[], [], []]
        for col in range(0, 3):
            for item in range(0, 3):
                self.col_index[col].append((item, col))
        self.diag_index = [[(1, 1), (2, 2), (3, 3)], [(3, 1), (2, 2), (1, 3)]]

    def player_turn(self, game_board, game_mode):
        choosing_move = True
        while choosing_move:
            plyr_input = ''
            if game_mode == 'one':
                plyr_input = input('\nPlease type a row and a column number separated by a comma.\nType here: ')
            elif game_mode == 1:
                plyr_input = input('\nPlayer 1, please type a row and a column number separated by a comma.'
                                   '\nType here: ')
            elif game_mode == 2:
                plyr_input = input('\nPlayer 2, please type a row and a column number separated by a comma.'
                                   '\nType here: ')
            if plyr_input == 'exit':
                return 'break'
            spaces_used = self.spaces_used(game_board)
            try:
                split_input = plyr_input.split(',')
                clean_input = int(split_input[0]) - 1, int(split_input[1]) - 1
                if clean_input in spaces_used:
                    print('This space is already occupied, please try again.')
                    self.player_turn(game_board, game_mode)
                elif clean_input[0] > 2 or clean_input[1] > 2 or clean_input[0] < 0 or clean_input[1] < 0:
                    print('Input out of range')
                    self.player_turn(game_board, game_mode)
                else:
                    return clean_input
            except ValueError:
                print('Input not recognised, please try again.')
            except IndexError:
                print('Input not recognised, please try again.')

    def computer_turn(self, game_board):
        print("\nComputer's Turn")
        spaces_used = self.spaces_used(game_board)
        # potential_spots = self.computer_ai(game_board)
        # print(potential_spots)
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
        h_lines_filled = False
        v_lines_filled = False
        d_lines_filled = False
        rows = [game_board[item, :] for item in range(0, 3)]
        cols = [game_board[:, item] for item in range(0, 3)]
        diag_tl_to_br = [game_board[0, 0].item(), game_board[1, 1].item(), game_board[2,2].item()]
        diag_bl_to_tr = [game_board[2, 0].item(), game_board[1, 1].item(), game_board[0, 2].item()]
        diags = [diag_tl_to_br, diag_bl_to_tr]
        spaces_filled = []

        for line in rows:
            if line[1] == line[0]:
                if line[2] == line[0]:
                    if line[0] == 1 or line[0] == 2:
                        return 'winner'
            for space in line:
                if space != 0:
                    spaces_filled.append('x')
        if len(spaces_filled) == 9:
            h_lines_filled = True

        for line in cols:
            if line[1] == line[0]:
                if line[2] == line[0]:
                    if line[0] == 1 or line[0] == 2:
                        return 'winner'
            for space in line:
                if space != 0:
                    spaces_filled.append('x')
        if len(spaces_filled) == 9:
            v_lines_filled = True

        for line in diags:
            if line[1] == line[0]:
                if line[2] == line[0]:
                    if line[0] == 1 or line[0] == 2:
                        return 'winner'
            for space in line:
                if space != 0:
                    spaces_filled.append('x')
        if len(spaces_filled) == 9:
            d_lines_filled = True

        if h_lines_filled and v_lines_filled and d_lines_filled:
            return 'draw'

    def spaces_used(self, game_board):
        row_num = 0
        spaces_used = []
        for row in game_board:
            col_num = 0
            for item in row:
                if item == 1 or item == 2:
                    spaces_used.append((row_num, col_num))
                col_num += 1
            row_num += 1
        return spaces_used

    # def computer_ai(self, game_board):
    #     print('checking for potential moves')
    #     def iterate_lines(lines, line_type):
    #         potential_move = ''
    #         moves_to_send = []
    #         player_moves = []
    #         line_n = 0
    #         print(self.row_index)
    #         print(self.col_index)
    #         print(self.diag_index)
    #         for line in lines:
    #             potential_moves = []
    #             print(f'{line_type}: {line}')
    #             space_n = 0
    #             for space in line:
    #                 if space == 2:
    #                     player_moves.append('x')
    #                 if space == 0:
    #                     if line_type == 'rows':
    #                         potential_move = self.row_index[line_n][space_n]
    #                     elif line_type == 'cols':
    #                         potential_move = self.col_index[line_n][space_n]
    #                     else:
    #                         potential_move = self.diag_index[line_n][space_n]
    #                     print(f'{line_type}_index = {space_n}')
    #                     print('potential move:')
    #                     print(potential_move)
    #                 space_n += 1
    #                 potential_moves.append(potential_move)
    #             if len(player_moves) > 1:
    #                 moves_to_send.append(potential_moves)
    #             line_n += 1
    #         return moves_to_send
    #
    #     rows = [game_board[item, :] for item in range(0, 3)]
    #     cols = [game_board[:, item] for item in range(0, 3)]
    #     diag_tl_to_br = [game_board[0, 0].item(), game_board[1, 1].item(), game_board[2, 2].item()]
    #     diag_bl_to_tr = [game_board[2, 0].item(), game_board[1, 1].item(), game_board[0, 2].item()]
    #     diags = [diag_tl_to_br, diag_bl_to_tr]
    #     playable_moves = []
    #
    #     potential_rows = iterate_lines(rows, 'rows')
    #     potential_cols = iterate_lines(cols, 'cols')
    #     potential_diags = iterate_lines(diags, 'diags')
    #
    #     for item in potential_rows:
    #         playable_moves.append(item)
    #     for item in potential_cols:
    #         playable_moves.append(item)
    #     for item in potential_diags:
    #         playable_moves.append(item)
    #
    #     print('playable moves:')
    #     print(playable_moves)
    #     return playable_moves
