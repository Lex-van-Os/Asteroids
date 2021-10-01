import pygame

width, height = 900, 500
win = pygame.display.set_mode((width,height))

FPS = 60

rocketImg = pygame.image.load('sprites/New_Piskel_1.png')
rocketImg = pygame.transform.scale(rocketImg, (60,60))

def drawWindow():
    win.blit(rocketImg, (410,200))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        drawWindow()
  