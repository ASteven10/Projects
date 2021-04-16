import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    def __init__(self, game_settings, screen, boss):
        #create an alien and its start position
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        #choosing the alien image
        self.path = game_settings.alien_codes.get(game_settings.alien_code, "nothing")
        #creating the alien's rect 
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (60,60)) #resizing the alien
        self.rect = self.image.get_rect()

        #setting the alien at its starting position
        self.rect.centerx = boss.centerx
        self.rect.x = self.rect.centerx
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


        #setting the alien direction
        self.hdirection = 0
        self.vdirection = 0
        self.get_new_coordinates()

    def update(self):
        
        if self.rect.x == self.nextx and self.rect.y == self.nexty:
            self.get_new_coordinates()
            
        #Moving the alien
        if self.rect.x == self.nextx:
            self.hdirection = 0 
        if self.rect.y == self.nexty:
            self.vdirection = 0
        
        self.x += (self.game_settings.alien_speed_factor * self.hdirection)
        self.rect.x = self.x
        self.y += (self.game_settings.alien_speed_factor * self.vdirection)
        self.rect.y = self.y


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            self.get_new_coordinates()
        elif self.rect.left <= 0:
            self.get_new_coordinates()
        elif self.rect.top <= 0:
            self.get_new_coordinates()
        elif self.rect.bottom >= 400:
            self.get_new_coordinates()


    def get_new_coordinates(self):
        self.nextx = randint(0, 1100)
        self.nexty = randint(0, 400)

        if self.rect.x > self.nextx:
            self.hdirection = -1
        elif self.rect.x < self.nextx:
            self.hdirection = 1            
        if self.rect.y > self.nexty:
            self.vdirection = -1
        elif self.rect.y < self.nexty:
            self.vdirection = 1





    def blitme(self):
        #Draw the alien at its current location
        self.screen.blit(self.image, self.rect)

