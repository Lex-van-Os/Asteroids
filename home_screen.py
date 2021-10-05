import pygame as pygame
import os

# Start game en icon aanmaken voor de applicatie plus een caption
pygame.init()
pygame.display.set_caption("Asteroids :)")
icon = pygame.image.load(os.path.join("assets", "spaceship_red.png"))
pygame.display.set_icon(icon)

# Maak scherm aan voor de game
screen = pygame.display.set_mode((1280, 720))

# Background aanmaken voor game
background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, (1280, 720))

# Titel van de game
titel = pygame.image.load("assets/Guardian.png")
titel = pygame.transform.scale(titel, (400, 280))

# titel positioneren
titel_rect = titel.get_rect()
titel_rect.center = (screen.get_width() / 2, titel_rect.height / 2.65)
titel.get_width()

# Start (MENU)
menu = pygame.image.load("assets/start_game.png")
menu = pygame.transform.scale(menu, (199, 50))

# Start positioneren
menu_rect = menu.get_rect()
menu_rect.center = (screen.get_width() / 2, menu_rect.height / 0.18)
menu.get_width()

# highscore (MENU)
highscore = pygame.image.load("assets/high_score.png")
highscore = pygame.transform.scale(highscore, (199, 50))

# highscore positioneren
highscore_rect = highscore.get_rect()
highscore_rect.center = (screen.get_width() / 2, highscore_rect.height / 0.14)
highscore.get_width()


def main():
    # game loop "running proces van de game"
    running = True
    while running:

        # RGB = red, green, blue
        # screen.fill((0, 0, 0))

        # Background
        screen.blit(background, (0, 0))
        screen.blit(titel, titel_rect)
        screen.blit(menu, menu_rect)
        screen.blit(highscore, highscore_rect)

        for event in pygame.event.get():
            screen.blit(menu, menu_rect)
            screen.blit(menu, menu_rect)
            pygame.display.update()
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
