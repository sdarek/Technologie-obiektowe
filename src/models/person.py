# person.py

import numpy as np

class Person:
    def __init__(self, position, speed, immune=False):
        self.position = position
        self.speed = speed
        self.infected = False
        self.symptomatic = False
        self.immune = immune
        self.infection_duration = 0

    def move(self, n, m):
        # Implementacja ruchu osobnika
        angle = np.random.uniform(0, 2 * np.pi)
        step = np.random.uniform(0, min(self.speed, min(n, m)) / 25)
        self.position.x += step * np.cos(angle)
        self.position.y += step * np.sin(angle)

        # Sprawdź, czy osobnik opuszcza obszar (tylko dla tych na brzegu)
        if (
                self.position.x <= 0 or self.position.x >= n or
                self.position.y <= 0 or self.position.y >= m
        ):
            if np.random.rand() < 0.5:
                # Zawróć do wewnątrz obszaru
                    self.position.x -= step * np.cos(angle)
                    self.position.y -= step * np.sin(angle)
            else:
                return False
        return True

    def infect(self):
        # Implementacja zakażania osobnika
        self.infected = True
        # Symptomy występują z pewnym prawdopodobieństwem
        self.symptomatic = np.random.rand() < 0.5

    def update_health(self, duration, steps_per_second):
        # Aktualizacja stanu zdrowia
        if self.infected:
            self.infection_duration += duration
            if self.infection_duration >= np.random.randint(20 * steps_per_second, 31 * steps_per_second):
                # Symulacja zdrowienia po 20-30 sekundach
                self.infected = False
                self.symptomatic = False
                self.immune = True
                self.infection_duration = 0

