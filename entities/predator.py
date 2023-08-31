from entities.creature import Creature


class Predator(Creature):
    """
    A class representing dynamic creatures known as predators.

    Predators are entities that are characterized by instances that resemble lions,
    and they aim to locate and consume resources in the form of herbivores.

    Attributes:
        coordinate (Coordinate): The current coordinate of the predator on the map.
        name (str): The name of the predator.
        emoji (str): The emoji representation of the predator.
        attack (int): The strength of the predator's attack.
        speed (int): The movement speed of the predator.
        HP (int): Health Points representing the predator's health or vitality.

    Args:
        coordinate (Coordinate): The initial coordinate of the predator.
        name (str): The name of the predator.

    """

    def __init__(self, coordinate, name):
        emj = '\U0001F981'  # lion emoji
        super().__init__(coordinate, name, emj)
        self.attack = 2
        self.speed = 3
        self.HP = 2

    def _attack_actions(self, world_map, path):
        target_cell = path[-1]
        target_entity = world_map.get_entity(target_cell)
        if target_entity:
            target_entity.HP -= self.attack
            if target_entity.HP <= 0:
                world_map.place_entity(target_cell, self)
                self.coordinate = target_cell
                world_map.del_entity(path[0])

            else:
                if len(path) > 2:
                    world_map.place_entity(path[-2], self)
                    self.coordinate = path[-2]
                    world_map.del_entity(path[0])