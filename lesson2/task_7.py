# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
def sum_func(number):
    return sum(range(1, number + 1))


def equation_func(number):
    return (number * (number + 1)) / 2


while True:
    n = input('Input natural number or "0" for exit:\n')
    if not n.isdigit() or int(n) < 0:
        print('Input positive natural number!')
        continue
    if n == '0':
        break

    sum_result = sum_func(int(n))
    equation_result = equation_func(int(n))
    print(f'Sum ({sum_result}) of {n} numbers', end=' ')
    if sum_result != equation_result:
        print('NOT', end=' ')
    print(f'equal to equation result ({equation_result})!')
