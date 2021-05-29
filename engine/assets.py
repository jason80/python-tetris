import pygame

class AssetManager:
	def __init__(self):
		self.assets = {}

	def get_image(self, ref):
		if ref not in self.assets:
			self.assets[ref] = pygame.image.load("assets/" + ref)
			print(f"Load {ref}")
		
		return self.assets[ref]
	
asset_manager = AssetManager()