import pygame.font

class Scoreboard():
    def __init__(self, game_settings, screen, stats):
        #Initiate scoreboard
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        #Font settings
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)

        #Making the score image
        self.prep_score()


    def prep_score(self):
        #Making an image of the score
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bgColor)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)



