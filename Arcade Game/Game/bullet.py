import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game_settings, screen, ship):
        #create a bullet at the ship's current position
        super().__init__()
        self.screen = screen

        
        #creating a bullet rect 
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        if game_settings.ship_code == 2: #determining ship2
            self.rect.centerx = ship.rect.centerx
        elif game_settings.bullet_place == 'L': #determining ship1, ship3 and ship4 bullets
            self.rect.centerx = ship.rect.centerx - 22 
            game_settings.bullet_place = 'R'
        elif game_settings.bullet_place == 'R':
            self.rect.centerx = ship.rect.centerx + 25
            game_settings.bullet_place = 'L'
    
        self.rect.top = ship.rect.top

        #storing the bullet's position
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor


    def update(self):
        #moving the bullet forward
        self.y -= self.speed_factor
        self.rect.y = self.y


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


