class Environment(): # Environment class, voor het vaststellen en makkelijk kunnen veranderen van scherm waardes

    def __init__(self):
        self.environment_width = 1280
        self.environment_height = 720
        # Idee van asteroid_window_width en height, is dat de asteroides door een gedefineerde height en width moeten komen, zodat ze dichterbij het middelpunt kruisen
        # Wordt nog niet gebruikt
        self.asteroid_window_width = self.environment_width / 100 * 20
        self.asteroid_window_height = self.environment_height / 100 * 20