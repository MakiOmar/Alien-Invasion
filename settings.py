import pygame
class Settings(object):
	"""A class to store all settings for Alien Invasion."""
	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.scrn_wdth = 640
		self.scrn_hght = 480
		self.bg_color = (230, 230, 230)
		# Ship settings
 		self.ship_speed_factor = 0.5

 		# Bullet settings
		self.bullet_speed_factor = 0.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 3, 139, 96
		self.bullets_allowed = 3

		#Ship movement flags
		self.move_right = False
		self.move_left = False

	def ai_icon (self, ico):
		icon = pygame.display.set_icon(pygame.image.load(ico))
		return icon

	def ai_screen_size(self):
		screen = pygame.display.set_mode((self.scrn_wdth, self.scrn_hght), pygame.RESIZABLE)
		return screen

	def ai_caption(self, ai_caption):
		pygame.display.set_caption(ai_caption)