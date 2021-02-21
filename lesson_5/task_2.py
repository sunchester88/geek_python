"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open('task_2.txt', 'rt', encoding='UTF-8') as file:
    content = file.readlines()
    print(f'Файл содержит {len(content)} строк')
    for index, line in enumerate(content, 1):
        print(f'Строка {index} содержит {len(line.split())} слов')
