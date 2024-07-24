import numpy as np


def print_board(setup):
    blank = '_'
    x = 'x'
    o = 'o'
    row_index = 0
    row_1 = []
    row_2 = []
    row_3 = []
    rows = [row_1, row_2, row_3]
    print(rows)
    print(setup)
    for row in range(3):
        index = 0
        print(row_index)
        for char in range(3):
            print(index)
            if setup[row_index, index] == 0:
                rows[row_index].append(f'{blank}')
                index += 1
            elif setup[row_index, index] == 1:
                rows[row_index].append(f'{x}')
                index += 1
            else:
                rows[row_index].append(f'{o}')
                index += 1
        print(f'Row {row_index}{rows[row_index]} finished.')
        row_index += 1
    for row in rows:
        index = 0
        for char in row:
            if row.index(char) == 0 or row.index(char) == 1:
                char_index = row.index(char)
                row[char_index] = f'{char} |'
    for row in rows:
        print(row[0], row[1], row[2])


ttt_setup = np.array([[1, 2, 1], [2, 2, 2], [2, 1, 2]])

print(ttt_setup.ndim)

print_board(ttt_setup)



