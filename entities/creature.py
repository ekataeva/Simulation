from abc import ABC, abstractmethod

from entities.entity import Entity


class Creature(Entity, ABC):
    """
    Abstract base class for creatures, serving as the superclass for herbivores and predators.

    Attributes:
        speed (int): Represents the number of cells a creature can traverse in one turn.
        HP (int): Stands for "Health Points," indicating the creature's health or vitality.

    Methods:
        make_move(path): Determines the movement of the creature.
            - If the path length is less than the creature's speed, it consumes the resource and gains health.
            - Otherwise, the creature moves towards the resource, losing health.

    This class is intended to be inherited by specific creature types.
    """
    speed = 2
    HP = 4

    def make_move(self, world_map, path):
        """
        MOVE the creature along the given path.

        Args:
            world_map (Map): The map of the simulation world.
            path (list): List of cells representing the path to the target.

        Returns:
            str or None: If the creature reaches the resource, returns "attack". Otherwise, returns None.
        """

        if self.speed + 1 >= len(path):
            self.HP += 1
            self._attack_actions(world_map, path)
        else:
            self.coordinate = path[self.speed]
            self.HP -= 1
            world_map.place_entity(self.coordinate, self)
            world_map.del_entity(path[0])

    @abstractmethod
    def _attack_actions(self, world_map, path):
        """
        Perform attack actions during a turn.

        Args:
            world_map (Map): The map of the simulation world.
            path (list): The path taken by the predator.

        """
        pass
