
import pygame

class SpriteSheet:
	def __init__(self, image, startx, starty, sx, sy, columns):
		self.image = image
		self.startx = startx
		self.starty = starty
		self.sx = sx
		self.sy = sy
		self.columns = columns

	
	def get_image(self, index):
		rect = pygame.Rect(self.startx + index % self.columns * self.sx,
							self.starty + int(index / self.columns) * self.sy,
							self.sx, self.sy)
		return self.image.subsurface(rect)

	def get_list(self, start, stop):
		lst = []
		for i in range(start, stop):
			lst.append(self.get_image(i))
		return lst

class Animation:
	def __init__(self, images, ticks):
		self.images = images
		self.ticks = ticks
		self.index = 0
		self.endtime = 0

		self.restart()

	def restart(self):
		self.index = 0
		self.endtime = pygame.time.get_ticks() + self.ticks

	def update(self):
		if (pygame.time.get_ticks() >= self.endtime):
			self.endtime = pygame.time.get_ticks() + self.ticks
			self.index += 1
			if self.index >= len(self.images): self.index = 0

	def get_image(self):
		return self.images[self.index]

