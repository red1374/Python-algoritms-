# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
number = input('Input 3-digit number:\n')
if not number.isdigit():
    exit(0)

digits_sum = 0
digit_mult = 1
for digit in (int(i) for i in number):
    digits_sum += digit
    digit_mult *= digit

print(f'Digits Sum={digits_sum}, Multiplication={digit_mult}')
