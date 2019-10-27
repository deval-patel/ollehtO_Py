from othello.OthelloGame.othello import Othello
from othello.player.player import Player
from othello.player.move import Move


class Controller:
    """
    The controller superclass will be the abstract
    class used to help implement all other controllers
    such as Human vs. Human, Human vs. Easy, etc

    === Public Attributes ===

    othello:
        The Othello class game manager
    player_one:
        The Player object that will be assigned as Player 1
    player_two:
        The Player object that will be assigned as Player 2
    """

    othello: Othello
    player_one: Player
    player_two: Player

    def __init__(self):
        """
        Initializes this game with a othello class game manager
        """

        self.othello = Othello()