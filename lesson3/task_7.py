# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
from random import randint
MAX_LENGHT = 15

numbers_list = [randint(-10, 70) for i in range(1, MAX_LENGHT)]
print(numbers_list)
numbers_list.sort()
print(f'Two minimal items in a list: {numbers_list[0]} and {numbers_list[1]}')
