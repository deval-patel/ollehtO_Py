from tkinter import *
from othello.Application.Pictures.Pictures import Pictures


class Token(Button):
    """
    Todo: Explain
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
        return self._x

    def get_y(self):
        return self._y

    def set_image(self, img_name: str):
        self.config(image=self.pic.get_image(img_name))

    def update_parent(self):
        self.master.update_othello(self)
