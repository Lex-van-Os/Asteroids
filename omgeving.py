import pygame

highscore = pygame.image.load('assets/highscore_button.png')
highscore_width, highscore_length = 600, 400
highscore_button = pygame.transform.scale( highscore, (highscore_width, highscore_length))

retry = pygame.image.load('assets/retry.png')
retry_width, retry_length = 600, 400
retry_button = pygame.transform.scale( retry, (retry_width, retry_length))

close = pygame.image.load('assets/close.png')
close_width, close_length = 600, 400
close_button = pygame.transform.scale( close, (close_width, close_length))