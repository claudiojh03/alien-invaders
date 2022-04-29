import pygame
import random
from pygame.sprite import Sprite

class Truck(Sprite):
    def __init__(self, P_game):
        super().__init__()
        self.screen = P_game.screen
        self.settings = P_game.settings
        self.screen_rect = P_game.screen.get_rect()

        self.image = pygame.image.load('Assets/Truck.jpeg')
        self.image = pygame.transform.scale(self.image, (150,100))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
            self.x -= self.settings.truck_speed
            self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)