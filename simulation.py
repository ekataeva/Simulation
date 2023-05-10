from abc import *

class Entity(metaclass=ABCMeta):
  # Корневой абстрактный класс для всех существ и объектов
  # навигация по классу мап
  defaultHP = 1
  def __init__(self, name):
    self.name = name

class Grass(Entity):
  emj = '\U0001F331' #!!!
  def __init__(self):
    # ресурс для травоядных
    pass

class Rock(Entity):
  # статичные объекты - нельзя взаимодействовать
  emj = '\U0001F5FB'
  def __init__(self):
    pass

class Tree(Entity):
  # статичные объекты - нельзя взаимодействовать
  emj = '\U0001F333'

  def __init__(self):

    pass

class Creature(Entity, metaclass=ABCMeta):
  # имеет скорость (сколько клеток может пройти за 1 ход),
  defaultSpeed = 3
  # hitpoints - "количество жизней"
  HP = 3

  # Имеет абстрактный метод makeMove() - сделать ход.
  # Наследники будут реализовывать этот метод каждый по-своему.
  def makeMove(self, coordinate):
    newCoordinate = findWay(coordinate)
    return newCoordinate
    
class Herbivore(Creature):
  emj = '\U0001F993' #zebra
  def __init__(self):
    pass
  # может потратить свой ход на движение в сторону травы, либо на её поглощение.

class Predator(Creature):
  force = 4
  emj = '\U0001F981' #lion
  def __init__(self):
    # В дополнение к полям класса Creature, имеет силу атаки.
    # Сила атаки - урон, который хищик наносит жертве при атаке
    # Например - HP травоядного = 10, сила атаки хищника = 5.
    # После атаки, у травоядного останется 10 - 5 = 5 жизней
    pass

  # может потратить ход на:
  # Переместиться (чтобы приблизиться к жертве - травоядному)
  # Атаковать травоядное. При этом количество HP травоядного уменьшается на силу атаки хищника.

class Map:
  # матрицa NxM, каждое существо или объект занимают клетку целиком, 
  # нахождение в клетке нескольких объектов/существ - недопустимо
  # содержит в себе коллекцию для хранения существ и их расположения
  def __init__(self, row, col):
    self.map = dict()
    for x in range(0, row):
      for y in range(0, col):
        self.map[x, y] = ' '

  # Размер поля ?

class Simulation:
  # Главный класс приложения, включает в себя:
  def __init__(self):
    # Карту
    # self.map =
    # Счётчик ходов
    self.moveCounter = 0
    # Рендерер поля ???? - function of all creations
      # -> function of all creatures thas act (one method)
    # Actions - список действий, исполняемых перед стартом симуляции или на каждом ходу (детали ниже)
    self.actions = []



  def nextTurn():
    # просимулировать и отрендерить один ход
    pass
  def startSimulation():
    # запустить бесконечный цикл симуляции и рендеринга
    pass
  def pauseSimulation():
    # приостановить бесконечный цикл симуляции и рендеринга
    pass
class Actions:
  # Action - действие, совершаемое над миром. 
  # Например - сходить всеми существами. Это действие 
  # итерировало бы существ и вызывало каждому makeMove(). 
  # Каждое действие описывается отдельным классом и совершает операции над картой. 
  # Симуляция содержит 2 массива действий:
    # initActions - действия, совершаемые перед стартом симуляции. Пример - расставить объекты и существ на карте
    # turnActions - действия, совершаемые каждый ход. Примеры - передвижение существ, добавить травы или травоядных, если их осталось слишком мало
  # алгоритм поиска пути
  pass

if __name__ == '__main__':
  lion = Predator()
  zebra = Herbivore()
  rock = Rock()
  tree = Tree()
  grass = Grass()

  row = col = 9
  map = Map(row, col)
  print(lion.emj, zebra.emj, rock.emj, tree.emj, grass.emj)
  for x in range(0, row):
    for y in range(0, col):
      print(map.map[x, y], end=" ")
    print()


  a = 0
