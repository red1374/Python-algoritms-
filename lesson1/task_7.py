# По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков. Если такой треугольник существует,
# то определить, является ли он разносторонним, равнобедренным или равносторонним.

a, b, c = input('Input A side length:\n'), input('Input B side length:\n'), input('Input C side length:\n')
if not a.isdigit() or not b.isdigit() or not c.isdigit():
    print("Error! Only digits are expected!")
    exit(0)

a, b, c = int(a), int(b), int(c)
if a + b > c and a + c > b and c + b > a:
    if a == b == c:
        print('You\'ve got equilateral triangle!')
    elif a == b or b == c or a == c:
        print('You\'ve got isosceles triangle!')
    else:
        print('You\'ve got versatile triangle!')
else:
    print('Triangle with given sides don\'t exists')
