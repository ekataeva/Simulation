from abc import ABC

from map import Coordinate


class Entity(ABC):
    """
    The base abstract class for all creatures and objects in the simulation.

    This class serves as the foundation for initializing core properties of entities,
    including their name, coordinates, emoji representation, and actuality status.

    Attributes:
        name (str): The name of the entity.
        coordinate (Coordinate): The current coordinate of the entity on the map.
        emj (str, optional): The emoji representation of the entity.
        is_actual (bool): A flag indicating whether the entity is still active in the simulation.

    Args:
        coordinate (Coordinate): The initial coordinate of the entity on the map.
        name (str): The name of the entity. Defaults to "ent".
        emj (strl): The emoji representation of the entity.

    """

    def __init__(self, coordinate: Coordinate, name, emj):
        self.name = name
        self.coordinate = coordinate
        self.emj = emj

    def __str__(self):
        return f"{self.emj.center(3)}"
