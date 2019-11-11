class ColourScheme:
    """
    The colour scheme for this application
    """
    BACKGROUND: str
    TEXT_COLOUR: str
    BUTTON_COLOUR: str

    def __init__(self):
        self.BACKGROUND = "#558C3B"
        self.TEXT_COLOUR = "white"
        self.BUTTON_COLOUR = "#204037"

    def set_background(self, bg: str):
        self.BACKGROUND = bg

    def set_text_colour(self, tc: str):
        self.TEXT_COLOUR = tc

    def set_button_colour(self, bc: str):
        self.BUTTON_COLOUR = bc
