# Во втором массиве сохранить индексы четных элементов первого массива. Например,
# если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить
# значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к.
# именно в этих позициях первого массива стоят четные числа.

from random import randint
MAX_LENGHT = 15

numbers_list = [randint(0, 100) for i in range(1, MAX_LENGHT)]
result_list = []

print(numbers_list)
for idx, v in enumerate(numbers_list):
    if v % 2 == 0:
        result_list.append(idx)
print(result_list)
