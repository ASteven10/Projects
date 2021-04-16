import pygame

class Ship():
    def __init__(self,game_settings, screen):
        #Initialize the ship and set its starting position
        self.screen = screen
        self.game_settings = game_settings

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship1.png')
        self.image = pygame.transform.scale(self.image, (100,100)) #resizing the ship
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 15

        #settibng the ship's image centers; these are dependent on the self.rect that was set earlier
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery) 
        
        #flags for changing ship position
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        

    #ship movements, position and limits
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.game_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.game_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.game_settings.ship_speed_factor
        
        #setting the ship's center to match the moving ship's image
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    
    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 15
        self.centery = self.rect.centery


    def blitme(self):
        #Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
