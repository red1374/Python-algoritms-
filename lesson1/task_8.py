# Определить, является ли год, который ввел пользователем, високосным или не високосным.

year = input('Input year:\n')
if not year.isdigit() or len(year) != 4:
    print('Wrong input value!')
    exit(0)

year = int(year)
if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
