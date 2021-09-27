# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import randint, random


def merge(left_list, right_list):
    """
    Sorting and Merge two unsorted sub lists into one sorted list
    :param left_list: left unsorted list
    :param right_list: right unsorted list
    :return: sorted list
    """
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Add Left list item to sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                # Add Right list item to sorted list
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Add rest of the Right list items to sorted list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Add rest of the Left list items to sorted list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(unsorted_list):
    """
    Function of sorting a list with merge sorting algorithm
    :param unsorted_list: unsorted list
    :return: sorted list
    """
    # End of recursion
    if len(unsorted_list) <= 1:
        return unsorted_list

    # Get middle of the list
    mid = len(unsorted_list) // 2

    # Sorting sub lists
    left_list = merge_sort(unsorted_list[:mid])
    right_list = merge_sort(unsorted_list[mid:])

    # Merge sorted lists
    return merge(left_list, right_list)


# rand_list = [randint(0, 50) for _ in range(15)]
rand_list = [round(random() * 100, 2) for _ in range(15)]
print(rand_list)
print(merge_sort(rand_list))
