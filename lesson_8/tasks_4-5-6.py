"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за
приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. Подсказка:
постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по
ООП. """


class Storage:
    __contents = []
    __contents_index = {}

    def __init__(self, contents_list=None):
        if contents_list is None:
            contents_list = []
        self.__contents.extend(contents_list)

    def add_utility(self, utility):
        self.__contents.append(utility)
        if utility.name in self.__contents_index:
            self.__contents_index[utility.name] += 1
        else:
            self.__contents_index[utility.name] = 1

    @property
    def contents(self):
        return self.__contents

    def send_utility(self, input_id, destination):
        for curr_utility in self.__contents:
            if curr_utility.id == input_id:
                utility = curr_utility
                break
        else:
            print("No utility found for this ID.")
            return
        print(f"Sending {utility.name} to {destination}.")
        self.__contents.remove(utility)
        self.__contents_index[utility.name] -= 1
        if self.__contents_index[utility.name] == 0:
            del self.__contents_index[utility.name]


class Utility:
    name = "Generic Utility"
    id = ""
    price = 0
    weight = 0
    dimensions = {"length": 0, "width": 0, "height": 0}

    def __init__(self, input_id):
        self.id = input_id

    def __str__(self):
        return f'Name = {self.name}; ID = {self.id}.\n'


class Printer(Utility):
    name = "Printer"
    num_of_colours = 256


class Scanner(Utility):
    name = "Scanner"
    resolution = {"vertical": 0, "horizontal": 0}


class Copier(Scanner, Printer):
    name = "Copier"
    copy_speed = 0


MainStorage = Storage()
MainStorage.add_utility(Printer('fiturte36346346'))
MainStorage.add_utility(Scanner('dfgsdg6475467'))
MainStorage.add_utility(Copier('sdfasag24534562'))
print(*MainStorage.contents)

MainStorage.send_utility('dfgsdg6475467', 'Loading')
print(*MainStorage.contents)

