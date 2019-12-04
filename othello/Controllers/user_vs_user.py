from othello.Controllers.controller import Controller
from othello.player.player_human import PlayerHuman
from othello.OthelloGame.board import Board


class UserVSUser(Controller):
    """
    This class is responsible for instantiating two human players
    players and running the controller through the main class
    """

    def __init__(self):
        """
        Initialize a human player and a medium AI
        """

        super().__init__()
        self.player_one = PlayerHuman(self.othello, Board.player1)
        self.player_two = PlayerHuman(self.othello, Board.player2)


def main():
    """
    Run this controller
    """

    othello_controller = UserVSUser()
    othello_controller.play()


if __name__ == "__main__":
    main()

