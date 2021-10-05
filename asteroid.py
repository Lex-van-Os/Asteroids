import pygame, os

ASTEROID_LARGE_IMG = pygame.image.load(os.path.join('assets/', 'asteroid_large.png'))
ASTEROID_MEDIUM_IMG = pygame.image.load(os.path.join('assets/', 'asteroid_medium.png'))
ASTEROID_SMALL_IMG = pygame.image.load(os.path.join('assets/', 'asteroid_small.png'))
ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT = 50, 50
ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT = 35, 35
ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT = 20, 20
ASTEROID_LARGE = pygame.transform.scale(ASTEROID_LARGE_IMG, (ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT))
ASTEROID_MEDIUM = pygame.transform.scale(ASTEROID_MEDIUM_IMG, (ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT))
ASTEROID_SMALL = pygame.transform.scale(ASTEROID_SMALL_IMG, (ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT))

class asteroid(object):

    def draw_window(asteroid_l, asteroid_m, asteroid_s, WIN):
        WIN.blit(ASTEROID_LARGE, (asteroid_l.x, asteroid_l.y))
        WIN.blit(ASTEROID_MEDIUM, (asteroid_m.x, asteroid_m.y))
        WIN.blit(ASTEROID_SMALL, (asteroid_s.x, asteroid_s.y))
        pygame.display.update()