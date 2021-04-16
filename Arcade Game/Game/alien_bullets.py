import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):
    def __init__(self, game_settings, screen, alien):
        #create a bullet at the alien's current position
        super().__init__()
        self.screen = screen

        #creating a bullet rect 
        self.rect = pygame.Rect(0, 0, game_settings.alien_bullet_width, game_settings.alien_bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        #storing the bullet's position
        self.y = float(self.rect.y)

        self.color = game_settings.alien_bullet_color
        self.speed_factor = game_settings.alien_bullet_speed_factor


    def update(self):
        #moving the bullet forward
        self.y -= self.speed_factor
        self.rect.y = self.y


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


