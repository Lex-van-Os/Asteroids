import pygame
from pygame.locals import*

pygame.init()

display_width = 700
display_height = 600
angle = 0

window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Rocket Movement')

crashed = False
img = pygame.image.load('sprites/New_Piskel_1.png')
img = pygame.transform.scale(img, (60,60))

def rocket(x,y):
    window.blit(img, (x,y))

x =  (display_width - (display_width / 2))
y = (display_height - (display_height / 2))

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y -= 0.1

    window.fill(0)
    rocket(x,y)
        
    pygame.display.update()

pygame.quit()
quit()