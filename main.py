
import pygame
import os
from Model.Spaceship import Spaceship
from Utilities.Consts import Consts
from game import *
from Window import *
from Model.Bullet import *
from Model.Stone import *



def main():
    pygame.init()
    yellowKeys = {'left': pygame.K_a, 'right': pygame.K_d,
              'up': pygame.K_w, 'down': pygame.K_s}
       
    redKeys = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT,
           'up': pygame.K_UP, 'down': pygame.K_DOWN}
    spaceship1 = Spaceship(100, 200, 55, 44, 'spaceship_yellow.png', 90, yellowKeys,10)
    #stone
    stoneKeys = {'movement': pygame.K_SPACE}
    stone = Stone(450, 300, Consts.STONE_WIDTH, Consts.STONE_HEIGHT, 'stone.png', 270, stoneKeys)   


    spaceship2 = Spaceship(700, 300, 55,
                            44, 'spaceship_red.png', 270, redKeys,10)
    window = Window(900,500,"bens game ")
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
                    game.spaceship1.bullets.append(bulletSpaceship1)

                if event.key == pygame.K_RSHIFT and len(game.spaceship2.bullets) < Consts.MAX_Bullet:
                    bulletSpaceship2 = Bullet(spaceship2)
                    game.spaceship2.bullets.append(bulletSpaceship2)

            if event.type == Consts.RED_HIT:
                game.spaceship2.Health -= 1
            if event.type == Consts.YELLOW_HIT:
                game.spaceship1.Health -= 1
        if  game.spaceship1.Health <= 0 or  game.spaceship2.Health <= 0:
            break

        game.spaceship1.move(Consts.STEP)
        game.spaceship2.move(Consts.STEP)

        game.handle_bullet()
        game.draw_window()
        stone.move(Consts.STEP)
    # pygame.quit()
    main()


if __name__ == "__main__":
    main()
