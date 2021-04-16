class GameStats():
    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.ships_health = 10
        self.game_active = False
        self.score = 0
    
    def reset_stats(self, game_settings):
        self.ships_health = 10
        self.score = 0
        game_settings.boss_code = 1
        game_settings.alien_code = 1
        game_settings.boss_speed_factor = 0.75
        game_settings.wave = 3
        game_settings.max_aliens = 8

