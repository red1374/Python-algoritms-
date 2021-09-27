# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не
# меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод
# сортировки, который не рассматривался на уроках.

M = 7
from random import randint, choice
from task_2 import merge_sort


def quickselect_median(r_list):
    """
    Get median value of given list
    :param r_list: unsorted list with random values
    :return: median value
    """
    if len(r_list) % 2 == 1:
        return quickselect(r_list, len(r_list) / 2)
    else:
        return 0.5 * (quickselect(r_list, len(r_list) / 2 - 1) +
                      quickselect(r_list, len(r_list) / 2))


def quickselect(r_list, k):
    """
    Select list item at 'k' position
    :param r_list: unsorted list with random values
    :param k: search index
    :return: k item from a r_list
    """
    if len(r_list) == 1:
        return r_list[0]

    pivot = choice(r_list)

    lows = [el for el in r_list if el < pivot]
    highs = [el for el in r_list if el > pivot]
    pivots = [el for el in r_list if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))


rand_list = [randint(-50, 50) for i in range(2 * M + 1)]
print(f'List of random values:\n\t{rand_list}')
print(f'Median found with Quick select algorithm is: {quickselect_median(rand_list)}')

sorted_list = merge_sort(rand_list)
print(f'\nSorted with merge\n\t{sorted_list}')
print(f'Median is: {sorted_list[len(rand_list) // 2]}')
