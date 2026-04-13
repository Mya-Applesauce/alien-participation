import pygame

class Ship:

    def __init__(self, alien_game):
        self.screen = alien_game.screen
        self.screen_rect = alien_game.screen.get_rect()

        self.image = pygame.image.load("alien invaders/alien-participation/images/spaceship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)