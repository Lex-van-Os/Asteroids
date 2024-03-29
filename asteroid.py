import pygame, os, random, math
from environment import Environment

class Asteroid(pygame.Rect):

    def __init__(self, size, speed, image, width, height, start_placement, end_placement, pre_defined_x=None, pre_defined_y=None):
        self.asteroid_size = size
        self.asteroid_image = image
        self.asteroid_speed = speed
        self.asteroid_width = width
        self.asteroid_height = height
        self.start_placement = start_placement
        self.end_placement = end_placement
        self.pre_defined_x = pre_defined_x
        self.pre_defined_y = pre_defined_y
        self.speed_delay = 0

        self.angle = 0 # Rotation voor het rotaten, begint bij 0. Wordt nog niet gebruikt ivm nog niet complete functionaliteit
        self.rotation = pygame.transform.rotate(self.asteroid_image, self.angle)
        self.rotationRect = self.rotation.get_rect()
        self.rotationRect.center = (self.x, self.y) # Set the rocket to the center of the screen

        # Definen van start en eind coördinaten voor random inladen
        self.define_starting_coords()
        self.define_target_coords()
        super().__init__(self.x_coords, self.y_coords, width, height)


    # Draw asteroid makes use of speed_delay and speed_delay_count to define the speed of asteroids
    # Asteroids only move when speed_delay_count is 0. Else the count gets incremented and reset based on speed_delay value
    # The higher speed delay, the slower asteroids move
    def place_asteroid(self):
        self.rotate_asteroid()
        self.move_asteroid()

        # pygame.display.update()

    def draw_asteroid(self, win):
        win.blit(self.rotation, self.rotationRect)


    # Defineren van starting coördinaten. Gaat doormiddel van kijken waarvandaan de asteroide komt, om zo de deels vastgestelde coords te bepalen
    def define_starting_coords(self):
        environment = Environment()

        # Liggend aan de positie, moet de x / y aan de zijkant van het scherm zijn. Vandaar 1280, 720 en 0 (Min en max width / height van de bijbehorende x / y)
        # Hiernaast is de tweede as waarde random, tussen de min en max van deze x / y as waarde
        if self.start_placement == 'top':
            self.x_coords = random.randint(0, environment.environment_width)
            self.y_coords = 0
        if self.start_placement == 'bottom':
            self.x_coords = random.randint(0, environment.environment_width)
            self.y_coords = 720
        if self.start_placement == 'left':
            self.x_coords = 0
            self.y_coords = random.randint(0, environment.environment_height)
        if self.start_placement == 'right':
            self.x_coords = 1280
            self.y_coords = random.randint(0, environment.environment_height)
        if self.start_placement == 'none':
            if self.pre_defined_x != None and self.pre_defined_y != None:
                self.x_coords = self.pre_defined_x
                self.y_coords = self.pre_defined_y
            else:
                self.x_coords = 0
                self.y_coords = 0


    # Functie voor het defineren van de target positie. Dit werkt hetzelfde als het defineren van de start coördinaten
    # Het verschil is de random as waarde, wat een kleiner scherm is, met doel dat asteroides dichter naar het middelpunt vliegen
    def define_target_coords(self):
        environment = Environment()

        if self.end_placement == 'top':
            self.target_x = random.randint(0, environment.asteroid_window_width)
            self.target_y = 0
        if self.end_placement == 'bottom':
            self.target_x = random.randint(0, environment.asteroid_window_height)
            self.target_y = 720
        if self.end_placement == 'left':
            self.target_x = 0
            self.target_y = random.randint(0, environment.asteroid_window_width)
        if self.end_placement == 'right':
            self.target_x = 1280
            self.target_y = random.randint(0, environment.asteroid_window_height)


    # Move asteroid roept methodes aan voor veranderen van x en y waardes. Omdat er constant gelijke waardes worden toegevoegd aan de x en y 
    # waardes, is de lineare lijn waarin de asteroides vliegen, altijd gelijk (met random start en eindpunten)
    # TODO: Ervoor zorgen dat de lineare lijn niet altijd even scherp is, door verschillende waardes aan de x / y posities te geven
    def move_asteroid(self):
            self.move_asteroid_x()
            self.move_asteroid_y()


    # Liggend aan waar de asteroide vandaan komt, wordt er de asteroide snelheid toegevoegd of afgetrokken van de x waarde (allebei int)
    def move_asteroid_x(self):
        if self.x_coords > self.target_x:
            self.x -= self.asteroid_speed
        elif self.x_coords < self.target_x:
            self.x += self.asteroid_speed


    # Liggend aan waar de asteroide vandaan komt, wordt er de asteroide snelheid toegevoegd of afgetrokken van de x waarde (allebei int)
    def move_asteroid_y(self):
        if self.y_coords > self.target_y:
            self.y -= self.asteroid_speed
        elif self.y_coords < self.target_y:
            self.y += self.asteroid_speed


    # Functie is Work In Progress, kwam hier niet uit. Image moet niet alleen gedraaid worden, maar ook gedraaid om zijn middelpunt -Lex
    def rotate_asteroid(self):
        self.angle += 5
        self.rotation = pygame.transform.rotate(self.asteroid_image, self.angle)
        self.rotationRect = self.rotation.get_rect()
        self.rotationRect.center = (self.x, self.y)


    def check_position(self):
        environment = Environment()
        # rect = pygame.Rect(self.x_coords, self.y_coords, self.asteroid_width, self.asteroid_height)
        if self.x < -50 or self.x > environment.out_of_bounds_width or self.y > environment.out_of_bounds_height or self.y < -50:
            return True
        else:
            return False