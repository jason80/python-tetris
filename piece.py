from engine.graphics import SpriteSheet
from engine.assets import asset_manager
from presets import *
import pygame
import copy
from random import randrange

class Piece():
	def __init__(self, board):
		self.board = board
		self.matrix = []
		self.sprites = SpriteSheet(asset_manager.get_image("tiles.png"), 0, 0, ssize, ssize, 7)
		self.x = 5
		self.y = 0

		self.stop_rotate_left = False
		self.stop_rotate_right = False

		self.pn = 0
		if pentha: self.pn = randrange(19)
		else: self.pn = randrange(7)

		if self.pn == 0:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 1, 1, 1, 0],
							[0, 0, 0, 0, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 1:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 0, 1, 1, 0],
							[0, 0, 1, 1, 0],
							[0, 0, 0, 0, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 2:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0] ]
		if self.pn == 3:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 1, 1, 0, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 4:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 1, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 5:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 1, 0, 0, 0],
							[0, 1, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 6:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 0, 0, 1, 0],
							[0, 0, 1, 1, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 7:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 0, 1, 1, 0],
							[0, 1, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 8:
			self.matrix = [ [0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0] ]
		if self.pn == 9:
			self.matrix = [ [0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 1, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 10:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 0, 0, 1, 0],
							[0, 0, 1, 1, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0] ]
		if self.pn == 11:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 0, 0, 1, 0],
							[0, 0, 1, 1, 0],
							[0, 0, 1, 1, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 12:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 1, 1, 1, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 13:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 1, 0, 1, 0],
							[0, 1, 1, 1, 0],
							[0, 0, 0, 0, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 14:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 1, 0, 0, 0],
							[0, 1, 0, 0, 0],
							[0, 1, 1, 1, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 15:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 1, 0, 0, 0],
							[0, 1, 1, 0, 0],
							[0, 0, 1, 1, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 16:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 1, 1, 1, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 0, 0, 0] ]
		if self.pn == 17:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 1, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0] ]
		if self.pn == 18:
			self.matrix = [ [0, 0, 0, 0, 0],
							[0, 1, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 1, 0],
							[0, 0, 0, 0, 0] ]

		r = randrange(4)

		while (r != 0):
			self.rotate_left()
			r -= 1
			
	def draw(self, screen):
		for j in range(5):
			for i in range(5):
				if (self.matrix[j][i]):
					xx = self.x * ssize + i * ssize - ssize * 3 + self.board.rect.x
					yy = self.y * ssize + j * ssize + self.board.rect.y
					screen.blit(self.sprites.get_image(self.pn % 7), (xx, yy))

	def rotate_left(self):
		tmp = copy.deepcopy(self.matrix)
		x = 0
		for j in range(5):
			y = 4
			for i in range(5):
				self.matrix[y][x] = tmp[j][i]
				y -= 1
			x += 1

	def rotate_right(self):
		tmp = copy.deepcopy(self.matrix)
		x = 4
		for j in range(5):
			y = 0
			for i in range(5):
				self.matrix[y][x] = tmp[j][i]
				y += 1
			x -= 1
