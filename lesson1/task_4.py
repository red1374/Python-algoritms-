# Написать программу, которая генерирует в указанных пользователем границах:
# - случайное целое число;
# - случайное вещественное число;
# - случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить
# случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ
# алфавита от 'a' до 'f' включительно.

from random import choice, randint


def frange(end, start=0.0, step=0.1):
    i = start
    while i < end:
        yield round(i, 1)
        i += step


random_type = input('Select character type: 1 - int, 2 - float, 3 - char\n')
print('Input range border values:')
range_from, range_to = input('input from:\n'), input('input to:\n')

if random_type == '1':
    print(randint(int(range_from), int(range_to) + 1))
elif random_type == '2':
    print(choice(tuple(frange(float(range_to) + 0.1, float(range_from)))))
elif random_type == '3':
    print(chr(randint(ord(range_from), ord(range_to) + 1)))
else:
    print('Wrong choice!')
