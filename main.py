from entities import Predator, Tree, Rock, Herbivore, Grass
from random import randrange


class Simulation:
    creatureList = {'herbivore': [], 'predator': [], 'tree': [], 'rock': [], 'grass': []}
    moveCounter = 0
    actions = []  # ???

    def __init__(self, row, col):
        self.map = Map()
        self.row = row
        self.col = col

    def makeCreatures(self):
        entityClasses = [Predator, Tree, Rock, Herbivore, Grass]
        for cls in entityClasses:
            for i in range(self.row):
                coordinate = None
                while coordinate is None or coordinate in self.map.locations:
                    x, y = randrange(0, self.row, 1), randrange(0, self.col, 1)
                    coordinate = Coordinate(x, y)
                entity = cls(f'{cls}: {i}'), coordinate)
                print(entity, coordinate)
                self.creatureList[cls.__name__.lower()].append(entity.name)
                self.map.addCreature(entity, coordinate)

    # def makeSimulation(self):
    #   # makeMove for all creatures
    #   pass


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
        self.locations = dict()

    def addCreature(self, creature, coordinate):
        self.locations[coordinate] = creature

    def delCreature(self, coordinate):
        del self.locations[coordinate]
        # + del creature from creatureList


if __name__ == '__main__':
    row = 9  # int(input("Choose map's row size: "))
    col = 9  # int(input("Choose map's column size: "))

    game = Simulation(row, col)
    game.makeCreatures()

    for x in range(row):
        for y in range(col):
            coordinate = Coordinate(x, y)
            if coordinate in game.map.locations:
                print(game.map.locations[coordinate].emj, end=" ")
        print()

    # game.makeSimulation()

    a = 0