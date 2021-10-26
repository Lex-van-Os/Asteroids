import pygame, os
import highscore_buttons
import game
import json


# start game
pygame.init()

# create display window and caption screen
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Score Screen!")

# adding a background image
background = pygame.image.load(os.path.join("assets/scores_bg.png"))
background = pygame.transform.scale(background, (1280, 720))

# load buttons
update_score = pygame.image.load(os.path.join("assets/update_btn.png")).convert_alpha()
update_score = pygame.transform.scale(update_score, (250, 80))
retry = pygame.image.load(os.path.join("assets/retry_btn.png")).convert_alpha()
retry = pygame.transform.scale(retry, (199, 60))
quit_game = pygame.image.load(os.path.join("assets/quit_btn3.png"))
quit_game = pygame.transform.scale(quit_game, (199, 60))


def check_for_new_highscore():
    # read the json file
    with open("mydata.json", "r") as jsondatafile:
        highscore_json = jsondatafile.readlines()
        for each in highscore_json:
            print(each)

    return each


# score display
score = check_for_new_highscore()
SCORE_FONT = pygame.font.SysFont("commicsans", 80)
score_text = SCORE_FONT.render("Score: " + str(score), 1, (255, 255, 255))

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
retry_button = Button(window.get_width() / 1.35, retry.get_rect().height / 0.13, retry)
quit_button = Button(
    window.get_width() / 1.35, quit_game.get_rect().height / 0.11, quit_game
)
update_button = Button(
    window.get_width() / 3.15, update_score.get_rect().height / 0.30, update_score
)


def show_score():
    SCORE_FONT = pygame.font.SysFont("commicsans", 120)
    # score_text = SCORE_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    # window.blit(score_text, (width / 2 - score_text.get_width() - 10, 300))


# game loop
def main():
    running = True

    while running:
        # drawing images on screen
        window.blit(background, (0, 0))
        # window.blit(score_text, (0, 0))
        # score_text.set_alpha(0)

        # set buttons
        if retry_button.draw():
            game.main()
            print("retry clicked")
        if show_score():
            score = check_for_new_highscore()
        if update_button.draw():
            print("update clicked")
            score = check_for_new_highscore()
            show_score()
            window.blit(score_text, (width / 2 - score_text.get_width(), 350))
        if quit_button.draw():
            running = False
            print("quit clicked")
        # event handler
        for event in pygame.event.get():
            # quit game
            pygame.display.update()
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
