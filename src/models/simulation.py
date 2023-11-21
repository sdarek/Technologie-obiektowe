# simulation.py

import pygame
import numpy as np
from vector import Vector2D
from person import Person
from population import Population

class Simulation:
    def __init__(self, n, m, max_speed, entry_frequency, prob_infection, initial_population, steps_per_second):
        self.n = n
        self.m = m
        self.max_speed = max_speed
        self.prob_turn_back = 0.5
        self.prob_leave_area = 0.5
        self.entry_frequency = entry_frequency
        self.prob_infection = prob_infection
        self.steps_per_second = steps_per_second

        self.population = Population(initial_population, entry_frequency, prob_infection, initial_immunity=0)

    def run(self, num_steps):
        pygame.init()

        screen_size = (800, 600)
        screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Infection Simulation")

        clock = pygame.time.Clock()

        running = True
        for step in range(num_steps):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            duration = 1 / self.steps_per_second  # Czas trwania jednego kroku symulacji

            self.population.move_people(self.n, self.m)
            self.population.introduce_new_people(self.prob_infection, duration)
            self.population.update_infections(duration, self.steps_per_second)

            # Wizualizacja ruchu osobników za pomocą Pygame
            screen.fill((255, 255, 255))  # Biały ekran
            for person in self.population.people:
                color = (255, 0, 0) if person.infected else (0, 0, 255)
                size = 20 if person.symptomatic else 10
                x, y = int(person.position.x / self.n * 800), int(person.position.y / self.m * 600)
                pygame.draw.circle(screen, color, (x, y), size)

            pygame.display.flip()
            clock.tick(self.steps_per_second)

        pygame.quit()

# Przykład użycia:
simulation = Simulation(n=50, m=50, max_speed=2.5, entry_frequency=0.1, prob_infection=0.1, initial_population=10, steps_per_second=100)
simulation.run(num_steps=10000)
