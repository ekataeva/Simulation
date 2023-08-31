"""
Entities Package
===============

This package contains classes that represent various entities in the simulation world.

Modules:
- entity: The root abstract class for all creatures and objects, initializing core properties.
- rock: The class for static objects that function as obstacles on the map.
- tree: The class for static objects that function as obstacles on the map.
- grass: The class for static objects that serve as resources for herbivores.
- creature: An abstract creatures class serves as the superclass for both herbivores and predators.
- herbivore: The class of dynamic creatures - herbivores - functions as a resource for predators.
- predator: The class of dynamic creatures - predators - strive to locate resources in the form of herbivores.

"""
from entities.entity import Entity
from entities.rock import Rock
from entities.tree import Tree
from entities.grass import Grass
from entities.creature import Creature
from entities.herbivore import Herbivore
from entities.predator import Predator
