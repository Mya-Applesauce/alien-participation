class GameStats:
    def __init__(self, alien_game):
        self.settings = alien_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit