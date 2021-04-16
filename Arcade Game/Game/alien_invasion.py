import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
from boss import Boss
import game_functions as gf
from health_bar  import Health
from boss_health_bar import BossHealth
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard




def lets_play():
    pygame.init()

    #setting the background screen
    game_settings = Settings()
    game_screen = pygame.display.set_mode((game_settings.width, game_settings.height))

    pygame.display.set_caption("Have Fun!")

    #Setting game stats
    stats = GameStats(game_settings)
    sb = Scoreboard(game_settings, game_screen, stats)

    #Creating ship and bullets
    myShip = Ship(game_settings, game_screen)
    health_bar = Health(game_settings, game_screen, myShip)
    bullets = Group()
    alien_bullets = Group()
    boss_bullets = Group()

    #Creating an Alien fleet
    aliens = Group()
   
    #creating boss and its health bar
    boss = Boss(game_settings, game_screen)
    boss_health_bar = BossHealth(game_settings, game_screen, boss)

    #Creating the play button
    play_button = Button(game_settings, game_screen, "Play")


    #running the game
    while True:
        gf.check_events(game_settings, game_screen, myShip, bullets, aliens, alien_bullets, stats, play_button, boss_bullets, boss, boss_health_bar, sb)
        if stats.game_active:
            myShip.update()
            health_bar.update(myShip)
            gf.update_bullets(game_settings,  aliens, bullets, alien_bullets, boss_bullets, boss, stats, boss_health_bar, sb)
            gf.update_alien_bullets(game_settings, game_screen, myShip, aliens, alien_bullets, stats, health_bar)
            gf.update_aliens(game_settings, game_screen, stats, myShip, aliens, alien_bullets, health_bar)
            gf.update_boss_bullets(game_settings, game_screen, myShip, boss, boss_bullets, stats, health_bar)
            gf.update_boss(game_settings, boss, myShip, game_screen, boss_bullets, stats, health_bar, aliens, boss_health_bar)
        gf.update_screen(game_settings, game_screen, myShip, aliens, bullets, alien_bullets, boss, boss_bullets, health_bar, boss_health_bar, stats, play_button, sb)
lets_play()




