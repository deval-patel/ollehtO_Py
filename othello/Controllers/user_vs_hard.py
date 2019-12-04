from othello.Controllers.controller import Controller
from othello.player.player_human import PlayerHuman
from othello.player.player_hard import PlayerHard
from othello.OthelloGame.board import Board


class UserVSHard(Controller):
    """
    This class is responsible for instantiating the human and hard AI
    players and running the controller through the main class
    """

    def __init__(self):
        """
        Initialize a human player and a hard AI
        """

        super().__init__()
        self.player_one = PlayerHuman(self.othello, Board.player1)
        self.player_two = PlayerHard(self.othello, Board.player2)


def main():
    """
    Run this controller
    """

    othello_controller = UserVSHard()
    othello_controller.play()


if __name__ == "__main__":
    main()

