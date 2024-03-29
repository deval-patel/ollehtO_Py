from __future__ import annotations


class Board:
    """
    Board class is responsible for keeping track of the board and everything
    that happens on it as well as handling board related tasks such as
    Player requesting a move.

        === Public Attributes ===
    both_players:
        String declaring that both players can make a move.
    no_players:
        Empty space declaring that there are no players located in
        current position.
    player1:
        Represents first Player's token
    player2:
        Represents second Player's token
    board:
        Represents board that consists of lists of lists
    """

    both_players: str = "both"
    no_players: str = "EMPTY"
    player1: str = "X"
    player2: str = "O"

    def __init__(self):
        """
        Construct a new Othello board which is an 8 by 8 list of lists
        containing empty spaces and default Player positions used to
        play a game of Othello.
        """

        self.board = []

        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(Board.no_players)
        self.board[3][3] = Board.player1
        self.board[3][4] = Board.player2
        self.board[4][4] = Board.player1
        self.board[4][3] = Board.player2

    @staticmethod
    def is_valid_coordinate(row: int, column: int) -> bool:
        """
        Return whether given coordinate is a valid location on the board
        """
        return not (row > 7 or column > 7 or row < 0 or column < 0)

    def get_player(self, row: int, column: int):
        """
        Return a Player that is located at the given location.
        """
        if self.is_valid_coordinate(row, column):
            return self.board[row][column]
        return Board.no_players

    def opposing_player(self, player: str) -> str:
        """
        Return the opposing Player of the given <Player> or <no_players>
        if none exist at the given location.
        """
        if player == Board.player1:
            return Board.player2
        elif player == Board.player2:
            return Board.player1
        else:
            return Board.no_players

    def get_token_count(self, player):
        """
        Return the number of tokens Player has on the board.
        """
        tokens = 0

        for row in range(8):
            for column in range(8):
                if self.board[row][column] == player:
                    tokens += 1
        return tokens

    def player_variation(self, row: int, column: int, row_move: int, column_move: int) -> str:
        """
        Return a string representation of Player that has a variation of
        current Player followed by an opposing Player starting at <row> and
        <column> coordinates in a direction of <row_move> and <column_move>.
        If no variation is found then return <no_players>.
        """

        # Prevent infinite loops
        if row_move == 0 and column_move == 0:
            return Board.no_players

        first_player = self.get_player(row, column)

        while self.is_valid_coordinate(row, column):
            current_player = self.get_player(row, column)

            if current_player == Board.no_players:
                return Board.no_players

            elif current_player != first_player:
                return current_player

            row += row_move
            column += column_move

    def flip_tokens(self, player: str, row: int, column: int, row_move: int, column_move: int) -> int:
        """
        Flip all of the tokens from starting position <row> and <column> into
        the direction <row_move> and <column_move> by the <Player>.
        """
        row += row_move
        column += column_move
        current_player = self.get_player(row, column)

        if (current_player == Board.no_players) or \
                (current_player == player) or \
                (row_move == 0 and column_move == 0) or \
                not (self.is_valid_coordinate(row, column)):
            return 0

        elif self.player_variation(row, column, row_move, column_move) == player:
            tokens_flipped = 0

            while current_player == self.opposing_player(player):
                self.board[row][column] = player
                row += row_move
                column += column_move
                tokens_flipped += 1
                current_player = self.get_player(row, column)
            return tokens_flipped

        else:
            return 0

    def _possible_move(self, row: int, column: int, row_move: int, column_move: int):
        """
        Helper function determining which Player could move into a
        given direction.
        """
        if not self.is_valid_coordinate(row, column):
            return Board.no_players
        elif self.get_player(row, column) == Board.no_players:
            return self.player_variation(row + row_move, column + column_move, row_move, column_move)
        else:
            return Board.no_players

    def has_move(self) -> str:
        """
        Return which Player has a possible move, or <both_players> if both
        players have a valid move or <no_players> if neither do.
        """

        player1_move = False
        player2_move = False
        for row in range(8):
            for column in range(8):
                for row_move in (-1, 0, 1):
                    for column_move in (-1, 0, 1):

                        token_moved = self._possible_move(row, column, row_move, column_move)
                        if token_moved == Board.player1:
                            player1_move = True
                        if token_moved == Board.player2:
                            player2_move = True
                        if player1_move and player2_move:
                            return self.both_players

        if player1_move and player2_move:
            return self.both_players
        elif player1_move:
            return Board.player1
        elif player2_move:
            return Board.player2
        else:
            return Board.no_players

    def move(self, player: str, row: int, column: int) -> bool:
        """
        This function is responsible for making <Player> move at a
        given location. Returns whether Player has moved, and modifies
        the board if so.
        """
        if not self.is_valid_coordinate(row, column) or not self.board[row][column] == Board.no_players:
            return False

        moved = False

        for row_move in (-1, 0, 1):
            for column_move in (-1, 0, 1):
                token_moved = self._possible_move(row, column, row_move, column_move)
                if token_moved == self.both_players or token_moved == player:
                    if self.flip_tokens(player, row, column, row_move, column_move) >= 1:
                        moved = True

        if moved:
            self.board[row][column] = player

        return moved

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
