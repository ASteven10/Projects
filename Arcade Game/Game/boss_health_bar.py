import pygame
from pygame.sprite import Sprite

class BossHealth(Sprite):
    def __init__(self, game_settings, screen, boss):
        #create a bar
        super().__init__()
        self.screen = screen

        #creating a health bar
        self.rect = pygame.Rect(0, 0, boss.health, 5)
        self.rect.centerx = boss.rect.centerx
        self.rect.bottom = boss.rect.top

        #storing the bar's position
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery) 
        
        self.color = (250,0,0)

    def update(self, boss):
        #moving the bar with the boss
        self.centerx = float(boss.centerx)
        self.centery = float(boss.rect.top - 5)
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
    def draw_bar(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


