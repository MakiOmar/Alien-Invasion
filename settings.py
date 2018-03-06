import pygame
class Settings(object):
	"""A class to store all settings for Alien Invasion."""
	def __init__(self):
		"""Initialize the game's settings."""
		self.game_initialize = pygame.init()
		# Screen settings
		self.scrn_wdth = 1024
		self.scrn_hght = 640
		self.bg_color = (230, 230, 230)
		# Ship settings
 		self.ship_speed_factor = 1.5

 		# Bullet settings
		self.bullet_speed_factor = 1.5
		self.bullet_width = 3
		self.bullet_height = 10
		self.bullet_color = 3, 139, 96
		self.bullets_allowed = 3

		# Alien settings
 		self.alien_speed_factor = 1

 		#Fleet speed
 		self.fleet_drop_speed = 10
 		
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		#Ship movement flags
		self.move_right = False
		self.move_left = False

		#ships left
		self.ship_limit = 3

		#sound settings
		self.NO_channels = pygame.mixer.set_num_channels(64)
 		self.volume = pygame.mixer.music.set_volume(2)

	def ai_icon (self, ico):
		icon = pygame.display.set_icon(pygame.image.load(ico))
		return icon

	def ai_screen_size(self):
		screen = pygame.display.set_mode((self.scrn_wdth, self.scrn_hght), pygame.RESIZABLE)
		return screen

	def ai_caption(self, ai_caption):
		pygame.display.set_caption(ai_caption)

	def main_sound(self):
 		return pygame.mixer.Channel(0).play(pygame.mixer.Sound("sounds/game_music.wav"))
 		

 	def bullet_sound(self):
 		return pygame.mixer.Channel(1).play(pygame.mixer.Sound("sounds/shoot.wav"))