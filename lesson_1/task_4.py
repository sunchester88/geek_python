"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

my_number = int(input())
maxi = 0
while my_number > 0:
    last_digit = my_number % 10
    if last_digit >= maxi:
        maxi = last_digit
    my_number //= 10
print(maxi)
