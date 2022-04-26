import sys
import pygame
from settings import Settings
from peep import A_Peep
from truck import A_Truck

class Peeper:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion")

        self.peep = A_Peep(self)
        self.truck = A_Truck(self)
        
    def run_game(self):
        while True:
            self._check_events()
            self.peep.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.peep.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.peep.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.peep.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.peep.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.peep.blitme()
        self.truck.blitme()
        
        pygame.display.flip()

if __name__ == '__main__':
    ai = Peeper()
    ai.run_game()