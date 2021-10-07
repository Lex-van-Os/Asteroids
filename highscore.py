import pygame, os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Highscore Screen")

FPS = 60

# Background image
HIGHSCORE_IMAGE = pygame.image.load('assets/highscore.png')
HIGHSCORE_WIDTH, HIGHSCORE_HEIGHT = 900, 500

def draw_window(HIGHSCORE_IMAGE):
    WIN.fill((0, 0, 0))
    WIN.blit(HIGHSCORE_IMAGE, (0, 0))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    draw_window(HIGHSCORE_IMAGE)            
    pygame.quit()

if __name__ == "__main__":
    main()