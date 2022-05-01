# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import randint, seed
MAX_LENGHT = 15

# seed(17)
numbers_list = [randint(-10, 70) for i in range(1, MAX_LENGHT)]

print(numbers_list)
# Первая попытка. Некорректно понял условие задачи
# del(numbers_list[numbers_list.index(max(numbers_list))], numbers_list[numbers_list.index(min(numbers_list))])
# print(sum(numbers_list))

# Вторая, корректная
min_value = numbers_list.index(min(numbers_list))
max_value = numbers_list.index(max(numbers_list))
sign = 1 if min_value < max_value else -1

slice_list = numbers_list[min_value + sign:max_value:sign]
print(f'Min value: {numbers_list[min_value]}')
print(f'Max value: {numbers_list[max_value]}')
print(f'Sum of {slice_list} items is {sum(slice_list)}')
