import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep
from pygame.sprite import Group
def update_screen(ai_stngs,screen, ai_ship, bullets, aliens,stats, play_button):
	# Redraw the screen during each pass through the loop.
	screen.fill(ai_stngs.bg_color)

	#Draw spaceship
	ai_ship.blitme()

	#draw Alien
	aliens.draw(screen)

	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	# Draw the play button if the game is inactive.
	if not stats.game_active:
		play_button.draw_button()

def fire_bullets(settings, screen, ship, bullets):
	if len(bullets) < settings.bullets_allowed:
			# Create a new bullet and add it to the bullets group.
			new_bullet = Bullet(settings, screen, ship)
			bullets.add(new_bullet)
			settings.bullet_sound()
def check_keydown_event(settings, event, screen, ship, bullets):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			settings.move_right = True

		elif event.key == pygame.K_LEFT:
			settings.move_left = True

		elif event.key == pygame.K_SPACE:
			fire_bullets(settings, screen, ship, bullets)
		elif  event.key == pygame.K_q:
			sys.exit()
			return

def check_keyup_event(settings, event):
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT:
			settings.move_right = False
		
		if event.key == pygame.K_LEFT:
			settings.move_left = False

def check_events(settings, screen, ship,aliens, bullets, stats, play_button):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			return
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(settings, screen,ship, aliens,bullets,stats, play_button, mouse_x, mouse_y)

		check_keydown_event(settings, event, screen, ship, bullets)

		check_keyup_event(settings, event)

def check_play_button(ai_settings, screen,ship, aliens,bullets,stats, play_button, mouse_x, mouse_y):
	"""Start a new game when the player clicks Play."""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and  not stats.game_active:
		# Reset the game statistics.
		stats.reset_stats()
		stats.game_active = True

		# Empty the list of aliens and bullets.
		aliens.empty()
		bullets.empty()

		ai_settings.main_sound(stats)
		# Create a new fleet and center the ship.
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		
def update_bullets(ai_settings, screen, ship, aliens, bullets):
	"""Update position of bullets and get rid of old bullets."""
	# Update bullet positions.
	bullets.update()
	# Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
	
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
	# Check for any bullets that have hit aliens.
	# If so, get rid of the bullet and the alien.
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens) == 0:
		# Destroy existing bullets and create new fleet.
		bullets.empty()
		create_fleet(ai_settings, screen, ship, aliens)

def get_number_rows(ai_settings, ship_height, alien_height):
	"""Determine the number of rows of aliens that fit on the screen."""
	available_space_y = (ai_settings.scrn_hght - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def get_number_aliens_x(ai_settings, alien_width):
	"""Determine the number of aliens that fit in a row."""
	available_space_x = ai_settings.scrn_wdth - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""Create an alien and place it in the row."""
	alien = Alien(ai_settings, screen)
	alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def check_fleet_edges(ai_settings, aliens):
	"""Respond appropriately if any aliens have reached an edge."""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	"""Drop the entire fleet and change the fleet's direction."""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens, ship, stats, screen, bullets):
	"""Check if the fleet is at an edge,and then update the postions of all aliens in the fleet."""
	check_fleet_edges(ai_settings, aliens)
	"""Update the postions of all aliens in the fleet."""
	aliens.update()
	# Look for alien-ship collisions.
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

	# Look for aliens hitting the bottom of the screen.
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def create_fleet(ai_settings, screen,ship, aliens):
	"""Create a full fleet of aliens."""
	# Create an alien and find the number of aliens in a row.
	# Spacing between each alien is equal to one alien width.
	alien = Alien(ai_settings, screen)

	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	for row_number in range(number_rows):
		# Create the first row of aliens.
		for alien_number in range(number_aliens_x):
			# Create an alien and place it in the row.
			create_alien(ai_settings, screen, aliens, alien_number, row_number)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
	"""Respond to ship being hit by alien."""
	if stats.ships_left > 0:
		# Decrement ships_left.
		stats.ships_left -= 1

		# Empty the list of aliens and bullets.
		aliens.empty()
		bullets.empty()

		# Create a new fleet and center the ship.
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		# Pause.
		sleep(0.5)
	else:
		stats.game_active = False

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
	"""Check if any aliens have reached the bottom of the screen."""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Treat this the same as if the ship got hit.
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
			break
