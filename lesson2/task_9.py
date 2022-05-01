# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
def sum_of_digit(number_str):
    return sum((int(i) for i in number_str))


string_of_numbers = input('Input several natural numbers separated by space:\n')
numbers = string_of_numbers.split(' ')
digits_sum = 0
result = {'sum': 0, 'number': 0}
for number in numbers:
    if not number.isdigit():
        continue

    digits_sum = sum_of_digit(number)
    if digits_sum > result['sum']:
        result['sum'] = digits_sum
        result['number'] = number

print(f'Max digits sum={result["sum"]} of number {result["number"]}')
