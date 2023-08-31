class Map:
    """
    Map - a field with dimensions NxM, contains a collection for storing entities and their locations.

    Attributes:
        __rows (int): The number of rows on the field.
        __cols (int): The number of columns on the field.
        __cells (dict): Simulation field - a dictionary where the key is a coordinate (row, col) and the value is an entity.
                        Only occupied cells are described.

    Methods:
        place_entity(coord, entity): Creates an entity - adds an entity to an empty cell at the specified coordinate.
        is_empty(coord): Checks if a cell is empty - whether such an array exists among the keys of the map.
        get_entity(coord): Returns an entity at the specified coordinate.
        del_entity(coord): Deletes an entity at the specified coordinate.
        get_list_of_creatures(): Returns a dictionary of lists of creatures, categorized by class name.
        get_list_of_grass(): Returns a list of grass entities.
    """
    def __init__(self, rows, cols):
        """
        Initialize a map with the specified number of rows and columns.

        Args:
            rows (int): The number of rows.
            cols (int): The number of columns.
        """
        self.__cells = dict()
        self.rows = rows
        self.cols = cols

    def place_entity(self, coord, entity):
        """
        Place an entity at the specified coordinate.

        Args:
            coord (Coordinate): The coordinate where the entity will be placed.
            entity (Entity): The entity to be placed.
        """
        self.__cells[coord] = entity

    def is_empty(self, coord):
        """
        Check if a cell at the specified coordinate is empty.

        Args:
            coord (Coordinate): The coordinate to check.

        Returns:
            bool: True if the cell is empty, False otherwise.
        """
        return coord not in self.__cells

    def get_entity(self, coord) -> object:
        """
        Get the entity at the specified coordinate.

        Args:
            coord (Coordinate): The coordinate to get the entity from.

        Returns:
            Entity or None: The entity at the specified coordinate, or None if the cell is empty.
        """
        return self.__cells.get(coord, None)

    def del_entity(self, coord):
        """
        Delete the entity at the specified coordinate.

        Args:
            coord (Coordinate): The coordinate to delete the entity from.
        """
        if not self.is_empty(coord):
            del self.__cells[coord]

    def get_list_of_creatures(self):
        """
        Get a dictionary of lists of creatures, categorized by their class names.

        Returns:
            dict: A dictionary containing lists of creatures, categorized by class name.
        """
        creatures_population = {'Predator': [], 'Herbivore': []}
        for entity in self.__cells.values():
            from entities import Creature
            if isinstance(entity, Creature):
                creatures_population[entity.__class__.__name__].append(entity)
        return creatures_population

    def get_list_of_grass(self):
        """
        Get a list of grass entities on the map.

        Returns:
            list: A list of grass entities present on the map.
        """
        from entities import Grass
        grass_population = [entity for entity in self.__cells.values() if isinstance(entity, Grass)]
        return grass_population
