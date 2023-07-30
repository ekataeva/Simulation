from abc import ABC, abstractmethod


class Entity(ABC):
    """
    Корневой абстрактный класс для всех существ и объектов.
    Инициализирует основные поля.
    """
    def __init__(self, coordinate, name="ent", emj=None):
        self.name = name
        self.coordinate = coordinate
        self.emj = emj
        self.is_actual = True

    def __str__(self):
        return f"{self.emj.center(3)}"


class Rock(Entity):
    """
    Класс статичных объектов, с которыми нельзя взаимодействовать.
    Экземпляры класса имеют спрайт, занимают клетку поля и являются препятствием на пути.
    """

    def __init__(self, coordinate, name):
        emj = '\U0001F5FB'
        super().__init__(coordinate, name, emj)


class Tree(Entity):
    """
    Класс статичных объектов, с которыми нельзя взаимодействовать.
    Экземпляры класса имеют спрайт, занимают клетку поля и являются препятствием на пути.
    """

    # статичные объекты - нельзя взаимодействовать
    def __init__(self, coordinate, name):
        emj = '\U0001F334'
        super().__init__(coordinate, name, emj)


class Grass(Entity):
    """
    Класс статичных объектов, которые являются ресурсом для травоядных.
    Экземпляры класса имеют спрайт и занимают клетку поля.
    """
    def __init__(self, coordinate, name):
        emj = '\U0001F96C'
        super().__init__(coordinate, name, emj)


class Creature(Entity, ABC):
    """
    Абстрактный класс существ - суперкласс для травоядных и хищников.
    Имеет общий для наследников метод make_move.
    """
    # скорость (сколько клеток может пройти за 1 ход)
    speed = 1
    HP = 4

    def make_move(self, path):
        # если длина пути меньше скорости - поедание ресурса
        if self.speed + 1 >= len(path):
            self.coordinate = path[-1]
            self.HP += 1
            return "attack"
        # иначе - движение в сторону ресурса
        else:
            self.coordinate = path[self.speed]
            self.HP -= 1
            return None


class Herbivore(Creature):
    """
    Класс динамичных существ - травоядных, являются ресурсом для хищников.
    Экземпляры класса имеют спрайт зебры и пытаются найти ресурс - траву.
    Их HP (hit-points - "количество жизней") уменьшается при нападении хищников на силу атаки хищника.
    При HP = 0 травоядное погибает.
    """

    def __init__(self, coordinate, name):
        emj = '\U0001F993'  # zebra
        super().__init__(coordinate, name, emj)


class Predator(Creature):
    """
    Класс динамичных существ - хищников.
    Экземпляры класса имеют спрайт льва и пытаются найти ресурс - травоядных.
    """
    def __init__(self, coordinate, name):
        emj = '\U0001F981'  # lion
        super().__init__(coordinate, name, emj)
        self.attack = 2  # сила атаки
        self.speed = 2
        self.HP = 2
