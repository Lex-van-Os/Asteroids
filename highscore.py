import pygame, os 

pygame.init()

#create display window
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hihgscore Screen!")

#adding a background image
background_img = pygame.image.load(os.path.join('game-programming-challenge-medium-rare-chicken/assets/', 'space_solar.png')).convert()
background_img = pygame.transform.scale(background_img(width, height), size)

#using an iterator for looping background
i = 0

#game loop
def main():
    running = True
    while running:
        window.fill((0, 0, 0))
        window.blit(background_img,(i, 0))
        window.blit(background_img, (width+i,0))
        if (i ==-width):
            window.blit(bg_img, (width+i,0))
            i=0
        i-=1
        #event handler
        for event in pygame.event.get():
            #quit game
            if event.type == QUIT:
                running = False
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()




















"""
#drawing text in Pygame
font_name = pygame.font.match_font('arial')
def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)



# Initialize 
pygame.init() # not needed for a screen
# Screen name and size
screen = 1280, 720
pygame.display.set_caption("Highscore Screen :)")

# Highscore screen
screen = pygame.display.set_mode((1280, 720))

# Background image
bg_img = pygame.image.load(os.path.join("assets/highscore_background.png"), pygame.transform.scale(bg_img(1280, 720))
#background = pygame.transform.scale(background, (1280, 720))

():
    # Game Loop "running process of the game"
    running = True
    while running:
    
        # RGB = red, green, blue
        #screen.fill((0, 0, 0))
        # Background
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()"""