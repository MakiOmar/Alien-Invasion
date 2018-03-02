import pygame
import sys
from bullet import Bullet
def update_screen(ai_stngs,screen, ai_ship, bullets):
	# Redraw the screen during each pass through the loop.
	screen.fill(ai_stngs.bg_color)

	#Draw spaceship
	ai_ship.blitme()
	#Check bullets limit to the value in settings

	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()

def fire_bullets(settings, screen, ship, bullets):
	if len(bullets) < settings.bullets_allowed:
			# Create a new bullet and add it to the bullets group.
			new_bullet = Bullet(settings, screen, ship)
			bullets.add(new_bullet)

def check_keydown_event(settings, event, screen, ship, bullets):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			settings.move_right = True

		elif event.key == pygame.K_LEFT:
			settings.move_left = True

		elif event.key == pygame.K_SPACE:
			fire_bullets(settings, screen, ship, bullets)

def check_keyup_event(settings, event):
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT:
			settings.move_right = False
		
		if event.key == pygame.K_LEFT:
			settings.move_left = False

def check_events(settings, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			return

		check_keydown_event(settings, event, screen, ship, bullets)

		check_keyup_event(settings, event)
			
def update_bullets(bullets):
	"""Update position of bullets and get rid of old bullets."""
	# Update bullet positions.
	bullets.update()
	# Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

