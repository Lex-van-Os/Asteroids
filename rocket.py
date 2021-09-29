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

def rocket(x,y,angle):
    imgCopy = pygame.transform.rotate(img, angle)
    window.blit(imgCopy, (x - int(imgCopy.get_width() / 2 ), y - int(imgCopy.get_height() / 2)))


x =  (display_width - (display_width / 2))
y = (display_height - (display_height / 2))

acceleration = 0.25

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y -= acceleration
    # if keys[pygame.K_DOWN]:
    #     y += 0.2
    if keys[pygame.K_RIGHT]:
        angle -= acceleration
    if keys[pygame.K_LEFT]:
        angle += acceleration

    window.fill(0)
    rocket(x,y,angle)
        
    pygame.display.update()

pygame.quit()
quit()