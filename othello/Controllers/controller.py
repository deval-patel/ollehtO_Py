from othello.OthelloGame.othello import Othello
from othello.player.player import Player


class Controller:
    othello: Othello
    player_one: Player
    player_two: Player

    def __init__(self):
        self.othello = Othello()
