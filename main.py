import pygame
from rocket import Rocket
from asteroid import asteroid

pygame.font.init()

width, height = 700, 600

backGround = pygame.image.load('assets/background.png')

pygame.display.set_caption("First Game!")

FPS = 60

SCORE_FONT = pygame.font.SysFont('commicsans', 40)

ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT = 50, 50
ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT = 35, 35
ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT = 20, 20

# Asteroid rectangles
asteroid_l = pygame.Rect(0, 200, ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT)
asteroid_m = pygame.Rect(900, 400, ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT)
asteroid_s = pygame.Rect(300, 0, ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT)

# border
BORDER = pygame.Rect(width//2 - 5, 0, 10, height)

def draw(rocket, score):
    win.blit(backGround, (0,0))
    rocket.draw(win)
    score_text = SCORE_FONT.render("score: " + str(score), 1, (255, 255, 0))
    win.blit(score_text, (width  - score_text.get_width() - 10, 10))
    asteroid.draw_window(asteroid_l, asteroid_m, asteroid_s, win)
    pygame.display.update()

score = 5

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

        draw(rocket, score)

if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((width,height))

    main()