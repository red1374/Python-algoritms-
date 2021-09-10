# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
# и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

number = input('Input a number:\n')
digit = input('Input a digit you want to count in a given number:\n')

print(f'There ara {number.count(digit)} digit {digit} in a number {number}')