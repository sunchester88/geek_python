"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

my_string = input().split()
for i in range(len(my_string)):
    if len(my_string[i]) > 10:
        my_string[i] = my_string[i][:10]
for el in enumerate(my_string):
    print(el)


