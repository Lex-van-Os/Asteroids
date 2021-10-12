import pygame
from rocket import Rocket
from asteroid import asteroid
from omgeving import highscore_button
from omgeving import retry_button
from omgeving import close_button
from omgeving import highscore_width
from omgeving import highscore_length
from omgeving import retry_width
from omgeving import retry_length
from omgeving import close_width 
from omgeving import close_length


pygame.font.init()
pygame.init()

width, height = 1280, 720

backGround = pygame.image.load('assets/background.png')
backGround = pygame.transform.scale(backGround, (1280, 720))

pygame.display.set_caption("asteroids")

FPS = 60

SCORE_FONT = pygame.font.SysFont('commicsans', 40)
SCORE_FONT_ELSE = pygame.font.SysFont('commicsans', 60)
GAME_OVER = pygame.font.SysFont("comicsans" , 100)

ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT = 50, 50
ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT = 35, 35
ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT = 20, 20

# Asteroid rectangles
asteroid_l = pygame.Rect(0, 200, ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT)
asteroid_m = pygame.Rect(900, 400, ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT)
asteroid_s = pygame.Rect(300, 0, ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT)

def draw(rocket, score):
    win.blit(backGround, (0,0))
    rocket.draw(win)
    asteroid.draw_window(asteroid_l, asteroid_m, asteroid_s, win)
    
    if hp >= 1:
        score_text = SCORE_FONT.render("score: " + str(score), 1, (255, 255, 0))
        win.blit(score_text, (width  - score_text.get_width() - 10, 10))
      
    else:
        score_text = SCORE_FONT_ELSE.render("score: " + str(score), 1, (255, 255, 0))
        win.blit(score_text, (width / 2 - 75 , 150))
        game_over_text = GAME_OVER.render("game over", 1, (255, 0 , 0))
        win.blit(game_over_text, (width / 2 - 150 , 75))
        win.blit(highscore_button, ( width / 2 - highscore_width / 2 , 400))
        win.blit(retry_button, ( width / 2 - retry_width / 2 , 300))
        win.blit(close_button, ( width / 2 - close_width / 2 , 500))
    
    
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(click)
        #print(mouse) 
        #highscore button trigger cords: 520 to 760 and 400 to 475
        if 520 + highscore_width > mouse[0] > 520 and 400 + highscore_length > mouse[1] >400:
            highscore_button.set_alpha(50)
            print("highscore")
            
        else:
            highscore_button.set_alpha(1000)
        
        #retry button trigger cords: 520 to 760 and 300 to 375
        if 520 + retry_width > mouse[0] > 520 and 300 + retry_length > mouse[1] > 300:
            retry_button.set_alpha(50)
            print("retry")
        else:
            retry_button.set_alpha(1000)
        
        #close button trigger cords: 520 to 760 and 500 to 575
        if 520 + close_width > mouse[0] > 520 and 500 + close_length > mouse[1] > 500:
            close_button.set_alpha(50)
            print("close")
        else:
            close_button.set_alpha(1000)
    pygame.display.update()


score = 5
hp = 3

def main():
    rocket = Rocket()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            rocket.moveForward()
        if keys[pygame.K_RIGHT]:
            rocket.turnRight()
        if keys[pygame.K_LEFT]:
            rocket.turnLeft()

        asteroid_l.x += 1
        asteroid_m.x -= 1
        asteroid_s.y += 1
        rocket.autoMove()

        draw(rocket, score)

if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((width,height))

    main()