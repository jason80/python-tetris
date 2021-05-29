
import pygame
from presets import *

class Display:
	def __init__(self):
		self.reset()
		self.font = pygame.font.SysFont(None, display_font_size)
		self.score_font = pygame.font.SysFont(None, score_font_size)

	def reset(self):
		self.score = 0
		self.lines = 0
		self.level = start_level
		self.level_lines = 0

	def add_lines(self, lines):
		self.level_lines += lines
		self.lines += lines
		if (self.level_lines >= 30):
			# Level up
			self.level += 1
			#pygame.time.set_timer(pygame.USEREVENT, level_base_interval - self.level * 100)
			self.level_lines -= 30

	def add_score(self, lines):
		points = 0
		if lines == 1:
			points = 40
		elif lines == 2:
			points = 100
		elif lines == 3:
			points = 300
		elif lines == 4:
			points = 1200
		else:
			points = 3600

		self.score += points * (self.level + 1)


	def draw(self, screen):
		screen.blit(self.score_font.render("Score: " + str(self.score), True, (255, 255, 255)),
				(display_x, display_y))
		screen.blit(self.font.render("Level: " + str(self.level), True, (255, 255, 255)),
				(display_x, display_y + 40))
		screen.blit(self.font.render("Lines: " + str(self.lines), True, (255, 255, 255)),
				(display_x, display_y + 80))

	