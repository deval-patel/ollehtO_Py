from __future__ import annotations


class Board:
    """
    Board class is responsible for keeping track of the board and everything
    that happens on it as well as handling board related tasks such as
    player requesting a move.

        === Public Attributes ===
    no_players:
        Empty space declaring that there are no players located in
        current position.
    player1:
        Represents first player's token
    player2:
        Represents second player's token
    """
    no_players: str
    player1: str
    player2: str

    def __init__(self):
        """
        Construct a new Othello board which is an 8 by 8 list of lists
        containing empty spaces and default player positions used to
        play a game of Othello.
        """

        no_players = " "
        player1 = "1"
        player2 = "2"

        self.board = []

        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(no_players)

        self.board[3][3] = player1
        self.board[3][4] = player2
        self.board[4][4] = player1
        self.board[4][3] = player2

    @staticmethod
    def is_valid_coordinate(row: int, column: int) -> bool:
        """
        Return whether given coordinate is a valid location on the board
        """
        return not (row > 7 or column > 7 or row < 0 or column < 0)

    def get_player(self, row: int, column: int):
        """
        Return a player that is located at the given location.
        """
        if self.is_valid_coordinate(row, column):
            return self.board[row][column]
        return self.no_players

    def __str__(self) -> str:
        """
        Return a representation of board in a formatted string.
        """
        visual = "  "
        current_col = 0

        for i in range(8):
            visual += str(i) + " "
        visual += "\n" + "-" * 17

        for row in self.board:
            visual += "\n"
            visual += str(current_col) + "|"
            current_col += 1

            for column in row:
                visual += column
                visual += "|"

            visual += "\n" + "-" * 18

        return visual