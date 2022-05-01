# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
def get_series(series_size):
    """
    Series generator
    :param series_size: size of series
    :return: series og given length
    """
    series_size = int(series_size)
    if series_size < 0 or series_size is None:
        return series_size

    sign = 1
    for i in range(series_size):
        if i % 2:
            sign = -1
        else:
            sign = 1
        yield sign * 1 / (2 ** i)


while True:
    n = int(input('Input length of series or "0" for exit:\n'))
    if n == 0:
        break
    if n < 0 or n is None:
        print('Wrong input value')
        continue

    # Generate series from n items and get sum of it elements
    print(f'Series items sum is: {sum(get_series(n))}')
