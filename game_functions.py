import pygame
def update_screen(ai_stngs,screen, ai_ship):
	# Redraw the screen during each pass through the loop.
	screen.fill(ai_stngs.bg_color)

	#Draw spaceship
	ai_ship.blitme()

def check_events():
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				turnning = False
