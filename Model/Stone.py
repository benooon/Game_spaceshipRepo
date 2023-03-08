import pygame
import os 
import random 
class Stone:
    def __init__(self, x, y, width, height, image, imageRotate, keys):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.movement = keys['movement']
        self.moveRight = True
        # self.right = keys['right']

import pygame
import random

class RandomObstacle(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height,width,hight):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width = width
        self.hight = hight
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'stone.png')), (self.width, self.hight))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)

    def update(self):
        self.rect.move_ip(random.randint(-5, 5), random.randint(-5, 5))

    def collide(self, sprite):
        if self.rect.colliderect(sprite.rect):
            return True
        return False

