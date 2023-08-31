from entities.creature import Creature


class Herbivore(Creature):
    """
    Class representing dynamic creatures known as herbivores.

    Herbivores function as resources for predators in the simulation. They have
    attributes like "sprite" and actively search for resources such as grass.

    Attributes:
        coordinate (Coordinate): The coordinate of the herbivore on the map.
        name (str): The name of the herbivore.
        emj (str): The emoji representation of the herbivore.
        speed (int): The speed at which the herbivore can move per turn.
        HP (int): The health points of the herbivore, representing its vitality.

    Args:
        coordinate (Coordinate): The coordinate of the herbivore on the map.
        name (str): The name of the herbivore.
    """
    def __init__(self, coordinate, name):
        emj = '\U0001F993'  # zebra emoji
        super().__init__(coordinate, name, emj)

    def _attack_actions(self, world_map, path):
        world_map.place_entity(path[-1], self)
        self.coordinate = path[-1]
        if world_map.get_entity(path[0]):
            world_map.del_entity(path[0])
