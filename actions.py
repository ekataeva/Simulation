from collections import deque


def bfs(cur_map, start_cell, target_class):
    parents = {cell: None for cell in cur_map.graph}
    checked = set()
    queue = deque([start_cell])
    target_cell = None

    while queue:
        cur_cell = queue.popleft()
        checked.add(cur_cell)
        for neigh in cur_map.graph[cur_cell]:
            neigh_ent = cur_map.get_entity(neigh)
            # Если соседняя клетка еще не проверена и (в клетке нет существа либо существо искомого класса):
            if neigh not in checked \
                    and (neigh_ent is None or isinstance(neigh_ent, target_class)):
                if parents[neigh] is None:
                    parents[neigh] = cur_cell
                    queue.append(neigh)
                if neigh_ent:
                    if isinstance(neigh_ent, target_class) and neigh_ent.is_actual:
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


def is_not_pause():
    is_not_pause = int(input("Продолжить - 1, пауза - 0: "))
    if not is_not_pause:
        if int(input("Нажмите 0 для выхода или 1 для продолжения: ")):
            return True
        else:
            # Вызвать исключение SystemExit для завершения программы
            raise SystemExit("Программа прервана")
