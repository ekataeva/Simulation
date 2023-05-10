from abc import *
from random import randrange


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
    HP = 3    # hitpoints - "количество жизней"

    def __init__(self, name, coordinate,):
        super().__init__(name, coordinate, 3)

    # Имеет абстрактный метод makeMove() - сделать ход.
    # Наследники будут реализовывать этот метод каждый по-своему.
    def makeMove(self, coordinate, destination):
        newCoordinate = self.findWay(coordinate, destination)
        return newCoordinate

    def findWay(self, coordinate, destination, speed):
        pass
        # realize: find destination or make closer to it


class Herbivore(Creature):
    emj = '\U0001F993'  # zebra
    speed = 4
    # может потратить свой ход на движение в сторону травы, либо на её поглощение.

    def makeMove(self):
        newCoordinate = self.findWay(self.coordinate, someGrass, speed)
        del someGrass
        self.coordinate = newCoordinate


class Predator(Creature):
    emj = '\U0001F981'  # lion
    attack = 3
    speed = 4

    def makeMove(self):
        newCoordinate = self.findWay(self.coordinate, someHerbivore, self.speed)
        if newCoordinate == someHerbivore.coordinate:
            someHerbivore.HP -= self.attack
            self.coordinate = newCoordinate
            if someHerbivore.HP < 1:
                del someHerbivore
            else:
                # one step before or makeMove again?
                self.coordinate = anotherCoordinate

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y
    def __hash__(self):
        return hash((self.x, self.y))


class Map:
    def __init__(self):
        self.map = dict()

    def addCreature(self, creature, coordinate):
        self.map[coordinate] = creature

    def delCreature(self, coordinate):
        del self.map[coordinate]
        # + del creature from creatureList


class Simulation:
    creatureList = {'herbivore': [], 'predators': []}
    moveCounter = 0
    actions = []  # ???
    def __init__(self, row, col):
        self.map = Map()
        self.row = row
        self.col = col

    def makeCreatures(self):
        classes = [Predator, Tree, Rock, Herbivore, Grass]
        for cls in classes:
            for i in range(self.row):
                coordinate = None
                while coordinate is None or coordinate not in self.map.map:
                    x, y = randrange(0, self.row, 1), randrange(0, self.col, 1)
                    coordinate = Coordinate(x, y)
                entity = cls(i, coordinate)
                self.creatureList[cls].append(entity.name)
                self.map.addCreature(coordinate, entity)

    def makeSimulation(self):
        # makeMove for all creatures
        pass


if __name__ == '__main__':
    row = int(input("Choose map's row size: "))
    col = int(input("Choose map's column size: "))
    game = Simulation(row, col)
    game.makeCreatures()
    game.makeSimulation()

    a = 0