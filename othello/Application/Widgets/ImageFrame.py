from tkinter import *
from othello.OthelloGame.othello import Othello
from PIL import Image, ImageTk

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
                # Opens image
                im = Image.open("Pictures/" + str(self._board.board[row][col]) + ".png")
                resized = im.resize((45, 45), Image.ANTIALIAS)
                # Creates Image
                temp_img = ImageTk.PhotoImage(resized)
                temp = Token(x=row, y=col, master=self, image=temp_img, bd=0)
                temp.image = temp_img
                temp.grid(row=row, column=col)
