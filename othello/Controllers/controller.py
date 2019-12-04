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
            self.print_state()

            if whose_turn == Board.player1:
                move = self.player_one.get_move()
            if whose_turn == Board.player2:
                move = self.player_two.get_move()

            self.print_move(whose_turn, move)
            self.othello.move(move.get_row(), move.get_col())

        self.print_winner()

    def print_state(self):
        """
        Prints the current board state to the console
        """
        board_string = self.othello.get_board_string()
        player_one_count = self.othello.piece_count(Board.player1)
        player_two_count = self.othello.piece_count(Board.player2)
        current_player = self.othello.get_current_player()

        string_report = board_string, Board.player1, ":", str(player_one_count), \
                        " ", Board.player2, ":", str(player_two_count), \
                        " ", str(current_player), " moves next"
        print(string_report)

    @staticmethod
    def print_move(whose_turn: str, move: Move):
        """
        Print the Player who made a move and the move they
        made on the specific coordinates on the board to the
        console.
        """

        string_report = whose_turn + " makes move: " + str(move)
        print(string_report)

    def print_winner(self):
        """
        Print the final board state of the game and who won the game
        """

        string_report = self.othello.get_board_string(), Board.player1, ":", self.othello.piece_count(), " ", \
                        Board.player2, ":", self.othello.piece_count(Board.player2), " ", \
                        self.othello.check_winner(), " won"
        print(string_report)
