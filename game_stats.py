class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Init Game stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Init stats that can change during the game"""

        self.ships_left = self.settings.ship_limit