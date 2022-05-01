# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
while True:
    number = input('Input natural number:\n')
    if not number.isdigit():
        print('Only digits are excepted!')
        continue

    even_count = odd_count = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f'Number {number} has {even_count} even and {odd_count} odd digits!')
    break
