"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате
 чч:мм:сс. Используйте форматирование строк.
"""

time_in_seconds = int(input())

hh = time_in_seconds // 3600
mm = (time_in_seconds % 3600) // 60
ss = (time_in_seconds % 3600) % 60

if hh < 10:
    hh = '0' + str(hh)
if mm < 10:
    mm = '0' + str(mm)
if ss < 10:
    ss = '0' + str(ss)

print(f'{hh}:{mm}:{ss}')
