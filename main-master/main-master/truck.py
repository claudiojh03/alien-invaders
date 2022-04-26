import pygame

class A_Truck:
    def __init__(self, ai_game):
            self.screen = ai_game.screen
            self.settings = ai_game.settings
            self.screen_rect = ai_game.screen.get_rect()

            self.image = pygame.image.load('Peeper/Assets/peep.jpeg')
            self.rect = self.image.get_rect()

            self.rect.midbottom = self.screen_rect.midbottom

            self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)