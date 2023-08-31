from time import sleep

from actions import Actions
from entities import Tree, Rock, Grass, Herbivore, Predator
from map import Coordinate, Map


class Simulation:
    """
    A simulation of a dynamic ecosystem with predators, herbivores and resources.

    Attributes:
        _rows (int): Number of rows in the simulation map.
        _cols (int): Number of columns in the simulation map.
        turn_counter (int): Counter for the simulation turns.
        map (Map): The simulation map.
        actions (Actions): The actions controller for the simulation.

    Methods:
        start_simulation(init_population_distribution): Starts the simulation loop.
        next_turn(list_of_creatures): Simulates and renders the next turn for all creatures.
        console_renderer(): Renders the current state of the simulation map in the console.
        pause_simulation(): Pauses the simulation loop based on user input.
    """

    def __init__(self, rows, cols, init_population_distribution):
        """
        Initialize the simulation.

        Args:
           rows (int): Number of rows in the simulation map.
           cols (int): Number of columns in the simulation map.
           init_population_distribution (dict): Initial population distribution for entities.
        """
        self.turn_counter = 0
        self.map = Map(rows, cols)
        self.actions = Actions(self.map)
        self.start_simulation(init_population_distribution)

    def start_simulation(self, init_population_distribution):
        """
        Starts an infinite loop of simulation and rendering.

        Args:
            init_population_distribution (dict): Initial population distribution for entities in percentage.
        """
        init_population = self.actions.init_actions(init_population_distribution)
        print("Симуляция начинается....")
        self.console_renderer()
        while True:
            list_of_creatures = self.map.get_list_of_creatures()
            print(f"Раунд {self.turn_counter}")
            none_path_counter = self.next_turn(list_of_creatures)
            if none_path_counter == len(list_of_creatures['Predator']):
                break
            if self.pause_simulation():
                continue
            if (len(list_of_creatures['Herbivore']) == 0 or
                    len(list_of_creatures['Predator']) == 0):
                break

        list_of_creatures = self.map.get_list_of_creatures()
        print(f"Симуляция завершилась за {self.turn_counter} раундов. \n"
              f"На поле осталось: ")
        for key, value in list_of_creatures.items():
            print(key + ": из " + str(init_population[key]) + " -> " + str(len(value)))

    def next_turn(self, list_of_creatures):
        """
        Simulates and renders the steps taken by all creatures in a single turn.

        Args:
            list_of_creatures (dict): Dictionary of creature populations.

        Returns:
            int: Number of turns with no valid path for predators.
        """
        none_path_counter = 0
        for creature in list_of_creatures['Herbivore'] + list_of_creatures['Predator']:
            none_path_counter += self.actions.turn_actions(creature, list_of_creatures['Herbivore'])
            self.console_renderer()
        self.turn_counter += 1
        return none_path_counter

    def console_renderer(self):
        """
        Renders the current state of the simulation map in the console.
        """
        for x in range(self.map.rows):
            for y in range(self.map.cols):
                coord = Coordinate(x, y)
                entity = self.map.get_entity(coord)
                if not self.map.is_empty(coord):
                    print(entity, end='')
                else:
                    emj = '\u2B1B'
                    print(f"{emj.center(3)}", end='')
            print("  " + str(x))
        print()
        sleep(1)

    @staticmethod
    def pause_simulation():
        """
        Pauses the infinite loop of simulation and rendering based on user input.

        Returns:
            bool: True if simulation should be paused, False otherwise.
        """
        is_not_pause = int(input("Продолжить - 1, пауза - 0: "))
        if not is_not_pause:
            if int(input("Нажмите 0 для выхода или 1 для продолжения: ")):
                return True
            else:
                raise SystemExit("Программа прервана")


if __name__ == '__main__':
    rows = 9
    cols = 9
    init_population_distribution = {Rock: 9,
                                    Tree: 10,
                                    Grass: 15,
                                    Herbivore: 10,
                                    Predator: 6}
    Simulation(rows, cols, init_population_distribution)
