import pygame

# Highscore button png load and highscore variables to make it easier to def where to render
highscore = pygame.image.load('assets/highscore_button.png')
highscore_width, highscore_length = 240, 75
highscore_button = pygame.transform.scale( highscore, (highscore_width, highscore_length))

# Retry button png load and retry variables to make it easier to def where to render
retry = pygame.image.load('assets/retry.png')
retry_width, retry_length = 240, 75
retry_button = pygame.transform.scale( retry, (retry_width, retry_length))

# Close button png load and close variables to make it easier to def where to render 
close = pygame.image.load('assets/close.png')
close_width, close_length = 240, 75
close_button = pygame.transform.scale( close, (close_width, close_length))