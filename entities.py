from abc import *


class Entity(metaclass=ABCMeta):
    """ Корневой абстрактный класс для всех существ и объектов
     навигация по классу мап"""

    def __init__(self, coordinate, name="ent", emj=None):
        self.name = name
        self.coordinate = coordinate
        self.emj = emj
        self.is_live = True

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
    speed = 3  # скорость (сколько клеток может пройти за 1 ход)

    def make_move(self, path):
        # если длина пути меньше скорости - поедание травы
        if len(path) <= self.speed:
            self.coordinate = path[-1]
            return "attack"
        # иначе - движение в сторону травы
        else:
            self.coordinate = path[self.speed]
            return None


class Herbivore(Creature):
    def __init__(self, coordinate, name="Herbivore"):
        self.HP = 4  # hit-points - "количество жизней"
        emj = '\U0001F993'  # zebra
        super().__init__(coordinate, name, emj)

    # def make_move(self, path):  # может потратить свой ход на движение в сторону травы, либо на её поглощение
    #     # если длина пути меньше скорости - поедание травы
    #     if len(path) <= self.speed + 1:
    #         self.coordinate = path[-1]
    #         return "attack"
    #     # иначе - движение в сторону травы
    #     else:
    #         self.coordinate = path[self.speed + 1]
    #         return None


class Predator(Creature):
    def __init__(self, coordinate, name="Predator"):
        emj = '\U0001F981'  # lion
        super().__init__(coordinate, name, emj)
        self.attack = 2  # сила атаки
        self.speed = 3  # скорость (сколько клеток может пройти за 1 ход)
        self.HP = 2  # hit-points - "количество жизней"

    # def make_move(self, path):
    #     # если длина пути больше 2 (начало и конец) - Переместиться (чтобы приблизиться к жертве - травоядному)
    #     if len(path) > 2:
    #         super().make_move(path)
    #         # + изменение координаты в карте симуляции -> в методе при возвращении None
    #     # Иначе - Атаковать травоядное
    #     else:
    #         self.coordinate = path[-1]
    #         return "predator attacked"
