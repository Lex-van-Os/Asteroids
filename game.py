import pygame, threading
from rocket import Rocket
from asteroid import Asteroid
from environment import Environment
from asteroid_manager import AsteroidManager
from omgeving import highscore_button
from omgeving import retry_button
from omgeving import close_button
from pygame import mixer
import os

pygame.init()

width, height = 1280, 720

# Environment for pre-defined width and height
environment = Environment()
asteroid_manager = AsteroidManager()

pygame.font.init()

width, height = 1280, 720
backGround = pygame.image.load(os.path.join('assets', 'background.png'))
backGround = pygame.transform.scale(backGround, (1280, 720))
shoot = pygame.mixer.Sound(os.path.join('assets', 'Gun+Silencer.mp3'))
# shoot = pygame.mixer.Sound(os.path.join('assets', 'hanghang69.mp3'))

pygame.display.set_caption('Asteroids')
win = pygame.display.set_mode((width,height))

FPS = 60

SCORE_FONT = pygame.font.SysFont('commicsans', 40)
SCORE_FONT_ELSE = pygame.font.SysFont('commicsans', 60)
GAME_OVER = pygame.font.SysFont("comicsans" , 100)

ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT = 50, 50
ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT = 35, 35
ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT = 20, 20

# Define asteroids list for storing newly created asteroids
asteroids = []

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

rocket = Rocket()
bullets = []

def draw(rocket, asteroids, score, hp):
    # Lijst van asteroides wordt meegegeven, waardoorheen geloopt wordt, om ze allemaal te laten bewegen
    win.blit(backGround, (0,0))
    rocket.draw(win)
    for asteroid in asteroids:
        asteroid.draw_asteroid(win)
    for b in bullets:
        b.draw(win)
       
    if hp >= 1:
        score_text = SCORE_FONT.render("SCORE: " + str(score), 1, (255, 255, 0))
        hp_text = SCORE_FONT.render("HP: " + str(hp), 1,(255, 255, 0))
        win.blit(score_text, (width  - score_text.get_width() - 10, 10))
        win.blit(hp_text, (width  - score_text.get_width() - 100, 10))
    elif hp <= 0:
        score_text = SCORE_FONT_ELSE.render("score: " + str(score), 1, (255, 255, 0))
        win.blit(score_text, (width - 450 , 150))
        game_over_text = GAME_OVER.render("game over", 1, (255, 0 , 0))
        win.blit(game_over_text, (width - 530 , 75))
        win.blit(highscore_button, ( 200 , 250))
        win.blit(retry_button, ( 200 , 200))
        win.blit(close_button, ( 200 , 300))
        
    pygame.display.update()

def main():
    hp = 3
    score = 0
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

        # Rocket collision with astroids
        for a in asteroids:
            # Calculate if rocket has same position as astroid
            if (a.x >= rocket.x - rocket.w//2 and a.x <= rocket.x + rocket.w//2) or (a.x + a.w <= rocket.x + rocket.w//2 and a.x + a.w >= rocket.x - rocket.w//2):
                if(a.y >= rocket.y - rocket.h//2 and a.y <= rocket.y + rocket.h//2) or (a.y  +a.h >= rocket.y - rocket.h//2 and a.y + a.h <= rocket.y + rocket.h//2):
                    # Delete the astroid and rocket
                    asteroids.pop(asteroids.index(a))
                    hp -= 1
                    # Game over
                    if hp <= 0:
                        rocket.destroyRocket()

            # Bullet collison with astroids
            for b in bullets:
                # Calculate if bullet has same position as astroid
                    if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                        if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:
                            # Delete the astroid
                            asteroids.pop(asteroids.index(a))
                            # Score plus 1
                            score += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            rocket.moveForward()
        if keys[pygame.K_RIGHT]:
            rocket.turnRight()
        if keys[pygame.K_LEFT]:
            rocket.turnLeft()

        rocket.autoMove()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if hp >= 1:
                        shoot.play()
                        bullets.append(Bullet())

        if asteroid_manager.asteroids_count <= 15:
            # print("Creating asteroid")
            asteroids.append(asteroid_manager.create_asteroid())

        draw(rocket, asteroids, score, hp)

if __name__ == "__main__":
    pygame.init()
    # Set window width and height based on pre-defined environment width and heights, that can be changed
    win = pygame.display.set_mode((environment.environment_width, environment.environment_height))

    main()