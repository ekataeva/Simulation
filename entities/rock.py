from entities.entity import Entity


class Rock(Entity):
    """
    Class representing static objects known as rocks.

    Rocks are instances that cannot be interacted with. They have attributes such as
    "sprite," and they occupy specific cells on the map. These objects serve as obstacles.

    Attributes:
        coordinate (Coordinate): The coordinate of the rock on the map.
        name (str): The name of the rock.
        emj (str): The emoji representation of the rock.

    Args:
        coordinate (Coordinate): The coordinate of the rock on the map.
        name (str): The name of the rock.
    """
    def __init__(self, coordinate, name):
        emj = '\U0001F5FB' # rock emoji
        super().__init__(coordinate, name, emj)
