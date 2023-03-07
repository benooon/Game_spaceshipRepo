
import pygame
import os
from Model.Spaceship import Spaceship
from Utilities.Consts import Consts
from game import *
from Window import *
from Model.Bullet import *

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 77, 66
maxHealth = 10
Window_Width, Window_Height = 1000,600


def main():
    yellowKeys = {'left_': pygame.K_d, 'right': pygame.K_g,
              'up': pygame.K_r, 'down': pygame.K_f}  
    redKeys = {'left_': pygame.K_LEFT, 'right': pygame.K_RIGHT,
           'up': pygame.K_UP, 'down': pygame.K_DOWN}
    spaceship1 = Spaceship(100, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, 'spaceship_yellow.png', 90, yellowKeys,maxHealth)
    spaceship2 = Spaceship(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, 'spaceship_red.png', 270, redKeys,maxHealth)

    window = Window(Window_Width,Window_Height,"SpaceShip Game")
    clock = pygame.time.Clock()  # to config FPS
    run = True
    game = Game(spaceship1,spaceship2,window)
    while run:

        game.draw_window()
        clock.tick(Consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(game.spaceship1.bullets) < Consts.MAX_Bullet:
                    
                    bulletSpaceship1 = Bullet(spaceship1) 
                    print(f'{bulletSpaceship1.y=}')
                    print(f'{spaceship2.y=}')
                    game.spaceship1.bullets.append(bulletSpaceship1)

                if event.key == pygame.K_RSHIFT and len(game.spaceship2.bullets) < Consts.MAX_Bullet:
                    bulletSpaceship2 = Bullet(spaceship2)
                    print(f'{bulletSpaceship2.y=}')
                    print(f'{spaceship1.y=}')
                    game.spaceship2.bullets.append(bulletSpaceship2)

            if event.type == Consts.RED_HIT:
                game.spaceship2.Health -= 1
            if event.type == Consts.YELLOW_HIT:
                game.spaceship1.Health -= 1
        if  game.spaceship1.Health <= 0 or  game.spaceship2.Health <= 0:
            break

        game.move(Consts.STEP,spaceship1)
        game.move(Consts.STEP,spaceship2)

        game.handle_bullet()
        game.draw_window()
    # pygame.quit()
    main()


if __name__ == "__main__":
    main()
