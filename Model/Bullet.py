import pygame
from Model.Spaceship import Spaceship

class Bullet(pygame.Rect):
    def __init__(self,spaceship:Spaceship):
          super().__init__(spaceship.x + spaceship.width, spaceship.y + spaceship.height / 2 - 5, 20, 20)

   