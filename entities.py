from abc import *


class Entity(metaclass=ABCMeta):
    """ Корневой абстрактный класс для всех существ и объектов
     навигация по классу мап"""

    def __init__(self, name="ent", coordinate=(0, 0), HP=1):
        self.name = name
        self.coordinate = coordinate
        self.HP = HP

    emj = " "

    def __str__(self):
        return f"{self.emj:3}"


class Rock(Entity):
    # статичные объекты - нельзя взаимодействовать
    emj = '\U0001F5FB'


class Tree(Entity):
    # статичные объекты - нельзя взаимодействовать
    emj = '\U0001F334'


class Grass(Entity):
    emj = '\U0001F96C'
    # ресурс для травоядных


class Creature(Entity, metaclass=ABCMeta):
    defaultSpeed = 3  # скорость (сколько клеток может пройти за 1 ход)
    defaultHP = 3  # hitpoints - "количество жизней"

    # Имеет абстрактный метод makeMove() - сделать ход.
    # Наследники будут реализовывать этот метод каждый по-своему.
    @abstractmethod
    def makeMove(self):
        pass
    # def makeMove(self, coordinate, destination):
    #     newCoordinate = self.findWay(coordinate, destination)
    #     return newCoordinate


class Herbivore(Creature):
    emj = '\U0001F993'  # zebra
    speed = 4

    # может потратить свой ход на движение в сторону травы, либо на её поглощение.

    def makeMove(self):
        # newCoordinate, isEat = self.findWay(self.coordinate, self.speed)
        # if isEat:
        #     self.coordinate = newCoordinate
        pass


class Predator(Creature):
    emj = '\U0001F981'  # lion
    attack = 3
    speed = 4

    def makeMove(self):
        # newCoordinate, isEat = self.findWay(self.coordinate, self.speed)
        # if isEat:
        #     self.coordinate = newCoordinate
        pass

# print(Rock())
# print(Tree())
# print(Grass())
# print(Herbivore())
# print(Predator())
