import pygame
from rocket import Rocket

width, height = 700, 600

backGround = pygame.image.load('sprites/background.png')

FPS = 60

def draw(rocket):
    win.blit(backGround, (0,0))
    rocket.draw(win)
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

        draw(rocket)

if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((width,height))

    main()