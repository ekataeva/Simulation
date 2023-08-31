from random import randrange
import math

from entities import Grass, Herbivore, Predator
from map import Coordinate
from actions.pathfinder import PathFinder


class Actions:
    """
    Class for performing actions in the simulation world.
    """

    def __init__(self, world_map):
        """
        Initialize the Actions object.

        Args:
            rows (int): Number of rows in the map.
            cols (int): Number of columns in the map.
            world_map (Map): The map of the simulation world.
        """

        self.map = world_map
        self.path_finder = PathFinder(world_map)

    def init_actions(self, init_population_distribution):
        """
        Initialize actions before the simulation starts: generate initial entities.

        Args:
            init_population_distribution (dict): Initial population distribution as a dictionary,
            where key is entities' class and value is its distribution.

        Returns:
            dict: Initial population of each entity type as a dictionary,
            where key is entities' class and value is its initial quantity.
        """
        init_population = {'Predator': 0, 'Herbivore': 0, 'Grass': 0, 'Tree': 0, 'Rock': 0}
        for ent_cls, value in init_population_distribution.items():
            ent_quantity = math.ceil(self.map.rows * self.map.cols * value / 100)
            self.make_entities(ent_cls, ent_quantity)
            init_population[ent_cls.__name__] = ent_quantity
        return init_population

    def make_entities(self, ent_cls, ent_quantity):
        """
        Place objects and entities on the map.

        Args:
            ent_cls (class): Class of the entity.
            ent_quantity (int): Quantity of entities to create.
        """
        coordinate = None
        for i in range(ent_quantity):
            while coordinate is None or not self.map.is_empty(coordinate):
                row = randrange(0, self.map.rows, 1)
                col = randrange(0, self.map.cols, 1)
                coordinate = Coordinate(row, col)
            entity = ent_cls(coordinate, f'{ent_cls.__name__} {i}', )
            self.map.place_entity(coordinate, entity)

    def turn_actions(self, creature, list_of_herbivores):
        """
        Actions performed on each turn.

        Args:
            creature (Creature): The creature taking the turn.
            list_of_herbivores (list): List of all herbivores.

        Returns:
            int: Number of turns with no valid path.
        """
        self.__check_gras(list_of_herbivores)
        none_path_counter = 0
        path = self.path_finder.find_path(creature)

        if path is None:
            creature.HP -= 1
            print(f'Для {creature} с координатами {creature.coordinate} нет достижимого ресурса')
            if isinstance(creature, Predator):
                none_path_counter += 1
        else:
            path_str = ', '.join(f"({cell.row}, {cell.col})" for cell in path)
            print(f"Path: {path_str}")
            creature.make_move(self.map, path)
            print(f"{creature} сходил на {creature.coordinate}")
        if creature.HP <= 0:
            self.map.del_entity(creature.coordinate)
        return none_path_counter

    def __check_gras(self, list_of_herbivores):
        """
        Add grass if its number is too low.

        Args:
            list_of_herbivores (list): List of all herbivores.
        """
        if len(list_of_herbivores) > len(self.map.get_list_of_grass()):
            self.make_entities(Grass, len(list_of_herbivores))
