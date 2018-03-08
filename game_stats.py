class GameStats():
	"""Track statistics for Alien Invasion."""
	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings

		#Initialize score value
		self.score = 0

		# Start Alien Invasion in an active state.
		self.game_active = False
		self.reset_stats()

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit