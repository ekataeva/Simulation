from entities.entity import Entity


class Tree(Entity):
    """
    Class representing static objects known as trees.

    Trees are instances that cannot be interacted with. They have attributes such as
    "sprite," and they occupy specific cells on the map. These objects serve as obstacles.

    Attributes:
        coordinate (Coordinate): The coordinate of the tree on the map.
        name (str): The name of the tree.
        emj (str): The emoji representation of the tree.

    Args:
        coordinate (Coordinate): The coordinate of the tree on the map.
        name (str): The name of the tree.
    """
    def __init__(self, coordinate, name):
        emj = '\U0001F334' # tree emoji
        super().__init__(coordinate, name, emj)
