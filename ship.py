import pygame
class Ship(object):
	def __init__(self,ai_settings, screen):
		"""Initialize the ship and set its starting position."""
		self.screen = screen

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = float(self.screen_rect.bottom)


	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

	def update(self, ai_settings):
		if ai_settings.move_right and self.rect.right <= self.screen_rect.right:
			self.rect.centerx += 1

		if ai_settings.move_left and self.rect.left >= 0:
			self.rect.centerx -= 1