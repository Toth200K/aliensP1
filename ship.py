import pygame
class Ship:
    def __init__(self, ai_game):
        # Init ship and startomg position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Spawn a ship at bottom middle of screeen
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ships horizontal posistion
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    # Update the ship's position based on movement flags
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        
        #Update the rect object from self.x
        self.rect.x = self.x
    

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    
