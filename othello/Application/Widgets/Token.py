from tkinter import *
from othello.Application.Pictures.Pictures import Pictures


class Token(Button):
    """
    This is the button which can be clicked to make a move for the game Othello. 
    The x and y coordinates of this class determines which cell on the OthelloBoard this Token should relate to. 
    The image of this Token determines on the value of the cell on OthelloBoard which corresponds to this Token's location.
    """
    _x: int
    _y: int
    pic: Pictures

    def __init__(self, x: int, y: int, pic: str, **kw):
        super().__init__(**kw)
        self._x = x
        self._y = y
        self.config(command=self.update_parent)
        self.pic = Pictures()
        self.image = self.pic.get_image("EMPTY")
        self.set_image(pic)

    def get_x(self):
	"""
	Returns the x coordinate of this Token.
	"""
        return self._x

    def get_y(self):
        """
	Returns the y coordinate of this Token.
	"""
        return self._y

    def set_image(self, img_name: str):
        """
	Sets the image of this Token depending on the value of the cell on OthelloBoard.
	"""
        img = self.pic.get_image(img_name)
        self.config(image=img)
        self.image = img

    def update_parent(self):
        """
	Notifies the ImageFrame to make a move because this Token has been clicked.
	"""
        self.master.update_othello(self)

    def __str__(self):
	"""
	String representation of this Token
	"""
        return "x: " + str(self._x) + ", y: "  +str(self._y)
