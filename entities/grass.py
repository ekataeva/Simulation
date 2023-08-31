from entities.entity import Entity


class Grass(Entity):
    """
    Class representing static objects that serve as resources for herbivores.

    Grass entities are positioned within cells on the map and provide sustenance
    for herbivores in the simulation.

    Attributes:
        coordinate (Coordinate): The coordinate of the grass entity on the map.
        name (str): The name of the grass entity.
        emj (str): The emoji representation of the grass entity.

    Args:
        coordinate (Coordinate): The coordinate of the grass entity on the map.
        name (str): The name of the grass entity.
    """

    def __init__(self, coordinate, name):
        emj = '\U0001F96C' # grass emoji
        super().__init__(coordinate, name, emj)
