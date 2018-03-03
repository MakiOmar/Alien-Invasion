import pygame
import settings
import ship
import game_functions as GF
from pygame.sprite import Group
from alien import Alien
def run_game():
	#@ai_stngs : Alien Invaders Settings
	ai_stngs = settings.Settings()

	# Initialize game and create a screen object.
	pygame.init()

	#game icon
	ai_stngs.ai_icon("images/alien.bmp")

	#build screen
	screen = ai_stngs.ai_screen_size()

	# Make an alien.
 	ai_alien = Alien(ai_stngs, screen)

	#game caption
	ai_stngs.ai_caption("Alien Invasion")

	#instantiate the ship objec
	ai_ship = ship.Ship(ai_stngs, screen)

	# Make a group to store bullets in.
	bullets = Group()

	while True:

		GF.check_events(ai_stngs, screen, ai_ship, bullets)

		#ship movement
		ai_ship.update()

		 
		GF.update_bullets(bullets)

		GF.update_screen(ai_stngs,screen, ai_ship, bullets, ai_alien)
		# Make the most recently drawn screen visible.
		pygame.display.flip()

run_game()
