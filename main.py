from simulation import Simulation
from entities import Tree, Rock, Grass, Herbivore, Predator


"""Симуляция 2D мира (матрица NxM), населённого травоядными и хищниками. 
    Мир содержит также траву, которой питаются травоядные, и статичные объекты.
    
    В момент запуска игры создается поле симуляции NхМ с существами (наследники класса Entity).
    далее - действия травоядных и хищников пока есть травоядные, прописаны в классе Simulation. 
        Трава появляется по необходимости (окончании  имеющейся).
        Действия: поиск и поедание ресурса, визуализация состояния поля.    
"""

rows = 9  # int(input("Enter map's row size: "))
cols = 9  # int(input("Enter map's column size: "))

population = {Rock: 10,  # int(input("Enter Rock's population in %: ")),
              Tree: 10,  # int(input("Enter Tree's population in %: ")),
              Grass: 15,  # int(input("Enter Grass's population in %: ")),
              Herbivore: 10,  # int(input("Enter Herbivore's population in %: ")),
              Predator: 5}  # int(input("Enter Predator's population in %: ")) }

game = Simulation(rows, cols, population)