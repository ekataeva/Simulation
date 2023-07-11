from abc import *


class Entity(metaclass=ABCMeta):
    """ Корневой абстрактный класс для всех существ и объектов
     навигация по классу мап"""

    def __init__(self, coordinate, name="ent", emj=None):
        self.name = name
        self.coordinate = coordinate
        self.emj = emj

    def __str__(self):
        return f"{self.emj:3}"


class Rock(Entity):
    # статичные объекты - нельзя взаимодействовать
    def __init__(self, coordinate, name="Rock"):
        emj = '\U0001F5FB'
        super().__init__(coordinate, name, emj)


class Tree(Entity):
    # статичные объекты - нельзя взаимодействовать
    def __init__(self, name="Tree", coordinate=(0, 0)):
        emj = '\U0001F334'
        super().__init__(coordinate, name, emj)


class Grass(Entity):
    # ресурс для травоядных
    def __init__(self, coordinate, name="Grass"):
        emj = '\U0001F96C'
        super().__init__(coordinate, name, emj)


class Creature(Entity, metaclass=ABCMeta):
    @abstractmethod
    def make_move(self, path):
        pass


class Herbivore(Creature):
    def __init__(self, coordinate, name="Herbivore"):
        emj = '\U0001F993'  # zebra
        super().__init__(coordinate, name, emj)

    speed = 2  # скорость (сколько клеток может пройти за 1 ход)
    HP = 4  # hit-points - "количество жизней"

    def make_move(self, path):
        # может потратить свой ход на движение в сторону травы, либо на её поглощение
        # если длина пути больше 2 (начало и конец) - движение в сторону травы
        if len(path) > 2:
            if self.speed + 1 > len(path) - 1:
                self.coordinate = path[-1]
            else:
                self.coordinate = path[self.speed + 1]
            return None
        # иначе - поедание травы
        else:
            self.coordinate = path[-1]
            return "herbivore attacked"


class Predator(Creature):
    def __init__(self, coordinate, name="Predator"):
        emj = '\U0001F981'  # lion
        super().__init__(coordinate, name, emj)

    attack = 2  # сила атаки
    speed = 4  # скорость (сколько клеток может пройти за 1 ход)
    HP = 2  # hit-points - "количество жизней"

    def make_move(self, path):
        # если длина пути больше 2 (начало и конец) - Переместиться (чтобы приблизиться к жертве - травоядному)
        if len(path) > 2:
            if self.speed + 1 > len(path) - 1:
                self.coordinate = path[-1]
            else:
                self.coordinate = path[self.speed + 1]
            # + изменение координаты в карте симуляции -> в методе при возвращении None
            return None
        # Иначе - Атаковать травоядное
        else:
            return "predator attacked"
