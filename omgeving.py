import pygame

highscore = pygame.image.load('assets/highscore.png')
highscore_button = pygame.transform.scale( highscore, (300 , 200))
retry = pygame.image.load('assets/retry.png')
retry_button = pygame.transform.scale( retry, (300 , 200))
close = pygame.image.load('assets/close.png')
close_button = pygame.transform.scale( close, (300 , 200))