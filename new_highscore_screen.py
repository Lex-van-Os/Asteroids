import pygame, os

# start game
pygame.init()

# create display window and caption screen
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hihgscore Screen!")

# adding a background image
background = pygame.image.load(os.path.join("assets/new_highscore_bg.png"))
background = pygame.transform.scale(background, (1280, 720))

# load buttons
scores = pygame.image.load(os.path.join("assets/scores_btn.png")).convert_alpha()
scores = pygame.transform.scale(scores, (199, 60))
retry = pygame.image.load(os.path.join("assets/retry_btn.png")).convert_alpha()
retry = pygame.transform.scale(retry, (199, 60))
quit_game = pygame.image.load(os.path.join("assets/quit_btn3.png")).convert_alpha()
quit_game = pygame.transform.scale(quit_game, (199, 60))


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


# create instance of buttons !!!!!
scores_button = Button(
    window.get_width() / 1.25, scores.get_rect().height / 0.13, scores
)
retry_button = Button(window.get_width() / 1.25, retry.get_rect().height / 0.11, retry)
quit_button = Button(
    window.get_width() / 1.25, quit_game.get_rect().height / 0.095, quit_game
)


# game loop
def main():
    running = True
    while running:
        # drawing images on screen
        window.blit(background, (0, 0))

        # set buttons
        if retry_button.draw():
            print("retry clicked")
        if scores_button.draw():
            print("scores clicked")
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
