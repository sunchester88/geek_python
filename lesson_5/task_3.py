"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('task_3.txt', 'rt', encoding='UTF-8') as file:
    content = file.readlines()
    count_of_employees = len(content)
    salary_sum = 0
    for record in content:
        employee, salary = record.split()
        salary = int(salary)
        salary_sum += salary
        if salary < 20000:
            print(f'Работник {employee} зарабатывает менее чем 20000')
    print(f'Средняя зарплата {int(salary_sum/count_of_employees)}')
