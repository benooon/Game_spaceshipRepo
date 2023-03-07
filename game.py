from Utilities.ErrorHandler import ErrorHandler
from Model.Spaceship import  Spaceship
from Window import * 
from Utilities.Consts import *
import pygame

class Game:
    def __init__(self, spaceship1:Spaceship, spaceship2:Spaceship, window:Window):
        if not isinstance(spaceship1, Spaceship):
            raise TypeError(ErrorHandler.ERROR_SPACESHIP1_MUST_BE_SPACESHIP)
        if not isinstance(spaceship2, Spaceship):
            raise TypeError(ErrorHandler.ERROR_SPACESHIP2_MUST_BE_SPACESHIP)
        if not isinstance(window, Window):
            raise TypeError(ErrorHandler.ERROR_WINDOW_MUST_BE_WINDOW)
      
        
        self.spaceship1 = spaceship1
        self.spaceship2 = spaceship2
        self.window = window

    
    @property
    def window(self):
        return self._window
    
    @window.setter
    def window(self, value):
        if not isinstance(value, Window):
            raise TypeError(ErrorHandler.ERROR_WINDOW_MUST_BE_WINDOW_CLASS)
        self._window = value
    
    @property
    def spaceship1(self):
        return self._spaceship1
    
    @spaceship1.setter
    def spaceship1(self, value):
        if not isinstance(value, Spaceship):
            raise TypeError(ErrorHandler.ERROR_SPACESHIP_MUST_BE_SPACESHIP_CLASS)
        self._spaceship1 = value
    
    @property
    def spaceship2(self):
        return self._spaceship2
    
    @spaceship2.setter
    def spaceship2(self, value):
        if not isinstance(value, Spaceship):
            raise TypeError(ErrorHandler.ERROR_SPACESHIP_MUST_BE_SPACESHIP_CLASS)
        self._spaceship2 = value
    
 

    def startGame(self):
        run = True
        clock = pygame.time.Clock()  # to config FPS
        self.spaceship1.buildSpaceship(self.window)
        self.spaceship2.buildSpaceship(self.window)
    BLACK = (0, 0, 0)

    def draw_window(self):
        # WINDOW.fill(WHITE)  # מילוי מסך
        self.window.screen.blit(self.window.bg, (0, 0))

        pygame.draw.rect(self.window.screen, Consts.BLACK, self.window.border)  # ציור של הבורדר למסך
        self.spaceship1.buildSpaceship(self.window)
        self.spaceship2.buildSpaceship(self.window)
        spaceship1_health_text = Consts.HEALTH_FONT.render("HEALTH " + str(self.spaceship1.Health), 1, Consts.WHITE)
        spaceship2_health_text = Consts.HEALTH_FONT.render("HEALTH " + str(self.spaceship2.Health), 1, Consts.WHITE)
        self.window.screen.blit(spaceship1_health_text,(self.window.width - spaceship1_health_text.get_width() - 10,10))
        self.window.screen.blit(spaceship2_health_text,(10,10))

        for bullet in self.spaceship1.bullets:
            pygame.draw.rect(self.window.screen, Consts.RED, bullet)
        for bullet in self.spaceship2.bullets:
            pygame.draw.rect(self.window.screen, Consts.YELLOW, bullet)
        pygame.display.update()  # רענון והזרקת נתונים חדשים למסךS1



    def  handle_bullet(self):
        for bullet in self.spaceship1.bullets:
            bullet.x += Consts.Bullet_Step
            print(f'{self.spaceship2.y},{bullet.y}')
            if self.spaceship2.collidedict(bullet):
                pygame.event.post(pygame.event.Event(Consts.YELLOW_HIT))
                self.spaceship1.bullets.clear()
            elif bullet.x > self.window.width:
                self.spaceship1.bullets.remove(bullet)
        for bullet in self.spaceship2.bullets:
            bullet.x -= Consts.Bullet_Step
            if self.spaceship1.colliderect(bullet):

                print(self.spaceship1.x,self.spaceship1.y)
                print(bullet.x,bullet.y)
                pygame.event.post(pygame.event.Event(Consts.RED_HIT))
                self.spaceship2.bullets.clear()
            elif bullet.x < 0:
                self.spaceship2.bullets.remove(bullet)


    def buildSpaceship(self, window :Window):
        window.screen.blit(self.image, (self.x, self.y))
 