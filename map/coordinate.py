class Coordinate:
    """
    Represents the coordinates of a location on a map.

    Attributes:
        row (int): The row number of the coordinate.
        col (int): The column number of the coordinate.
    """

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        """
        Returns a string representation of the coordinate in the format (row, col).
        """
        return f'({self.row}, {self.col})'

    def __eq__(self, other):
        """
        Checks if two coordinates are equal.
        """
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        """
        Returns a hash value for the coordinate.
        """
        return hash((self.row, self.col))
