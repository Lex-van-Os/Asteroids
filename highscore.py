import pygame, os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Highscore Screen")

FPS = 60

# Background image
HIGHSCORE_IMAGE = pygame.image.load('assets/highscore.png')
HIGHSCORE_WIDTH, HIGHSCORE_HEIGHT = 900, 500

def draw_window():
# Game Loop
    run = True
    while run:
        # RGB = Red, Green, Blue
        WIN.fill((0, 0, 0))
        # Load Background Image
        WIN.blit(HIGHSCORE_IMAGE, (0, 0))

        pygame.display.flip()

def draw_main():

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()






# Call the blit method to draw image on screen
screen.blit(HIGHSCORE_IMAGE, (0, 0))





"""
HIGHSCORE_IMAGE = pygame.image.load(os.path.join)('game-programming-challenge-medium-rare-chicken/assets/', 'highscore.png')
BACKGROUND_COLOR = (0, 0, 0)

def draw_window(HIGHSCORE_IMAGE):
    WIN.fill(BACKGROUND_COLOR)
    pygame.display.update()
    
"""