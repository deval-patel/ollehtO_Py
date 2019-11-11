from tkinter import *
from PIL import Image, ImageTk


class Pictures:
    def __init__(self):
        self.image_name = ["EMPTY", "X", "O"]
        self.images = {}
        # Construct images dictionary
        for i in self.image_name:
            img = Image.open("Pictures/"+ str(i + ".png"))
            resized = img.resize((45, 45), Image.ANTIALIAS)
            photo_img = ImageTk.PhotoImage(resized)
            self.images[i] = photo_img

    def get_image(self, img: str):
        return self.images[img]
