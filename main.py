import pygame
from rocket import Rocket
from asteroid import asteroid

width, height = 700, 600
backGround = pygame.image.load('sprites/background.png')

FPS = 60

import pygame, threading
from rocket import Rocket
from asteroid import Asteroid
from environment import Environment
from asteroid_manager import AsteroidManager
from omgeving import highscore_button
from omgeving import retry_button
from omgeving import close_button

# Environment for pre-defined width and height
environment = Environment()
asteroid_manager = AsteroidManager()

pygame.font.init()

width, height = 1280, 720
backGround = pygame.image.load('assets/background.png')
backGround = pygame.transform.scale(backGround, (1280, 720))

pygame.display.set_caption("First Game!")

FPS = 60

SCORE_FONT = pygame.font.SysFont('commicsans', 40)
SCORE_FONT_ELSE = pygame.font.SysFont('commicsans', 60)
GAME_OVER = pygame.font.SysFont("comicsans" , 100)

ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT = 50, 50
ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT = 35, 35
ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT = 20, 20

def draw(rocket, asteroid_l, asteroid_m, asteroid_s):
    win.blit(backGround, (0,0))
    rocket.draw(win)
    asteroid.draw_window(asteroid_l, asteroid_m, asteroid_s, win)
    pygame.display.update()

def main():
    asteroid_l = pygame.Rect(0, 200, ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT)
    asteroid_m = pygame.Rect(900, 400, ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT)
    asteroid_s = pygame.Rect(300, 0, ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT)

# Define asteroids list for storing newly created asteroids
asteroids = []


def draw(rocket, asteroids, score):
    # Lijst van asteroides wordt meegegeven, waardoorheen geloopt wordt, om ze allemaal te laten bewegen
    win.blit(backGround, (0,0))
    rocket.draw(win)
    for asteroid in asteroids:
        asteroid.draw_asteroid(win)
       
    if hp >= 1:
        score_text = SCORE_FONT.render("score: " + str(score), 1, (255, 255, 0))
        win.blit(score_text, (width  - score_text.get_width() - 10, 10))
    else:
        score_text = SCORE_FONT_ELSE.render("score: " + str(score), 1, (255, 255, 0))
        win.blit(score_text, (width - 450 , 150))
        game_over_text = GAME_OVER.render("game over", 1, (255, 0 , 0))
        win.blit(game_over_text, (width - 530 , 75))
        win.blit(highscore_button, ( 200 , 250))
        win.blit(retry_button, ( 200 , 200))
        win.blit(close_button, ( 200 , 300))
        
    pygame.display.update()

score = 5
hp = 0

def main():
    rocket = Rocket()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            rocket.moveForward()
        if keys[pygame.K_RIGHT]:
            rocket.turnRight()
        if keys[pygame.K_LEFT]:
            rocket.turnLeft()

        asteroid_l.x += 1
        asteroid_m.x -= 1
        asteroid_s.y += 1

        draw(rocket, asteroid_l, asteroid_m, asteroid_s)

if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((width,height))
    
        # Ervoor zorgen dat er niet meer dan een aantal astroides worden ingeladen
        if asteroid_manager.asteroids_count <= 15:
            print("Creating asteroid")
            asteroids.append(asteroid_manager.create_asteroid())

        rocket.autoMove()
        draw(rocket, asteroids, score)


if __name__ == "__main__":
    pygame.init()
    # Set window width and height based on pre-defined environment width and heights, that can be changed
    win = pygame.display.set_mode((environment.environment_width, environment.environment_height))

    main()