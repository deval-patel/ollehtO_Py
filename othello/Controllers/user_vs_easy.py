from othello.Controllers.controller import Controller
from othello.player.player_human import PlayerHuman
from othello.player.player_easy import PlayerEasy
from othello.OthelloGame.board import Board


class UserVSEasy(Controller):

    def __init__(self):
        super().__init__()
        self.player_one = PlayerHuman(self.othello, Board.player1)
        self.player_two = PlayerEasy(self.othello, Board.player2)


def main():
    othello_controller = UserVSEasy()
    othello_controller.play()


if __name__ == "__main__":
    main()

