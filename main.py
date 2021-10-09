import pygame, threading
from rocket import Rocket
from asteroid import Asteroid
from environment import Environment
from asteroid_manager import AsteroidManager

# Environment for pre-defined width and height
environment = Environment()
asteroid_manager = AsteroidManager()

backGround = pygame.image.load('assets/background.png')

FPS = 60
ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT = 50, 50
ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT = 35, 35
ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT = 20, 20

# Define asteroids list for storing newly created asteroids
asteroids = []


def draw(rocket, asteroids):
    # Lijst van asteroides wordt meegegeven, waardoorheen geloopt wordt, om ze allemaal te laten bewegen
    win.blit(backGround, (0,0))
    rocket.draw(win)
    for asteroid in asteroids:
        asteroid.draw_asteroid(win)
    pygame.display.update()


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

        # Ervoor zorgen dat er niet meer dan een aantal astroides worden ingeladen
        if asteroid_manager.asteroids_count <= 15:
            print("Creating asteroid")
            asteroids.append(asteroid_manager.create_asteroid())

        draw(rocket, asteroids)


if __name__ == "__main__":
    pygame.init()
    # Set window width and height based on pre-defined environment width and heights, that can be changed
    win = pygame.display.set_mode((environment.environment_width, environment.environment_height))

    main()