class Move:
    """ A Player where the user chooses its moves.

    === Public Attributes ===
    row:
        The row that move takes place.
    col:
        The column that move takes place.
    """
    row: int
    col: int

    def __init__(self, row: int, col: int) -> None:
        """ Creates Move with <row> row and <col> column.
        """
        self.row = row
        self.col = col

    def get_row(self) -> int:
        """ Returns the row.
        """
        return self.row

    def get_col(self) -> int:
        """ Returns the column.
        """
        return self.col

    def to_string(self) -> str:
        """ Returns the string representation of Move in (row, column).
        """
        return "(" + str(self.row) + "," + str(self.col) + ")"
