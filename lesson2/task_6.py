# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

from random import choice

MIN_VALUE = 0
MAX_VALUE = 100
TRY_COUNT = 10
number = choice(range(MIN_VALUE, MAX_VALUE))

print(f'Try to guess a number from "{MIN_VALUE}" to "{MAX_VALUE}" for {TRY_COUNT} tries')
i = 0
while i < TRY_COUNT:
    user_number = input(f'Input your variant\n')
    if not user_number.isdigit():
        print('Only digits are accepted!')
        continue
    user_number = int(user_number)
    if user_number == number:
        print('Congratulations! YOU WIN!')
        break
    elif user_number > number:
        print('Your number is grater then mine!')
    else:
        print('Your number is less then mine!')
    i += 1
else:
    print(f'You lose. The number is "{number}"')
