from tkinter import *
from othello.OthelloGame.othello import Othello
from othello.Application.Widgets.Token import Token
from othello.Application.ColourScheme import ColourScheme
# example = [["" for i in range(8)] for j in range(8)]
# for i in range(8):
#     for j in range(8):
#         if (i == 3 and j == 3) or (i == 4 and j == 4):
#             example[i][j] = "X"
#         elif (i == 3 and j == 4) or (i == 4 and j == 3):
#             example[i][j] = "O"
#         else:
#             example[i][j] = "EMPTY"


class ImageFrame(Frame):
    """
    TODO: Explain
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
        move = self._othello.move(event.get_x(), event.get_y())
        print(move)
        if move:
            self._board = self._othello.get_board()
            for child in self.children.values():
                print("loop executes")
                child_token = self.children[child]
                child_token.set_image(self._board.board[child_token.get_x()][child_token.get_y()])
