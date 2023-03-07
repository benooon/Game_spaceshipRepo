import pygame
import os
from Model.Window import *
from Utilities.ErrorHandler import ErrorHandler

class Spaceship(pygame.Rect):
    def __init__(self, x, y, width, height, image, imageRotate, keys, Health,bulletDirRight:bool):
        if not isinstance(x, int):
            raise TypeError(ErrorHandler.ERROR_X_MUST_BE_INTEGER)
        if not isinstance(y, int):
            raise TypeError(ErrorHandler.ERROR_Y_MUST_BE_INTEGER)
        if not isinstance(width, int):
            raise TypeError(ErrorHandler.ERROR_HEIGHT_MUST_BE_INTEGER)
        if not isinstance(height, int):
            raise TypeError(ErrorHandler.ERROR_HEIGHT_MUST_BE_INTEGER)
        if not isinstance(Health, int):
            raise TypeError(ErrorHandler.ERROR_MAX_HEALTH_MUST_BE_INTEGER)
        super().__init__(x,y,width,height)
        self._height = height
        self._width = width
        self._x = x
        self._y = y
        self.Health = Health
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', image)), (self._height, self._width)), imageRotate)
        self.left_ = keys['left']
        self.right = keys['right']
        self.up = keys['up']
        self.down = keys['down']
        self.bullets = []
        self.bulletDirRight = bulletDirRight


    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError(ErrorHandler.ERROR_X_MUST_BE_INTEGER)
        self._x = value
    
    

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError(ErrorHandler.ERROR_Y_MUST_BE_INTEGER)
        self._y = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError(ErrorHandler.ERROR_WIDTH_MUST_BE_INTEGER)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(ErrorHandler.ERROR_HEIGHT_MUST_BE_INTEGER)
        self._height = value

    @property
    def Health(self):
        return self._Health

    @Health.setter
    def Health(self, value):
        if not isinstance(value, int):
            raise ValueError(ErrorHandler.ERROR_MAX_HEALTH_MUST_BE_INTEGER)
        self._Health = value
            
    def move(self, STEP, game):
        pygame.init()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.left_]:
            self.move_left(STEP, game.window.width)
        if keys_pressed[self.right]:
            self.move_right(STEP, game.window.width)
        if keys_pressed[self.up]:
            self.move_up(STEP, game.window.height)
        if keys_pressed[self.down]:
            self.move_down(STEP, game.window.height)

    def move_left(self, STEP, window_width):
        if self.x - STEP < 0:
            self.x = window_width - STEP
        else:
            self.x -= STEP

    def move_right(self, STEP, window_width):
        if self.x + self.width + STEP > window_width:
            self.x = 0
        else:
            self.x += STEP

    def move_up(self, STEP, window_height):
        if self.y - STEP < 0:
            self.y = window_height - STEP
        else:
            self.y -= STEP

    def move_down(self, STEP, window_height):
        if self.y + self.height + STEP > window_height:
            self.y = 0
        else:
            self.y += STEP



    def buildSpaceship(self, window: Window):
        window.screen.blit(self.image, (self.x, self.y))



    def changeBulletDir(self):
        self.bulletDirRight = not self.bulletDirRight
        self.image = pygame.transform.rotate(self.image, 180)
        self.bullets.clear()
           


    