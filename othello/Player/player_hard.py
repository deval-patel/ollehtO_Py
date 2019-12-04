import random

from othello.Player.player import Player
from othello.OthelloGame.othello import Othello
from othello.Player.player_moves import PlayerMoves


class PlayerHard(Player):
    """ An AI Player that plays at a hard difficulty.

    === Private Attributes ===
    _othello:
        An Othello game object from the Othello class.
    _character:
        An Othello Player.
    _chance:
        A number that represents the 1 in chance
    """
    _othello: Othello
    _character: chr
    _chance: int

    def __init__(self, othello: Othello, character: chr, chance: int) -> None:
        """ Creates PlayerHard.
        """
        Player.__init__(self, othello, character)
        self._chance = chance

    def get_move(self) -> tuple:
        """ Returns a random move but in a "1 in <chance>" return the best move.
        """
        if random.randint(1, self._chance) == self._chance:  # random move
            return PlayerMoves(self._othello, self._character).random_move
        else:                                               # best move
            return PlayerMoves(self._othello, self._character).best_move
