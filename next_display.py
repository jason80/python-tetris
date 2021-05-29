from presets import *
from engine.graphics import SpriteSheet
from engine.assets import asset_manager
import pygame

class NextDisplay:
	def __init__(self, board):
		self.board = board
		self.rect = pygame.Rect(next_display_x, next_display_y, next_display_size, next_display_size)
		self.sprites = SpriteSheet(asset_manager.get_image("tiles.png"),
						0, 0, ssize, ssize, 7)

	def draw(self, screen):
		pygame.draw.rect(screen, border_color, self.rect, border_width)
		self.draw_piece(screen)

	def draw_piece(self, screen):
		for j in range(5):
			for i in range(5):
				if (self.board.next_piece.matrix[j][i]):
					xx = self.rect.x + i * ssize
					yy = self.rect.y + j * ssize
					screen.blit(self.sprites.get_image(self.board.next_piece.pn % 7), (xx, yy))