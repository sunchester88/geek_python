"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""


class ComplexNumbers:
    real = float(0)
    imaginary = float(0)

    def __init__(self, real_part, imaginary_part):
        self.real = float(real_part)
        self.imaginary = float(imaginary_part)

    def __str__(self):
        return f'{self.real} + ({self.imaginary})*i'

    def __add__(self, other):
        return ComplexNumbers(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumbers((self.real * other.real) - (self.imaginary * other.imaginary),
                              (self.real * other.imaginary) + (self.imaginary * other.real))


ComplexNumberA = ComplexNumbers(3, 4)
ComplexNumberB = ComplexNumbers(5, 6)

print(ComplexNumberA + ComplexNumberB)
print(ComplexNumberA * ComplexNumberB)
