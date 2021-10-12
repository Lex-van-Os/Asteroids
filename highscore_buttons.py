import pygame, os

#create display window
width, height = 1280, 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Button')

#load button images
score_img = pygame.image.load(os.path.join('assets/score_btn.png')).convert() #convert to the same pixel format 
exit_img = pygame.image.load(os.path.join('assets/exit_btn.png')).convert() #as the one you use for the final display

#button class
class Button(): #Why is Button underlined? 
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

        def draw_Button(self):
            action = False
            #get mouse position
            pos = pygame.mouse.get_pos()
            #check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            #draw button on screen
            screen.blit(self.image, (self.rect.x, self.rect.y))

            return action

#create button instances
score_button = Button(100, 200, score_img, 0.8)
exit_button = Button(450, 200, exit_img, 0.8)

#game loop
run = True
while run:

    screen.fill((255, 255, 255))

    if score_button.draw(): #'Button' object has no attribute 'draw'...
        print('SCORE')
    if exit_button.draw():
        print('EXIT')
    
    #event handler
    for event in pygame.event.get():
    #quit game
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()