# Написать два алгоритма нахождения i-го по счёту простого числа.
#  - Без использования Решета Эратосфена;
#  - Использовать алгоритм решето Эратосфена

from math import log
import cProfile


def get_set_len(number):
    n = 100
    while number > n / log(n):
        n += 1000

    return n


def is_prime_number(number, primes_list):
    for i in primes_list:
        if number % i == 0:
            return False

    return True


def get_prime_digit(k):
    """
    Get prime natural number at position with number k
    :param k: - position of prime number
    :return: prime number at k position
    """
    natural_set = range(2, get_set_len(k) + 1)
    primes = list()
    for i in natural_set:
        if len(primes) > 0 and not is_prime_number(i, primes):
            continue

        for j in range(i + 1, len(natural_set) + 3):
            if j % i == 0:
                if len(primes) > 0 and not is_prime_number(j, primes):
                    continue
                else:
                    break

        primes.append(i)
        if len(primes) == k:
            break

    return primes[k - 1]


def get_prime_digit_with_sieve(k):
    """
    Get prime natural number at position with number k with Eratosthenes sieve
    :param k: - position of prime number
    :return: prime number at k position
    """
    n = get_set_len(k)
    natural_set = list(range(2, n + 1))

    series = list()
    for i in natural_set:
        if i == 0:
            continue

        # for j in natural_set[i - 1::]:
        #     if i == 0:
        #         continue
        #
        #     if j % i == 0:
        #         natural_set[j - 2] = 0
        # series.append(i)
        # if len(series) == k:
        #     return series[k-1]

        for j in range(2 * i, n + 1, i):
            natural_set[j - 2] = 0

    natural_set = [i for i in natural_set if i != 0]

    return natural_set[k - 1]


def main():
    print(get_prime_digit(10000))
    print(get_prime_digit_with_sieve(10000))


cProfile.run('main()')

#  k - 1000
# 7919
# 7919
# 31223 function calls in 0.376 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.376    0.376 <string>:1(<module>)
#     14094    0.025    0.000    0.025    0.000 task_2.py:17(is_simple_number)
#         1    0.348    0.348    0.374    0.374 task_2.py:25(get_simple_digit)
#         1    0.002    0.002    0.002    0.002 task_2.py:46(get_simple_digit_with_sieve)
#         1    0.000    0.000    0.000    0.000 task_2.py:72(<listcomp>)
#         1    0.000    0.000    0.376    0.376 task_2.py:77(main)
#         2    0.000    0.000    0.000    0.000 task_2.py:9(get_set_len)
#         1    0.000    0.000    0.376    0.376 {built-in method builtins.exec}
#     16096    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        22    0.000    0.000    0.000    0.000 {built-in method math.log}
#      1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#  k - 10000
#          389474 function calls in 40.673 seconds
# 104729
# 104729
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   40.673   40.673 <string>:1(<module>)
#    179613    2.369    0.000    2.369    0.000 task_2.py:17(is_simple_number)
#         1   38.260   38.260   40.643   40.643 task_2.py:25(get_simple_digit)
#         1    0.028    0.028    0.028    0.028 task_2.py:46(get_simple_digit_with_sieve)
#         1    0.001    0.001   40.673   40.673 task_2.py:71(main)
#         2    0.000    0.000    0.000    0.000 task_2.py:9(get_set_len)
#         1    0.000    0.000   40.673   40.673 {built-in method builtins.exec}
#    199615    0.013    0.000    0.013    0.000 {built-in method builtins.len}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#       236    0.000    0.000    0.000    0.000 {built-in method math.log}
#     10000    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
