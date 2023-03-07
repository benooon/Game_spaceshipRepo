
import pygame
import os
from Model.Spaceship import Spaceship
from Utilities.Consts import Consts
from game import *
from Model.Window import *
from Model.Bullet import *
from Model.Stone import *



def main():


    yellowKeys = {'left': pygame.K_d, 'right': pygame.K_g,
              'up': pygame.K_r, 'down': pygame.K_f}  
    redKeys = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT,
           'up': pygame.K_UP, 'down': pygame.K_DOWN}
    spaceship1 = Spaceship(100, int(Consts.WINDOW_HEIGHT/2), Consts.SPACESHIP_WIDTH, Consts.SPACESHIP_HEIGHT, 'spaceship_yellow.png', 90, yellowKeys,Consts.MAX_HEALTH,True)
    spaceship2 = Spaceship(Consts.WINDOW_WIDTH-100, int(Consts.WINDOW_HEIGHT/2), Consts.SPACESHIP_WIDTH, Consts.SPACESHIP_HEIGHT, 'spaceship_red.png', 270, redKeys,Consts.MAX_HEALTH,False)

    window = Window(Consts.WINDOW_WIDTH,Consts.WINDOW_HEIGHT,"SpaceShip Game")
    clock = pygame.time.Clock()  # to cDonfig FPS
    run = True
    game = Game(spaceship1,spaceship2,window)
    #obstacle = RandomObstacle(game.window.width, game.window.height,20,20)

    pygame.mixer.init()
    music = pygame.mixer.Sound(Consts.GENERAL_SOUND)
    music.play()
    while run:
        game.draw_window()
        clock.tick(Consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
                pygame.quit()
            if game.isEnd:
                music.stop()
                main()
             
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(game.spaceship1.bullets) < Consts.MAX_Bullet:
                    bulletSpaceship1 = Bullet(spaceship1) 
                    game.spaceship1.bullets.append(bulletSpaceship1)
                    sound = pygame.mixer.Sound(Consts.SOUND_SHOOT)
                    sound.play()
                if event.key == pygame.K_RSHIFT and len(game.spaceship2.bullets) < Consts.MAX_Bullet:
                    bulletSpaceship2 = Bullet(spaceship2)
                    game.spaceship2.bullets.append(bulletSpaceship2)
                    sound = pygame.mixer.Sound(Consts.SOUND_SHOOT)
                    sound.play()
                #if event.key == pygame.K_SPACE:
                   


                #changes sides
                if event.key == pygame.K_RCTRL:
                    game.spaceship2.changeBulletDir()   
                if event.key == pygame.K_LCTRL:
                    game.spaceship1.changeBulletDir()                            

            if event.type == Consts.RED_HIT:
                game.spaceship2.Health -= 1
            if event.type == Consts.YELLOW_HIT:
                game.spaceship1.Health -= 1
        if  game.spaceship1.Health <= 0 or  game.spaceship2.Health <= 0:
            game.publishResult()
            

      
        game.spaceship1.move(Consts.STEP,game)
        game.spaceship2.move(Consts.STEP,game)

        game.handle_bullet()
        game.draw_window()
        #obstacle.update()
    
    main()


if __name__ == "__main__":
    main()
