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

    Симуляция содержит 2 массива действий:
    - initActions - действия, совершаемые перед стартом симуляции. Пример - расставить объекты и существ на карте
    - turnActions - действия, совершаемые каждый ход. Примеры - передвижение существ, добавить травы
     или травоядных, если их осталось слишком мало

    Методы:
    -------
    start_simulation() - запустить бесконечный цикл симуляции и рендеринга
    is_not_pause()     - приостановить бесконечный цикл симуляции и рендеринга
    next_turn()        - просимулировать и отрендерить один ход

"""

    def __init__(self, rows, cols):
        self.map = Map(rows, cols)
        self._rows = rows
        self._cols = cols
        self.move_counter = 0
        self.is_pause = False
        self.init_actions()

    _entity_list = {'herbivore': [], 'predator': [], 'tree': [], 'rock': [], 'grass': []}

    def init_actions(self):
        print("Симуляция начинается....")
        for ent_cls in [Predator, Tree, Rock, Herbivore, Grass]:
            self.make_entities(ent_cls)
        self.render()
        while self._entity_list['herbivore']:  # => len(self._entity_list['herbivore']) > 0
            if not self.is_pause:
                print(f"Раунд {self.move_counter}")
                if len(self._entity_list['herbivore']) > len(self._entity_list['grass']):
                    self.make_entities(Grass)
                self.turn_actions()
                self.__clean_not_live_ent()     # из self._entity_list
                if self.is_not_pause():
                    continue

    def make_entities(self, ent_cls):
        coordinate = ()
        for i in range(3): #self._rows - подумать над количеством!
            while len(coordinate) < 2 or not self.map.is_free(coordinate):
                x = randrange(0, self._rows, 1)
                y = randrange(0, self._cols, 1)
                coordinate = (x, y)
            entity = ent_cls(coordinate, f'{ent_cls}: {i}', )
            self._entity_list[ent_cls.__name__.lower()].append(entity)
            self.map.add_entity(coordinate, entity)

    def render(self):
        for x in range(self._rows):
            for y in range(self._cols):
                coord = (x, y)
                if not self.map.is_free(coord) and self.map.cells[coord].is_live:
                    print(self.map.cells[coord], end='')
                else:
                    print('{:3}'.format('\u2B1B'), end='')
            print(x)
        print()

    def is_not_pause(self):
        is_not_pause = int(input("Продолжить - 1, пауза - 0: "))
        if not is_not_pause:
            self.is_pause = True
            if int(input("Нажмите 0 для выхода или 1 для продолжения: ")):
                return True
            else:
                # Вызвать исключение SystemExit для завершения программы
                raise SystemExit("Программа прервана")

    def turn_actions(self):
        # шаги всех существ симуляции за один раунд
        if len(self._entity_list['herbivore']) > len(self._entity_list['grass']):
            self.make_entities(Grass)
        for creatures in (self._entity_list['herbivore'], self._entity_list['predator']):
            for creature in creatures:
                if creature.is_live:
                    print(f"{creature.name} {creature} ищет путь")
                    path = self._find_way(creature)
                    if path is not None:
                        print(f"{creature} нашел путь")
                        move_status = creature.make_move(path)
                        if path[0] in self.map.cells:
                            del self.map.cells[path[0]]
                        if move_status is not None:
                            print(move_status)
                        if move_status == "attack":
                            # хищник атаковал травоядное: количество HP травоядного уменьшается на силу атаки хищника
                            if hasattr(self.map.cells[path[-1]], 'HP'):
                                self.map.cells[path[-1]].HP -= creature.attack
                                if self.map.cells[path[-1]].HP <= 0:
                                    # мягкое удаление травоядного
                                    self.map.cells[path[-1]].is_live = False
                                    self.map.cells[path[-1]] = creature
                                else:
                                    self.map.cells[path[-2]] = creature
                                    creature.coordinate = path[-2]
                            # травоядное съело траву:
                            else:
                                #   мягкое удаление травы (объект по координате)
                                #   координата травоядного = координата конца пути
                                self.map.cells[path[-1]].is_live = False
                                self.map.cells[path[-1]] = creature
                        else:
                            self.map.cells[creature.coordinate] = creature
                        print(f"{creature} сделал ход")
                    else:
                        print(f'Для {creature} нет ресурса')
                    self.render()
                    # time.sleep(2)
        self.move_counter += 1

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
            for neigh in self.map.graph[cur_cell]:
                if neigh not in checked \
                        and (neigh not in self.map.cells or isinstance(self.map.cells[neigh], target_class)):
                    if parents[neigh] is None:
                        parents[neigh] = cur_cell
                        queue.append(neigh)
                    if neigh in self.map.cells:
                        if isinstance(self.map.cells[neigh], target_class) and self.map.cells[neigh].is_live:
                            target_cell = neigh
                            queue.clear()
                            break

        if target_cell is not None:
            path = [target_cell]
            parents[start_cell] = None
            parent = parents[target_cell]
            while parent is not None:
                path.append(parent)
                parent = parents[parent]
            path = path[::-1]
            return path
        else:
            return None

    def __clean_not_live_ent(self):
        # очищение списка существ после мягкого удаления в цикле turn_actions
        self._entity_list['herbivore'] = [obj for obj in self._entity_list['herbivore'] if obj.is_live]
        self._entity_list['grass'] = [obj for obj in self._entity_list['grass'] if obj.is_live]
