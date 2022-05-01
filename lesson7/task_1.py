# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint


def bubble_sorting(array):
    """
    Sorting function with bubble algorithm
    :param array: input list
    :return: sorted list
    """
    n = 1
    is_sorted = True
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                is_sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
        if is_sorted:
            print('Already sorted!')
            return array
        n += 1

    return array


rand_list = [randint(-100, 100) for _ in range(15)]
# rand_list = [i for i in range(-10, 10)]

print(rand_list)
print(bubble_sorting(rand_list))
