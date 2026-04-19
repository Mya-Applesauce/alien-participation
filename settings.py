import pygame

class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (69, 32, 136)
        self.bg_image = pygame.image.load("images/space.png")
        
        self.ship_speed = 8
        self.ship_limit = 3

        self.alien_speed = 2.0
        self.fleet_drop_speed = 10.0
        self.fleet_direction = 1

        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (240, 60, 60)
        self.bullet_image = pygame.image.load("images/bullet.png")

        self.bullets_allowed = 20