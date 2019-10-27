from othello.player.player import Player
from othello.Controllers.othello import Othello
from othello.player.player_moves import PlayerMoves


class PlayerEasy(Player):
    """ An AI player that plays at an easy difficulty.

    === Private Attributes ===
    _othello:
        An Othello game object from the Othello class.
    _character:
        An Othello player.
    """
    _othello: Othello
    _character: chr

    def __init__(self, othello: Othello, character: chr) -> None:
        """ Creates PlayerEasy.
        """
        self._othello = othello
        self._character = character

    def getMove(self) -> tuple:
        """ Returns the worst move.
        """
        return PlayerMoves(self._othello, self._character).random_move
