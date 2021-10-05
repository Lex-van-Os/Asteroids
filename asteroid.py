import pygame, os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")

FPS = 60

BACKGROUND_COLOR = (0, 0, 0)
ASTEROID_LARGE_IMG = pygame.image.load(os.path.join('game-programming-challenge-medium-rare-chicken/assets/', 'asteroid_large.png'))
ASTEROID_MEDIUM_IMG = pygame.image.load(os.path.join('game-programming-challenge-medium-rare-chicken/assets/', 'asteroid_medium.png'))
ASTEROID_SMALL_IMG = pygame.image.load(os.path.join('game-programming-challenge-medium-rare-chicken/assets/', 'asteroid_small.png'))
ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT = 50, 50
ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT = 35, 35
ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT = 20, 20
ASTEROID_LARGE = pygame.transform.scale(ASTEROID_LARGE_IMG, (ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT))
ASTEROID_MEDIUM = pygame.transform.scale(ASTEROID_MEDIUM_IMG, (ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT))
ASTEROID_SMALL = pygame.transform.scale(ASTEROID_SMALL_IMG, (ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT))


def draw_window(asteroid_l, asteroid_m, asteroid_s):
    WIN.fill(BACKGROUND_COLOR)
    WIN.blit(ASTEROID_LARGE, (asteroid_l.x, asteroid_l.y))
    WIN.blit(ASTEROID_MEDIUM, (asteroid_m.x, asteroid_m.y))
    WIN.blit(ASTEROID_SMALL, (asteroid_s.x, asteroid_s.y))
    pygame.display.update()


def main():
    asteroid_l = pygame.Rect(0, 200, ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT)
    asteroid_m = pygame.Rect(900, 400, ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT)
    asteroid_s = pygame.Rect(300, 0, ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        asteroid_l.x += 1
        asteroid_m.x -= 1
        asteroid_s.y += 1
        draw_window(asteroid_l, asteroid_m, asteroid_s)
    
    pygame.quit()


if __name__ == "__main__":
    main()
