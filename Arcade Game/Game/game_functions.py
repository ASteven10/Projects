import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
from alien_bullets import AlienBullet
from boss_bullets import BossBullet
from boss_health_bar import BossHealth
from boss import Boss
from pygame.sprite import Sprite



#creating a function to check events
def check_events(game_settings, screen, ship, bullets, aliens, alien_bullets, stats, play_button, boss_bullets, boss, boss_health_bar, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #on pressing keys
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets, aliens, alien_bullets)
        
        #on lifting keys
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, game_settings, screen, ship, bullets)

        #on mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets, boss_bullets, boss, game_settings, boss_health_bar, ship, sb)





#creating a function to check-down events
def check_keydown_events(event, game_settings, screen, ship, bullets, aliens, alien_bullets):
    #ship movements by pressing arrow keys
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    
    #spacebar for bullets
    elif event.key == pygame.K_SPACE:
        if game_settings.ship_code == 1 or game_settings.ship_code == 3:
            fire_bullet(game_settings, screen, ship, bullets)
            fire_bullet(game_settings, screen, ship, bullets)
        else:
            fire_bullet(game_settings, screen, ship, bullets)

    #change ship
    elif event.key == pygame.K_1: 
        change_ship(game_settings, ship, 'images/ship1.png', 1.75, 2, 6, 35, 1)
    elif event.key == pygame.K_2:
        change_ship(game_settings, ship, 'images/ship2.png', 0.90, 1.3, 55, 5, 2)
    elif event.key == pygame.K_3: 
        change_ship(game_settings, ship, 'images/ship3.png', 2.50, 3.25, 8, 55, 3)
    elif event.key == pygame.K_4:
        change_ship(game_settings, ship, 'images/ship4.png', 1.30, 1.75, 75, 7, 4)

    #shut the game
    elif event.key == pygame.K_q:
        sys.exit()
    


#creating a function to check-up events
def check_keyup_events(event, game_settings, screen, ship, bullets):
    #ship movements by lifting arrow keys
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    
    #adding an extra bullet effect to ship1
    elif event.key == pygame.K_SPACE and (game_settings.ship_code == 1 or game_settings.ship_code == 3):
            new_bullet = Bullet(game_settings, screen, ship)
            bullets.add(new_bullet)
            new_bullet = Bullet(game_settings, screen, ship)
            bullets.add(new_bullet)




#on clicking the play button
def check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets, boss_bullets, boss, game_settings, boss_health_bar, ship, sb):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        #start a new game
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not stats.game_active:
            stats.reset_stats(game_settings)
            stats.game_active = True
            aliens.empty()
            bullets.empty()
            boss_bullets.empty()
            next_boss(game_settings, boss, stats)
            next_boss_health(boss_health_bar, boss)
            ship.center_ship()
            change_ship(game_settings, ship, 'images/ship1.png', 1.75, 2, 6, 35, 1)
            sb.prep_score()











#creating a function to manage bullets
def update_bullets(game_settings, aliens, bullets, alien_bullets, boss_bullets, boss, stats, boss_health_bar, sb):
    bullets.update()
    #deleting old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    bullet_collisions(game_settings, aliens, alien_bullets, bullets, boss_bullets, boss, stats, boss_health_bar, sb)


#creating a function to manage bullets' collisions
def bullet_collisions(game_settings, aliens, alien_bullets, bullets, boss_bullets, boss, stats, boss_health_bar, sb):
    #check bullet-alien collisions
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.score += game_settings.alien_points
        sb.prep_score()
    #check bullets-alien_bullets collision
    collisions = pygame.sprite.groupcollide(bullets, alien_bullets, True, True)
    #check bullets-boss_bullets collision
    collisions = pygame.sprite.groupcollide(bullets, boss_bullets, True, True)
    #check bullets-boss collision
    if pygame.sprite.spritecollideany(boss, bullets):
        stats.score += game_settings.boss_points
        sb.prep_score()
        boss_hit(stats, boss, bullets, boss_health_bar, game_settings, sb)


#on firing a bullet
def fire_bullet(game_settings, screen, ship, bullets):
    #create new bullet and add it to the bullets group
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)










#creating a function to manage boss
def update_boss(game_settings, boss, ship, screen, boss_bullets, stats, health_bar, aliens, boss_health_bar):
    if boss.check_edges():
        game_settings.boss_direction *= -1
    
    if boss.centerx % 80 == 0:
        fire_boss_bullet(game_settings, screen, boss, boss_bullets)
    
    if (boss.centerx + 75) % 200 == 0 and game_settings.boss_code == 1:
        create_fleet(game_settings, screen, aliens, boss) #summon next wave
    elif (boss.centerx) % 300 == 0 and game_settings.boss_code == 2:
        create_fleet(game_settings, screen, aliens, boss) #summon next wave
    elif (boss.centerx) % 75 == 0 and game_settings.boss_code == 3:
        create_fleet(game_settings, screen, aliens, boss) #summon next wave
    
    boss.update()
    boss_health_bar.update(boss)
    if pygame.sprite.collide_rect(ship, boss): #check if boss and ship collide
        ship_hit(game_settings, screen, stats, boss_bullets, boss, 'boss', health_bar, ship)


#creating a function to fire boss bullets
def fire_boss_bullet(game_settings, screen, boss, boss_bullets):
    #create boss bullets and add it to the boss_bullets group
    if len(boss_bullets) < game_settings.boss_bullets_allowed:
        new_bullet = BossBullet(game_settings, screen, boss)
        boss_bullets.add(new_bullet)


#creating a function to manage boss bullets
def update_boss_bullets(game_settings, screen, ship, boss, boss_bullets, stats, health_bar):
    boss_bullets.update()
    #deleting old bullets
    for bullet in boss_bullets.copy():
        if bullet.rect.top >= ship.screen_rect.bottom:
            boss_bullets.remove(bullet)
    #check bullet-ship collisions
    if pygame.sprite.spritecollideany(ship, boss_bullets):
        ship_hit(game_settings, screen, stats, boss_bullets, boss, 'hit', health_bar, ship)









#creating a function to create and summon next wave
def create_fleet(game_settings, screen, aliens, boss):
    alien = Alien(game_settings, screen, boss)
    deploy_aliens = game_settings.wave

    for alien_number in range(deploy_aliens):
        if len(aliens) <= game_settings.max_aliens:
            #Create an alien and placing it with the boss
            alien = Alien(game_settings, screen, boss)
            aliens.add(alien)
    change_alien_type(game_settings)


#chaning the alien type
def change_alien_type(game_settings):
    #changing the alien type for the next wave
    game_settings.alien_code += 1
    if game_settings.alien_code > 4:
        game_settings.alien_code = 1




#creating a function to manage aliens
def update_aliens(game_settings, screen, stats, ship, aliens, alien_bullets, health_bar):
    for alien in aliens.sprites():
        alien.check_edges()
        if alien.x % 100 == 0 or alien.y % 100 == 0:
            fire_alien_bullet(game_settings, screen, alien,  alien_bullets)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, screen, stats, alien_bullets, aliens, 'crash', health_bar, ship)
    

#creating a function to fire alien bullets
def fire_alien_bullet(game_settings, screen, alien, alien_bullets):
    #create alien bullets and add it to the alient_bullets group
    if len(alien_bullets) < game_settings.alien_bullets_allowed:
        new_bullet = AlienBullet(game_settings, screen, alien)
        alien_bullets.add(new_bullet)


#creating a function to manage alien bullets
def update_alien_bullets(game_settings, screen, ship, aliens, alien_bullets, stats, health_bar):
    alien_bullets.update()
    #deleting old bullets
    for bullet in alien_bullets.copy():
        if bullet.rect.top >= ship.screen_rect.bottom:
            alien_bullets.remove(bullet)
    #check bullet-ship collisions
    if pygame.sprite.spritecollideany(ship, alien_bullets):
        ship_hit(game_settings, screen, stats, alien_bullets, aliens, 'hit', health_bar,ship)
    









#when a ship is hit
def ship_hit(game_settings, screen, stats, enemy_bullets, enemy, how, health_bar, ship):
    #Decrease the health left
    if stats.ships_health > 0:
        stats.ships_health -= 1
        health_bar.rect = health_bar.rect.inflate(-10, 0)
        if how == 'hit': #remove bullets
            enemy_bullets.empty()
        elif how == 'boss':
            ship.center_ship()
        else:
            enemy.empty() #remove aliens
    else: #when health is 0
        enemy_bullets.empty()
        stats.game_active = False
        stats.reset_stats(game_settings)
        health_bar.rect = health_bar.rect.inflate(100, 0)




#when boss is hit
def boss_hit(stats, boss, bullets, boss_health_bar, game_settings, sb):
    #Decrease the health left
    if boss.health > 0:
        boss.health -= game_settings.damage #reducing boss health
        boss_health_bar.rect = boss_health_bar.rect.inflate(-game_settings.damage, 0) #only takes integer values in arguments
        collisions = pygame.sprite.spritecollideany(boss, bullets) #remove the bullet
        bullets.remove(collisions)
    else:
        sleep(3)
        #boss code
        next_lvl(game_settings, stats, sb)
        game_settings.boss_code += 1
        if game_settings.boss_code > 3:
            game_settings.boss_code = 1
            stats.game_active = False
        else:
            next_boss(game_settings, boss, stats)
            next_boss_health(boss_health_bar, boss)




#creating a function to manage next boss
def next_boss(game_settings, boss, stats):
    #boss size
    game_settings.boss_size = game_settings.boss_sizes.get(game_settings.boss_code, "nothing")
    #boss image
    img = game_settings.boss_path.get(game_settings.boss_code, "nothing")
    boss.image = pygame.image.load(img)
    boss.image = pygame.transform.scale(boss.image, (game_settings.boss_size, game_settings.boss_size))
    #boss rect = image rect
    boss.rect = boss.image.get_rect()
    #boss position
    boss.rect.centerx = boss.screen_rect.centerx
    boss.rect.top = boss.screen_rect.top + 15
    boss.centerx = float(boss.rect.centerx)
    boss.centery = float(boss.rect.centery)
    #boss health
    boss.health = game_settings.boss_size
    


#creating a function to manage next boss health
def next_boss_health(boss_health_bar, boss):
    boss_health_bar.rect = pygame.Rect(0, 0, boss.health, 5)
    boss_health_bar.rect.centerx = boss.rect.centerx
    boss_health_bar.rect.bottom = boss.rect.top

    #storing the bar's position
    boss_health_bar.centerx = float(boss_health_bar.rect.centerx)
    boss_health_bar.centery = float(boss_health_bar.rect.centery) 
        


#creating a function to initiate next level
def next_lvl (game_settings, stats, sb):
    stats.score += (game_settings.boss_points * 10 * game_settings.boss_code)
    sb.prep_score()
    game_settings.boss_speed_factor += 0.5
    game_settings.wave += 2
    game_settings.max_aliens +=2
    game_settings.boss_points += 5









#creating a function to change ship
def change_ship(game_settings, ship, image, ship_speed, bullet_speed, width, height, code):
    #changing the ship and bullets
    ship.image = pygame.image.load(image)
    game_settings.ship_speed_factor = ship_speed
    game_settings.bullet_speed_factor = bullet_speed
    game_settings.bullet_width = width
    game_settings.bullet_height = height
    ship.image = pygame.transform.scale(ship.image, (100,100))
    game_settings.ship_code = code


#creating a function to manage screen
def update_screen(game_settings, screen, ship, aliens, bullets, alien_bullets, boss, boss_bullets, health_bar, boss_health_bar, stats, play_button, sb):
    #update images on screen and flip to new screen
    screen.fill(game_settings.bgColor)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in alien_bullets:
        bullet.draw_bullet()
    for bullet in boss_bullets:
        bullet.draw_bullet()
    ship.blitme()
    health_bar.draw_bar()
    aliens.draw(screen)
    boss.blitme()
    boss_health_bar.draw_bar()

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    #make the most recent screen visible
    pygame.display.flip()

