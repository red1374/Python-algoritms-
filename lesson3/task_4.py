# Определить, какое число в массиве встречается чаще всего

from random import randint
MAX_LENGHT = 15

numbers_list = [randint(1, 5) for i in range(1, MAX_LENGHT)]
max_value = {'number': 0, 'count': 0}

print(numbers_list)
for key, value in ((number, numbers_list.count(number)) for number in set(numbers_list)):
    if value > max_value['count']:
        max_value['count'] = value
        max_value['number'] = key

print(f'Number "{max_value["number"]}" occurs "{max_value["count"]}" times in the list')
