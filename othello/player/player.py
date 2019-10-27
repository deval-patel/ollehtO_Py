from othello.OthelloGame.othello import Othello


class Player:
    """ A player that the user chooses its moves.

    === Private Attributes ===
    _othello:
        An Othello game object from the Othello class.
    _character:
        An Othello player.
    """
    _othello: Othello
    _character: chr

    def __init__(self, othello: Othello, character: chr) -> None:
        """ Creates Player.
        """
        self._othello = othello
        self._character = character

    def getMove(self):  # abstract function
        raise NotImplementedError
