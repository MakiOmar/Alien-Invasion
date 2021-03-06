import pygame,settings,ship,sounds
import game_functions as GF
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from pygame import time
def run_game():

	#@ai_stngs : Alien Invaders Settings
	ai_stngs = settings.Settings()

	#game icon
	ai_stngs.ai_icon("images/alien.bmp")

	#build screen
	screen = ai_stngs.ai_screen_size()

	#game caption
	ai_stngs.ai_caption("Alien Invasion")

	
	# Create an instance to store game statistics and create a scoreboard.
	stats = GameStats(ai_stngs)

	# Make the Play button.
	play_button = Button(ai_stngs, screen, "Play")
	sb = Scoreboard(ai_stngs, screen, stats)

	#instantiate the ship objec
	ai_ship = ship.Ship(ai_stngs, screen)

	# Make a group to store bullets in.
	bullets = Group()

	# Make a group to store aliens in.
	aliens = Group()

	# Create the fleet of aliens.
	GF.create_fleet(ai_stngs, screen, ai_ship, aliens)

	clock = pygame.time.Clock()

	while True:
		GF.check_events(ai_stngs, screen, ai_ship,aliens, bullets,stats, play_button,sb)
		if not stats.game_paused:
			if stats.game_active:
				#ship movement
				ai_ship.update()

				GF.update_bullets(ai_stngs, screen, ai_ship, aliens, bullets,stats,sb)

				GF.update_aliens(ai_stngs, aliens, ai_ship, stats, screen, bullets,sb)

		GF.update_screen(ai_stngs, screen, ai_ship, bullets, aliens,stats, play_button,sb)
		
		# Make the most recently drawn screen visible.
		pygame.display.flip()
		
		clock.tick(150)

run_game()
