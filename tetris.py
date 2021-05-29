from menu import MainMenu
from board import Board
from engine.game import Game
from presets import *

class Tetris(Game):
    def __init__(self) -> None:
        super().__init__("Tetris", screen_width, screen_height)
        self.fps = fps
        self.board = Board(self)
        self.board.enabled = False

    def init(self) -> None:
        self.add_stage(self.board)
        self.add_stage(MainMenu(self))

if __name__ == "__main__":
    tetris = Tetris()
    tetris.run()