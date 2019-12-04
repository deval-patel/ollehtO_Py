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
	"""
	Set the background colour for this GUI
	"""
	self.BACKGROUND = bg

    def set_text_colour(self, tc: str):
	"""
	Set the text colour for this GUI
	"""
        self.TEXT_COLOUR = tc

    def set_button_colour(self, bc: str):
	"""
	Set the button colour for this GUI
	"""
        self.BUTTON_COLOUR = bc

