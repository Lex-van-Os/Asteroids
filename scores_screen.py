import pygame, os
import game
import json
import home_screen

# start game
pygame.init()

# create display window and caption screen
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Score Screen!")

# adding a background image
background = pygame.image.load(os.path.join("assets/background.png"))
background = pygame.transform.scale(background, (1280, 720))

# title game
title = pygame.image.load(os.path.join("assets", "title_scores.png"))
title = pygame.transform.scale(title, (400, 280))

# title position
title_rect = title.get_rect()
title_rect.center = (window.get_width() / 2, title_rect.height / 2.65)
title.get_width()

# load buttons
retry = pygame.image.load(os.path.join("assets/retry_btn.png")).convert_alpha()
retry = pygame.transform.scale(retry, (210, 60))
quit_game = pygame.image.load(os.path.join("assets/quit_btn.png"))
quit_game = pygame.transform.scale(quit_game, (210, 60))

# button class
class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            # remove mouse position, when negative load position again
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        # now we can click on the buttons as many times as we want
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

            # draw button on screen
        window.blit(self.image, (self.rect.x, self.rect.y))
        return action


# create instance of buttons
retry_button = Button(window.get_width() / 2.35, retry.get_rect().height / 0.13, retry)
quit_button = Button(
    window.get_width() / 2.35, quit_game.get_rect().height / 0.11, quit_game
)

# game loop
def main():
    running = True

    while running:
        # drawing images on screen
        window.blit(background, (0, 0))
        window.blit(title, title_rect)
        # with the open statement, load the updata json file
        with open("mydata.json") as json_file:
            data = json.load(json_file)
            # positioning score text
            SCORE_FONT = pygame.font.SysFont("commicsans", 80)
            score_text = SCORE_FONT.render(
                "Your New Score: " + str(data), 1, (255, 255, 255)
            )
            # display score text
            window.blit(score_text, (width - score_text.get_width() - 350, 300))

        # set buttons
        if retry_button.draw():
            game.main(difficulty=1)
        if quit_button.draw():
            home_screen.main()
        # event handler
        for event in pygame.event.get():
            # quit game
            pygame.display.update()
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
