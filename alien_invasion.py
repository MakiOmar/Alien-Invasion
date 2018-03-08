import pygame
import settings
import ship
import game_functions as GF
from pygame.sprite import Group
from game_stats import GameStats
import sounds
from button import Button
def run_game():

	#@ai_stngs : Alien Invaders Settings
	ai_stngs = settings.Settings()

	#game icon
	ai_stngs.ai_icon("images/alien.bmp")

	#build screen
	screen = ai_stngs.ai_screen_size()

	#game caption
	ai_stngs.ai_caption("Alien Invasion")

	# Make the Play button.
	play_button = Button(ai_stngs, screen, "Play")

	# Create an instance to store game statistics.
	stats = GameStats(ai_stngs)

	#instantiate the ship objec
	ai_ship = ship.Ship(ai_stngs, screen)

	# Make a group to store bullets in.
	bullets = Group()

	# Make a group to store aliens in.
	aliens = Group()

	# Create the fleet of aliens.
	GF.create_fleet(ai_stngs, screen, ai_ship, aliens)
	while True:
		GF.check_events(ai_stngs, screen, ai_ship,aliens, bullets,stats, play_button)
		if stats.game_active:
			#ship movement
			ai_ship.update()

			GF.update_bullets(ai_stngs, screen, ai_ship, aliens, bullets)

			GF.update_aliens(ai_stngs, aliens, ai_ship, stats, screen, bullets)

		GF.update_screen(ai_stngs, screen, ai_ship, bullets, aliens,stats, play_button)
		# Make the most recently drawn screen visible.
		pygame.display.flip()

run_game()
