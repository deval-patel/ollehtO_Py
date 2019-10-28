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
    board:
        Represents board that consists of lists of lists
    """
    no_players: str
    player1: str
    player2: str
    board: list

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

    def opposing_player(self, player) -> str:
        """
        Return the opposing player of the given <player> or <no_players>
        if none exist at the given location.
        """
        if player == self.player1:
            return self.player2
        elif player == self.player2:
            return self.player1
        else:
            return self.no_players

    def player_variation(self, row: int, column: int, row_move: int, column_move: int) -> str:
        """
        Return a string representation of player that has a variation of
        current player followed by an opposing player starting at <row> and
        <column> coordinates in a direction of <row_move> and <column_move>.
        If no variation is found then return <no_players>.
        """

        # Prevent infinite loops
        if row_move == 0 and column_move == 0:
            return self.no_players

        first_player = self.get_player(row, column)

        while self.is_valid_coordinate(row, column):
            current_player = self.get_player(row, column)

            if current_player == self.no_players:
                return self.no_players

            elif current_player != first_player:
                return current_player

            row += row_move
            column += column_move

    def flip_tokens(self, player: str, row: int, column: int, row_move: int, column_move: int) -> int:
        """
        Flip all of the tokens from starting position <row> and <column> into
        the direction <row_move> and <column_move> by the <player>.
        """
        row += row_move
        column += column_move
        current_player = self.get_player(row, column)

        if (current_player == self.no_players) or \
                (current_player == player) or \
                (row_move == 0 and column_move == 0) or \
                not (self.is_valid_coordinate(row, column)):
            return 0

        elif self.player_variation(row, column, row_move, column_move) == player:
            tokens_flipped = 0

            while current_player == self.opposing_player(player):
                row += row_move
                column += column_move
                tokens_flipped += 1
                current_player = self.get_player(row, column)
            return tokens_flipped

        else:
            return 0

    def __str__(self) -> str:
        """
        Return a representation of board in a formatted string.
        """
        visual = "  "
        current_col = 0

        for i in range(8):
            visual += str(i) + " "
        visual += "\n" + "-" * 18

        for row in self.board:
            visual += "\n"
            visual += str(current_col) + "|"
            current_col += 1

            for column in row:
                visual += column
                visual += "|"

            visual += "\n" + "-" * 18

        return visual
