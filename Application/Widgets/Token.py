pip from tkinter import *


class Token(Button):
    """
    Todo: Explain
    """
    _x: int
    _y: int

    def __init__(self, x: int, y: int, **kw):
        super().__init__(**kw)
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
