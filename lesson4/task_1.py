# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках практического
# задания первых трех уроков

import timeit

number_str = ''.join((str(i) for i in range(1, 100)))

testcode1 = '''
def reverse_number_slice(number: str):
    return number[::-1]

reverse_number_slice('{}')
'''

testcode2 = '''
def reverse_number_int(number: str):
    number = int(number)
    result = ''
    while number > 0:
        result += str(number % 10)
        number = number // 10

    return result

reverse_number_int('{}')
'''

testcode3 = '''
def reverse_number_str(number: str):
    result = ''
    for digit in number:
        result = digit + result

    return result

reverse_number_str('{}')
'''

# print(number_str)
# print(f'Test 0: {timeit.timeit(stmt=testcode0)}')
print(f'Reverse number (slice): {timeit.timeit(stmt=testcode1.format(number_str))}')
print(f'Reverse number (number): {timeit.timeit(stmt=testcode2.format(number_str))}')
print(f'Reverse number (string): {timeit.timeit(stmt=testcode3.format(number_str))}')

# -- Results --------------------------------------------------
# Input string generated from 10 digits strlen=9
# Reverse number (slice): 0.248546221
# Reverse number (number): 2.5595905329999997
# Reverse number (string): 0.7127167710000002
#
# Input string generated from 100 digits strlen=189
# Reverse number (slice): 0.39237335
# Reverse number (number): 93.95126031000001
# Reverse number (string): 11.262344650000003
