from othello.Player.player import Player
from othello.OthelloGame.othello import Othello
from othello.Player.player_moves import PlayerMoves


class PlayerEasy(Player):
    """ An AI Player that plays at an easy difficulty.

    === Private Attributes ===
    _othello:
        An Othello game object from the Othello class.
    _character:
        An Othello Player.
    """
    _othello: Othello
    _character: chr

    def __init__(self, othello: Othello, character: chr) -> None:
        """ Creates PlayerEasy.
        """
        Player.__init__(self, othello, character)

    def get_move(self) -> tuple:
        """ Returns the worst move.
        """
        return PlayerMoves(self._othello, self._character).random_move
