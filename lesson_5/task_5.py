"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

with open('task_5.txt', 'wt', encoding='UTF-8') as f:
    i = 0
    while i < 10:
        f.write(str(random.randint(1, 50))+' ')
        i += 1

with open('task_5.txt', 'rt', encoding='UTF-8') as f:
    my_sum = 0
    content = f.read()
    for number in content.split():
        my_sum += int(number)

print(my_sum)
