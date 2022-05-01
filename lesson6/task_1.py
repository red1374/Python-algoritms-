# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти

from pympler import tracker
from memory_profiler import profile

tr = tracker.SummaryTracker()
number_str = ''.join((str(i) for i in range(1, 10000)))
tr.print_diff()


@profile
def reverse_number_slice(number: str):
    return number[::-1]


@profile
def reverse_number_int(number: str):
    number = int(number)
    result = ''
    while number > 0:
        result += str(number % 10)
        number = number // 10
    return result


@profile
def reverse_number_str(number: str):
    result = ''
    for digit in number:
        result = digit + result
    return result


tr1 = tracker.SummaryTracker()
reverse_number_slice(number_str)
tr1.print_diff()
reverse_number_int(number_str)
tr1.print_diff()
reverse_number_str(number_str)
tr1.print_diff()

# Generating "number_str" string
#                   types |   # objects |   total size
# ======================= | =========== | ============
#                    list |        3212 |    302.08 KB
#                     str |        3209 |    225.57 KB
#                     int |         701 |     19.17 KB
#                    dict |           3 |    592     B
#                    code |           1 |    144     B
#   function (store_info) |           1 |    136     B
#                    cell |           2 |     96     B
#                   tuple |          -3 |   -272     B
# --------------------------------------------------------------------------------------
#
# Analyze function "reverse_number_slice"
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     12     26.1 MiB     26.1 MiB           1   @profile
#     13                                         def reverse_number_slice(number: str):
#     14     26.1 MiB      0.0 MiB           1       return number[::-1]
#
#
#                   types |   # objects |   total size
# ======================= | =========== | ============
#                    list |        3215 |    303.36 KB
#                     str |        3320 |    233.64 KB
#                     int |         698 |     19.09 KB
#                    dict |           4 |     18.55 KB
#                    type |           0 |    664     B
#                    code |           1 |    144     B
#                   tuple |           2 |    144     B
#   function (store_info) |           1 |    136     B
#                    cell |           2 |     96     B
#                   float |           1 |     24     B
#             abc.ABCMeta |           0 |   -168     B
# --------------------------------------------------------------------------------------
#
# Analyze function "reverse_number_int"
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     17     26.8 MiB     26.8 MiB           1   @profile
#     18                                         def reverse_number_int(number: str):
#     19     26.8 MiB      0.0 MiB           1       number = int(number)
#     20     26.8 MiB      0.0 MiB           1       result = ''
#     21     27.0 MiB      0.0 MiB        2890       while number > 0:
#     22     27.0 MiB      0.2 MiB        2889           result += str(number % 10)
#     23     27.0 MiB      0.0 MiB        2889           number = number // 10
#     24     27.0 MiB      0.0 MiB           1       return result
#
#   types |   # objects |   total size
# ======= | =========== | ============
#    dict |           1 |    240     B
#    list |           1 |     88     B
#     str |           1 |     70     B
# --------------------------------------------------------------------------------------
#
# Analyze function "reverse_number_str"
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     27     27.9 MiB     27.9 MiB           1   @profile
#     28                                         def reverse_number_str(number: str):
#     29     27.9 MiB      0.0 MiB           1       result = ''
#     30     27.9 MiB      0.0 MiB        2890       for digit in number:
#     31     27.9 MiB      0.0 MiB        2889           result = digit + result
#     32     27.9 MiB      0.0 MiB           1       return result
#
#
#   types |   # objects |   total size
# ======= | =========== | ============
#    dict |           1 |    240     B
