from tkinter import *
from othello.OthelloGame.othello import Othello
from othello.Application.Widgets.Token import Token
from othello.Application.ColourScheme import ColourScheme


class ImageFrame(Frame):
    """
    This class contains the board of the game. It handles how to make moves when the buttons on the grid are clicked.
    When the buttons are clicked, the corresponding move is made in the Othello game.
    """
    colour: ColourScheme
    _othello: Othello  # The game to give and receive information from

    def __init__(self, master, colour_scheme: ColourScheme, othello: Othello, **kw):
        super().__init__(master=master, **kw)
        self.colour = colour_scheme
        self.config(bd=10, bg=self.colour.BACKGROUND)
        self._othello = othello
        self._board = self._othello.get_board()
        # Creating a 8 by 8 Image Buttons
        for row in range(8):
            for col in range(8):
                temp = Token(x=row, y=col, master=self, pic=self._board.board[row][col], bd=0)
                temp.grid(row=row, column=col)

    def update_othello(self, event: Token):
	"""
	This is the event-handler for all of the Tokens on the board. When any Token is clicked, this method 
	is called. This method will make a move at the location of the Token using its x and y co-ordinates.
	It only makes a move if there is a valid move at the Token's location.
	"""
        move = self._othello.move(event.get_x(), event.get_y())
        print(move)
        if move:
            self._board = self._othello.get_board()
            print(self._board)
            for child in self.children.values():
                child.set_image(self._board.board[child.get_x()][child.get_y()])
                temp.grid(row=row, column=col)

