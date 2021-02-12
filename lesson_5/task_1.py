"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


with open('task_1.txt', 'wt', encoding='UTF-8') as f:
    while True:
        some_string = input('Введите строку ')
        if not some_string:
            break
        f.write(some_string + '\n')
