import pygame
from pygame.sprite import Sprite

class Boss():
    def __init__(self,game_settings, screen):
        #Initialize the boss and set its starting position
        self.screen = screen
        self.game_settings = game_settings

        #creating the boss's rect 
        self.image = pygame.image.load("images/boss1.png")
        self.image = pygame.transform.scale(self.image, (120,120)) #resizing the boss
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start the boss at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top + 15 # +15 is to have the health bar on top

        #settibng the boss's image centers; these are dependent on the self.rect that was set earlier
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #Assign boss health
        self.health = 120
    


    #boss movements
    def update(self):
        self.centerx += (self.game_settings.boss_speed_factor * self.game_settings.boss_direction)
        self.rect.centerx = self.centerx
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        

    def blitme(self):
        #Draw the boss at its current location
        self.screen.blit(self.image, self.rect)
