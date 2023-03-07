import pygame
import os 
import random 
class Stone:
    def __init__(self, x, y, width, height, image, imageRotate, keys):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', image)), (self.height, self.width)), imageRotate)
        self.movement = keys['movement']
        self.moveRight = True
        # self.right = keys['right']

    def move(self, STEP):
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.movement] and bool(random.getrandbits(1)):
            if bool(random.getrandbits(1)):
                self.x -= STEP
            else:
                self.x += STEP
            