from othello.player.player import Player
from othello.OthelloGame.othello import Othello
from othello.player.player_moves import PlayerMoves


class PlayerMedium(Player):
    """ An AI player that plays at a medium difficulty.

    === Private Attributes ===
    _othello:
        An Othello game object from the Othello class.
    _character:
        An Othello player.
    """
    _othello: Othello
    _character: chr

    def __init__(self, othello: Othello, character: chr) -> None:
        """ Creates PlayerMedium.
        """
        Player.__init__(self, othello, character)

    def getMove(self) -> tuple:
        """ Returns a random move.
        """
        return PlayerMoves(self._othello, self._character).random_move
