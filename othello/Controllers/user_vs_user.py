from othello.Controllers.controller import Controller
from othello.Player.player_human import PlayerHuman
from othello.OthelloGame.board import Board


class UserVSUser(Controller):

    def __init__(self):
        super().__init__()
        self.player_one = PlayerHuman(self.othello, Board.player1)
        self.player_two = PlayerHuman(self.othello, Board.player2)


def main():
    othello_controller = UserVSUser()
    othello_controller.play()


if __name__ == "__main__":
    main()

