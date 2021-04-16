import pygame
from pygame.sprite import Sprite

class Health(Sprite):
    def __init__(self, game_settings, screen, ship):
        #create a bar
        super().__init__()
        self.screen = screen

        #creating a health bar
        self.rect = pygame.Rect(0, 0, 100, 5)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.bottom

        #storing the bar's position
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery) 
        
        self.color = (0,250,0)

    def update(self, ship):
        #moving the bar with the ship
        self.centerx = float(ship.centerx)
        self.centery = float(ship.rect.bottom + 5)
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
    def draw_bar(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


