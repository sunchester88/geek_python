"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
 V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class Clothes(ABC):
    _quantity = 0

    @abstractmethod
    def cloth_amount(self):
        pass


class Coat(Clothes):

    @property
    def size(self):
        return self._quantity

    @size.setter
    def size(self, value):
        self._quantity = value

    def cloth_amount(self):
        return self._quantity/6.5 + 0.5


class Suit(Clothes):

    @property
    def height(self):
        return self._quantity

    @height.setter
    def height(self, value):
        self._quantity = value

    def cloth_amount(self):
        return self._quantity * 2 + 0.3


CoatInstance = Coat()
CoatInstance.size = 60
print(CoatInstance.cloth_amount())

SuitInstance = Suit()
SuitInstance.height = 10
print(SuitInstance.cloth_amount())
