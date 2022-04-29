import sys
import pygame
import random
import threading
from time import sleep, time
from pygame.sprite import Sprite
from settings import Settings
from peep import A_Peep
from truck import Truck

class Peeper:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Peeper")

        self.peep = A_Peep(self)
        self.trucks = pygame.sprite.Group()
        self.min_trucks = self.settings.min_trucks
        self.max_trucks = self.settings.max_trucks
        pygame.time.set_timer(pygame.USEREVENT, 750)

    def _create_truck(self):
        truck = Truck(self)
        truck_width, truck_height = truck.rect.size
        Lanes = ['L1','L2', 'L3', 'L4', 'L5', 'L6']
        lane = random.choice(Lanes)
        if lane == 'L2':
            y=250
            x=0
        if lane == 'L4':
            y=550
            x=0
        if lane == 'L6':
            y=850
            x=0
        if lane == 'L1':
            y=100
            x=1920
        if lane == 'L3':
            y=400
            x=1920
        if lane == 'L5':
            y=700
            x=1920
        truck.rect.y = y
        truck.x = x
        self.trucks.add(truck)

    def hit(self):
        sleep(0.5)

    def _update_trucks(self):
        self.trucks.update()
        if pygame.sprite.spritecollideany(self.peep, self.trucks):
            self.hit()
        self.screen_rect = P_game.screen.get_rect()
        for truck in self.trucks.copy():
            if truck.rect.left > self.screen_rect.right:
                self.trucks.remove(truck)

    def run_game(self):
        while True:
            self._check_events()
            self.peep.update()
            self._update_trucks()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.USEREVENT:
                self._create_truck()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.peep.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.peep.moving_left = True
        elif event.key == pygame.K_UP:
            self.peep.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.peep.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.peep.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.peep.moving_left = False
        elif event.key == pygame.K_UP:
            self.peep.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.peep.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.peep.blitme()
        self.trucks.draw(self.screen)
        
        pygame.display.flip()

if __name__ == '__main__':
    P_game = Peeper()
    P_game.run_game()