# По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.

x1, y1 = int(input('Input x1 coordinate:\n')), int(input('Input y1 coordinate:\n'))
x2, y2 = int(input('Input x2 coordinate:\n')), int(input('Input y2 coordinate:\n'))
k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1
print(f' y = {k}x {"+" if b > 0 else "-"} {abs(b)}')
