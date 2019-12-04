from __future__ import annotations
from othello.OthelloGame.board import Board


class Othello:
    """
    This Othello class is responsible for managing the game rules and
    deciding the winner of the game.

    === Private Attributes ===
    _whose_turn:
        The string value of the current Player ("1" or "2")
        depending on whose turn it is.
    _board:
        The reference to the board object of this game.
    """

    _board = Board()
    _current_player = _board.player1

    def get_current_player(self) -> str:
        """
        Return the string value of the current Player who has the turn
        """

        return self._current_player

    def get_board(self) -> Board:
        """
        the board object of this Othello game
        """

        return self._board

    def move(self, row: int, col: int) -> bool:
        """
        Attempt to make a move on the board on the coordinates row and
        col. Return true if move was successful and false otherwise. If
        the other Player has a move after the current Player makes a move,
        set _whose_turn to the other Player. Else, the turn remains in
        control of the current Player. Return false if the move was unsuccessful
        """
        if self._board.move(row=row, column=col, player=self.get_current_player()):
            if self._board.has_move() == self._board.both_players:
                self._current_player = self._board.opposing_player(self.get_current_player())
            return True
        else:
            return False

    def piece_count(self, player: str) -> int:
        """
        Return how many pieces Player has on the board
        """

        return self._board.piece_count(player)

    def check_game_over(self) -> bool:
        """
        Return if the game is over or not depending on whether
        one or more players can make a move on the board
        """
        if self._board.has_move == Board.no_players:
            return True
        else:
            return False

    def check_winner(self) -> str:
        """
        Return the string value of the Player who won based on
        Othello game rules.
        """
        if not self.check_game_over():
            return Board.no_players

        player_one_count = self.piece_count(Board.player1)
        player_two_count = self.piece_count(Board.player2)

        if player_one_count > player_two_count:
            return Board.player1
        elif player_two_count > player_one_count:
            return Board.player2
        else:
            return Board.no_players

    def get_board_string(self):
        """
        Return the string representation of the current game state and
        board state
        """

        return self._board.__str__

