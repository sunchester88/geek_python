"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:

    def __init__(self, date):
        self.date = date

    @classmethod
    def to_int(cls, date):
        return [int(i) for i in date.split('-')]

    @staticmethod
    def is_work(date):
        day, month, year = [int(i) for i in date.split('-')]
        if 0 > day > 31:
            return False
        if 1 > month > 12:
            return False
        if (day > 30) and (month in [4, 6, 9, 11]):
            return False
        if (day > 28) and (month == 2) and not (year % 4 == 0):
            return False
        else:
            if (day > 29) and (month == 2):
                return False
        return True


print(Data.to_int("25-4-2005"))
print(Data.is_work("13-4-2010"))
