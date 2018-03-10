import json
class GameStats():
	"""Track statistics for Alien Invasion."""
	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings

		#Initialize score value
		self.score = 0

		# High score should never be reset.
		try:
	 		with open(self.ai_settings.score_file) as f_obj:
	 			high_score = json.load(f_obj)
				self.high_score = high_score[0]

		except:
			self.high_score = 0
			with open(self.ai_settings.score_file, "w+") as f_obj:
				json.dump([self.high_score], f_obj)

		self.level = 1
		
		# Start Alien Invasion in an active state.
		self.game_active = False
		self.reset_stats()

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit