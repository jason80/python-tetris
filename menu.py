
from abc import abstractmethod
#from typing import Text
import pygame
from presets import *
from engine.stage import Stage
from engine.assets import asset_manager

class MenuItem:
    def __init__(self, menu, text, x, y):
        self.menu = menu
        self.text = text
        self.selected = False
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.menu.font.render(self.text, True, menu_color), (self.x, self.y))
        if (self.selected):
            screen.blit(self.menu.font.render(">", True, menu_color), (self.x - 15, self.y))

class Menu(Stage):
    def __init__(self, game, name):
        super().__init__(game, name)
        self.items = []
        self.index = 0
        self.font = pygame.font.SysFont(None, menu_font_size)
        self.freeze = True

    def reset(self):
        self.index = 0

    def update_items(self):
        for i in range(len(self.items)):
            if (i == self.index):
                self.items[i].selected = True
            else: self.items[i].selected = False

    def key_down(self, key):

        if key == pygame.K_DOWN:
            self.index += 1
            if self.index >= len(self.items): self.index = 0

        if key == pygame.K_UP:
            self.index -= 1
            if (self.index < 0): self.index = len(self.items) - 1

        self.update_items()

        if self.freeze: return None

        if key == pygame.K_RETURN:
            self.item_action(self.items[self.index])

    def key_up(self, key):
        self.freeze = False

    def update(self, delta) -> None:
        pass

    def draw(self, screen):
        for i in self.items: i.draw(screen)

    @abstractmethod
    def item_action(self, item):
        pass

class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game, "main")
        self.items = [
            MenuItem(self, "Start game", menu_x, menu_y),
            MenuItem(self, "Level " + str(game.board.display.level), menu_x, menu_y + 25),
            MenuItem(self, "Stage " + str(game.board.stage), menu_x, menu_y + 50),
            MenuItem(self, "Quit", menu_x, menu_y + 75)
        ]

        self.update_items()

    def item_action(self, item):
        if item.text == "Start game":
            self.game.board.enabled = True
            self.game.board.reset()
            self.kill()

        if item.text.startswith("Level"):
            self.game.board.display.level += 1
            if self.game.board.display.level > 9:
                self.game.board.display.level = 0

            item.text = "Level " + str(self.game.board.display.level)

        if item.text.startswith("Stage"):
            self.game.board.stage += 3
            if self.game.board.stage > 12:
                self.game.board.stage = 0

            item.text = "Stage " + str(self.game.board.stage)

        if item.text == "Quit":
            self.game.running = False

class PausedMenu(Menu):
    def __init__(self, game):
        super().__init__(game, "pause")
        self.items = [
            MenuItem(self, "Continue", menu_x, menu_y),
            MenuItem(self, "End game", menu_x, menu_y + 25)
        ]

        self.image = asset_manager.get_image("paused.png")

    def item_action(self, item):
        if item.text == "Continue":
            self.game.board.enabled = True
        if item.text == "End game":
            self.game.add_stage(MainMenu(self.game))

        self.kill()

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.image, (board_x + 40, board_y + 100))


