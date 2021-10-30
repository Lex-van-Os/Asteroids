import math
import pygame

width, height = 1280, 720
win = pygame.display.set_mode((width,height))

# Rocket image
playerRocket = pygame.image.load('assets/spaceship_yellow.png')
playerRocket = pygame.transform.scale(playerRocket, (40,70))

SPEED = 4

# Player class
class Rocket(object):
    # Set the variables
    def __init__(self):
        self.img = playerRocket
        self.widthRocket = self.img.get_width()
        self.heightRocket = self.img.get_height()
        self.xAxis = width//2
        self.yAxis = height//2
        self.angle = 0
        self.rotation = pygame.transform.rotate(self.img, self.angle) # Rotate the rocket
        self.rotationRect = self.rotation.get_rect()
        self.rotationRect.center = (self.xAxis, self.yAxis) # Set the rocket to the center of the screen
        # Calculate with direction the rocket is facing
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.xAxis + self.cosine * self.widthRocket//2, self.yAxis - self.sine * self.heightRocket//2)

    # Draw the rocket on screen
    def draw(self, win):
        win.blit(self.rotation, self.rotationRect)

    # Calculate the rotation of the rocket
    def calculateRotation(self):
        self.rotation = pygame.transform.rotate(self.img, self.angle) # Rotate the rocket
        self.rotationRect = self.rotation.get_rect()
        self.rotationRect.center = (self.xAxis, self.yAxis) # Set the rocket to the center of the screen
        # Calculate with direction the rocket is facing
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.xAxis + self.cosine * self.widthRocket//2, self.yAxis - self.sine * self.heightRocket//2)

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
        self.xAxis += self.cosine * SPEED
        self.yAxis -= self.sine * SPEED
        Rocket.calculateRotation(self)

    # Auto move the rocket to the direction he is facing
    def autoMove(self):
        self.xAxis += self.cosine * 1
        self.yAxis -= self.sine * 1
        Rocket.calculateRotation(self)

    # Track the location of the player / not offscreen
    def updateLocation(self):
        if self.xAxis > width + 50:
            self.xAxis = 0
        elif self.xAxis < 0 - self.widthRocket:
            self.xAxis = width
        elif self.yAxis < -50:
            self.yAxis = height
        elif self.yAxis > height + 50:
            self.yAxis = 0

    def destroyRocket(self):
        playerRocket.set_alpha(0)

    
    def reset_position(self):
        self.xAxis = width//2
        self.yAxis = height//2