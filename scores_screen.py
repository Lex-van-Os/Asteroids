import pygame, os
import highscore_buttons

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
# scores = pygame.image.load(os.path.join("assets/scores_btn.png"))
# scores = pygame.transform.scale(scores, (199, 50))
retry = pygame.image.load(os.path.join("assets/retry_btn.png")).convert_alpha()
retry = pygame.transform.scale(retry, (199, 60))
back = pygame.image.load(os.path.join("assets/back_btn.png"))
back = pygame.transform.scale(back, (199, 60))

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
# scores_button = Button(window.get_width() / 1.35, scores.get_height() / 0.20, scores)
retry_button = Button(window.get_width() / 1.35, retry.get_rect().height / 0.13, retry)
back_button = Button(window.get_width() / 1.35, back.get_rect().height / 0.11, back)


# game loop
def main():
    running = True

    while running:
        # drawing images on screen
        window.blit(background, (0, 0))

        # set buttons
        # if scores_button.draw():
        #     print("scores clicked")
        if retry_button.draw():
            print("retry clicked")
        if back_button.draw():
            print("quit clicked")
        # event handler
        for event in pygame.event.get():
            # quit game
            pygame.display.update()
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()

# game variables, goes outside of the game loop
# additional check, does the score.txt file exists?
# if os.path.exists('scores.txt', 'r') as file:
#     # load in the file
#     with open('scores.txt', 'r') as file:
#         high_score = int(file.read())

# # update highscore when 'game_over == True'
# if score > high_score:
#     high_score = score
#     with open('score.txt', 'w') as file:
#         file.write(str(highscore))
