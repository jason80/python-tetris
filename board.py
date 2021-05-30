import pygame
from presets import *
from piece import Piece
from collide import *
from display import Display
from next_display import NextDisplay
from menu import MainMenu, PausedMenu
from engine.assets import asset_manager
from engine.stage import Stage
from engine.graphics import SpriteSheet
import random


class Board(Stage):
	def __init__(self, game) -> None:
		super().__init__(game, "board")
		self.rect = pygame.Rect(board_x, board_y, board_width, board_height)

		self.sprites = SpriteSheet(asset_manager.get_image("tiles.png"), 0, 0, ssize, ssize, 7)
		self.display = Display()
		self.next_display = NextDisplay(self)

		self.matrix = []
		self.piece = None
		self.next_piece = None

		self.g_over = False

		self.stage = 0

		self.reset()

		self.stop_rotate_left = False
		self.stop_rotate_right = False
		self.stop_falling = False

		self.move_left_time = 0
		self.move_right_time = 0

		self.fall_time = 0

	def reset(self):
		self.matrix = []

		for j in range(22):
			self.matrix.append([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1])

		self.matrix.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
		self.matrix.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
		self.matrix.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

		self.set_stage()

		self.piece = Piece(self)
		self.next_piece = Piece(self)

	def draw(self, screen: pygame.Surface) -> None:

		# Draw border
		pygame.draw.rect(screen, border_color, self.rect, border_width)

		# Draw board
		for j in range(22):
			for i in range(3, 13):
				if self.matrix[j][i]:
					xx = self.rect.x + (i - 3) * ssize
					yy = self.rect.y + j * ssize
					screen.blit(self.sprites.get_image(self.display.level % 7), (xx, yy))

		# Draw piece
		self.piece.draw(screen)

		# Draw display
		self.display.draw(screen)

		# Draw next display
		self.next_display.draw(screen)

	def update(self, delta) -> None:
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			if self.move_left_time < pygame.time.get_ticks():
				self.move_piece_left()
				self.move_left_time = pygame.time.get_ticks() + piece_move_interval
		else:
			self.move_left_time = 0

		if key[pygame.K_RIGHT]:
			if self.move_right_time < pygame.time.get_ticks():
				self.move_piece_right()
				self.move_right_time = pygame.time.get_ticks() + piece_move_interval
		else:
			self.move_right_time = 0

		if key[pygame.K_DOWN]:
			if not self.stop_falling: self.move_piece_down()
		else:
			self.stop_falling = False

		# Piece falling
		if pygame.time.get_ticks() >= self.fall_time:
			self.move_piece_down()
			self.fall_time = pygame.time.get_ticks() + level_base_interval - self.display.level * 100

	def key_down(self, key):
		if key == pygame.K_SPACE:
			self.rotate_piece_left()

		if key == pygame.K_UP:
			self.rotate_piece_right()

		if key == pygame.K_RETURN:
			# Pause tetris
			self.enabled = False
			self.game.add_stage(PausedMenu(self.game))

	def move_piece_right(self):
		self.piece.x += 1
		if collision_detected(self, self.piece): self.piece.x -= 1

	def move_piece_left(self):
		self.piece.x -= 1
		if collision_detected(self, self.piece): self.piece.x += 1

	def move_piece_down(self):
		self.piece.y += 1
		if collision_detected(self, self.piece): 
			self.piece.y -= 1
			self.piece_on_botton()

	def rotate_piece_left(self):
		self.piece.rotate_left()
		if collision_detected(self, self.piece): self.piece.rotate_right()

	def rotate_piece_right(self):
		self.piece.rotate_right()
		if collision_detected(self, self.piece): self.piece.rotate_left()

	def piece_on_botton(self):
		add_to_board(self, self.piece)
		self.stop_falling = True

		# Generates a new piece
		self.piece = self.next_piece
		self.next_piece = Piece(self)

		# Game over
		if collision_detected(self, self.piece):
			self.game_over()
		
		# Check lines
		lines = self.check_lines()
		if (lines):
			self.clear_lines(lines)
			self.display.add_lines(len(lines))
			self.display.add_score(len(lines))

	def check_lines(self):

		lines = []

		for l in range(22):
			if (self.is_line_fill(l)):
				lines.append(l)

		return lines


	def is_line_fill(self, y):
		for i in range(3, 13):
			if self.matrix[y][i] == 0: return False
		return True

	def clear_lines(self, lines):
		for l in lines:
			self.matrix.pop(l)
			self.matrix.insert(0, [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1])

	def set_stage(self):
		y = 21
		for i in range(self.stage):
			dots = random.randint(4, 8)
			line = [1] * dots
			line += [0] * (10 - dots)
			random.shuffle(line)
			line = [1, 1, 1] + line + [1, 1, 1]
			self.matrix[y] = line
			y -= 1

	def game_over(self):
		self.enabled = False
		self.g_over = True
		self.game.add_stage(MainMenu(self.game))
