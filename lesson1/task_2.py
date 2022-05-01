# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

digit_a = 5
digit_b = 6
print(f'Login AND:\t\t{bin(digit_a)} & {bin(digit_b)} = {digit_a & digit_b}')
print(f'Login OR:\t\t{bin(digit_a)} | {bin(digit_b)} = {digit_a | digit_b}')
print(f'Login EXCEPT:\t{bin(digit_a)} ^ {bin(digit_b)} = {digit_a ^ digit_b}')

print(f'Bitwise right shift:{bin(digit_a)} >> 2 = {digit_a >> 2}')
print(f'Bitwise left shift:\t{bin(digit_a)} << 2 = {digit_a << 2}')
