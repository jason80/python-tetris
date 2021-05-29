import pygame
from abc import ABC, abstractmethod

from engine.stage import Stage

class Game(ABC):
	def __init__(self, caption:str, sw:int, sh:int) -> None:
		pygame.init()

		self.screen_width = sw
		self.screen_height = sh
		self.screen = pygame.display.set_mode((sw, sh))
		pygame.display.set_caption(caption)
		self.running = False
		self.fps = 120

		self.stages = []

	@abstractmethod
	def init(self) -> None:
		pass

	def run(self) -> None:
		self.running = True
		clock = pygame.time.Clock()
		disposed_stages = []

		delta = 0

		self.init()

		while self.running:
			self.screen.fill((0, 0, 0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
				if event.type == pygame.KEYDOWN:
					for stage in self.stages:
						if stage.enabled:
							stage.key_down(event.key)
				if event.type == pygame.KEYUP:
					for stage in self.stages:
						if stage.enabled:
							stage.key_up(event.key)

			# Check for disposed
			if disposed_stages:
				for stage in disposed_stages:
					self.stages.remove(stage)
				disposed_stages = []

			# Update
			for stage in self.stages:
				if stage.disposed: disposed_stages.append(stage)
				if stage.enabled: stage.update(delta)

			# Draw
			for stage in self.stages:
				if stage.visible: stage.draw(self.screen)

			delta = clock.tick(self.fps)

			pygame.display.flip()

		pygame.quit()

	def add_stage(self, stage:Stage) -> None:
		self.stages.append(stage)

