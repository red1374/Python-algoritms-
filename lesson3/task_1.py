# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# каждому из чисел в диапазоне от 2 до 9.

MIN_VALUE = 2
MAX_VALUE = 99
numbers_list = range(MIN_VALUE, MAX_VALUE + 1)


def count_div(number):
    count = 0
    for i in numbers_list:
        if i % number == 0:
            count += 1

    return count


for i in range(2, 10):
    print(f'{count_div(i)} numbers divided by {i}')
