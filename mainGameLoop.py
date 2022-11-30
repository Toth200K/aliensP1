import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        """Init game and creat game resources"""
        pygame.init()
        self.settings = Settings()
       

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #After reading, it seems confusing that in ship.py we have two
        #parametres for __init__(self,ai_game)
        #here when we call it we just need to pass the second parameter
        #which in the ship.py init would be the ai_game but here below is just 
        #self

        self.ship = Ship(self)
        

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 6
                if event.key == pygame.K_LEFT:
                    self.ship.rect.x -= 6
           
                
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()