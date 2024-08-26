import sys
import math
from random import random
import pygame
from Settings import settings
from Ship import ship 
from Bullet import bullet
from Alien import alien
from Star import star
from time import sleep
from Game_stats import GameStats

class Alien_invasion :
    def __init__(self) :
        pygame.init()
        self.settings = settings()
        # self.screen = pygame.display.set_mode((800,900))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        self.ship = ship(self)
        self.fps = 0
        self.font = pygame.font.SysFont('Consolas', 30)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self._fill_with_stars()
        self._create_fleet()
        
        

    def run_game(self):
        start_time = pygame.time.get_ticks()
        fps = 0
        while (True) :
            self._check_event()
            self.ship.update_position()
            self.update_aliens()
            self.bullets.update()
            
                
            
            pygame.time.wait(math.floor((1/self.settings.FPS*10)))
            fps += 1
            if  pygame.time.get_ticks()-start_time >= 1000:
                self.fps = fps
                fps =0 
    
            self._update_screen()
            
            


    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
        
            
    def update_aliens(self):
        self.aliens.update()
        self.check_fleet_edges()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self.ship_hit()
    def ship_hit(self):
        self.stats.ships_left -= 1
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        self.ship.center_ship()
        sleep(0.5)
    
    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.alien_drop_speed
        self.settings.fleet_direction *=-1

        
                    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.screen.blit(self.font.render(str(self.fps),True,(0,59,0)),(20,20))
        for s in self.stars.sprites():
            s.draw()
        for b in self.bullets.sprites():
            b.draw()
        for a in self.aliens.sprites():
            a.draw()
        

        pygame.display.flip()
    
    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            self.exit()
        if event.key == pygame.K_SPACE:
            if len(self.bullets) < self.settings.bullets_allowed:
                self._fire_bullet()


    def _check_keyup_event(self, event):
        if event.key== pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        al = alien(self)
        alien_width = al.rect.width
        alien_height = al.rect.height
        available_spacex = self.settings.screen_width - (2*alien_width)
        aliens_number = available_spacex // (2*alien_width)
        print(aliens_number)
        for i in range(5):
            for alien_number in range(aliens_number):
                al = alien(self)
                al.x = alien_width + 2 * alien_width * alien_number
                al.y = alien_height*2*i + alien_height
                al.rect.x = al.x
                al.rect.y = al.y
                self.aliens.add(al)
    def _fill_with_stars(self):
        for i in range(self.settings.BG_stars):
            new_star = star(self)
            new_star.rect.x= (self.settings.screen_width)*random()
            new_star.rect.y= (self.settings.screen_height)*random()
            self.stars.add(new_star)





    def exit(self):
        pygame.quit()
        sys.exit()
    def _fire_bullet(self):
        new_bullet = bullet(self)
        self.bullets.add(new_bullet)
        


if __name__ == "__main__":
    ai = Alien_invasion()
    ai.run_game()
       
