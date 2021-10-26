from asteroid import Asteroid
from random import choice, randrange
import pygame, os

ASTEROID_LARGE_IMG = pygame.image.load(os.path.join('assets/', 'asteroid_large.png'))
ASTEROID_MEDIUM_IMG = pygame.image.load(os.path.join('assets/', 'asteroid_medium.png'))
ASTEROID_SMALL_IMG = pygame.image.load(os.path.join('assets/', 'asteroid_small.png'))
ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT = 35, 35
ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT = 25, 25
ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT = 15, 15
ASTEROID_LARGE = pygame.transform.scale(ASTEROID_LARGE_IMG, (ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT))
ASTEROID_MEDIUM = pygame.transform.scale(ASTEROID_MEDIUM_IMG, (ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT))
ASTEROID_SMALL = pygame.transform.scale(ASTEROID_SMALL_IMG, (ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT))

# Vastgestelde waardes voor de verschillende grootes en de posities waarvan en waarnaar de asteroides vliegen
asteroid_sizes = ['l', 'm', 's']
asteroid_speeds = [1, 2, 3]
asteroid_placements = ['top', 'bottom', 'left', 'right']

class AsteroidManager():
    asteroids_count = 0

    def create_asteroid(self):
        if self.asteroids_count <= 15: # Bepaalt hoeveel asteroides er worden ingeladen
            asteroid_placements = self.define_placements()
            num = randrange(0, 3)
            if num == 0:
                return self.create_l_asteroid(asteroid_placements[0], asteroid_placements[1])
            elif num == 1:
                return self.create_m_asteroid(asteroid_placements[0], asteroid_placements[1])
            elif num == 2:
                return self.create_s_asteroid(asteroid_placements[0], asteroid_placements[1])


    # Deze functie bepaalt welke richting de asteroides vliegen, door een start en eind positie te geven
    # (Het geven van start en eindposities gaat door top, bottom, left, right. Coördinaten worden later vastgesteld in de Asteroid class)
    def define_placements(self):
        placements = []
        placements.append(choice(asteroid_placements))
        while len(placements) == 1: # Start en eind mag niet hetzelfde zijn
            ran_placement = choice(asteroid_placements)
            if ran_placement != placements[0]:
                placements.append(ran_placement)
        return placements


    # Verschillende create functies, aangezien verschillende asteroides verschillende attributen hebben
    
    def create_l_asteroid(self, starting_placement, ending_placement):
        asteroid = Asteroid(asteroid_sizes[0], asteroid_speeds[0], ASTEROID_LARGE, ASTEROID_L_WIDTH, ASTEROID_L_HEIGHT, starting_placement, ending_placement)
        self.asteroids_count = self.asteroids_count + 1
        return asteroid


    def create_m_asteroid(self, starting_placement, ending_placement):
        asteroid = Asteroid(asteroid_sizes[1], asteroid_speeds[1], ASTEROID_MEDIUM, ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT, starting_placement, ending_placement)
        self.asteroids_count = self.asteroids_count + 1
        return asteroid

    
    def create_s_asteroid(self, starting_placement, ending_placement):
        asteroid = Asteroid(asteroid_sizes[2], asteroid_speeds[2], ASTEROID_SMALL, ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT, starting_placement, ending_placement)
        self.asteroids_count = self.asteroids_count + 1
        return asteroid

    def split_l_asteroid(self, parent_asteroid_x, parent_asteroid_y):
        return_asteroids = []
        asteroid_m = Asteroid(asteroid_sizes[1], asteroid_speeds[1], ASTEROID_MEDIUM, ASTEROID_M_WIDTH, ASTEROID_M_HEIGHT, 'none', choice(asteroid_placements), parent_asteroid_x, parent_asteroid_y)
        asteroid_s = Asteroid(asteroid_sizes[2], asteroid_speeds[2], ASTEROID_SMALL, ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT, 'none', choice(asteroid_placements), parent_asteroid_x, parent_asteroid_y)
        self.asteroids_count = self.asteroids_count + 2
        return_asteroids.extend((asteroid_m, asteroid_s))
        return return_asteroids


    def split_m_asteroid(self, parent_asteroid_x, parent_asteroid_y):
        return_asteroids = []
        asteroid_s_1 = Asteroid(asteroid_sizes[2], asteroid_speeds[2], ASTEROID_SMALL, ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT, 'none', choice(asteroid_placements), parent_asteroid_x, parent_asteroid_y)
        asteroid_s_2 = Asteroid(asteroid_sizes[2], asteroid_speeds[2], ASTEROID_SMALL, ASTEROID_S_WIDTH, ASTEROID_S_HEIGHT, 'none', choice(asteroid_placements), parent_asteroid_x, parent_asteroid_y)
        self.asteroids_count = self.asteroids_count + 2
        return_asteroids.extend((asteroid_s_1, asteroid_s_2))
        return return_asteroids
