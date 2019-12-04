from othello.Controllers.controller import Controller
from othello.player.player_human import PlayerHuman
from othello.player.player_hard import PlayerHard
from othello.OthelloGame.board import Board


class UserVSHard(Controller):

    def __init__(self):
        super().__init__()
        self.player_one = PlayerHuman(self.othello, Board.player1)
        self.player_two = PlayerHard(self.othello, Board.player2)


def main():
    othello_controller = UserVSHard()
    othello_controller.play()


if __name__ == "__main__":
    main()

