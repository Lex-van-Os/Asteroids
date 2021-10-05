import math
import pygame

width, height = 700, 600

playerRocket = pygame.image.load('sprites/New_Piskel_1.png')
playerRocket = pygame.transform.scale(playerRocket, (60,60))

# Player class
class Rocket(object):
    
    def __init__(self):
        self.img = playerRocket
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = width//2
        self.y = height//2
        self.angle = 0
        self.rotation = pygame.transform.rotate(self.img, self.angle) # Rotate the rocket
        self.rotationRect = self.rotation.get_rect()
        self.rotationRect.center = (self.x, self.y) # Set the rocket to the center of the screen
        # Calculate with direction the rocket is facing
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    def draw(self, win):
        win.blit(self.rotation, self.rotationRect)

    def turnLeft(self):
        self.angle += 5
        self.rotation = pygame.transform.rotate(self.img, self.angle) # Rotate the rocket
        self.rotationRect = self.rotation.get_rect()
        self.rotationRect.center = (self.x, self.y) # Set the rocket to the center of the screen
        # Calculate with direction the rocket is facing
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    def turnRight(self):
        self.angle -= 5
        self.rotation = pygame.transform.rotate(self.img, self.angle) # Rotate the rocket
        self.rotationRect = self.rotation.get_rect()
        self.rotationRect.center = (self.x, self.y) # Set the rocket to the center of the screen
        # Calculate with direction the rocket is facing
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotation = pygame.transform.rotate(self.img, self.angle) # Rotate the rocket
        self.rotationRect = self.rotation.get_rect()
        self.rotationRect.center = (self.x, self.y) # Set the rocket to the center of the screen
        # Calculate with direction the rocket is facing
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)