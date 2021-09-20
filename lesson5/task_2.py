# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как коллекция, элементы которой это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма
# чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]


def to_decimal(number_list: list):
    """
    Convert hexadecimal digit into decimal
    :param number_list: digits list of hexadecimal number
    :return: decimal number
    """
    if len(number_list) <= 0:
        return None

    result = 0
    for index, digit in enumerate(reversed(number_list)):
        result += alphabet.index(str(digit).lower()) * 16 ** index

    return result


def to_hexadecimal(number: int):
    """
    
    :param number:
    :return:
    """
    if number < 0:
        return None

    result = []
    whole_part = number
    while whole_part > 16:
        number = whole_part
        whole_part //= 16
        result.append(number - whole_part * 16)
    else:
        result.append(whole_part)

    return [alphabet[digit].upper() for digit in reversed(result)]


alphabet = [str(i) for i in range(10)] + [chr(i) for i in range(ord('a'), ord('f') + 1)]

print(to_hexadecimal(to_decimal('4')))
