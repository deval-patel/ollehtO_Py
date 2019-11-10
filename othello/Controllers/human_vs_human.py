from othello.Controllers import controller
from othello.player import player_human
from othello.OthelloGame import board


class HumanVsHuman(controller):

    def __init__(self):
        super()
        self.player_one = player_human(self.othello, board.player1)
        self.player_two = player_human(self.othello, board.player2)

    def main(self):
        othello_controller = HumanVsHuman()
        othello_controller.play()

    if __name__ == "__main__":
        main()
