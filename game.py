from Utilities.ErrorHandler import ErrorHandler
from Model.Spaceship import  Spaceship
from Model.Window import * 
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
        self.isEnd = False 

    
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

        students_names = 'Ben Rosenbaum & Sali Haham & Dorin Averbach'
        self.spaceship1.buildSpaceship(self.window)
        self.spaceship2.buildSpaceship(self.window)
        spaceship1_health_text = Consts.HEALTH_FONT.render("HEALTH " + str(self.spaceship1.Health), 1, Consts.WHITE)
        spaceship2_health_text = Consts.HEALTH_FONT.render("HEALTH " + str(self.spaceship2.Health), 1, Consts.WHITE)
        self.window.screen.blit(spaceship1_health_text,(self.window.width - spaceship1_health_text.get_width() - 10,10))
        self.window.screen.blit(spaceship2_health_text,(10,10))
        show_students_names = Consts.HEALTH_FONT.render(students_names ,False ,Consts.PINK)
        self.window.screen.blit(show_students_names,(5,550))
        
        

        for bullet in self.spaceship1.bullets:
            pygame.draw.rect(self.window.screen, Consts.YELLOW, bullet)
        for bullet in self.spaceship2.bullets:
            pygame.draw.rect(self.window.screen, Consts.RED, bullet)
        
        if self.isEnd:
            spaceShipWin = 'right spaceship'
            if self.spaceship1.Health == 0:
                spaceShipWin = 'left spaceship'
            finishText = Consts.WINNER_FONT.render("the winner is:  " + spaceShipWin, 1, Consts.BLACK)
            self.window.screen.blit(finishText,(300,200))
            pygame.time.delay(5)
            
            
            
        pygame.display.update()  # רענון והזרקת נתונים חדשים למסךS1
        
        
    def isCollide(self,obj1,obj2):
        return obj1.colliderect(obj2)
    
    def isBulletesCollide(self,bulet,spaceShip:Spaceship):
        for b in spaceShip.bullets:
            if self.isCollide(b,bulet):
                spaceShip.bullets.remove(b)
                return True
                break
        return False
    

    
    def  handle_bullet(self):
        for bullet in self.spaceship1.bullets:
            if self.spaceship1.bulletDirRight:
                bullet.x += Consts.Bullet_Step
            else:
                bullet.x -= Consts.Bullet_Step
            if self.isCollide(self.spaceship2,bullet):
                pygame.event.post(pygame.event.Event(Consts.YELLOW_HIT))
                self.spaceship1.bullets.remove(bullet)
            elif self.isBulletesCollide(bullet,self.spaceship2):
                self.spaceship1.bullets.remove(bullet)

            elif bullet.x > self.window.width or  bullet.x <0:
                self.spaceship1.bullets.remove(bullet)
        for bullet in self.spaceship2.bullets:
            if self.spaceship2.bulletDirRight:
                bullet.x += Consts.Bullet_Step
            else:
                bullet.x -= Consts.Bullet_Step
            if self.isCollide(self.spaceship1,bullet):
                pygame.event.post(pygame.event.Event(Consts.RED_HIT))
                self.spaceship2.bullets.remove(bullet)
            elif self.isBulletesCollide(bullet,self.spaceship1):
                self.spaceship2.bullets.remove(bullet)
            elif bullet.x < 0 or bullet.x>self.window.width:
                self.spaceship2.bullets.remove(bullet)



    def publishResult(self):
        self.isEnd=True
        
        


    def buildSpaceship(self, window :Window):
        window.screen.blit(self.image, (self.x, self.y))
    

    