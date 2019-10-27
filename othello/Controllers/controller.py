from othello.OthelloGame.othello import Othello
from othello.player.player import Player
from othello.player.move import Move
from othello.OthelloGame.board import Board


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

    def play(self):
        """
        If the game is not over, print the current board state
        and keep getting moves from whoever's turn it is,
        reporting the moves made to the console. When the game
        is over, report who the winner is

        """
        while not self.othello.check_game_over():
            whose_turn = self.othello.get_current_player()
            self.report()

            if whose_turn == Board.player1:
                move = self.player_one.getMove()
            if whose_turn == Board.player2:
                move = self.player_two.getMove()

            self.report_move(whose_turn, move)
            self.othello.move(move.getRow(), move.getCol())

        self.report_final()

    def report(self):
        """
        Prints the current board state to the console
        """

        raise NotImplementedError

    def report_move(self, whose_turn: str, move: Move):
        """
        Print the player who made a move and the move they
        made on the specific coordinates on the board to the
        console.
        """

        raise NotImplementedError

    def report_final(self):
        """
        Print the final board state of the game and who won the game
        """

        raise NotImplementedError
