from abc import *



class Entity(metaclass=ABCMeta):
    # Корневой абстрактный класс для всех существ и объектов
    # навигация по классу мап
    defaultHP = 1

    def __init__(self, name, coordinate , HP=defaultHP):
        self.name = name
        self.coordinate = coordinate
        self.HP = HP


class Rock(Entity):
    # статичные объекты - нельзя взаимодействовать
    emj = '\U0001F5FB'


class Tree(Entity):
    # статичные объекты - нельзя взаимодействовать
    emj = '\U0001F333'


class Grass(Entity):
    emj = '\U0001F331'
    # ресурс для травоядных


class Creature(Entity, metaclass=ABCMeta):
    defaultSpeed = 3    # скорость (сколько клеток может пройти за 1 ход)
    defaultHP = 3    # hitpoints - "количество жизней"

    def __init__(self, name, coordinate,HP=defaultHP):
        super().__init__(name, coordinate, HP)

    # Имеет абстрактный метод makeMove() - сделать ход.
    # Наследники будут реализовывать этот метод каждый по-своему.
    @abstractmethod
    def makeMove(self):
        pass
    # def makeMove(self, coordinate, destination):
    #     newCoordinate = self.findWay(coordinate, destination)
    #     return newCoordinate

    def findWay(self, coordinate, speed):
        # if isEat:
        #     someHerbivore.HP -= self.attack
        # if someHerbivore.HP < 1:
        #     del someHerbivore
        pass
        # return newCoordinate, isEat
        # realize: find destination or make closer to it


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


