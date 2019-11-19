from tkinter import *
from othello.Application.ColourScheme import ColourScheme


class ButtonFrame(Frame):
    """
    Todo: Explain
    """
    colour: ColourScheme
    game_mode: Button
    settings: Button
    quit: Button
    space_holder_1: Label
    space_holder_2: Label

    def __init__(self, master, colour_scheme, **kw):
        super().__init__(master=master, **kw)
        self.colour = colour_scheme
        self.config(bd=10, bg=self.colour.BACKGROUND, width=520)
        # Button Frame
        self.game_button = Button(self, text="Game Modes", font=("Roboto", 20, "bold"), foreground=self.colour.TEXT_COLOUR,
                                  width=14, padx=0, bg=self.colour.BUTTON_COLOUR)
        self.game_button.grid(row=0, column=0)
        space_holder_1 = Label(self, width=15, bg=self.colour.BACKGROUND)
        space_holder_1.grid(row=0, column=1)
        self.settings = Button(self, text="Settings", font=("Roboto", 20, "bold"), foreground=self.colour.TEXT_COLOUR,
                               width=14, padx=0, bg=self.colour.BUTTON_COLOUR)
        self.settings.grid(row=0, column=2)
        space_holder_2 = Label(self, width=15, bg=self.colour.BACKGROUND)
        space_holder_2.grid(row=0, column=3)
        self.quit = Button(self, text="Exit", font=("Roboto", 20, "bold"), foreground=self.colour.TEXT_COLOUR,
                           width=14, padx=0, bg=self.colour.BUTTON_COLOUR)
        self.quit.grid(row=0, column=4)


