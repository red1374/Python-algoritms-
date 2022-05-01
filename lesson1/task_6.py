# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
alphabet = range(ord('a'), ord('z') + 1)
letter_position = input('Input letter number:\n')

if not letter_position.isdigit():
    print('Wrong input value!')
elif len(alphabet) > int(letter_position) - 1 > 0:
    print(f'Your letter is "{chr(alphabet[int(letter_position) - 1])}"')
else:
    print('Not in alphabet range!')
