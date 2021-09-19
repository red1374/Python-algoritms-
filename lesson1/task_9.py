# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a, b, c = input('Input first number:\n'), input('Input second number:\n'), input('Input third number:\n')
if not a.isdigit() or not b.isdigit() or not c.isdigit():
    print('ERROR. Wrong input values!')
    exit(0)

a, b, c = int(a), int(b), int(c)
if b < a < c or c < a < b or a == b:
    print(f'Middle value is {a}')
elif a < b < c or c < b < a or b == c:
    print(f'Middle value is {b}')
else:
    print(f'Middle value is {c}')
