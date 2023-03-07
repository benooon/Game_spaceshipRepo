from Utilities.ErrorHandler import ErrorHandler
import pygame
import os 
from Utilities.Consts import Consts

class Window:
    def __init__(self, width, height, caption=''):
        self._width = width
        self._height = height
        self._caption = caption
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)
        self.border = pygame.Rect(self._width / 2 - 5, 0, 10, self._height )
        self.bg =  pygame.transform.scale(Consts.SPACE,(self.width,self.width))
        self.screen.blit(self.bg,(0,0))
        
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError(ErrorHandler.ERROR_WIDTH)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError(ErrorHandler.ERROR_HEIGHT)
        self._height = value
    @property
    def caption(self):
        return self._caption

    @caption.setter
    def caption(self, value):
        if not isinstance(value, str):
            raise ValueError(ErrorHandler.ERROR_CAPTION)
        self._caption = value
        pygame.display.set_caption(self.caption)


