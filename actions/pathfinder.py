from collections import deque

from entities import Grass, Herbivore
from map import Coordinate


class PathFinder:
    """
        Find a path for the target using breadth-first search.
    """
    def __init__(self, world_map):
        """
        Initialize the PathFinder object.

        Args:
            rows (int): Number of rows in the map.
            cols (int): Number of columns in the map.
            world_map (Map): The map where creatures move.
        """
        self.map = world_map
        self.__graph = {Coordinate(row, col): set() for row in range(self.map.rows) for col in range(self.map.cols)}
        self._make_graph()

    def _make_graph(self):
        """
        Build the graph of coordinates for BFS.

        Args:
            rows (int): Number of rows in the map.
            cols (int): Number of columns in the map.
        """
        for i in range(self.map.rows):
            for j in range(self.map.cols):
                v1 = Coordinate(i, j)
                for i_modified, j_modified in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= i_modified < self.map.rows and 0 <= j_modified < self.map.cols:
                        v2 = Coordinate(i_modified, j_modified)
                        self._add_edge(v1, v2)

    def _add_edge(self, v1, v2):
        self.__graph[v1].add(v2)
        self.__graph[v2].add(v1)

    def find_path(self, creature) -> list or None:
        """
        Find a path for a creature to a target resource.

        Args:
            creature (Creature): The creature (Herbivore or Predator) to find a path for.

        Returns:
            list or None: A list of cells representing the path, or None if no path is found.
        """
        start_cell = creature.coordinate
        if type(creature) is Herbivore:
            target_class = Grass
        else:
            target_class = Herbivore
        print(f"{creature.name} {creature} ищет {target_class.__name__}")

        path = self._bfs(start_cell, target_class)
        return path

    def _bfs(self, start_cell, target_class):
        """
        Perform breadth-first search to find a path to a target class.

        Args:
            start_cell (tuple): The starting cell for the search.
            target_class (class): The target class to find a path to.

        Returns:
            list or None: A list of cells representing the path, or None if no path is found.
        """
        parents = {cell: None for cell in self.__graph}
        checked = set()
        queue = deque([start_cell])
        target_cell = None

        while queue:
            cur_cell = queue.popleft()
            checked.add(cur_cell)
            for neigh in self.__graph[cur_cell]:
                neigh_ent = self.map.get_entity(neigh)
                if neigh not in checked \
                        and (neigh_ent is None or isinstance(neigh_ent, target_class)):
                    if parents[neigh] is None:
                        parents[neigh] = cur_cell
                        queue.append(neigh)
                    if neigh_ent and isinstance(neigh_ent, target_class):
                        target_cell = neigh
                        queue.clear()
                        break

        return self._reconstruct_path(start_cell, target_cell, parents)

    @staticmethod
    def _reconstruct_path(start_cell, target_cell, parents):
        """
        Reconstruct the path based on parent cells.

        Args:
            start_cell (tuple): The starting cell of the path.
            target_cell (tuple): The target cell of the path.
            parents (dict): A dictionary mapping cells to their parent cells.

        Returns:
            list or None: A list of cells representing the path, or None if no path is found.
        """
        if target_cell is not None:
            path = [target_cell]
            parents[start_cell] = None
            parent = parents[target_cell]
            while parent is not None:
                path.append(parent)
                parent = parents[parent]
            path.reverse()
            return path
        else:
            return None
