class Map:
    """
    Карта - поле размером NxM, содержит в себе коллекцию для хранения существ и их расположения.

    АТРИБУТЫ:
    --------
    __rows - количество строк поля

    __cols - количество колонок поля

    __cells - поле симуляции - словарь, где ключ - координата (х, у) - массив двух чисел, значение - существо. Описываются только занятые клетки.

    graph - карта для навигации существ - граф в виде словаря, где ключ - координата (х, у) - массив двух чисел, значение - сет, содержащий соседние клетки поля.

    МЕТОДЫ:
    -------
    place_entity - создает существо - добавляет существо в пустую клетку по заданной координате

    is_empty    - проверяет, занята ли клетка - существует ли такой массив в ключах карты

    get_entity  - возвращает существо по заданной координате

    del_entity - удаляет существо по заданной координате

    _make_graph - создает карту для дальнейшей навигации существ
    """

    def __init__(self, rows, cols):
        self.__cells = dict()
        self.__rows = rows
        self.__cols = cols
        self.graph = {(x, y): set() for x in range(rows) for y in range(cols)}
        self._make_graph()

    def place_entity(self, coord, entity):
        self.__cells[coord] = entity

    def is_empty(self, coord):
        if coord in self.__cells:
            return False
        return True

    def get_entity(self, coord) -> object:
        if self.is_empty(coord):
            return None
        return self.__cells[coord]

    def del_entity(self, coord):
        if not self.is_empty(coord):
            del self.__cells[coord]

    def _make_graph(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                v1 = (i, j)
                for i_modified, j_modified in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= i_modified < self.__rows and 0 <= j_modified < self.__cols:
                        v2 = (i_modified, j_modified)
                        self._add_edge(v1, v2)

    def _add_edge(self, v1, v2):
        self.graph[v1].add(v2)
        self.graph[v2].add(v1)
