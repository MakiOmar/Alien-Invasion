import pygame
import settings
import ship
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
		screen.fill(ai_stngs.bg_color)
		ai_ship.blitme()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				turnning = False


		# Make the most recently drawn screen visible.
		pygame.display.flip()

run_game()
