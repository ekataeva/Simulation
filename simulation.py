from typing import Any, Dict

from entities import Tree, Rock, Grass, Herbivore, Predator
from actions import bfs, is_not_pause
from random import randrange
from map import Map
import math
from time import sleep


class Simulation:
    """Главный класс приложения

    Атрибуты:
    -------

    - Карту
    - Счётчик ходов
    - Рендерер поля
    - Actions - список действий, исполняемых перед стартом симуляции или на каждом ходу

    Симуляция содержит 2 основных массива действий:
    - initActions - действия, совершаемые перед стартом симуляции. Пример - расставить объекты и существ на карте
    - turnActions - действия, совершаемые каждый ход. Примеры - передвижение существ, добавить травы
     или травоядных, если их осталось слишком мало

    Методы:
    -------
    start_simulation() - запустить бесконечный цикл симуляции и рендеринга
    is_not_pause()     - приостановить бесконечный цикл симуляции и рендеринга
    next_turn()        - просимулировать и отрендерить один ход

"""

    def __init__(self, rows, cols, population):
        self.map = Map(rows, cols)
        self._rows = rows
        self._cols = cols
        self.move_counter = 0
        self.init_actions(population)

    _entity_list = {'Predator': [], 'Herbivore': [], 'Grass': [], 'Tree': [], 'Rock': []}

    def init_actions(self, population):
        print("Симуляция начинается....")
        init_population_list = {'Predator': 0, 'Herbivore': 0, 'Grass': 0, 'Tree': 0, 'Rock': 0}
        for ent_cls, value in population.items():
            ent_quantity = math.ceil(self._rows * self._cols * value / 100)
            self.make_entities(ent_cls, ent_quantity)
            init_population_list[ent_cls.__name__] = ent_quantity
        self.console_render()

        while self._entity_list['Herbivore'] and self._entity_list['Predator']:
            print(f"Раунд {self.move_counter}")
            none_path_counter = self.turn_actions()
            if none_path_counter == len(self._entity_list['Predator']):
                break
            # удаление экземпляров классов Grass & Herbivore из self._entity_list (is_actual = False)
            self.__clean_not_actual_ent()
            if is_not_pause():
                continue

        print(f"Симуляция завершилась за {self.move_counter} раундов. \n"
              f"На поле осталось: ")
        for key, value in self._entity_list.items():
            print(key + ": из " + str(init_population_list[key]) + " -> " + str(len(value)))

    def make_entities(self, ent_cls, ent_quantity):
        coordinate = ()
        for i in range(ent_quantity):
            while len(coordinate) < 2 or not self.map.is_empty(coordinate):
                x = randrange(0, self._rows, 1)
                y = randrange(0, self._cols, 1)
                coordinate = (x, y)
            entity = ent_cls(coordinate, f'{ent_cls.__name__} {i}', )
            self._entity_list[ent_cls.__name__].append(entity)
            self.map.place_entity(coordinate, entity)

    def console_render(self):
        for x in range(self._rows):
            for y in range(self._cols):
                coord = (x, y)
                entity = self.map.get_entity(coord)
                if not self.map.is_empty(coord) and entity.is_actual:
                    print(entity, end='')
                else:
                    emj = '\u2B1B'
                    print(f"{emj.center(3)}", end='')
            print("  " + str(x))
        print()
        sleep(1)

    def turn_actions(self):
        self.__check_gras()
        none_path_counter = 0

        # шаги всех существ симуляции за один раунд
        for creature in (self._entity_list['Herbivore'] + self._entity_list['Predator']):
            if creature.is_actual:
                # Найти путь существа к ресурсу
                path = self._find_way(creature)

                # Если путь отсутствует -> нет ресурса или тупик
                if path is None:
                    print(f'Для {creature} с координатами {creature.coordinate} нет достижимого ресурса')
                    creature.HP -= 1
                    if isinstance(creature, Predator):
                        none_path_counter += 1

                else:
                    # Ход существа
                    move_status = creature.make_move(path)
                    # Удалить исходную позицию существа
                    if self.map.get_entity(path[0]):
                        self.map.del_entity(path[0])
                    # Обработать ход существа в карте
                    if move_status == "attack":
                        self.__attack_actions(creature, path)
                    else:
                        self.map.place_entity(creature.coordinate, creature)
                    print(f"{creature} сходил на {creature.coordinate}")

                if creature.HP <= 0:
                    creature.is_actual = False
                self.console_render()

        self.move_counter += 1
        return none_path_counter

    def __check_gras(self):
        if len(self._entity_list['Herbivore']) > len(self._entity_list['Grass']):
            self.make_entities(Grass, len(self._entity_list['Herbivore']))

    def __attack_actions(self, creature, path):
        # хищник атаковал травоядное: количество HP травоядного уменьшается на силу атаки хищника
        if hasattr(self.map.get_entity(path[-1]), 'HP'):
            self.map.get_entity(path[-1]).HP -= creature.attack
            if self.map.get_entity(path[-1]).HP <= 0:
                # 'мягкое' удаление травоядного
                self.map.get_entity(path[-1]).is_actual = False
                self.map.place_entity(path[-1], creature)
            else:
                self.map.place_entity(path[-2], creature)
                creature.coordinate = path[-2]
        # травоядное съело траву:
        else:
            #   мягкое удаление травы (объект по координате)
            #   координата травоядного = координата конца пути
            self.map.get_entity(path[-1]).is_actual = False
            self.map.place_entity(path[-1], creature)

    def _find_way(self, creature):
        start_cell = creature.coordinate
        if type(creature) is Herbivore:
            target_class = Grass
        else:
            target_class = Herbivore
        print(f"{creature.name} {creature} ищет {target_class.__name__}")
        path = bfs(self.map, start_cell, target_class)
        print(f"Path: {path}")
        return path

    def __clean_not_actual_ent(self):
        # очищение списка существ после мягкого удаления в цикле turn_actions
        self._entity_list['Predator'] = [obj for obj in self._entity_list['Predator'] if obj.is_actual]
        self._entity_list['Herbivore'] = [obj for obj in self._entity_list['Herbivore'] if obj.is_actual]
        self._entity_list['Grass'] = [obj for obj in self._entity_list['Grass'] if obj.is_actual]
