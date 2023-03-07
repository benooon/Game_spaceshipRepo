import pygame
import os 
class Consts:
    pygame.font.init()
    HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
    WHITE = (255, 255, 255)
    PINK = (255,192,203)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)
    FPS = 60  # frame per second
    STEP = 5
    Bullet_Step = 7
    MAX_Bullet = 5
    YELLOW_HIT = pygame.USEREVENT + 1
    RED_HIT = pygame.USEREVENT + 2
    SPACE = pygame.image.load(os.path.join('Assets','space.jpg'))
    STONE_WIDTH, STONE_HEIGHT = 66, 66
    SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 77, 66
    MAX_HEALTH = 10
    WINDOW_WIDTH, WINDOW_HEIGHT = 1500,700