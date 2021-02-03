"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления
произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

import functools

my_list = [i for i in range(100, 1001, 2)]


def multiply(curr, nex):
    return curr * nex


result = functools.reduce(multiply, my_list)
print(result)
