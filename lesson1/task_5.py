# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и
# сколько между ними находится букв.

first_letter, second_letter = input('Input first letter:\n'), input('Input second letter:\n')

alphabet = range(ord('a'), ord('z') + 1)
pos1, pos2 = alphabet.index(ord(first_letter)), alphabet.index(ord(second_letter))
letter_length = abs(pos2 - pos1)
letter_length -= 1 if letter_length >= 1 else 0
print(f'"{first_letter}" letter position is {pos1 + 1}')
print(f'"{second_letter}" letter position is {pos2 + 1}')
print(f'{letter_length} letter(s) between "{first_letter}" and "{second_letter}"')
