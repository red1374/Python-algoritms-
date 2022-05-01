# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
from random import randint
MAX_ROWS = 4
MAX_COLS = 4
matrix = []

calc_type = '-1'
while True:
    if calc_type == '0' or matrix:
        break

    calc_type = input(f'To fill in matrix {MAX_ROWS}x{MAX_COLS} manually type "1",\
            \n "2" - to generate it automatically,\n "0" - for exit\n')

    if calc_type == '2':
        # -- Generate matrix automatically -----------------
        for i in range(0, MAX_ROWS):
            matrix.append([])
            for j in range(0, MAX_COLS):
                matrix[i].append(randint(-1, 5))
                if j == (MAX_COLS - 1):
                    matrix[i].append(sum(matrix[i]))
    elif calc_type == '1':
        # -- Fill in matrix automatically -----------------
        for i in range(0, MAX_ROWS):
            matrix_row = input(f'Input row {i + 1} of {MAX_ROWS} with {MAX_COLS} items throw a space:\n')
            matrix.append([int(j) for j in matrix_row.split()])
            matrix[i].append(sum(matrix[i]))
    else:
        print('Wrong option!')

# Print out generated matrix with sum column
for row in matrix:
    print('\t'.join(str(item) for item in row))
