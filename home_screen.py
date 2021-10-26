import pygame as pygame
import os
import webbrowser
from pygame import mixer
import time
import subprocess
import game

# Start game en icon aanmaken voor de applicatie plus een caption
pygame.init()
pygame.display.set_caption("Asteroids :)")
icon = pygame.image.load(os.path.join("assets", "spaceship_red.png"))
pygame.display.set_icon(icon)

# Maak scherm aan voor de game
screen = pygame.display.set_mode((1280, 720))

# Background aanmaken voor game
background = pygame.image.load(os.path.join("assets", "background.png"))
background = pygame.transform.scale(background, (1280, 720))

# Titel van de game
titel = pygame.image.load(os.path.join("assets", "Guardian.png"))
titel = pygame.transform.scale(titel, (400, 280))

# titel positioneren
titel_rect = titel.get_rect()
titel_rect.center = (screen.get_width() / 2, titel_rect.height / 2.65)
titel.get_width()

# load buttons
start = pygame.image.load(os.path.join("assets", "start_game.png")).convert_alpha()
start = pygame.transform.scale(start, (199, 50))
highscore = pygame.image.load(os.path.join("assets", "high_score.png")).convert_alpha()
highscore = pygame.transform.scale(highscore, (199, 50))
stop_game = pygame.image.load(os.path.join("assets", "quit_game.png")).convert_alpha()
stop_game = pygame.transform.scale(stop_game, (199, 50))
easy_mode = pygame.image.load(os.path.join("assets", "easy_mode.png")).convert_alpha()
easy_mode = pygame.transform.scale(easy_mode, (199, 50))
normal_mode = pygame.image.load(
    os.path.join("assets", "normal_mode.png")
).convert_alpha()
normal_mode = pygame.transform.scale(normal_mode, (199, 50))
hard_mode = pygame.image.load(os.path.join("assets", "hard_mode.png")).convert_alpha()
hard_mode = pygame.transform.scale(hard_mode, (199, 50))

# Linkedin pages
# Nilesh Linkedin
nilesh_linkedin_page = pygame.image.load(
    os.path.join("assets", "nilesh_button.png")
).convert_alpha()
nilesh_linkedin_page = pygame.transform.scale(nilesh_linkedin_page, (199, 50))

# Lex Linkedin
lex_linkedin_page = pygame.image.load(
    os.path.join("assets", "lex_button.png")
).convert_alpha()
lex_linkedin_page = pygame.transform.scale(lex_linkedin_page, (199, 50))

# Babs Linkedin
babs_linkedin_page = pygame.image.load(
    os.path.join("assets", "babs_button.png")
).convert_alpha()
babs_linkedin_page = pygame.transform.scale(babs_linkedin_page, (199, 50))

# Chris linkedin
chris_linkedin_page = pygame.image.load(
    os.path.join("assets", "chris_button.png")
).convert_alpha()
chris_linkedin_page = pygame.transform.scale(chris_linkedin_page, (199, 50))

# Quylian linkedin
qulian_linkedin_page = pygame.image.load(
    os.path.join("assets", "quylian_button.png")
).convert_alpha()
qulian_linkedin_page = pygame.transform.scale(qulian_linkedin_page, (199, 50))

# Button class so we can create buttons very easy and quickly
class Button:
    def __init__(self, x, y, image):

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        # get mouse position
        positie = pygame.mouse.get_pos()

        # check mouse position and condition for click
        if self.rect.collidepoint(positie):
            # Remove mouse position to negative for so mouse can take position again
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                # With this we can click on the buttons again
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw buttons
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


# Nilesh meme image loading
nilesh = pygame.image.load(os.path.join("assets", "nilesh.jpg"))
nilesh = pygame.transform.scale(nilesh, (200, 150))
nilesh_rect = nilesh.get_rect()
nilesh_rect.center = (screen.get_width() / 6, nilesh_rect.height / 0.3)

# Doge meme image loading
doge = pygame.image.load(os.path.join("assets", "dogedexstrong-1.png"))
doge = pygame.transform.scale(doge, (200, 160))
doge_rect = doge.get_rect()
doge_rect.center = (screen.get_width() / 1.2, doge_rect.height / 0.28)

# Gordon ramsey meme image loading
gordon = pygame.image.load(os.path.join("assets", "gordon.jpg"))
gordon = pygame.transform.scale(gordon, (200, 150))
gordon_rect = gordon.get_rect()
gordon_rect.center = (screen.get_width() / 1.2, gordon_rect.height / 0.5)

# create instance of buttons
start_button = Button(screen.get_width() / 2.35, start.get_rect().height / 0.20, start)
highscore_button = Button(
    screen.get_width() / 2.35, highscore.get_rect().height / 0.15, highscore
)
quit_button = Button(
    screen.get_width() / 2.35, start.get_rect().height / 0.12, stop_game
)
easy_button = Button(
    screen.get_width() / 2.35, start.get_rect().height / 0.10, easy_mode
)
normal_button = Button(
    screen.get_width() / 2.9, start.get_rect().height / 0.09, normal_mode
)
hard_button = Button(
    screen.get_width() / 1.98, start.get_rect().height / 0.09, hard_mode
)

# Linkedin Buttons
Nileshlink_button = Button(
    screen.get_width() / 25, start.get_rect().height / 1.8, nilesh_linkedin_page
)
lexLink_button = Button(
    screen.get_width() / 25, start.get_rect().height / 0.55, lex_linkedin_page
)
babsLink_button = Button(
    screen.get_width() / 25, start.get_rect().height / 0.325, babs_linkedin_page
)
chrisLink_button = Button(
    screen.get_width() / 25, start.get_rect().height / 0.23, chris_linkedin_page
)
qulianLink = Button(
    screen.get_width() / 25, start.get_rect().height / 0.178, qulian_linkedin_page
)
# Create Background sound
pygame.mixer.init()
# pygame.mixer.music.load(os.path.join("assets", "masterchief.mp3"))
# pygame.mixer.music.play()


def main():
    # game loop "running proces van de game"
    running = True

    while running:

        # Background, titel, nilesh, doge, gordon putting them in the screen...
        screen.blit(background, (0, 0))
        screen.blit(titel, titel_rect)
        screen.blit(nilesh, nilesh_rect)
        screen.blit(doge, doge_rect)
        screen.blit(gordon, gordon_rect)

        # Buttons for the images and also performing some actions
        if Nileshlink_button.draw():
            webbrowser.open("https://www.linkedin.com/in/nilesh-d-502035177/")
        if lexLink_button.draw():
            webbrowser.open("https://www.linkedin.com/in/lex-van-os-a2b012198/")
        if babsLink_button.draw():
            webbrowser.open("https://www.linkedin.com/in/babette-van-aubel-b35386190/")
        if chrisLink_button.draw():
            webbrowser.open("https://www.linkedin.com/in/chris-gerritsen-5b252217b/")
        if qulianLink.draw():
            print("testqulian")
        if start_button.draw():
            print("start clicked")
            game.main()
        if highscore_button.draw():
            print("high score clicked")
        if quit_button.draw():
            running = False
            print("quit clicked")
            os.startfile(os.path.join("assets", "Tyeffect4k.mp4"))
            time.sleep(5.8)
            subprocess.call("taskkill /f /im Video.UI.exe", shell=True)
        if easy_button.draw():
            easy_mode.set_alpha(50)
            normal_mode.set_alpha(1000)
            hard_mode.set_alpha(1000)
            print("verander difficulty naar 1")

        if normal_button.draw():
            easy_mode.set_alpha(1000)
            normal_mode.set_alpha(50)
            hard_mode.set_alpha(1000)
            print("testnormal")

        if hard_button.draw():
            easy_mode.set_alpha(1000)
            normal_mode.set_alpha(1000)
            hard_mode.set_alpha(50)
            print("testhard")

        for event in pygame.event.get():
            #
            pygame.display.update()

            if event.type == pygame.QUIT:

                running = False


if __name__ == "__main__":

    main()
