"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
 (зима, весна, лето, осень). Напишите решения через list и через dict.
"""
# через list
month = int(input())
list_of_months = ['зиме', 'весне', 'лету', 'осени']

if month == 1 or month == 2 or month == 12:
    print(f'Данный месяц относится к {list_of_months[0]}')
elif month == 3 or month == 4 or month == 5:
    print(f'Данный месяц относится к {list_of_months[1]}')
elif month == 6 or month == 7 or month == 8:
    print(f'Данный месяц относится к {list_of_months[2]}')
else:
    print(f'Данный месяц относится к {list_of_months[3]}')

# через dict
month_2 = int(input())
dict_of_months = {'зиме': [1, 2, 12],
                  'весне': [3, 4, 5],
                  'лету': [6, 7, 8],
                  'осени': [9, 10, 11]}
for key, value in dict_of_months.items():
    if month_2 in value:
        print(f'Данный месяц относится к {key}')

