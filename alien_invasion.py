import pygame
import settings
import ship
import game_functions as GF
def run_game():
	#@ai_stngs : Alien Invaders Settings
	ai_stngs = settings.Settings()

	# Initialize game and create a screen object.
	pygame.init()

	#game icon
	ai_stngs.ai_icon("images/alien.png")

	#build screen
	screen = ai_stngs.ai_screen_size()

	#game caption
	ai_stngs.ai_caption("Alien Invasion")

	#instantiate the ship objec
	ai_ship = ship.Ship(ai_stngs, screen)

	turnning = True
	while turnning:
		GF.update_screen(ai_stngs,screen, ai_ship)

		GF.check_events()


		# Make the most recently drawn screen visible.
		pygame.display.flip()

run_game()
