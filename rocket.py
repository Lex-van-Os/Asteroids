import math
import pygame

width, height = 1280, 720
win = pygame.display.set_mode((width,height))

# Rocket image
playerRocket = pygame.image.load('assets/rocket.png')
playerRocket = pygame.transform.scale(playerRocket, (60,60))

SPEED = 4

# Player class
class Rocket(object):
    # Set the variables
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

    # Draw the rocket on screen
    def draw(self, win):
        win.blit(self.rotation, self.rotationRect)

    # Calculate the rotation of the rocket
    def calculateRotation(self):
        self.rotation = pygame.transform.rotate(self.img, self.angle) # Rotate the rocket
        self.rotationRect = self.rotation.get_rect()
        self.rotationRect.center = (self.x, self.y) # Set the rocket to the center of the screen
        # Calculate with direction the rocket is facing
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    # Rotate the rocket to the left
    def turnLeft(self):
        self.angle += 5
        Rocket.calculateRotation(self)

    # Rotate the rocket to the Right
    def turnRight(self):
        self.angle -= 5
        Rocket.calculateRotation(self)

    # Move the rocket to the direction he is facing
    def moveForward(self):
        self.x += self.cosine * SPEED
        self.y -= self.sine * SPEED
        Rocket.calculateRotation(self)

    # Auto move the rocket to the direction he is facing
    def autoMove(self):
        self.x += self.cosine * 1
        self.y -= self.sine * 1
        Rocket.calculateRotation(self)

    def updateLocation(self):
        if self.x > width + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = width
        elif self.y < -50:
            self.y = height
        elif self.y > height + 50:
            self.y = 0