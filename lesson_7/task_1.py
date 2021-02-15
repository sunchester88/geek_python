"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
 (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
 с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    content = []
    width = 0
    height = 0

    def __init__(self, input_content):
        self.content = []
        self.width = 0
        self.height = 0
        for sub_content in input_content:
            self.content.append([])
            self.height += 1
            row = self.content[self.height - 1]
            for value in sub_content:
                row.append(float(value))

    def __str__(self):
        rows = []
        for row in self.content:
            str_row = row[::]
            for ind, value in enumerate(str_row):
                str_row[ind] = str(value)
            rows.append(', '.join(str_row))
        return str(rows)

    def __add__(self, other):
        new_content = self.content[::]
        for i, row in enumerate(new_content):
            for j, value in enumerate(row):
                new_content[i][j] += float(other.content[i][j])
        return Matrix(new_content)


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[3, 4, 5], [6, 7, 8], [9, 10, 11]])

print(m_1)
print(m_1 + m_2)
