# Определить количество различных подстрок с использованием хеш-функции.
# Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib

string = input('Input string:\n')
substring_hashes = set()
for i in range(len(string)):
    for j in range(len(string), i, -1):
        substring_hashes.add(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
        # substring_hashes.add(string[i:j])

print(f'Total {len(substring_hashes) - 1} different substrings in a given string')
# print(*substring_hashes)
