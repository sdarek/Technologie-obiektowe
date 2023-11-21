# population.py

import numpy as np
from person import Person
from vector import Vector2D

class Population:
    def __init__(self, size, entry_frequency, prob_infection, initial_immunity):
        self.size = size
        self.people = [Person(Vector2D(np.random.uniform(0, 50), np.random.uniform(0, 50)),
                              np.random.uniform(0, 2.5))
                       for _ in range(size)]
        self.entry_frequency = entry_frequency
        self.prob_infection = prob_infection
        self.initial_immunity = initial_immunity

    def move_people(self, n, m):
        for person in self.people:
            if not person.move(n, m):
                self.remove_person(person)

    def introduce_new_people(self, prob_infection, duration):
        # Decyduj, czy nowy osobnik wchodzi do populacji
        if np.random.rand() < self.entry_frequency:
            new_person = Person(Vector2D(np.random.uniform(0, 50), np.random.uniform(0, 50)),
                               np.random.uniform(0, 2.5), immune=np.random.rand() < self.initial_immunity)
            # Losowe zakażenie nowego osobnika
            if np.random.rand() < prob_infection:
                new_person.infect()
            self.people.append(new_person)

    def remove_person(self, person):
        self.people.remove(person)

    def update_infections(self, duration, steps_per_second):
        for person in self.people:
            # Sprawdź, czy zakażony osobnik zaraża innych w zasięgu
            if person.infected:
                for other_person in self.people:
                    if other_person != person and not other_person.infected and not other_person.immune:
                        distance_vector = Vector2D(person.position.x - other_person.position.x,
                                                   person.position.y - other_person.position.y)
                        distance = distance_vector.abs()
                        # Warunki zakażenia: odległość, czas utrzymania odległości i zdrowie osoby
                        if distance < 2 and np.random.rand() < 0.5 and np.random.uniform(0, 3) < 1:
                            if person.symptomatic:
                                other_person.infected = True
                                other_person.symptomatic = np.random.rand() < 0.5
                                other_person.update_health(duration, steps_per_second)
                            else:
                                other_person.infected = np.random.rand() < 0.1
                                other_person.symptomatic = np.random.rand() < 0.5
                                other_person.update_health(duration, steps_per_second)
