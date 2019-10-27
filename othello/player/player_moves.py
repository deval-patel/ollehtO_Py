import copy
import random

from othello.OthelloGame.othello import Othello
from othello.player.move import Move


class PlayerMoves:
    """ A class containing all types of moves that a non-human player can make.

    === Private Attributes ===
    _othello:
        An Othello game object from the Othello class.
    _character:
        An Othello player.
    """
    _othello: Othello
    _character: chr

    def __init__(self, othello: Othello, character: chr) -> None:
        """ Creates PlayerMoves.
        """
        self._othello = othello
        self._character = character

    def random_move(self) -> tuple:
        """ Returns a valid random move.
        """
        moves = []
        for row in range(0, self._othello.DIMENSION):
            for col in range(0, self._othello.DIMENSION):
                new_othello = copy.deepcopy(self._othello)
                if new_othello.move(row, col):
                    moves.append(tuple(row, col))
        return_move = random.choice(moves)
        return Move(return_move[0], return_move[1])

    def best_move(self) -> tuple:
        """ Returns the move that flips over the most tokens.
        """
        new_othello = copy.deepcopy(self._othello)
        best_move = None
        best_move_total = new_othello.getCount(self._character)
        for row in range(0, self._othello.DIMENSION):
            for col in range(0, self._othello.DIMENSION):
                new_othello = copy.deepcopy(self._othello)
                if new_othello.move(row, col) \
                        and new_othello.getCount() > best_move_total:
                    best_move = (row, col)
                    best_move_total = new_othello.getCount(self._character)
        return Move(best_move[0], best_move[1])

    def worst_move(self) -> tuple:
        """ Returns the move that flips over the least tokens.
        """
        new_othello = copy.deepcopy(self._othello)
        worst_move = None
        worst_move_total = new_othello.getCount(self._character)
        for row in range(0, self._othello.DIMENSION):
            for col in range(0, self._othello.DIMENSION):
                new_othello = copy.deepcopy(self._othello)
                if new_othello.move(row, col) \
                        and new_othello.getCount() < worst_move_total:
                    worst_move = (row, col)
                    worst_move_total = new_othello.getCount(self._character)
        return Move(worst_move[0], worst_move[1])
