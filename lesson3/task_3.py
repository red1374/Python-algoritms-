# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint
MAX_LENGHT = 15

numbers_list = [randint(0, 100) for i in range(1, MAX_LENGHT)]
result_list = []

print(numbers_list)
max_index, min_index = numbers_list.index(max(numbers_list)), numbers_list.index(min(numbers_list))
print(f'Max value {numbers_list[max_index]} ({max_index})')
print(f'Min value {numbers_list[min_index]} ({min_index})')
numbers_list[max_index], numbers_list[min_index] = numbers_list[min_index], numbers_list[max_index]
print(numbers_list)
