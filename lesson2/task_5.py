# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32
# и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
FROM_SYMBOL = 32
TO_SYMBOL = 127
ITEM_PER_ROW = 10

print(f'----- ASCII symbols table from {FROM_SYMBOL} to {TO_SYMBOL} item ---')
for i, value in enumerate(range(FROM_SYMBOL, TO_SYMBOL + 1)):
    end_of_line = ' '
    if (i + 1) % ITEM_PER_ROW == 0:
        end_of_line = '\n'

    print(f'{value}-{chr(value)}', end=end_of_line)
