from othello.Controllers.controller import Controller
from othello.player.player_human import PlayerHuman
from othello.player.player_easy import PlayerEasy
from othello.OthelloGame.board import Board


class UserVSEasy(Controller):
    """
    This class is responsible for instantiating the human and easy AI
    players and running the controller through the main class
    """

    def __init__(self):
        """
        Initialize a human player and an easy AI
        """

        super().__init__()
        self.player_one = PlayerHuman(self.othello, Board.player1)
        self.player_two = PlayerEasy(self.othello, Board.player2)


def main():
    """
    Run this controller
    """

    othello_controller = UserVSEasy()
    othello_controller.play()


if __name__ == "__main__":
    main()

