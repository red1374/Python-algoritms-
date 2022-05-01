# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
from random import randint
MAX_LENGHT = 15

numbers_list = [randint(-20, 50) for i in range(1, MAX_LENGHT)]
print(numbers_list)
maximin = max(i for i in numbers_list if i < 0)
print(f'The max of negative items is {maximin} on position {numbers_list.index(maximin)}')
