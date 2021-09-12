# Найти максимальный элемент среди минимальных элементов столбцов матрицы
from random import randint

MAX_ROWS = 4
MAX_COLS = 4
matrix = []

for i in range(0, MAX_ROWS):
    matrix.append([])
    for j in range(0, MAX_COLS):
        matrix[i].append(randint(-1, 5))

# Print out generated matrix with sum column
for row in matrix:
    print('\t'.join(str(item) for item in row))

print(f'Maximum value of minimal item in each column is {max(min(row[j] for row in matrix) for j in range(0, MAX_COLS))}')

# To explain for myself -----------------------
# for j in range(0, MAX_COLS):
#     print(min(row[j] for row in matrix))  -->

# min_vals = [min(row[j] for row in matrix) for j in range(0, MAX_COLS)] -->
# print(max(min_vals))