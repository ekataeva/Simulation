from entities import Tree, Rock, Grass, Herbivore, Predator


class Map:
    """Карта, содержит в себе коллекцию для хранения существ и их расположения.


    АТРИБУТЫ:
    --------

    МЕТОДЫ:
    -------
    при инициации - создание словаря, где ключ - (х, у) - массив двух чисел, значение - существо.
    Описываются только занятые клетки.

    создать существо - приватный - проверяет, занята ли клетка и добавляет существо в пустую клетку.
    проверка занята ли клетка - существует ли такой массив в ключах карты
    удалить существо
    """

    def __init__(self, rows, cols):
        self.cells = dict()
        self.__rows = rows
        self.__cols = cols
        self.graph = {(x, y): set() for x in range(rows) for y in range(cols)}
        self.make_graph()

    # def is_in_borders(self, coord):
    #     if coord[0] < self.__rows and coord[1] < self.__cols:
    #         return True
    #     return False

    def add_entity(self, coord, entity):
        if self.is_free(coord):
            self.cells[coord] = entity

    def is_free(self, coord):
        if coord in self.cells:
            return False
        return True

    # def del_entity(self, coord):
    #     if not self.is_free(coord):
    #         del self.cells[coord]

    def make_graph(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                v1 = (i, j)
                for i_modified, j_modified in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    # (i + 1, j + 1), (i - 1, j + 1), (i - 1, j - 1), (i + 1, j -1):
                    if 0 <= i_modified < self.__rows and 0 <= j_modified < self.__cols:
                        v2 = (i_modified, j_modified)
                        self._add_edge(v1, v2)

    def _add_edge(self, v1, v2):
        self.graph[v1].add(v2)
        self.graph[v2].add(v1)
