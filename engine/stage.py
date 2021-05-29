
from abc import ABC, abstractmethod
import pygame

class Stage(ABC):
    def __init__(self, game, name:str) -> None:
        self.game = game
        self.name = name

        self.enabled = True
        self.visible = True
        self.disposed = False

    @abstractmethod
    def update(self, delta) -> None:
        pass

    @abstractmethod
    def draw(self, screen:pygame.Surface) -> None:
        pass

    def kill(self):
        self.disposed = True

    def key_down(self, key):
        pass

    def key_up(self, key):
        pass
