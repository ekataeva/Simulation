from collections import deque

from entities import Tree, Rock, Grass, Herbivore, Predator
from random import randrange
from map import Map
import time


class Simulation:
    """Главный класс приложения, включает в себя:

    - Карту
    - Счётчик ходов
    - Рендерер поля
    - Actions - список действий, исполняемых перед стартом симуляции или на каждом ходу

    Методы:
    -------
    next_turn()          - просимулировать и отрендерить один ход
    start_simulation()   - запустить бесконечный цикл симуляции и рендеринга
    pause_simulation()   - приостановить бесконечный цикл симуляции и рендеринга

    Actions
    --------
    Action - действие, совершаемое над миром. Например - сходить всеми существами.
    Это действие итерировало бы существ и вызывало каждому makeMove().
    Каждое действие описывается отдельным классом и совершает операции над картой.
    Симуляция содержит 2 массива действий:
    - initActions - действия, совершаемые перед стартом симуляции. Пример - расставить объекты и существ на карте
     turnActions - действия, совершаемые каждый ход. Примеры - передвижение существ, добавить травы
     или травоядных, если их осталось слишком мало
"""

    def __init__(self, rows, cols):
        self.map = Map(rows, cols)
        self._rows = rows
        self._cols = cols
        self.move_counter = 0
        self.is_pause = False
        self.init_actions()

    _entity_classes = [Predator, Tree, Rock, Herbivore, Grass]
    _entity_list = {'herbivore': [], 'predator': [], 'tree': [], 'rock': [], 'grass': []}

    def init_actions(self):
        print("Симуляция начинается....")
        for ent_cls in self._entity_classes:
            self.make_entities(ent_cls)
        self.render()
        while self._entity_list['herbivore']:  # => len(self._entity_list['predator']) > 0
            if not self.is_pause:
                print(f"Раунд {self.move_counter}")
                self.next_turns()
                is_not_pause = int(input("Продолжить - 1, пауза - 0: "))
                if not is_not_pause:
                    self.is_pause = True
                    if int(input("Нажмите 0 для выхода или 1 для продолжения: ")):
                        continue
                    else:
                        # Вызвать исключение SystemExit для завершения программы
                        raise SystemExit("Программа прервана")

    def make_entities(self, ent_cls):
        coordinate = ()
        for i in range(self._rows):
            while len(coordinate) < 2 or not self.map.is_free(coordinate):
                x = randrange(0, self._rows, 1)
                y = randrange(0, self._cols, 1)
                coordinate = (x, y)
            entity = ent_cls(f'{ent_cls}: {i}', coordinate)
            self._entity_list[ent_cls.__name__.lower()].append(entity)
            self.map.add_entity(coordinate, entity)

    def render(self):
        for x in range(self._rows):
            for y in range(self._cols):
                coord = (x, y)
                if not self.map.is_free(coord):
                    print(self.map.cells[coord], end='')
                else:
                    print('{:3}'.format('\u2B1B'), end='')
            print(x)
        print()

    def next_turns(self):
        for creatures in (self._entity_list['herbivore'], self._entity_list['predator']):
            for creature in creatures:
                print(f"{creature} ищет путь")
                path = self._find_way(creature)
                print(f"{creature} нашел путь")
                self._move(creature, path)
                print(f"{creature} сделал ход")
                self.render()
                time.sleep(1)
        self.move_counter += 1
        if len(self._entity_list['herbivore']) > len(self._entity_list['grass']):
            self.make_entities(Grass)

    def _find_way(self, creature):
        start_cell = creature.coordinate
        if type(creature) is Herbivore:
            target_class = Grass
        else:
            target_class = Herbivore
        print(f'target_class: {target_class}')
        path = self.__bfs(start_cell, target_class)
        print(f"Creature: {creature}, path: {path}")
        return path

    def __bfs(self, start_cell, target_class):
        parents = {cell: None for cell in self.map.graph}
        checked = set()
        queue = deque([start_cell])
        target_cell = None

        while queue:
            cur_cell = queue.popleft()
            checked.add(cur_cell)
            print(f'cur_cell: {cur_cell}')
            for neigh in self.map.graph[cur_cell]:
                if neigh not in checked:
                    if parents[neigh] is None:
                        parents[neigh] = cur_cell
                        # print(f"parents {neigh}: {parents[neigh]}")
                        queue.append(neigh)
                        # print(f"queue: {queue}")
                    if neigh in self.map.cells:
                        # print(f' neigh {neigh} type {type(self.map.cells[neigh])} in self.map.cells')
                        # print(f' isinstance: {isinstance(self.map.cells[neigh], target_class)}')
                        if isinstance(self.map.cells[neigh], target_class):
                            target_cell = neigh
                            print(f'target_cell: {target_cell}')
                            queue.clear()
                            break

        path = [target_cell]
        parents[start_cell] = None
        parent = parents[target_cell]
        print(parents)
        print(f'parent of target cell {target_cell} is {parent}')
        while parent is not None:
            print(f'parent of current cell is {parent}')
            path.append(parent)
            print(path)
            parent = parents[parent]
        path = path[::-1]
        print(f"path: {path}")
        return path

    def _move(self, creature, path):
        pass
