# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.

signs = ('+', '-', '*', '/')
str = '-1'

while str != '0':
    str = input('Input two digits through a space:\n')
    if str == '0':
        break

    str = str.split()
    if len(str) != 2:
        print('Incorrect input values count!\n')
        continue
    if not str[0].isdigit() or not str[1].isdigit():
        print('Only digits are accepted!\n')
        continue

    sign = input(f'Input operation ({", ".join(signs)}):\n')
    while sign not in signs and str != '0':
        sign = input(f'Select operation from the list: ({", ".join(signs)}) or 0 for exit:\n')
        if sign == '0':
            exit(0)

    result = 0
    str[0] = int(str[0])
    str[1] = int(str[1])
    if sign == '+':
        result = str[0] + str[1]
    elif sign == '-':
        result = str[0] - str[1]
    elif sign == '*':
        result = str[0] * str[1]
    elif sign == '/':
        if str[1] == 0:
            print('You can`t divide by zero!\n')
            continue
        result = str[0] / str[1]
    print(f'{str[0]} {sign} {str[1]} = {result}')
