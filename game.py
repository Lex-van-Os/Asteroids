import pygame, threading
from rocket import Rocket
from asteroid import Asteroid
from environment import Environment
from asteroid_manager import AsteroidManager
from game_over import highscore_button, retry_button, close_button
from game_over import highscore_width, retry_width, close_width
from game_over import highscore_length, retry_length, close_length
from rocket import playerRocket
import scores_screen
import json
import home_screen

from pygame import mixer
import os

pygame.init()
pygame.font.init()
width, height = 1280, 720

# Environment for pre-defined width and height
environment = Environment()
asteroid_manager = AsteroidManager()

width, height = 1280, 720
backGround = pygame.image.load(os.path.join("assets", "background.png"))
backGround = pygame.transform.scale(backGround, (1280, 720))

shoot = pygame.mixer.Sound(f".\\" + os.path.join("assets", "Gun+Silencer.mp3"))
explosion_sound = pygame.mixer.Sound(
    f".\\" + os.path.join("assets", "explosion_sound.wav")
)
idiot_sandwich = pygame.mixer.Sound("assets/Idiot_Sandwich.mp3")
shoot = pygame.mixer.Sound(os.path.join("assets", "Gun+Silencer.mp3"))

# shoot = pygame.mixer.Sound(os.path.join('assets', 'hanghang69.mp3'))

pygame.display.set_caption("Asteroids")
win = pygame.display.set_mode((width, height))

FPS = 60


# Score and Game Over titles fonts
SCORE_FONT = pygame.font.SysFont("commicsans", 40)
SCORE_FONT_ELSE = pygame.font.SysFont("commicsans", 60)
GAME_OVER = pygame.font.SysFont("comicsans", 100)
# asteroids perameters
ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT = 50, 50
ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT = 35, 35
ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT = 20, 20

# Bullet class
class Bullet(object):
    def __init__(self):
        self.point = rocket.head
        self.xAxis, self.yAxis = self.point
        self.widthBullet = 4
        self.heightBullet = 4
        self.cosine = rocket.cosine
        self.sine = rocket.sine
        self.xv = self.cosine * 10
        self.yv = self.sine * 10

    def move(self):
        self.xAxis += self.xv
        self.yAxis -= self.yv

    def draw(self, win):
        pygame.draw.rect(
            win,
            (255, 255, 255),
            [self.xAxis, self.yAxis, self.widthBullet, self.heightBullet],
        )

    def checkOffScreen(self):
        if (
            self.xAxis < -50
            or self.xAxis > width
            or self.yAxis > height
            or self.yAxis < -50
        ):
            return True


rocket = Rocket()
bullets = []
# Define asteroids list for storing newly created asteroids
asteroids = []
speed_delay = 0


def draw(rocket, score, hp, difficulty):
    # Lijst van asteroides wordt meegegeven, waardoorheen geloopt wordt, om ze allemaal te laten bewegen
    win.blit(backGround, (0, 0))
    rocket.draw(win)
    for asteroid in asteroids:
        if asteroid.speed_delay == difficulty:
            asteroid.place_asteroid()
            asteroid.speed_delay = 0
        else:
            asteroid.speed_delay += 1
        if asteroid.check_position():
            asteroids.pop(asteroids.index(asteroid))
            asteroid_manager.asteroids_count = asteroid_manager.asteroids_count - 1
        asteroid.draw_asteroid(win)

    # Draw bullets on screen
    for bullet in bullets:
        bullet.draw(win)

    # Score and game over screens render
    if hp >= 1:
        score_text = SCORE_FONT.render("SCORE: " + str(score), 1, (255, 255, 0))
        hp_text = SCORE_FONT.render("HP: " + str(hp), 1, (255, 255, 0))
        win.blit(score_text, (width - score_text.get_width() - 10, 10))
        win.blit(hp_text, (width - score_text.get_width() - 100, 10))
    elif hp <= 0:
        score_text = SCORE_FONT_ELSE.render("score: " + str(score), 1, (255, 255, 0))

        win.blit(score_text, (width / 2 - 75, 200))
        game_over_text = GAME_OVER.render("game over", 1, (255, 0, 0))
        win.blit(game_over_text, (width / 2 - 200, 75))
        win.blit(highscore_button, (width / 2 - highscore_width / 2, 400))
        win.blit(retry_button, (width / 2 - retry_width / 2, 300))
        win.blit(close_button, (width / 2 - close_width / 2, 500))
        # idiot_sandwich.play()

        # interactive buttons
        win.blit(score_text, (width / 2 - 75, 200))
        game_over_text = GAME_OVER.render("game over", 1, (255, 0, 0))
        win.blit(game_over_text, (width / 2 - 200, 75))
        win.blit(highscore_button, (width / 2 - highscore_width / 2, 400))
        win.blit(retry_button, (width / 2 - retry_width / 2, 300))
        win.blit(close_button, (width / 2 - close_width / 2, 500))

        mouse = pygame.mouse.get_pos()
        # highscore button darkener cords: 520 to 760 and 400 to 475
        for event in pygame.event.get():

            if (
                520 + highscore_width > mouse[0] > 520
                and 400 + highscore_length > mouse[1] > 400
            ):
                highscore_button.set_alpha(50)  # Makes the highscore button darker
                # print("highscore")
                # So we know it works

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        scores_screen.main()
                        print("highscore pressed")
                        # So we know it works

            else:
                highscore_button.set_alpha(
                    1000
                )  # when mouse not over it goes back to normal

            # retry button darkener cords: 520 to 760 and 300 to 375
            if (
                520 + retry_width > mouse[0] > 520
                and 300 + retry_length > mouse[1] > 300
            ):
                retry_button.set_alpha(50)  # Makes the retry button darker
                # print("retry")
                # So we know it works
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print("retry pressed")
                    # So we know it works

                    asteroid_manager.asteroids_count = 0
                    asteroids.clear()
                    # Resets asteroids
                    playerRocket.set_alpha(1000)
                    main(difficulty)
                    # Makes the rocked visible again

            else:
                retry_button.set_alpha(
                    1000
                )  # when mouse not over it goes back to normal

            # close button darkener cords: 520 to 760 and 500 to 575
            if (
                520 + close_width > mouse[0] > 520
                and 500 + close_length > mouse[1] > 500
            ):
                close_button.set_alpha(50)  # Makes the close button darker
                # print("close")
                # So we know it works
                if event.type == pygame.MOUSEBUTTONDOWN:

                    home_screen.main()
                    print("closed pressed")

            else:
                close_button.set_alpha(
                    1000
                )  # when mouse not over it goes back to normal

    pygame.display.update()


def main(difficulty):
    hp = 3
    score = 0
    count = 0
    clock = pygame.time.Clock()
    run = True
    # Added commented music logic to be turned on on specific occassions :)
    # mixer.music.load(os.path.join('', 'on_on.mp3'))
    # mixer.music.play()
    # mixer.music.set_volume(0.5)

    while run:
        clock.tick(FPS)
        count += 1

        rocket.updateLocation()
        for bullet in bullets:
            bullet.move()
            if bullet.checkOffScreen():
                bullets.pop(bullets.index(bullet))

        # Rocket collision with astroids
        for asteroid in asteroids:
            # Calculate if rocket has same position as astroid
            if (
                asteroid.x >= rocket.xAxis - rocket.widthRocket // 2
                and asteroid.x <= rocket.xAxis + rocket.widthRocket // 2
            ) or (
                asteroid.x + asteroid.w <= rocket.xAxis + rocket.widthRocket // 2
                and asteroid.x + asteroid.w >= rocket.xAxis - rocket.widthRocket // 2
            ):
                if (
                    asteroid.y >= rocket.yAxis - rocket.heightRocket // 2
                    and asteroid.y <= rocket.yAxis + rocket.heightRocket // 2
                ) or (
                    asteroid.y + asteroid.h >= rocket.yAxis - rocket.heightRocket // 2
                    and asteroid.y + asteroid.h
                    <= rocket.yAxis + rocket.heightRocket // 2
                ):
                    # Delete the astroid and rocket
                    asteroids.pop(asteroids.index(asteroid))
                    asteroid_manager.asteroids_count = (
                        asteroid_manager.asteroids_count - 1
                    )
                    hp -= 1
                    # Game over
                    if hp <= 0:
                        jsondatafile = open("mydata.json", "r")
                        highscore_json = jsondatafile
                        for each in highscore_json:
                            if int(each) < score:
                                with open("mydata.json", "w") as file:
                                    json.dump(score, file)

                        rocket.destroyRocket()

            # Bullet collison with astroids
            for bullet in bullets:
                # Calculate if bullet has same position as astroid

                if (
                    (
                        bullet.xAxis >= asteroid.x
                        and bullet.xAxis <= asteroid.x + asteroid.w
                    )
                    or bullet.xAxis + bullet.widthBullet >= asteroid.x
                    and bullet.xAxis + bullet.widthBullet <= asteroid.x + asteroid.w
                ):
                    if (
                        (
                            bullet.yAxis >= asteroid.y
                            and bullet.yAxis <= asteroid.y + asteroid.h
                        )
                        or bullet.yAxis + bullet.heightBullet >= asteroid.y
                        and bullet.yAxis + bullet.heightBullet
                        <= asteroid.y + asteroid.h
                    ):
                        # Delete the bullet
                        bullets.pop(bullets.index(bullet))
                        # Splitting of the asteroid in case of size large or medium
                        if asteroid.asteroid_size == "l":
                            asteroids.extend(
                                asteroid_manager.split_l_asteroid(
                                    asteroid.x, asteroid.y
                                )
                            )
                        elif asteroid.asteroid_size == "m":
                            asteroids.extend(
                                asteroid_manager.split_m_asteroid(
                                    asteroid.x, asteroid.y
                                )
                            )
                        # Delete the astroid
                        asteroids.pop(asteroids.index(asteroid))
                        asteroid_manager.asteroids_count = (
                            asteroid_manager.asteroids_count - 1
                        )
                        # Score plus 1
                        score += 1
                        # Add a explosion effect and sound effect
                        explosion_sound.play()

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            rocket.moveForward()
        if keys[pygame.K_RIGHT]:
            rocket.turnRight()
        if keys[pygame.K_LEFT]:
            rocket.turnLeft()

        rocket.autoMove()

        # Quiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Shooting
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if hp >= 1:
                        shoot.play()
                        bullets.append(Bullet())

        # Astroids spawning
        if asteroid_manager.asteroids_count <= 15:
            asteroids.append(asteroid_manager.create_asteroid())

        draw(rocket, score, hp, difficulty)


if __name__ == "__main__":
    pygame.init()
    # Set window width and height based on pre-defined environment width and heights, that can be changed
    win = pygame.display.set_mode(
        (environment.environment_width, environment.environment_height)
    )

    # main()
