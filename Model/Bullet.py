import pygame


class Bullet(pygame.Rect):
    def __init__(self,spaceship):
          super().__init__((spaceship.x + spaceship.width), ((spaceship.y + spaceship.height / 2) - 5), 20, 20)

   