# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как коллекция, элементы которой это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма
# чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]
class WrongInputDataError(Exception):
    def __init__(self, date_value):
        self.txt = f'Wrong input data! {date_value} - has not hexadecimal characters'


class HexNumber:
    __alphabet = [str(i) for i in range(10)] + [chr(i) for i in range(ord('a'), ord('f') + 1)]

    def __init__(self, str_value: str):
        self.is_hexadeciaml_value(str_value)

        self.value = list(str_value)

    def __add__(self, other: str):
        return HexNumber(self.to_hexadecimal(self.to_decimal(self.value) + self.to_decimal(other.value)))

    def __str__(self):
        res = [f"{key} : {value}" for key, value in self.__dict__.items()]
        return ', '.join(res)

    def __mul__(self, other):
        return HexNumber(self.to_hexadecimal(self.to_decimal(self.value) * self.to_decimal(other.value)))

    def is_hexadeciaml_value(self, value: str):
        has_trash = len(set(i.lower() for i in value).difference(set(self.__alphabet)))
        if has_trash:
            raise WrongInputDataError(value)

    def to_decimal(self, number_list: list):
        """
        Convert hexadecimal digit into decimal
        :param number_list: digits list of hexadecimal number
        :return: decimal number
        """
        if len(number_list) <= 0:
            return None

        result = 0
        for index, digit in enumerate(reversed(number_list)):
            result += self.__alphabet.index(str(digit).lower()) * 16 ** index

        return result

    def to_hexadecimal(self, number: int):
        """
        Convert Decimal number to Hexadecimal
        :param number: decimal number
        :return: number in hexadecimal system
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

        return [self.__alphabet[digit].upper() for digit in reversed(result)]


a = HexNumber('A2')
b = HexNumber('C4F')
c = a + b
print(f'Sum:\n\t{a.value} + {b.value} = {c.value}')

d = a * b
print(f'\nMultiplication:\n\t{a.value} * {b.value} = {d.value}')
