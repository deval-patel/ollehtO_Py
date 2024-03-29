from tkinter import *
from othello.Application.ColourScheme import ColourScheme
from othello.Application.Widgets.ImageFrame import ImageFrame
from othello.Application.Widgets.ButtonFrame import ButtonFrame
from othello.OthelloGame.othello import Othello


class Application:
    """
    This class contains the main Application for ollehtO.
    It is responsible for creating the new components and main widgets required to make the GUI visualize.
    Run this file to start the game.
    """
    frame: Frame
    header: Label
    images: ImageFrame
    buttons: ButtonFrame
    message: StringVar
    message_label: Message
    colour: ColourScheme
    othello: Othello


    def __init__(self, master):
        self.othello = Othello()
        self.colour = ColourScheme()
        self.root = master
        self.root.config(bg=self.colour.BACKGROUND)
        self.header = Label(self.root, text="ollehtO", font=("Times", "30", "bold"), bg=self.colour.BACKGROUND,
                            foreground=self.colour.TEXT_COLOUR)
        self.header.grid(row=0, column=0)
        self.images = ImageFrame(master=self.root, colour_scheme=self.colour, othello=self.othello)
        self.images.grid(row=1, column=0)
        self.message = StringVar()
        self.message_label = Message(self.root, textvariable=self.message, font=("Roboto", 20),
                                     bg=self.colour.BACKGROUND, width=600,
                                     justify=CENTER, foreground=self.colour.TEXT_COLOUR)
        self.message.set("This is where the message will be displayed")
        self.message_label.grid(row=2, column=0)
        self.buttons = ButtonFrame(self.root, self.colour)
        self.buttons.grid(row=3, column=0)


    def set_message(self, msg: str):
	"""
	Sets the on screen message
	"""
        self.message.set(msg)


if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    print("made app")
    root.mainloop()

    root = Tk()
    app = Application(root)
    root.mainloop()

