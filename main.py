import pygame
from rocket import Rocket
from asteroid import asteroid

pygame.init()

width, height = 1280, 720

backGround = pygame.image.load('assets/background.png')
backGround = pygame.transform.scale(backGround, (1280, 720))

pygame.display.set_caption('Asteroids')
win = pygame.display.set_mode((width,height))

FPS = 60

ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT = 50, 50
ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT = 35, 35
ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT = 20, 20

# Asteroid rectangles
asteroid_l = pygame.Rect(0, 200, ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT)
asteroid_m = pygame.Rect(900, 400, ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT)
asteroid_s = pygame.Rect(300, 0, ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT)

# Bullet class
class Bullet(object):

    def __init__(self):
        self.point = rocket.head
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
        self.c = rocket.cosine
        self.s = rocket.sine
        self.xv = self.c * 10
        self.yv = self.s * 10

    def move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), [self.x, self.y, self.w, self.h])

    def checkOffScreen(self):
        if self.x < -50 or self.x > width or self.y > height or self.y < -50:
            return True

def draw(rocket):
    win.blit(backGround, (0,0))
    rocket.draw(win)
    asteroid.draw_window(asteroid_l, asteroid_m, asteroid_s, win)

    for b in bullets:
        b.draw(win)
    
    pygame.display.update()


rocket = Rocket()
bullets = []
count = 0
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    count += 1

    rocket.updateLocation()
    for b in bullets:
        b.move()
        if b.checkOffScreen():
            bullets.pop(bullets.index(b))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rocket.moveForward()
    if keys[pygame.K_RIGHT]:
        rocket.turnRight()
    if keys[pygame.K_LEFT]:
        rocket.turnLeft()

    asteroid_l.x += 1
    asteroid_m.x -= 1
    asteroid_s.y += 1
    rocket.autoMove()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet())

    draw(rocket)