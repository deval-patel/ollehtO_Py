from othello.player.player import Player
from othello.Controllers.othello import Othello
from othello.player.move import Move


class PlayerHuman(Player):
    """ A player where the user chooses its moves.

    === Private Attributes ===
    _othello:
        An Othello game object from the Othello class.
    _character:
        An Othello player.
    """
    _othello: Othello
    _character: chr

    def __init__(self, othello: Othello, character: chr) -> None:
        """ Creates PlayerHuman.
        """
        self._othello = othello
        self._character = character

    def getMove(self) -> tuple:
        """ Return the move that Player wants to make.
        """
        row = self.__getMove("row: ")
        col = self.__getMove("col: ")
        return Move(row, col)

    def __getMove(self, message: str) -> int:
        """ Return the row or col that the user inputs.
        """
        upper = self._othello.DIMENSION - 1
        lower = 0
        while True:
            try:
                num = input(message)
                if lower <= num <= upper:
                    return num
                else:
                    print("Invalid number, please enter 1-8")
            except IOError:
                print("Invalid number, please enter 1-8")
            except TypeError:
                print("Invalid number, please enter 1-8")
