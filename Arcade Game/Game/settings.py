class Settings():

    def __init__(self):
        #screen settings
        self.width = 1500
        self.height = 775
        self.bgColor = (10, 10, 10)

        #ship settings
        self.ship_speed_factor = 1.75
        self.ship_code = 1

        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 6
        self.bullet_height = 35
        self.bullet_color = 0, 250, 250
        self.bullets_allowed = 16
        self.bullet_place = 'R'
        self.damage = 1

        #Alien settings
        self.alien_speed_factor = 1
        self.alien_points = 5
        #giving the alien a code
        self.alien_code = 1
        self.alien_codes = {
            1: "images/e1.png",
            2: "images/e2.png",
            3: "images/e3.png",
            4: "images/e4.png",
        }
        #aliens per summon
        self.wave = 3
        self.max_aliens = 8

        #Alien bullet settings
        self.alien_bullet_speed_factor = -1.5
        self.alien_bullet_width = 6
        self.alien_bullet_height = 35
        self.alien_bullet_color = 250, 0, 0
        self.alien_bullets_allowed = 80

        #Boss settings
        self.boss_direction = 1
        self.boss_speed_factor = 0.75
        self.boss_points = 10
        #giving the boss a code
        self.boss_code = 1
        self.boss_path = {
            1: "images/boss1.png",
            2: "images/boss2.png",
            3: "images/omega.png",
        }

        #giving the boss a size
        self.boss_size = 120
        self.boss_sizes = {
            1: 120,
            2: 160,
            3: 220
        }

        #Boss bullet settings
        self.boss_bullet_speed_factor = -7.5
        self.boss_bullet_width = 12
        self.boss_bullet_height = 85
        self.boss_bullet_color = 250, 0, 200
        self.boss_bullets_allowed = 6