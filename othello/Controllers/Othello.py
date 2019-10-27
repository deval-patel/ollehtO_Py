from __future__ import annotations
from othello.OthelloGame.board import Board


class Othello:
    """
    This Othello class is responsible for managing the game rules and
    deciding the winner of the game.

    === Private Attributes ===
    _whose_turn:
        The string value of the current player ("1" or "2")
        depending on whose turn it is.
    _board:
        The reference to the board object of this game.
    """

    _whose_turn = Board.player1
    _board = Board()

    def get_whose_turn(self) -> str:
        """
        Return the string value of the current player who has the turn
        """

        return self._whose_turn

    def get_board(self) -> Board:
        """
        the board object of this Othello game
        """

        return self._board

    def move(self, row: int, col: int) -> bool:
        """
        Attempt to make a move on the board on the coordinates row and
        col. Return true if move was successful and false otherwise. If
        the other player has a move after the current player makes a move,
        set _whose_turn to the other player. Else, the turn remains in
        control of the current player. Return false if the move was unsuccessful
        """

        if self._board.move(row, col, self.get_whose_turn()):
            if (self._board.has_move() == Board.both) or (self.board.has_move() == Board.both):
                self._whose_turn = Board.other_player(self.get_whose_turn())

            return True
        else:
            return False

    def get_count(self, player: str) -> int:
        """
        Return how many pieces player has on the board
        """

        return self._board.get_count(player)

    def is_game_over(self) -> bool:
        """
        Return if the game is over or no depending on whether
        one or more players can make a move on the board
        """
        if self._board.has_move == Board.no_players:
            return True
        else:
            return False

    def get_winner(self) -> str:
        """
        Return the string value of the player who won based on
        Othello game rules.
        """
        if not self.is_game_over():
            return Board.no_players

        player_one_count = self.get_count(Board.player1)
        player_two_count = self.get_count(Board.player2)

        if player_one_count > player_two_count:
            return Board.player1
        elif player_two_count > player_one_count:
            return Board.player2
        else:
            return Board.no_players
